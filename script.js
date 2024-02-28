
document.getElementById("save").addEventListener("click", function() {
  // Get the form data
  const formData = new FormData(document.getElementById("extemporaneous-form"));

  // Send the form data to the server using AJAX
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "save_data.php");
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        // Data saved successfully
        console.log(xhr.responseText);
        alert("Data saved successfully!");
      } else {
        // Error saving data
        console.error(xhr.responseText);
        alert("Error saving data. Please try again later.");
      }
    }
  };
  xhr.send(formData);
});

