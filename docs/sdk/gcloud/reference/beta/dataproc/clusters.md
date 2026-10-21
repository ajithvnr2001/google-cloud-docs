---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/
title: gcloud beta dataproc clusters \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:51.977258+00:00
---

# gcloud beta dataproc clusters  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc clusters Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc clusters - create and manage Dataproc clusters 
SYNOPSIS
    

`gcloud beta dataproc clusters` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create and manage Dataproc clusters. 
EXAMPLES
     To create a cluster, run: 
    
    
    [gcloud beta dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/create) my-cluster --region=us-central1

To resize a cluster, run: 
    
    
    [gcloud beta dataproc clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/update) my-cluster --region=us-central1 --num-workers 5

To delete a cluster, run: 
    
    
    [gcloud beta dataproc clusters delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/delete) my-cluster --region=us-central1

To view the details of a cluster, run: 
    
    
    [gcloud beta dataproc clusters describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/describe) my-cluster --region=us-central1

To see the list of all clusters, run: 
    
    
    [gcloud beta dataproc clusters list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[gke](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/gke)`
     `(BETA)` Create Dataproc GKE-based virtual clusters. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/create)`
     `(BETA)` Create a cluster. 
`[create-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/create-from-file)`
     `(BETA)` Create a cluster from a file. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/delete)`
     `(BETA)` Delete a cluster. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/describe)`
     `(BETA)` View the details of a cluster. 
`[diagnose](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/diagnose)`
     `(BETA)` Run a detailed diagnostic on a cluster. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/export)`
     `(BETA)` Export a cluster. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/get-iam-policy)`
     `(BETA)` Get IAM policy for a cluster. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/import)`
     `(BETA)` Import a cluster. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/list)`
     `(BETA)` View a list of clusters in a project. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/set-iam-policy)`
     `(BETA)` Set IAM policy for a cluster. 
`[start](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/start)`
     `(BETA)` Start a cluster. 
`[stop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/stop)`
     `(BETA)` Stop a cluster. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/update)`
     `(BETA)` Update labels and/or the number of worker nodes in a cluster. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc clusters](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters)
    
    
    [gcloud alpha dataproc clusters](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
