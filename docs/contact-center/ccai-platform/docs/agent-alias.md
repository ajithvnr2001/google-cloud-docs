---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-alias/
title: Agent aliases \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:52.870139+00:00
---

# Agent aliases  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-alias/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent aliases Stay organized with collections  Save and categorize content based on your preferences. 

CCAI Platform lets an agent substitute an alias for their real name when communicating with end-users. Administrators can configure agent aliases manually or with a bulk upload. An agent can configure their own alias if they have permissions. Administrators can also add an agent alias attribute to a chat shortcut.

Agent aliases are displayed to end-users only with the mobile and web SDKs. Agent aliases are not used in reporting.

## Add an agent alias to a user

To add an agent alias to a user, follow these steps:

  1. Click menu **Menu** , and then click **Settings > Users and teams**.

  2. In the **All users** pane, in the row for the user that you want to add an agent alias to, click more_horiz **More** , and then click **Edit user**. The **Edit a user** dialog appears.

  3. In the **Alias (Optional)** field, enter the agent alias, and then click **Update**.


**Note:** You can also create an agent alias when creating a user. For more information, see [Add users](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent_team_configuration/team.md#add-users).

## Do a bulk import of agent aliases

To do a bulk import of agent aliases, follow these steps:

  1. Click menu **Menu** , and then click **Settings > Users and teams**.

  2. Click **Bulk user management** , and then click **Upload users**. The **Import users** pane appears.

  3. Click **Template**. The **bulk_user_manage_template.csv** template downloads to your computer.

  4. Open **bulk_user_manage_template.csv**.

  5. In the **Alias** column of the template, enter an agent alias for each user that requires one.

  6. Save and close **bulk_user_manage_template.csv**.

  7. In the **Import users** pane, browse for **bulk_user_manage_template.csv** on your computer or drag the file into the pane.

  8. Click **Process**.




For more information, see [Bulk user management templates](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent_team_configuration/team.md#bulk-user-management-templates)

### Let agents create their own aliases

You can grant agents permissions to create their own aliases.

To grant an agent permissions to create their own alias, follow these steps:

  1. In the CCAI Platform portal, go to **Settings > Users and teams**.

  2. Click the **roles and permissions** tab.

  3. In the **agent** row, click **Visibility**. The **edit role** display appears.

  4. In the **user profile** row, click **expand**.

  5. Select the **agent alias** checkbox, and then click **Update**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
