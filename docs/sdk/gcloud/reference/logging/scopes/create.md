---
url: https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes/create/
title: gcloud logging scopes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:59:58.716965+00:00
---

# gcloud logging scopes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud logging scopes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud logging scopes create - create a log scope 
SYNOPSIS
    

`gcloud logging scopes create` `LOG_SCOPE_ID` `--resource-names`=[`RESOURCE_NAMES`,…] [`--description`=`DESCRIPTION`] [`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     After creating a log scope, you can use it to view logs in 1 or more resources. 
EXAMPLES
     To create a log scope in a project, run: 
    
    
    gcloud logging scopes create my-scope --resource-names=projects/my-project

To create a log scope in a project with a description, run: 
    
    
    gcloud logging scopes create my-scope --resource-names=projects/my-project --description="my
    custom log scope"

To create a log scope that contains more than 1 resource, such as projects and views, run: 
    
    
    gcloud logging scopes create my-scope --resource-names=projects/my-project,projects/my-project2, projects/my-project/locations/global/buckets/my-bucket/views/my-view1, projects/my-project/locations/global/buckets/my-bucket/views/my-view2,

POSITIONAL ARGUMENTS
    

`LOG_SCOPE_ID`
     ID of the log scope to create. 
REQUIRED FLAGS
    

`--resource-names`=[`RESOURCE_NAMES`,…]
     Comma-separated list of resource names in this log scope. It could be one or more parent resources or one or more views. A log scope can include a maximum of 50 projects and a maximum of 100 resources in total. For example, projects/[PROJECT_ID], projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]` `
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     A textual description for the log scope. 
At most one of these can be specified: 

`--folder`=`FOLDER_ID`
     Folder of the log scope to create. 
`--organization`=`ORGANIZATION_ID`
     Organization of the log scope to create. 
`--project`=`PROJECT_ID`
     Project of the log scope to create. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
