---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-git-project-already-exists/
title: Troubleshooting the Git error \"Project with that name already exists\" \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:38.027354+00:00
---

# Troubleshooting the Git error "Project with that name already exists"  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-git-project-already-exists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting the Git error "Project with that name already exists" Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot the "Project with that name already exists" error in Looker. This error can occur when you try to create a new project with a name that's already in use by another project, even if that project isn't visible in the UI. This error typically occurs because remnants of the project—often in a Git branch or on the server file system—still exist.

## Troubleshooting tree

Use the following decision tree to troubleshoot this error. [Open the decision tree in a new tab to zoom in.](https://docs.cloud.google.com/looker/docs/diagrams/git-project-already-exists-troubleshooting-tree)

## Troubleshooting steps

The following sections describe the scenarios in the tree in further detail.

### Step 1: Check development branches

Remnants of a project may exist in one or more development branches. To check development branches, follow these steps:

  1. Turn on [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode).
  2. Navigate to your LookML projects and check every development branch—especially personal branches—for a project with the conflicting name.
  3. If you find a project with the conflicting name, delete the project in the IDE, commit the change, and then deploy to production to remove the lingering Git reference.



### Step 2: Reset Git connection

Resetting the Git connection can force a cleanup of local repository inconsistencies. To reset the Git connection, follow these steps:

  1. Go to **Project Settings** for the project.
  2. On the **Configuration** tab, select **Reset Git Connection**.
  3. Re-enter the Git URL. If you're using SSH, upload the new deploy key to your Git provider.



### Step 3: Check pending projects

A model may have been configured using the project name without the project itself ever having been generated. This would have created a _pending project_. To check for pending projects, follow these steps:

  1. Turn on [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode).
  2. View the **LookML Projects** page.
  3. Check the **Pending Projects** section. If a project exists with the conflicting name, delete the pending model configuration.



### Step 4: Server-side resolution (bare repos only)

If your Looker instance uses a bare Git repository (customer-hosted), the files may be lingering on the server. To clean up files on the server, sign in to the Looker host server and manually rename or delete the bare repository folders that are associated with the project:

  * Rename or delete the directory: `~/models/YOUR_PROJECT_TO_DELETE`
  * Rename or delete the bare repository directory: `~/bare_models/YOUR_PROJECT_TO_DELETE.git`

**Warning:** These operations require specific server access and should only be performed by a system or Looker admin.

### Step 5: Delete the project by using the Looker API

If the previous steps don't resolve the error, you can use the Looker API to manually delete the project to force an internal cleanup. This method uses the 4.0 API endpoints and requires Looker Admin privileges.

#### 1\. Get an access token

Use your API credentials (**Client ID** and **Secret**) to obtain a bearer token.
    
    
    curl -d "client_id=CLIENT_ID&client_secret=CLIENT_SECRET" https://INSTANCE_HOSTNAME.cloud.looker.com/api/4.0/login
    

The response will contain an `access_token`.

#### 2\. Switch session to Development Mode

You must delete the project in Development Mode. Switching to Development Mode changes the API session context.
    
    
    curl -X PATCH "https://INSTANCE_HOSTNAME.cloud.looker.com/api/4.0/session" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer BEARER_TOKEN" \
    -d '{"workspace_id": "dev"}'
    

#### 3\. Delete the project

Once the session is in Development Mode, use the `DELETE /projects/{project_id}` endpoint to delete the project.
    
    
    curl -X DELETE "https://INSTANCE_HOSTNAME.cloud.looker.com/api/4.0/projects/PROJECT_ID_TO_DELETE" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer BEARER_TOKEN"
    

A successful call will return an empty response (`204 No Content`) or a successful deletion message. You should now be able to re-create the project in the Looker UI.

These API calls can also be performed using API tools such as Postman.

## Final review and support

If these troubleshooting steps fail to resolve the error, [contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) to troubleshoot further.

## Additional resources

  * [Accessing and editing project information](https://docs.cloud.google.com/looker/docs/manage-projects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
