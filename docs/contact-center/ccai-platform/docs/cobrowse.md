---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse/
title: Screen Share \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:28.904351+00:00
---

# Screen Share  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Screen Share Stay organized with collections  Save and categorize content based on your preferences. 

Screen Share lets an agent see an end user's screen and, optionally, take control of it. Screen Share is an optional add-on with an incremental monthly cost per agent.

To set up Screen Share for your agents, do the following:

  * Get your instance provisioned for Screen Share

  * Install and configure the web SDK for Screen Share

  * Create and apply a custom role to agents




## Get your instance provisioned for Screen Share

Contact your account manager and request that they provision your Contact Center AI Platform (CCAI Platform) instance for Screen Share. After your account manager fulfills your request, your instance is configured for Screen Share by generating the Screen Share domain, license key, and JWT token.

**Note:** When Screen Share is enabled, all available Screen Share modes are enabled by default. If you don't want all Screen Share modes enabled, contact Google Cloud support to request a change to your CCAI Platform instance.

To confirm that your CCAI Platform instance is provisioned for Screen Share, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Developer Settings**.

  2. In the **Screen Share** pane, click the toggle to the on position. If the **Screen Share domain** and **License Key** fields are populated, your instance is provisioned for Screen Share. The JWT token isn't visible. Make a note of your Screen Share domain and license key. You need them to configure the web SDK for Screen Share.


**Note:** To disable Screen Share for your contact center instance, click the toggle in the **Screen Share** pane to the off position.

## Install and configure the web SDK for Screen Share

To use Screen Share, [initialize the web SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#initialize-web-sdk) and [configure it for Screen Share](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#configure-web-sdk-for-cobrowse). You need the web SDK regardless of whether you use Screen Share with web chats or with mobile chats. If you use [Screen Share mode](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse-agent-guide#screen-share-mode), install the web SDK on the web page that you expect end-users to share.

### Customize Screen Share

When you configure the web SDK for Screen Share, the web SDK provides default consent dialogs and a default end-session button. Consent dialogs let an end-user consent to an initial Screen Share session request, as well as a subsequent remote control request or full device access request. Optionally, you can customize the consent dialogs and end-session button. For more information, see [Customize the co-browse consent dialogs and end-session button](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#customize-cobrowse-consent-dialog-and-end-button).

## Create a custom role and apply it to agents

To enable your agents to use Screen Share, create a new custom role and apply it to every agent that needs to use Screen Share.

  1. To create a custom role, do the following:

     1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Users and Teams**. The **Users and Team Settings** page appears.

     2. Click **Roles and Permissions**.

     3. Click **Add Roles**. The **Add Role** pane appears.

     4. Enter a role name, a label name, and an optional description.

     5. In the **Function** row, click  expand_more **Expand more**.

     6. Select the **Screen Share - Calls and chats** checkbox, and then click **Save**. The new custom role for Screen Share is created.

  2. To apply the custom role to an agent, do the following:

     1. On the **Users and Teams Settings: Roles and Permissions** page, click **Manage Users and Teams**. The **Users and Teams Settings** page appears.

     2. In the **Roles (Users)** area, click **Agent** to view a list of agents.

     3. For the agent that you want to apply the role to, click more_horiz **More** , and then click **Edit user**. The **Edit a User** pane appears.

     4. Click the **Select Role** field, and then click the name of the custom role that you created earlier in this procedure.

     5. Click **Update**. The new custom role is applied to the agent.

     6. Repeat step 2 for every agent who needs the custom role.




## Customize the Start Screen Share button

You can customize the color of the **Start Screen Share** button in the agent adapter or your own app to match your brand's color palette.

To customize the **Start Screen Share** button, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. On the **Screen Share** pane, click the toggle to the on position.

  3. Click the **Customize the Color of the Screen Share Adapter button** toggle to the on position.

  4. Click the **Enter Hex Color Code** field, enter the hex code for the color you want, and then press **Tab**. A sample of your color appears.

  5. Click **Save Changes**.




## Record Screen Share sessions

You can record Screen Share sessions and save them to external storage. Recordings are saved in external storage for the duration that you set.

### Set up external storage for Screen Share recording

To set up external storage for Screen Share recording, follow these steps:

  1. Follow the instructions in [Set up external storage using Cloud Storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage#set-up-external-storage-cloud-storage) or [Set up external storage using an SFTP server](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage#set-up-external-storage-sftp-server), depending on your use case.

  2. Click the **Screen Share** checkbox when configuring the type of data that you want to store.




## CRM integration

If you've integrated a customer relationship management (CRM) app with CCAI Platform, you can [configure how a Screen Share recording is referenced in a CRM record](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage#configure-how-screen-share-recording-is-referenced). For more information, see [Set up external storage for CRMs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage).

## Screen Share historical data

Screen Share provides historical data for storage in your CRM or in external storage, depending on your Screen Share setup. After each Screen Share session, Screen Share provides the following historical data:

  * The user who requested the Screen Share session.

  * Whether the Screen Share session request was accepted or denied.

  * Whether control of a device was requested and whether the request was accepted or denied.

  * Whether full-device screen sharing was requested and whether the request was accepted or denied.




## What's next

  * To learn about how an agent uses Screen Share, see [Screen Share agent guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse-agent-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
