---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/
title: gcloud beta deployment-manager deployments \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:42.512365+00:00
---

# gcloud beta deployment-manager deployments  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta deployment-manager deployments Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta deployment-manager deployments - commands for Deployment Manager deployments 
SYNOPSIS
    

`gcloud beta deployment-manager deployments` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Commands to create, update, delete, and examine deployments of resources. 
EXAMPLES
     To create a deployment, run: 
    
    
    [gcloud beta deployment-manager deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/create) my-deployment --config config.yaml

To update a deployment, run: 
    
    
    [gcloud beta deployment-manager deployments update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/update) my-deployment --config new_config.yaml

To stop a deployment create or update in progress, run: 
    
    
    [gcloud beta deployment-manager deployments stop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/stop) my-deployment

To cancel a previewed create or update, run: 
    
    
    [gcloud beta deployment-manager deployments cancel-preview](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/cancel-preview) my-deployment

To delete a deployment, run: 
    
    
    [gcloud beta deployment-manager deployments delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/delete) my-deployment

To view the details of a deployment, run: 
    
    
    [gcloud beta deployment-manager deployments describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/describe) my-deployment

To see the list of all deployments, run: 
    
    
    [gcloud beta deployment-manager deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[cancel-preview](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/cancel-preview)`
     `(BETA)` Cancel a pending or running deployment preview. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/create)`
     `(BETA)` Create a deployment. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/delete)`
     `(BETA)` Delete a deployment. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/describe)`
     `(BETA)` Provide information about a deployment. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/list)`
     `(BETA)` List deployments in a project. 
`[stop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/stop)`
     `(BETA)` Stop a pending or running deployment update or creation. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/update)`
     `(BETA)` Update a deployment based on a provided config file. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud deployment-manager deployments](https://docs.cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments)
    
    
    [gcloud alpha deployment-manager deployments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/deployments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
