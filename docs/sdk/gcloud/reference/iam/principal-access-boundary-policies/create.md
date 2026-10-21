---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create/
title: gcloud iam principal-access-boundary-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:35:28.319084+00:00
---

# gcloud iam principal-access-boundary-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam principal-access-boundary-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam principal-access-boundary-policies create - create PrincipalAccessBoundaryPolicy instance 
SYNOPSIS
    

`gcloud iam principal-access-boundary-policies create` (`PRINCIPAL_ACCESS_BOUNDARY_POLICY` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--annotations`=[`ANNOTATIONS`,…]] [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--etag`=`ETAG`] [[`--details-rules`=[`description`=`DESCRIPTION`],[`effect`=`EFFECT`],[`resources`=`RESOURCES`] : `--details-enforcement-version`=`DETAILS_ENFORCEMENT_VERSION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create PrincipalAccessBoundaryPolicy instance. 
EXAMPLES
     To create a policy instance called `my-policy`, run: 
    
    
    gcloud iam principal-access-boundary-policies create my-policy --organization=123 --location=global

POSITIONAL ARGUMENTS
    

PrincipalAccessBoundaryPolicy resource - Identifier. The resource name of the principal access boundary policy. 

The following format is supported: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{policy_id}` The arguments in this group can be used to specify the attributes of this resource. 

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
    

`--annotations`=[`ANNOTATIONS`,…]
     User defined annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitations. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --annotations=string=string

`JSON Example:`
    
    
    --annotations='{"string": "string"}'

`File Example:`
    
    
    --annotations=path_to_file.(yaml|json)

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     The description of the principal access boundary policy. Must be less than or equal to 63 characters. 
`--etag`=`ETAG`
     The etag for the principal access boundary. If this is provided on update, it must match the server's etag. 
Principal access boundary policy details 
`--details-rules`=[`description`=`DESCRIPTION`],[`effect`=`EFFECT`],[`resources`=`RESOURCES`]
     Required, A list of principal access boundary policy rules. The number of rules in a policy is limited to 500. 

`description`
     The description of the principal access boundary policy rule. Must be less than or equal to 256 characters. 
`effect`
     The access relationship of principals to the resources in this rule. 
`resources`
     A list of Resource Manager resources. If a resource is listed in the rule, then the rule applies for that resource and its descendants. The number of resources in a policy is limited to 500 across all rules in the policy. 

The following resource types are supported: 

  * Organizations, such as `//cloudresourcemanager.googleapis.com/organizations/123`. 
  * Folders, such as `//cloudresourcemanager.googleapis.com/folders/123`. 
  * Projects, such as `//cloudresourcemanager.googleapis.com/projects/123` or `//cloudresourcemanager.googleapis.com/projects/my-project-id`. 


`Shorthand Example:`
    
    
    --details-rules=description=string,effect=string,resources=[string] --details-rules=description=string,effect=string,resources=[string]

`JSON Example:`
    
    
    --details-rules='[{"description": "string", "effect": "string", "resources": ["string"]}]'

`File Example:`
    
    
    --details-rules=path_to_file.(yaml|json)

This flag argument must be specified if any of the other arguments in this group are specified. 

`--details-enforcement-version`=`DETAILS_ENFORCEMENT_VERSION`
     The version number (for example, `1` or `latest`) that indicates which permissions are able to be blocked by the policy. If empty, the PAB policy version will be set to the most recent version number at the time of the policy's creation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v3` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This variant is also available: 
    
    
    [gcloud beta iam principal-access-boundary-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/principal-access-boundary-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
