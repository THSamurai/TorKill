<?php
  $ptf = $_POST['Ptf'];
  $brw = $_POST['Brw'];
  $cc = $_POST['Cc'];
  $ram = $_POST['Ram'];
  $ven = $_POST['Ven'];
  $ren = $_POST['Ren'];
  $ht = $_POST['Ht'];
  $wd = $_POST['Wd'];
  $os = $_POST['Os'];


  $data['dev'][] = array('platform' => $ptf,
  'browser' => $brw,
  'cores' => $cc,
  'ram' => $ram,
  'vendor' => $ven,
  'render' => $ren,
  'ip' => $ip,
  'ht' => $ht,
  'wd' => $wd,
  'os' => $os);
  $jdata = json_encode($data);
  $f = fopen('C:\xampp\htdocs\e\2.txt', 'w+');
  fwrite($f, $jdata);
  fclose($f);

?>
