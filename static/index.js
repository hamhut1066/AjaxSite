// Do ajaxy things

var doAjax = function() {
  // Make request to server and put content into web page
  $.ajax("/endpoint").done(function(data) {
    console.log(data)
    $("#content").html(data)
  })
}

var registerCallback = function() {
  // Call function on click
  $("#button").on("click", function() {

    doAjax()
  })
}

// Runs when the page loads
$( document ).ready(function() {

  registerCallback()

  $("#hide-button").on("click", function() {
    $("#content").html("")
  })
})
