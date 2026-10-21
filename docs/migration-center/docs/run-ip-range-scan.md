---
url: https://docs.cloud.google.com/migration-center/docs/run-ip-range-scan/
title: Run an IP range scan \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:33:00.638714+00:00
---

# Run an IP range scan  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/run-ip-range-scan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Run an IP range scan Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to run an IP range scan using the `mcdc` CLI.

## Overview

IP range scan lets you detect assets on the network, verify credentials, and collect data from the detected assets. The collected data includes data about the running applications on your machines, which includes both virtual machine (VM) instances and physical servers, and details about the machine configuration, hardware, network, as well as open files, services, and processes.

IP range scan is useful in the following scenarios:

  * If you want to scan assets on environments for which the Migration Center discovery client CLI doesn't support [inventory discovery](https://docs.cloud.google.com/migration-center/docs/run-inventory-discovery), such as VMs running on Azure or machines running in your on-premises infrastructure.
  * If you have have several machines in an IP range, or you don't have much knowledge about the infrastructure you want to scan.
  * If you want to do a complete scan of VMs running on VMware even if you lack access to the vCenter API, you can use IP range scan as an alternative to [guest discovery](https://docs.cloud.google.com/migration-center/docs/run-guest-discovery).
  * If you want to do a complete scan of VMs running on AWS even if you lack access to the AWS API, you can use IP range scan as an alternative to guest discovery.



IP range scan is a two-step process:

  * First, the `mcdc` CLI scans IP addresses to detect assets in your infrastructure.
  * Then, it scans the detected assets for data required to perform an assessment.



The `mcdc` CLI supports data collection through IP range scan for both Linux and Windows target machines. During the IP range scan, the `mcdc` CLI connects to Linux machines using SSH, and to Windows machines using Windows Management Instrumentation (WMI). IP range scan collects the same data as running a guest discovery remotely with SSH or WMI.

To scan an environment with both Windows and Linux machines, run `mcdc` CLI from a Windows workstation. Windows machines require WMI for connection during scanning, and WMI is only supported on Windows workstations.

## Before you begin

  1. Review the [requirements for downloading and running the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements).
  2. Complete the steps to [download `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/download-collector-cli).



## Run an IP scan to discover assets

  * To detect assets in your infrastructure, run the following command:

### Linux
        
        ./mcdc discover ipscan --ranges IP_RANGE

### Windows
        
        mcdc.exe discover ipscan --ranges IP_RANGE

Replace IP_RANGE with a single IP address or a range of IP addresses that you want to scan. The IP ranges can be hyphenated or in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). For example, `0.0.0.0-0.0.0.3` or `0.0.0.0/30`. You can specify more than one range at a time using multiple `--ranges` flags.

  * Alternatively, you can specify a file that contains a list of IP ranges to scan:

### Linux
        
        ./mcdc discover ipscan --file IP_RANGE_FILE.csv

### Windows
        
        mcdc.exe discover ipscan --file IP_RANGE_FILE.csv

Replace IP_RANGE_FILE with the name of the CSV file which contains the range of IP addresses you want to scan. The file must contain comma-separated ranges or ranges in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). Following in an example of an IP range file:
        
        rangeStart,rangeEnd,CIDR
        192.168.9.0,192.168.9.255,""
        "","",192.168.10.0/24
        


**Note:** You can specify ranges using either the `--ranges` flag or `--file` flag. You can't use both of these flags in a single command.

This command then outputs a CSV file containing the list IP addresses of the detected assets. The file looks similar to the following example:
    
    
    ipAddress
    192.168.9.1
    192.168.9.2
    

This file is used as an input for the next step, which is to scan and collect data on the detected assets. By default, this file is saved in the same directory where you installed the `mcdc` CLI.

## Scan the discovered assets

  1. After you've scanned your infrastructure and have the file containing a list of discovered IPs, run a scan on the discovered assets:

### Linux
         
         ./mcdc discover ips --file SCANNED_IPS.csv

### Windows
         
         mcdc.exe discover ips --file SCANNED_IPS.csv

Replace the following:

     * SCANNED_IPS: the path to the file generated by the `discover ipscan` command which contains a list of the IP addresses of your discovered assets.
  2. When prompted, accept the terms and conditions.

Optionally, to skip this step and accept the terms and conditions in the previous step, you can include the `--accept-terms` flag with the `discover ips` command command.

  3. When prompted, enter the credentials using JSON format:

     * Enter username and password:
           
           [{"username":"USERNAME","password":"PASSWORD"}]
           

     * Enter username and specify the path to the identity file:
           
           [{"username":"USERNAME","identityFile":"IDENTITY_FILE"}]
           

     * Enter the username, specify the path to the encrypted identity file, and enter the passphrase:
           
           [{"username":"USERNAME","identityFile":"IDENTITY_FILE","passphrase":"PASSPHRASE"}]
           

If required, you can specify multiple credentials at a time:
    
    [{"username":"FIRST_USERNAME","password":"FIRST_PASSWORD"},{"username":"SECOND_USERNAME","password":"SECOND_PASSWORD"}]
    




After the scan is complete, the collected data is saved in the same local directory where you installed the `mcdc` CLI on the host machine. Additionally, a CSV file is also generated in the same directory, which provides you with the details about the successful and unsuccessful scans. If you want to specify a different location for this CSV file, you can use the `--output-file` with the `discover ips` command.

## What's next

  * Learn how to [export collected data to Migration Center](https://docs.cloud.google.com/migration-center/docs/export-collected-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
