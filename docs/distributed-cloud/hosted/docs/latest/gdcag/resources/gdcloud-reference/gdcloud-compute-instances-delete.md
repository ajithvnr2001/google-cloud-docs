---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-compute-instances-delete/
title: gdcloud compute instances delete \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:15.176437+00:00
---

# gdcloud compute instances delete  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-compute-instances-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud compute instances delete Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute instances delete - Delete virtual machine instances.

## SYNOPSIS
    
    
    gdcloud compute instances delete INSTANCE_NAME [flags]
    

### EXAMPLES
    
    
    To delete an instance named "example-instance" in project "example-project", run:
    
        gdcloud compute instances delete example-instance --project example-project
    

### OPTIONAL FLAGS
    
    
          --delete-disks DISK_TYPE   The types of disks to delete with instance deletion regardless of the
                                     disks' auto-delete configuration on the VM instance. When this flag is
                                     provided, the auto-delete bits on the attached disks are modified
                                     accordingly before the instance deletion request is issued.
                                     
                                     DISK_TYPE must be one of:
                                     all: All disks
                                     boot: Only the disks where first partition is reserved for the root filesystem
                                     data: Only non-boot disks
                                     The default is to leave the auto-delete bits on the attached disks unchanged.
          --keep-disks DISK_TYPE     The types of disks to NOT delete with instance deletion regardless of
                                     the disks' auto-delete configuration on the VM instance. When this flag
                                     is provided, the auto-delete bits on the attached disks are modified
                                     accordingly before the instance deletion request is issued.
                                     
                                     DISK_TYPE must be one of:
                                     all: All disks
                                     boot: Only the disks where first partition is reserved for the root filesystem
                                     data: Only non-boot disks
                                     The default is to leave the auto-delete bits on the attached disks unchanged.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
