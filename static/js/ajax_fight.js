$(".fight").submit(function(e){
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
            if ("success" in response){
                
                document.querySelector('.msg_at').innerHTML = response["msg_at"]
                document.querySelector('.msg_def').innerHTML = response["msg_def"]
                document.querySelector('.msg_bot_a').innerHTML = response["msg_bot_a"]
                document.querySelector('.msg_bot_def').innerHTML = response["msg_bot_def"]

                location.reload()
            }
            else if("error" in response){
                document.querySelector('.form-errors').innerHTML = "<b>Form errors</b>"
                for (let key in response["error"]) {
                    document.querySelector('.form-errors').innerHTML += key + ": " + response["error"][key] + "</br>"
                }
            }
        }
    })
})