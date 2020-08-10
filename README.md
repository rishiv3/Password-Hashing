# Password Hashing

## Python
Password hashing using SHA256 and Salt in Python

As of Python 3.4, the `hashlib` module in the standard library contains [key derivation](https://docs.python.org/3/library/hashlib.html#key-derivation) functions which are *"designed for secure password hashing"*.


## PHP

As of PHP 5.5, PHP has simple, secure functions for hashing and verifying passwords, [password_hash()](http://php.net/manual/en/function.password-hash.php) and [password_verify()](http://php.net/manual/en/function.password-verify.php)

    $password = 'anna';
    $hash = password_hash($password, PASSWORD_DEFAULT);
    $expensiveHash = password_hash($password, PASSWORD_DEFAULT, array('cost' => 20));
    
    password_verify('anna', $hash); //Returns true
    password_verify('anna', $expensiveHash); //Also returns true
    password_verify('elsa', $hash); //Returns false

When `password_hash()` is used, it generates a random salt and includes it in the outputted hash (along with the the cost and algorithm used.) `password_verify()` then reads that hash and determines the salt and encryption method used, and verifies it against the provided plaintext password.

Providing the `PASSWORD_DEFAULT` instructs PHP to use the default hashing algorithm of the installed version of PHP. Exactly which algorithm that means is intended to change over time in future versions, so that it will always be one of the strongest available algorithms.

Increasing cost (which defaults to 10) makes the hash harder to brute-force but also means generating hashes and verifying passwords against them will be more work for your server's CPU.

Note that even though the default hashing algorithm may change, old hashes will continue to verify just fine because the algorithm used is stored in the hash and `password_verify()` picks up on it.
