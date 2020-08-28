# Rename APs in bulk in Ekahau

## Summary

Often when performing a post install validation survey, we like to see actual AP
names instead of randomly assigned names. And because AP names aren't
necessarily advertised in the beacons, we have to manually type them in
Ekahau Pro.

In Ekahau's current version (10.0.2), renaming APs is only possible using the
GUI, by editing APs one by one, which can be laborious if you have many APs in
the survey.

This simple script allows you to import a list of BSSIDs and their associated AP
names into Ekahau pro.

## Prerequisites

> **This tool can only be ran after the survey is completed. You will not be
> able to see AP names during a live survey.**

### 1) Obtain a BSSID table containing the BSSID <-> AP name mapping

Prior to running the tool, you need to collect the BSSID <-> AP name mapping
for all BSSes that you'd like to have named in Ekahau.
There are many ways to do that depending on which WiFi vendor you have and which
tool do you use to monitor your WiFi infrastructure. It is up to you how you
want to collect that information.

After you have collected the BSSID table, edit the data in a text file to have
it confom to this format:

```
<apname1>,<macaddress1>
<apname2>,<macaddress2>
```
> Each line should contain comma separated AP name/MAC address pairings.
> The MAC addresses in the file must be in the colon separated octets 
> format (MAC address and AP names are not case sensitive).
> example: 00:11:22:aa:bb:cc

### 2)  Unzip the esx file

Once the survey is complete and the Ekahau project is saved, go ahead and
unzip the corresponding esx file (yes it is a zip file). You will need to
provide the path to that resulting unzipped folder.

## Dependencies

Python 3.5 or greater installed.

Any archiving utility capable of zipping and unzipping (e.g. Winzip, Mac OS
native compression software).

## Usage Examples

```
$python3 rename_ekahau_apnames.py -b ~/bssidmapping.csv -f ~/myekahauproject/
AP were successfully named in accessPoints.json. Now zip all the files in that folder and change the extention from .zip to .esx.")
```

## Disclaimer

This script does not have a lot of error handling in place(lots of TODOs) so
make sure your input files (BSSID mapping and esx folder) are in the right
format.
