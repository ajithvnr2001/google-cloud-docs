---
url: https://docs.cloud.google.com/agent-registry/manage-skill-revisions/
title: Manage skill revisions \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:14.778073+00:00
---

# Manage skill revisions  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/manage-skill-revisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Manage skill revisions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In Agent Registry, a [skill revision](https://docs.cloud.google.com/agent-registry/concepts#skill-revision) represents an immutable, versioned snapshot of a skill package. When you update the code or instructions of a skill, you create a new revision. This decoupled architecture allows for version control of your skills.

This document explains how to create and manage skill revisions. For information about updating the default revision of a specific skill, see [Update skill metadata or default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).

## Before you begin

Before you start, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) and [register a standalone skill](https://docs.cloud.google.com/agent-registry/register-skills). You need [the project ID](https://support.google.com/googleapi/answer/7014113) to perform these tasks.

To use the Google Cloud CLI commands in this document, make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

### Required roles

To get the permissions that you need to manage skill revisions in Agent Registry, ask your administrator to grant you the following IAM roles on the project: 

  * List, view, and download skill revisions: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * Create, update, and delete skill revisions: [Agent Registry User ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.user) (`roles/agentregistry.user`) 
  * Manage skill revisions and other Agent Registry resources: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Other Agent Registry roles might also include the permissions required to view, download, create, update, and delete skill revisions. For more information, see [Agent Registry roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

## Create a skill revision

Creating a new revision uploads a new ZIP payload to the existing skill container. When you create a skill revision, it automatically becomes the active version of the skill. However, you can [update the default revision of a skill](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill) at any time. Only revisions that are active can be downloaded.

For information about pricing and feature costs for skills, see [Agent Registry pricing](https://docs.cloud.google.com/agent-registry/pricing).

The maximum ZIP file size of a skill revision is 500 KB.

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab, and click the name of your skill.
  3. In the **Skill Details** page, locate the **Version history** table.
  4. Click add **Add version**.
  5. In the **Add version** panel, choose one of the following options:

     * **File:** Upload the package or ZIP file containing your code or prompt instructions (`SKILL.md`) file. You can click **Browse** to find your file in your local environment.
     * **Bucket:** Provide a Cloud Storage URI (`gs://...`) containing a valid ZIP bundle. You can click **Browse** to find your file in your Cloud Storage buckets.

**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, for example, if you have never created a skill, trigger its creation for the Agent Registry API by following the steps in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting IAM permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).
  6. Click **Create**.




The **Skill Details** page displays the skill revision in the **Version history** table.

###  gcloud 

You can create a skill revision by uploading either a local ZIP file or importing a package stored in Cloud Storage.

Replace the following:

  * `REVISION_ID`: The ID you want to assign to the skill revision.
  * `SKILL_ID`: The ID of the skill you are using for the revision.
  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.

  * **Upload a local ZIP file** : To create a skill revision using a local ZIP payload:
        
        gcloud alpha agent-registry skills revisions create REVISION_ID \
          --skill=SKILL_ID \
          --project=PROJECT_ID \
          --location=LOCATION \
          --payload="LOCAL_ZIP_PATH"
        

Replace `LOCAL_ZIP_PATH` with the path to your packaged skill archive on your local machine.

  * **Import from a Cloud Storage bucket** : To create a skill revision using a ZIP archive hosted in a Cloud Storage bucket:
        
        gcloud alpha agent-registry skills revisions create REVISION_ID \
          --skill=SKILL_ID \
          --project=PROJECT_ID \
          --location=LOCATION \
          --gcs-source-uri="gs://BUCKET_NAME/SKILL_PACKAGE.zip"
        

**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, for example, if you have never created a skill, trigger its creation for the Agent Registry API by following the steps in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting IAM permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

Replace the following:

    * `BUCKET_NAME`: The Cloud Storage bucket name that contains the ZIP bundle.
    * `SKILL_PACKAGE`: The name of the skill package containing the skill revision.



###  REST 

To create a skill revision, send a `POST` request to the revisions collection. You can upload the ZIP payload directly or point to a Cloud Storage path.

  * **Upload a local ZIP file** : Specify `archiveUploadSource` containing the base64-encoded ZIP bytes in the request body. You can use the inline `base64` command in `curl`:
        
        curl -X POST \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              -H "Content-Type: application/json" \
              -d '{
                "archiveUploadSource": {
                  "archiveContent": "$(base64 -w0 local_skill.zip)"
                }
              }' \
              "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions?skillRevisionId=REVISION_ID"
        

  * **Import from a Cloud Storage bucket** : Specify `gcsSource` in the request body pointing to your bucket path:
        
        curl -X POST \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              -H "Content-Type: application/json" \
              -d '{
                "gcsSource": {
                  "uri": "gs://BUCKET_NAME/SKILL_PACKAGE.zip"
                }
              }' \
              "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions?skillRevisionId=REVISION_ID"
        


