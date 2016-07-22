<?php

echo "<h1>Hey Dude, you are AWESOME!</h1>";

if (getenv('ENVIRONMENT') == 'stg')
{
  echo "<h2>I am staging</h2>";
}
else if (getenv('ENVIRONMENT') == 'prd')
{ 
  echo "<h2>I am production</h2>";
}
else
{ 
  echo "<h2>I don't know which environment I am.</h2>";
}
