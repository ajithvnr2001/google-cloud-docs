---
url: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update/
title: gcloud netapp storage-pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:38:02.306533+00:00
---

# gcloud netapp storage-pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud netapp storage-pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud netapp storage-pools update - update a Cloud NetApp Storage Pool 
SYNOPSIS
    

`gcloud netapp storage-pools update` (`STORAGE_POOL` : `--location`=`LOCATION`) [`--active-directory`=`ACTIVE_DIRECTORY`] [`--allow-auto-tiering`=`ALLOW_AUTO_TIERING`] [`--async`] [`--capacity`=`CAPACITY`] [`--description`=`DESCRIPTION`] [`--qos-type`=`QOS_TYPE`] [`--replica-zone`=`REPLICA_ZONE`] [`--total-iops`=`TOTAL_IOPS`] [`--total-throughput`=`TOTAL_THROUGHPUT`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--zone`=`ZONE`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Updates a Storage Pool with given arguments 
EXAMPLES
     The following command updates a Storage Pool named NAME in the given location 
    
    
    gcloud netapp storage-pools update NAME --location=us-central1 --capacity=4096 --active-directory=ad-2 --description="new description" --update-labels=key1=val1

POSITIONAL ARGUMENTS
    

Storage pool resource - The Storage Pool to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

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
`--capacity`=`CAPACITY`
     The desired capacity of the Storage Pool in GiB or TiB units.If no capacity unit is specified, GiB is assumed. 
`--description`=`DESCRIPTION`
     A description of the Cloud NetApp Storage Pool 
`--qos-type`=`QOS_TYPE`
     Quality of service (QoS) type for the Storage Pool. `QOS_TYPE` must be one of: `auto`, `manual`, `qos-type-unspecified`. 
`--replica-zone`=`REPLICA_ZONE`
     String indicating replica zone for the Storage Pool 
`--total-iops`=`TOTAL_IOPS`
     Integer indicating total IOPS of the Storage Pool 
`--total-throughput`=`TOTAL_THROUGHPUT`
     The total throughput of the Storage Pool in MiB/s or GiB/s units. If no throughput unit is specified, MiB/s is assumed. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--zone`=`ZONE`
     String indicating active zone of the Storage Pool 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud netapp storage-pools update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud netapp storage-pools update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha netapp storage-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/storage-pools/update)
    
    
    [gcloud beta netapp storage-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/storage-pools/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
