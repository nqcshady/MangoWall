<?php

echo "

<div class='navbar navbar-fixed-top'>
      <div class='navbar-inner'>
        <div class='container'>
          <button type='button' class='btn btn-navbar' data-toggle='collapse' data-target='.nav-collapse'>
            <span class='icon-bar'></span>
            <span class='icon-bar'></span>
            <span class='icon-bar'></span>
          </button>
          <a class='brand' href='index.php'>Dashboard</a>
          <div class='nav-collapse collapse pull-right'>
            <ul class='nav'>
            <li class='dropdown'>
	        <a href='#' class='dropdown-toggle' data-toggle='dropdown'>Account<b class='caret'></b></a>
		<ul class='dropdown-menu' role='menu'>
		  <li><a href='logout.php'>Logout</a></li>
		</ul>
	      </li>
            </ul>
          </div>
        </div>
      </div>
    </div>


";

?>
