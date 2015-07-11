<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login Page</title>
    <meta name="description" content="Source code generated using layoutit.com">
    <meta name="author" content="LayoutIt!">
    <link href="/static/bootstrap.min.css" rel="stylesheet">
    <link href="/static/style.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>

  <script>
  $( document ).ready(function() {

 	$( "#loginbtn" ).click(function() {
            console.log("Login btn clicked ");
            var postObj = {};
            $("#error").html("");
            postObj["username"] = $( "#loginemail" ).val();
            postObj["password"] = $( "#loginpassword" ).val();
            $.post("/login",postObj,
    			function(data, status){
                                //$("#content").text(data);
                                console.log(data);
                                
                                $("#error").html(data);
                                if(data=="User authentication sucessfull"){
                                localStorage.setItem("username",postObj["username"] );
                                console.log(localStorage.getItem("username"));
                                window.location.replace("/main");

                                }
               		});
        })

        $( "#regbtn" ).click(function() {
            console.log("Reg btn clicked ");
            var postObj = {};
            $("#error2").html("");
            postObj["username"] = $( "#regemail" ).val();
            postObj["password"] = $( "#regpassword1" ).val();
            $.post("/registeruser",postObj,
                        function(data, status){
                                //$("#content").text(data);
                                console.log(data);
                                $("#error2").html(data);
                        });
            
        })



});



  </script>

  </head>
  <body>
    <div class="container-fluid">
	<div class="row" >
		<div class="col-md-4 col-md-offset-5" >
			<h3>
				Login :
			</h3>
				<div class="form-group">
					 
					<label for="exampleInputEmail1">
						Email address
					</label>
					<input type="email" class="form-control" id="loginemail">
				</div>
				<div class="form-group">
					 
					<label for="exampleInputPassword1">
						Password
					</label>
					<input type="password" class="form-control" id="loginpassword">
				</div>
				<button class="btn btn-default" id="loginbtn">
					Login
				</button>
                                <div id="error"></div>
		</div>
	</div>
</div>


    <div class="container-fluid">
        <div class="row" >
                <div class="col-md-4 col-md-offset-5" >
                        <h3>
                                User Registration:
                        </h3>
                                <div class="form-group">

                                        <label for="exampleInputEmail1">
                                                Email address
                                        </label>
                                        <input type="email" class="form-control" id="regemail">
                                </div>
                                <div class="form-group">

                                        <label for="exampleInputPassword1">
                                                Password
                                        </label>
                                        <input type="password" class="form-control" id="regpassword1">
                                </div>
                                <div class="form-group">

                                        <label for="exampleInputPassword1">
                                                Confirm Password
                                        </label>
                                        <input type="password" class="form-control" id="regpassword2">
                                </div>
                                <button class="btn btn-default" id="regbtn">
                                        Register
                                </button>
                                <div id="error2"></div>
                </div>
        </div>
</div>

  </body>
</html>
