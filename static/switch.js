function requestData() {
    var requests = $.get("/switch-state");

  var tm = requests.done(function (result) {
    if (result == 1) {
        document.getElementById("switch").innerText
    } else {
        document.getElementById("switch").innerText
    }
  });

  // call it again after one second
  setTimeout(requestData, 500);
}

requestData()