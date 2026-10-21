---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-layer7-ddos-defense-threshold-config/
title: gcloud compute security-policies remove-layer7-ddos-defense-threshold-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:51:09.723760+00:00
---

# gcloud compute security-policies remove-layer7-ddos-defense-threshold-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-layer7-ddos-defense-threshold-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute security-policies remove-layer7-ddos-defense-threshold-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute security-policies remove-layer7-ddos-defense-threshold-config - remove a layer7 ddos defense threshold config from a Compute Engine security policy 
SYNOPSIS
    

`gcloud compute security-policies remove-layer7-ddos-defense-threshold-config` `NAME` `--threshold-config-name`=`THRESHOLD_CONFIG_NAME` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute security-policies remove-layer7-ddos-defense-threshold-config` is used to remove layer7 ddos defense threshold configs from security policies. 
EXAMPLES
     To remove a layer7 ddos defense threshold config run the following command: 
    
    
    [gcloud compute security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies) remove-layer7-ddos-defense-threshold-config NAME --threshold-config-name=my-threshold-config-name

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the security policy to update. 
REQUIRED FLAGS
    

`--threshold-config-name`=`THRESHOLD_CONFIG_NAME`
     The name for the threshold config. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/security-policies) remove-layer7-ddos-defense-threshold-config
    
    
    [gcloud beta compute security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/security-policies) remove-layer7-ddos-defense-threshold-config
    
    
    [gcloud preview compute security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies) remove-layer7-ddos-defense-threshold-config

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
