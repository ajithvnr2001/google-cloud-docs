---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/customize-mobile-web-messages/
title: Customize mobile and web SDK channel messages \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:59.858295+00:00
---

# Customize mobile and web SDK channel messages  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/customize-mobile-web-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Customize mobile and web SDK channel messages Stay organized with collections  Save and categorize content based on your preferences. 

When mobile and web SDKs have been installed, you can customize timely messages displayed to consumers.

Messages can be configured in the global settings and at the queue level.

### Setting mobile messages in global settings

Mobile messages are available for the Android and iOS SDKs, and they can be configured by language and app if you use multiple apps.

Global messages are located in **Settings > Languages & Messages**.

To update Mobile messages, select **Original App** as the channel.

To update Web SDK messages, select the **Web SDK** channel.

Once the **Display an After Hours Message Mobile** option is enabled in **Settings > Support Center Details**, the After Hour messages can also be configured by queue in **Settings > Queue > Mobile > Selected queue menu settings**.

  * **Default Greeting Message** : Used as the first message sent to the consumer when starting a chat conversation.

Sample Mobile default message: _Thanks for reaching out Kat Jones. Please send us any details you can while we connect you to an agent._

  * **After Hour Messaging** : When the call or chat option is selected for a queue that is outside of operating hours, this message will be displayed in the app.

    * **Call** : Shows once the call option is selected.

Sample Mobile call after hours message: _We're gone home for the day! Call back between 9am PST and 6pm PST Monday to Friday. If you still need help, email support@yourcompany.com_

    * **Chat** : Shows once the chat option is selected with the option to restart the Mobile menu flow.

Sample Mobile chat After Hours message:_We're gone home for the day! Call back between 9am PST and 6pm PST Monday to Friday._




### Web SDK channel messages

The web SDK channel messages are for use with the Web SDKs installed on your web pages and can be configured by language.

  * **Default Greeting Message** : Used as the first message sent to the consumer once the agent has been assigned to a chat session.

  * **After Hour Messaging** : When the call or chat option is selected for a queue that is outside of operating hours, and after hour deflection and overcapacity deflection are both disabled, this message will be displayed in the app.

    * **Call** : Shows once the call option is selected with the option to start a new conversation in another channel

Sample After Hours call message: _We're gone home for the day! Call back between 9am PST and 6pm PST Monday to Friday. If you still need help, email support@yourcompany.com_

    * **Chat** : Shows once the chat option is selected with other queues available for selection

Example after hours chat screen:




## Sample variable attributes for customizing web and mobile messages

The following variables can be inserted into Mobile and Web SDK messages and reference either information passed from the SDK or wait information.

