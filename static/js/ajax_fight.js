$(document).on('submit', '.fight', function(e){
    e.preventDefault();
    var action_url = $(this).attr("action")
    formData = new FormData($(this).get(0));
    $.ajax({
        type: "POST",
        url: action_url,
        data: formData,
        contentType: false,
        processData: false,
        success: function(response){
            if ("html" in response){
                var html = response["html"]
                var newhtml = document.open("text/html","replace");
                newhtml.write(html)
                newhtml.close();
            }
            else if("error" in response){
                document.querySelector('.err').innerHTML = "<b>Form errors</b>"
                for (let key in response["error"]) {
                    document.querySelector('.err').innerHTML += key + ": " + response["error"][key] + "</br>"
                }
            }
        }
    })
})