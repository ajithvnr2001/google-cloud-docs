---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/
title: gcloud apigee \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:28.660442+00:00
---

# gcloud apigee  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apigee Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apigee - manage Apigee resources 
SYNOPSIS
    

`gcloud apigee` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage Apigee resources. 
EXAMPLES
     To list API proxies in the active Cloud Platform project, run: 
    
    
    [gcloud apigee apis list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/list)

To deploy an API proxy named ``hello-world`` to the ``test`` environment, run: 
    
    
    [gcloud apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/deploy) --environment=test --api=hello-world

To get the status of that deployment, run: 
    
    
    [gcloud apigee deployments describe](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/describe) --environment=test --api=hello-world

To undeploy that API proxy, run: 
    
    
    [gcloud apigee apis undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy) --environment=test --api=hello-world

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[apis](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis)`
     Manage Apigee API proxies. 
`[applications](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/applications)`
     Manage third-party applications which call Apigee API proxies. 
`[deployments](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments)`
     Manage deployments of Apigee API proxies in runtime environments. 
`[developers](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/developers)`
     Manage Apigee developers. 
`[environments](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/environments)`
     Manage Apigee environments. 
`[organizations](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/organizations)`
     Manage Apigee organizations. 
`[products](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products)`
     Manage Apigee API products. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha apigee](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee)
    
    
    [gcloud beta apigee](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
