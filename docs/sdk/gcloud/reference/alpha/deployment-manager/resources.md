---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/resources/
title: gcloud alpha deployment-manager resources \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:27:13.972697+00:00
---

# gcloud alpha deployment-manager resources  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha deployment-manager resources Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha deployment-manager resources - commands for Deployment Manager resources 
SYNOPSIS
    

`gcloud alpha deployment-manager resources` `COMMAND` [`--deployment`=`DEPLOYMENT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Commands to list and examine resources within a deployment. 
EXAMPLES
     To view all details about a resource, run: 
    
    
    [gcloud alpha deployment-manager resources describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/resources/describe) my-resource --deployment my-deployment

To see the list of all resources in a deployment, run: 
    
    
    [gcloud alpha deployment-manager resources list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/resources/list) --deployment my-deployment

FLAGS
    

`--deployment`=`DEPLOYMENT`
     Deployment name 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/resources/describe)`
     `(ALPHA)` Provide information about a resource. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/resources/list)`
     `(ALPHA)` List resources in a deployment. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud deployment-manager resources](https://docs.cloud.google.com/sdk/gcloud/reference/deployment-manager/resources)
    
    
    [gcloud beta deployment-manager resources](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/resources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
