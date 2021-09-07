let btnUpload = $("#upload_file")
btnOuter = $(".button_outer");
btnUpload.on("change", function(e){
    let value = e.target.files[0].name.split(".");
    // var ext = btnUpload.val().split('.').pop().toLowerCase();
    if($.inArray(value[1], ['gif','png','jpg','jpeg']) == -1) {
        $(".error_msg").text("Not an Image...");
    } else {
        $(".error_msg").text("");
        btnOuter.addClass("file_uploading");
        setTimeout(function(){
            btnOuter.addClass("file_uploaded");
        },3000);
        var uploadedFile = URL.createObjectURL(e.target.files[0]);
        var postFormData = new FormData();
        postFormData.append("title", value[0])
        postFormData.append("image", e.target.files[0])
        // postFormData = {
        //     "title": value[0],
        //     "image": uploadedFile
        // }
        var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        var xhttp = new XMLHttpRequest();
        xhttp.open( 'POST', "https://imageuploaderpardeshi.herokuapp.com/", true);
        xhttp.setRequestHeader("X-CSRFToken", $crf_token);
        xhttp.send(postFormData);
        xhttp.onreadystatechange = function(result) {
            if (this.status == 201 && this.readyState == 4) {
                console.log(
                    'Photo Submitted!'
                );

            }
            else{
                console.log(
                    `OOPS`,
                    `green`
                );
            }
        }
        // xhttp.send(formData);
        setTimeout(function(){
            $("#myModal").modal('show');
            $("#uploaded_view").append('<img src="'+uploadedFile+'" />').addClass("show");
        },3500);
    }
});
$(".file_remove").on("click", function(e){
    $("#uploaded_view").removeClass("show");
    $("#uploaded_view").find("img").remove();
    btnOuter.removeClass("file_uploading");
    btnOuter.removeClass("file_uploaded");
});

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })