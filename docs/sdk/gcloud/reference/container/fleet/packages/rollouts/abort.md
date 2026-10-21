---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/packages/rollouts/abort/
title: gcloud container fleet packages rollouts abort \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:30:46.672208+00:00
---

# gcloud container fleet packages rollouts abort  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/packages/rollouts/abort/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container fleet packages rollouts abort Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container fleet packages rollouts abort - abort Rollout resource 
SYNOPSIS
    

`gcloud container fleet packages rollouts abort` (`ROLLOUT` : `--fleet-package`=`FLEET_PACKAGE` `--location`=`LOCATION`) [`--reason`=`REASON`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Abort Rollout resource. 
EXAMPLES
     To abort Rollout `20240318` for `cert-manager-app` in `us-central1`, run: 
    
    
    gcloud container fleet packages rollouts abort 20240318 --fleet-package=cert-manager-app --location=us-central1

POSITIONAL ARGUMENTS
    

Rollout resource - The rollout to abort. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`ROLLOUT`
     ID of the rollout or fully qualified identifier for the rollout. 

To set the `rollout` attribute: 

  * provide the argument `rollout` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--fleet-package`=`FLEET_PACKAGE`
     Fleet Package name. 

To set the `fleet-package` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * provide the argument `--fleet-package` on the command line. 


`--location`=`LOCATION`
     Google Cloud zone or region for the rollout. 

To set the `location` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `config_delivery/location`. 


FLAGS
    

`--reason`=`REASON`
     Reason for aborting rollout. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container fleet packages rollouts abort](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/packages/rollouts/abort)
    
    
    [gcloud beta container fleet packages rollouts abort](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/packages/rollouts/abort)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
