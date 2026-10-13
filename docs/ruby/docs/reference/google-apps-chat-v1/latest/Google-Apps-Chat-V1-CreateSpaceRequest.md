---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-CreateSpaceRequest/
title: Google Chat V1 API - Class Google::Apps::Chat::V1::CreateSpaceRequest (v0.31.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:14.181510+00:00
---

# Google Chat V1 API - Class Google::Apps::Chat::V1::CreateSpaceRequest (v0.31.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-CreateSpaceRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Chat V1 API - Class Google::Apps::Chat::V1::CreateSpaceRequest (v0.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.0 (latest)  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Google Chat V1 API class Google::Apps::Chat::V1::CreateSpaceRequest.

A request to create a named space with no members.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — 

Optional. A unique ID for this request. A random UUID is recommended. Specifying a request ID makes the request idempotent, which ensures that multiple identical requests with the same request ID result in only a single space being created. Subsequent requests with the same request ID return the existing space and do not update the space, even if the requested details differ from the current state.

To use this field effectively:

    * Ensure that subsequent requests are identical and use the same authentication credentials as the original request.
    * If a space was already created with the provided request ID, the request returns that space. Note that the returned space might not be fully populated; the API echoes the space in your request with the system-assigned resource name populated. To retrieve the latest metadata for the space, call `GetSpace`.
    * Reusing an existing request ID with a different authenticated user results in an error.



### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. A unique ID for this request. A random UUID is recommended. Specifying a request ID makes the request idempotent, which ensures that multiple identical requests with the same request ID result in only a single space being created. Subsequent requests with the same request ID return the existing space and do not update the space, even if the requested details differ from the current state.

To use this field effectively:

    * Ensure that subsequent requests are identical and use the same authentication credentials as the original request.
    * If a space was already created with the provided request ID, the request returns that space. Note that the returned space might not be fully populated; the API echoes the space in your request with the system-assigned resource name populated. To retrieve the latest metadata for the space, call `GetSpace`.
    * Reusing an existing request ID with a different authenticated user results in an error.



**Returns**

  * (::String) — 

Optional. A unique ID for this request. A random UUID is recommended. Specifying a request ID makes the request idempotent, which ensures that multiple identical requests with the same request ID result in only a single space being created. Subsequent requests with the same request ID return the existing space and do not update the space, even if the requested details differ from the current state.

To use this field effectively:

    * Ensure that subsequent requests are identical and use the same authentication credentials as the original request.
    * If a space was already created with the provided request ID, the request returns that space. Note that the returned space might not be fully populated; the API echoes the space in your request with the system-assigned resource name populated. To retrieve the latest metadata for the space, call `GetSpace`.
    * Reusing an existing request ID with a different authenticated user results in an error.



### #space
    
    
    def space() -> ::Google::Apps::Chat::V1::Space

**Returns**

  * ([::Google::Apps::Chat::V1::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Space)) — Required. The `displayName` and `spaceType` fields must be populated. Only `SpaceType.SPACE` and `SpaceType.GROUP_CHAT` are supported. `SpaceType.GROUP_CHAT` can only be used if `importMode` is set to true.

If you receive the error message `ALREADY_EXISTS`, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.

The space `name` is assigned on the server so anything specified in this field will be ignored. 




### #space=
    
    
    def space=(value) -> ::Google::Apps::Chat::V1::Space

**Parameter**

  * **value** ([::Google::Apps::Chat::V1::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Space)) — Required. The `displayName` and `spaceType` fields must be populated. Only `SpaceType.SPACE` and `SpaceType.GROUP_CHAT` are supported. `SpaceType.GROUP_CHAT` can only be used if `importMode` is set to true.

If you receive the error message `ALREADY_EXISTS`, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.

The space `name` is assigned on the server so anything specified in this field will be ignored. 




**Returns**

  * ([::Google::Apps::Chat::V1::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Space)) — Required. The `displayName` and `spaceType` fields must be populated. Only `SpaceType.SPACE` and `SpaceType.GROUP_CHAT` are supported. `SpaceType.GROUP_CHAT` can only be used if `importMode` is set to true.

If you receive the error message `ALREADY_EXISTS`, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.

The space `name` is assigned on the server so anything specified in this field will be ignored. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
