---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/disk-migrations/create/
title: gcloud alpha compute migration disk-migrations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:49:19.467731+00:00
---

# gcloud alpha compute migration disk-migrations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/disk-migrations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute migration disk-migrations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute migration disk-migrations create - create a disk migration resource to migrate a disk to Compute Engine 
SYNOPSIS
    

`gcloud alpha compute migration disk-migrations create` (`DISK_MIGRATION` : `--location`=`LOCATION` `--source`=`SOURCE`) `--source-volume-id`=`SOURCE_VOLUME_ID` [`--disk-id`=`DISK_ID`] [`--disk-type`=`DISK_TYPE`] [`--kms-key`=`KMS_KEY`] [`--labels`=[`KEY`=`VALUE`,…]] [`--target-project`=`TARGET_PROJECT`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha compute migration disk-migrations create lets you create disk migration resource. You must create a disk migration resource before you can migrate your disk from any migration source to a Compute Engine disk. The disk migration resource tracks the progress of the disk migration. To use this command, you must enable VM Migration API in your project. 

Note that this command only creates a disk migration resource. It does not initiate the disk migration process. After creating the disk migration resource, you must initiate the migration process using the run command. 

EXAMPLES
     To create a disk migration resource to migrate a volume vol-12345 from an AWS source my-aws-source to my-target-project in us-central1, create the my-disk-migration disk migration resource in my-project in us-central1, run: 
    
    
    gcloud alpha compute migration disk-migrations create my-disk-migration --project=my-project --location=us-central1 --source=my-aws-source --source-volume-id=vol-12345 --disk-id=gcp-disk1 --target-project=projects/my-project/locations/global/targetProjects/my-target-project

POSITIONAL ARGUMENTS
    

Disk migration resource - The disk migration resource you want to create. This would be the disk ID if --disk-id is not given. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `disk_migration` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DISK_MIGRATION`
     ID of the disk_migration or fully qualified identifier for the disk_migration. 

To set the `disk_migration` attribute: 

  * provide the argument `disk_migration` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Resource location. 

To set the `location` attribute: 

  * provide the argument `disk_migration` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


`--source`=`SOURCE`
     The client source environment object. 

To set the `source` attribute: 

  * provide the argument `disk_migration` on the command line with a fully specified name; 
  * provide the argument `--source` on the command line. 


REQUIRED FLAGS
    

`--source-volume-id`=`SOURCE_VOLUME_ID`
     The ID of the source volume that you want to migrate to Compute Engine. 
OPTIONAL FLAGS
    

`--disk-id`=`DISK_ID`
     The ID of the disk that will be migrated to Compute Engine. The default value is the disk migration resource name. 
`--disk-type`=`DISK_TYPE`
     The Compute Engine disk type to use for the migrated disk. The default value is COMPUTE_ENGINE_DISK_TYPE_STANDARD. `DISK_TYPE` must be one of: 

`compute-engine-disk-type-balanced`
     Compute Engine Disk Type Balanced. 
`compute-engine-disk-type-hyperdisk-balanced`
     Compute Engine Disk Type hyperdisk-balanced. 
`compute-engine-disk-type-ssd`
     Compute Engine Disk Type SSD. 
`compute-engine-disk-type-standard`
     Compute Engine Disk Type Standard. 
`--kms-key`=`KMS_KEY`
     Fully qualified identifier for the Cloud KMS (Key Management Service) cryptokey that will be used to protect the disk. 
`--labels`=[`KEY`=`VALUE`,…]
     A map of labels to associate with the disk. 
`--target-project`=`TARGET_PROJECT`
     The target project resource path to which the disk will be migrated. Default is the host project. To get a list of the target projects run the gcloud alpha migration vms target-projects list command. 
`--zone`=`ZONE`
     The zone in which to create the disk. The default value is the first zone of the Google Cloud location parameter given. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vmmigration/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/migrate/virtual-machines>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
