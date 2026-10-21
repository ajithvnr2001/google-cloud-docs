---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset/analyze-iam-policy/
title: gcloud alpha asset analyze-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:47.454109+00:00
---

# gcloud alpha asset analyze-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset/analyze-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha asset analyze-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha asset analyze-iam-policy - ALPHA version, Analyzes IAM policies that match a request 
SYNOPSIS
    

`gcloud alpha asset analyze-iam-policy` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`--access-time`=`ACCESS_TIME`] [`--full-resource-name`=`FULL_RESOURCE_NAME`] [`--identity`=`IDENTITY`] [`--saved-analysis-query`=`SAVED_ANALYSIS_QUERY`] [`--analyze-service-account-impersonation` `--execution-timeout`=`EXECUTION_TIMEOUT` `--expand-groups` `--expand-resources` `--expand-roles` `--include-deny-policy-analysis` `--output-group-edges` `--output-resource-edges` `--show-response`] [`--permissions`=[`PERMISSIONS`,…] `--roles`=[`ROLES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Analyzes IAM policies that match a request. 
EXAMPLES
     To find out which users have been granted the iam.serviceAccounts.actAs permission on a service account, run: 
    
    
    gcloud alpha asset analyze-iam-policy --organization=YOUR_ORG_ID --full-resource-name=YOUR_SERVICE_ACCOUNT_FULL_RESOURCE_NAME --permissions='iam.serviceAccounts.actAs'

To find out which resources a user can access, run: 
    
    
    gcloud alpha asset analyze-iam-policy --organization=YOUR_ORG_ID --identity='user:u1@foo.com'

To find out which roles or permissions a user has been granted on a project, run: 
    
    
    gcloud alpha asset analyze-iam-policy --organization=YOUR_ORG_ID --full-resource-name=YOUR_PROJECT_FULL_RESOURCE_NAME --identity='user:u1@foo.com'

To find out which users have been granted the iam.serviceAccounts.actAs permission on any applicable resources, run: 
    
    
    gcloud alpha asset analyze-iam-policy --organization=YOUR_ORG_ID --permissions='iam.serviceAccounts.actAs'

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder ID on which to perform the analysis. Only policies defined at or below this folder will be targeted in the analysis. 
`--organization`=`ORGANIZATION_ID`
     Organization ID on which to perform the analysis. Only policies defined at or below this organization will be targeted in the analysis. 
`--project`=`PROJECT_ID`
     Project ID or number on which to perform the analysis. Only policies defined at or below this project will be targeted in the analysis. 
OPTIONAL FLAGS
    

The hypothetical context to evaluate IAM conditions. 
`--access-time`=`ACCESS_TIME`
     The hypothetical access timestamp to evaluate IAM conditions. 
Specifies a resource for analysis. Leaving it empty means ANY. 
`--full-resource-name`=`FULL_RESOURCE_NAME`
     The full resource name. 
Specifies an identity for analysis. Leaving it empty means ANY. 
`--identity`=`IDENTITY`
     The identity appearing in the form of principals in the IAM policy binding. 
Specifies the name of a saved analysis query. 
`--saved-analysis-query`=`SAVED_ANALYSIS_QUERY`
     The name of a saved query. When a `saved_analysis_query` is provided, its query content will be used as the base query. Other flags' values will override the base query to compose the final query to run. IDs might be in one of the following formats: 

  * projects/project_number/savedQueries/saved_query_id` folders/folder_number/savedQueries/saved_query_id` organizations/organization_number/savedQueries/saved_query_id 


The analysis options. 
`--analyze-service-account-impersonation`
     If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use AnalyzeIamPolicyLongrunning rpc instead. Default is false. 
`--execution-timeout`=`EXECUTION_TIMEOUT`
     The amount of time the executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json). Deafult is empty. 
`--expand-groups`
     If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding. Default is false. 
`--expand-resources`
     If true, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy. Default is false. 
`--expand-roles`
     If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions. Default is false. 
`--include-deny-policy-analysis`
     If true, the response will include analysis for deny policies.This is a very expensive operation, because many derived queries will be executed. 
`--output-group-edges`
     If true, the result will output the relevant membership relationships between groups. Default is false. 
`--output-resource-edges`
     If true, the result will output the relevant parent/child relationships between resources. Default is false. 
`--show-response`
     If true, the response will be showed as-is in the command output. 
Specifies roles or permissions for analysis. Leaving it empty means ANY. 
`--permissions`=[`PERMISSIONS`,…]
     The permissions to appear in the result. 
`--roles`=[`ROLES`,…]
     The roles to appear in the result. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud asset analyze-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy)
    
    
    [gcloud beta asset analyze-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/asset/analyze-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
