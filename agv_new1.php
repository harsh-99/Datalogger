<?php
print_r($_FILES);
if (file_exists("upload/" . $_FILES["file"]["name"]))
        {
            echo $_FILES["file"]["name"] . " already exists. ";
        }
else
  {
    mkdir("upload/".$title, 0700);
    move_uploaded_file($_FILES["file"]["tmp_name"],
    "upload/".$title . $_FILES["file"]["name"]);
    echo "Stored in: " ."upload/".$title . $_FILES["file"]["name"];
  }

?>    
