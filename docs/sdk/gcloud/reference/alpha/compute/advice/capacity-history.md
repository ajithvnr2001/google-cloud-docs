---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/advice/capacity-history/
title: gcloud alpha compute advice capacity-history \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:38.519879+00:00
---

# gcloud alpha compute advice capacity-history  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/advice/capacity-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute advice capacity-history Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute advice capacity-history - show historical data on Spot VMs preemption and price 
SYNOPSIS
    

`gcloud alpha compute advice capacity-history` `--machine-type`=`MACHINE_TYPE` `--provisioning-model`=`PROVISIONING_MODEL` `--types`=`HISTORY_TYPE`,[…] (`--region`=`REGION` | `--zone`=`ZONE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Show historical data on Spot VMs preemption and price. 

Use this command to retrieve historical data on Spot VM preemption and price for a specific machine type and location. By analyzing historical trends, you can choose configurations for creating new VM instances that increase stability or lower your costs. 

EXAMPLES
     To check recent price history for `n2-standard-32` Spot VMs in `us-central1`, run the following command: 
    
    
    gcloud alpha compute advice capacity-history --provisioning-model=SPOT --machine-type=n2-standard-32 --types=PRICE --region=us-central1

To check recent preemption and price history for `n2-standard-32` Spot VMs in `us-central1-a`, run the following command: 
    
    
    gcloud alpha compute advice capacity-history --provisioning-model=SPOT --machine-type=n2-standard-32 --types=PREEMPTION,PRICE --zone=us-central1-a

REQUIRED FLAGS
    

`--machine-type`=`MACHINE_TYPE`
     The machine type for the VM, such as `n2-standard-4`. 
`--provisioning-model`=`PROVISIONING_MODEL`
     Specifies the provisioning model. `PROVISIONING_MODEL` must be (only one value is supported): 

`SPOT`
     Compute Engine may preempt a Spot VM whenever it needs capacity. Because Spot VMs don't have a guaranteed runtime, they come at a discounted price. 
`--types`=`HISTORY_TYPE`,[…]
     Specifies types of the request query. `HISTORY_TYPE` must be one of: 

`PREEMPTION`
     Historical preemption rates for Spot VMs, calculated as the number of Spot VMs preempted by Compute Engine divided by the total number of Spot VMs suspended, stopped, or deleted by users, or stopped or deleted resulting from preemption. The rate is expressed in decimal numbers. For more information about the preemption process, see: <https://docs.cloud.google.com/compute/docs/instances/spot#preemption>
`PRICE`
     Historical Spot VMs prices in USD. For more information about Spot VMs pricing, see: <https://docs.cloud.google.com/compute/docs/instances/spot#pricing>
Exactly one of these must be specified: 

`--region`=`REGION`
     Region of the advice to get history. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     The zone to query within the specified region, for example, `us-central1-a`. If omitted, you will view history across all zones in the region. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute advice capacity-history](https://docs.cloud.google.com/sdk/gcloud/reference/compute/advice/capacity-history)
    
    
    [gcloud beta compute advice capacity-history](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/advice/capacity-history)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
