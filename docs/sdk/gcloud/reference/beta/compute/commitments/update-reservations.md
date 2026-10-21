---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/commitments/update-reservations/
title: gcloud beta compute commitments update-reservations \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:39.067110+00:00
---

# gcloud beta compute commitments update-reservations  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/commitments/update-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute commitments update-reservations Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute commitments update-reservations - update the resource shape of reservations within the commitment 
SYNOPSIS
    

`gcloud beta compute commitments update-reservations` `COMMITMENT` [`--region`=`REGION`] [`--reservations-from-file`=`PATH_TO_FILE` | [`--dest-reservation`=[`machine-type`=`MACHINE-TYPE`],[`min-cpu-platform`=`MIN-CPU-PLATFORM`],[`require-specific-reservation`=`REQUIRE-SPECIFIC-RESERVATION`],[`reservation`=`RESERVATION`],[`reservation-zone`=`RESERVATION-ZONE`],[`vm-count`=`VM-COUNT`] `--source-reservation`=[`machine-type`=`MACHINE-TYPE`],[`min-cpu-platform`=`MIN-CPU-PLATFORM`],[`require-specific-reservation`=`REQUIRE-SPECIFIC-RESERVATION`],[`reservation`=`RESERVATION`],[`reservation-zone`=`RESERVATION-ZONE`],[`vm-count`=`VM-COUNT`] : `--dest-accelerator`=[`count`=`COUNT`],[`type`=`TYPE`] `--dest-local-ssd`=[`interface`=`INTERFACE`],[`size`=`SIZE`] `--dest-share-setting`=`DEST_SHARE_SETTING` `--dest-share-with`=`SHARE_WITH`,[`SHARE_WITH`,…] `--source-accelerator`=[`count`=`COUNT`],[`type`=`TYPE`] `--source-local-ssd`=[`interface`=`INTERFACE`],[`size`=`SIZE`] `--source-share-setting`=`SOURCE_SHARE_SETTING` `--source-share-with`=`SHARE_WITH`,[`SHARE_WITH`,…]]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update the resource shape of reservations within the commitment. 
EXAMPLES
     To update reservations of the commitment called ``commitment-1`` in the ``us-central1`` region with values from ``reservations.yaml``, run: 
    
    
    gcloud beta compute commitments update-reservations commitment-1 --reservations-from-file=reservations.yaml

For detailed examples, please refer to <https://cloud.google.com/compute/docs/instances/reserving-zonal-resources#modifying_reservations_that_are_attached_to_commitments>

POSITIONAL ARGUMENTS
    

`COMMITMENT`
     Name of the commitment to update reservation. 
FLAGS
    

`--region`=`REGION`
     Region of the commitment to update reservation. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

Manage reservations that are attached to the commitment. 

At most one of these can be specified: 

`--reservations-from-file`=`PATH_TO_FILE`
     Path to a YAML file of two reservations' configuration. Use a full or relative path to a local file containing the value of reservations. 
Or at least one of these can be specified: 

Specify source and destination reservations configuration. 
`--dest-reservation`=[`machine-type`=`MACHINE-TYPE`],[`min-cpu-platform`=`MIN-CPU-PLATFORM`],[`require-specific-reservation`=`REQUIRE-SPECIFIC-RESERVATION`],[`reservation`=`RESERVATION`],[`reservation-zone`=`RESERVATION-ZONE`],[`vm-count`=`VM-COUNT`]
     destination reservation configuration. 

`reservation`
     Name of the destination reservation to operate on. 
`reservation-zone`
     Zone of the destination reservation to operate on. 
`vm-count`
     The number of VM instances that are allocated to this reservation. The value of this field must be an int in the range [1, 1000]. 
`machine-type`
     The type of machine (name only) which has a fixed number of vCPUs and a fixed amount of memory. This also includes specifying custom machine type following `custom-number_of_CPUs-amount_of_memory` pattern, e.g. `custom-32-29440`. 
`min-cpu-platform`
     Optional minimum CPU platform of the reservation to create. 
`require-specific-reservation`
     Indicates whether the reservation can be consumed by VMs with "any reservation" defined. If enabled, then only VMs that target this reservation by name using `--reservation-affinity=specific` can consume from this reservation. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--source-reservation`=[`machine-type`=`MACHINE-TYPE`],[`min-cpu-platform`=`MIN-CPU-PLATFORM`],[`require-specific-reservation`=`REQUIRE-SPECIFIC-RESERVATION`],[`reservation`=`RESERVATION`],[`reservation-zone`=`RESERVATION-ZONE`],[`vm-count`=`VM-COUNT`]
     source reservation configuration. 

`reservation`
     Name of the source reservation to operate on. 
`reservation-zone`
     Zone of the source reservation to operate on. 
`vm-count`
     The number of VM instances that are allocated to this reservation. The value of this field must be an int in the range [1, 1000]. 
`machine-type`
     The type of machine (name only) which has a fixed number of vCPUs and a fixed amount of memory. This also includes specifying custom machine type following `custom-number_of_CPUs-amount_of_memory` pattern, e.g. `custom-32-29440`. 
`min-cpu-platform`
     Optional minimum CPU platform of the reservation to create. 
`require-specific-reservation`
     Indicates whether the reservation can be consumed by VMs with "any reservation" defined. If enabled, then only VMs that target this reservation by name using `--reservation-affinity=specific` can consume from this reservation. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--dest-accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]
     Manage the configuration of the type and number of accelerator cards attached. 

`count`
     The number of accelerators to attach to each instance in the reservation. 
`type`
     The specific type (e.g. `nvidia-tesla-k80` for nVidia Tesla K80) of accelerator to attach to instances in the reservation. Use `[gcloud compute accelerator-types list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/accelerator-types/list)` to learn about all available accelerator types. 
`--dest-local-ssd`=[`interface`=`INTERFACE`],[`size`=`SIZE`]
     Manage the size and the interface of local SSD to use. See <https://cloud.google.com/compute/docs/disks/local-ssd> for more information. 

`interface`
     The kind of disk interface exposed to the VM for this SSD. Valid values are `scsi` and `nvme`. SCSI is the default and is supported by more guest operating systems. NVME may provide higher performance. 
`size`
     The size of the local SSD in base-2 GB. 
`--dest-share-setting`=`DEST_SHARE_SETTING`
     The projects that can use the reservation. `DEST_SHARE_SETTING` must be one of: 

`local`
     Only your project can use the reservation. This is the default value. 
`projects`
     Your project and up to 100 other projects within your project's organization can use the reservation. If you specify this value, then you must also include the \--share-with flag in the command. 
`--dest-share-with`=`SHARE_WITH`,[`SHARE_WITH`,…]
     If this reservation is shared (--share-setting=projects), then specify a comma-separated list of projects to share the reservation with. List projects using project IDs or project numbers. 
`--source-accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]
     Manage the configuration of the type and number of accelerator cards attached. 

