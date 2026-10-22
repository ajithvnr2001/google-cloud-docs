---
url: https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-inline-editor/
title: Inline editor \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:37.524641+00:00
---

# Inline editor  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-inline-editor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Inline editor Stay organized with collections  Save and categorize content based on your preferences. 

The Dialogflow Console has a built-in code editor, called the _inline editor_ that you can use to create fulfillment code and deploy the code to [Cloud Functions](https://docs.cloud.google.com/functions/docs). Cloud Functions has associated charges, but the service is available for no charge up to a [significant number of monthly invocations](https://docs.cloud.google.com/functions/pricing). Note that you still must register and provide a valid billing account. Cancel anytime. 

When you initially enable the inline editor, Node.js fulfillment code is pre-populated with default handlers for [default intents](https://docs.cloud.google.com/dialogflow/docs/intents-default) that are included for all agents. The code also has commented instructions for adding handlers for developer-defined intents. 

The inline editor is intended for simple fulfillment testing and prototyping. Once you are ready to build a production application, you should create a [webhook service](https://docs.cloud.google.com/dialogflow/docs/fulfillment-webhook). 

## Dialogflow fulfillment library

The inline editor uses the [Dialogflow fulfillment library](https://github.com/dialogflow/dialogflow-fulfillment-nodejs) by default. This library is no longer maintained, but it remains useful as a simple fulfillment library solution. This library should only be used by inline editor code.

The Dialogflow fulfillment library does not support [versioning](https://docs.cloud.google.com/dialogflow/es/docs/agents-versions). If you need to use versioning, choose one of the following options:

  * Overwrite the default inline editor code with your custom webhook code.
  * [Deploy custom webhook code to Cloud Functions directly](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook#gcf).
  * Fork and modify the Dialogflow fulfillment library to support versioning.



## Using the inline editor

The [fulfillment quickstart](https://docs.cloud.google.com/dialogflow/docs/quick/fulfillment) has step-by-step instructions for using the inline editor.

## Download your code

Once you're ready to move your fulfillment code to another system, use the download _get_app_ button on the inline editor.

## Network calls

Network calls originating from Cloud Functions code to destinations outside of Google's network are [charged by the Cloud Functions service](https://cloud.google.com/functions/pricing#networking).

## Limitations

The following limitations apply:

  * The inline editor only supports Node.js.
  * If you modify your code with the Cloud Functions console, you can no longer use the inline editor to modify your code. Your function will continue to provide fulfillment for your agent, but future edits must be made in the Cloud Functions console.
  * The inline editor function must be named `dialogflowFirebaseFulfillment`.
  * You cannot save or download code modified in the inline editor without deploying it first.
  * The inline editor only supports two files: 
    * **`index.js`** : Contains all of your fulfillment code.
    * **`package.json`** : Modifying this file will install any dependencies you specify upon deployment.
  * See the Dialogflow fulfillment library section for limitations of this library that is used by the inline editor by default.



[ Previous arrow_back  Fulfillment  ](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-overview)

[ Next Webhook service  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
