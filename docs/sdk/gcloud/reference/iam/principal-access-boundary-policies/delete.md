---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete/
title: gcloud iam principal-access-boundary-policies delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:15:39.783673+00:00
---

# gcloud iam principal-access-boundary-policies delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam principal-access-boundary-policies delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam principal-access-boundary-policies delete - delete PrincipalAccessBoundaryPolicy instance 
SYNOPSIS
    

`gcloud iam principal-access-boundary-policies delete` (`PRINCIPAL_ACCESS_BOUNDARY_POLICY` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--async`] [`--etag`=`ETAG`] [`--force`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete PrincipalAccessBoundaryPolicy instance. 
EXAMPLES
     To delete `my-policy` instance in organization `123`, run: 
    
    
    gcloud iam principal-access-boundary-policies delete my-policy --organization=123 --location=global

POSITIONAL ARGUMENTS
    

PrincipalAccessBoundaryPolicy resource - The name of the principal access boundary policy to delete. 

Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}` The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`PRINCIPAL_ACCESS_BOUNDARY_POLICY`
     ID of the principalAccessBoundaryPolicy or fully qualified identifier for the principalAccessBoundaryPolicy. 

To set the `principal_access_boundary_policy` attribute: 

  * provide the argument `principal_access_boundary_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the principalAccessBoundaryPolicy resource. 

To set the `location` attribute: 

  * provide the argument `principal_access_boundary_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization id of the principalAccessBoundaryPolicy resource. 

To set the `organization` attribute: 

  * provide the argument `principal_access_boundary_policy` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--etag`=`ETAG`
     The etag of the principal access boundary policy. If this is provided, it must match the server's etag. 
`--force`
     If set to true, the request will force the deletion of the policy even if the policy is referenced in policy bindings. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v3` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This variant is also available: 
    
    
    [gcloud beta iam principal-access-boundary-policies delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/principal-access-boundary-policies/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
