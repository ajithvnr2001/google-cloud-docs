---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-overview/
title: Agent desktop \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:43.536522+00:00
---

# Agent desktop  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent desktop Stay organized with collections  Save and categorize content based on your preferences. 

Agent desktop is a customizable interface that provides agents quick access to the information and tools they need to handle customer sessions. The [desktop layout](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts) includes the agent adapter as well as configurable panels that display information or tools. You can configure a distinct desktop layout for each session type: inbound calls, outbound calls, or chats. You can then configure which [desktop layout that an agent sees](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-set-desktop-layouts) when they answer an inbound call, place an outbound call, or handle a chat. You can also [configure announcements](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-announcements#permissions) to communicate updates, alerts, and other important information directly to agents.

## Before you begin

Before you can use the agent desktop, you need to turn on the agent desktop extension.

To turn on the agent desktop extension, follow these steps:

  1. In the Google Cloud console, go to the project selector dashboard and select the project that contains your instance.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the navigation menu, click **CCAI Platform**.

[CCAI Platform instances](https://console.cloud.google.com/contact-center-ai-platform)

The **CCAI Platform instances** page appears.

  3. Click the instance that you want to edit. The **CCAI Platform instance Detail** page appears.

  4. Click **Edit > Configure extensions**.

  5. For **Extensions** , select the **Agent desktop** checkbox, and then click **Save**.




## Permissions

Users with the Admin role can configure agent desktop settings and announcements but can't use the agent desktop. Conversely, users with the Agent role can use the agent desktop but can't configure agent desktop settings and announcements. If you're an administrator who needs to use the agent desktop, be sure that your user has both the Admin and the Agent roles. For more information, see [User roles and permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions).

You can create a [custom role](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#custom_roles_permissions) if the default user roles in CCAI Platform don't meet your needs. If you want a custom role that lets a user configure the agent desktop, configure announcements, or use the agent desktop, you need to select the correct permission settings for that custom role. The following procedure shows you how to find the agent desktop permission settings that you need when you create a [custom role](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#custom_roles_permissions).

To find the permission settings for the agent desktop, do the following:

  1. In the CCAI Platform portal, click **Settings > Users & Teams**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Click **Roles & Permissions**.

  3. Do either of the following:

     * To find the permission settings for configuring the agent desktop and announcements, do the following:

       1. For **Admin** , click visibility **View**. The **Edit Role** dialog appears.

       2. For **Settings > Agent Desktop**, click expand_more to display the remaining **Agent Desktop** permission settings. The following agent desktop permissions for administrators display:

          * **Settings > Operation Management > All**

          * **Settings > Agent Desktop > All**

          * **Settings > Agent Desktop > Layout and panel Management**

          * **Settings > Announcement Management**

     * To find the permission settings for using the agent desktop, do the following:

       1. For **Agent** , click visibility **View**. The **Edit Role** dialog appears.

       2. For **Function > Agent > All**, click expand_more to display the **Agent** permission settings. The following agent desktop permissions for agents display:

          * **Function > Agent > All**

          * **Function > Agent > Calls, chats, messaging**

          * **Function > Agent > Agent Desktop**

  4. Click **Cancel**.


**Important:** The preceding procedure is for finding the agent desktop settings you need if you want to create a [custom role](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#custom_roles_permissions) for an agent desktop.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
