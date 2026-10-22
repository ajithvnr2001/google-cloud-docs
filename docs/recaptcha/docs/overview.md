---
url: https://docs.cloud.google.com/recaptcha/docs/overview/
title: Google Cloud Fraud Defense overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:10.801508+00:00
---

# Google Cloud Fraud Defense overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/overview/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Google Cloud Fraud Defense overview Stay organized with collections  Save and categorize content based on your preferences. 

Google has been defending millions of sites with reCAPTCHA for over a decade. reCAPTCHA has become a part of Google Cloud Fraud Defense, a fraud and abuse prevention platform for bot, account, and transaction protection across the agentic web. With Fraud Defense, you can add a layer of protection to your website or mobile applications against spam and abuse, and detect other types of fraudulent activities, such as credential stuffing, account takeover (ATO), and automated account creation. Fraud Defense offers enhanced detection with more granular scores, reason codes for risky events, mobile app SDKs, Password defense, multi-factor authentication (MFA), and the ability to tune your site-specific model to protect enterprise businesses.

## Fraud Defense tiers

Fraud Defense offers three usage-based tiers: Enterprise, Premium, and Essentials.

To compare features across tiers, see [Compare features between Fraud Defense tiers](https://docs.cloud.google.com/recaptcha/docs/compare-tiers).

## How Fraud Defense works

When Fraud Defense is deployed in your environment, it interacts with your backend and client (web pages or mobile applications).

When an end user visits a web page or uses a mobile application, the following events are triggered in a sequence:

  1. The client loads the web page from the backend or launches the mobile application.
  2. The web page or mobile application initializes the reCAPTCHA JavaScript API or mobile SDK, which begins collecting signals.
  3. When the end user triggers an action protected by Fraud Defense such as login, the reCAPTCHA JavaScript API or the mobile SDK in the client requests a verdict from Fraud Defense.
  4. Fraud Defense returns an encrypted reCAPTCHA token to the client for later use.
  5. The client sends the encrypted reCAPTCHA token to the backend for assessment.
  6. The backend sends the create assessment (`assessments.create`) request and the encrypted reCAPTCHA token to Fraud Defense.
  7. Fraud Defense returns a verdict to the backend based on the evaluated risk of the request. The verdict includes a risk score from 0.0 to 1.0 and reason codes.
  8. Depending on the verdict, you can determine the next steps to take for that specific user request or action.



The following sequence diagram shows the Fraud Defense workflow:

![Sequence diagram showing the interaction between the client, backend, and Fraud Defense when creating an assessment.](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagramv1.svg)

## What's next

  * [Test reCAPTCHA in a demo website](https://docs.cloud.google.com/recaptcha/docs/quickstart-app).
  * [Get started with reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow).
  * [Find the legacy reCAPTCHA secret key for plugins](https://docs.cloud.google.com/recaptcha/docs/create-key-website#find-key).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
