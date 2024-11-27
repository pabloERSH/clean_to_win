from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


class WelcomeTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        binary_yandex_driver_file = "D:\\Yandex Driver\\yandexdriver.exe"
        options = webdriver.ChromeOptions()

        service = Service(binary_yandex_driver_file)
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def wait(self):
        return WebDriverWait(self.driver, 20)

    def testHomePage(self):
        # Arrange
        self.driver.get(self.live_server_url)

        # Act
        self.wait().until(EC.presence_of_element_located((By.TAG_NAME, "title")))  # заголовок всей страницы
        # Ожидаем появления элемента <h1>
        h1_element = self.wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title-first")))
        h2_elements = self.wait().until(EC.presence_of_all_elements_located((By.TAG_NAME, "h2")))

        # Получаем текст из всех дочерних элементов <span>
        span_elements = h1_element.find_elements(By.CSS_SELECTOR, "span")
        actual_text_h1 = " ".join([span.text for span in span_elements])

        # Ожидаемый текст
        expected_text_h1 = "CLEAN TO WIN сделаем мир лучше"
        # Проверяем текст каждого элемента <h2>
        expected_texts_h2 = [
            "чем мы занимаемся", "интересные задания", "наши отзывы", "присоединиться к сообществу"
        ]
        # Найти элемент по CSS-селектору
        link = self.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn_animated')

        # Проверить, что ссылка существует и имеет правильный href
        self.assertEqual(link.get_attribute('href'), 'https://web.telegram.org/k/#@clean_to_win_bot')

        # Открыть ссылку в новой вкладке
        link.click()

        # Проверить, что новая вкладка открылась
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Проверить, что новая вкладка открылась с правильным URL
        self.assertEqual(self.driver.current_url, 'https://web.telegram.org/k/#@clean_to_win_bot')

        # Закрыть новую вкладку
        self.driver.close()

        # Вернуться на исходную вкладку
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Проверить, что вернулись на исходную вкладку
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/')



        # Assert
        self.assertIn("Clean to win", self.driver.title)
        # Проверяем, что текст соответствует ожидаемому
        self.assertEqual(actual_text_h1, expected_text_h1)
        for i, h2_element in enumerate(h2_elements):
            self.assertEqual(h2_element.text.strip().lower(), expected_texts_h2[i])

    def testFooterLinks(self):
        self.driver.get(self.live_server_url)

        # Ожидаем появления элемента <ul> с классом footer_list
        footer_list_element = self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, "footer__list")))

        # Находим все ссылки внутри элемента <ul>
        links = footer_list_element.find_elements(By.CLASS_NAME, "footer__link")

        # Ожидаемые заголовки для каждой страницы
        expected_titles = {
            "/about": "о нашем проекте",
            "/feedback": "отзывы наших клиентов",
            "/gallery": "делаем мир лучше",
            "/": "clean to win сделаем мир лучше"
        }

        # Проверяем каждую ссылку
        for i in range(len(links)):
            # Получаем URL ссылки
            link_url = links[i].get_attribute("href")

            # Определяем ожидаемый заголовок для этой страницы
            expected_title_h1 = expected_titles.get(link_url.replace(self.live_server_url, ""))
            # Переходим по ссылке
            self.driver.execute_script("arguments[0].click();", links[i])

            # Ожидаем загрузки новой страницы
            self.wait().until(EC.url_changes(self.live_server_url))

            # Проверяем, что мы находимся на правильной странице по заголовку
            h1_element = self.wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title-first")))
            span_elements = h1_element.find_elements(By.CSS_SELECTOR, "span")
            actual_text_h1 = " ".join([span.text for span in span_elements])

            self.assertEqual(actual_text_h1.strip().lower(), expected_title_h1)
            # Возвращаемся на исходную страницу
            self.driver.get(self.live_server_url)

            # Ожидаем, что исходная страница загрузится
            self.wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title-first")))
            footer_list_element = self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, "footer__list")))

            # Повторно находим все ссылки внутри элемента <ul>
            links = footer_list_element.find_elements(By.CLASS_NAME, "footer__link")

    def testGalleryPage(self):
        # Arrange
        self.driver.get(f"{self.live_server_url}/gallery/")

        # Act
        self.wait().until(EC.presence_of_element_located((By.TAG_NAME, "title")))  # заголовок всей страницы
        # Ожидаем появления элемента <h1>
        h1_element = self.wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title-first")))

        h2_element = self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, "title-secondary")))

        # Получаем текст из всех дочерних элементов <span>
        span_elements = h1_element.find_elements(By.CSS_SELECTOR, "span")

        actual_text_h1 = " ".join([span.text for span in span_elements])

        # Ожидаем появления всех элементов с классом composition
        composition_element = self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, "composition")))

        images = composition_element.find_elements(By.TAG_NAME, "img")
        image_srcs = [img.get_attribute("src") for img in images]

        gallery_section = self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, "section-galary")))

        row_elements = gallery_section.find_elements(By.CLASS_NAME, "row")

        # Ожидаемый текст
        expected_text_h1 = "делаем мир лучше"
        expected_text_h2 = "коллекция наших снимков"

        # Assert
        self.assertIn("Clean to win", self.driver.title)
        # Проверяем, что текст соответствует ожидаемому
        self.assertEqual(actual_text_h1.strip().lower(), expected_text_h1)
        self.assertEqual(h2_element.text.strip().lower(), expected_text_h2)

        self.assertEqual(len(image_srcs), len(set(image_srcs)))
        self.assertTrue(len(row_elements) > 0)

        # Проверяем каждый элемент row
        for row in row_elements:
            # Находим все элементы с классом col-1-of-3 внутри элемента row
            col_elements = row.find_elements(By.CLASS_NAME, "col-1-of-3")
            if len(col_elements) > 0:
                # Проверяем, что внутри каждого row ровно 3 элемента с классом col-1-of-3
                self.assertEqual(len(col_elements), 3)

    def testAboutPage(self):
        # Arrange
        self.driver.get(f"{self.live_server_url}/about/")

        # Act
        self.wait().until(EC.presence_of_element_located((By.TAG_NAME, "title")))  # заголовок всей страницы

        author_section = self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, "section-about_author")))

        card_images = author_section.find_elements(By.CLASS_NAME, "about-card__img")
        card_boxes = author_section.find_elements(By.CLASS_NAME, "about-card__box")

        images = [card_image.find_element(By.TAG_NAME, "img").get_attribute("src") for card_image in card_images]
        roles = [card_box.find_element(By.TAG_NAME, "h3").text.strip().capitalize() for card_box in card_boxes]

        expected_roles = ["Frontend разработчик", "Backend разработчик", "Backend разработчик"]

        # Assert
        self.assertIn("Clean to win", self.driver.title)
        self.assertEqual(len(images), len(set(images)))
        self.assertEqual(roles, expected_roles)


