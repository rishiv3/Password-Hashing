$password = 'johndoe';
$hash = password_hash($password, PASSWORD_DEFAULT);
$expensiveHash = password_hash($password, PASSWORD_DEFAULT, array('cost' => 20));

password_verify('johndoe', $hash); //Returns true
password_verify('johndoe', $expensiveHash); //Also returns true
password_verify('johncena', $hash); //Returns false
