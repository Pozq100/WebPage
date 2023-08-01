function requestData() {
    // Ajax call to get the Data from Flask
    var requests = $.get("/data_current");
    $.get("/get-switch-state", function(result) {
      var sysRunText = document.getElementById("sys-run-text");
      var circle = document.querySelector(".circle");
  
      if (result == 1) {
        sysRunText.innerText = "System Running";
        circle.classList.add("started");
        circle.classList.remove("stopped");
      } else if (result == -1) {
        sysRunText.innerText = "System Stopped";
        circle.classList.add("stopped");
        circle.classList.remove("started")
      }
    });
  // call it again
    setTimeout(requestData, 500);
  }
  
  requestData();
  