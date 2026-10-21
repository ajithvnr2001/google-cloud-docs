---
url: https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/
title: gcloud filestore backups \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:16:23.279184+00:00
---

# gcloud filestore backups  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud filestore backups Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud filestore backups - create and manage Filestore backups 
SYNOPSIS
    

`gcloud filestore backups` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a backup with the name 'my-backup', run: 
    
    
    [gcloud filestore backups create](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/create) my-backup --region=Region

To delete a backup with the name 'my-backup', run: 
    
    
    [gcloud filestore backups delete](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/delete) my-backup --region=Region

To display the details for an backup with the name 'my-backup', run: 
    
    
    [gcloud filestore backups describe](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/describe) my-backup --region=Region

To list all the backups, run: 
    
    
    [gcloud filestore backups list](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/list) [--region=Region]

To set the label 'env' to 'prod' for an backup with the name 'my-backup', run: 
    
    
    gcloud filestore backups my-backup --update-labels=env=prod

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/create)`
     Create a Filestore backup. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/delete)`
     Delete a Filestore backup. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/describe)`
     Describe a Filestore backup. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/list)`
     List Filestore backups. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/backups/update)`
     Update a Filestore backup. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha filestore backups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/backups)
    
    
    [gcloud beta filestore backups](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/backups)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
