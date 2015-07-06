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
					 <a id="modal-812511" href="#modal-container-812511" role="button" class="btn" data-toggle="modal">Post a Picture</a><br>
					
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
					<img alt="Bootstrap Image Preview" src="http://lorempixel.com/140/140/" class="img-thumbnail"><br><img alt="Bootstrap Image Preview"  class="img-thumbnail" src="http://lorempixel.com/140/140/">
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
