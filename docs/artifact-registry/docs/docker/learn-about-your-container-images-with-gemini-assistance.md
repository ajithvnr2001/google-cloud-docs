---
url: https://docs.cloud.google.com/artifact-registry/docs/docker/learn-about-your-container-images-with-gemini-assistance/
title: Learn about your container images with Gemini assistance \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:01.917852+00:00
---

# Learn about your container images with Gemini assistance  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/docker/learn-about-your-container-images-with-gemini-assistance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Learn about your container images with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview —[Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use Gemini Cloud Assist to list your Artifact Registry repositories and container images stored in Docker-format repositories.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Limitations

Your Google Cloud project must be created in an [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. If you don't have any container images stored in an Artifact Registry repository, then follow the instructions in [Store Docker container images in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images).
  3. [Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).
  4. Ensure that you have the necessary Identity and Access Management (IAM) permissions to complete the tasks in this document.



### Required roles

To get the permissions that you need to list repositories and container images in Artifact Registry, ask your administrator to grant you the [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) IAM role on the project or repository. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Open Gemini Cloud Assist chat

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

You can open the **Cloud Assist** panel to use Gemini Cloud Assist chat from anywhere in the Google Cloud console.

  1. In the Google Cloud console, select a project where you have container images stored in Artifact Registry.  


[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. To open the **Cloud Assist** panel, click spark **Open or close Gemini AI chat**.

  3. To enter a prompt, type the prompt and click send **Send prompt**.



## List repositories

You can prompt Gemini Cloud Assist to list repositories in the current project and filter the response by the following:

  * **Location** (required). The [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repositories you want to list.
  * **Labels** (optional). [Labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos) are key-value pairs that are used to organize resources.
  * **Tags** (optional). [Tags](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos) are used to group repositories and other resources across Google Cloud for reporting, auditing, and access control within your Google Cloud organization.



To list repositories, do the following:

  * In **Gemini Cloud Assist** chat, enter the following prompt:
        
        List repositories in the location LOCATION
        

Replace `LOCATION` with the location of your repositories—for example, `us-west1`.

For example, the following prompt asks Gemini Cloud Assist to list repositories in the region `us-west1` that have the label `env:dev`:
        
        List repositories for us-west1 with the label env:dev
        

The response includes a list of repositories in the specified location that have the label `env:dev`.




## List container images

You can prompt Gemini Cloud Assist to list container images in a Docker [format](https://docs.cloud.google.com/artifact-registry/docs/supported-formats) repository in the current project, and filter the response by the following:

  * **Repository ID** (required). The repository ID.
  * **Location** (required). The location of the repository you want to list images from.
  * **Labels** (optional). [Labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos) are key-value pairs that are used to organize resources.
  * **Docker tags** (optional). [Docker tags](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags) are used when you push or pull an image to a repository to specify the version of an image.



To list your images in a repository, do the following:

  * In **Gemini Cloud Assist** chat, enter the following prompt:
        
        List my images for REPOSITORY in LOCATION with the tag TAG
        

Replace the following:

    * REPOSITORY: the repository ID
    * LOCATION: the location of the repository—for example, `us-west1`
    * TAG: a Docker tag—for example, `latest`

The response includes a list of images that have the specified tag, repository, and location.




## What's next

  * Learn more about [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
