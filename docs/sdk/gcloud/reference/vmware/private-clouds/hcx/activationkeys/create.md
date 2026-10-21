---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/hcx/activationkeys/create/
title: gcloud vmware private-clouds hcx activationkeys create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:03.682964+00:00
---

# gcloud vmware private-clouds hcx activationkeys create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/hcx/activationkeys/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vmware private-clouds hcx activationkeys create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vmware private-clouds hcx activationkeys create - create a Google Cloud VMware HCX activation key 
SYNOPSIS
    

`gcloud vmware private-clouds hcx activationkeys create` (`HCX_ACTIVATION_KEY` : `--location`=`LOCATION` `--private-cloud`=`PRIVATE_CLOUD`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a HCX activation key in a VMware Engine private cloud. Successful creation of a HCX activation key results in a HCX activation key in AVAILABLE state. Check the progress of a HCX activation key using `[gcloud vmware private-clouds hcx activationkeys list](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/hcx/activationkeys/list)`. 
EXAMPLES
     To create a HCX activation key called `key1` in private cloud `my-private-cloud` in zone `us-west2-a`, run: 
    
    
    gcloud vmware private-clouds hcx activationkeys create key1 --location=us-west2-a --project=my-project --private-cloud=my-private-cloud
    
    
    Or:
    
    
    gcloud vmware private-clouds hcx activationkeys create my-cluster --private-cloud=my-private-cloud

In the second example, the project and location are taken from gcloud properties core/project and compute/zone. 

POSITIONAL ARGUMENTS
    

HCX activation key resource - hcxactivationkey. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `hcx_activation_key` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`HCX_ACTIVATION_KEY`
     ID of the HCX activation key or fully qualified identifier for the HCX activation key. 

To set the `hcx-activation-key` attribute: 

  * provide the argument `hcx_activation_key` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the private cloud or cluster. 

To set the `location` attribute: 

  * provide the argument `hcx_activation_key` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/zone`. 


`--private-cloud`=`PRIVATE_CLOUD`
     VMware Engine private cloud. 

To set the `private-cloud` attribute: 

  * provide the argument `hcx_activation_key` on the command line with a fully specified name; 
  * provide the argument `--private-cloud` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
