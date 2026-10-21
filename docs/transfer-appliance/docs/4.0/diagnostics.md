---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/diagnostics/
title: Check for configuration issues \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:20.203577+00:00
---

# Check for configuration issues  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/diagnostics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Check for configuration issues Stay organized with collections  Save and categorize content based on your preferences. 

`ta check` is a command line tool to detect and help fix configuration issues with Transfer Appliance.

To check all categories:
    
    
    ta check
    

To check a single category:
    
    
    ta check CATEGORY
    

For a list of valid categories, see Categories and checks below.

## Responses and logs

Each test returns one of the following statuses:

  * **Passed:** All conditions were met.
  * **Failed:** Any of the required conditions weren't met.
  * **Warning** : The conditions weren't met but does not block the appliance from being used.
  * **Skipped** : The check is not supported by the appliance type or the check failed due to internal errors.



More information is captured by the log file, found at `/mnt/ta_metadata/logs/tacheck/tacheck.log`.

## Categories and checks

Category | Check | Notes | Transfer Appliance | Online-enabled Transfer Appliance  
---|---|---|---|---  
`hardware` | Encrypt disks | Ensures that the appliance's data disks have been encrypted. | check_circle | check_circle  
Drives | Verifies the correct number of boot disks and data disks. | check_circle | check_circle  
`software` | Firmware | Confirms whether the device firmware is up to date. | remove | check_circle  
OS version | Ensures that the device OS is up to date. | remove | check_circle  
Google APIs | Ensures that all required Google Cloud APIs are enabled. | remove | check_circle  
`encryption` | Encrypt disks | Ensures that the appliance's data disks have been encrypted. | check_circle | check_circle  
TPM-wrapped DEK | Ensures that the encrypted data encryption key (DEK) is present on the device. | check_circle | check_circle  
`keys` | Key | Looks for the existence of the `key.json` service account key file on the device. The file must be at either `/tmp/key.json` or `/mnt/ta_metadata/key.json`.  | remove | check_circle  
`network` | Network interfaces | Makes sure that all ethernet ports on the device are functioning. | remove | check_circle  
Ethernet ports IP | Checks if the required ports have an IP assigned. | remove | check_circle  
Access | Confirms network access by pinging google.com | remove | check_circle  
`usage` | Data usage | Compares data disk usage against the threshold (75%). | check_circle | check_circle  
Boot usage | Compares boot disk usage against the threshold (75%). | check_circle | check_circle  
RAM usage | Compares total memory usage of the RAM against the threshold (75%).  | check_circle | check_circle  
`SSH` | Unique hosts count | Counts the number of unique hosts located in the `~/.ssh/config` file and warns if there are too many. | remove | check_circle  
SSH config | Reports typos in the `~/.ssh/config` file. | remove | check_circle  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
