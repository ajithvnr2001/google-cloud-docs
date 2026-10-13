---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Reason
title: Class Reason (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:53.617384+00:00
---

# Class Reason (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Reason

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Reason (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    Reason(value)

Enum that represents potential reasons for annotating an assessment.

## Enums  
  
---  
**Name** | **Description**  
`REASON_UNSPECIFIED` | Unspecified reason. Do not use.  
`CHARGEBACK` | Indicates that the transaction had a chargeback issued with no other details. When possible, specify the type by using CHARGEBACK_FRAUD or CHARGEBACK_DISPUTE instead.  
`CHARGEBACK_FRAUD` | Indicates that the transaction had a chargeback issued related to an alleged unauthorized transaction from the cardholder's perspective (for example, the card number was stolen).  
`CHARGEBACK_DISPUTE` | Indicates that the transaction had a chargeback issued related to the cardholder having provided their card details but allegedly not being satisfied with the purchase (for example, misrepresentation, attempted cancellation).  
`REFUND` | Indicates that the completed payment transaction was refunded by the seller.  
`REFUND_FRAUD` | Indicates that the completed payment transaction was determined to be fraudulent by the seller, and was cancelled and refunded as a result.  
`TRANSACTION_ACCEPTED` | Indicates that the payment transaction was accepted, and the user was charged.  
`TRANSACTION_DECLINED` | Indicates that the payment transaction was declined, for example due to invalid card details.  
`PAYMENT_HEURISTICS` | Indicates the transaction associated with the assessment is suspected of being fraudulent based on the payment method, billing details, shipping address or other transaction information.  
`INITIATED_TWO_FACTOR` | Indicates that the user was served a 2FA challenge. An old assessment with `ENUM_VALUES.INITIATED_TWO_FACTOR` reason that has not been overwritten with `PASSED_TWO_FACTOR` is treated as an abandoned 2FA flow. This is equivalent to `FAILED_TWO_FACTOR`.  
`PASSED_TWO_FACTOR` | Indicates that the user passed a 2FA challenge.  
`FAILED_TWO_FACTOR` | Indicates that the user failed a 2FA challenge.  
`CORRECT_PASSWORD` | Indicates the user provided the correct password.  
`INCORRECT_PASSWORD` | Indicates the user provided an incorrect password.  
`SOCIAL_SPAM` | Indicates that the user sent unwanted and abusive messages to other users of the platform, such as spam, scams, phishing, or social engineering.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
