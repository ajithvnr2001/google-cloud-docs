---
url: https://docs.cloud.google.com/recaptcha/docs/setup-overview-web/
title: Setup overview for websites \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:20.509193+00:00
---

# Setup overview for websites  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/setup-overview-web/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Setup overview for websites Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a high-level overview of setting up Google Cloud Fraud Defense on websites.

Setting up Fraud Defense on a website involves the following steps:

  1. Create a reCAPTCHA key for your website (also known as key).

The key is required to collect information about the user actions and send it to Fraud Defense.

     1. [Choose the key type that is best for your use case](https://docs.cloud.google.com/recaptcha/docs/choose-key-type).
     2. [Create a key for your website](https://docs.cloud.google.com/recaptcha/docs/create-key-website).
  2. Integrate with your website frontend:

Install the key that you created on your web pages by using the reCAPTCHA JavaScript API.

     * [Install score-based keys](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages).
     * [Install checkbox keys](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox).
     * [Install policy-based challenge keys](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-policy).
  3. Integrate with your backend:

     1. To verify the token sent by reCAPTCHA and assess the risk, [create assessments](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website) from your backend server.
     2. [Interpret the assessment scores and the associated risk](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website), and define how to handle users, for example, allow the user to log in only when the score is high and the risk is low.
  4. Optional: Configure an IP address allowlist

[Add trusted IP addresses to an allowlist](https://docs.cloud.google.com/recaptcha/docs/allowlist-ip) to exclude them from Fraud Defense enforcement.




## What's next

  * [Choose the reCAPTCHA key type that is best for your use case](https://docs.cloud.google.com/recaptcha/docs/choose-key-type).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
