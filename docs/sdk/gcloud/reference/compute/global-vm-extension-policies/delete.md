---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/delete/
title: gcloud compute global-vm-extension-policies delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:08:26.723874+00:00
---

# gcloud compute global-vm-extension-policies delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute global-vm-extension-policies delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute global-vm-extension-policies delete - delete a Compute Engine global VM extension policy 
SYNOPSIS
    

`gcloud compute global-vm-extension-policies delete` `NAME` [`--rollout-custom-plan`=`ROLLOUT_CUSTOM_PLAN`] [`--rollout-predefined-plan`=`ROLLOUT_PREDEFINED_PLAN`] [`--rollout-retry-uuid`=`ROLLOUT_RETRY_UUID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete a Compute Engine global VM extension policy. 
EXAMPLES
     To delete a global VM extension policy, run: 
    
    
    gcloud compute global-vm-extension-policies delete test-policy-name

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the global vm extension policy to delete. 
FLAGS
    

`--rollout-custom-plan`=`ROLLOUT_CUSTOM_PLAN`
     Provide the name of a custom rollout plan to be used for the rollout. 

One of either --rollout-predefined-plan or --rollout-custom-plan must be specified, but not both. 

`--rollout-predefined-plan`=`ROLLOUT_PREDEFINED_PLAN`
     Provide the name of a predefined rollout plan from [fast_rollout, slow_rollout] to be used for the rollout. 

One of either --rollout-predefined-plan or --rollout-custom-plan must be specified, but not both. 

`ROLLOUT_PREDEFINED_PLAN` must be one of: `fast_rollout`, `slow_rollout`. 

`--rollout-retry-uuid`=`ROLLOUT_RETRY_UUID`
     The UUID of the rollout retry action. Only set it if this is a retry for an existing resource. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute global-vm-extension-policies delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/global-vm-extension-policies/delete)
    
    
    [gcloud beta compute global-vm-extension-policies delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/global-vm-extension-policies/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
