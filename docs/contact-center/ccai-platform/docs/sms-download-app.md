---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-download-app/
title: App download SMS \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:33.248462+00:00
---

# App download SMS  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-download-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  App download SMS Stay organized with collections  Save and categorize content based on your preferences. 

SmartActions (receiving photos, videos, screenshots, verifying customers, and receiving text input) are not typically available during an IVR call. You can use Smart Actions by prompting the consumer to launch their app for your company. Once the app is installed and launched, you can use these Smart Actions with a consumer during an IVR call.

The Agent on the IVR call will need to take action to either send an SMS that provides a link to download or a link to launch the app. You may have an indicator in your CRM, or the Agent can ask the caller if they already have the app installed on a device they have nearby.

If you are using multiple mobile apps, these settings are now available in **Settings** > **Developer Settings** > **Multiple Mobile Apps**.

## Requirements for setup

  * Existing iOS and or Android mobile app with the CCAI Platform SDK integrated.

  * Deep links are required from your mobile development team for iOS and Android app to open URLs (steps 4 and 6 below). Deep linking allows for a consumer to tap on the link from their mobile device and the device will then launch the already installed app.




## Configuration

In order for agents to have an SMS to send with your app links, first the download and launch link needs to be configured in the CCAI Platform portal. These links will be added to the SMS messages sgents send, Agents won't need to enter the link manually.

To configure your SMS links, follow these steps:

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. Go to the **Enable Send SMS to Download App** pane. 

  3. Toggle **Enable Send SMS to Download App** to the on position.

  4. Specify at least one of the following URLs:

     * **iOS App Store URL:** Insert the iOS App Store URL for your app. This link can be provided by your mobile development team or gathered directly from the App store.

     * **iOS App Open URL:** Insert the deep-link to your iOS app. This link should be supplied by your mobile development team.

     * **Google Play Store App Store URL:** Insert the Google Play Store URL for your app. This link can be provided by your mobile development team or gathered directly from the Play Store.

     * **Android App open URL:** Insert the deep-link to your Android App. This is supplied by your mobile development team.

  5. Click **Save SMS To Download App**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
