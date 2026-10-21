---
url: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-permissions/describe/
title: gcloud access-context-manager supported-permissions describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:27:33.263118+00:00
---

# gcloud access-context-manager supported-permissions describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-permissions/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud access-context-manager supported-permissions describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud access-context-manager supported-permissions describe - describes which permissions in a provided role are supported by VPC Service Controls 
SYNOPSIS
    

`gcloud access-context-manager supported-permissions describe` `ROLE_ID` [`--organization`=`ORGANIZATION` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describes which permissions in a provided role are supported by VPC Service Controls. 
EXAMPLES
     To describe which permissions VPC Service Controls supports for a provided role, run: 
    
    
    gcloud access-context-manager supported-permissions describe roles/example.role.name

This command prints out a list of all supported permissions in a tabular form: 
    
    
    ROLE NAME               SUPPORT STATUS SUPPORTED PERMISSIONS
    roles/example.role.name SUPPORTED      example.permission.one
                                           example.permission.two

To describe which permissions VPC Service Controls supports for a custom role, run: 
    
    
    gcloud access-context-manager supported-permissions describe TestCustomRole --project=example-project

NOTE: If the provided role is a custom role, an organization or project must be specified. 

This command prints out a list of all supported permissions in a tabular form: 
    
    
    ROLE NAME                                      SUPPORT STATUS SUPPORTED PERMISSIONS
    projects/example-project/roles/TestCustomRole  SUPPORTED      example.permission.one

POSITIONAL ARGUMENTS
    

`ROLE_ID`
     ID of the role to describe. Curated roles example: roles/viewer. Custom roles example: CustomRole. For custom roles, you must also specify the `--organization` or `--project` flag. 
FLAGS
    

At most one of these can be specified: 

`--organization`=`ORGANIZATION`
     Organization of the role you want to describe. 
`--project`=`PROJECT_ID`
     Project of the role you want to describe. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha access-context-manager supported-permissions describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-permissions/describe)
    
    
    [gcloud beta access-context-manager supported-permissions describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-permissions/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
