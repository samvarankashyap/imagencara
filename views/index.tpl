<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Imagen Cara</title>

    <meta name="author" content="LayoutIt!">

    <link href="/static/bootstrap.min.css" rel="stylesheet">
    <link href="/static/style.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script>
    $( document ).ready(function() {
         
           $("#uploadform").submit(function(event) {
                      event.preventDefault();
                     var data = new FormData(this);
                      data.append("username","samvaran@gmail.com");
                     console.log(data);
                   $.ajax({
                       type        : "POST",
                       url         : "/uploadimage",
                       data        : data,
                       contentType : false,
                       processData : false
                       }).done(function (data) {
                            console.log(data);
                       });
            });
         $("#mypictures").click(function(event) {
                   console.log("Login btn clicked ");
                   var postObj = {};
                   $("#error").html("");
                   postObj["username"] = "samvaran@gmail.com";
                   $.post("/getmypictures",postObj,
                        function(data, status){
                                //$("#content").text(data);
                                console.log(data);
                                $("#feed").html(data);

                        });
         });
          $("#allpictures").click(function(event) {
                   console.log("all pictures btn clicked ");
                   var postObj = {};
                   $("#error").html("");
                   postObj["username"] = "samvaran@gmail.com";
                   $.post("/getallpictures",postObj,
                        function(data, status){
                                //$("#content").text(data);
                                console.log(data);
                                $("#feed").html(data);
                        });
          });

           /* $.post("/login",postObj,
                        function(data, status){
                                //$("#content").text(data);
                                console.log(data);

                                window.location.replace("/main");

                                }
                        });
        });
       */

});

 function deleteimage(post_id) {
             console.log("delete the image ");
                   var postObj = {};
                   postObj["username"] = "samvaran@gmail.com";
                   postObj["post_id"] = post_id;
                   $.post("/deleteimage",postObj,
                        function(data, status){
                                //$("#content").text(data);
                                console.log(data);
                                $( "#mypictures" ).click();
                                $( "#allpictures" ).click();
                        });
           }


    </script>

  </head>
  <body>

    <div class="container-fluid">
	<div class="row">
		<div class="col-md-12">
			<div class="page-header">
				<h1>
					Welcome to the CARA Imagen
				</h1>
			</div>
			<div class="row">
				<div class="col-md-2">
                                        <h2>User Details </h2>
					<img alt="Bootstrap Image Preview" src="http://lorempixel.com/140/140/" class="img-rounded"><br>
					<h6>UserID:</h6>
					<h6>First Name:</h6>
					<h6>Last Name:</h6>
					 <a id="modal-60321" href="#modal-container-60321" role="button" class="btn" data-toggle="modal">Upload Profile Pic</a>
					
					<div class="modal fade" id="modal-container-60321" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
						<div class="modal-dialog">
							<div class="modal-content">
								<div class="modal-header">
									 
									<button type="button" class="close" data-dismiss="modal" aria-hidden="true">
										x
									</button>
									<h4 class="modal-title" id="myModalLabel">
										Upload Profile Picture
									</h4>
								</div>
								<div class="modal-body">
									...
								</div>
								<div class="modal-footer">
									 
									<button type="button" class="btn btn-default" data-dismiss="modal">
										Close
									</button> 
									<button type="button" class="btn btn-primary">
										Save changes
									</button>
								</div>
							</div>
							
						</div>
						
					</div>
					
				</div>
				<div class="col-md-10">
                                         <h2>Picture Feed</h2>
					 <a id="modal-812511" href="#modal-container-812511" role="button" class="btn" data-toggle="modal">Post a Picture</a>   <a id="mypictures" role="button" class="btn" >My Pictures</a>  <a id="allpictures" role="button" class="btn" >All Pictures</a>    <br>
					
					<div class="modal fade" id="modal-container-812511" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
						<div class="modal-dialog">
							<div class="modal-content">
								<div class="modal-header">
									 
									<button type="button" class="close" data-dismiss="modal" aria-hidden="true">
										×
									</button>
									<h4 class="modal-title" id="myModalLabel">
										Upload a Picture
									</h4>
								</div>
								<div class="modal-body">
                                                                        <form id="uploadform" >
									Select File : <input type="file" id="uploadimage" name="uploadimage"><br>
                                                                        <input type="hidden" name="username" value="" id="hiddenusername">
                                                                        <input type="submit" id="uploadbtn" value="Upload">
                                                                        </form>
								</div>
								<div class="modal-footer">
									 
									<button type="button" class="btn btn-default" data-dismiss="modal">
										Close
									</button> 
									<button type="button" class="btn btn-primary">
										Save changes
									</button>
								</div>
							</div>
							
						</div>
						
					</div>
                                        <div id="feed">
					     <img alt="Bootstrap Image Preview" src="http://lorempixel.com/140/140/" class="img-thumbnail"><br>
                                             <img alt="Bootstrap Image Preview"  class="img-thumbnail" src="http://lorempixel.com/140/140/">
                                        </div>
				</div>
			</div>
		</div>
	</div>
</div>

    <script src="/static/jquery.min.js"></script>
    <script src="/static/bootstrap.min.js"></script>
    <script src="/static/scripts.js"></script>
  </body>
</html>
