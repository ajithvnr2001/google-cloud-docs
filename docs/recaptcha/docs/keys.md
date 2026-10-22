---
url: https://docs.cloud.google.com/recaptcha/docs/keys/
title: reCAPTCHA keys overview \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:01.264633+00:00
---

# reCAPTCHA keys overview  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/keys/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  reCAPTCHA keys overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of reCAPTCHA keys (also known as _keys_).

A reCAPTCHA key is a unique, case-sensitive string of 40 characters that needs to be installed on web pages, in mobile applications, or at the WAF layer to integrate reCAPTCHA.

A reCAPTCHA key returns a score for each request, which is based on the user interactions with your site or application. By interpreting these scores, you can take appropriate actions for your site or application, such as allowing or blocking users.

Example reCAPTCHA key: `6Lcm3XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX5mfX`

**Note:** In some parts of the API reference documentation, reCAPTCHA keys are also referred to as _site keys_.

reCAPTCHA keys can have one of the following integration types:

  * `SCORE`: Returns risk scores. It doesn't display the **I'm not a robot** checkbox and never shows CAPTCHA challenges.
  * `CHECKBOX`: Displays the **I'm not a robot** checkbox and might show CAPTCHA challenges after the checkbox is checked.
  * `POLICY_BASED_CHALLENGE`: Triggers CAPTCHA challenges based on a score threshold and challenge difficulty.
  * `INVISIBLE`: Doesn't display the **I'm not a robot** checkbox, but might show CAPTCHA challenges after risk analysis.

The following table lists reCAPTCHA keys that are supported for each platform: Platform | Description | Supported keys | Challenge type  
---|---|---|---  
web | For integration on web pages. | Score-based keys | `SCORE`  
Checkbox keys | `CHECKBOX`  
Policy-based challenge keys  | `POLICY_BASED_CHALLENGE`  
mobile | For integration with Android and iOS apps. | reCAPTCHA keys for Android | `SCORE`  
reCAPTCHA keys for iOS | `SCORE`  
WAF | For web pages and APIs served through WAF or Edge compute servers. | action-token keys | `SCORE` and `CHECKBOX`  
session-token keys | `SCORE`  
challenge-page keys | `INVISIBLE`  
API | For integration with APIs or clients like IoT devices that do not support the reCAPTCHA JavaScript or mobile SDKs. | express keys | `SCORE`  
  
## What's next

  * [Choose the appropriate reCAPTCHA key type for your platform](https://docs.cloud.google.com/recaptcha/docs/choose-key-type)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
