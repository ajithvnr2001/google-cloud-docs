---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/assured/workloads/describe/
title: gcloud beta assured workloads describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:38.610623+00:00
---

# gcloud beta assured workloads describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/assured/workloads/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta assured workloads describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta assured workloads describe - describe Assured Workloads environment 
SYNOPSIS
    

`gcloud beta assured workloads describe` (`WORKLOAD` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--version`=`VERSION`; default="v1"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Obtain details about a given Assured Workloads environment. 
EXAMPLES
     To describe an Assured Workloads environment in the us-central1 region, belonging to an organization with ID 123, with workload ID 456, run: 
    
    
    gcloud beta assured workloads describe organizations/123/locations/us-central1/workloads/456

To describe an Assured Workloads V2 environment: 
    
    
    gcloud beta assured workloads describe organizations/123/locations/us-central1/workloads/456 --version=v2

POSITIONAL ARGUMENTS
    

Workload resource - The Assured Workloads environment resource to describe. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`WORKLOAD`
     ID of the workload or fully qualified identifier for the workload. 

To set the `workload` attribute: 

  * provide the argument `workload` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the workload. 

To set the `location` attribute: 

  * provide the argument `workload` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The parent organization for the workload. 

To set the `organization` attribute: 

  * provide the argument `workload` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


FLAGS
    

`--version`=`VERSION`; default="v1"
     Assured Workloads API version to use. Options are v1 and v2. Defaults to v1. `VERSION` must be one of: `v1`, `v2`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud assured workloads describe](https://docs.cloud.google.com/sdk/gcloud/reference/assured/workloads/describe)
    
    
    [gcloud alpha assured workloads describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
