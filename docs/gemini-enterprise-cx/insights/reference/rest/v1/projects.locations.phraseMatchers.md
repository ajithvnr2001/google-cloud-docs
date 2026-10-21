---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers
title: REST Resource: projects.locations.phraseMatchers \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:46:16.797768+00:00
---

# REST Resource: projects.locations.phraseMatchers  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.phraseMatchers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PhraseMatcher
    * JSON representation
  * PhraseMatcherType
  * PhraseMatchRuleGroup
    * JSON representation
  * PhraseMatchRuleGroupType
  * PhraseMatchRule
    * JSON representation
  * PhraseMatchRuleConfig
    * JSON representation
  * ExactMatchConfig
    * JSON representation
  * Methods



## Resource: PhraseMatcher

The phrase matcher resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "revisionId": string,
      "versionTag": string,
      "revisionCreateTime": string,
      "displayName": string,
      "type": enum ([PhraseMatcherType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatcherType)),
      "active": boolean,
      "phraseMatchRuleGroups": [
        {
          object ([PhraseMatchRuleGroup](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRuleGroup))
        }
      ],
      "activationUpdateTime": string,
      "roleMatch": enum ([Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Role)),
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` The resource name of the phrase matcher. Format: projects/{project}/locations/{location}/phraseMatchers/{phraseMatcher}  
`revisionId` |  `string` Output only. Immutable. The revision ID of the phrase matcher. A new revision is committed whenever the matcher is changed, except when it is activated or deactivated. A server generated random ID will be used. Example: locations/global/phraseMatchers/my-first-matcher@1234567  
`versionTag` |  `string` The customized version tag to use for the phrase matcher. If not specified, it will default to `revisionId`.  
`revisionCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the revision was created. It is also the create time when a new matcher is added.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` The human-readable name of the phrase matcher.  
`type` |  `enum (`[PhraseMatcherType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatcherType)`)` Required. The type of this phrase matcher.  
`active` |  `boolean` Applies the phrase matcher only when it is active.  
`phraseMatchRuleGroups[]` |  `object (`[PhraseMatchRuleGroup](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRuleGroup)`)` A list of phase match rule groups that are included in this matcher.  
`activationUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time at which the activation status was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`roleMatch` |  `enum (`[Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Role)`)` The role whose utterances the phrase matcher should be matched against. If the role is ROLE_UNSPECIFIED it will be matched against any utterances in the transcript.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time at which the phrase matcher was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## PhraseMatcherType

Specifies how to combine each phrase match rule group to determine whether there is a match.

Enums  
---  
`PHRASE_MATCHER_TYPE_UNSPECIFIED` | Unspecified.  
`ALL_OF` | Must meet all phrase match rule groups or there is no match.  
`ANY_OF` | If any of the phrase match rule groups are met, there is a match.  
  
## PhraseMatchRuleGroup

A message representing a rule in the phrase matcher.

JSON representation  
---  
      
    
    {
      "type": enum ([PhraseMatchRuleGroupType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRuleGroupType)),
      "phraseMatchRules": [
        {
          object ([PhraseMatchRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRule))
        }
      ]
    }  
  
Fields  
---  
`type` |  `enum (`[PhraseMatchRuleGroupType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRuleGroupType)`)` Required. The type of this phrase match rule group.  
`phraseMatchRules[]` |  `object (`[PhraseMatchRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRule)`)` A list of phrase match rules that are included in this group.  
  
## PhraseMatchRuleGroupType

Specifies how to combine each phrase match rule for whether there is a match.

Enums  
---  
`PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED` | Unspecified.  
`ALL_OF` | Must meet all phrase match rules or there is no match.  
`ANY_OF` | If any of the phrase match rules are met, there is a match.  
  
## PhraseMatchRule

The data for a phrase match rule.

JSON representation  
---  
      
    
    {
      "query": string,
      "negated": boolean,
      "config": {
        object ([PhraseMatchRuleConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRuleConfig))
      }
    }  
  
Fields  
---  
`query` |  `string` Required. The phrase to be matched.  
`negated` |  `boolean` Specifies whether the phrase must be missing from the transcript segment or present in the transcript segment.  
`config` |  `object (`[PhraseMatchRuleConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRuleConfig)`)` Provides additional information about the rule that specifies how to apply the rule.  
  
## PhraseMatchRuleConfig

Configuration information of a phrase match rule.

JSON representation  
---  
      
    
    {
    
      // Union field config can be only one of the following:
      "exactMatchConfig": {
        object ([ExactMatchConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#ExactMatchConfig))
      }
      // End of list of possible types for union field config.
    }  
  
Fields  
---  
Union field `config`. The configuration of the phrase match rule. `config` can be only one of the following:  
`exactMatchConfig` |  `object (`[ExactMatchConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#ExactMatchConfig)`)` The configuration for the exact match rule.  
  
## ExactMatchConfig

Exact match configuration.

JSON representation  
---  
      
    
    {
      "caseSensitive": boolean
    }  
  
Fields  
---  
`caseSensitive` |  `boolean` Whether to consider case sensitivity when performing an exact match.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/create)`

|  Creates a phrase matcher.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/delete)`

|  Deletes a phrase matcher.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/get)`

|  Gets a phrase matcher.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/list)`

|  Lists phrase matchers.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/patch)`

|  Updates a phrase matcher.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
