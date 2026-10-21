---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings/create/
title: gcloud alpha app domain-mappings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:30.196083+00:00
---

# gcloud alpha app domain-mappings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha app domain-mappings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha app domain-mappings create - creates a domain mapping 
SYNOPSIS
    

`gcloud alpha app domain-mappings create` `DOMAIN` [`--certificate-id`=`CERTIFICATE_ID`] [`--certificate-management`=`CERTIFICATE_MANAGEMENT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a domain mapping. 
EXAMPLES
     To create a new App Engine domain mapping with an automatically managed certificate, run: 
    
    
    gcloud alpha app domain-mappings create 'example.com'

Note: managed certificates do not support wildcard domain mappings. 

To create a domain with a manual certificate, run: 
    
    
    gcloud alpha app domain-mappings create '*.example.com' --certificate-management=manual --certificate-id=1234

To create a domain with no associated certificate, run: 
    
    
    gcloud alpha app domain-mappings create '*.example.com' --certificate-management=manual

POSITIONAL ARGUMENTS
    

`DOMAIN`
     A valid domain which may begin with a wildcard, such as: `example.com` or `*.example.com`
FLAGS
    

`--certificate-id`=`CERTIFICATE_ID`
     A certificate id to use for this domain. May not be used on a domain mapping with automatically managed certificates. Use the `[gcloud app ssl-certificates list](https://docs.cloud.google.com/sdk/gcloud/reference/app/ssl-certificates/list)` to see available certificates for this app. 
`--certificate-management`=`CERTIFICATE_MANAGEMENT`
     Type of certificate management. 'automatic' will provision an SSL certificate automatically while 'manual' requires the user to provide a certificate id to provision. `CERTIFICATE_MANAGEMENT` must be one of: `automatic`, `manual`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud app domain-mappings create](https://docs.cloud.google.com/sdk/gcloud/reference/app/domain-mappings/create)
    
    
    [gcloud beta app domain-mappings create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
