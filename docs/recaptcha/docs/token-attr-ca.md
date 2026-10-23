---
url: https://docs.cloud.google.com/recaptcha/docs/token-attr-ca/
title: reCAPTCHA token attributes for Google Cloud Armor \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:19.236043+00:00
---

# reCAPTCHA token attributes for Google Cloud Armor  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/token-attr-ca/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  reCAPTCHA token attributes for Google Cloud Armor Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the reCAPTCHA action-tokens attributes and reCAPTCHA session-tokens attributes that you can use when configuring security policies for Cloud Armor.

## reCAPTCHA action-tokens attributes

The following table lists the reCAPTCHA action-tokens attributes for Cloud Armor:

Attribute name | Data type | Description  
---|---|---  
`score` | float | The score from a reCAPTCHA token. A valid score ranges from 0.0 to 1.0. The score 1.0 indicates that the interaction poses low risk and is likely legitimate, whereas 0.0 indicates that the interaction poses high risk and might be fraudulent. For more information, see [Interpreting scores](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment#interpret_scores).  
`captcha_status` | string | The CAPTCHA status from a reCAPTCHA token. The following are the three possible statuses: 

  * `NONE`: Challenges were not involved when assessing the user.
  * `PASS`: Challenges were involved, and the user solved them correctly.
  * `FAIL`: Challenges were involved, and the user failed to solve them.

  
`action` | string | `action` is the action parameter that you specified for a user interaction when calling `grecaptcha.enterprise.execute()`. For more information, see [Action names](https://docs.cloud.google.com/recaptcha/docs/actions-website). **Important:** Make sure to verify that the `action` attribute matches the `action` parameter that you specified when calling `grecaptcha.enterprise.execute()`. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.   
`key` | string | `key` is the reCAPTCHA key (action-token key) that you created and used in this request. For more information, see [reCAPTCHA keys overview](https://docs.cloud.google.com/recaptcha/docs/keys).   
  
## reCAPTCHA session-tokens attributes

The following table lists the reCAPTCHA session-tokens attributes for Cloud Armor:

Attribute name | Data type | Description  
---|---|---  
`Score` | float | The score from a reCAPTCHA token. A valid score ranges from 0.0 to 1.0. The score 1.0 indicates that the interaction poses low risk and is likely legitimate, whereas 0.0 indicates that the interaction poses high risk and might be fraudulent. For more information, see [Interpreting scores](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment#interpret_scores).  
`key` | string | `key` is the reCAPTCHA key (session-token key) that you created and used in this request. For more information, see [reCAPTCHA keys overview](https://docs.cloud.google.com/recaptcha/docs/keys).   
  
## What's next

  * Learn about the [features of reCAPTCHA for Cloud Armor](https://docs.cloud.google.com/recaptcha/docs/features-ca).
  * [Integrate reCAPTCHA for Cloud Armor](https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
