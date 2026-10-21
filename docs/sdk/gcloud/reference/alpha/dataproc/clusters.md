---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/
title: gcloud alpha dataproc clusters \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:00.637974+00:00
---

# gcloud alpha dataproc clusters  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataproc clusters Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataproc clusters - create and manage Dataproc clusters 
SYNOPSIS
    

`gcloud alpha dataproc clusters` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create and manage Dataproc clusters. 
EXAMPLES
     To create a cluster, run: 
    
    
    [gcloud alpha dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/create) my-cluster --region=us-central1

To resize a cluster, run: 
    
    
    [gcloud alpha dataproc clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/update) my-cluster --region=us-central1 --num-workers 5

To delete a cluster, run: 
    
    
    [gcloud alpha dataproc clusters delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/delete) my-cluster --region=us-central1

To view the details of a cluster, run: 
    
    
    [gcloud alpha dataproc clusters describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/describe) my-cluster --region=us-central1

To see the list of all clusters, run: 
    
    
    [gcloud alpha dataproc clusters list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[gke](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/gke)`
     `(ALPHA)` Create Dataproc GKE-based virtual clusters. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/create)`
     `(ALPHA)` Create a cluster. 
`[create-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/create-from-file)`
     `(ALPHA)` Create a cluster from a file. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/delete)`
     `(ALPHA)` Delete a cluster. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/describe)`
     `(ALPHA)` View the details of a cluster. 
`[diagnose](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/diagnose)`
     `(ALPHA)` Run a detailed diagnostic on a cluster. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/export)`
     `(ALPHA)` Export a cluster. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/get-iam-policy)`
     `(ALPHA)` Get IAM policy for a cluster. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/import)`
     `(ALPHA)` Import a cluster. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/list)`
     `(ALPHA)` View a list of clusters in a project. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/set-iam-policy)`
     `(ALPHA)` Set IAM policy for a cluster. 
`[start](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/start)`
     `(ALPHA)` Start a cluster. 
`[stop](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/stop)`
     `(ALPHA)` Stop a cluster. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/update)`
     `(ALPHA)` Update labels and/or the number of worker nodes in a cluster. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dataproc clusters](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters)
    
    
    [gcloud beta dataproc clusters](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
