---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/
title: gcloud beta apigee \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:07.880806+00:00
---

# gcloud beta apigee  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta apigee Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta apigee - manage Apigee resources 
SYNOPSIS
    

`gcloud beta apigee` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage Apigee resources. 
EXAMPLES
     To list API proxies in the active Cloud Platform project, run: 
    
    
    [gcloud beta apigee apis list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/list)

To deploy an API proxy named ``hello-world`` to the ``test`` environment, run: 
    
    
    [gcloud beta apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/deploy) --environment=test --api=hello-world

To get the status of that deployment, run: 
    
    
    [gcloud beta apigee deployments describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments/describe) --environment=test --api=hello-world

To undeploy that API proxy, run: 
    
    
    [gcloud beta apigee apis undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/undeploy) --environment=test --api=hello-world

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[apis](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis)`
     `(BETA)` Manage Apigee API proxies. 
`[applications](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/applications)`
     `(BETA)` Manage third-party applications which call Apigee API proxies. 
`[archives](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives)`
     `(BETA)` Manage Apigee archive deployments. 
`[deployments](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments)`
     `(BETA)` Manage deployments of Apigee API proxies in runtime environments. 
`[developers](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/developers)`
     `(BETA)` Manage Apigee developers. 
`[environments](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/environments)`
     `(BETA)` Manage Apigee environments. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/operations)`
     `(BETA)` Manage Apigee long running operations. 
`[organizations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/organizations)`
     `(BETA)` Manage Apigee organizations. 
`[products](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/products)`
     `(BETA)` Manage Apigee API products. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud apigee](https://docs.cloud.google.com/sdk/gcloud/reference/apigee)
    
    
    [gcloud alpha apigee](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
