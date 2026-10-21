---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies/add-user-defined-field/
title: gcloud preview compute security-policies add-user-defined-field \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:24:09.480935+00:00
---

# gcloud preview compute security-policies add-user-defined-field  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies/add-user-defined-field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute security-policies add-user-defined-field Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute security-policies add-user-defined-field - add a user defined field to a Compute Engine security policy 
SYNOPSIS
    

`gcloud preview compute security-policies add-user-defined-field` `NAME` `--base`=`BASE` `--offset`=`OFFSET` `--size`=`SIZE` `--user-defined-field-name`=`USER_DEFINED_FIELD_NAME` [`--mask`=`MASK`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute security-policies add-user-defined-field` is used to add user defined fields to security policies. 
EXAMPLES
     To add a user defined field run this: 
    
    
    gcloud preview compute security-policies add-user-defined-field SECURITY_POLICY --user-defined-field-name=my-field --base=ipv6 --offset=10 --size=3

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the security policy to update. 
REQUIRED FLAGS
    

`--base`=`BASE`
     The base relative to which offset is measured. `BASE` must be one of: `ipv4`, `ipv6`, `tcp`, `udp`. 
`--offset`=`OFFSET`
     Offset of the first byte of the field (in network byte order) relative to base. 
`--size`=`SIZE`
     Size of the field in bytes. Valid values: 1-4. 
`--user-defined-field-name`=`USER_DEFINED_FIELD_NAME`
     The name for the user defined field. 
OPTIONAL FLAGS
    

`--mask`=`MASK`
     If specified, apply this mask (bitwise AND) to the field to ignore bits before matching. Encoded as a hexadecimal number (starting with "0x"). 
`--region`=`REGION`
     Region of the security policy to update. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute security-policies add-user-defined-field](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field)
    
    
    [gcloud alpha compute security-policies add-user-defined-field](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/security-policies/add-user-defined-field)
    
    
    [gcloud beta compute security-policies add-user-defined-field](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/security-policies/add-user-defined-field)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
