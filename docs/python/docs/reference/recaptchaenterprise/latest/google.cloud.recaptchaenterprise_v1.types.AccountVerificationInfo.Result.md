---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AccountVerificationInfo.Result
title: Class Result (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:53.215211+00:00
---

# Class Result (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AccountVerificationInfo.Result

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Result (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    Result(value)

Result of the account verification as contained in the verdict token issued at the end of the verification flow. Ensure that applications can handle values not explicitly listed.

## Enums  
  
---  
**Name** | **Description**  
`RESULT_UNSPECIFIED` | No information about the latest account verification.  
`SUCCESS_USER_VERIFIED` | The user was successfully verified. This means the account verification challenge was successfully completed.  
`ERROR_USER_NOT_VERIFIED` | The user failed the verification challenge.  
`ERROR_SITE_ONBOARDING_INCOMPLETE` | The site is not properly onboarded to use the account verification feature.  
`ERROR_RECIPIENT_NOT_ALLOWED` | The recipient is not allowed for account verification. This can occur during integration but should not occur in production.  
`ERROR_RECIPIENT_ABUSE_LIMIT_EXHAUSTED` | The recipient has already been sent too many verification codes in a short amount of time.  
`ERROR_CRITICAL_INTERNAL` | The verification flow could not be completed due to a critical internal error.  
`ERROR_CUSTOMER_QUOTA_EXHAUSTED` | The client has exceeded their two factor request quota for this period of time.  
`ERROR_VERIFICATION_BYPASSED` | The request cannot be processed at the time because of an incident. This bypass can be restricted to a problematic destination email domain, a customer, or could affect the entire service.  
`ERROR_VERDICT_MISMATCH` | The request parameters do not match with the token provided and cannot be processed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
