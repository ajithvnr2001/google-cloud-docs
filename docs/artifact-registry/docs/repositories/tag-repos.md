---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos/
title: Tag repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:20.329119+00:00
---

# Tag repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Tag repositories Stay organized with collections  Save and categorize content based on your preferences. 

Use tags to group repositories and other resources across Google Cloud for reporting, auditing, and access control within your Google Cloud organization.

To group repositories within Artifact Registry for automation and billing purposes, use [labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos). Tags and labels work independently of each other, and you can apply both to the same repository. For more information on the differences between tags and labels see [Tags and labels](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels).

## What are tags?

Tags are key-value pairs you can apply to your resources for fine-grained access control.

Project administrators create tags for resources across Google Cloud at the organization level and manage them in [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). When you attach a tag to a Artifact Registry repository, you can use the tag with IAM conditions to grant conditional access to the repository. You cannot attach tags to individual artifacts.

Keep these restrictions in mind:

  * [Organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) can conditionally reference tags that are inherited from the parent project and higher, but they don't support tags that you directly attach to repositories.

  * [Cloud Audit logs](https://docs.cloud.google.com/artifact-registry/docs/audit-logging) are not generated for attaching tags and viewing tag bindings on repositories.




For more information about tags and conditional access control with tags, see [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control).

## Required permissions

To get the permissions that you need to manage tags, ask your administrator to grant you the following IAM roles: 

  * [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) on the resources the tags are attached to
  * View and manage tags at the organization level: [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`) on the organization 
  * Create, update, and delete tag definitions: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on the resource you're creating, updating, or deleting tags for 
  * Attach and remove tags from resources: [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value and the resources that you are attaching or removing the tag value to 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Attaching tags to repositories

After a project administrator [creates tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating), you can attach tags to a repository. Each tag has a key and a value. You tag a repository by binding a value to the repository.

To attach a tag to a repository:

###  Console 

  1. Obtain the tag value to attach from your administrator.

You can attach a tag value with one of these [types of identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions):

     * A _namespaced name_ , such as `123456789012/env/dev`
     * A _permanent ID_ , such as `tagValues/567890123456`
  2. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  3. Select the repository you want to tag.

  4. In the **Repository Details** section, click **Show more**.

Existing tags for the repository, including inherited tags, are shown.

  5. Click the ![Edit](https://docs.cloud.google.com/static/artifact-registry/docs/images/pencil-icon.png)**Edit tags** icon.

  6. In the **Direct tags** section, click **Select scope**.

  7. Select your repository project.

  8. In the **key** field, type to filter the tag list, then select the tag key.

  9. In the **Value** field, type to filter the tag list, then select the tag value.

  10. Click **Save**.

  11. Click **Confirm**.

The tag is attached to your repository.




###  gcloud CLI 

  1. Obtain the tag value to attach from your administrator.

You can attach a tag value with one of these [types of identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions):

     * A _namespaced name_ , such as `123456789012/env/dev`
     * A _permanent ID_ , such as `tagValues/567890123456`
  2. Attach the tag value with the following command:
         
         gcloud resource-manager tags bindings create \
             --tag-value=TAG_VALUE \
             --parent=REPOSITORY_ID \
             --location=LOCATION
         

Replace the following values:

     * `TAG_VALUE` is the permanent ID or namespaced name of the tag value to attach.

     * `REPOSITORY_ID` is the full ID of the repository, including the API domain name to identify the type of resource (`//artifactregistry.googleapis.com/`). For example, `//artifactregistry.googleapis.com/projects/my-project/locations/us-east1/repositories/my-repo`

     * `LOCATION` is the [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repository.

Consider the following example:

     * Tag value: `815471563813/env/dev`
     * Project: `my-project`
     * Repository: `my-repo`
     * Repository location: `us-east1`

The following gcloud CLI command attaches the tag to the repository:
    
    gcloud resource-manager tags bindings create \
        --tag-value=815471563813/env/dev \
        --parent=//artifactregistry.googleapis.com/projects/my-project/locations/us-east1/repositories/my-repo \
        --location=us-east1
    




## Listing tags attached to repositories

You can list tags that are attached to a resource that you have permissions to access.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Select the repository you want to view.

  3. In the **Repository Details** section, click **Show more**.

The **Tags** list shows all repository tags including direct tags, and inherited tags from higher in the resource hierarchy.




###  gcloud CLI 

To list tags attached to a repository, run the following command:
    
    
    gcloud resource-manager tags bindings list \
            --parent=REPOSITORY_ID \
            --location=LOCATION
    

The command only lists tags directly attached to the specified resource, so it doesn't return tags inherited from the parent project or higher. You can list tags inherited from the parent project by specifying a project instead of a repository with the `--parent` flag.

For example, this command lists tags attached to the repository `my-repo` in the project `my-project` and the location `us-east1`:
    
    
    gcloud resource-manager tags bindings list \
        --parent=//artifactregistry.googleapis.com/projects/my-project/locations/us-east1/repositories/my-repo \
        --location=us-east1
    

This command lists tags attached to the project number `7890123456`:
    
    
    gcloud resource-manager tags bindings list \
        --parent=//cloudresourcemanager.googleapis.com/projects/7890123456 \
    

## Detaching tags from repositories

You can detach a tag that is directly attached to a repository. If you need to remove a tag that is inherited from the parent project or another part of the resource hierarchy, a project administrator must [detach](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#detaching) it from the resource where the tag is attached.

To remove a tag that is attached to a repository:

###  Console 

  1. Obtain the tag value you want to remove. If you don't know the tag value, list tags attached to the repository.

  2. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  3. Select the repository.

  4. In the **Repository Details** section, click **Show more**.

Existing tags for the repository, including inherited tags, are shown.

  5. Click the ![Edit](https://docs.cloud.google.com/static/artifact-registry/docs/images/pencil-icon.png)**Edit tags** icon.

  6. In the **Direct tags** section, locate the tag you want to remove.

  7. Click the delete **delete** icon next to the tag you want to remove.

  8. Click **Save**.

  9. Click **Confirm**.

The tag is removed from your repository.




###  gcloud CLI 

  1. Obtain the tag value you want to remove. If you don't know the tag value, list tags attached to the repository.

  2. Detach the tag value with the following command:
         
         gcloud resource-manager tags bindings delete \
             --tag-value=TAG_VALUE \
             --parent=REPOSITORY_ID \
             --location=LOCATION
         

Replace the following values:

     * `TAG_VALUE` tag value to detach.

     * `REPOSITORY_ID` is the full ID of the repository, including the API domain name to identify the type of resource (`//artifactregistry.googleapis.com/`). For example, `//artifactregistry.googleapis.com/projects/my-project/my-repo`

     * `LOCATION` is the [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repository.

Consider the following example:

     * Tag value: `815471563813/env/dev`
     * Project: `my-project`
     * Repository: `my-repo`
     * Repository location: `us-east1`

The following gcloud CLI command detaches the tag from the repository:
    
    gcloud resource-manager tags bindings delete \
        --tag-value=815471563813/env/dev \
        --parent=//artifactregistry.googleapis.com/projects/my-project/locations/us-east1/repositories/my-repo \
        --location=us-east1
    




## What's next

  * Learn about [repository labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
