---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/integrating-apigee-contact-center-ai/
title: Integrating with Contact Center AI \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:57.237339+00:00
---

# Integrating with Contact Center AI  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/integrating-apigee-contact-center-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Integrating with Contact Center AI Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document describes the support available in Apigee for integrating with Google's [Contact Center AI](https://cloud.google.com/solutions/contact-center). 

## Introduction

Google's Contact Center AI solution offers natural interactions based on AI-powered conversation. By using the Contact Center AI, you can automate the interactions between your customers and your backend support agents. The Contact Center AI frees human agents to focus on more complex and specialized calls, providing them with real-time information, workflows, and turn-by-turn guidance. 

The Contact Center AI has many components. One of the components is Dialogflow which lets you create advanced Virtual Agents within a short time. These Virtual Agents can seamlessly switch between topics, handle supplemental questions, and operate across multiple channels 24/7 to minimize live agent interventions. 

When your customer is interacting with a Dialogflow virtual agent, the agent might access your backend services to gather information. Also, the agent might send information that you want to store in your backend systems. Dialogflow defines the format of the response data. So, a Dialogflow agent accepts the response data from your backend services only in the specified format. Similarly, your backend services might require the request data in a specific format. As a backend service integrator, you have to ensure seamless communication between your Dialogflow agent and your backend services. 

## Support for Dialogflow in Apigee

You can use Apigee to manage the interactions between Dialogflow and your backend services. Apigiee's ParseDialogflowRequest and SetDialogflowResponse policies enable easier integration with Dialogflow. By using these policies, you can easily plug-in your backend services to handle fulfillment requests from Dialogflow. 

The ParseDialogflowRequest policy processes the [WebhookRequest](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#webhook-request) from a Dialogflow virtual agent before sending the request data to your backend services. The policy extracts data from the WebhookRequest into the flow variables, which your backend services can use. For more information, see [ParseDialogflowRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy). 

The SetDialogflowResponse policy processes and formats the response data from your backend services as a [WebhookResponse](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#webhook-response) to the Dialogflow virtual agent. The policy constructs a WebhookResponse in the required format for a Dialogflow agent. For more information, see [SetDialogflowResponse policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy). 

If you are a backend service integrator, you need not spend time understanding the format of the Dialogflow's WebhookRequest or WebhookResponse. The Dialogflow policies will handle the format conversion for you. 

The following image shows how the ParseDialogflowRequest and SetDialogflowResponse policies assist you in handling Webhook requests and responses from the Dialogflow agents. 

![Diagram of Webhook requests in Apigee runtime.](https://docs.cloud.google.com/static/apigee/docs/api-platform/develop/images/dialogflow-request-response.png)

Apart from the ParseDialogflowRequest and SetDialogflowResponse policies, Apigee provides the AssertCondition policy that lets you evaluate conditional statements using your flow variables. You can use the AssertCondition policy together with the Dialogflow policies to further simplify your effort in integrating Apigee with Dialogflow. For more information, see [AssertCondition policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
