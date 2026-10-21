---
url: https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents/
title: Share agents from Google Cloud console \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:24:15.633907+00:00
---

# Share agents from Google Cloud console  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Share agents from Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to share agents with users in your organization and how administrators can transfer ownership of shared agents. As an administrator, you can share the available agents (Google-made, employee-made, and custom-made) with individual users, groups, Workforce Identity Pool groups, or all users in your organization, and transfer ownership of shared employee-made agents to yourself or another user. For more information about the different types of agents available in Gemini Enterprise, see [Agents overview](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview#types-of-agents).

**Note:** To share employee-made agents, you must have one or more agents created using Workflow Builder in your Gemini Enterprise web app. For information about creating agents using Workflow Builder, see [Create an agent using Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent).

## Before you begin

Before you can share an agent, you must meet the following requirements:

  1. You must have an existing Gemini Enterprise web app. To create a new app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  2. To share custom agents, you must have registered or added the custom agents to Gemini Enterprise using any of the following options:

     * [Register and manage A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent)
     * [Register and manage ADK agents hosted on Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent)
     * [Add and manage A2A agents from Google Cloud Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents)
     * [Register and manage Dialogflow agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent)



## Share an agent

To share an agent, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.



[Go to **Gemini Enterprise**](https://console.cloud.google.com/gemini-enterprise/products)

  1. Select your project.

  2. Click your app from the **Name** column. The navigation menu updates.

  3. Click **Agents** from the navigation menu.

  4. Click the **Display name** of the agent that you want to share.

  5. Click the **User permissions** tab, and the **Permissioned users** page displays.

  6. Click **Add user**. The **Add user permissions roles to agent** dialog displays.

  7. Configure the permission details:

     1. Select one of the following options in the **Member type** section:

        * **User** : An individual end user. For this member type to function, you must include the correct IAM role. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control).

        * **Group** : A collection of end users. For this member type to function, you must include the correct IAM role. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control).

        * **Principal** : A single identity in a Workforce Identity Pool group, which includes external groups that aren't managed by Google.

        * **Workforce identity pool** : All identities in a Workforce Identity Pool.

        * **All users** : All users in the organization.

     2. Enter the unique member identification, and select a role:

**Member type** | **Description**  
---|---  
**User** |  Enter email addresses in the **Member** field.  
Select a role in the **Assign role** field.   
**Group** |  Enter email addresses in the **Member** field.   
Select a role in the **Assign role** field.   
**Principal** |  A single identity within a WIF.   
**Workforce identity pool** |  Enter _Principal identifier_ in the **Member** field.   
Select a role in the **Assign role** field.  
  
For examples of principal sets, see Principal sets.   
**All users** |  Select a role in the **Assign role** field.   
  8. Click **Save**.




#### Principal sets

The following are examples of principal sets that you can specify for the **Workforce identity pool** member type:

**Principal set** | **Description**  
---|---  
`//iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ID` | A single identity in a WIF.  
`//iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_ID` | All workforce identities in a group.  
`//iam.googleapis.com/locations/global/workforcePools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE` | All workforce identities with a specific attribute value.  
`//iam.googleapis.com/locations/global/workforcePools/POOL_ID/*` | All identities in a workforce identity pool.  
  
Replace the following placeholders with values in the code sample:

  * **`PROJECT_NUMBER`** : the number used in the resource path to identify a specific Google Cloud project.
  * **`GROUP_ID`** : a specific group identifier from an external Identity Provider (IdP), letting you grant access to all members of that group.
  * **`POOL_ID`** : the unique ID for the workforce identity pool that you create in Google Cloud.
  * **`SUBJECT_ID`** : the unique subject identifier for a single identity within a workforce identity pool.
  * **`ATTRIBUTE_NAME`** : a user-defined name of a custom attribute that you have mapped from an external Identity Provider (IdP).
  * **`ATTRIBUTE_VALUE`** : the specific value of the `ATTRIBUTE_NAME` used to restrict access.



## Transfer agent ownership

As an administrator, you can transfer ownership of a shared agent to another user in your organization or to yourself. This capability is useful in scenarios such as:

  * **Departing employees:** Transferring agents created by employees who leave the organization to active team members to ensure uninterrupted maintenance.
  * **Contractor handoffs:** Handing over agents created by temporary or contract workers to full-time staff.
  * **Team restructuring:** Reassigning agent responsibilities as roles or projects evolve.



### Considerations and limitations

Before transferring agent ownership, note the following considerations and limitations:

  * **Administrator permission:** Only administrators with the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role (`roles/discoveryengine.agentspaceAdmin`) or the [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) role (`roles/discoveryengine.admin`) can transfer agent ownership. The current agent owner cannot transfer ownership unless they are also an administrator.
  * **Shared agents only:** You can only transfer ownership of agents that are already shared. On the **Agents** page in the Google Cloud console, the agent's **Sharing** column must display **Enabled**. Private (unshared) agents cannot be transferred.
  * **Single owner:** Each agent has exactly one owner. When ownership is transferred, the selected recipient becomes the sole owner of the agent.
  * **Previous owner access:** When ownership is transferred, the previous owner is demoted to a user on the agent with the `agentUser` role. They retain permission to query and run the agent, but can no longer edit the agent's configuration or settings.
  * **Supported agent types:** Ownership transfer is supported for employee-made agents (low-code and workflow agents created in the web app).
  * **Agents with schedules or triggers:** If the transferred agent has a schedule trigger or event trigger, the transfer operation marks them as disabled schedules or events. The new owner must enable the schedule or event trigger before being able to use the agent.



### Transfer ownership of an agent

To transfer ownership of an agent, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to **Gemini Enterprise**](https://console.cloud.google.com/gemini-enterprise/products)

  2. Select your project.

  3. Click your app from the **Name** column. The navigation menu updates.

  4. Click **Agents** from the navigation menu.

  5. Click the **Display name** of the shared agent.

  6. Click the **User permissions** tab. The **Permissioned users** list displays.

  7. Click **Transfer ownership**. The **Transfer ownership** dialog opens.

  8. Under **Transfer ownership to** , choose one of the following options:

     * **Myself** : Transfer ownership of the agent to your current administrator account. This option is disabled if you already own the agent.
     * **Another user** : Transfer ownership to another user in your organization.
  9. If you selected **Another user** , specify the new owner:

     * **Google Identity and Cloud Identity:** Enter the user's email address in the **New owner email** field (for example, `user@example.com`).
     * **Workforce Identity Federation (WIF) accounts:** Enter the single identity principal identifier in the **New owner principal** field:
    
    //iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ID
    

Alternatively, you can include the `principal:` prefix:
    
    principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ID
    

Replace the following:

     * POOL_ID: The unique ID of your workforce identity pool.
     * SUBJECT_ID: The user's subject identifier in the workforce identity pool.
**Note:** Workforce Identity Federation principal identifiers are case-sensitive. Ensure that the identifier matches the exact casing configured in your identity provider's `google.subject` mapping. 
  10. Click **Transfer ownership**.

The agent's owner is updated. The previous owner is retained as a permissioned user with the `agentUser` role.

**Note:** If the transferred agent has a schedule trigger or event trigger, the transfer operation marks them as disabled schedules or events. The new owner must enable the trigger before being able to use the agent. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
