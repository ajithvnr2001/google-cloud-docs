---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/node-groups/
title: gcloud beta dataproc node-groups \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:55.018677+00:00
---

# gcloud beta dataproc node-groups  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/node-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc node-groups Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc node-groups - manage Dataproc node groups 
SYNOPSIS
    

`gcloud beta dataproc node-groups` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage and modify Dataproc node groups created with a parent cluster. 
EXAMPLES
     To describe a node group: 
    
    
    [gcloud beta dataproc node-groups describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/node-groups/describe) NODE_GROUP_ID --cluster cluster_name --region region

To resize a node group: 
    
    
    [gcloud beta dataproc node-groups resize](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/node-groups/resize) NODE_GROUP_ID --cluster cluster_name --region region --size new_size

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/node-groups/describe)`
     `(BETA)` Describe the node group. 
`[resize](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/node-groups/resize)`
     `(BETA)` Resize the number of nodes in the node group. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc node-groups](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/node-groups)
    
    
    [gcloud alpha dataproc node-groups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/node-groups)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
