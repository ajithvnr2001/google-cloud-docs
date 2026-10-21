---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/
title: gcloud beta app domain-mappings \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:55.980992+00:00
---

# gcloud beta app domain-mappings  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app domain-mappings Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app domain-mappings - view and manage your App Engine domain mappings 
SYNOPSIS
    

`gcloud beta app domain-mappings` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This set of commands can be used to view and manage your app's domain mappings. 

App Engine Domain Mappings allow an application to be served via one or many custom domains, such as `example.com`, instead of the default `https://<PROJECT-ID>.<REGION-ID>.r.appspot.com` address. You can use a custom domain with or without SSL. 

Use the AUTOMATIC management type to automatically provision an SSL certificate for your domain. Use the MANUAL management type to provide your own certificate or omit SSL. 

EXAMPLES
     To list your App Engine domains, run: 
    
    
    [gcloud beta app domain-mappings list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/list)

To create a domain with an automatically managed certificate, run: 
    
    
    [gcloud beta app domain-mappings create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/create) 'example.com' --certificate-management=AUTOMATIC

To create a domain with a manual certificate, run: 
    
    
    [gcloud beta app domain-mappings create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/create) 'example.com' --certificate-management=manual --certificate-id=1234

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/create)`
     `(BETA)` Creates a domain mapping. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/delete)`
     `(BETA)` Deletes a specified domain mapping. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/describe)`
     `(BETA)` Describes a specified domain mapping. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/list)`
     `(BETA)` Lists domain mappings. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/update)`
     `(BETA)` Updates a domain mapping. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud app domain-mappings](https://docs.cloud.google.com/sdk/gcloud/reference/app/domain-mappings)
    
    
    [gcloud alpha app domain-mappings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
