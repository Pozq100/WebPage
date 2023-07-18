function requestData() {
    var request = $.get("/switch-state");

  var tm = request.done(function (result) {
    if (result == 1) {
        document.getElementById("switch").innerText
    } else {
        document.getElementById("switch").innerText
    }
  });
}

requestData()