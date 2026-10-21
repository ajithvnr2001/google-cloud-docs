---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/enforce/
title: gcloud beta access-context-manager perimeters dry-run enforce \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:01.900669+00:00
---

# gcloud beta access-context-manager perimeters dry-run enforce  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/enforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta access-context-manager perimeters dry-run enforce Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta access-context-manager perimeters dry-run enforce - enforces a Service Perimeter's dry-run configuration 
SYNOPSIS
    

`gcloud beta access-context-manager perimeters dry-run enforce` (`PERIMETER` : `--policy`=`POLICY`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Copies a Service Perimeter's dry-run mode configuration to its enforcement mode configuration and unsets the explicit dry-run spec. After this operation succeeds, the Service Perimeter will not have an explicit dry-run mode configuration, and, instead, the previous dry-run mode configuration will become the enforcement mode configuration. The operation will not be performed if there is no explicit dry-run mode configuration or if the dry-run mode configuration is incompatible with the overall enforcement mode VPC Service Controls policy. 
EXAMPLES
     To enforce the dry-run mode configuration for a Service Perimeter: 
    
    
    gcloud beta access-context-manager perimeters dry-run enforce my-perimeter

POSITIONAL ARGUMENTS
    

Perimeter resource - The service perimeter to reset. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`PERIMETER`
     ID of the perimeter or fully qualified identifier for the perimeter. 

To set the `perimeter` attribute: 

  * provide the argument `perimeter` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--policy`=`POLICY`
     The ID of the access policy. 

To set the `policy` attribute: 

  * provide the argument `perimeter` on the command line with a fully specified name; 
  * provide the argument `--policy` on the command line; 
  * set the property `access_context_manager/policy`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud access-context-manager perimeters dry-run enforce](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/enforce)
    
    
    [gcloud alpha access-context-manager perimeters dry-run enforce](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/enforce)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
