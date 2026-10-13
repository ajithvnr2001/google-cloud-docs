---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-publishing-v1/latest/Google-Api-FieldBehavior/
title: Eventarc Publishing V1 API - Module Google::Api::FieldBehavior (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:12.496221+00:00
---

# Eventarc Publishing V1 API - Module Google::Api::FieldBehavior (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-publishing-v1/latest/Google-Api-FieldBehavior/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Eventarc Publishing V1 API - Module Google::Api::FieldBehavior (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.2  1.4.1  1.3.3  1.2.0  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Eventarc Publishing V1 API module Google::Api::FieldBehavior.

An indicator of the behavior of a given field (for example, that a field is required in requests, or given as output but ignored as input). This **does not** change the behavior in protocol buffers itself; it only denotes the behavior and may affect how API tooling handles the field.

Note: This enum **may** receive new values in the future.

## Constants 

### FIELD_BEHAVIOR_UNSPECIFIED

**value:** 0  
Conventional default for enums. Do not use this.

### OPTIONAL

**value:** 1  
Specifically denotes a field as optional. While all fields in protocol buffers are optional, this may be specified for emphasis if appropriate.

### REQUIRED

**value:** 2  
Denotes a field as required. This indicates that the field **must** be provided as part of the request, and failure to do so will cause an error (usually `INVALID_ARGUMENT`).

### OUTPUT_ONLY

**value:** 3  
Denotes a field as output only. This indicates that the field is provided in responses, but including the field in a request does nothing (the server _must_ ignore it and _must not_ throw an error as a result of the field's presence).

### INPUT_ONLY

**value:** 4  
Denotes a field as input only. This indicates that the field is provided in requests, and the corresponding field is not included in output.

### IMMUTABLE

**value:** 5  
Denotes a field as immutable. This indicates that the field may be set once in a request to create a resource, but may not be changed thereafter.

### UNORDERED_LIST

**value:** 6  
Denotes that a (repeated) field is an unordered list. This indicates that the service may provide the elements of the list in any arbitrary order, rather than the order the user originally provided. Additionally, the list's order may or may not be stable.

### NON_EMPTY_DEFAULT

**value:** 7  
Denotes that this field returns a non-empty default value if not set. This indicates that if the user provides the empty value in a request, a non-empty value will be returned. The user will not be aware of what non-empty value to expect.

### IDENTIFIER

**value:** 8  
Denotes that the field in a resource (a message annotated with google.api.resource) is used in the resource name to uniquely identify the resource. For AIP-compliant APIs, this should only be applied to the `name` field on the resource.

This behavior should not be applied to references to other resources within the message.

The identifier field of resources often have different field behavior depending on the request it is embedded in (e.g. for Create methods name is optional and unused, while for Update methods it is required). Instead of method-specific annotations, only `IDENTIFIER` is required.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
