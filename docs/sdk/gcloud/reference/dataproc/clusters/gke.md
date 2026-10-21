---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/
title: gcloud dataproc clusters gke \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:12.128535+00:00
---

# gcloud dataproc clusters gke  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataproc clusters gke Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataproc clusters gke - create Dataproc GKE-based virtual clusters 
SYNOPSIS
    

`gcloud dataproc clusters gke` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     All interactions other than creation should be handled by "gcloud dataproc clusters" commands. 
EXAMPLES
     To create a cluster, run: 
    
    
    gcloud dataproc clusters gke my-cluster --region='us-central1' --gke-cluster='my-gke-cluster' --spark-engine-version='latest' --pools='name=dp,roles=default'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create)`
     Create a GKE-based virtual cluster. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha dataproc clusters gke](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/gke)
    
    
    [gcloud beta dataproc clusters gke](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/gke)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
