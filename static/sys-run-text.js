function requestData() {
    $.get("/get-switch-state", function(result) {
      if (result == 1) {
        document.getElementById("sys-run-text").innerText = "System Running";
      } else if (result == -1) {
        document.getElementById("sys-run-text").innerText = "System Stopped";
      }
    });
  }
  
  $(document).ready(function () {
    setInterval(requestData, 500);
  });
  