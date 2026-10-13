---
url: https://docs.cloud.google.com/sdk/gcloud/reference/run/
title: gcloud run \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:45.218756+00:00
---

# gcloud run  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud run Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud run - manage your Cloud Run applications 
SYNOPSIS
    

`gcloud run` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The gcloud run command group lets you deploy container images to Google Cloud Run. 
EXAMPLES
     To deploy your container, use the `[gcloud run deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy)` command: 
    
    
    [gcloud run deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) <service-name> --image <image_name>

For more information, run:
    
    
    [gcloud run deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) --help

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[compose](https://docs.cloud.google.com/sdk/gcloud/reference/run/compose)`
     Support Docker Compose workflows on Cloud Run. 
`[domain-mappings](https://docs.cloud.google.com/sdk/gcloud/reference/run/domain-mappings)`
     View and manage your Cloud Run for Anthos domain mappings. 
`[jobs](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs)`
     View and manage your Cloud Run jobs. 
`[multi-region-services](https://docs.cloud.google.com/sdk/gcloud/reference/run/multi-region-services)`
     Manage your Cloud Run multi-region services. 
`[regions](https://docs.cloud.google.com/sdk/gcloud/reference/run/regions)`
     View available Cloud Run (fully managed) regions. 
`[revisions](https://docs.cloud.google.com/sdk/gcloud/reference/run/revisions)`
     View and manage your Cloud Run revisions. 
`[services](https://docs.cloud.google.com/sdk/gcloud/reference/run/services)`
     View and manage your Cloud Run services. 
`[worker-pools](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools)`
     View and manage your Cloud Run worker pools. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy)`
     Create or update a Cloud Run service. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run)
    
    
    [gcloud beta run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
