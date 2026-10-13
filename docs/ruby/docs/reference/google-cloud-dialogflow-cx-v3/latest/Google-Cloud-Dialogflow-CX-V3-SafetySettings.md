---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::SafetySettings (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:27.175470+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::SafetySettings (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::SafetySettings (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::SafetySettings.

Settings for Generative Safety.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #banned_phrases
    
    
    def banned_phrases() -> ::Array<::Google::Cloud::Dialogflow::CX::V3::SafetySettings::Phrase>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::SafetySettings::Phrase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-Phrase)>) — Banned phrases for generated text. 



### #banned_phrases=
    
    
    def banned_phrases=(value) -> ::Array<::Google::Cloud::Dialogflow::CX::V3::SafetySettings::Phrase>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::CX::V3::SafetySettings::Phrase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-Phrase)>) — Banned phrases for generated text. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::SafetySettings::Phrase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-Phrase)>) — Banned phrases for generated text. 



### #default_banned_phrase_match_strategy
    
    
    def default_banned_phrase_match_strategy() -> ::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PhraseMatchStrategy

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PhraseMatchStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-PhraseMatchStrategy)) — Optional. Default phrase match strategy for banned phrases. 



### #default_banned_phrase_match_strategy=
    
    
    def default_banned_phrase_match_strategy=(value) -> ::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PhraseMatchStrategy

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PhraseMatchStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-PhraseMatchStrategy)) — Optional. Default phrase match strategy for banned phrases. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PhraseMatchStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-PhraseMatchStrategy)) — Optional. Default phrase match strategy for banned phrases. 



### #default_rai_settings
    
    
    def default_rai_settings() -> ::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-RaiSettings)) — Optional. Immutable. Default RAI settings to be annotated on the agent, so that users will be able to restore their RAI configurations to the default settings. Read-only field for the API proto only. 



### #default_rai_settings=
    
    
    def default_rai_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-RaiSettings)) — Optional. Immutable. Default RAI settings to be annotated on the agent, so that users will be able to restore their RAI configurations to the default settings. Read-only field for the API proto only. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-RaiSettings)) — Optional. Immutable. Default RAI settings to be annotated on the agent, so that users will be able to restore their RAI configurations to the default settings. Read-only field for the API proto only. 



### #prompt_security_settings
    
    
    def prompt_security_settings() -> ::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PromptSecuritySettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PromptSecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-PromptSecuritySettings)) — Optional. Settings for prompt security checks. 



### #prompt_security_settings=
    
    
    def prompt_security_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PromptSecuritySettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PromptSecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-PromptSecuritySettings)) — Optional. Settings for prompt security checks. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::PromptSecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-PromptSecuritySettings)) — Optional. Settings for prompt security checks. 



### #rai_settings
    
    
    def rai_settings() -> ::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-RaiSettings)) — Optional. Settings for Responsible AI checks. 



### #rai_settings=
    
    
    def rai_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-RaiSettings)) — Optional. Settings for Responsible AI checks. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SafetySettings::RaiSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SafetySettings-RaiSettings)) — Optional. Settings for Responsible AI checks. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
