---
url: https://docs.cloud.google.com/telecom-network-automation/docs/control-blueprints/
title: Control blueprints and deployments \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:39.351699+00:00
---

# Control blueprints and deployments  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/control-blueprints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Control blueprints and deployments Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the create, edit, propose, approve, and delete operations on the Telecom Network Automation resources, blueprints, and deployments. 

## Blueprints

Before you perform operations on a blueprint, ensure you have the Telco Automation Admin (`roles/telcoautomation.admin`) role.

### Create blueprints

  1. From the navigation menu, click **Blueprints > Import from Library**.
  2. Select the blueprint you want. Click **Add Blueprint**.
  3. Specify the blueprint name. 
     1. Optional: Add any labels you require.
  4. Click **Create**. Your Blueprint appears in the **Draft Blueprints** list.



### Edit a blueprint

  1. From the navigation menu, click **Blueprints > Drafts Blueprint**.
  2. Select the blueprints you want to edit. A blueprint editor appears.
  3. Edit the files you want to change.
  4. Click **Save File**.

**Note:** You must save each file individually.



### Propose a blueprint

  1. From the navigation menu, click **Blueprints > Drafts Blueprint**.
  2. Select the blueprints. A blueprint editor appears.
  3. Click **Propose**. The status of the blueprint changes to **Proposed**.



### Approve, reject, or delete a blueprint

  1. From the navigation menu, click **Blueprints**.
  2. Click the **Action** menu by the blueprint name.
  3. Select either of the following: 
     1. **Approve** : approve a blueprint.
     2. **Reject** : reject a blueprint.
     3. **Delete** : delete a blueprint.



### Edit metadata

  1. From the navigation menu, click **Blueprints**.
  2. Click the **Action** icon by the blueprint name.
  3. Select **Edit Metadata**. A dialog appears.
  4. In the dialog, edit the metadata fields **Name** and **Labels**.
  5. Click **Save**.



## Deployments

Before you perform operations on a deployment, ensure you have one of the following roles:

  * Telco Automation Admin (`roles/telcoautomation.admin`)
  * Telco Automation Blueprint Designer (`roles/telcoautomation.blueprintDesigner`)
  * Telco Automation Deployment Admin (`roles/telcoautomation.deploymentAdmin`)



### Create a deployment

  1. From the navigation menu, click **Blueprints** **>** **Approved Blueprints**.
  2. Select the name of the blueprint to deploy.
  3. Click **Create Deployment**.
  4. Provide a deployment name.
  5. Click **Create Deployment**. The deployment appears in **Draft Deployment**.



### Edit a deployment

  1. From the navigation menu, click **Deployments**.
  2. Select the name of the deployment to edit.
  3. Click **Edit**. The **Deployment Editor** appears.

**Note:** Depending on the deployment, you can only edit certain files, such as the `setters.yaml` file.
  4. Edit the files. Afterwards, click **Save File**.

**Note:** You must save each file individually.



### Apply a Deployment

  1. From the navigation menu, click **Deployments**.
  2. Select the name of the deployment to apply.
  3. Click **Edit**. The **Deployment Editor** appears.
  4. Click **Deploy**.
  5. Confirm your selection. The deployment appears in **Applied Deployment**.



### Delete a Deployment

  * **Delete a draft deployment** :

    1. From the navigation menu, click **Deployments**.
    2. In the drop-down menu, select the deployment you want to delete.
    3. Click **Draft Deployments**.
    4. Click the Action icon next to the name of the deployment.
    5. Click **Delete**. A dialog appears.
    6. Click **Delete**.
  * **Delete an applied deployment** :

    1. From the navigation menu, click **Deployments**.
    2. In the drop-down menu, select the deployment you want to delete.
    3. Click **Applied Deployments**.
    4. Click the Action icon.
    5. Click **Delete**. A dialog appears.
    6. Do either of the following:
    7. Click **Delete**.
    8. Delete from the deployment name: 
       * Navigate to **Deployments**.
       * Select the orchestration cluster that you want from the drop-down menu.
       * Click **Applied Deployments**.
       * Select the name of the deployment you want to delete.
       * Click **Delete**.



### Roll back a deployment

  1. From the navigation menu, click **Deployments**.
  2. In the drop-down menu, select your orchestration cluster.
  3. Click **Applied Deployments**.

**Note:** Only applied deployments have versions you can roll back.
  4. Select the name of the deployment you want to roll back.

  5. Click **Version History**.

  6. In the list of deployment versions, click **Rollback** on the version to roll back the deployment.


**Note:** Deployment names must be 254 characters or less, consist of lowercase alphanumeric characters, include a dash or a period, and must start and end with an alphanumeric character.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
