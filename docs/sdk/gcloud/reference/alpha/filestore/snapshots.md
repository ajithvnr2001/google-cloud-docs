---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/
title: gcloud alpha filestore snapshots \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:46.511594+00:00
---

# gcloud alpha filestore snapshots  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha filestore snapshots Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha filestore snapshots - create and manage Filestore snapshots 
SYNOPSIS
    

`gcloud alpha filestore snapshots` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a snapshot with the name 'my-snapshot', run: 
    
    
    [gcloud alpha filestore snapshots create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/create) my-snapshot

To delete a snapshot with the name 'my-snapshot', run: 
    
    
    [gcloud alpha filestore snapshots delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/delete) my-snapshot

To display the details for an snapshot with the name 'my-snapshot', run: 
    
    
    [gcloud alpha filestore snapshots describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/describe) my-snapshot

To list all the snapshots, run: 
    
    
    [gcloud alpha filestore snapshots list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/list)

To set the label 'env' to 'prod' for an snapshot with the name 'my-snapshot', run: 
    
    
    gcloud alpha filestore snapshots my-snapshot --update-labels=env=prod

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/create)`
     `(ALPHA)` Create a Filestore snapshot. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/delete)`
     `(ALPHA)` Delete a Filestore snapshot. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/describe)`
     `(ALPHA)` Describe a Filestore snapshot. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/list)`
     `(ALPHA)` List Filestore snapshots. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/update)`
     `(ALPHA)` Update a Filestore snapshot. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
