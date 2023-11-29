document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("demo-form2");

  form.addEventListener("submit", function (event) {
      event.preventDefault();

      const formData = new FormData(form);

      $.ajax({
          url: form.action,
          type: form.method,
          data: formData,
          processData: false,
          contentType: false,
          success: function (response) {
              Swal.fire({
                  title: response.title,
                  text: response.message,
                  icon: response.icon,
              }).then(() => {
                  if (response.success && response.redirect_url) {
                      window.location.href = response.redirect_url;
                  } else {
                      window.location.reload();
                  }
              });
          },
          error: function (error) {
              console.error(error);
          },
      });
  });
});
