---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/create/
title: gcloud iam workload-identity-pools namespaces create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:15:53.527695+00:00
---

# gcloud iam workload-identity-pools namespaces create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam workload-identity-pools namespaces create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam workload-identity-pools namespaces create - create a workload identity pool namespace 
SYNOPSIS
    

`gcloud iam workload-identity-pools namespaces create` (`NAMESPACE` : `--location`=`LOCATION` `--workload-identity-pool`=`WORKLOAD_IDENTITY_POOL`) [`--async`] [`--description`=`DESCRIPTION`] [`--disabled`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a workload identity pool namespace. 
EXAMPLES
     The following command creates a workload identity pool namespace with the ID `my-namespace`: 
    
    
    gcloud iam workload-identity-pools namespaces create my-namespace --location="global" --workload-identity-pool="my-workload-identity-pool" --description="My namespace description" --disabled

POSITIONAL ARGUMENTS
    

Workload identity pool namespace resource - The workload identity pool namespace to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `namespace` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NAMESPACE`
     ID of the workload identity pool namespace or fully qualified identifier for the workload identity pool namespace. 

To set the `namespace` attribute: 

  * provide the argument `namespace` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `namespace` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--workload-identity-pool`=`WORKLOAD_IDENTITY_POOL`
     The ID to use for the pool, which becomes the final component of the resource name. This value should be 4-32 characters, and may contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `workload-identity-pool` attribute: 

  * provide the argument `namespace` on the command line with a fully specified name; 
  * provide the argument `--workload-identity-pool` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A description of the namespace. 
`--disabled`
     Whether the namespace is disabled. If disabled, credentials may no longer be issued for identities in this namespace. Existing credentials may continue to be accepted until they expire. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
