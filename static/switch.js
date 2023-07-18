document.getElementById('switch-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission

  // Make an AJAX request to the server
  $.ajax({
    type: 'POST',
    url: '/switch-state',
    success: function(result) {
      if (result == 1) {
        document.getElementById("switch").innerText = "Stop System";
        sysRunText.innerText = "System Running";
        circle.classList.remove("stopped");
      } else if (result == -1) {
        document.getElementById("switch").innerText = "Start System";
        sysRunText.innerText = "System Stopped";
        circle.classList.add("stopped");
      }
    },
    error: function(error) {
      console.log(error);
    }
  });
});
