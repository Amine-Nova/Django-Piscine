function cookiesVal(key){
    var cookies = document.cookie
    cookies = cookies.split("; ").find(row => row.startsWith(key))
    ?.split("=")[1];
    return cookies;
}

$(document).on("click", "#login", function () {
  username = $("#id_username").val();
  password = $("#id_password").val();
  $.ajax({
    url: "http://127.0.0.1:8000/login",
    type: "POST",
    data: {
      username: username,
      password: password,
      csrfmiddlewaretoken: cookiesVal("csrftoken"),
    },
    success: function (data) {
      $(".login-error").text("");
      $("body")
        .html(`<div
      class="welcome-heading text-uppercase text-center row"
      style="position: relative"
    >
      <div class="col-12">
        
        <h1 class="mb-4">Hello World</h1>
        <p class="fs-3 text-center welcome-user mt-3">Logged as ${username}</p>
        <button
          id="logout"
          class="btn btn-light m-3 px-4 py-2 fs-5 z-3"
          style="position: absolute; top: 0; right: 0"
        >
          Logout
        </button>
      </div>
    </div>`);
    },
    error: function (xhr) {
      $(".login-error")
        .text("Invalid username or password")
        .removeClass("d-none");
      console.log(xhr.status);
    },
  });
});

$(document).on("click", "#logout", function () {
    console.log();
  $.ajax({
    url: "http://127.0.0.1:8000/logout",
    type: "POST",
    data: {
      csrfmiddlewaretoken: cookiesVal("csrftoken"),
    },
    success: function (xhr) {
        console.log("has succeeded", xhr.status);
        $("body")
        .html(`<div
      class="welcome-heading main d-flex justify-content-center align-items-center min-vh-100"
    >
        <h1 class="">User Logged Out!</h1>
    </div>`);
    },
    error: function (xhr) {
      console.log(xhr.status);
    },
  });
});
