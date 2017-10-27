<?php
    $ip = $_POST["ip"];
    $oid = $_POST["oid"];
    try{
    shell_exec("python script.py -i".$ip." -o".$oid);
    }
    catch (Exception $e) {
    echo 'Caught exception: ',  $e->getMessage(), "\n";
}
?>
