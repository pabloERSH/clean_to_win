// Существуют разные способы получить DOM-узел; здесь мы определяем саму форму и
// поле ввода email и элемент span, в который поместим сообщение об ошибке
const form = document.getElementsByClassName("form")[0];

const email = document.getElementById("mail");
const emailError = document.querySelector("#mail + span.error");

const name_surname = document.getElementById("name_surname");
const name_surnameError = document.querySelector("#name_surname + span.error");

//const option=document.getElementsByName('cheked');
//const optionError = document.querySelector("#option + span.error");

email.addEventListener("input", function (event) {
  // Каждый раз, когда пользователь что-то вводит,
  // мы проверяем, являются ли поля формы валидными
  if (email.validity.valid) {
    // Если на момент валидации какое-то сообщение об ошибке уже отображается,
    // если поле валидно, удаляем сообщение
    emailError.textContent = ""; // Сбросить содержимое сообщения
    emailError.className = "error"; // Сбросить визуальное состояние сообщения
  } else {
    // Если поле не валидно, показываем правильную ошибку
    showError();
  }
});

name_surname.addEventListener("input", function (event) {
  if (name_surname.validity.valid) {
    name_surnameError.textContent = ""; 
    name_surnameError.className = "error"; 
  } else {
    showError_1();
  }
})

// option.addEventListener("input", function (event) {
//   if (option.validity.valid) {
//     optionError.textContent = ""; 
//     optionError.className = "error"; 
//   } else {
//     showError_2();
//   }
// })

form.addEventListener("submit", function (event) {
  // Если поле email валидно, позволяем форме отправляться

  if (!email.validity.valid) {
    // Если поле email не валидно, отображаем соответствующее сообщение об ошибке
    showError();
    // Затем предотвращаем стандартное событие отправки формы
    event.preventDefault();
  }
  //login
  if (!name_surname.validity.valid) {
    showError_1();
    event.preventDefault();
  }
  //radio
  // if (!option.validity.valid) {
  //   showError_2();
  //   event.preventDefault();
  // }
});





function showError() {
  if (email.validity.valueMissing) {
    // Если поле пустое,
    // отображаем следующее сообщение об ошибке
    emailError.textContent = "Нужно ввести ваш email адрес";
  } else if (email.validity.typeMismatch) {
    // Если поле содержит не email-адрес,
    // отображаем следующее сообщение об ошибке
    emailError.textContent = "Введеное значение должно быть email адресом.";
  } else if (email.validity.tooShort) {
    // Если содержимое слишком короткое,
    // отображаем следующее сообщение об ошибке
    emailError.textContent = `email содержит минимум ${email.minLength} символов; введено ${email.value.length}.`;
  }
  // Задаём соответствующую стилизацию
  emailError.className = "error active";
}

function showError_1() {
  if (name_surname.validity.valueMissing) {
    name_surnameError.textContent = "Нужно ввести имя и фамилию.";
  } else if (name_surname.validity.tooShort) {
    name_surnameError.textContent = `Имя содержит минимум ${name_surname.minLength} символов; введено ${name_surname.value.length}.`;
  } else if(name_surname.validity.patternMismatch) {
    name_surnameError.textContent = "Нужно ввести по образцу 'Алексей Кондратенко', русскими буквами с соблюдением регистра";
  }
  name_surnameError.className = "error active";
}
//radio
function checkForm() {
  let chosenOption = '';
  const len = document.userForm.getElementsByClassName("form__input-radio").length;

  for (i = 0; i < len; i++) {
    if (document.userForm.getElementsByClassName("form__input-radio")[i].checked) {
      chosenOption = document.userForm.getElementsByClassName("form__input-radio")[i].value
    }
  }

  if (chosenOption == '') {

    alert('Вы забыли выбрать тип полета!');
    return false;
  } else {
    console.log(chosenOption)
  }
}