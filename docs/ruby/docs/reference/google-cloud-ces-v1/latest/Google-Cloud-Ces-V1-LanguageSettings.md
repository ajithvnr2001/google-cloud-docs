---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-LanguageSettings/
title: Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::LanguageSettings (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:09.391742+00:00
---

# Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::LanguageSettings (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-LanguageSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::LanguageSettings (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1 API class Google::Cloud::Ces::V1::LanguageSettings.

Language settings of the app.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #default_language_code
    
    
    def default_language_code() -> ::String

**Returns**

  * (::String) — Optional. The default language code of the app. 



### #default_language_code=
    
    
    def default_language_code=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The default language code of the app. 



**Returns**

  * (::String) — Optional. The default language code of the app. 



### #enable_multilingual_support
    
    
    def enable_multilingual_support() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Enables multilingual support. If true, agents in the app will use pre-built instructions to improve handling of multilingual input. 



### #enable_multilingual_support=
    
    
    def enable_multilingual_support=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Enables multilingual support. If true, agents in the app will use pre-built instructions to improve handling of multilingual input. 



**Returns**

  * (::Boolean) — Optional. Enables multilingual support. If true, agents in the app will use pre-built instructions to improve handling of multilingual input. 



### #fallback_action
    
    
    def fallback_action() -> ::String

**Returns**

  * (::String) — 

Optional. Deprecated: This feature is no longer supported. Use `enable_multilingual_support` instead to improve handling of multilingual input. The action to perform when an agent receives input in an unsupported language.

This can be a predefined action or a custom tool call. Valid values are:

    * A tool's full resource name, which triggers a specific tool execution.
    * A predefined system action, such as "escalate" or "exit", which triggers an [EndSession](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EndSession "Google::Cloud::Ces::V1::EndSession \(class\)") signal with corresponding [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EndSession#Google__Cloud__Ces__V1__EndSession_metadata_instance_ "Google::Cloud::Ces::V1::EndSession#metadata \(method\)") to terminate the conversation.



### #fallback_action=
    
    
    def fallback_action=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. Deprecated: This feature is no longer supported. Use `enable_multilingual_support` instead to improve handling of multilingual input. The action to perform when an agent receives input in an unsupported language.

This can be a predefined action or a custom tool call. Valid values are:

    * A tool's full resource name, which triggers a specific tool execution.
    * A predefined system action, such as "escalate" or "exit", which triggers an [EndSession](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EndSession "Google::Cloud::Ces::V1::EndSession \(class\)") signal with corresponding [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EndSession#Google__Cloud__Ces__V1__EndSession_metadata_instance_ "Google::Cloud::Ces::V1::EndSession#metadata \(method\)") to terminate the conversation.



**Returns**

  * (::String) — 

Optional. Deprecated: This feature is no longer supported. Use `enable_multilingual_support` instead to improve handling of multilingual input. The action to perform when an agent receives input in an unsupported language.

This can be a predefined action or a custom tool call. Valid values are:

    * A tool's full resource name, which triggers a specific tool execution.
    * A predefined system action, such as "escalate" or "exit", which triggers an [EndSession](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EndSession "Google::Cloud::Ces::V1::EndSession \(class\)") signal with corresponding [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EndSession#Google__Cloud__Ces__V1__EndSession_metadata_instance_ "Google::Cloud::Ces::V1::EndSession#metadata \(method\)") to terminate the conversation.



### #supported_language_codes
    
    
    def supported_language_codes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. List of languages codes supported by the app, in addition to the `default_language_code`. 



### #supported_language_codes=
    
    
    def supported_language_codes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. List of languages codes supported by the app, in addition to the `default_language_code`. 



**Returns**

  * (::Array<::String>) — Optional. List of languages codes supported by the app, in addition to the `default_language_code`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
