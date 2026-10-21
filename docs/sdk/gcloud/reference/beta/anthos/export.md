---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/anthos/export/
title: gcloud beta anthos export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:09.644422+00:00
---

# gcloud beta anthos export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/anthos/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta anthos export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta anthos export - export current configuration of an Anthos cluster 
SYNOPSIS
    

`gcloud beta anthos export` `CLUSTER` [`--project`=`PROJECT_ID`] [`--location`=`LOCATION`] [`--output-directory`=`OUTPUT-DIR`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Export current configuration of an Anthos cluster. 
EXAMPLES
     To export configuration from cluster 'my-cluster' to the local directory `my-dir` using project 'my-project': 
    
    
    gcloud beta anthos export my-cluster --project=my-project --output-directory=my-dir

POSITIONAL ARGUMENTS
    

`CLUSTER`
     The cluster name from which to export the configurations. 
COMMONLY USED FLAGS
    

`--project`=`PROJECT_ID`
     Project ID. Overrides the default `core/project` property value for this command invocation. 
OTHER FLAGS
    

`--location`=`LOCATION`
     Specifies the Google Cloud location to use. If notspecified will use the current compute/zone property. 
`--output-directory`=`OUTPUT-DIR`
     The output directory of the cluster resources. If empty will export files to ./CLUSTER_NAME 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha anthos export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/anthos/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
