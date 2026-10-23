---
url: https://docs.cloud.google.com/agent-registry/register-skills/
title: Register skills \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:16.627138+00:00
---

# Register skills  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/register-skills/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Register skills Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Agent Registry lets you package and manually register [standalone skills](https://docs.cloud.google.com/agent-registry/skills-architecture). Standalone skills bundle agent instructions with associated metadata assets and optional scripts to extend an agent's reasoning and workflow. By registering your own standalone skills in Agent Registry, you can centrally govern, version, and share reusable capabilities alongside the Google-managed skills that are available when you set up Agent Registry.

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  3. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



### Required roles

To get the permissions that you need to register skills in Agent Registry, ask your administrator to grant you the following IAM roles on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * Register and manage standalone skills: [Agent Registry User ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.user) (`roles/agentregistry.user`) 
  * Register and manage standalone skills and other Agent Registry resources: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Other Agent Registry roles might also include the permissions required to register and manage skills and skill revisions. For more information, see [Agent Registry roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

### Ingestion payload constraints

To register a skill, you must package the skill's source files into a ZIP archive. The archive must include a `SKILL.md` instruction file at its root. During the ingestion phase of the skill registration process, Agent Registry validates that the payload complies with the following constraints:

  * **ZIP archive size** : maximum compressed archive size of 500 KB.
  * **Total uncompressed payload size** : maximum uncompressed size of 10 MB.
  * **Individual file size** : maximum uncompressed size of 1 MB per file.
  * **Deep nesting** : maximum directory nesting depth of 8 levels.
  * **Specification compliance** : the `SKILL.md` file must contain a valid YAML front matter section defining the name, description, and metadata as defined in the [Agent Skills Specification](https://agentskills.io/specification).



## Register a skill

You can manually register your own skills in Agent Registry. For information about pricing and feature costs for skills, see [Agent Registry pricing](https://docs.cloud.google.com/agent-registry/pricing).

To register your skills, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page:

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select your Google Cloud project.

  3. Select the **Skills** tab.

  4. In the **Skills** tab, the **Add skill** button displays two options to create a skill container and import your initial skills package. Choose one of the following:

     * **Add skill** : create a new skill container in the registry. You can optionally upload a skill package to create the first revision.
     * **Import skill** : register a new custom skills package by uploading a ZIP bundle containing your `SKILL.md` instructions file and optional scripts.
  5. In the **Create skill** or **Import skill** panel, specify the following details:

     * **Display name** : enter a user-friendly name for the skill.
     * **Description** : enter a brief summary explaining the skill capabilities.
     * **Location** : select the geographic region, for example, `global`, `us`, or `eu`.
  6. In the **Payload source** section, choose one of the following:

     * **File** : drag your packaged skill ZIP file, or browse your local directory.
     * **Bucket** : enter the path to your ZIP archive stored in a Cloud Storage bucket, in the format `gs://BUCKET_NAME/SKILL_PACKAGE.zip`.

**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, such as when you have never created a skill, trigger its creation for the Agent Registry API. For instructions, see [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting Identity and Access Management (IAM) permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).
  7. Click **Create**.

Your skill is created in the **Disabled** (`DISABLED`) state. For all subsequent skill operations, refer to your skill as `private-SKILL_ID`, as displayed in the Google Cloud console.

  8. To make the skill available for agent discovery, set its default revision and update the target state to **Active**. For instructions, see [Manage skill lifecycle states](https://docs.cloud.google.com/agent-registry/manage-skills#lifecycle).




###  gcloud 

  1. Create the skill container and upload its initial revision payload with the [`gcloud alpha agent-registry skills create`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skills/create) command. You can upload either a local ZIP file or import a package stored in Cloud Storage:

     * **Upload a local ZIP file** : to register a skill using a local ZIP payload:
           
           gcloud alpha agent-registry skills create SKILL_ID \
               --project=PROJECT_ID \
               --location=LOCATION \
               --display-name="DISPLAY_NAME" \
               --description="DESCRIPTION" \
               --target-state=disabled \
               --payload="LOCAL_ZIP_PATH"
           

Replace `LOCAL_ZIP_PATH` with the path to your packaged skill archive on your local machine, for example, `./workspace-docs-skill.zip`.

     * **Import from a Cloud Storage bucket** : to register a skill using a ZIP archive hosted in a Cloud Storage bucket:
           
           gcloud alpha agent-registry skills create SKILL_ID \
               --project=PROJECT_ID \
               --location=LOCATION \
               --display-name="DISPLAY_NAME" \
               --description="DESCRIPTION" \
               --target-state=disabled \
               --gcs-source-uri="gs://BUCKET_NAME/SKILL_PACKAGE.zip"
           

**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, such as when you have never created a skill, trigger its creation for the Agent Registry API. For instructions, see [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting IAM permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

Replace the following:

       * `BUCKET_NAME`: the Cloud Storage bucket name that contains the ZIP bundle.
       * `SKILL_PACKAGE`: the name of the skill package containing the skill payload.

Replace the following in either command:

     * `SKILL_ID`: the resource ID of the skill, for example, `workspace-docs-skill`. After creation, the registry automatically prepends the `private-` prefix. You must use the prefixed ID in all subsequent skill commands, for example, `private-workspace-docs-skill`.
     * `PROJECT_ID`: the project ID.
     * `LOCATION`: the geographic region, for example, `global`, `us`, or `eu`.
     * `DISPLAY_NAME`: a user-friendly name for the skill.
     * `DESCRIPTION`: a brief summary explaining the skill capabilities.
  2. Newly created skills start in the **Disabled** (`DISABLED`) state. To make the skill available for agent discovery, set its default revision and update the target state to **Active**. For instructions, see [Manage skill lifecycle states](https://docs.cloud.google.com/agent-registry/manage-skills#lifecycle).




###  REST 

  1. Create the skill container with an initial revision inline:

#### HTTP method and URL
         
         POST https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills?skillId=SKILL_ID
         

Replace the following:

     * `PROJECT_ID`: the project ID.
     * `LOCATION`: the registry location.
     * `SKILL_ID`: a unique identifier for the skill container.

#### Request JSON body (local file upload)

To create a skill by uploading local ZIP archive bytes directly, use the `archiveUploadSource` payload. During creation, `targetState` must be set to `TARGET_STATE_DISABLED`:
    
    {
      "displayName": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "type": "SIMPLE",
      "targetState": "TARGET_STATE_DISABLED",
      "initialRevision": {
        "archiveUploadSource": {
          "archiveContent": "BASE64_ZIP_BYTES"
        }
      }
    }
    

Replace the following:

     * `DISPLAY_NAME`: a user-friendly name for the skill.
     * `DESCRIPTION`: a brief summary explaining the skill capabilities.
     * `BASE64_ZIP_BYTES`: the base64-encoded string representation of your local ZIP archive.

#### Request JSON body (import from Cloud Storage)

Alternatively, to create a skill using an archive stored in a Cloud Storage bucket, use `gcsSource`:
    
    {
      "displayName": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "type": "SIMPLE",
      "targetState": "TARGET_STATE_DISABLED",
      "initialRevision": {
        "gcsSource": {
          "uri": "gs://BUCKET_NAME/SKILL_PACKAGE.zip"
        }
      }
    }
    

**Important:** Before Agent Registry can access your skill files, you must grant its service agent access to the ZIP archive in your Cloud Storage bucket. The Agent Registry service agent uses the following format: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If this service agent doesn't exist in your project, such as when you have never created a skill, trigger its creation for the Agent Registry API. For instructions, see [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents). The service agent requires the `storage.objects.get` permission on the Cloud Storage bucket containing your ZIP archive. For instructions on granting IAM permissions on bucket resources, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

Replace the following:

     * `DISPLAY_NAME`: a user-friendly name for the skill.
     * `DESCRIPTION`: a brief summary explaining the skill capabilities.
     * `BUCKET_NAME`: the Cloud Storage bucket name that contains the ZIP bundle.
     * `SKILL_PACKAGE`: the name of the skill package containing the skill payload.

#### `curl` command (local file upload)
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "displayName": "DISPLAY_NAME",
          "description": "DESCRIPTION",
          "type": "SIMPLE",
          "targetState": "TARGET_STATE_DISABLED",
          "initialRevision": {
            "archiveUploadSource": {
              "archiveContent": "'"$(base64 -w0 local_skill.zip)"'"
            }
          }
        }' \
        "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills?skillId=SKILL_ID"
    

Replace the following:

     * `DISPLAY_NAME`: a user-friendly name for the skill.
     * `DESCRIPTION`: a brief summary explaining the skill capabilities.
     * `PROJECT_ID`: the project ID.
     * `LOCATION`: the registry location.
     * `SKILL_ID`: a unique identifier for the skill container.

For a Cloud Storage bucket file upload, replace the request JSON body with the corresponding fields and values.

  2. Newly created skills start in the **Disabled** (`DISABLED`) state. To make the skill available for agent discovery, set its default revision and update the target state to **Active**. For instructions, see [Manage skill lifecycle states](https://docs.cloud.google.com/agent-registry/manage-skills#lifecycle).




The skills that you or other users create are automatically assigned to the default `private` publisher to avoid name collisions with Google-managed skills. For that reason, the published ID of a particular skill becomes `private-SKILL_ID`. You can't specify a custom publisher during skill creation.

For example, if you create a skill with the ID `workspace-tools`, the [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) is created as `projects/PROJECT_NUMBER/locations/LOCATION/skills/private-workspace-tools`. The [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) is assigned as `urn:skill:projects-PROJECT_NUMBER:locations:LOCATION:private-workspace-tools`. You must use the `private-workspace-tools` published ID for all subsequent skill operations.

## What's next

  * Learn how to [manage your registered skills](https://docs.cloud.google.com/agent-registry/manage-skills).
  * Learn how to [add and manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).
  * Review [verified publisher details](https://docs.cloud.google.com/agent-registry/review-publishers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
