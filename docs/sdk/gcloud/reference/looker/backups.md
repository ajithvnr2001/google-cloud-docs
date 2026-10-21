---
url: https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/
title: gcloud looker backups \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:12:47.916129+00:00
---

# gcloud looker backups  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud looker backups Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud looker backups - manage Looker instances 
SYNOPSIS
    

`gcloud looker backups` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a backup of an instance with the name `my-looker-instance` and in the region `us-central1`, run: 
    
    
    [gcloud looker backups create](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/create) --instance='my-looker-instance --region=us-central1'

To delete a backup with the name `looker-backup` that is a backup of an instance with the name `my-looker-instance` and in the region `us-central1`, run: 
    
    
    [gcloud looker backups delete](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/delete) looker-backup --instance=my-looker-instance --region=us-central1

To display the details for a backup with the name `looker-backup` that is a backup of an instance with the name `my-looker-instance` and in the region `us-central1`, run: 
    
    
    [gcloud looker backups describe](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/describe) looker-backup --instance=my-looker-instance --region=us-central1

To list all backups of an instance with the name `my-looker-instance` and in the region `us-central1`, run: 
    
    
    [gcloud looker backups list](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/list) --instance=my-looker-instance --region=us-central1

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/create)`
     Create a backup of a Looker instance. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/delete)`
     Delete a backup of a Looker instance. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/describe)`
     Show metadata of a backup for a Looker instance. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/list)`
     List backups of a Looker instance. 
NOTES
     This variant is also available: 
    
    
    [gcloud alpha looker backups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/looker/backups)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
