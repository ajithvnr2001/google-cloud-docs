---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Grafeas-V1-AttestationNote/
title: Binary Authorization V1 API - Class Grafeas::V1::AttestationNote (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:31.791292+00:00
---

# Binary Authorization V1 API - Class Grafeas::V1::AttestationNote (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Grafeas-V1-AttestationNote/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Binary Authorization V1 API - Class Grafeas::V1::AttestationNote (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.8.0  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.1  0.1.2 

Reference documentation and code samples for the Binary Authorization V1 API class Grafeas::V1::AttestationNote.

Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one `Authority` for "QA" and one for "build". This note is intended to act strictly as a grouping mechanism for the attached occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the ability for a principle to attach an occurrence to a given note. It also provides a single point of lookup to find all attached attestation occurrences, even if they don't all live in the same project.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #hint
    
    
    def hint() -> ::Grafeas::V1::AttestationNote::Hint

**Returns**

  * ([::Grafeas::V1::AttestationNote::Hint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Grafeas-V1-AttestationNote-Hint)) — Hint hints at the purpose of the attestation authority. 



### #hint=
    
    
    def hint=(value) -> ::Grafeas::V1::AttestationNote::Hint

**Parameter**

  * **value** ([::Grafeas::V1::AttestationNote::Hint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Grafeas-V1-AttestationNote-Hint)) — Hint hints at the purpose of the attestation authority. 



**Returns**

  * ([::Grafeas::V1::AttestationNote::Hint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Grafeas-V1-AttestationNote-Hint)) — Hint hints at the purpose of the attestation authority. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
