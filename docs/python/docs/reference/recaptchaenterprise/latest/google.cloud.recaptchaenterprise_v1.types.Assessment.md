---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment
title: Class Assessment (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:54.022393+00:00
---

# Class Assessment (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Assessment (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    Assessment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A reCAPTCHA Enterprise assessment resource.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. The resource name for the Assessment in the format `projects/{project}/assessments/{assessment}`.   
`event` |  `[google.cloud.recaptchaenterprise_v1.types.Event](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Event)`   
Optional. The event being assessed.   
`risk_analysis` |  `[google.cloud.recaptchaenterprise_v1.types.RiskAnalysis](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RiskAnalysis)`   
Output only. The risk analysis result for the event being assessed.   
`token_properties` |  `[google.cloud.recaptchaenterprise_v1.types.TokenProperties](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.TokenProperties)`   
Output only. Properties of the provided event token.   
`account_verification` |  `[google.cloud.recaptchaenterprise_v1.types.AccountVerificationInfo](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AccountVerificationInfo)`   
Optional. Account verification information for identity verification. The assessment event must include a token and site key to use this feature.   
`account_defender_assessment` |  `[google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment)`   
Output only. Assessment returned by Account defense when an account identifier is provided.   
`private_password_leak_verification` |  `[google.cloud.recaptchaenterprise_v1.types.PrivatePasswordLeakVerification](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.PrivatePasswordLeakVerification)`   
Optional. The private password leak verification field contains the parameters that are used to to check for leaks privately without sharing user credentials.   
`firewall_policy_assessment` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallPolicyAssessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallPolicyAssessment)`   
Output only. Assessment returned when firewall policies belonging to the project are evaluated using the field firewall_policy_evaluation.   
`fraud_prevention_assessment` |  `[google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment)`   
Output only. Assessment returned by Fraud Prevention when TransactionData is provided.   
`fraud_signals` |  `[google.cloud.recaptchaenterprise_v1.types.FraudSignals](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FraudSignals)`   
Output only. Fraud Signals specific to the users involved in a payment transaction.   
`phone_fraud_assessment` |  `[google.cloud.recaptchaenterprise_v1.types.PhoneFraudAssessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.PhoneFraudAssessment)`   
Output only. Assessment returned when a site key, a token, and a phone number as `user_id` are provided. SMS defense needs to be enabled.   
`assessment_environment` |  `[google.cloud.recaptchaenterprise_v1.types.AssessmentEnvironment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AssessmentEnvironment)`   
Optional. The environment creating the assessment. This describes your environment (the system invoking CreateAssessment), NOT the environment of your user.   
`policy_evaluation` |  `[google.cloud.recaptchaenterprise_v1.types.PolicyEvaluation](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.PolicyEvaluation)`   
Output only. Provides information about the policy evaluation for this assessment.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
