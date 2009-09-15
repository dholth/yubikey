#!/usr/bin/env php
<?php
$modhex_json = file_get_contents("modhexmap.js");
$modhex_data = json_decode($modhex_json);
$modhexmap_alphabets = $modhex_data[0];
$modhexmap_reverse_index = array();
foreach($modhex_data[1] as $key => $value) {
    $modhexmap_reverse_index[$key] = $value;
}
$export = var_export(array($modhexmap_alphabets, $modhexmap_reverse_index), true);
print "<?php\n\$modhexmap=" . $export . ";\n";
