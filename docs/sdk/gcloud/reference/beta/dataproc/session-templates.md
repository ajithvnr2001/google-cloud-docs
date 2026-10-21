---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/
title: gcloud beta dataproc session-templates \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:56.117954+00:00
---

# gcloud beta dataproc session-templates  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc session-templates Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc session-templates - create and manage Dataproc session templates 
SYNOPSIS
    

`gcloud beta dataproc session-templates` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create and manage Dataproc session templates. 
EXAMPLES
     To see the list of all session templates, run: 
    
    
    [gcloud beta dataproc session-templates list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/list)

To view the details of a session template, run: 
    
    
    [gcloud beta dataproc session-templates describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/describe) my-template

To view just the non-output only fields of a session template, run: 
    
    
    [gcloud beta dataproc session-templates export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/export) my-template --destination template-file.yaml

To create or update a session template, run: 
    
    
    [gcloud beta dataproc session-templates import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/import) my-template --source template-file.yaml

To delete a session template, run: 
    
    
    [gcloud beta dataproc session-templates delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/delete) my-template

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/delete)`
     `(BETA)` Delete a session template. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/describe)`
     `(BETA)` Describe a session template. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/export)`
     `(BETA)` Export a session template. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/import)`
     `(BETA)` Import a session template. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/list)`
     `(BETA)` List session templates. 
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
