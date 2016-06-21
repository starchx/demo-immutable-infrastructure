<?php

echo "<h1>Hey Dude #1</h1>";

if(stristr($_SERVER[HTTP_HOST], 'stg.opq.com.au') === TRUE)
{
  echo "<h2>I am staging</h2>";
}
else
{ 
  echo "<h2>I am production</h2>";
}
