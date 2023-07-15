class CustomImage {
  constructor(imgUrl, size) {
    this.imgUrl = imgUrl;
    this.size = size;
  }

  backgroundImage() {
    var img = document.querySelector(".jumbotron");
    var text =
      "margin:auto;" +
      "background-image: url(" +
      this.imgUrl +
      ");" +
      "background-size: cover;" +
      "opacity: 1;" +
      "background-blend-mode: darken;" +
      "height: " +
      this.size +
      "vh;";

    img.style.cssText = text;
  }

  centerTitle() {
    var t1 = document.querySelector("#title");
    t1.classList.add("text-black");
    t1.classList.add("text-center");
    t1.classList.add("display-3");
  }
}

const imgUrl =
  "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Devops-toolchain.svg/640px-Devops-toolchain.svg.png";
const size = "25";
var obj = new CustomImage(imgUrl, size);
obj.backgroundImage();
obj.centerTitle();

function requestData() {
  // Ajax call to get the Data from Flask
  var requests = $.get("/data_current");

  var tm = requests.done(function (result) {
    if (result.length > 0) {
      document.getElementById("pHGraph").innerText =
        "Current pH level of the solution ('Potentiometer' readings): " +
        result[4];
      document.getElementById("TempGraph").innerText =
        "Current Ambient Temperature ('Temperature' readings): " + result[1];
      document.getElementById("HumidGraph").innerText =
        "Current Relative Humidity ('Humidity' readings): " + result[2];
      document.getElementById("LightGraph").innerText =
        "Current Ambient lighting intensity ('LDR' readings): " + result[5];
      document.getElementById("ECGraph").innerText =
        "Current EC level ('Moisture sensor' readings): " + result[3];
    } else {
      // Handle the case when data is not available
      document.getElementById("pHGraph").innerText = "No data available";
      document.getElementById("TempGraph").innerText = "No data available";
      document.getElementById("HumidGraph").innerText = "No data available";
      document.getElementById("LightGraph").innerText = "No data available";
      document.getElementById("ECGraph").innerText = "No data available";
    }
  });

  // call it again after one second
  setTimeout(requestData, 500);
}

requestData();
