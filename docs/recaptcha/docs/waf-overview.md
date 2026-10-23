---
url: https://docs.cloud.google.com/recaptcha/docs/waf-overview/
title: Integration with WAF service providers overview \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:18.917816+00:00
---

# Integration with WAF service providers overview  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/waf-overview/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)



Send feedback 

#  Integration with WAF service providers overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of reCAPTCHA for WAF and its integration with web application firewall (WAF) service providers.

reCAPTCHA provides a plugin that is deployed as a service at the WAF layer. It enables WAFs to help you protect your site from spam and abuse. It uses advanced risk analysis techniques to distinguish between legitimate and fraudulent requests.

## reCAPTCHA for WAF integration

reCAPTCHA provides a plugin that is responsible for bot detection at the WAF layer to detect, stop, or manage automated activity accessing your websites or services.

reCAPTCHA for WAF integrates with the following WAF service providers:

  * Google Cloud's built-in WAF: [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * Third-party WAF service providers: [Fastly Edge Compute](https://www.fastly.com/products/edge-compute) and [Cloudflare Workers](https://developers.cloudflare.com/workers/)



To control access to the applications or services, WAF service providers use a set of rules called policies that filter traffic based on conditions. Conditions include IP address, IP range, region code, or request headers of an incoming request. Cloud Armor uses [security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview).

reCAPTCHA for WAF interacts with WAF service providers to do the following:

  1. The end user triggers an application action protected by reCAPTCHA for WAF.
  2. The reCAPTCHA JavaScript client issues an encrypted token that contains the reCAPTCHA's assessment and the associated attributes.
  3. The reCAPTCHA token is attached to the follow-up requests.
  4. The WAF service provider deciphers this token. Based on the token attributes and configured security rules, the WAF service provider allows, blocks, or redirects the incoming requests to an interstitial challenge page.

The following diagram is a graphical representation of how the WAF service provider interacts with reCAPTCHA for WAF to enforce frictionless assessment:

![](https://docs.cloud.google.com/static/recaptcha/images/token_overview.svg)![](https://docs.cloud.google.com/static/recaptcha/images/token_overview.svg)




## When to use reCAPTCHA for WAF integration

Use this integration when your application is already behind a WAF and you want to decouple reCAPTCHA policy changes from frontend and backend code.

## Benefits

The reCAPTCHA for WAF integration provides the following benefits:

  * The backend server code does not need to be modified as the integration occurs at the WAF layer.
  * Frontend JavaScript does not need to be modified as reCAPTCHA for WAF integrations can dynamically inject a JavaScript client integration (for session-token and challenge-page keys) or no client at all is needed (for express keys).
  * Bot traffic is mitigated at the edge of your network, reducing load on your protected backend.
  * [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview) streamline access rules to your protected application.



## What's next

  * Learn about the [features](https://docs.cloud.google.com/recaptcha/docs/features-ca) offered by reCAPTCHA for WAF.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
