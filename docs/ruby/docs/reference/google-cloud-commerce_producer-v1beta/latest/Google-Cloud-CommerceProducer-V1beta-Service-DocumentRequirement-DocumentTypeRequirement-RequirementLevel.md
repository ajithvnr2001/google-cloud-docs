---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-Service-DocumentRequirement-DocumentTypeRequirement-RequirementLevel/
title: Cloud Commerce Producer V1BETA API - Module Google::Cloud::CommerceProducer::V1beta::Service::DocumentRequirement::DocumentTypeRequirement::RequirementLevel (v0.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:42.880554+00:00
---

# Cloud Commerce Producer V1BETA API - Module Google::Cloud::CommerceProducer::V1beta::Service::DocumentRequirement::DocumentTypeRequirement::RequirementLevel (v0.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-Service-DocumentRequirement-DocumentTypeRequirement-RequirementLevel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Commerce Producer V1BETA API - Module Google::Cloud::CommerceProducer::V1beta::Service::DocumentRequirement::DocumentTypeRequirement::RequirementLevel (v0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.0 

Reference documentation and code samples for the Cloud Commerce Producer V1BETA API module Google::Cloud::CommerceProducer::V1beta::Service::DocumentRequirement::DocumentTypeRequirement::RequirementLevel.

Requirement level for the document type.

## Constants 

### REQUIREMENT_LEVEL_UNSPECIFIED

**value:** 0  
Unspecified requirement level. Do not use.

### REQUIRED

**value:** 1  
The document type is mandatory for private offers on this service. Exactly one document of this type must be attached.

### OPTIONAL

**value:** 2  
The document type is optional for private offers on this service. At most one document of this type may be attached.

### NOT_ALLOWED

**value:** 3  
The document type is not permitted for private offers on this service. No document of this type may be attached.

A document type omitted from `document_type_requirements` is also not permitted. This value is used to state the restriction explicitly.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
