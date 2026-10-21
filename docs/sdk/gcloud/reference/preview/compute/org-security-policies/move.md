---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/move/
title: gcloud preview compute org-security-policies move \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:03:30.766377+00:00
---

# gcloud preview compute org-security-policies move  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute org-security-policies move Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute org-security-policies move - move a Compute Engine organization security policy 
SYNOPSIS
    

`gcloud preview compute org-security-policies move` `SECURITY_POLICY` [`--folder`=`FOLDER`] [`--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute org-security-policies move` is used to move is used to move organization security policies to new parent nodes. 
EXAMPLES
     To move an organization security policy under folder with ID ``123456789`` to folder ``987654321``, run: 
    
    
    gcloud preview compute org-security-policies move 123456789 --folder=987654321

POSITIONAL ARGUMENTS
    

`SECURITY_POLICY`
     Short name or ID of the security policy to move. 
FLAGS
    

`--folder`=`FOLDER`
     Folder to which the organization security policy is to be moved. 
`--organization`=`ORGANIZATION`
     Organization in which the organization security policy is to be moved. Must be set if SECURITY_POLICY is the short name. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute org-security-policies move](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/move)
    
    
    [gcloud alpha compute org-security-policies move](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies/move)
    
    
    [gcloud beta compute org-security-policies move](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/org-security-policies/move)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
