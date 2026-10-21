---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ivr-purchase-flow-messages/
title: IVR Purchase Flow Messages \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:00.023371+00:00
---

# IVR Purchase Flow Messages  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ivr-purchase-flow-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  IVR Purchase Flow Messages Stay organized with collections  Save and categorize content based on your preferences. 

While the caller is in the payment process, a series of messages are played. You can leave these messages or update the text-to-speech script.

These messages can be customized at **Settings > Languages & Messages > IVR Purchase Flow Messages**.

Dynamic content variables are available specifically for Secure Payments. See [Using Variables for Dynamic Consumer Messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/variables-dynamic-consumer-messages#UUID-12a5c965-2ea0-b869-9f91-5332152e6abb).

**Payment Confirmation**

`The total purchase amount including taxes and shipping is @{TOTAL_AMOUNT}. Please press 1 to confirm, press 2 if it is the incorrect product or price. If you would like to return to the agent at any time please press the star key.`

**Request Credit Card**

`Please input your credit card using the dial pad and press pound when you're done.`

**Invalid Credit Card**

`Sorry, that credit card number was invalid, please try again! If you would like to return to the agent, press the star key.`

**Confirm Credit Card**

`Your credit card number is @{CREDIT_CARD}. Please press 1 to confirm, press 2 to try again.`

**Request Expiry Date**

`Please input your 4 digit expiry date using the dial pad and press pound when you're done.`

**Invalid Expiry Date**

`Sorry, that expiry date was invalid, please try again! If you would like to return to the agent, press the star key.`

**Confirm Expiry Date**

`Your expiry date is @{EXPIRY_DATE}. Please press 1 to confirm, press 2 to try again.`

**Request CVC**

`Please input your CVC code using the dial pad and press pound when you're done.`

**Invalid CVC**

`Sorry, that CVC code was invalid, please try again! If you would like to return to the agent, press the star key.`

**Confirm CVC**

`Your CVC code is @{CVC}. Please press 1 to confirm, press 2 to try again.`

**Request ZIP Code**

`Please input your zip code using the dial pad and press pound when you're done.`

**Invalid ZIP Code**

`Sorry, that zip code was invalid, please try again! If you would like to return to the agent, press the star key.`

**Confirm ZIP Code**

`Your Zip Code is @{ZIP_CODE}. Please press 1 to confirm, press 2 to try again.`

**Success**

`Thank you for providing your payment information. It has been sent and you will now be connected back to the agent.`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
