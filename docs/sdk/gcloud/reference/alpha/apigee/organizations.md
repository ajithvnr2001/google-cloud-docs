---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/
title: gcloud alpha apigee organizations \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:51.570957+00:00
---

# gcloud alpha apigee organizations  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apigee organizations Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apigee organizations - manage Apigee organizations 
SYNOPSIS
    

`gcloud alpha apigee organizations` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage Apigee organizations. 

`gcloud alpha apigee organizations` contains commands for managing Apigee organizations, the highest-level grouping of Apigee objects. All API proxies, environments, and so forth each belong to one organization. 

Apigee organizations are distinct from Cloud Platform organizations, being more similar to Cloud Platform projects in scope and purpose. 

EXAMPLES
     To list all accessible organizations and their associated Cloud Platform projects, run: 
    
    
    [gcloud alpha apigee organizations list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/list)

To get a JSON array of all organizations whose Cloud Platform project names contain the word ``sandbox``, run: 
    
    
    [gcloud alpha apigee organizations list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/list) --format=json --filter="project:(sandbox)"

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/delete)`
     `(ALPHA)` Delete an Apigee organization. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/list)`
     `(ALPHA)` List Apigee organizations and their paired Cloud Platform projects. 
`[provision](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision)`
     `(ALPHA)` Provision an Apigee SaaS organization. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud apigee organizations](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/organizations)
    
    
    [gcloud beta apigee organizations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/organizations)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
