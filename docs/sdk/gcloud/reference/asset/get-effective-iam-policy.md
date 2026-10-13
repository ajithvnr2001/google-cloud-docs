---
url: https://docs.cloud.google.com/sdk/gcloud/reference/asset/get-effective-iam-policy/
title: gcloud asset get-effective-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:25.024495+00:00
---

# gcloud asset get-effective-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/asset/get-effective-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud asset get-effective-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud asset get-effective-iam-policy - get effective IAM policies for a specified list of resources within accessible scope, such as a project, folder or organization 
SYNOPSIS
    

`gcloud asset get-effective-iam-policy` `--names`=`NAMES`,[`NAMES`,…] `--scope`=`SCOPE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Batch get effective IAM policies that match a request. 
EXAMPLES
     To list effective IAM policies of 1 resource in an organization, run: 
    
    
    gcloud asset get-effective-iam-policy --scope=organizations/YOUR_ORG_ID --names=RESOURCE_NAME1

To list effective IAM policies of 2 resources in a folder, run: 
    
    
    gcloud asset get-effective-iam-policy --scope=folders/YOUR_FOLDER_ID --names=RESOURCE_NAME1,RESOURCE_NAME2

To list effective IAM policies of 3 resources in a project using project ID, run: 
    
    
    gcloud asset get-effective-iam-policy --scope=projects/YOUR_PROJECT_ID --names=RESOURCE_NAME1,RESOURCE_NAME2,RESOURCE_NAME3

To list effective IAM policies of 2 resources in a project using project number, run: 
    
    
    gcloud asset get-effective-iam-policy --scope=projects/YOUR_PROJECT_NUMBER --names=RESOURCE_NAME1,RESOURCE_NAME2

REQUIRED FLAGS
    

`--names`=`NAMES`,[`NAMES`,…]
     Names refer to a list of [full resource names](https://cloud.google.com/asset-inventory/docs/resource-name-format) of [searchable asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types). For each batch call, total number of names provided is between 1 and 20. 

The example value is: 

  * `//cloudsql.googleapis.com/projects/{PROJECT_ID}/instances/{INSTANCE}` (e.g. ``//cloudsql.googleapis.com/projects/probe-per-rt-project/instances/instance1``) 


`--scope`=`SCOPE`
     Scope can be a project, a folder, or an organization. The search is limited to the IAM policies within this scope. The caller must be granted the ``cloudasset.assets.analyzeIamPolicy``, ``cloudasset.assets.searchAllResources``, ``cloudasset.assets.searchAllIamPolicies`` permissions on the desired scope. 

The allowed values are: 

  * `projects/{PROJECT_ID}` (e.g. ``projects/foo-bar``) 
  * `projects/{PROJECT_NUMBER}` (e.g. ``projects/12345678``) 
  * `folders/{FOLDER_NUMBER}` (e.g. ``folders/1234567``) 
  * `organizations/{ORGANIZATION_NUMBER}` (e.g. ``organizations/123456``) 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
