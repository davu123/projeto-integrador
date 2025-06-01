document.addEventListener("DOMContentLoaded", function () {
  const forms = document.querySelectorAll("form");

  forms.forEach((form) => {
      form.addEventListener("submit", function (event) {
          const inputs = form.querySelectorAll("input[required]");
          let valid = true;

          inputs.forEach((input) => {
              if (!input.value.trim()) {
                  input.classList.add("erro");
                  valid = false;
              } else {
                  input.classList.remove("erro");
              }
          });

          if (!valid) {
              event.preventDefault();
              alert("Por favor, preencha todos os campos obrigatórios.");
          }
      });
  });
});
