---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings/
title: GenerativeSettings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:32.926851+00:00
---

# GenerativeSettings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  GenerativeSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FallbackSettings
    * JSON representation
  * PromptTemplate
    * JSON representation
  * SafetySettings
    * JSON representation
  * PhraseMatchStrategy
  * Phrase
    * JSON representation
  * RaiSettings
    * JSON representation
  * CategoryFilter
    * JSON representation
  * SafetyCategory
  * SafetyFilterLevel
  * PromptSecuritySettings
    * JSON representation
  * KnowledgeConnectorSettings
    * JSON representation



Settings for Generative AI.

JSON representation  
---  
      
    
    {
      "name": string,
      "fallbackSettings": {
        object ([FallbackSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#FallbackSettings))
      },
      "generativeSafetySettings": {
        object ([SafetySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#SafetySettings))
      },
      "knowledgeConnectorSettings": {
        object ([KnowledgeConnectorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#KnowledgeConnectorSettings))
      },
      "languageCode": string,
      "llmModelSettings": {
        object ([LlmModelSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/LlmModelSettings))
      }
    }  
  
Fields  
---  
`name` |  `string` Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`fallbackSettings` |  `object (`[FallbackSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#FallbackSettings)`)` Settings for Generative Fallback.  
`generativeSafetySettings` |  `object (`[SafetySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#SafetySettings)`)` Settings for Generative Safety.  
`knowledgeConnectorSettings` |  `object (`[KnowledgeConnectorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#KnowledgeConnectorSettings)`)` Settings for knowledge connector.  
`languageCode` |  `string` Language for this settings.  
`llmModelSettings` |  `object (`[LlmModelSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/LlmModelSettings)`)` LLM model settings.  
  
## FallbackSettings

Settings for Generative Fallback.

JSON representation  
---  
      
    
    {
      "selectedPrompt": string,
      "promptTemplates": [
        {
          object ([PromptTemplate](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#PromptTemplate))
        }
      ]
    }  
  
Fields  
---  
`selectedPrompt` |  `string` Display name of the selected prompt.  
`promptTemplates[]` |  `object (`[PromptTemplate](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#PromptTemplate)`)` Stored prompts that can be selected, for example default templates like "conservative" or "chatty", or user defined ones.  
  
## PromptTemplate

Prompt template.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "promptText": string,
      "frozen": boolean
    }  
  
Fields  
---  
`displayName` |  `string` Prompt name.  
`promptText` |  `string` Prompt text that is sent to a LLM on no-match default, placeholders are filled downstream. For example: "Here is a conversation $conversation, a response is: "  
`frozen` |  `boolean` If the flag is true, the prompt is frozen and cannot be modified by users.  
  
## SafetySettings

Settings for Generative Safety.

JSON representation  
---  
      
    
    {
      "defaultBannedPhraseMatchStrategy": enum ([PhraseMatchStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#PhraseMatchStrategy)),
      "bannedPhrases": [
        {
          object ([Phrase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#Phrase))
        }
      ],
      "raiSettings": {
        object ([RaiSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#RaiSettings))
      },
      "defaultRaiSettings": {
        object ([RaiSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#RaiSettings))
      },
      "promptSecuritySettings": {
        object ([PromptSecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#PromptSecuritySettings))
      }
    }  
  
Fields  
---  
`defaultBannedPhraseMatchStrategy` |  `enum (`[PhraseMatchStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#PhraseMatchStrategy)`)` Optional. Default phrase match strategy for banned phrases.  
`bannedPhrases[]` |  `object (`[Phrase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#Phrase)`)` Banned phrases for generated text.  
`raiSettings` |  `object (`[RaiSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#RaiSettings)`)` Optional. Settings for Responsible AI checks.  
`defaultRaiSettings` |  `object (`[RaiSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#RaiSettings)`)` Optional. Immutable. Default RAI settings to be annotated on the agent, so that users will be able to restore their RAI configurations to the default settings. Read-only field for the API proto only.  
`promptSecuritySettings` |  `object (`[PromptSecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#PromptSecuritySettings)`)` Optional. Settings for prompt security checks.  
  
## PhraseMatchStrategy

Strategy for matching phrases.

Enums  
---  
`PHRASE_MATCH_STRATEGY_UNSPECIFIED` | Unspecified, defaults to PARTIAL_MATCH.  
`PARTIAL_MATCH` | Text that contains the phrase as a substring will be matched, e.g. "foo" will match "afoobar".  
`WORD_MATCH` | Text that contains the tokenized words of the phrase will be matched, e.g. "foo" will match "a foo bar" and "foo bar", but not "foobar".  
  
## Phrase

Text input which can be used for prompt or banned phrases.

JSON representation  
---  
      
    
    {
      "text": string,
      "languageCode": string
    }  
  
Fields  
---  
`text` |  `string` Required. Text input which can be used for prompt or banned phrases.  
`languageCode` |  `string` Required. Language code of the phrase.  
  
## RaiSettings

Settings for Responsible AI.

JSON representation  
---  
      
    
    {
      "categoryFilters": [
        {
          object ([CategoryFilter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#CategoryFilter))
        }
      ]
    }  
  
Fields  
---  
`categoryFilters[]` |  `object (`[CategoryFilter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#CategoryFilter)`)` Optional. RAI blocking configurations.  
  
## CategoryFilter

Configuration of the sensitivity level for blocking an RAI category.

JSON representation  
---  
      
    
    {
      "category": enum ([SafetyCategory](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#SafetyCategory)),
      "filterLevel": enum ([SafetyFilterLevel](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#SafetyFilterLevel))
    }  
  
Fields  
---  
`category` |  `enum (`[SafetyCategory](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#SafetyCategory)`)` RAI category to configure.  
`filterLevel` |  `enum (`[SafetyFilterLevel](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/GenerativeSettings#SafetyFilterLevel)`)` Blocking sensitivity level to configure for the RAI category.  
  
## SafetyCategory

RAI categories to configure.

Enums  
---  
`SAFETY_CATEGORY_UNSPECIFIED` | Unspecified.  
`DANGEROUS_CONTENT` | Dangerous content.  
`HATE_SPEECH` | Hate speech.  
`HARASSMENT` | Harassment.  
`SEXUALLY_EXPLICIT_CONTENT` | Sexually explicit content.  
  
## SafetyFilterLevel

Sensitivity level for RAI categories.

Enums  
---  
`SAFETY_FILTER_LEVEL_UNSPECIFIED` | Unspecified -- uses default sensitivity levels.  
`BLOCK_NONE` | Block no text -- effectively disables the category.  
`BLOCK_FEW` | Block a few suspicious texts.  
`BLOCK_SOME` | Block some suspicious texts.  
`BLOCK_MOST` | Block most suspicious texts.  
  
## PromptSecuritySettings

Settings for prompt security checks.

JSON representation  
---  
      
    
    {
      "enablePromptSecurity": boolean
    }  
  
Fields  
---  
`enablePromptSecurity` |  `boolean` Optional. Enable prompt security checks.  
  
## KnowledgeConnectorSettings

Settings for knowledge connector. These parameters are used for LLM prompt like "You are . You are a helpful and verbose  at , . Your task is to help humans on ".

JSON representation  
---  
      
    
    {
      "business": string,
      "agent": string,
      "agentIdentity": string,
      "businessDescription": string,
      "agentScope": string,
      "disableDataStoreFallback": boolean
    }  
  
Fields  
---  
`business` |  `string` Name of the company, organization or other entity that the agent represents. Used for knowledge connector LLM prompt and for knowledge search.  
`agent` |  `string` Name of the virtual agent. Used for LLM prompt. Can be left empty.  
`agentIdentity` |  `string` Identity of the agent, e.g. "virtual agent", "AI assistant".  
`businessDescription` |  `string` Company description, used for LLM prompt, e.g. "a family company selling freshly roasted coffee beans".  
`agentScope` |  `string` Agent scope, e.g. "Example company website", "internal Example company website for employees", "manual of car owner".  
`disableDataStoreFallback` |  `boolean` Whether to disable fallback to Data Store search results (in case the LLM couldn't pick a proper answer). Per default the feature is enabled.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-20 UTC."],[],[]] 
