---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/
title: gcloud alpha apigee \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:46.214989+00:00
---

# gcloud alpha apigee  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apigee Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apigee - manage Apigee resources 
SYNOPSIS
    

`gcloud alpha apigee` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage Apigee resources. 
EXAMPLES
     To list API proxies in the active Cloud Platform project, run: 
    
    
    [gcloud alpha apigee apis list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/list)

To deploy an API proxy named ``hello-world`` to the ``test`` environment, run: 
    
    
    [gcloud alpha apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/deploy) --environment=test --api=hello-world

To get the status of that deployment, run: 
    
    
    [gcloud alpha apigee deployments describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe) --environment=test --api=hello-world

To undeploy that API proxy, run: 
    
    
    [gcloud alpha apigee apis undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/undeploy) --environment=test --api=hello-world

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[apis](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis)`
     `(ALPHA)` Manage Apigee API proxies. 
`[applications](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications)`
     `(ALPHA)` Manage third-party applications which call Apigee API proxies. 
`[archives](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives)`
     `(ALPHA)` Manage Apigee archive deployments. 
`[deployments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments)`
     `(ALPHA)` Manage deployments of Apigee API proxies in runtime environments. 
`[developers](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/developers)`
     `(ALPHA)` Manage Apigee developers. 
`[environments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/environments)`
     `(ALPHA)` Manage Apigee environments. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/operations)`
     `(ALPHA)` Manage Apigee long running operations. 
`[organizations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations)`
     `(ALPHA)` Manage Apigee organizations. 
`[products](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/products)`
     `(ALPHA)` Manage Apigee API products. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud apigee](https://docs.cloud.google.com/sdk/gcloud/reference/apigee)
    
    
    [gcloud beta apigee](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
