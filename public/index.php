<?php

declare(strict_types=1);

require __DIR__ . "/../vendor/autoload.php";
require_once __DIR__ . "/../config/config.php";

$route = $_SERVER["REQUEST_URI"];

switch($route){
    case "/":
        echo "funktioniert";
        exit;

    default:
        echo "404";
        break;
}