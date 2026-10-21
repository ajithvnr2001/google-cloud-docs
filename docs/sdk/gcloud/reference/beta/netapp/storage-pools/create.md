---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/storage-pools/create/
title: gcloud beta netapp storage-pools create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:53.214498+00:00
---

# gcloud beta netapp storage-pools create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/storage-pools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta netapp storage-pools create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta netapp storage-pools create - create a Cloud NetApp Storage Pool 
SYNOPSIS
    

`gcloud beta netapp storage-pools create` (`STORAGE_POOL` : `--location`=`LOCATION`) `--capacity`=`CAPACITY` `--network`=[`name`=`NAME`],[`psa-range`=`PSA-RANGE`] `--service-level`=`SERVICE_LEVEL` [`--active-directory`=`ACTIVE_DIRECTORY`] [`--allow-auto-tiering`=`ALLOW_AUTO_TIERING`] [`--async`] [`--custom-performance-enabled`=`CUSTOM_PERFORMANCE_ENABLED`] [`--description`=`DESCRIPTION`] [`--enable-hot-tier-auto-resize`=`ENABLE_HOT_TIER_AUTO_RESIZE`] [`--enable-ldap`=`ENABLE_LDAP`] [`--hot-tier-size`=`HOT_TIER_SIZE`] [`--kms-config`=`KMS_CONFIG`] [`--labels`=[`KEY`=`VALUE`,…]] [`--mode`=`MODE`] [`--qos-type`=`QOS_TYPE`] [`--replica-zone`=`REPLICA_ZONE`] [`--scale-tier`=`SCALE_TIER`] [`--scale-type`=`SCALE_TYPE`] [`--total-iops`=`TOTAL_IOPS`] [`--total-throughput`=`TOTAL_THROUGHPUT`] [`--type`=`TYPE`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Creates a Storage Pool to contain Volumes with a specified Service Level and capacity. 
EXAMPLES
     The following command creates a Storage Pool named NAME using all possible arguments with a VPC network in the same project 
    
    
    gcloud beta netapp storage-pools create NAME --location=us-central1 --service-level=standard --capacity=2048 --network=name=default --active-directory=ad1 --kms-config=kms-config1 --enable-ldap=true --description="example description"

The following command creates a Storage pool named NAME using all possible arguments with a shared VPC network in a separate project called VPC_PROJECT 
    
    
    gcloud beta netapp storage-pools create NAME --location=us-central1 --service-level=standard --capacity=2048 --network=name=projects/VPC_PROJECT/locations/us-central1/networks/default --active-directory=ad1 --kms-config=kms-config1 --enable-ldap=true --description="example description"

POSITIONAL ARGUMENTS
    

Storage pool resource - The Storage Pool to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `storage_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`STORAGE_POOL`
     ID of the storage_pool or fully qualified identifier for the storage_pool. 

To set the `storage_pool` attribute: 

  * provide the argument `storage_pool` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the storage_pool. 

To set the `location` attribute: 

  * provide the argument `storage_pool` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


REQUIRED FLAGS
    

`--capacity`=`CAPACITY`
     The desired capacity of the Storage Pool in GiB or TiB units.If no capacity unit is specified, GiB is assumed. 
`--network`=[`name`=`NAME`],[`psa-range`=`PSA-RANGE`]
     Network configuration for a Cloud NetApp Files Storage Pool. Specifying `psa-range` is optional. 

`name`
     The name of the Google Compute Engine [VPC network](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the volume is connected. Short-form (VPC network ID) or long-form (full VPC network name: projects/PROJECT/locations/LOCATION/networks/NETWORK) are both accepted, but please use the long-form when attempting to create a Storage Pool using a shared VPC. 
`psa-range`
     This field is not implemented. The values provided in this field are ignored. 
`--service-level`=`SERVICE_LEVEL`
     The service level for the Cloud NetApp Storage Pool. For more details, see: <https://cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview#service_levels>

`SERVICE_LEVEL` must be one of: 

`extreme`
     Extreme Service Level for Cloud NetApp Storage Pool. The Extreme Service Level has a throughput per GiB of allocated volume size of 128 KiB/s. 
`flex`
     Flex Service Level for Cloud NetApp Storage Pool. The Flex Service Level has a throughput per GiB of allocated volume size of 16 KiB/s. 
`premium`
     Premium Service Level for Cloud NetApp Storage Pool. The Premium Service Level has a throughput per GiB of allocated volume size of 64 KiB/s. 
`standard`
     Standard Service Level for Cloud NetApp Storage Pool. The Standard Service Level has a throughput per GiB of allocated volume size of 16 KiB/s. 
OPTIONAL FLAGS
    

Active directory resource - The Active Directory to attach to the Storage Pool. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--active-directory` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--active-directory` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


`--active-directory`=`ACTIVE_DIRECTORY`
     ID of the active_directory or fully qualified identifier for the active_directory. 

To set the `active_directory` attribute: 

  * provide the argument `--active-directory` on the command line. 


`--allow-auto-tiering`=`ALLOW_AUTO_TIERING`
     Boolean flag indicating whether Storage Pool is allowed to use auto-tiering 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--custom-performance-enabled`=`CUSTOM_PERFORMANCE_ENABLED`
     Boolean flag indicating whether Storage Pool is a custom performance Storage Pool or not 
`--description`=`DESCRIPTION`
     A description of the Cloud NetApp Storage Pool 
`--enable-hot-tier-auto-resize`=`ENABLE_HOT_TIER_AUTO_RESIZE`
     Boolean flag indicating whether Storage Pool is allowed to use hot tier auto resize 
`--enable-ldap`=`ENABLE_LDAP`
     Boolean flag indicating whether Storage Pool is a NFS LDAP Storage Pool or not 
`--hot-tier-size`=`HOT_TIER_SIZE`
     The hot tier size of the Storage Pool in GiB units. This is a required field when --allow-auto-tiering is set for flex service level. 
Kms config resource - The KMS config to attach to the Storage Pool. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--kms-config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--kms-config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


`--kms-config`=`KMS_CONFIG`
     ID of the kms_config or fully qualified identifier for the kms_config. 

To set the `kms_config` attribute: 

  * provide the argument `--kms-config` on the command line. 


`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--mode`=`MODE`
     The mode of the Storage Pool. `ONTAP` mode is for performing ONTAP operations with ONTAP Mode APIs. `DEFAULT` mode is for performing operations allowed with NetApp Files APIs. `MODE` must be one of: `default`, `ontap`. 
`--qos-type`=`QOS_TYPE`
     Quality of service (QoS) type for the Storage Pool. `QOS_TYPE` must be one of: `auto`, `manual`, `qos-type-unspecified`. 
`--replica-zone`=`REPLICA_ZONE`
     String indicating replica zone for the Storage Pool 
`--scale-tier`=`SCALE_TIER`
     (DEPRECATED) The scale tier of the Storage Pool. `standard` scale tier is for standard capacity and performance tier. `enterprise` scale tier is for higher capacity and performance tier. 

The `--scale-tier` flag is deprecated. Use `--scale-type` instead. `SCALE_TIER` must be one of: `enterprise`, `standard`. 

`--scale-type`=`SCALE_TYPE`
     The scale type of the Storage Pool. `default` scale type is for standard capacity and performance. `scaleout` scale type is for higher capacity and performance. `SCALE_TYPE` must be one of: `default`, `scaleout`. 
`--total-iops`=`TOTAL_IOPS`
     Integer indicating total IOPS of the Storage Pool 
`--total-throughput`=`TOTAL_THROUGHPUT`
     The total throughput of the Storage Pool in MiB/s or GiB/s units. If no throughput unit is specified, MiB/s is assumed. 
`--type`=`TYPE`
     The type of the Storage Pool. `FILE` pools support file-based volumes only. `UNIFIED` pools support both file and block volumes. `TYPE` must be one of: 

`file`
     File-based volumes only (default). 
`unified`
     Both file and block volumes. 
`--zone`=`ZONE`
     String indicating active zone of the Storage Pool 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud netapp storage-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/create)
    
    
    [gcloud alpha netapp storage-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/storage-pools/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
