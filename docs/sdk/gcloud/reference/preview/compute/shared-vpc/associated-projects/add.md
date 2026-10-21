---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/shared-vpc/associated-projects/add/
title: gcloud preview compute shared-vpc associated-projects add \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:11:29.101218+00:00
---

# gcloud preview compute shared-vpc associated-projects add  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/shared-vpc/associated-projects/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute shared-vpc associated-projects add Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute shared-vpc associated-projects add - associate the given project with a given shared VPC host project 
SYNOPSIS
    

`gcloud preview compute shared-vpc associated-projects add` `PROJECT_ID` `--host-project`=`HOST_PROJECT` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Associate the given project with a given shared VPC host project. 
EXAMPLES
     To add the project `service-project` as an associated service project of the shared VPC host project `host-project`, run: 
    
    
    gcloud preview compute shared-vpc associated-projects add --host-project=host-project service-project

POSITIONAL ARGUMENTS
    

`PROJECT_ID`
     ID for the project to add to the host project 
REQUIRED FLAGS
    

`--host-project`=`HOST_PROJECT`
     The XPN host to add an associated project to 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute shared-vpc associated-projects add](https://docs.cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/associated-projects/add)
    
    
    [gcloud alpha compute shared-vpc associated-projects add](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/shared-vpc/associated-projects/add)
    
    
    [gcloud beta compute shared-vpc associated-projects add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/shared-vpc/associated-projects/add)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
