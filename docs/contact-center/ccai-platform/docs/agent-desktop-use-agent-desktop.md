---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-use-agent-desktop/
title: Use the agent desktop \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:31.235113+00:00
---

# Use the agent desktop  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-use-agent-desktop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Use the agent desktop Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use the agent desktop.

## Open the agent desktop

To open the agent desktop, in the CCAI Platform portal, click **Apps > Agent Desktop**. If you don't see the **Apps** menu, click menu **Menu**. The agent desktop opens in a new browser tab. j

To change the display language, go to the menu bar, click language **Languages** , and then click the language to switch to.

## Get network diagnostic information

You can get network diagnostic information to help you assess network performance and troubleshoot connection issues.

To get network diagnostic information, in the navigation menu, click ![The diagnostics icon](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-agent-desktop-network.png)**Diagnostics**. The network diagnostic information appears.

## Answer an incoming call

To answer an incoming call, you must have the CCAI Platform portal open in a separate browser window or tab.

When an incoming call arrives, the menu bar displays the **Incoming call** pane.

![The "incoming call"
pane](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/agent-desktop-answer.png)

To answer the call, do the following:

  1. Click **Answer**. A new session tab opens and a desktop layout for receiving incoming calls appears. The specific layout that appears depends on how your administrator configured the agent desktop. For more information, see [Set desktop layouts for agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-set-desktop-layouts).

  2. Use the call adapter to assist you in handling the call. It works the same way as the call adapter in the CCAI Platform portal. For more information, see [Agent call adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls).

**Note:** If you're using an external call adapter instead of the CCAI Platform call adapter, the external call adapter appears outside of the agent desktop.
  3. Use the capabilities in the panels of the agent desktop to assist you in handling the call.

  4. End the call, or let the end-user end it.

  5. If your instance is configured for wrap-up, then complete your wrap-up tasks.




The session tab remains open until you close it or until the maximum time that a session tab can remain open is reached. For information about how an administrator configures session tab limits, see [Session tab limits](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-general-desktop-settings#session-tab-limits).

## Place an outgoing call

To place an outgoing call, do the following:

  1. Click ![The dial pad icon.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-dialpad.png) in the menu bar. A new session tab opens and the call adapter appears.

**Note:** The panels in the agent desktop don't populate until you place your call.
  2. Place your call.

  3. Use the call adapter to assist you in handling the call. It works the same way as the call adapter in the CCAI Platform portal. For more information, see [Agent call adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls).

  4. Use the capabilities in the panels of the agent adapter to assist you in handling the call.

  5. End the call, or let the end-user end it.

  6. If your instance is configured for wrap-up, then complete your wrap-up tasks.




The session tab remains open until you close it or until the maximum time that a session tab can remain open is reached. For information about how an administrator configures session tab limits, see [Session tab limits](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-general-desktop-settings#session-tab-limits).

## Handle an incoming chat

When an incoming chat arrives, the menu bar displays the **New Chat** button.

![The "new chat" option in the menu
bar](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/agent-desktop-new-chat.png)

To handle the incoming chat, do the following:

  1. Click **New Chat**. A new session tab opens and a desktop layout for handling chats appears. The specific layout that appears depends on how your administrator configured agent desktop. For more information, see [Set desktop layouts for agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-set-desktop-layouts).

  2. Use the chat adapter to assist you in handling the chat. It works the same way as the chat adapter in the CCAI Platform portal. For more information, see [Handle a chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/handle-a-chat).

  3. Use the capabilities in the panels of the agent adapter to assist you in handling the chat.

  4. End the chat, or let the end-user end it.

  5. If your instance is configured for wrap-up, then complete your wrap-up tasks.




The session tab remains open until you close it or until the maximum time that a session tab can remain open is reached. For more information, see [Session tab limits](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-general-desktop-settings#session-tab-limits).

You can click the session tabs of multiple active chat sessions to switch between them.

## Handle an email

To handle an email, follow these steps:

  1. Click **new emails** in the menu bar.

![The 'new emails' option in the menu bar](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/agent-desktop-menu-bar-new-emails.png)

The email navigation view appears. This view works similarly to the [Email navigation view](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#email-navigation-view) in the email adapter.

  2. Navigate to the email that you want to handle, and then click it. The email appears in the **Email Adapter** panel.

  3. Handle the email in the same way that you'd handle an email in the [Email adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter).




## Announcements

Your administrator can send you announcements to communicate updates, alerts, and other important information. Announcements appear in the agent desktop as notification banners. These banners persist until you dismiss them by clicking **Okay**. Announcements also appear in the announcement list.

There are two types of announcements:

  * **One-time** : For one-time announcements, notification banners appear only once. You can remove one-time announcements from the announcement list.

  * **Persistent**. For persistent announcements, notification banners reappear every time you sign into the agent desktop. You can't remove persistent announcements from the announcement list.




### Notification banners

Notification banners appear in the agent desktop in the following circumstances:

  * Your administrator sends you a new announcement. The announcement immediately appears.

  * You sign into the agent desktop. Persistent announcements appear, even if you dismissed them previously.




The following image shows a notification banner:

![Notification banner that appears in the agent
desktop](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/agent-desktop-notification-banner.png)

The **Announcements** button displays the number of new announcements for which you haven't yet dismissed the notification banner—for example, ![The Announcements button with a number indicating the
number of new notification banners](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-agent-desktop-announcements-2.png). In this example, you have two new notification banners that you haven't yet dismissed. Dismissing a new notification banner lowers the number on the **Announcements** button. When you dismiss all new notification banners, the **Announcements** button no longer displays a number.

When you dismiss a notification banner for a persistent announcement, the notification banner reappears the next time you sign into the agent desktop. Because this notification banner isn't for a new announcement, it's not included in the number count of the **Announcements** button.

### View announcements in the announcement list

In addition to the notification banners that appear in the agent adapter, you can view announcements in the announcement list.

To view announcements in the announcement list, do the following. In the agent desktop, click ![The announcements button that opens the announcement
list](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-agent-desktop-announcements.png)**Announcements**. The announcement list appears.

### Remove one-time announcements from the announcement list

You can remove one-time announcements from the announcement list. You can't remove persistent announcements from the announcements list.

To remove one-time announcements from the announcement list, do the following:

  1. In the agent desktop, click ![The announcements button that opens the
announcement list](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-agent-desktop-announcements.png)**Announcements**. The announcement list appears.

  2. To remove a one-time announcement, click ![The delete icon to remove a one-time announcement.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-agent-desktop-trash.png)**Delete** for the announcement that you want to remove.

  3. To remove all one-time announcements, for **Announcements** , click ![The delete icon to remove all one-time
announcements.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-agent-desktop-trash.png)**Delete All**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
