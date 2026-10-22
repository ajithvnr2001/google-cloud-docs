---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/list-repos/
title: View and list repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:37.127573+00:00
---

# View and list repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/list-repos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  View and list repositories Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you view and list repositories in your Google Cloud project to inspect available artifact locations and configuration details.

## Before you begin

Optional: [Configure defaults for Google Cloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).

### Required roles

To get the permissions that you need to view and list repositories, ask your administrator to grant you the following IAM roles: 

  * View and list all repositories in a Google Cloud project: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the project 
  * View a specific repository: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the repository 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view and list repositories. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view and list repositories:

  * `artifactregistry.repositories.get`
  * `artifactregistry.repositories.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Viewing repositories

You can view repositories within a Google Cloud project.

To view a list of repositories:

###  Console 

Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

The page displays a list of your repositories.

To filter the Artifact Registry repository list:

  1. Above the repository list, click **Filter Table**.
  2. Choose a filter from the filter list.
  3. Specify the value that you want to use for filtering the list.



###  gcloud 

To list existing repositories, run the following command:
    
    
    gcloud artifacts repositories list [--project=PROJECT] \
    [--location=LOCATION]

To view the type of encryption configured for a repository, run the following command:
    
    
    gcloud artifacts repositories describe REPOSITORY \
    [--project=PROJECT] [--location=LOCATION]

In the previous commands, replace the following values:

  * `PROJECT` is the project ID. If this flag is omitted, the current or default project is used.
  * `REPOSITORY` is the name of the repository.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. Use the `--location` flag to view repositories in a specific location. You can also use `--location=all` to list repositories across all locations.

If you omit this flag, the command uses the [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set) location if a default is configured. Otherwise, omitting this flag lists repositories across all locations.




For more information about the command, run the following command:
    
    
     gcloud artifacts repositories list --help
    

## What's next

  * Configure [access](https://docs.cloud.google.com/artifact-registry/docs/access-control) to your repositories. 
  * [Download individual files](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files) within artifacts stored in your repositories. 
  * Learn to [restrict artifact downloads with download rules](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
