---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete/
title: gcloud alpha assured workloads delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:18:24.017488+00:00
---

# gcloud alpha assured workloads delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha assured workloads delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha assured workloads delete - delete Assured Workloads environment 
SYNOPSIS
    

`gcloud alpha assured workloads delete` (`WORKLOAD` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--async`] [`--etag`=`ETAG`] [`--version`=`VERSION`; default="v1"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Delete a given Assured Workloads environment. 
EXAMPLES
     To delete a V1 Assured Workload using a full resource name: 
    
    
    gcloud alpha assured workloads delete organizations/123/locations/us-central1/workloads/456 --etag=789

To delete a V1 Assured Workload using discrete resource flags: 
    
    
    gcloud alpha assured workloads delete 456 --organization=123 --location=us-central1 --etag=789

To delete a V2 Assured Workload using a full resource name: 
    
    
    gcloud alpha assured workloads delete organizations/123/locations/us-central1/workloads/456 --version=v2

To delete a V2 Assured Workload using discrete resource flags: 
    
    
    gcloud alpha assured workloads delete 456 --organization=123 --location=us-central1 --version=v2

To delete a V2 Assured Workload asynchronously: 
    
    
    gcloud alpha assured workloads delete 456 --organization=123 --location=us-central1 --async --version=v2

POSITIONAL ARGUMENTS
    

Workload resource - The Assured Workloads environment resource to delete. The arguments in this group can be used to specify the attributes of this resource. 

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
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--etag`=`ETAG`
     The etag acquired by reading the Assured Workloads environment. 
`--version`=`VERSION`; default="v1"
     Assured Workloads API version to use. Options are v1 and v2. Defaults to v1. `VERSION` must be one of: `v1`, `v2`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud assured workloads delete](https://docs.cloud.google.com/sdk/gcloud/reference/assured/workloads/delete)
    
    
    [gcloud beta assured workloads delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/assured/workloads/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
