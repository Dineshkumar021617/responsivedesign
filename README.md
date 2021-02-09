# Design of Responsive Website
## AIM:
To design a responsive website with two break points.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and Bootstrap.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Two break points</title>
  </head>
  <body>
    {%load static%}
    <!DOCTYPE HTML>
    <html lang='en'>
        <head>
            <title>DK Silicon Chip PVT Ltd</title>      
        </head>
        <body>
            <div class="container-fluid text-center" style="height: 50%;
                                                            background-image : url('/static/photos/chipbanner.jpg');
                                                            background-size:cover;">
                <h1 style="padding-top:5%;
                           padding-bottom:5%;
                           color:white;">
                    DK Silicon Chip PVT Ltd
                </h1>
            </div>
            <div class="text-center" style="padding-top: 50px;">
                <div href="/home" class="btn btn-primary" style="background-color: red;"><a class="col-12 col-md-3">Home</a></div> 
                <div href="/products" class="btn btn-primary" style="background-color: red;"><a>Products</a></div> 
                <div  href="/people" class="btn btn-primary" style="background-color: red;"><a>People</a></div>
                <div href="/contactus" class="btn btn-primary" style="background-color: red;"><a>Contact Us</a></div> 
                <h3 style="padding-top: 50px;" >Our Premium Products</h3>
                <div class="row">
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c1.jpg" class="card-img-top" style="padding-top:20px;" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">4GB DDRA4 laptop memory</h5>
                            <p class="card-text">Price: Rs.2000.00</p>
                            <a href="#" class="btn btn-primary" style=>More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3" style="padding-top:20px;">
                        <img src="/static/photos/c2.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">1TB Laptop HDD</h5>
                            <p class="card-text">Price: Rs.5000.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c3.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">1TB 665p Series M.2 2280 PCIe NVMe 3.0 x4 3D3, QLC Internal Solid State Drive (SSD)</h5>
                            <p class="card-text">Price: Rs.12000.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c4.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">2TB 3D NAND NVMe PCIe Internal SSD</h5>
                            <p class="card-text">Price: Rs.38000.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3" style="padding-top:20px;"> 
                        <img src="/static/photos/c5.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">16GB Single DDR4 2666  PC4-21300 DR x8 SODIMM 260-Pin RAM</h5>
                            <p class="card-text">Price: Rs.7000.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c6.jpg"  alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">8GB DDR4 modules for notebooks 2666 Laptop Memory</h5>
                            <p class="card-text">Price: Rs.10000.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3" style="padding-top:20px;">
                        <img src="/static/photos/c7.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">8GB DDR4-2400 PC4-19200 CL-17 SODIMM RAM</h5>
                            <p class="card-text">Price: Rs.2800.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c8.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">Analog to Digital Breakout Board</h5>
                            <p class="card-text">Price: Rs.600.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c9.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">ATmega32 Microcontroller</h5>
                            <p class="card-text">Price: Rs.100.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c10.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">PIC Development Board ZIF Socket with On Board PIC16F877A MAX232</h5>
                            <p class="card-text">Price: Rs.900.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c11.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">Quick Starter Development Board and AVR USB ISP Programmer Starter Kits</h5>
                            <p class="card-text">Price: Rs.1000.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                    <div class="card col-12 col-md-3">
                        <img src="/static/photos/c12.jpg" class="card-img-top" alt="product image">
                        <div class="card-body">
                            <h5 class="card-title">Infrared (IR) Proximity or Obstacle Detecting Sensor Module</h5>
                            <p class="card-text">Price: Rs.100.00 </p>
                            <a href='#' class="btn btn-primary">More details</a>
                        </div>
                    </div>
                </div>
                </div>
                <div class="footer text-center" style="background-color:red;">
                    Copyright © 2020 Silicon Company Private Limited, Developed by Dineshkumar.S
                </div>
                </div>
            </div>
        </body>
    </html>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

## OUTPUT:
### Mobile view:
![output](./static/photos/Mobileview.png)
### Laptop view:
![output](./static/photos/Laptopview.png)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://dineshkumars.student.saveetha.in:8000/2breaks . HTML code is validated.