For a full list see [Using variables for dynamic consumer messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/variables-dynamic-consumer-messages#UUID-12a5c965-2ea0-b869-9f91-5332152e6abb).

### @{END_USER}

Description: inserts the name of the consumer.

**Important:** This variable is limited by the amount of information CCAI Platform can pass from your Web or Mobile SDK.

If you have the Web SDK configured on an unauthenticated page (no login required by the consumer) Contact Center AI Platform (CCAI Platform) won't be able to pass individual information about the consumer.

When authenticated, the `Full name` is shown.

When unauthenticated, the term `Customer` is shown.

### @{AGENT}

Description: inserts the name of the Agent.

### @{NEXT_REOPEN_HOUR}

Description: include this variable to automatically display opening time based on operation hours.

For example: `We are closed for today, please try again tomorrow. We open {NEXT_REOPEN_HOUR}`.

### @{ESTIMATED_WAIT_TIME_IN_MINUTES}

Description: The numerical value for minutes or hours for the current estimated queue wait time is inserted. This can be used in the greeting and deflection messages.

After the numerical value, the word `Minutes` will be appended and will be translated to the associated language.

Sample Inputs

**German** : `Jemand wird so schnell wie möglich bei Ihnen sein. Die derzeitige geschätzte Wartezeit beträgt @{ESTIMATED_WAIT_TIME_IN_MINUTES}.`

**English** :`A representative will be with you ASAP. The current estimated wait is @{ESTIMATED_WAIT_TIME_IN_MINUTES}.`

Output to consumer

**German** : _Jemand wird so schnell wie möglich bei Ihnen sein. Die derzeitige geschätzte Wartezeit beträgt 5 Minuten._

**English** : _A representative will be with you ASAP. The current estimated wait is 5 minutes._

### @{QUEUE_SIZE}

Description: The numerical value representing the current total number of consumers waiting in queue including the consumer seeing the number is inserted. This is specific to the chat greeting message.

When configuring the message, add the `supporting label` to the end of the variable in the associated language. For the example, we added `in line`.

Sample input

`A representative will be with you ASAP. You are number @{QUEUE_SIZE} in line.`

Output to consumer

_A representative will be with you ASAP. You are number 3._

### @{TIME_UNTIL_DISMISSAL}

Description: this variable contains the remaining time until the chat is dismissed.

For example, when the Chat dismissal timer = 3min, the dismissal notification timer = 1min TIME_UNTIL_DISMISSAL will insert 2.

When configuring this message, add the `supporting label` to the end of the variable in the associated language (minute(s)).

## Configuring global default greeting and after-hours messages

  1. Go to **Settings > Support Center Details**.

  2. Navigate to **Display an After Hours Message Mobile** and toggle to **On**.

  3. Go to **Settings > Languages & Messages**.

  4. Navigate to the Mobile and Web SDK section.

  5. Select the language and Channel you want to set the messages for.

When selecting a Mobile App, the **Channel** drop-down automatically regulates all message configurations listed in both "Mobile & Web SDK" and "Audible Messages" sections for the selected mobile app, with the following exceptions:

     * IVR Purchase Flow Messages

     * All IVR messages customized for use within a mobile app can only be configured for English US.

  6. Messages to enter with examples

Default Greeting Message: Message sent using chat when the chat is initiated.

_Hi, @{END_USER}. We are sorry to hear that you are having a problem. Stand by while we connect you to an agent._

After Hour Messaging Title

_Sorry, we are closed._

After Hour Messaging Message

_We are closed for today, try again tomorrow after 9am Pacific Time._

Waiting for Agent Assignment Message: Message sent to the consumer right after queue selection. If a DAP is being used, this message is sent right away since the queue is auto-selected.

_We're assigning a representative to help you with @{QUEUE}._

Agent Assigned Message: Message sent to the consumer once an agent has been assigned to the session. _@{AGENT} will chat with you about @{QUEUE}_

Dismissal Warning Notification (Web Only): When inactive chats are set to auto-dismiss messages, this message is sent to the consumer based on the timer set in **Settings > Chat**. _Are you still there? Respond in the next @{TIME_UNTIL_DISMISSAL} minute(s) or the chat session will be closed._

  7. Enter the message.

Include Variable attributes if needed.

To add hyperlinks to the message, follow the structure outlined. The output in the SDK will depend on the version of the Mobile or Web SDK your company has installed:

Text format structure: `{​{https://www.yourcompany.co | Visit our website}​}`

Web SDK and Mobile SDK versions >= 0.34.1

Text displayed: [Visit our website](https://www.ujet.co)

Mobile SDK versions < 0.34.1

Text displayed: Visit our website [https://www.yourcompany.co](http://)

  8. Click **Apply**.

  9. Repeat by changing the **Channel** setting and set the messages for other SDKs if applicable.




## Configuring Mobile After Hour Messages by queue

  1. Go to **Settings > Queue > Mobile Edit/View**.

  2. Select a **queue**.

  3. Toggle **Display After Hour Deflection Message** to **On**.

  4. Select **Use custom After Hours message**.

  5. Enter the **custom message** for this queue.




To add hyperlinks to the message, follow the structure. The output in the SDK will depend on the version of the Mobile or Web SDK your company has installed:

  * Text format structure: `{​{https://www.yourcompany.co | Visit our website}​}`

  * For Web SDK versions >= 1.15 and Mobile SDK versions >= 0.34.

  * Text displayed: [Visit our website](http://www.ujet.co)

  * For Web SDK versions < 1.15 and Mobile SDK versions < 0.34

  * Text displayed: Visit our website <https://www.yourcompany.co>




Click **Set Custom After Hours Options** to save.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
