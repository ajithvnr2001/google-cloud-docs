---
url: https://docs.cloud.google.com/agent-registry/manage-skills/
title: Manage skills \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:59.783179+00:00
---

# Manage skills  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/manage-skills/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Manage skills Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After [registering a standalone skill](https://docs.cloud.google.com/agent-registry/register-skills) in Agent Registry, you can view its details, update its description, override its active revision pointer (`default_revision`), manage its lifecycle states, or delete it from Agent Registry. You can also list and view Google-created skills, which are visible immediately when you set up Agent Registry.

This document explains how to perform these administrative tasks.

## Before you begin

Before you start, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) and [register a standalone skill](https://docs.cloud.google.com/agent-registry/register-skills). You need [the project ID](https://support.google.com/googleapi/answer/7014113) to perform these tasks.

To use the Google Cloud CLI commands in this document, make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

### Required roles

To get the permissions that you need to manage skills in Agent Registry, ask your administrator to grant you the following IAM roles on the project: 

  * List and view skills: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * Update, transition lifecycle states, and delete skills: [Agent Registry User ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.user) (`roles/agentregistry.user`) 
  * Manage skills and other Agent Registry resources: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Other Agent Registry roles might also include the permissions required to view, update, and delete skills. For more information, see [Agent Registry roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

## List and view skills

You can browse all registered skills or search for specific capabilities:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Review the list of skills. You can filter the display using the **Location** or **Status** menus.
  4. Click any skill name to open its **Skill Details** page, which displays the name, description, active version, skill URN, last updated, custom metadata, and revision history.



###  gcloud 

To list all skills in a location:
    
    
    gcloud alpha agent-registry skills list \
      --project=PROJECT_ID \
      --location=LOCATION
    

To view details of a specific skill:
    
    
    gcloud alpha agent-registry skills describe SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION
    

Replace the following:

  * `SKILL_ID`: The ID of the skill you want to review.
  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.



###  REST 

To retrieve the list of all skills:
    
    
    curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills"
    

To retrieve a single skill container:
    
    
    curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID"
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.
  * `SKILL_ID`: The ID of the skill you want to review.



## Update skill metadata or default revision

You can modify a skill's display name, description, or manually change the default revision pointer to deploy a different version. To create new skill revisions, see [Manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).

To update skill metadata or the default revision of a particular skill, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Review the list of skills. You can filter the display using the **Location** or **Status** menus.
  4. Click any skill name to open its **Skill Details** page, which displays the name, description, active version, skill URN, last updated, custom metadata, and revision history.
  5. Choose between the following options:

     * **Update skill metadata** :

       1. Click edit **Edit**.
       2. In the **Edit skill** panel, update the display name or description of your skill.
       3. Click **Save**.
     * **Update the default revision** :

       1. Locate the **Version history** table.
       2. Find the revision you want to set as active.
       3. In the actions column, click **Activate version**.



###  gcloud 

  * To update a skill's metadata:
        
        gcloud alpha agent-registry skills update SKILL_ID \
          --project=PROJECT_ID \
          --location=LOCATION \
          --display-name="DISPLAY_NAME" \
          --description="DESCRIPTION"
        

  * To update a skill's default serving revision:
        
        gcloud alpha agent-registry skills update SKILL_ID \
          --project=PROJECT_ID \
          --location=LOCATION \
          --default-revision="projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID"
        




Replace the following:

  * `SKILL_ID`: The ID of the skill you want to update.
  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.
  * `DISPLAY_NAME`: The updated display name.
  * `DESCRIPTION`: The updated description.
  * `REVISION_ID`: The ID of the skill revision you want to set as default.



###  REST 

Send a `PATCH` request specifying the fields you want to update:
    
    
    curl -X PATCH \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -d '{
            "displayName": "DISPLAY_NAME",
            "description": "DESCRIPTION",
            "defaultRevision": "projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID"
          }' \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID?updateMask=displayName,description,defaultRevision"
    

Replace the following:

  * `DISPLAY_NAME`: The updated display name of the skill.
  * `DESCRIPTION`: The updated description of the skill.
  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.
  * `SKILL_ID`: The ID of the skill you want to update.
  * `REVISION_ID`: The ID of the skill revision you want to activate.



## Manage skill lifecycle states

To control how a skill is resolved at runtime, you can change the skill's target state:

  * **Draft:** The skill is in its initial creation or development phase. It isn't served at runtime, and payload downloads are blocked. You can modify the skill configuration and payloads freely in this state before promoting the skill to the **Active** target state.
  * **Active:** The skill is served and fully resolvable.
  * **Disabled:** Resolving the skill fails immediately, and downloads are blocked. Unlike the **Decommissioned** state, you can re-enable the skill later, which means returning it to the **Active** target state.
  * **Deprecated:** The skill remains loadable but returns warning headers indicating it will be sunset.
  * **Decommissioned:** The skill is permanently deactivated, no longer served, and _cannot_ be reverted back to **Active** or any other state. A skill can be decommissioned only after it has already been deprecated. Provide sufficient time to migrate before decommissioning the skill. This is a terminal state, recommended to be used with extreme caution.



To transition a skill's lifecycle state:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Review the list of skills. You can filter the display using the **Location** or **Status** menus.
  4. Click any skill name to open its **Skill Details** page, which displays the name, description, active version, skill URN, last updated, custom metadata, and revision history.
  5. Use the status control buttons to transition the target state. The buttons that the page displays depend on the current state of the skill, for example, **Enable** , **Disable** , **Deprecate** , or **Decommission**.



###  gcloud 

Update the skill container with the `--target-state` flag:
    
    
    gcloud alpha agent-registry skills update SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION \
      --target-state=DISABLED
    

Allowed values for the target state are:

  * `DRAFT`
  * `ACTIVE`
  * `DISABLED`
  * `DEPRECATED`
  * `DECOMMISSIONED`.



###  REST 

Send a `PATCH` request specifying the `targetState` in the body and in the update mask:
    
    
    curl -X PATCH \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -d '{
            "targetState": "TARGET_STATE_DISABLED"
          }' \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID?updateMask=targetState"
    

Allowed values for the target state are:

  * `TARGET_STATE_DRAFT`
  * `TARGET_STATE_ACTIVE`
  * `TARGET_STATE_DISABLED`
  * `TARGET_STATE_DEPRECATED`
  * `TARGET_STATE_DECOMMISSIONED`.



## Delete a skill

Deleting a skill container permanently deletes the skill container and all associated immutable `SkillRevision` version history. Agents attempting to resolve the deleted skill URN fail at runtime.

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Review the list of skills. You can filter the display using the **Location** or **Status** menus.
  4. Click the name of the skill you want to delete.
  5. In the **Skill Details** page, click delete **Delete**.
  6. In the confirmation dialog, enter `DELETE` and click **Delete**.



###  gcloud 
    
    
    gcloud alpha agent-registry skills delete SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION
    

###  REST 
    
    
    curl -X DELETE \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/SKILL_ID?force=true"
    

## What's next

  * Learn how to [upload new revisions and download packages](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).
  * Understand [roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions) for governing skills.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
