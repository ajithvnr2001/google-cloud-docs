---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reservations/create/
title: gcloud preview compute reservations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:41:45.536045+00:00
---

# gcloud preview compute reservations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reservations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute reservations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute reservations create - create a Compute Engine reservation 
SYNOPSIS
    

`gcloud preview compute reservations create` `RESERVATION` (`--vm-count`=`VM_COUNT` (`--source-instance-template`=`SOURCE_INSTANCE_TEMPLATE` | [`--machine-type`=`MACHINE_TYPE` : `--accelerator`=[`count`=`COUNT`],[`type`=`TYPE`] `--local-ssd`=[`count`=`COUNT`],[`interface`=`INTERFACE`],[`size`=`SIZE`] `--min-cpu-platform`=`MIN_CPU_PLATFORM`]) : `--require-specific-reservation` `--resource-policies`=[`KEY`=`VALUE`,…]) [`--description`=`DESCRIPTION`] [`--reservation-sharing-policy`=`RESERVATION_SHARING_POLICY`] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--zone`=`ZONE`] [`--share-setting`=`SHARE_SETTING` `--share-with`=`SHARE_WITH`,[`SHARE_WITH`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Create a Compute Engine reservation. 
EXAMPLES
     To create a Compute Engine reservation by specifying VM properties using an instance template, run: 
    
    
    gcloud preview compute reservations create my-reservation --vm-count=1 --source-instance-template=example-instance-template --zone=fake-zone

To create a Compute Engine reservation by directly specifying VM properties, run: 
    
    
    gcloud preview compute reservations create my-reservation --vm-count=1 --machine-type=custom-8-10240 --min-cpu-platform="Intel Haswell" --accelerator=count=2,type=nvidia-tesla-v100 --local-ssd=size=375,interface=scsi --zone=fake-zone

POSITIONAL ARGUMENTS
    

`RESERVATION`
     Name of the reservation to create. 
REQUIRED FLAGS
    

Manage the SpecificSKU reservation properties. 

This must be specified. 

`--vm-count`=`VM_COUNT`
     The number of VM instances that are allocated to this reservation. The value of this field must be an int in the range [1, 1000]. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--require-specific-reservation`
     Indicates whether the reservation can be consumed by VMs with "any reservation" defined. If enabled, then only VMs that target this reservation by name using `--reservation-affinity=specific` can consume from this reservation. 
`--resource-policies`=[`KEY`=`VALUE`,…]
     The resource policies to include in this reservation. If you omit this flag, no resource policies are added. You can specify any string as the key, and specify the name of a resource policy as the value. 
Manage the instance properties for the SpecificSKU reservation. 

Exactly one of these must be specified: 

`--source-instance-template`=`SOURCE_INSTANCE_TEMPLATE`
     The url of the instance template that will be used to populate the fields of the reservation. Instance properties can not be defined in addition to source instance template. 
Or at least one of these can be specified: 

Define the individual instance properties for the SpecificSKU reservation. 
`--machine-type`=`MACHINE_TYPE`
     The type of machine (name only) that has a fixed number of vCPUs and a fixed amount of memory. You can also specify a custom machine type by using the pattern `custom-number_of_CPUs-amount_of_memory`-for example, `custom-32-29440`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]
     Manage the configuration of the type and number of accelerator cards attached. 

`count`
     The number of accelerators to attach to each instance in the reservation. 
`type`
     The specific type (e.g. `nvidia-tesla-k80` for nVidia Tesla K80) of accelerator to attach to instances in the reservation. Use `[gcloud compute accelerator-types list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/accelerator-types/list)` to learn about all available accelerator types. 
`--local-ssd`=[`count`=`COUNT`],[`interface`=`INTERFACE`],[`size`=`SIZE`]
     Manage the size and the interface of local SSD to use. See <https://cloud.google.com/compute/docs/disks/local-ssd> for more information. 

`interface`
     The kind of disk interface exposed to the VM for this SSD. Valid values are `scsi` and `nvme`. SCSI is the default and is supported by more guest operating systems. NVME may provide higher performance. 
`size`
     The size of the local SSD in base-2 GB. 
`count`
     The number of local SSD to use per VM. If you don't specify this argument, then the default value is 1. 
`--min-cpu-platform`=`MIN_CPU_PLATFORM`
     Optional minimum CPU platform of the reservation to create. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional description of the reservation to create. 
`--reservation-sharing-policy`=`RESERVATION_SHARING_POLICY`
     The reservation sharing policy to use for this reservation. `RESERVATION_SHARING_POLICY` must be one of: 

`ALLOW_ALL`
     The reservation can be shared with Google Cloud services. 
`DISALLOW_ALL`
     The reservation won't be shared with Google Cloud services. If you omit this flag during creation, the default value is DISALLOW_ALL. 
`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     Resource manager tags to be bound to the reservation. 
`--zone`=`ZONE`
     Zone of the reservation to create. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

Manage the properties of a shared reservation. 
`--share-setting`=`SHARE_SETTING`
     The projects that can use the reservation. `SHARE_SETTING` must be one of: 

`local`
     Only your project can use the reservation. This is the default value. 
`projects`
     Your project and up to 100 other projects within your project's organization can use the reservation. If you specify this value, then you must also include the \--share-with flag in the command. 
`--share-with`=`SHARE_WITH`,[`SHARE_WITH`,…]
     If this reservation is shared (--share-setting=projects), then specify a comma-separated list of projects to share the reservation with. List projects using project IDs or project numbers. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute reservations create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create)
    
    
    [gcloud alpha compute reservations create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations/create)
    
    
    [gcloud beta compute reservations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
