---
url: https://docs.cloud.google.com/recaptcha/docs/implementation-workflow/
title: Understand the Fraud Defense implementation \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:56.184345+00:00
---

# Understand the Fraud Defense implementation  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/implementation-workflow/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Understand the Fraud Defense implementation Stay organized with collections  Save and categorize content based on your preferences. 

This document shows the implementation path of Fraud Defense to protect your websites, mobile applications, APIs, or content served by a web application firewall (WAF).

## Fraud Defense workflow for websites

The following illustration provides a high-level overview of the implementation of Fraud Defense on websites:

![A workflow diagram that shows the implementation workflow for websites](https://docs.cloud.google.com/static/recaptcha/images/recaptcha-web-workflow-img.svg)

![The implementation workflow for websites.](https://docs.cloud.google.com/static/recaptcha/images/recaptcha-web-workflow-img.svg)

Setting up Fraud Defense on websites involves the following steps:

  1. Create reCAPTCHA keys: Choose the reCAPTCHA key type that is best for your use case and create the keys.

  2. Integrate Fraud Defense with your website: To collect information about the user actions and send it to Fraud Defense, install the keys that you created on your web pages by using the reCAPTCHA JavaScript API.

  3. Integrate Fraud Defense with your backend: From your backend server, create assessments to verify the token sent by Fraud Defense and assess the risk. Interpret the assessment scores and the associated risk, and define how to handle users—for example, allow the user to sign in only when the score is high, which indicates low risk.




After you set up Fraud Defense, we recommend that you annotate the assessments whenever you have more information about the user interactions. This helps Fraud Defense to tune your site-specific model and improve the risk detection.

You can also set up additional security to protect user accounts and payment workflows on your websites.

For instructions, see [Set up Fraud Defense on websites](https://docs.cloud.google.com/recaptcha/docs/setup-overview-web).

## Fraud Defense workflow for mobile applications

The following illustration provides a high-level overview of the implementation of Fraud Defense on mobile applications:

![A workflow diagram that shows the implementation workflow for mobile applications](https://docs.cloud.google.com/static/recaptcha/images/recaptcha-mobile-workflow-img.svg)

![A workflow diagram that shows the implementation workflow for mobile applications.](https://docs.cloud.google.com/static/recaptcha/images/recaptcha-mobile-workflow-img.svg)

Setting up Fraud Defense on mobile applications involves the following steps:

  1. Create reCAPTCHA keys: Create score-based keys for your mobile applications.
  2. Integrate with your mobile application: To collect information about the user actions and send it to Fraud Defense, install the keys that you created on your mobile application by using the Fraud Defense SDK.
  3. Integrate with your backend: From your backend server, create assessments to verify the token sent by Fraud Defense and assess the risk. Interpret the assessment scores and the associated risk, and define how to handle users—for example, allow the user to sign in only when the score is high, which indicates low risk.



After you set up Fraud Defense, we recommend that you annotate the assessments whenever you have more information about the user interactions. This helps Fraud Defense to tune your site-specific model and improve the risk detection.

You can also set up additional security to protect user accounts on your mobile applications.

For instructions, see [Set up Fraud Defense on mobile applications](https://docs.cloud.google.com/recaptcha/docs/setup-overview-mobile).

## Fraud Defense workflow for WAF

The following illustration provides a high-level overview of the implementation of Fraud Defense at the WAF layer:

![A workflow diagram that shows the implementation workflow for WAF](https://docs.cloud.google.com/static/recaptcha/images/recaptcha-waf-workflow-img.svg)

![High-level implementation at the WAF level.](https://docs.cloud.google.com/static/recaptcha/images/recaptcha-waf-workflow-img.svg)

Setting up Fraud Defense at the WAF layer involves the following steps:

  1. Select WAF features: Understand the WAF features and choose one or more WAF features that suit your use case.
  2. Integrate with your website or mobile application: Create reCAPTCHA keys for WAF. To collect information about the user actions and send it to Fraud Defense, install the keys that you created on your web pages by using the reCAPTCHA JavaScript API or on mobile applications by using the Fraud Defense SDK.
  3. Integrate with your WAF service provider: To let your WAF service provider manage the incoming user requests, configure policies based on the scores returned by Fraud Defense.



After you set up Fraud Defense, we recommend that you annotate the assessments whenever you have more information about the user interactions. This helps Fraud Defense to tune your site-specific model and improve the risk detection.

For instructions, see [Set up Fraud Defense at the WAF layer](https://docs.cloud.google.com/recaptcha/docs/setup-overview-ca).

## reCAPTCHA express workflow for application servers

The following illustration provides a high-level overview of the implementation of reCAPTCHA express on application servers.

![A workflow diagram that shows the implementation workflow for application servers](https://docs.cloud.google.com/static/recaptcha/images/recaptcha-express-imp-workflow-img.svg)

![High-level overview of the implementation of Fraud Defense express on application servers.](https://docs.cloud.google.com/static/recaptcha/images/recaptcha-express-imp-workflow-img.svg)

Setting up reCAPTCHA express on application servers involves the following steps:

  1. Create express keys for your application server.
  2. Integrate with your backend: From your backend server, create assessments to assess the risk. Interpret the assessment scores and the associated risk, and define how to handle users—for example, allow the user to sign in only when the score is high, which indicates low risk.



After you set up Fraud Defense, we recommend that you annotate the assessments whenever you have more information about the user interactions. This helps Fraud Defense to tune your site-specific model and improve the risk detection.

For instructions, see [Set up reCAPTCHA express on application servers](https://docs.cloud.google.com/recaptcha/docs/express-standalone).

## What's next

  * [Set up Fraud Defense on websites](https://docs.cloud.google.com/recaptcha/docs/setup-overview-web)
  * [Set up Fraud Defense on mobile applications](https://docs.cloud.google.com/recaptcha/docs/setup-overview-mobile)
  * [Set up Fraud Defense at the WAF layer](https://docs.cloud.google.com/recaptcha/docs/setup-overview-ca)
  * [Set up reCAPTCHA express on application servers](https://docs.cloud.google.com/recaptcha/docs/express-standalone)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
