---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/define-requests-for-users-admin/
title: Create user requests \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:06.576296+00:00
---

# Create user requests  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/define-requests-for-users-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create user requests

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to create a request template and demonstrates the end-to-end flow, from a user submitting a request to a playbook automatically handling the case.

You can define requests for end users to select directly from the homepage. These requests serve as an internal ticketing system, letting different teams like IT and the SOC, or a Managed Security Service Provider (MSSP) and an end user—to communicate more efficiently.

Each request can be handled in one of two ways:

  * Manually by an analyst
  * Automatically by a playbook, which streamlines the entire process



You can define requests that users can select on the homepage. An analyst can handle each request manually or a playbook can automate them, where the platform serves as an internal ticketing system. Each request enters the platform as a case with the label **Request**.

Examples of such requests include the following:

  * Blocking malicious IPs
  * Optimizing SIEM rules
  * Onboarding a new user



This document demonstrates how to create a request template and shows the end-to-end flow.

## Add permissions for internal users

For this use case, we recommend that you plan which requests to automate and then build the accompanying playbook.

### Define a request

To define a request for Salesforce permissions: 

  1. Go to **Settings > Environments > Requests**.
  2. Click  add  **Add Requests**. 
  3. In the **Add Request Flow** dialog, enter a logical name and select an environment.
  4. Select a **Request Type**. This category determines which entities are displayed in the **Event Fields** list. For this use case, choose request type **Login**. 
  5. **Event Fields** provide a way for the platform to recognize the incoming case request and perform the appropriate mapping and modeling behind the scenes.
  6. In the **Event Fields** section, manually enter a field name and then select the field type (for example, `email` or `string`).
  7. In the **Watermark** field, add an instruction for the requester.
  8. In the **Raw event field** list, you can choose to use an event field to bring in a raw event or use entities that you can use in playbooks later. This example uses the **Username** and **SourceUserName** entities.
  9. Click **Add**.



### Build a playbook

The following procedure shows how to build a playbook that automatically runs when the new case request enters the platform: 

  1. Create a new playbook with an appropriate name and environment. 
  2. Select the **Alert Type Trigger** , set the condition to **Equals to** , and the value to the request template you created. In this case, **Salesforce Permission Approvals**.
  3. Add the **Enrich Entities** active directory to get more information about the user.
  4. Add the **Active Directory: Add User to Group** action and set these parameters:
     * **Action Type: Manual** : The playbook stops running and waits for further instructions.
     * **Assign to: Administrator** : Assign the step to a specific user or a SOC role, such as **Administrator**. The pending action is then displayed on the homepage and in the **Case View**.
     * **Message to Assignee** : This message appears as part of the pending action details. For example, enter **Please approve or decline permission for user [Entity.Identifier] to Salesforce group.**
     * Time to respond: Enable this timer and give the assigned user a day to respond. 
  5. Add the **Siemplify Close Case** action. This action closes the playbook after the administrator approves or declines the request. 



The request is now created with the corresponding playbook. 

### Approve the request

The user chooses a request. For details, see [fill out a request from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/filling-out-request-from-workdesk). After a user submits the request selection, it enters the system as a **Request Case**. The playbook then waits for the administrator's input to continue. 

You can see the pending request and approve it in three separate places within the platform: 

  * **Cases** : Under the relevant alert, click the **Playbooks** tab and click **Execute** in the side drawer to approve the request. 
  * **Cases > Overview**: Click **Execute** in the appropriate widget. 
  * **Homepage** : Click the **Pending Actions** tab, select **Required Pending Action** , and click **Execute** to approve the request. 

**Note:** Standard users see the **Execute** and **Skip** options. The collaborator user sees **Approve** and **Decline** and is prompted to provide a reason if they decline the action. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
