---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/application-awareness/configure-strict-priority-policy/
title: gcloud compute interconnects application-awareness configure-strict-priority-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:44:02.177137+00:00
---

# gcloud compute interconnects application-awareness configure-strict-priority-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/application-awareness/configure-strict-priority-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute interconnects application-awareness configure-strict-priority-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute interconnects application-awareness configure-strict-priority-policy - configure strict priority policy for application awareness configuration of a Compute Engine interconnect 
SYNOPSIS
    

`gcloud compute interconnects application-awareness configure-strict-priority-policy` `NAME` [`--enabled`] [`--profile-description`=`PROFILE_DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute interconnects application-awareness configure-strict-priority-policy` is used to configure strict priority policy for using application awareness on interconnect. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To configure strict priority policy for an interconnect example-interconnect, run: 
    
    
    [gcloud compute interconnects application-awareness](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/application-awareness) configure-strict-priority-policy example-interconnect --enabled --profile-description="some string"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect to patch. 
FLAGS
    

`--enabled`
     Enable or disable application awareness on the interconnect. Application awareness enablement will fail if the application awareness configuration is not specified. Use --no-enabled to disable it. 
`--profile-description`=`PROFILE_DESCRIPTION`
     Add profile description for application awareness. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute interconnects application-awareness](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/application-awareness) configure-strict-priority-policy
    
    
    [gcloud beta compute interconnects application-awareness](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/application-awareness) configure-strict-priority-policy
    
    
    [gcloud preview compute interconnects application-awareness](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/application-awareness) configure-strict-priority-policy

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
