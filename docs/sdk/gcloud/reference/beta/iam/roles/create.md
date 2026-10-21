---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/roles/create/
title: gcloud beta iam roles create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:47.230040+00:00
---

# gcloud beta iam roles create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/roles/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam roles create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam roles create - create a custom role for a project or an organization 
SYNOPSIS
    

`gcloud beta iam roles create` `ROLE_ID` (`--organization`=`ORGANIZATION` | `--project`=`PROJECT_ID`) [`--file`=`FILE` | `--description`=`DESCRIPTION` `--permissions`=`PERMISSIONS` `--stage`=`STAGE` `--title`=`TITLE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command creates a custom role with the provided information. 
EXAMPLES
     To create a custom role ``ProjectUpdater`` from a YAML file, run: 
    
    
    gcloud beta iam roles create ProjectUpdater --organization=12345 --file=role_file_path

To create a custom role ``ProjectUpdater`` with flags, run: 
    
    
    gcloud beta iam roles create ProjectUpdater --project=myproject --title=ProjectUpdater --description="Have access to get and update the project" --permissions=resourcemanager.projects.get,resourcemanager.projects.update

POSITIONAL ARGUMENTS
    

`ROLE_ID`
     ID of the custom role to create. You must also specify the `--organization` or `--project` flag. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--organization`=`ORGANIZATION`
     Organization of the role you want to create. 
`--project`=`PROJECT_ID`
     Project of the role you want to create. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

OPTIONAL FLAGS
    

At most one of these can be specified: 

`--file`=`FILE`
     The JSON or YAML file with the IAM Role to create. See <https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles>. 
Or at least one of these can be specified: 

Roles Settings 
`--description`=`DESCRIPTION`
     The description of the role you want to create. 
`--permissions`=`PERMISSIONS`
     The permissions of the role you want to create. Use commas to separate them. 
`--stage`=`STAGE`
     The state of the role you want to create. This represents a role's lifecycle phase: `ALPHA`, `BETA`, `GA`, `DEPRECATED`, `DISABLED`, `EAP`. 
`--title`=`TITLE`
     The title of the role you want to create. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iam roles create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/create)
    
    
    [gcloud alpha iam roles create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/roles/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
