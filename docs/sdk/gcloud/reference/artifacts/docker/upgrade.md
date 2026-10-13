---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/
title: gcloud artifacts docker upgrade \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:09.739035+00:00
---

# gcloud artifacts docker upgrade  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts docker upgrade Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts docker upgrade - commands to support Container Registry to Artifact Registry upgrade 
SYNOPSIS
    

`gcloud artifacts docker upgrade` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     To print an equivalent Artifact Registry IAM policy for 'gcr.io/my-project': 
    
    
    gcloud artifacts docker upgrade print-iam-policy gcr.io --project=my-project

To migrate a project from Container Registry to Artifact Registry using gcr.io repos: 
    
    
    [gcloud artifacts docker upgrade migrate](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate) --projects=my-project

To migrate a project from Container Registry to Artifact Registry using pkg.dev repos: 
    
    
    [gcloud artifacts docker upgrade migrate](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate) --from-gcr-io=gcr.io/from-project --to-pkg-dev=to-project/to-repo

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[migrate](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate)`
     Migrate projects from Container Registry to Artifact Registry. 
NOTES
     This variant is also available: 
    
    
    [gcloud beta artifacts docker upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/upgrade)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
