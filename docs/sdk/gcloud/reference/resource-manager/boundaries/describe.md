---
url: https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/boundaries/describe/
title: gcloud resource-manager boundaries describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:28:33.855094+00:00
---

# gcloud resource-manager boundaries describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/boundaries/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud resource-manager boundaries describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud resource-manager boundaries describe - describe a boundary 
SYNOPSIS
    

`gcloud resource-manager boundaries describe` (`BOUNDARY` : `--folder`=`FOLDER` `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud resource-manager boundaries describe` describes a boundary given its ID and parent or its full resource name. 
EXAMPLES
     To describe a boundary with ID `my-boundary` in an organization with ID `123456789012`, run: 
    
    
    gcloud resource-manager boundaries describe my-boundary --organization=123456789012

To describe a boundary by full resource name, run: 
    
    
    gcloud resource-manager boundaries describe organizations/123456789012/boundaries/my-boundary

POSITIONAL ARGUMENTS
    

Boundary resource - The boundary to describe. The arguments in this group can be used to specify the attributes of this resource. This resource can be one of the following types: [cloudresourcemanager.organizations.boundaries, cloudresourcemanager.folders.boundaries]. 

This must be specified. 

`BOUNDARY`
     ID of the boundary or fully qualified identifier for the boundary. 

To set the `boundary` attribute: 

  * provide the argument `boundary` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     Folder ID or full resource name of the boundary. 

To set the `folder` attribute: 

  * provide the argument `boundary` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [cloudresourcemanager.folders.boundaries]. 


`--organization`=`ORGANIZATION`
     Organization ID or full resource name of the boundary. 

To set the `organization` attribute: 

  * provide the argument `boundary` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [cloudresourcemanager.organizations.boundaries]. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha resource-manager boundaries describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/boundaries/describe)
    
    
    [gcloud beta resource-manager boundaries describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/boundaries/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
