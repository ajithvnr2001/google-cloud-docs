---
url: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/describe/
title: gcloud access-context-manager cloud-bindings describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:12.292402+00:00
---

# gcloud access-context-manager cloud-bindings describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud access-context-manager cloud-bindings describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud access-context-manager cloud-bindings describe - show details about a cloud access binding 
SYNOPSIS
    

`gcloud access-context-manager cloud-bindings describe` (`--binding`=`BINDING` : `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Show details about an existing cloud access binding. 
EXAMPLES
     To get details about an existing cloud access binding, run: 
    
    
    gcloud access-context-manager cloud-bindings describe --binding=binding-id

REQUIRED FLAGS
    

Cloud access binding resource - The cloud access binding you want to show details about The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--binding`=`BINDING`
     ID of the cloud-access-binding or fully qualified identifier for the cloud-access-binding. 

To set the `binding` attribute: 

  * provide the argument `--binding` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     The ID of the organization. To set the `organization` attribute: 

  * provide the argument `--binding` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property `access_context_manager/organization`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha access-context-manager cloud-bindings describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
