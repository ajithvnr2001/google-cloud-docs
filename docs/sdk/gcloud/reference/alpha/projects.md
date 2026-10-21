---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/
title: gcloud alpha projects \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:00.575528+00:00
---

# gcloud alpha projects  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha projects Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha projects - create and manage project access policies 
SYNOPSIS
    

`gcloud alpha projects` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The gcloud alpha projects group lets you create and manage IAM policies for projects on the Google Cloud Platform. Resources are organized hierarchically and assigned to a particular project. A Project resource is required to use Google Cloud Platform, and forms the basis for creating, enabling and using all Cloud Platform services, managing APIs, enabling billing, adding and removing collaborators, and managing permissions. 

More information on the Cloud Platform Resource Hierarchy and the project resource can be found here: <https://cloud.google.com/resource-manager/docs/creating-managing-organization> and detailed documentation on creating and managing projects can be found here: <https://cloud.google.com/resource-manager/docs/creating-managing-projects>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/add-iam-policy-binding)`
     `(ALPHA)` Add IAM policy binding for a project. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/create)`
     `(ALPHA)` Create a new project. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/delete)`
     `(ALPHA)` Delete a project. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/describe)`
     `(ALPHA)` Show metadata for a project. 
`[get-ancestors](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/get-ancestors)`
     `(ALPHA)` Get the ancestors for a project. 
`[get-ancestors-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/get-ancestors-iam-policy)`
     `(ALPHA)` Get IAM policies for a project and its ancestors. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/get-iam-policy)`
     `(ALPHA)` Get the IAM policy for a project. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/list)`
     `(ALPHA)` List projects for which the user has resourcemanager.projects.list permission. 
`[move](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/move)`
     `(ALPHA)` Move a project into an organization. 
`[remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/remove-iam-policy-binding)`
     `(ALPHA)` Remove IAM policy binding for a project. 
`[search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/search)`
     `(ALPHA)` Search for projects matching the given query. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/set-iam-policy)`
     `(ALPHA)` Set IAM policy for a project. 
`[undelete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/undelete)`
     `(ALPHA)` Undelete a project. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/update)`
     `(ALPHA)` Update the name and/or labels of a project. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud projects](https://docs.cloud.google.com/sdk/gcloud/reference/projects)
    
    
    [gcloud beta projects](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
