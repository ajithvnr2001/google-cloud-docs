---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/advice/calendar-mode/
title: gcloud preview compute advice calendar-mode \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:38.349642+00:00
---

# gcloud preview compute advice calendar-mode  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/advice/calendar-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute advice calendar-mode Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute advice calendar-mode - recommends the optimal time window and zone for Future Reservations 
SYNOPSIS
    

`gcloud preview compute advice calendar-mode` ([`--chip-count`=`CHIP_COUNT` `--tpu-version`=`TPU_VERSION` : `--workload-type`=`WORKLOAD_TYPE`] | [`--machine-type`=`MACHINE_TYPE` `--vm-count`=`VM_COUNT` : `--local-ssd`=[`interface`=`INTERFACE`],[`size`=`SIZE`]]) [`--duration-range`=[`max`=`MAX`],[`min`=`MIN`]] [`--location-policy`=[`ZONE`=`POLICY`,…]] [`--region`=`REGION`] [`--start-time-range`=[`from`=`FROM`],[`to`=`TO`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Recommends the optimal time window and zone for Future Reservations. 
EXAMPLES
     To request an advice for a future reservation of 8 a3-highgpu-8g VMs, run: 
    
    
    gcloud preview compute advice calendar-mode --region=fake-region --machine-type=a3-megagpu-8g --vm-count=8 --duration-range=min=7d,max=14d --start-time-range=from=2025-02-20,to=2025-03-25

To request advice for a future reservation of 512 v5e TPUs, run: 
    
    
    gcloud preview compute advice calendar-mode --region=fake-region --location-policy=fake-zone-1=DENY,fake-zone-2=ALLOW --tpu-version=V5E --chip-count=16 --workload-type=BATCH --duration-range=min=30d,max=90d --start-time-range=from=2025-02-25,to=2025-06-25

REQUIRED FLAGS
    
    
    
    Specify the properties of the resources that you want to view the availability of.

Exactly one of these must be specified: 
    
    
    You must define the version and number of TPUs to reserve.

`--chip-count`=`CHIP_COUNT`
     The number of chips to check for availability. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--tpu-version`=`TPU_VERSION`
     The version of Cloud TPU to reserve. `TPU_VERSION` must be one of: 

`TPU7X`
     Cloud TPU v7x 
`V5E`
     Cloud TPU v5e Lite 
`V5P`
     Cloud TPU v5p 
`V6E`
     Cloud TPU v6e 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--workload-type`=`WORKLOAD_TYPE`
     Type of the workload that will be running on the reserved TPUs. `WORKLOAD_TYPE` must be one of: 

`BATCH`
     Reserved resources will be optimized for BATCH workloads that handle large amounts of data in single or multiple operations, such as ML training workloads. 
`SERVING`
     Reserved resources will be optimized for SERVING workloads that handle concurrent requests and require minimal network latency, such as ML inference. 
    
    
    Define individual instance properties for the specific SKU reservation.

`--machine-type`=`MACHINE_TYPE`
     The type of machine (name only) that has a fixed number of vCPUs and a fixed amount of memory. You can also specify a custom machine type by using the pattern `custom-number_of_CPUs-amount_of_memory`-for example, `custom-32-29440`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--vm-count`=`VM_COUNT`
     The number of instances to check for availability. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--local-ssd`=[`interface`=`INTERFACE`],[`size`=`SIZE`]
     Manage the size and the interface of local SSD to use. See <https://cloud.google.com/compute/docs/disks/local-ssd> for more information. 

`interface`
     The kind of disk interface exposed to the VM for this SSD. The only valid value is `nvme`. 
`size`
     The size of the local SSD in base-2 GB. 
OPTIONAL FLAGS
    

`--duration-range`=[`max`=`MAX`],[`min`=`MIN`]
     A duration range for the duration of the Future Reservation. Defined as a list of key-value pairs. 

The key is either "min" or "max", and the value is a duration in seconds. For example, specify `30m` for a duration of 30 minutes or specify `1d2h3m4s` for a duration of 1 day, 2 hours, 3 minutes, and 4 seconds. 

See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 

`min`
     The minimum duration of the Future Reservation. 
`max`
     The maximum duration of the Future Reservation. 

Example: 
    
    
    gcloud compute advice calendar-mode --duration-range=min=24h,max=72h

`--location-policy`=[`ZONE`=`POLICY`,…]
     Policy for which zones to include or exclude when looking for the optimal time window and zone for Future Reservations within a region. Policy is defined as a list of key-value pairs, with the key being the zone name, and value being the applied policy. Available policies are `allow` and `deny`. Default for zones if left unspecified is `allow`. 

Example: 
    
    
    gcloud compute advice calendar-mode --location-policy=us-central1-a=allow,us-central1-b=deny

`--region`=`REGION`
     Region of the resources to get advice on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--start-time-range`=[`from`=`FROM`],[`to`=`TO`]
     A time range for the start time of the Future Reservation. Defined as a list of key-value pairs. 

The key is either "from" or "to", and the value is a datetime. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 

`from`
     The earliest possible start time for the reservation. 
`to`
     The latest possible start time for the reservation. 

Example: 
    
    
    gcloud compute advice calendar-mode --start-time-range=from=2024-08-01T00:00:00Z,to=2024-08-02T00:00:00Z

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute advice calendar-mode](https://docs.cloud.google.com/sdk/gcloud/reference/compute/advice/calendar-mode)
    
    
    [gcloud alpha compute advice calendar-mode](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/advice/calendar-mode)
    
    
    [gcloud beta compute advice calendar-mode](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/advice/calendar-mode)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
