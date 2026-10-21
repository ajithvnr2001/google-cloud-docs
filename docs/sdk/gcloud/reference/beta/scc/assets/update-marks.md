---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/assets/update-marks/
title: gcloud beta scc assets update-marks \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:47:11.983733+00:00
---

# gcloud beta scc assets update-marks  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/assets/update-marks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta scc assets update-marks Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta scc assets update-marks - update Cloud Security Command Center asset's security marks 
SYNOPSIS
    

`gcloud beta scc assets update-marks` (`ASSET` : `--organization`=`ORGANIZATION`) [`--security-marks`=[`KEY`=`VALUE`,…]] [`--start-time`=`START_TIME`] [`--update-mask`=`UPDATE_MASK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update Cloud Security Command Center asset's security marks. 
EXAMPLES
     Selectively update value of security mark (key1) with 'val1.1' on asset 5678 under organization 123456. Note that other security marks on the same asset will not change. 
    
    
    gcloud beta scc assets update-marks 5678 --organization=123456 --security-marks="key1=val1.1" --update-mask="marks.key1"

Update value of security mark (key1) and delete other marks on asset 5678 under organization 123456: 
    
    
    gcloud beta scc assets update-marks 5678 --organization=123456 --security-marks="key1=updatedVal"

Update value of security mark (key1) and delete other marks on asset 5678 under project example-project: 
    
    
    gcloud beta scc assets update-marks projects/example-project/assets/5678 --security-marks="key1=updatedVal"

Update value of security mark (key1) and delete other marks on asset 5678 under folder 456: 
    
    
    gcloud beta scc assets update-marks folders/456/assets/5678 --security-marks="key1=updatedVal"

Delete all security marks on asset 5678 under organization 123456: 
    
    
    gcloud beta scc assets update-marks 5678 --organization=123456 --security-marks=""

POSITIONAL ARGUMENTS
    

Asset resource - The asset to be used for the SCC (Security Command Center) command. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`ASSET`
     ID of the asset or fully qualified identifier for the asset. 

To set the `asset` attribute: 

  * provide the argument `asset` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     (Optional) If the full resource name isn't provided e.g. organizations/123, then provide the organization id which is the suffix of the organization. Example: organizations/123, the id is 123. To set the `organization` attribute: 

  * provide the argument `asset` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * Set the organization property in configuration using `gcloud config set scc/organization` if it is not specified in command line.. 


FLAGS
    

`--security-marks`=[`KEY`=`VALUE`,…]
     SecurityMarks resource to be passed as the request body. It's a key=value pair separated by comma (,). For example: --security-marks="key1=val1,key2=val2". 
`--start-time`=`START_TIME`
     Time at which the updated SecurityMarks take effect. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on supported time formats. 
`--update-mask`=`UPDATE_MASK`
     Use update-mask if you want to selectively update marks represented by \--security-marks flag. For example: --update-mask="marks.key1,marks.key2". If you want to override all the marks for the given asset either skip the update-mask flag or provide an empty value (--update-mask '') for it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securitycenter/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud scc assets update-marks](https://docs.cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks)
    
    
    [gcloud alpha scc assets update-marks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/assets/update-marks)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
