$("form[name=signup_form").submit(function (e) {
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();
  console.log("jjjjj", data);

  $.ajax({
    url: "/user/signup",
    method: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      window.location.href = "/";
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    },
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function (e) {
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      window.location.href = "/index/";
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    },
  });

  e.preventDefault();
});
