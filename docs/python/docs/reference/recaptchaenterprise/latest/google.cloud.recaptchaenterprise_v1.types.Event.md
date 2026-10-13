---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Event
title: Class Event (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:55.667895+00:00
---

# Class Event (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Event

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Event (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    Event(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The event being assessed.

## Attributes  
  
---  
**Name** | **Description**  
`token` |  `str`   
Optional. The user response token provided by the reCAPTCHA Enterprise client-side integration on your site.   
`site_key` |  `str`   
Optional. The site key that was used to invoke reCAPTCHA Enterprise on your site and generate the token.   
`user_agent` |  `str`   
Optional. The user agent present in the request from the user's device related to this event.   
`user_ip_address` |  `str`   
Optional. The IP address in the request from the user's device related to this event.   
`expected_action` |  `str`   
Optional. The expected action for this type of event. This should be the same action provided at token generation time on client-side platforms already integrated with recaptcha enterprise. Required for Universal keys.   
`hashed_account_id` |  `bytes`   
Optional. Deprecated: use `user_info.account_id` instead. Unique stable hashed user identifier for the request. The identifier must be hashed using hmac-sha256 with stable secret.   
`express` |  `bool`   
Optional. Flag for a reCAPTCHA express request for an assessment without a token. If enabled, `site_key` must reference an Express site key.   
`requested_uri` |  `str`   
Optional. The URI resource the user requested that triggered an assessment.   
`waf_token_assessment` |  `bool`   
Optional. Flag for running Web Application Firewall (WAF) token assessment. If enabled, the token must be specified, and have been created by a WAF-enabled key.   
`ja3` |  `str`   
Optional. JA3 fingerprint for SSL clients. To learn how to compute this fingerprint, please refer to https://github.com/salesforce/ja3.   
`ja4` |  `str`   
Optional. JA4 fingerprint for SSL clients. To learn how to compute this fingerprint, please refer to https://github.com/FoxIO-LLC/ja4.   
`headers` |  `MutableSequence[str]`   
Optional. HTTP header information about the request.   
`firewall_policy_evaluation` |  `bool`   
Optional. Flag for enabling firewall policy config assessment. If this flag is enabled, the firewall policy is evaluated and a suggested firewall action is returned in the response.   
`transaction_data` |  `[google.cloud.recaptchaenterprise_v1.types.TransactionData](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.TransactionData)`   
Optional. Data describing a payment transaction to be assessed. Sending this data enables reCAPTCHA Enterprise Fraud Prevention and the FraudPreventionAssessment component in the response.   
`user_info` |  `[google.cloud.recaptchaenterprise_v1.types.UserInfo](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UserInfo)`   
Optional. Information about the user that generates this event, when they can be identified. They are often identified through the use of an account for logged-in requests or login/registration requests, or by providing user identifiers for guest actions like checkout.   
`fraud_prevention` |  `[google.cloud.recaptchaenterprise_v1.types.Event.FraudPrevention](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Event.FraudPrevention)`   
Optional. The Fraud Prevention setting for this assessment.   
  
## Classes 

### FraudPrevention
    
    
    FraudPrevention(value)

Setting that controls Fraud Prevention assessments. Ensure that applications can handle values not explicitly listed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
