---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/operations/describe/
title: gcloud beta compute operations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:06:36.633730+00:00
---

# gcloud beta compute operations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/operations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute operations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute operations describe - describe a Compute Engine operation 
SYNOPSIS
    

`gcloud beta compute operations describe` `NAME` [`--global` | `--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute operations describe` displays all data associated with a Compute Engine operation in a project. 
EXAMPLES
     To get details about a global operation (e.g. operation-111-222-333-444), run: 
    
    
    gcloud beta compute operations describe operation-111-222-333-444 --global

To get details about a regional operation, run: 
    
    
    gcloud beta compute operations describe operation-111-222-333-444 --region=us-central1

To get details about a zonal operation, run: 
    
    
    gcloud beta compute operations describe operation-111-222-333-444 --zone=us-central1-a

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the operation returned by an asynchronous command. Use `[gcloud compute operations list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list)` to display recent operations. 
FLAGS
    

At most one of these can be specified: 

`--global`
     If set, the operation is global. 
`--region`=`REGION`
     Region of the operation to describe. Overrides the default `compute/region` property value for this command invocation. 
`--zone`=`ZONE`
     Zone of the operation to describe. Overrides the default `compute/zone` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/describe)
    
    
    [gcloud alpha compute operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/operations/describe)
    
    
    [gcloud preview compute operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/operations/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
