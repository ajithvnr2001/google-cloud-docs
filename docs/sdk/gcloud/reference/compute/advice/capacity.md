---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/advice/capacity/
title: gcloud compute advice capacity \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:07:55.425184+00:00
---

# gcloud compute advice capacity  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/advice/capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute advice capacity Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute advice capacity - get capacity advice for Compute Engine resources 
SYNOPSIS
    

`gcloud compute advice capacity` `--provisioning-model`=`PROVISIONING_MODEL` `--size`=`SIZE` `--target-distribution-shape`=`TARGET_DISTRIBUTION_SHAPE` (`--instance-flexibility-policy`=[`INSTANCE_FLEXIBILITY_POLICY`,…] | `--instance-selection`=`INSTANCE_SELECTION` `--instance-selection-machine-types`=[`MACHINE_TYPE`,…]) [`--accelerator-topology`=`ACCELERATOR_TOPOLOGY`] [`--max-run-duration`=`MAX_RUN_DURATION`] [`--region`=`REGION`] [`--zones`=[`ZONE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Get capacity advice for Compute Engine resources. 

This command helps you view future resource availability for a specific number of VM instances, machine type, provisioning model, and zone. After you confirm resource availability, you can specify those configurations when you create VM instances. This action improves the success rate of your VM instance creation request. 

EXAMPLES
     To check the availability of 100 `n2-standard-32` Spot VMs in any single zone in the `us-central1` region, run the following command: 
    
    
    gcloud compute advice capacity --region="us-central1" --provisioning-model="SPOT" --size=100 --instance-selection-machine-types="n2-standard-32" --target-distribution-shape="any-single-zone"

To check the availability of 50 Spot VMs, allowing either `e2-standard-8` or `e2-standard-16` machine types, distributed across `us-central1-a` and `us-central1-b`, run the following command: 
    
    
    gcloud compute advice capacity --region="us-central1" --provisioning-model="SPOT" --size=50 --instance-selection="name=my-selection,machine-type=e2-standard-8,machine-type=e2-standard-16" --target-distribution-shape="any" --zones="us-central1-a,us-central1-b"

To check the availability of 10 `ct5lp-hightpu-4t` Flex-start VMs that will run for 1 day in any single zone in the `us-central1` region, run the following command: 
    
    
    gcloud compute advice capacity --region="us-central1" --provisioning-model="FLEX_START" --max-run-duration=1d --size=10 --instance-selection-machine-types="ct5lp-hightpu-4t" --target-distribution-shape="any-single-zone" --accelerator-topology="2x2"

REQUIRED FLAGS
    

`--provisioning-model`=`PROVISIONING_MODEL`
     Specifies the provisioning model. `PROVISIONING_MODEL` must be one of: 

`FLEX_START`
     Compute Engine will attempt to allocate the requested capacity within a specific time frame. If it succeeds, the VMs will start running and keep running for a maximum of 7 days. 
`SPOT`
     Compute Engine may preempt a Spot VM whenever it needs capacity. Because Spot VMs don't have a guaranteed runtime, they come at a discounted price. 
`--size`=`SIZE`
     The total number of VMs being requested in the capacity query. 
`--target-distribution-shape`=`TARGET_DISTRIBUTION_SHAPE`
     Defines the distribution requirement for the requested VMs. `TARGET_DISTRIBUTION_SHAPE` must be one of: 

`ANY`
     When you specify ANY for VM instance creation across multiple zones, you specify that you want to create your VM instances in one or more zones based on resource availability. 
`ANY_SINGLE_ZONE`
     When you specify ANY_SINGLE_ZONE for VM instance creation, you specify that you want to create all VM instances in a single available zone. Compute Engine selects this zone based on resource availability and on any unused, matching reservation in your project. However, zonal resource availability constraints might prevent Compute Engine from creating all your requested VM instances. Use ANY_SINGLE_ZONE when the VM instances in your workloads need to frequently communicate among each other. 
`BALANCED`
     Prioritizes provisioning VMs in zones where resources are available. Compute Engine then distributes VMs as evenly as possible across zones. If resources are unavailable in one or more zones, then the actual distribution might be uneven. Use BALANCED to minimize the impact of zonal failures. 
Specifies the machine types for which advice is being sought. 

Exactly one of these must be specified: 

`--instance-flexibility-policy`=[`INSTANCE_FLEXIBILITY_POLICY`,…]
     Specifies the instance flexibility policy. This policy lets you define one or more named selections of machine types for which capacity advice is sought. Within each selection, you can list your preferred machine types, assign an optional rank to indicate priority (lower rank values are considered higher priority), and specify additional instance properties, such as minimum CPU platform and disk configurations. 
Or at least one of these can be specified: 

`--instance-selection`=`INSTANCE_SELECTION`
     Named selection of machine types. For example, \--instance-selection="name=instance-selection-1,machine-type=e2-standard-8,machine-type=t2d-standard-8". 
`--instance-selection-machine-types`=[`MACHINE_TYPE`,…]
     Specifies a comma-separated list of preferred machine types for creating virtual machines. 
OPTIONAL FLAGS
    

`--accelerator-topology`=`ACCELERATOR_TOPOLOGY`
     Topology required to create a partition for VMs that have interconnected GPUs or TPUs. For example, `2x2` for `ct5l-hightpu-4t`. 
`--max-run-duration`=`MAX_RUN_DURATION`
     Maximum duration for which the requested VMs can run. This flag must be used when the requested provisioning model is `FLEX_START`. 

The duration is formatted as the number of days, hours, minutes, and seconds followed by d, h, m, and s respectively. For example, specify `30m` for a duration of 30 minutes or specify `1d2h3m4s` for a duration of 1 day, 2 hours, 3 minutes, and 4 seconds. 

`--region`=`REGION`
     Region of the resources to get advice on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zones`=[`ZONE`,…]
     A comma-separated list of zones to query within the specified region, for example, `us-central1-a,us-central1-b`. If you omit this flag, then you view availability for your requested capacity across all zones in the region. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute advice capacity](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/advice/capacity)
    
    
    [gcloud beta compute advice capacity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/advice/capacity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
