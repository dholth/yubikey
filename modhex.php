#!/usr/bin/php
<?php
/* Nearly-any-keymap modhex decoder
Copyright (c) 2009 Daniel Holth <dholth@fastmail.fm>
MIT license. */

require_once("modhexmap.php");

function strtr_utf8($str, $from, $to) {
    $keys = array();
    $values = array();
    preg_match_all('/./u', $from, $keys);
    preg_match_all('/./u', $to, $values);
    $mapping = array_combine($keys[0], $values[0]);
    return strtr($str, $mapping);
}

function decode_modhex_brute($otp, $to="0123456789abcdef") {
    global $modhexmap;
    $alphabets = $modhexmap[0];
    // brute force regex method
    $translations = array();
    foreach($alphabets as $alphabet) {
        $re = "/^[" . $alphabet . "]+$/u";
        $matches = false;
        $rc = preg_match($re, $otp);
        if($rc) {
            $from = $alphabet;
            $translations[strtr_utf8($otp, $from, $to)] = true;
        } 
    }
    return array_keys($translations);
}

function decode_modhex($otp, $to="0123456789abcdef") {
    global $modhexmap;
    $alphabets = &$modhexmap[0];
    $reverse_index = &$modhexmap[1];

    $letters = array();
    preg_match_all('/./u', $otp, $letters);
    $letterset = array_unique($letters[0]);
    $possible = array();
    foreach($letterset as $letter) {
        $possible[] = $reverse_index[$letter];
    }
    if(sizeof($possible) === 0) {
        return array();
    }
    // call_user_func_array(array_intersect) is much slower:
    $result = call_user_func_array(array_merge, $possible);
    $result = array_count_values($result);
    arsort($result);
    $translations = array();
    foreach($result as $key => $value) {
        if($value === sizeof($possible)) {
            $from = $alphabets[$key];
            $translations[strtr_utf8($otp, $from, $to)] = true;
        } else {
            break;
        }
    }
    return array_keys($translations);
}

if(php_sapi_name() == 'cli') {
    $otp="jjjjjjjjtux.bucbkbtecgh.hpcthcnpcgpjhxbjxphp";
    if(sizeof($argv) > 1) {
        $otp=$argv[1];
    }

    $COUNT=1<<13;

    $time_start = microtime(true);
    for($i=0; $i<$COUNT; $i++) {
        $translations = decode_modhex_brute($otp);
    }
    $time_end = microtime(true);
    print_r($translations);
    print "Regex method took " . ($time_end - $time_start) . "s for $COUNT runs\n";

    $time_start = microtime(true);
    for($i=0; $i<$COUNT; $i++) {
        $translations = decode_modhex($otp);
    }
    $time_end = microtime(true);
    print_r($translations);
    print "Reverse index method took " . ($time_end - $time_start) . "s for $COUNT runs\n";
}
