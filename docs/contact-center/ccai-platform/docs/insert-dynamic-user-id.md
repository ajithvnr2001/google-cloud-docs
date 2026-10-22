---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/insert-dynamic-user-id/
title: Insert a dynamic user ID \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:05.482459+00:00
---

# Insert a dynamic user ID  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/insert-dynamic-user-id/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Insert a dynamic user ID Stay organized with collections  Save and categorize content based on your preferences. 

This feature enables the CCAI Platform portal to work with your mobile or web SDKs User ID/unique ID as a session variable for tracking or content personalization. When the variable is included in the Automatic Redirect to website option, the User ID value is dynamically inserted into the URL.

Example use cases:

  * Show order details for a specific user with Mobile or Web queues

  * Present your users with product offerings based on their locations by directing to a specialized web page based on user ID

  * Mobile FAQ page landing can be personalized to show the right page for the user's membership tier based on the User ID




## Feature details

  * If mobile or Web SDK passes User ID/identifier to CCAI Platform portal, it can be inserted as a session variable into your manual deflection webpage or FAQ link

  * From the CCAI Platform portal ccaas_portal, an administrator can add "@@USER_ID@@" into the URL in Manual Deflection to Webpage field under Mobile or Web queues to dynamically retrieve and insert User ID

  * From the CCAI Platform portal, an CCAI Platform portal can add "@@USER_ID@@" into the URL for Mobile FAQ to dynamically retrieve and insert UID




## Automatic redirect

  1. Go to **Settings** > **Queue** > **Mobile** OR **Web**.

  2. Click the queue you want to redirect to a URL.

  3. Click to **show** Automatic Redirect options, then click **Website**.

![Automatic redirect settings](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce5491c52e.png)

  4. Enter the **mobile-friendly website** and add the User ID identifier as a session variable to the URL by including "**@@USER_ID@@** " in the URL for tracking or content personalization purposes.

**Example:** <https://www.domain.com?uid=@@USER_ID@@>

**Note:** Mobile-friendly web pages are always highly recommended even if the end user is accessing the web SDK, they could be on mobile.



## Mobile FAQ

When enabled, Mobile FAQ lets you show a webpage while remaining in the app, with an option of showing a phone number as well on the screen. To enable contact support,

  1. Go to **Settings** > **Operation Management**.

  2. Navigate to the **Mobile: Display FAQ** section and insert **@@USER_ID@@** into the URL where needed.

**Ex** : <https://www.domain.com?uid=@@USER_ID@@>

  3. Click **Set FAQ**.




## Session variable output

The User ID variable format inserts the user ID value only.

For the example "https://www.domain.com?uid=@@USER_ID@@," If user_ID value is '12345' for a given session, the rendered URL would be: https://www.domain.com?uid=12345.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
