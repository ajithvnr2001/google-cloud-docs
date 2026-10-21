---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/storage-pools/create/
title: gcloud beta compute storage-pools create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:49:26.638821+00:00
---

# gcloud beta compute storage-pools create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/storage-pools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute storage-pools create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute storage-pools create - create a storage pool 
SYNOPSIS
    

`gcloud beta compute storage-pools create` `STORAGE_POOL` `--provisioned-capacity`=`PROVISIONED_CAPACITY` `--storage-pool-type`=`STORAGE_POOL_TYPE` [`--async`] [`--capacity-provisioning-type`=`CAPACITY_PROVISIONING_TYPE`] [`--description`=`DESCRIPTION`] [`--performance-provisioning-type`=`PERFORMANCE_PROVISIONING_TYPE`] [`--provisioned-iops`=`PROVISIONED_IOPS`] [`--provisioned-throughput`=`PROVISIONED_THROUGHPUT`] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a storage pool. 
EXAMPLES
     To create a new storage pool named `my-storage-pool`, run the following command: 
    
    
    gcloud beta compute storage-pools create my-storage-pool --storage-pool-type=hyperdisk-throughput --provisioned-capacity=10TB --provisioned-throughput=200

POSITIONAL ARGUMENTS
    

Storage pool resource - The name of the storage pool you want to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `storage_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `zone` attribute: 

  * provide the argument `storage_pool` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * set the property `compute/zone`. 



This must be specified. 

`STORAGE_POOL`
     ID of the storage pool or fully qualified identifier for the storage pool. 

To set the `storage_pool` attribute: 

  * provide the argument `storage_pool` on the command line. 


REQUIRED FLAGS
    

`--provisioned-capacity`=`PROVISIONED_CAPACITY`
     Provisioned capacity of the storage pool. 
Storage pool type resource - Type of the storage pool. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--storage-pool-type` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `zone` attribute: 

  * provide the argument `--storage-pool-type` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * set the property `compute/zone`. 



This must be specified. 

`--storage-pool-type`=`STORAGE_POOL_TYPE`
     ID of the storage pool type or fully qualified identifier for the storage pool type. 

To set the `storage-pool-type` attribute: 

  * provide the argument `--storage-pool-type` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--capacity-provisioning-type`=`CAPACITY_PROVISIONING_TYPE`
     Capacity provisioning type. `CAPACITY_PROVISIONING_TYPE` must be one of: `advanced`, `standard`. 
`--description`=`DESCRIPTION`
     Description of the storage pool. 
`--performance-provisioning-type`=`PERFORMANCE_PROVISIONING_TYPE`
     Performance provisioning type. `PERFORMANCE_PROVISIONING_TYPE` must be one of: `advanced`, `standard`. 
`--provisioned-iops`=`PROVISIONED_IOPS`
     IOPS with which to provision the pool. 
`--provisioned-throughput`=`PROVISIONED_THROUGHPUT`
     Throughput in MB/s with which to provision the pool. 
`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     Resource manager tags to be bound to the storage pool. 
`--zone`=`ZONE`
     For resources [storage-pool-type, storage_pool], provides fallback value for resource zone attribute. When the resource's full URI path is not provided, zone will fallback to this flag value. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/beta` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute storage-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create)
    
    
    [gcloud alpha compute storage-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/storage-pools/create)
    
    
    [gcloud preview compute storage-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/storage-pools/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
