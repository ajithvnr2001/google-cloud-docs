---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse-agent-guide/
title: Use Screen Share \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:10.933355+00:00
---

# Use Screen Share  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse-agent-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Use Screen Share Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Screen Share, which enables screen sharing with an end-user (consumer). Optionally, it enables remote control of the end-user's device. You can initiate a Screen Share session during an active web or mobile chat session using the **Smart Actions** menu in the agent adapter.

## Screen Share modes

Screen Share has three modes, with each mode giving you a different level of control over the end-user's device. Each time you initiate a different Screen Share mode, a message is sent to the end-user that describes the requested level of access and gives them the opportunity to approve or deny access.

Here are the three Screen Share modes:

  * Screen Share mode. You can view, but not control, the end-user's screen.

  * Remote control mode. You can view and control the end-user's screen.

  * Full device mode. You can view the end-user's active screen. If the end-user moves to another screen, your view changes to that screen. You can't control the end-user's screens.


**Note:** By default all modes are enabled when Screen Share is enabled, however depending on the business needs you may find only certain modes are enabled.

### Screen Share mode

With Screen Share mode, you can view, but not control, the end-user's screen. Every Screen Share session starts in Screen Share mode. In Screen Share mode, behavior varies slightly depending on whether you're using the web channel or the mobile channel. The following list explains the difference:

  * **Web channel:** With Screen Share mode using the web channel, you can see the end-user's active browser tab.

  * **Mobile channel:** With Screen Share mode using the mobile channel, you can see the end-user's active screen within the app. If the end-user minimizes the app, their screen isn't visible to you until they reopen the app.




To initiate a Screen Share session during an active chat session, do the following:

  1. In the agent adapter, click **Smart Actions** > **Request Screen Share**. A message is sent to the end-user requesting consent to share their screen. If the end-user clicks **Allow** , you receive a notification with a **View** button.

  2. Click **View** to start the Screen Share session.

  3. Optional: Click the laser pointer icon to point on the end-user's screen.

  4. Optional: Click edit **Pencil** to draw on the end-user's screen.

  5. Optional: Click delete **Trash** to erase your drawings.




### Remote control mode

With remote control mode, you can view and control the end-user's screen. You need to have an active Screen Share session before you can enter remote control mode. In remote control mode, behavior varies slightly depending on whether you're using the web channel or the mobile channel. The following list explains the difference:

  * **Web channel**. With remote control mode using the web channel, you can control mouse and keyboard actions on the end-user's active browser tab.

  * **Mobile channel**. With remote control mode using the mobile channel, you can control mouse and keyboard actions on the end-user's active screen within the app. If the end-user minimizes the app, their screen isn't visible to you until they reopen the app.




To enter remote control mode from Screen Share mode, follow these steps:

  1. Start with an active Screen Share session in Screen Share mode. For information about initiating a Screen Share session, see Screen Share mode.

  2. In the agent adapter, click pan_tool_alt **Remote control**. A message is sent to the end-user requesting consent for the agent to take control of their screen. If the end-user clicks **Allow** , the Screen Share session enters remote control mode.




### Full device mode

With full device mode, you can view the end-user's active screen. If the end-user moves to another screen, your view changes to that screen. You can't control the end-user's screens. In full device mode, behavior varies slightly depending on whether you're using the web channel or the mobile channel. The following list explains the difference:

  * **Web channel**. With full device mode using the web channel, you can see whichever browser tab that the end-user makes active.

  * **Mobile channel**. With full device mode using the mobile channel, you can see the end-user's active screen within the app. If the end-user minimizes the app, their screen remains visible.




To enter full device mode from Screen Share mode or remote control mode, follow these steps:

  1. Start with an active Screen Share session. The active session can be in either Screen Share mode or remote control mode.

  2. In the agent adapter, click the **Full device** toggle to the on position. A message is sent to the end-user requesting consent to share their full screen with the agent. If the end-user clicks **Allow** , the Screen Share session enters full device mode. If you were previously in remote control mode, remote control is automatically disabled.




### Request a Screen Share session: All call types

  1. During a session, the agent can request the consumer to obtain the six-digit access code needed to initiate the Screen Share session. The six-digit access code should be generated on your website.

  2. Click Actions > Enter Screen Share code on the agent adapter.

  3. Enter the six-digit code provided by the consumer.

**Note:** The code must be six digits and numeric, and cannot be reused. After the Screen Share session has been used, a new code must be generated. If the code is incorrectly entered, or contains non-numeric characters, an error message will appear, stating "Code must consist of six digits".
  4. Click **start session**.

The consumer must allow access before the Screen Share session begins. Once allowed, a new window will open, showing the consumer's screen.




### End a Screen Share session

The Screen Share session can be ended at any time by the agent or the consumer.

Before a session is ended a confirmation message "End Co-browsing - Would you like to end the session?" will allow the consumer or agent to click **yes** or **no**.

  * **Web**



**Agent** : the session can be ended by clicking the **End Screen Share** button.

**Consumer** : the session can be ended by clicking the **Screen Share** button.

  * **Mobile**



The agent or consumer can end the session by clicking the **End Screen Share** button.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
