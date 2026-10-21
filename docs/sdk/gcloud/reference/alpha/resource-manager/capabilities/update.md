---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/capabilities/update/
title: gcloud alpha resource-manager capabilities update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:53.425964+00:00
---

# gcloud alpha resource-manager capabilities update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/capabilities/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager capabilities update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager capabilities update - update a folder capability 
SYNOPSIS
    

`gcloud alpha resource-manager capabilities update` `CAPABILITY_ID` `--[no-]enable` [`--update-mask`=`UPDATE_MASK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Command to Update/Set the `value` field of the Folder capability. This can be done by using the `--enable` flag to set the value to True, and the `--no-enable` flag to set the value to False. 

This command can fail for the following reasons: 

  * There is no folder parenting the given capability name. 
  * The active account does not have permission to update the given folder/capability. 


EXAMPLES
     The following command updates a capability with the ID `folders/123/capabilities/app-management` to have the value True: 
    
    
    gcloud alpha resource-manager capabilities update "folders/123/capabilities/app-management" --enable

In order to set the value to False, the following command can be used: 
    
    
    gcloud alpha resource-manager capabilities update "folders/123/capabilities/app-management" --no-enable

POSITIONAL ARGUMENTS
    

`CAPABILITY_ID`
     ID for the capability you want to update. 
REQUIRED FLAGS
    

`--[no-]enable`
     Enable the Capability. Use `--enable` to enable and `--no-enable` to disable. 
OPTIONAL FLAGS
    

`--update-mask`=`UPDATE_MASK`
     Update Mask. This is an optional field, and the only valid value this can be set to currently is "value". 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud resource-manager capabilities update](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/capabilities/update)
    
    
    [gcloud beta resource-manager capabilities update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/capabilities/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
