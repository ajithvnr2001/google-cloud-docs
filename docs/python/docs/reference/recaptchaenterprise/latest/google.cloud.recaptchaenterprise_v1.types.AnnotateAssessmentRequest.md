---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest
title: Class AnnotateAssessmentRequest (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:53.689095+00:00
---

# Class AnnotateAssessmentRequest (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AnnotateAssessmentRequest (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    AnnotateAssessmentRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request message to annotate an Assessment.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource name of the Assessment, in the format `projects/{project}/assessments/{assessment}`.   
`annotation` |  `[google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Annotation](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Annotation)`   
Optional. The annotation that is assigned to the Event. This field can be left empty to provide reasons that apply to an event without concluding whether the event is legitimate or fraudulent.   
`reasons` |  `MutableSequence[[google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Reason](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Reason)]`   
Optional. Reasons for the annotation that are assigned to the event.   
`account_id` |  `str`   
Optional. A stable account identifier to apply to the assessment. This is an alternative to setting `account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request.   
`hashed_account_id` |  `bytes`   
Optional. A stable hashed account identifier to apply to the assessment. This is an alternative to setting `hashed_account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request.   
`transaction_event` |  `[google.cloud.recaptchaenterprise_v1.types.TransactionEvent](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.TransactionEvent)`   
Optional. If the assessment is part of a payment transaction, provide details on payment lifecycle events that occur in the transaction.   
`phone_authentication_event` |  `[google.cloud.recaptchaenterprise_v1.types.PhoneAuthenticationEvent](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.PhoneAuthenticationEvent)`   
Optional. If using an external multi-factor authentication provider, provide phone authentication details for fraud detection purposes.   
  
## Classes 

### Annotation
    
    
    Annotation(value)

Enum that represents the types of annotations.

### Reason
    
    
    Reason(value)

Enum that represents potential reasons for annotating an assessment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
