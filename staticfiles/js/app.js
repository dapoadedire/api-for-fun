function copy() {
    var text_to_copy = document.getElementById("copy-text").innerHTML;

    navigator.clipboard.writeText(text_to_copy).then(
        function(){
            alert("Copied successfully"); // success 
        })
      .catch(
         function() {
            alert("Error"); // error
      });
} 

