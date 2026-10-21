---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/kaj-config/describe/
title: gcloud alpha kms kaj-config describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:40.887898+00:00
---

# gcloud alpha kms kaj-config describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/kaj-config/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms kaj-config describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms kaj-config describe - describe the KajPolicyConfig of an organization/folder/project 
SYNOPSIS
    

`gcloud alpha kms kaj-config describe` (`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha kms kaj-config describe can be used to retrieve the KajPolicyConfig, the default KAJ policy, of an organization/folder/project. 
EXAMPLES
     The following command retrieves the KajPolicyConfig of organizations/123: 
    
    
    gcloud alpha kms kaj-config describe --organization=123

The following command retrieves the KajPolicyConfig of folders/456: 
    
    
    gcloud alpha kms kaj-config describe --folder=456

The following command retrieves the KajPolicyConfig of projects/789: 
    
    
    gcloud alpha kms kaj-config describe --project=789

REQUIRED FLAGS
    

The parent of KajPolicyConfig. 

Exactly one of these must be specified: 

`--folder`=`FOLDER`
     The ID of the folder under which the KajPolicyConfig exists. Use this flag only if KajPolicyConfig is directly under a folder. 
`--organization`=`ORGANIZATION`
     The ID of the organization under which the KajPolicyConfig exists. Use this flag only if KajPolicyConfig is directly under an organization. 
`--project`=`PROJECT_ID`
     The ID of the project underwhich the KajPolicyConfig exists. Use this flag only if KajPolicyConfig is directly under a project. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta kms kaj-config describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/kaj-config/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
