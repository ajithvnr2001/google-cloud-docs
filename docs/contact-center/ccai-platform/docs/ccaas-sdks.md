---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaas-sdks/
title: About the Google Cloud CCaaS SDKs \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:11.859253+00:00
---

# About the Google Cloud CCaaS SDKs  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaas-sdks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  About the Google Cloud CCaaS SDKs Stay organized with collections  Save and categorize content based on your preferences. 

Today's customers expect to contact support agents when they need them directly and seamlessly from any device - including when they're on the go.

Our SDKs make help you provide voice and chat support to your customers on your website or right inside your app on iOS and Android.

## Web SDK

With the Contact Center AI Platform web SDK, your customers will be able to get in touch with your support team directly on your website.

  * Instant web calls: Provide visitors with an estimated wait time and automatically initiate an outbound call to a site visitor when their place in the support queue is reached.

  * Scheduled calls: Allow site visitors to schedule a time to talk with your support team.

  * Queue deflection: Automatically route end users to a message or page on your site.

  * Chat support: Provide live chat support directly from your website.

  * Proactive triggers: Display a contact bubble for web calls and chats automatically based on visitor behavior. Proactive triggers can be configured based on:

    * Specific page URL.

    * Time spent on page.

    * Number of visits to a particular page.

  * Mobile web support: Customers on mobile devices can also access your Web SDK.

  * Direct access points: Decide which queue, language, or channel an end-user should reach when on a particular page or with predefined account details.




## Mobile SDKs (iOS and Android)

With the CCAI Platform mobile SDKs, you can create seamless voice and chat support experiences for users directly inside your iPhone, iPad, and Android apps. To ensure a consistent experience for all your customers, both SDKs share a core set of features:

  * VoIP calls: Allow users to make voice calls using data instead of minutes.

  * PSTN fallback calls: When the end-user doesn't have a strong enough data connection for a VoIP call, CCAI Platform will fallback to a PSTN call while still sending the important custom data packet to your CRM record.

  * Scheduled calls: Allow users to schedule a time to talk with your support team; AI-powered algorithms predict and provide 15-minute time slots based on agent availability, ensuring your users never have to wait on hold.

  * SmartActions: Instantly verify users with biometrics (Touch ID and Face ID for iOS and iPad devices or fingerprint and face for Android devices) or passcodes, and request photos, videos, screenshots and text input.

  * SMS SmartActions: Send an SMS to activate SmartActions inside your app.

  * Call deflections: Configure call deflections based on volume and business hours, and, if needed, to:

    * Allow the user to schedule a call for another time.

    * Provide an email address.

    * Forward the call to another number directly.

    * Forward the call to voicemail.

  * Provide unique visual queue configuration settings:

    * Direct queues to a particular website, like a help center article for a common question.

    * Direct queues to a visual message.

  * Direct access points: Decide which queue, language, or channel an end-user should reach when the SDK is invoked in various parts of your app based on predefined contact details.




### Platform-specific capabilities

While both SDKs offer the same core functionality, they also take advantage of unique features built into their respective operating systems:

#### Unique to the iOS SDK

  * **CallKit integration** : The iOS SDK integrates with Apple's CallKit (for iOS 10.0 and greater), which allows for in-app calls to appear on the built-in iOS call screen, logs the interactions in the user's phone call history, and displays a custom icon on the lock screen when receiving a call.

  * **Full device screen sharing** : By adding a broadcast extension, the iOS SDK supports full device screen sharing. This allows support agents to view screens from outside your specific application, which is helpful if they need to check system settings or watch the user navigate between multiple apps.




#### Unique to the Android SDK

  * **Call conversion from native dialer** : Detect when a user dials your main support number directly from their device's built-in dialer and automatically convert that standard call into a mobile SDK call.

  * **Live chat resiliency** : Lets you configure a secondary fallback messaging media layer that automatically takes over if the primary media layer experiences an outage, improving the overall uptime of live chat.

  * **Background call notifications (Android 10+)** : Uses specialized notifications to alert users of incoming calls when the host app is in the background or the screen is locked, giving them the option to accept or decline the call, fully complying with Android's background activity restrictions.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
