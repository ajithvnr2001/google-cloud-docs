---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/create/
title: gcloud alpha projects create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:30:36.934696+00:00
---

# gcloud alpha projects create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha projects create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha projects create - create a new project 
SYNOPSIS
    

`gcloud alpha projects create` [`PROJECT_ID`] [`--no-enable-cloud-apis`] [`--folder`=`FOLDER_ID`] [`--labels`=[`KEY`=`VALUE`,…]] [`--name`=`NAME`] [`--organization`=`ORGANIZATION_ID`] [`--set-as-default`] [`--tags`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a new project with the given project ID. By default, projects are not created under a parent resource. To do so, use either the `--organization` or `--folder` flag. 
EXAMPLES
     The following command creates a project with ID `example-foo-bar-1`, name `Happy project` and label `type=happy`: 
    
    
    gcloud alpha projects create example-foo-bar-1 --name="Happy project" --labels=type=happy

By default, projects are not created under a parent resource. The following command creates a project with ID `example-2` with parent `folders/12345`: 
    
    
    gcloud alpha projects create example-2 --folder=12345

The following command creates a project with ID `example-3` with parent `organizations/2048`: 
    
    
    gcloud alpha projects create example-3 --organization=2048

POSITIONAL ARGUMENTS
    

[`PROJECT_ID`]
     ID for the project you want to create. 

Project IDs are immutable and can be set only during project creation. They must start with a lowercase letter and can have lowercase ASCII letters, digits or hyphens. Project IDs must be between 6 and 30 characters. 

FLAGS
    

`--enable-cloud-apis`
     Enable `cloudapis.googleapis.com` during creation. Enabled by default, use `--no-enable-cloud-apis` to disable. 
`--folder`=`FOLDER_ID`
     ID for the folder to use as a parent 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--name`=`NAME`
     Name for the project you want to create. If not specified, will use project id as name. 
`--organization`=`ORGANIZATION_ID`
     ID for the organization to use as a parent 
`--set-as-default`
     Set newly created project as [core/project] property. 
`--tags`=[`KEY`=`VALUE`,…]
     List of tags KEY=VALUE pairs to bind. Each item must be expressed as `<tag-key-namespaced-name>=<tag-value-short-name>`. 

Example: `123/environment=production,123/costCenter=marketing`

Note: Currently this field is in Preview. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

SEE ALSO
     See <https://support.google.com/cloud/answer/6251787> for information on creating or deleting projects from the Google Cloud Platform Console. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud projects create](https://docs.cloud.google.com/sdk/gcloud/reference/projects/create)
    
    
    [gcloud beta projects create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
