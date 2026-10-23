---
url: https://docs.cloud.google.com/application-integration/docs/view-integration-details/
title: Manage integrations \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:32.987464+00:00
---

# Manage integrations  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/view-integration-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage integrations

You can modify an integration by configuring tasks, triggers, or edge connections. You can also update the integration details, such as modifying the setting for masking variables in logs, Cloud Logging, local logging, and updating the service account and the description of your integration.

## Integration edit locks

Integrations are design time entities that are often developed in collaboration with multiple authors. Although an integration can only be actively edited by one author at a time, teams can collaborate on an integration and track changes in state through its _versions_. 

You can edit only a `DRAFT` version of the integration, and execute only the `ACTIVE` version of the integration. For information about different integration versions, see [Integration versions](https://docs.cloud.google.com/application-integration/docs/integration-versions). 

When you open an integration, you might find a message similar to the following in the integration editor:

  * If you open the integration that is being edited by another user, the following message appears in the integration editor because only one user can update the integration at a given time: 
        
        test-user@gmail.com is currently editing the integration. Edit features are temporarily disabled.

**Note:** The integration is locked for editing by others for 15 minutes from the last update. Locks are released after 15 minutes from the last update.

To edit the integration, click **Take Over**. A new version in the `DRAFT` state is created in the integration for you and the editing capability is disabled for the other users. The following figure shows the edit lock in the integration editor.

![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-take-over-edit-lock.png)![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-take-over-edit-lock.png)

  * If you open a published integration, then the integration version is in the `ACTIVE` state. To edit the integration, click **Enable Editing**. A new version is created with the `DRAFT` state. 
        
        This version is currently active. Editing features are disabled.

To edit the integration, click **Enable Editing**. A new version in the `DRAFT` state is created in the integration for you. The following figure shows the edit lock in the integration editor.

![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)




## Edit an integration

To view and edit an integration flow, follow these steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears, listing all the integrations available in the Google Cloud project. 

  3. Click the integration that you want to edit. This opens the integration in the integration editor.

If the integration is not in `DRAFT` state, then the integration is locked for editing. For information about edit locks, see Integration edit locks.




## Delete integrations

**Warning:** When you delete an integration, you permanently delete all the versions of that integration, including all the integration variables, configured triggers, tasks, and data mappings. Deleting an integration cannot be undone.

To delete an integration, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Do any one of the following steps in the **Integrations List** page: 
     1. For the existing integration that you want to delete, click  more_vert **Actions**.
     2. Select **Delete** in the drop-down menu. 

A confirmation dialog appears.

Or 
     1. Click the existing integration that you want to delete. 

This opens the integration in the _integration editor_.

     2. In the designer toolbar, click  more_vert  (Actions menu) and select **Clone integration > Delete all versions**. 

A confirmation dialog appears.

     3. Click **Delete** to permanently delete the integration.



## Manage integration details

You can view the integration summary and update settings for your integration. The following image shows the **settings Integration settings** and **info Integration information** icons on the Application Integration editor toolbar: 

![image showing integration settings](https://docs.cloud.google.com/static/application-integration/images/integration-settings-details.png)![image showing integration settings](https://docs.cloud.google.com/static/application-integration/images/integration-settings-details.png)

### View integration details

To view the details of an integration, open the integration in the integration editor and click info (**Integration information**) in the designer toolbar. The following image shows the integration details: 

![image showing integration information dialog](https://docs.cloud.google.com/static/application-integration/images/integration-information-dialog.png)![image showing integration information dialog](https://docs.cloud.google.com/static/application-integration/images/integration-information.png)

The integration summary includes the following information:

  * **Integration name:** The name of the integration.
  * **Version:** The current version of the integration along with the version name (if any). For information about versioning, see [Versions](https://docs.cloud.google.com/application-integration/docs/integration-versions).
  * **Publish status:** The publish status of the current version of the integration; **Published** or **Unpublished**.
  * **Total versions:** The count of the total number of integration versions created for the integration.
  * **Last modified:** The date and time when the current integration version was last edited or modified.
  * **Last modified by** The name of the user who last edited or modified the integration version.
  * **Region:** The regional location where the integration was created.
  * **Description:** The integration description. To generate integration description using Gemini, see [Build integrations with Gemini Code Assist](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini).



### Edit integration details

To edit the details of an integration, open the integration in the integration editor and click settings (**Integration settings**) in the designer toolbar. The following image shows the **Integration Settings** pane:

![image showing integration settings dialog](https://docs.cloud.google.com/static/application-integration/images/integration-settings-dialog.png)![image showing integration settings dialog](https://docs.cloud.google.com/static/application-integration/images/integration-settings.png)

The integration summary includes the following information:

  * **Service account:** The service account attached to the integration.
  * **Enable Variable Masking in logs ([preview](https://cloud.google.com/products#product-launch-stages)):** The setting to enable masking of variables in the integration execution logs. If you enable masking for your integration, ensure that you have also enabled masking at the [region](https://docs.cloud.google.com/application-integration/docs/enable-new-region#edit-region) and the [variable](https://docs.cloud.google.com/application-integration/docs/variables) levels. 

For information about masking, see [Mask sensitive data in logs](https://docs.cloud.google.com/application-integration/docs/mask-sensitive-data-logs).

  * **Enable Cloud Logging:** The setting to enable or disable Cloud Logging. For more information, see [View logs in Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging).
  * **Local logging:** The setting to enable or disable saving integration's data or metadata during its execution. By default, local logging is set to **Enable(async)**. In this mode, the integration takes a relatively lesser time to execute when compared to the **Enable(sync)** mode, because Application Integration writes the log data asynchronously during the integration execution. However, this mode doesn't guarantee the generation of logs for all the executions. In rare cases–such as a physical server failure–it's possible that logs aren't generated for an integration execution. For more information, see [Local logging](https://docs.cloud.google.com/application-integration/docs/local-logging).

**Note:** Except for the **Service account** and **Description** fields, you can't edit or change any of the other integration information.

## What's next

  * Learn how to [test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn how to [create an integration](https://docs.cloud.google.com/application-integration/docs/create-integrations#create-a-new-integration).
  * Learn how to [clone integrations](https://docs.cloud.google.com/application-integration/docs/clone-integrations).
  * Learn about [logs in Application Integration](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
