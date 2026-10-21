---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/organize/
title: Use deployments to organize CBSDs \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:29.647607+00:00
---

# Use deployments to organize CBSDs  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/organize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Use deployments to organize CBSDs Stay organized with collections  Save and categorize content based on your preferences. 

Administrators can assign permissions to users to restrict visibility to a subset of their Spectrum Access System (SAS) customer accounts. Use the [deployments list](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#deployment-list) to create deployments and assign user permissions to existing deployments and customer accounts.

## Find the CBSDs in a single deployment

To find the CBSDs in a single deployment, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. Optional: If you have access to multiple deployments, select a deployment from the **Deployments** list.
  4. Click **Open**.



## Find the CBSDs from a multiple deployment

To find the CBSDs from a multiple deployment, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. Select your [customer account](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#customer-acct) or [node](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#node).

**Important:** If you've already created nodes within your customer account, the node hierarchy appears after your customer account on the left.
  4. To view CBSDs from all deployments that exist under the selected customer account or node, click **Open**.

**Important:** When you view multiple deployments, you can't create a new CBSD. To create a CBSD, open the deployment that contains the user ID that the CBSD uses to register with SAS.



## Create a deployment

Only _administrators_ of a customer account or node can create deployments. To create a deployment, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
  2. Click **View deployments**.
  3. Select your customer account or node from the **Deployments** list. The new deployment is created under your selected customer account or node.
  4. On the left, click add**New deployment**.
  5. On the right, name the deployment and assign a unique [user ID](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#userid).
  6. Click **Create**.



## Create CBSD configurations in a deployment

To create a CBSD configuration in a deployment, which is the lowest branch of the organizational hierarchy, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
  2. Click **View deployments**.
  3. Optional: If you have access to multiple deployments, select a deployment from the **Deployments** list.
  4. Click **Open**.
  5. Click table_chart **Table view**.
  6. Click **Create CBSD**.

**Tip:** The **user ID** field automatically populates with the **deployment ID** of the selected deployment. You can also use the import function to add multiple CBSD configurations at the same time.

## Manage users in a deployment

Administrators can add or remove users at the level of customer account, node, or deployment. Users added at the customer account or node level keep the same permissions for all nodes and deployments under that level. [Learn about user roles](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal).

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
  2. Click **View deployments**. 
     * If you have access to a single deployment, to access **User management** , click settings **Settings**.
     * If you have access to multiple customer accounts, nodes, or deployments, make sure that you select the specific group where users must be added or removed.
  3. On the right, click lock **Unlock deployment settings**.
  4. In the **User management** section, do the following: 
     * **[Add a user](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal#add-user)**.
     * **[Remove a user](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal#remove-user)**.
     * **Edit a user:** Follow the steps to [add a user](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal#add-user). When you give them a new role, you can remove them from their old role.
  5. To prevent further changes, click lock_open **Lock deployment settings**.



## What's next

  * Learn how to [use PALs in the SAS Portal](https://spectrum-access-system/docs/use-pals).
  * Learn how to use [SAS sync](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
