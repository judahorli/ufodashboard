function call_random_report() {
  var req = new XMLHttpRequest()
  req.onreadystatechange = function() {
    if (req.readyState == 4) {
      if (req.status != 200) {
        //error handling code here
        console.log(req.responseText);
      } else {
        var response = JSON.parse(req.responseText);
        document.getElementById('random_report').innerHTML = response.html;
      }
    }
  }

  req.open('POST', '/random');
  req.setRequestHeader("Content-type", "application/x-www-form-urlencoded;charset=UTF-8");
  req.send();

  return false;
}

