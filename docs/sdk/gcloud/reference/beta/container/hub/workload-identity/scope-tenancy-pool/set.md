---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/workload-identity/scope-tenancy-pool/set/
title: gcloud beta container hub workload-identity scope-tenancy-pool set \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:31:48.444417+00:00
---

# gcloud beta container hub workload-identity scope-tenancy-pool set  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/workload-identity/scope-tenancy-pool/set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub workload-identity scope-tenancy-pool set Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub workload-identity scope-tenancy-pool set - set Scope Tenancy Pool 
SYNOPSIS
    

`gcloud beta container hub workload-identity scope-tenancy-pool set` `WORKLOAD_IDENTITY_POOL` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Set the scope tenancy pool for a fleet. 
EXAMPLES
     To set the scope tenancy pool using a fully qualified identifier for the Workload Identity Pool: 
    
    
    [gcloud beta container hub workload-identity scope-tenancy-pool](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/workload-identity/scope-tenancy-pool) set projects/my-project/locations/global/workloadIdentityPools/test-pool

To set the scope tenancy pool using a Workload Identity Pool ID and project: 
    
    
    [gcloud beta container hub workload-identity scope-tenancy-pool](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/workload-identity/scope-tenancy-pool) set test-pool --project=my-project

POSITIONAL ARGUMENTS
    

Workloadidentitypool resource - The group of arguments defining a Workload Identity Pool. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `WORKLOAD_IDENTITY_POOL` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `WORKLOAD_IDENTITY_POOL` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 



This must be specified. 

`WORKLOAD_IDENTITY_POOL`
     ID of the workloadidentitypool or fully qualified identifier for the workloadidentitypool. 

To set the `workloadidentitypool` attribute: 

  * provide the argument `WORKLOAD_IDENTITY_POOL` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub workload-identity scope-tenancy-pool set](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/workload-identity/scope-tenancy-pool/set)
    
    
    [gcloud alpha container hub workload-identity scope-tenancy-pool set](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/workload-identity/scope-tenancy-pool/set)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
