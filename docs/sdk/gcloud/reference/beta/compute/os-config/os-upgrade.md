---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/os-upgrade/
title: gcloud beta compute os-config os-upgrade \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:52:12.882118+00:00
---

# gcloud beta compute os-config os-upgrade  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/os-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute os-config os-upgrade Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute os-config os-upgrade - upgrade the instances OS version 
SYNOPSIS
    

`gcloud beta compute os-config os-upgrade` `INSTANCE_NAME` `--source-os`=`SOURCE_OS` `--target-os`=`TARGET_OS` [`--async`] [`--auto-rollback`] [`--no-create-machine-backup`] [`--log-location`=`LOG_LOCATION`] [`--timeout`=`TIMEOUT`; default="2h"] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute os-config os-upgrade` upgrades the instance's OS version. 

OS Upgrade involves: 

  * Create a snapshot and/or machine image for the instance. 
  * Create an install media disk and attach it to the instance. 
  * Upgrade the OS version. 
  * Cleanup install media disk after upgrade. 



Virtual instances, snapshots, machine images, and disks in Compute Engine and files stored on Cloud Storage incur charges. See <https://cloud.google.com/compute/docs/images/importing-virtual-disks#resource_cleanup>. 

EXAMPLES
     To upgrade a instance named `my-instance` from windows-2008r2 to windows-2012r2, run: 
    
    
    gcloud beta compute os-config os-upgrade my-instance --source-os=windows-2008r2 --target-os=windows-2012r2

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to os-upgrade. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
REQUIRED FLAGS
    

`--source-os`=`SOURCE_OS`
     OS version of the source instance to upgrade. `SOURCE_OS` must be (only one value is supported): `windows-2008r2`. 
`--target-os`=`TARGET_OS`
     Version of the OS after upgrade. `TARGET_OS` must be (only one value is supported): `windows-2012r2`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--auto-rollback`
     When auto rollback is enabled, the instance and its resources are restored to their original state. Otherwise, the instance and any temporary resources are left in the intermediate state of the time of failure. This is useful for debugging. 
`--create-machine-backup`
     When enabled, a machine image is created that backs up the original state of your instance. Enabled by default, use `--no-create-machine-backup` to disable. 
`--log-location`=`LOG_LOCATION`
     Directory in Cloud Storage to hold build logs. If not set, `gs://<project num>.cloudbuild-logs.googleusercontent.com/` is created and used. 
`--timeout`=`TIMEOUT`; default="2h"
     Maximum time an upgrade can last before it fails as "TIMEOUT". For example, if you specify `2h`, the process fails after 2 hours. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information about duration formats. 

This timeout option has a maximum value of 24 hours. 

`--zone`=`ZONE`
     Zone of the instance to os-upgrade. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha compute os-config os-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-config/os-upgrade)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
