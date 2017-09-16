<?php

$udp = shell_exec('tcpdump -n udp');
$tcp = shell_exec('tcpdump -n tcp');
$icmp = shell_exec('tcpdump -n icmp');
echo "
  <h2>Traffic</h2>
    <table class='table'>
      <thead>
        <th><span class='color'>UDP Connections</span></th>
";
echo("<tr><td><pre>".$tcp."</pre></tr></td>");
echo("<th><span class='color'>TCP Connections</span></th>");
echo("<tr><td><pre>".$udp."</pre></tr></td>");
echo("<th><span class='color'>ICMP Connections</span></th>");
echo("<tr><td><pre>".$icmp."</pre></tr></td>");

echo "</thead>";
echo "</table>";

?>