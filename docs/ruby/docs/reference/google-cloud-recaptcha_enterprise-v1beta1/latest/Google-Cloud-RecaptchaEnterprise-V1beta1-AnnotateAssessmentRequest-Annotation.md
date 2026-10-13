---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1beta1/latest/Google-Cloud-RecaptchaEnterprise-V1beta1-AnnotateAssessmentRequest-Annotation/
title: reCAPTCHA Enterprise V1beta1 API - Module Google::Cloud::RecaptchaEnterprise::V1beta1::AnnotateAssessmentRequest::Annotation (v0.21.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:14.577575+00:00
---

# reCAPTCHA Enterprise V1beta1 API - Module Google::Cloud::RecaptchaEnterprise::V1beta1::AnnotateAssessmentRequest::Annotation (v0.21.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recaptcha_enterprise-v1beta1/latest/Google-Cloud-RecaptchaEnterprise-V1beta1-AnnotateAssessmentRequest-Annotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  reCAPTCHA Enterprise V1beta1 API - Module Google::Cloud::RecaptchaEnterprise::V1beta1::AnnotateAssessmentRequest::Annotation (v0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.20.0  0.19.1  0.18.0  0.17.3  0.16.1  0.15.2  0.14.0  0.13.0  0.12.2  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the reCAPTCHA Enterprise V1beta1 API module Google::Cloud::RecaptchaEnterprise::V1beta1::AnnotateAssessmentRequest::Annotation.

Enum that represents the types of annotations.

## Constants 

### ANNOTATION_UNSPECIFIED

**value:** 0  
Default unspecified type.

### LEGITIMATE

**value:** 1  
Provides information that the event turned out to be legitimate.

### FRAUDULENT

**value:** 2  
Provides information that the event turned out to be fraudulent.

### PASSWORD_CORRECT

**value:** 3  
Provides information that the event was related to a login event in which the user typed the correct password. Deprecated, prefer indicating CORRECT_PASSWORD through the reasons field instead.

### PASSWORD_INCORRECT

**value:** 4  
Provides information that the event was related to a login event in which the user typed the incorrect password. Deprecated, prefer indicating INCORRECT_PASSWORD through the reasons field instead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
