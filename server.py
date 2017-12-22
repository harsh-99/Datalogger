
Added Aditya Rathore. Press backspace to remove.

Skip to content
Using Gmail with screen readers
 
 
More 
1 of 794
 
doda
Inbox
	x
Yash Goyal <goyalyash32@gmail.com>
	
Attachments1:15 AM (1 hour ago)
	
to me
Warm Regards,

Yash Goyal
Vice President Business Expansions
AIESEC IIT KHARAGPUR


Mobile: +91 9602765070
E-mail: goyalyash32@gmail.com


Attachments area
Harsh Maheshwari <harshmaheshwari135@gmail.com>
	
Attachments1:16 AM (1 hour ago)
	
to Aditya
-- 
With Regards,
Harsh Maheshwari
Attachments area
	
Click here to Reply or Forward
6.8 GB (45%) of 15 GB used
Manage
Terms - Privacy
Last account activity: 22 minutes ago
Details
	
	
	Yash Goyal
goyalyash32@gmail.com
Show details

<?php

$dbhost = 'localhost';
$dbuser = 'shubhagr_retina';
$dbpass = 'anveshan_doda';
$dbname = 'shubhagr_agvdata';
$conn=mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

if(!$conn){

die(mysql_error());

}



if(isset($_GET['lati'])&&isset($_GET['longi'])&&isset($_GET['speed'])&&isset($_GET['heading'])&&isset($_GET['gearposition'])&&isset($_GET['brakeposition'])&&isset($_GET['mode'])){


$lati    = $_GET['lati'];
$longi   = $_GET['longi'];
$speed = $_GET['speed'];
$heading    = $_GET['heading'];
$gearposition   = $_GET['gearposition'];
$brakeposition   = $_GET['brakeposition'];
$mode   = $_GET['mode'];

$sql = "INSERT INTO variables (lati, longi, speed, heading, gearposition, brakeposition, mode) VALUES ($lati, $longi, $speed, $heading, $gearposition, $brakeposition, $mode)";

if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
    echo "Current Latitude : " . $lati . "Current Longitude :" . $longi ."Current Speed :" . $speed . "Current Heading :" . $heading . "Gear Position :" . $gearposition ."Brake Status :" . $brakeposition . "Mode :" . $mode . " | ";
} else {
    echo "no record created : " . $sql . "<br>" . mysqli_error($conn);
}


}
else
{
    echo " Dhang se daalo request" ;

}
mysqli_close($conn);

?>

<html>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCDSBgT0i8uM-pk8J62gon4jwkHpn14dT0&callback=initMap" type="text/javascript"></script>

<script type="text/javascript">

var customIcons = {
      restaurant: {
        icon: 'http://labs.google.com/ridefinder/images/mm_20_blue.png'
      },
      bar: {
        icon: 'http://labs.google.com/ridefinder/images/mm_20_red.png'
      }
    };



function myMap() {
  var map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(22.316273, 87.306028),
        zoom: 13,
        mapTypeId: 'roadmap'
      });
  var point = new google.maps.LatLng(
              parseFloat($CLat),
              parseFloat($CLong));

  var icon = customIcons[restaurant] || {};

  var marker = new google.maps.Marker({
            map: map,
            position: point,
            icon: icon.icon
          });

  var icon = customIcons[bar] || {};

  var point = new google.maps.LatLng(
              parseFloat($TLat),
              parseFloat($TLong));

  var marker = new google.maps.Marker({
            map: map,
            position: point,
            icon: icon.icon
          });


}
</script>

<body onload="myMap()">

<h1>            Retina Squared : Google Maps</h1>

<div id="map" style="width:100%;height:500px"></div>


</body>
</html>

doda.php
Displaying doda.php.