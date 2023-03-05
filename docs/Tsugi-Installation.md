# Tsugi Installation

## Pre-Requisites

- Install a PHP/MySQL Environment like MAMP following the instructions below OR watching the [Youtube Video](https://www.youtube.com/watch?v=CwwF801i5_4&t=4s).
  - Install MAMP from [here](https://www.mamp.info/en/mac/)
  - Open MAMP, start the server.
  - Go to [http://localhost:8888/MAMP/](http://localhost:8888/MAMP/)
  - Go to ```phpInfo``` tab.
  - Find ```Loaded Configuration File```, open ```php.ini``` file based on the URL in this row.
  - Find ```display_errors = Off``` and ```display_startup_errors = Off```, and set to: ```display_errors = On``` and ```display_startup_errors = On```.
  - Restart MAMP. Go to ```phpInfo``` tab. Make sure ```display_errors = On``` and ```display_startup_errors = On```

## Installation

Download the source code from Github.

```code
  git clone https://github.com/tsugiproject/tsugi.git
```

Set up the Database.

```code
  CREATE DATABASE tsugi DEFAULT CHARACTER SET utf8;
  CREATE USER 'ltiuser'@'localhost' IDENTIFIED BY 'ltipassword';
  GRANT ALL ON tsugi.* TO 'ltiuser'@'localhost';
  CREATE USER 'ltiuser'@'127.0.0.1' IDENTIFIED BY 'ltipassword';
  GRANT ALL ON tsugi.* TO 'ltiuser'@'127.0.0.1';

  Or

  CREATE DATABASE ltiuser DEFAULT CHARACTER SET utf8;
  GRANT ALL ON tsugi.* TO ltiuser@'localhost';
  GRANT ALL ON tsugi.* TO ltiuser@'127.0.0.1';
  SET PASSWORD FOR 'ltiuser'@'localhost' = PASSWORD('ltipassword');
  SET PASSWORD FOR 'ltiuser'@'127.0.0.1' = PASSWORD('ltipassword');
```

Modify ```config.php``` file. Note 8891 is apache port (default port is 8888).

Under the code

```code
// Set the path to the Tsugi folder without a trailing slash
if ( $apphome ) {
    $wwwroot = $apphome . '/tsugi';
} else if ( U::get($_SERVER,'SERVER_PORT') == 8888 ) {
    $wwwroot = 'http://localhost:8888/tsugi'; // Mac XAMP
} else {
    $wwwroot = "http://localhost/tsugi";
}
```

Add this:

```code
$wwwroot = "http://localhost:8891/tsugi";
```

Set ```$CFG-pdo```. Note: mysql port 8889 should be the same with the mysql setting in MAMP.

```code
// $CFG->pdo       = 'mysql:host=tsugi_db;dbname=tsugi';
$CFG->pdo       = 'mysql:host=127.0.0.1;port=8889;dbname=tsugi'; // MAMP
```

Open MAMP, set ```Document root``` to path/to/parent folder of tsugi. Then start the MAMP server.

Open [http://localhost:8891/tsugi/](http://localhost:8891/tsugi/)
