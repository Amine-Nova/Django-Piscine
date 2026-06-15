const room_name = document.getElementById("room_name").textContent;
const user = document.getElementById("username").textContent.trim();

function append_users(connected, room) {
  let html = '';
  for (const con of connected) {
    html += `<div class="d-flex align-items-center gap-2 p-1">
          <span class="bg-success rounded-circle" style="width: 8px; height: 8px;"></span>
          <span>${con}</span>
        </div>`
  }
  $("#connected").html(html)
}

function cookiesVal(key) {
  var cookies = document.cookie;
  cookies = cookies
    .split("; ")
    .find((row) => row.startsWith(key))
    ?.split("=")[1];
  return cookies;
}

$(document).ready(function () {
  const socket = new WebSocket(
    "ws://127.0.0.1:8000/ws/message/" + room_name + "/",
  );
  socket.onopen = function (e) {
    $("#messages").scrollTop($("#messages")[0].scrollHeight);
    console.log("Connection Established!");
  };
  socket.onmessage = function (event) {
    const data = JSON.parse(event.data);

    if (data.type == "connected") {
      $("#messages").append(`<div class="d-flex justify-content-center mb-3">
                          <p class="mb-0 text-success">${data.user} has joined the chat!</p>
                        </div>
                      `);
      append_users(data.active, data.room)
      console.log(data);
      
    } else if (data.type == "disconnected") {
      $("#messages").append(`<div class="d-flex justify-content-center mb-3">
                          <p class="mb-0 text-danger">${data.user} has left the chat!</p>
                        </div>
                      `);
      append_users(data.active, data.room)

    } else if (data.type == "chat") {
      if (data["user"] === user) {
        $("#messages").append(`<div class="d-flex justify-content-end mb-3">
                                  <div class="bg-info text-white rounded-3 px-3 py-2" style="max-width: 70%;">
                                  <p class="mb-0">${data.message}</p>
                                  <span class="small opacity-75">${data.user}</span>
                                  </div>
                                </div>
                              `);
        $.post(
        "http://127.0.0.1:8000/chat/save",
        {
          text: data.message,
          room: room_name,
          csrfmiddlewaretoken: cookiesVal("csrftoken"),
        },
      );
      } else {
        $("#messages").append(`<div class="d-flex justify-content-start mb-3">
                                  <div class="bg-primary text-white rounded-3 px-3 py-2" style="max-width: 70%;">
                                  <p class="mb-0">${data.message}</p>
                                  <span class="small opacity-75">${data.user}</span>
                                  </div>
                                </div>
                              `);
      }
    }
    $("#messages").scrollTop($("#messages")[0].scrollHeight);
  };

  $("#btn-send").on("click", function () {
    const $input = $("#message-input");
    const message = $input.val().trim();

    if (message != "" && socket.readyState == WebSocket.OPEN) {
      socket.send(message);
      $input.val("");
    }
  });

  socket.onclose = function (event) {
    console.log("CLOSED", socket.readyState);
    console.log(event);
  };
});

$("#message-input").focus();


$("#message-input").on("keydown", function (e) {
  if (e.which === 13 || e.key === "Enter") {
    e.preventDefault();
    $("#btn-send").trigger("click");
  }
});
