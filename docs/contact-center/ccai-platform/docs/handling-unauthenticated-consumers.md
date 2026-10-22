---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/handling-unauthenticated-consumers/
title: Handling Unauthenticated Consumers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:08.700805+00:00
---

# Handling Unauthenticated Consumers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/handling-unauthenticated-consumers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Handling Unauthenticated Consumers Stay organized with collections  Save and categorize content based on your preferences. 

When using the Web SDK and Mobile SDK, some user flows allow for your customers or prospects (referred to as consumer) to contact support before logging into the website or app. Since the user didn't enter any login credentials, there is no way to tie the user back to your exiting database right away. CCAI Platform will track the anonymous user when possible with a new temporary unique ID and merge to your existing user record/ID once the user has logged in.

Unauthenticated consumers may include:

  * Prospects contacting your support or sales team using your webpage

  * Current customers who are logged out of your app and contacting support to get help with their login

  * New users in the critical first stage of onboarding before a login has been created



  1. Since no identifying information is passed to your CRM without the user logging in, they will be recognized anonymously as a **Web User**.

**Note:** Web SDK must be installed on your website to receive chats.
  2. A ticket or case is created in your CRM with the following information for the consumer, and an internal process should dictate how the agent should edit the data so that the name of the contact is either updated to be correct or merged with an existing contact in your CRM.

\- First Name: Web User - {Month/Day Hour:Minute} (ex: Web User 10/05 10:15)

\- Unique Visitor Identifier

  3. If the same user comes back to the web SDK and then is able to sign in, the prior tickets while unauthenticated can be merged with ID they have now logged in with.

**Note:** If the end user clears their local storage, their unique visitor ID won't be recognized and a new contact will be created for this ticket



## Mobile: Unauthenticated Consumers

  1. Since no identifying information is passed to your CRM without the user logging in, they will be recognized anonymously as a **Mobile User** _._

**Note:** Mobile SDK must be installed on your website to receive calls and chats.
  2. A ticket or case is created in your CRM with the following information for the consumer, and an internal process should dictate how the agent should edit the data so that the name of the contact is either updated to be correct or merged with an existing contact in your CRM.

\- First Name: Mobile User - {Month/Day Hour:Minute} (ex: Mobile User 10/05 10:15)

\- Mobile SDK Identifier

  3. If the same user comes back to the Web SDK or Mobile SDK and then is able to sign in, the prior tickets while unauthenticated can be merged with ID they have now logged in with.

**Note for Android Devices** : If the user uninstalls and reinstalls your app, their unique mobile SDK ID won't be recognized, and a new contact will be created.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