**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, for example, if you have never created a skill, trigger its creation for the Agent Registry API by following the steps in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting IAM permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.
  * `SKILL_ID`: The ID of the skill container.
  * `REVISION_ID`: The ID you want to assign to this revision.
  * `BUCKET_NAME`: The Cloud Storage bucket name containing the ZIP.
  * `SKILL_PACKAGE`: The name of the ZIP package.



## List and describe revisions

You can view the list of all revisions for a skill and inspect their metadata. If you want to update the default revision of a skill, see [Update skill metadata or default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).

To list and see details of a revision, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab, and click the name of your skill.
  3. In the **Skill Details** page, locate the **Version history** table.
  4. Review the version IDs, creation time, revision state, and available actions.



###  gcloud 

To list all revisions for a skill:
    
    
    gcloud alpha agent-registry skills revisions list \
      --skill=SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION
    

To describe metadata of a specific revision:
    
    
    gcloud alpha agent-registry skills revisions describe REVISION_ID \
      --skill=SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION
    

###  REST 

To list revisions:
    
    
    curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions"
    

To get metadata for a single revision:
    
    
    curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID"
    

## Download revision payload

You can download a specific revision's compiled ZIP file payload for local verification or debugging.

To download the payload, both of the following conditions must be met:

  * **Skill** : The [skill](https://docs.cloud.google.com/agent-registry/concepts#skill) must be in the **Active** or **Deprecated** state. To change the skill's target state, see [Manage skill lifecycle states](https://docs.cloud.google.com/agent-registry/manage-skills#lifecycle).
  * **Skill revision** : The [revision](https://docs.cloud.google.com/agent-registry/concepts#skill-revision) must be in the **Active** state. Revisions in **Failed** or **Creating** states cannot be downloaded. To review the state of a skill revision, list and describe revisions. You can [update the default revision of a skill](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill) to make a specific revision active.



To download the revision payload of an active revision, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab, and click the name of your skill.
  3. In the **Skill Details** page, locate the **Version history** table.
  4. Find the revision you want to download.
  5. In the actions column, click **Download**. The ZIP payload downloads to your local machine.



###  gcloud 

To download a revision's archive payload, run the `describe` command with the `--alt=media` flag and redirect the output to a file:
    
    
    gcloud alpha agent-registry skills revisions describe REVISION_ID \
      --skill=SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION \
      --flags="alt=media" > skill_payload.zip
    

###  REST 

Send a `GET` request to the revision's resource URL adding the query parameter `alt=media`. You must use the `-L` flag with `curl` to follow HTTP redirect streams:
    
    
    curl -L -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -o skill_payload.zip \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID?alt=media"
    

## Delete a specific revision

Deleting a specific revision removes its ZIP payload and metadata history from Agent Registry.

Deleting individual revisions is typically restricted to administrators. You can't delete a revision that is set as the skill's default revision. To update the default revision of a skill, see [Update skill metadata or default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).

To delete a specific revision, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab, and click the name of your skill.
  3. In the **Skill Details** page, locate the **Version history** table.
  4. Find the revision you want to delete.
  5. In the actions column, click **Delete** and confirm the action.



###  gcloud 
    
    
    gcloud alpha agent-registry skills revisions delete REVISION_ID \
      --skill=SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION
    

###  REST 
    
    
    curl -X DELETE \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID"
    

## What's next

  * Learn how to [explore verified publishers](https://docs.cloud.google.com/agent-registry/review-publishers).
  * Understand [quotas and limits](https://docs.cloud.google.com/agent-registry/quotas) for skill revisions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
