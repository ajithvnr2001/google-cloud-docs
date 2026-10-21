---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/access-policies/describe/
title: gcloud beta iam access-policies describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:44.315268+00:00
---

# gcloud beta iam access-policies describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/access-policies/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam access-policies describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam access-policies describe - get AccessPolicy instance 
SYNOPSIS
    

`gcloud beta iam access-policies describe` (`ACCESS_POLICY` : `--folder`=`FOLDER` `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get AccessPolicy instance. 
EXAMPLES
     To get the details of a single policy `my-policy` in organization `123`, run: 
    
    
    gcloud beta iam access-policies describe my-policy --organization=123 --location=global

POSITIONAL ARGUMENTS
    

AccessPolicy resource - The name of the access policy to retrieve. 

Format: `projects/{project_id}/locations/{location}/accessPolicies/{access_policy_id}` `projects/{project_number}/locations/{location}/accessPolicies/{access_policy_id}` `folders/{folder_id}/locations/{location}/accessPolicies/{access_policy_id}` `organizations/{organization_id}/locations/{location}/accessPolicies/{access_policy_id}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `access_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [iam.folders.locations.accessPolicies, iam.organizations.locations.accessPolicies, iam.projects.locations.accessPolicies]. 



This must be specified. 

`ACCESS_POLICY`
     ID of the accessPolicy or fully qualified identifier for the accessPolicy. 

To set the `access_policy` attribute: 

  * provide the argument `access_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     The folder id of the accessPolicy resource. 

To set the `folder` attribute: 

  * provide the argument `access_policy` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [iam.folders.locations.accessPolicies]. 


`--location`=`LOCATION`
     The location id of the accessPolicy resource. 

To set the `location` attribute: 

  * provide the argument `access_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization id of the accessPolicy resource. 

To set the `organization` attribute: 

  * provide the argument `access_policy` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [iam.organizations.locations.accessPolicies]. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v3beta` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud iam access-policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/iam/access-policies/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
