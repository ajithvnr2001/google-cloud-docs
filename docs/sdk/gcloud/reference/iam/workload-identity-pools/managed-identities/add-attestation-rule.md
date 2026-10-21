---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/add-attestation-rule/
title: gcloud iam workload-identity-pools managed-identities add-attestation-rule \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:15:51.596431+00:00
---

# gcloud iam workload-identity-pools managed-identities add-attestation-rule  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/add-attestation-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam workload-identity-pools managed-identities add-attestation-rule Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam workload-identity-pools managed-identities add-attestation-rule - add an attestation rule on a workload identity pool managed identity 
SYNOPSIS
    

`gcloud iam workload-identity-pools managed-identities add-attestation-rule` (`MANAGED_IDENTITY` : `--location`=`LOCATION` `--namespace`=`NAMESPACE` `--workload-identity-pool`=`WORKLOAD_IDENTITY_POOL`) `--google-cloud-resource`=`GOOGLE_CLOUD_RESOURCE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Add an attestation rule on a workload identity pool managed identity. 
EXAMPLES
     The following command adds an attestation rule with a Google Cloud resource on a workload identity pool managed identity `my-managed-identity`. 
    
    
    [gcloud iam workload-identity-pools managed-identities](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities) add-attestation-rule my-managed-identity --namespace="my-namespace" --workload-identity-pool="my-workload-identity-pool" --location="global" --google-cloud-resource="//compute.googleapis.com/projects/123/type/Instance/attached_service_account.uid/12345"

POSITIONAL ARGUMENTS
    

Workload identity pool managed identity resource - The workload identity pool managed identity to add attestation rule on. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `managed_identity` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MANAGED_IDENTITY`
     ID of the workload identity pool managed identity or fully qualified identifier for the workload identity pool managed identity. 

To set the `managed_identity` attribute: 

  * provide the argument `managed_identity` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `managed_identity` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--namespace`=`NAMESPACE`
     The ID to use for the namespace. This value must be 2-63 characters, and may contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `namespace` attribute: 

  * provide the argument `managed_identity` on the command line with a fully specified name; 
  * provide the argument `--namespace` on the command line. 


`--workload-identity-pool`=`WORKLOAD_IDENTITY_POOL`
     The ID to use for the pool, which becomes the final component of the resource name. This value should be 4-32 characters, and may contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `workload-identity-pool` attribute: 

  * provide the argument `managed_identity` on the command line with a fully specified name; 
  * provide the argument `--workload-identity-pool` on the command line. 


REQUIRED FLAGS
    

`--google-cloud-resource`=`GOOGLE_CLOUD_RESOURCE`
     A single workload operating on Google Cloud. This will be set in the attestation rule to be added. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
