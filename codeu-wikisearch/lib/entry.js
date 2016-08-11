function getText() {
  var text = ""
  var first = document.getElementById("ftextField").value;
  var option = operation.options[operation.selectedIndex].text;
  var second = document.getElementById("ftextField").value;
  text = first + option + second
  // document.getElementById("result").value = text
}
