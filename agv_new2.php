<?php


$dbhost = 'localhost';
$dbuser = 'shubhagr_retina';
$dbpass = 'anveshan_doda';
$dbname = 'shubhagr_agvdata';
$conn=mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

$latiarray = array();
$longiarray = array();
$speedarray = array();
$headingarray = array();
$gearpositionarray = array();
$brakepositionarray = array();
$modearray = array();

if(!$conn){

die(mysqli_error());

}



if(isset($_GET['lati'])&&isset($_GET['longi'])&&isset($_GET['speed'])&&isset($_GET['heading'])&&isset($_GET['gearposition'])&&isset($_GET['brakeposition'])&&isset($_GET['mode'])){


$lati    = $_GET['lati'];
$longi   = $_GET['longi'];
$speed = $_GET['speed'];
$heading    = $_GET['heading'];
$gearposition   = $_GET['gearposition'];
$brakeposition   = $_GET['brakeposition'];
$mode   = $_GET['mode'];

$sql = "INSERT INTO variables_data (lati, longi, speed, heading, gearposition, brakeposition, mode) VALUES ($lati, $longi, $speed, $heading, $gearposition, $brakeposition, $mode)";


if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
    echo "Current Latitude : " . $lati . "Current Longitude :" . $longi ."Current Speed :" . $speed . "Current Heading :" . $heading . "Gear Position :" . $gearposition ."Brake Status :" . $brakeposition . "Mode :" . $mode . " | ";
} else {
    echo "no record created : " . $sql . "<br>" . mysqli_error($conn);
}


}
else
{
 $sql = "  SELECT id, lati, longi, speed, heading, gerposition, brakeposition, mode FROM variables_data ORDER BY id DESC LIMIT 20";

$result = $conn->query($sql);
if ($result->num_rows>0)
{
    while ($row = $result->fetch_assoc())
{

    echo "id: " . $row["id"] . " | latitude: " . $row["lati"] . " | longitude: " . $row["longi"] . " | speed: " . $row["speed"] . " | heading: " . $row["heading"] . " | gearposition: " . $row["gearposition"] . " | brakeposition: " . $row["brakeposition"];
    array_push( $latiarray  , $row["lati"]  );
    array_push( $longiarray  , $row["longi"] );
    array_push( $speedarray  , $row["speed"] );
    array_push( $headingarray  , $row["heading"] );
    array_push( $gearpositionarray  , $row["gearposition"] );
    array_push( $brakepositionarray  , $row["brakeposition"] );
    array_push( $modearray  , $row["mode"] );

}

}
}

?>

<html>

<div id="dom" style= "color:#0000FF" >
  <?php
  $z="|";
  echo htmlspecialchars("Latitude");
  echo htmlspecialchars($z);
  echo htmlspecialchars("Longitude");
  echo htmlspecialchars($z);
  echo htmlspecialchars("Speed");
  echo htmlspecialchars($z);
  echo htmlspecialchars("Heading");
  echo htmlspecialchars($z);
  echo htmlspecialchars("Gearposition");
  echo htmlspecialchars($z);
  echo htmlspecialchars("Brakeposition");
  echo htmlspecialchars($z);
  echo htmlspecialchars("Mode");
  echo htmlspecialchars($z);

  for ($x = 0; $x <= 19; $x++){
     echo htmlspecialchars($latiarray[$x]);
     echo htmlspecialchars($z);
     echo htmlspecialchars($longiarray[$x]);
     echo htmlspecialchars($z);
     echo htmlspecialchars($speedarray[$x]);
     echo htmlspecialchars($z);
     echo htmlspecialchars($headingarray[$x]);
     echo htmlspecialchars($z);
     echo htmlspecialchars($gearpositionarray[$x]);
     echo htmlspecialchars($z);
     echo htmlspecialchars($brakepositionarray[$x]);
     echo htmlspecialchars($z);
     echo htmlspecialchars($mode[$x]);
     echo htmlspecialchars($z);
  }

  ?>
</div>
<head>
  <meta http-equiv="refresh" content="50">
</head> 
</html>