`count`
     The number of accelerators to attach to each instance in the reservation. 
`type`
     The specific type (e.g. `nvidia-tesla-k80` for nVidia Tesla K80) of accelerator to attach to instances in the reservation. Use `[gcloud compute accelerator-types list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/accelerator-types/list)` to learn about all available accelerator types. 
`--source-local-ssd`=[`interface`=`INTERFACE`],[`size`=`SIZE`]
     Manage the size and the interface of local SSD to use. See <https://cloud.google.com/compute/docs/disks/local-ssd> for more information. 

`interface`
     The kind of disk interface exposed to the VM for this SSD. Valid values are `scsi` and `nvme`. SCSI is the default and is supported by more guest operating systems. NVME may provide higher performance. 
`size`
     The size of the local SSD in base-2 GB. 
`--source-share-setting`=`SOURCE_SHARE_SETTING`
     The projects that can use the reservation. `SOURCE_SHARE_SETTING` must be one of: 

`local`
     Only your project can use the reservation. This is the default value. 
`projects`
     Your project and up to 100 other projects within your project's organization can use the reservation. If you specify this value, then you must also include the \--share-with flag in the command. 
`--source-share-with`=`SHARE_WITH`,[`SHARE_WITH`,…]
     If this reservation is shared (--share-setting=projects), then specify a comma-separated list of projects to share the reservation with. List projects using project IDs or project numbers. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha compute commitments update-reservations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
