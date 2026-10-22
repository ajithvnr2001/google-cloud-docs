---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks/
title: Manage playbook actions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:51.196343+00:00
---

# Manage playbook actions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage playbook actions

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Actions are the next set of components that you can define for a playbook. Each action is categorized under an integration in the system. They include tasks or actions to be performed by the playbook. For example, you can assign an analyst to a case, or in case of an external product integration (such as Trellix ePO product), you can set an action to update the Trellix Agent. For each integration, there's a list of sub-actions.

## Before you begin

To use the required actions, make sure you have the integrations downloaded and configured from the Content Hub. For more information about integrations, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

When the playbook runs, each action returns information that can include the following:

  * Output message, tables, attachments, links, JSON
  * Script result (only valid within the playbook itself)



You can view this information on the case wall or on the cases page.

## Understand key terms for actions

The following is a list of terms within actions:

  * **Parameters** : Input of some type including text, placeholder (Google SecOps variable), or list options.
  * **Placeholders** : Google SecOps variable which is populated at running time. For details about parameters and placeholders, see [Use the Expression Builder](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder).
  * **Enrichment** : Gathers more information and attributes on an entity. Learn more about [ using enrichment](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks#add-enrichment).
  * **Script Result** : Google SecOps-defined return value of an action.
  * **JSON Result** : Raw data that the action returns.
  * **Expression Builder** : Enables manipulating JSON results and extracting specific data to use in Playbook actions. For details, see [Use the Expression Builder](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder).



## Add an action

To add an action to the playbook, do the following:

  1. On the **Response > Playbooks** page, click **Add Step**.
  2. On the **Step Selection** tab, select the **Actions** section.
  3. In the **Actions** section, click  arrow_drop_down  **Down Arrow** next to an integration name and select the action item. In this example, select **Email > Send Email**.
  4. Drag the **Send Email** item to **Drag a step over here**.
  5. Double-click to open the sidebar. The sidebar displays the action's name and description, along with the final action result (shown by the Output Name). For this procedure, assume you're in the middle of a data loss protection (DLP) use case playbook and configure the fields as required. 
  6. Choose the instance to use for this playbook. For more information, see [Support multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).
  7. Define the entities the action will run on.
  8. Set the email recipient for this action by inserting an **Entity Identifier** placeholder. For this example, add an Entity Identifier placeholder.



### Add a placeholder

To add a placeholder, do the following:

  1. In the **Recipients** field, click the placeholder icon ([ ]) 
  2. In **Placeholder Selection** , select **Object > Entity.Property > Identifier**.
  3. Click **OK**.
  4. Click **Save**. The action is saved as _Action name_Sub Action name_.  




### Assign actions

In the Playbook Designer, you can assign actions or playbook blocks to a specific user or SOC role. The assignee determines the outcome of that step in the playbook run. You also have the option to include a message about the required action and enable a **Time to respond** countdown. The timer starts as soon as the playbook reaches that point in the flow. For more information, see [Assign actions and playbook blocks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-actions-and-playbook-blocks).

To assign an action in a playbook, do the following:

  1. Double-click on the required action in the playbook.
  2. In the **Action Type** list, select **Manual**.
  3. In the **Assign To** list, select the user or SOC role.
  4. Add a clear message explaining the required action. You can insert a placeholder in this message, which is then displayed to the user in the **Pending Actions** widget on their homepage and on the **Cases Overview** page.
  5. Optional: You can enable **Time to respond** to set a deadline for the action's completion. If the deadline isn't met, the action fails. To manage this outcome, configure the subsequent conditional step in your playbook to use the **If previous action fails** setting to control the flow.
  6. Click **Save**.



After a playbook is triggered (usually by an ingested alert), it runs automatically until it reaches a **Manual Action** level. This action pauses the playbook and appears in the **Pending Actions** widget on the homepage and the **Case Overview** , which requires a user to execute or skip it to continue the flow.

### Add enrichment to entities

Enrichment is additional data collected on an entity (such as hostnames, IP addresses, and artifacts).

On the **Cases** tab, click an entity to see all the existing attributes that belong to it. These attributes, also known as _enrichment parameters_ , can also be used in placeholders. If an entity is missing attributes you need, use an action to execute enrichment. To do this, follow these steps:

  1. Under the case top bar, click  settings  **Manual Action** to open the **Manual Actions** dialog.
  2. Select **Google Workspace > Enrich Entities**, and then select a specific entity. In this example, select the user **Javier**.
  3. Click **Execute**. Once the green arrow appears, close this box.
  4. In **Entities Highlights** , click the entity **Javier**. A new Entity Explorer page appears.
  5. On the **Entity Explorer** page, scroll to see who Javier reports to.
  6. Return to the main case page. All the enrichment attributes are now in the Google SecOps platform and are treated as entities in and of themselves. For example, the person that Javier reports to now can be chosen as an entity.



## Create a new entity

The analyst chooses the required entity when building the playbook. There are different sets of entities that the action will run on. You can also choose to add new entity sets. 

To create a new entity for a single playbook, do the following:

  1. In the **Actions** column, select **Flow > Entity Selection**, and drag it into the final step.
  2. Click **Entity Selection**.
  3. Select the required entity parameters. In this example, select **Reports To entity** (now populated in the system due to the enrichment action you ran earlier).
  4. Set its value to **Director** and click **Save**.
  5. The new entity set is saved as `Entity_Selection_1` and is immediately available for use within this playbook. If you create additional sets, they are sequentially numbered (for example, `Entity_Selection_2`, `Entity_Selection_3`).



## Edit and manage playbook steps

  * **Cut, copy, delete, or paste** : Right-click the required step to access the **Edit** menu. You can copy and paste steps within the current playbook or to a different one.
  * **Select multiple steps** : Press the **Shift** key while you left-click to select multiple steps. Then, right-click any highlighted step to perform a bulk action (**Cut** , **Copy** , **Delete** , or **Paste**).
  * **Configure step** : Double-click any step to open its configuration settings.



## Rerun an action

When an action fails and causes the playbook to stop, you can often fix the issue and resume the flow. When this happens, select the failed action to view the error message, correct any mistakenly entered parameters, and then rerun the action.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
