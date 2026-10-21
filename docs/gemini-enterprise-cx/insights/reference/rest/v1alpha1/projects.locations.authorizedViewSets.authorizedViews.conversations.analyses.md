---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses
title: REST Resource: projects.locations.authorizedViewSets.authorizedViews.conversations.analyses \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:28:14.412636+00:00
---

# REST Resource: projects.locations.authorizedViewSets.authorizedViews.conversations.analyses  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.authorizedViewSets.authorizedViews.conversations.analyses Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Analysis
    * JSON representation
    * AnalysisResult
      * JSON representation
    * CallAnalysisMetadata
      * JSON representation
    * CallAnnotation
      * JSON representation
    * InterruptionData
    * SilenceData
    * HoldData
    * EntityMentionData
      * JSON representation
    * MentionType
    * IntentMatchData
      * JSON representation
    * PhraseMatchData
      * JSON representation
    * IssueMatchData
      * JSON representation
    * IssueAssignment
      * JSON representation
    * Entity
      * JSON representation
    * Type
    * ConversationLevelSentiment
      * JSON representation
    * ConversationLevelSilence
      * JSON representation
    * Intent
      * JSON representation
    * IssueModelResult
      * JSON representation
    * QaScorecardResult
      * JSON representation
    * QaAnswer
      * JSON representation
    * AnswerSource
      * JSON representation
    * SourceType
    * QaTagResult
      * JSON representation
    * ScoreSource
      * JSON representation
    * SourceType
  * Methods



## Resource: Analysis

The analysis resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "requestTime": string,
      "createTime": string,
      "analysisResult": {
        object ([AnalysisResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.AnalysisResult))
      },
      "annotatorSelector": {
        object ([AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotatorSelector))
      }
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis}  
`requestTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the analysis was requested.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the analysis was created, which occurs when the long-running operation completes.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`analysisResult` |  `object (`[AnalysisResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.AnalysisResult)`)` Output only. The result of the analysis, which is populated when the analysis finishes.  
`annotatorSelector` |  `object (`[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotatorSelector)`)` To select the annotators to run and the phrase matchers to use (if any). If not specified, all annotators will be run.  
  
### AnalysisResult

The result of an analysis.

JSON representation  
---  
      
    
    {
      "endTime": string,
    
      // Union field metadata can be only one of the following:
      "callAnalysisMetadata": {
        object ([CallAnalysisMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.CallAnalysisMetadata))
      }
      // End of list of possible types for union field metadata.
    }  
  
Fields  
---  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the analysis ended.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `metadata`. Metadata discovered during analysis. `metadata` can be only one of the following:  
`callAnalysisMetadata` |  `object (`[CallAnalysisMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.CallAnalysisMetadata)`)` Call-specific metadata created by the analysis.  
  
### CallAnalysisMetadata

Call-specific metadata created during analysis.

JSON representation  
---  
      
    
    {
      "annotations": [
        {
          object ([CallAnnotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.CallAnnotation))
        }
      ],
      "entities": {
        string: {
          object ([Entity](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.Entity))
        },
        ...
      },
      "sentiments": [
        {
          object ([ConversationLevelSentiment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.ConversationLevelSentiment))
        }
      ],
      "silence": {
        object ([ConversationLevelSilence](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.ConversationLevelSilence))
      },
      "intents": {
        string: {
          object ([Intent](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.Intent))
        },
        ...
      },
      "phraseMatchers": {
        string: {
          object ([PhraseMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.PhraseMatchData))
        },
        ...
      },
      "issueModelResult": {
        object ([IssueModelResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IssueModelResult))
      },
      "qaScorecardResults": [
        {
          object ([QaScorecardResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaScorecardResult))
        }
      ]
    }  
  
Fields  
---  
`annotations[]` |  `object (`[CallAnnotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.CallAnnotation)`)` A list of call annotations that apply to this call.  
`entities` |  `map (key: string, value: object (`[Entity](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.Entity)`))` All the entities in the call.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`sentiments[]` |  `object (`[ConversationLevelSentiment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.ConversationLevelSentiment)`)` Overall conversation-level sentiment for each channel of the call.  
`silence` |  `object (`[ConversationLevelSilence](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.ConversationLevelSilence)`)` Overall conversation-level silence during the call.  
`intents` |  `map (key: string, value: object (`[Intent](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.Intent)`))` All the matched intents in the call.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`phraseMatchers` |  `map (key: string, value: object (`[PhraseMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.PhraseMatchData)`))` All the matched phrase matchers in the call.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`issueModelResult` |  `object (`[IssueModelResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IssueModelResult)`)` Overall conversation-level issue modeling result.  
`qaScorecardResults[]` |  `object (`[QaScorecardResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaScorecardResult)`)` Results of scoring QaScorecards.  
  
### CallAnnotation

A piece of metadata that applies to a window of a call.

JSON representation  
---  
      
    
    {
      "channelTag": integer,
      "annotationStartBoundary": {
        object ([AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotationBoundary))
      },
      "annotationEndBoundary": {
        object ([AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotationBoundary))
      },
    
      // Union field data can be only one of the following:
      "interruptionData": {
        object ([InterruptionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.InterruptionData))
      },
      "sentimentData": {
        object ([SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData))
      },
      "silenceData": {
        object ([SilenceData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.SilenceData))
      },
      "holdData": {
        object ([HoldData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.HoldData))
      },
      "entityMentionData": {
        object ([EntityMentionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.EntityMentionData))
      },
      "intentMatchData": {
        object ([IntentMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IntentMatchData))
      },
      "phraseMatchData": {
        object ([PhraseMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.PhraseMatchData))
      },
      "issueMatchData": {
        object ([IssueMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IssueMatchData))
      }
      // End of list of possible types for union field data.
    }  
  
Fields  
---  
`channelTag` |  `integer` The channel of the audio where the annotation occurs. For single-channel audio, this field is not populated.  
`annotationStartBoundary` |  `object (`[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotationBoundary)`)` The boundary in the conversation where the annotation starts, inclusive.  
`annotationEndBoundary` |  `object (`[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotationBoundary)`)` The boundary in the conversation where the annotation ends, inclusive.  
Union field `data`. The data in the annotation. `data` can be only one of the following:  
`interruptionData` |  `object (`[InterruptionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.InterruptionData)`)` Data specifying an interruption.  
`sentimentData` |  `object (`[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData)`)` Data specifying sentiment.  
`silenceData` |  `object (`[SilenceData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.SilenceData)`)` Data specifying silence.  
`holdData` |  `object (`[HoldData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.HoldData)`)` Data specifying a hold.  
`entityMentionData` |  `object (`[EntityMentionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.EntityMentionData)`)` Data specifying an entity mention.  
`intentMatchData` |  `object (`[IntentMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IntentMatchData)`)` Data specifying an intent match.  
`phraseMatchData` |  `object (`[PhraseMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.PhraseMatchData)`)` Data specifying a phrase match.  
`issueMatchData` |  `object (`[IssueMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IssueMatchData)`)` Data specifying an issue match.  
  
### InterruptionData

This type has no fields.

The data for an interruption annotation.

### SilenceData

This type has no fields.

The data for a silence annotation.

### HoldData

This type has no fields.

The data for a hold annotation.

### EntityMentionData

The data for an entity mention annotation. This represents a mention of an `Entity` in the conversation.

JSON representation  
---  
      
    
    {
      "entityUniqueId": string,
      "type": enum ([MentionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.MentionType)),
      "sentiment": {
        object ([SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData))
      }
    }  
  
Fields  
---  
`entityUniqueId` |  `string` The key of this entity in conversation entities. Can be used to retrieve the exact `Entity` this mention is attached to.  
`type` |  `enum (`[MentionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.MentionType)`)` The type of the entity mention.  
`sentiment` |  `object (`[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData)`)` Sentiment expressed for this mention of the entity.  
  
### MentionType

The supported types of mentions.

Enums  
---  
`MENTION_TYPE_UNSPECIFIED` | Unspecified.  
`PROPER` | Proper noun.  
`COMMON` | Common noun (or noun compound).  
  
### IntentMatchData

The data for an intent match. Represents an intent match for a text segment in the conversation. A text segment can be part of a sentence, a complete sentence, or an utterance with multiple sentences.

JSON representation  
---  
      
    
    {
      "intentUniqueId": string
    }  
  
Fields  
---  
`intentUniqueId` |  `string` The id of the matched intent. Can be used to retrieve the corresponding intent information.  
  
### PhraseMatchData

The data for a matched phrase matcher. Represents information identifying a phrase matcher for a given match.

JSON representation  
---  
      
    
    {
      "phraseMatcher": string,
      "displayName": string
    }  
  
Fields  
---  
`phraseMatcher` |  `string` The unique identifier (the resource name) of the phrase matcher.  
`displayName` |  `string` The human-readable name of the phrase matcher.  
  
### IssueMatchData

The data for an issue match annotation.

JSON representation  
---  
      
    
    {
      "issueAssignment": {
        object ([IssueAssignment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IssueAssignment))
      }
    }  
  
Fields  
---  
`issueAssignment` |  `object (`[IssueAssignment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IssueAssignment)`)` Information about the issue's assignment.  
  
### IssueAssignment

Information about the issue.

JSON representation  
---  
      
    
    {
      "issue": string,
      "score": number,
      "displayName": string
    }  
  
Fields  
---  
`issue` |  `string` Resource name of the assigned issue.  
`score` |  `number` Score indicating the likelihood of the issue assignment. currently bounded on [0,1].  
`displayName` |  `string` Immutable. Display name of the assigned issue. This field is set at time of analysis and immutable since then.  
  
### Entity

The data for an entity annotation. Represents a phrase in the conversation that is a known entity, such as a person, an organization, or location.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.Type)),
      "metadata": {
        string: string,
        ...
      },
      "salience": number,
      "sentiment": {
        object ([SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData))
      }
    }  
  
Fields  
---  
`displayName` |  `string` The representative name for the entity.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.Type)`)` The entity type.  
`metadata` |  `map (key: string, value: string)` Metadata associated with the entity.For most entity types, the metadata is a Wikipedia URL (`wikipedia_url`) and Knowledge Graph MID (`mid`), if they are available. For the metadata associated with other entity types, see the Type table below.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`salience` |  `number` The salience score associated with the entity in the [0, 1.0] range.The salience score for an entity provides information about the importance or centrality of that entity to the entire document text. Scores closer to 0 are less salient, while scores closer to 1.0 are highly salient.  
`sentiment` |  `object (`[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData)`)` The aggregate sentiment expressed for this entity in the conversation.  
  
### Type

The type of the entity. For most entity types, the associated metadata is a Wikipedia URL (`wikipedia_url`) and Knowledge Graph MID (`mid`). The table below lists the associated fields for entities that have different metadata.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified.  
`PERSON` | Person.  
`LOCATION` | Location.  
`ORGANIZATION` | Organization.  
`EVENT` | Event.  
`WORK_OF_ART` | Artwork.  
`CONSUMER_GOOD` | Consumer product.  
`OTHER` | Other types of entities.  
`PHONE_NUMBER` | Phone number.The metadata lists the phone number (formatted according to local convention), plus whichever additional elements appear in the text:

  * `number` \- The actual number, broken down into sections according to local convention.
  * `national_prefix` \- Country code, if detected.
  * `area_code` \- Region or area code, if detected.
  * `extension` \- Phone extension (to be dialed after connection), if detected.

  
`ADDRESS` | Address.The metadata identifies the street number and locality plus whichever additional elements appear in the text:

  * `street_number` \- Street number.
  * `locality` \- City or town.
  * `street_name` \- Street/route name, if detected.
  * `postal_code` \- Postal code, if detected.
  * `country` \- Country, if detected.
  * `broad_region` \- Administrative area, such as the state, if detected.
  * `narrow_region` \- Smaller administrative area, such as county, if detected.
  * `sublocality` \- Used in Asian addresses to demark a district within a city, if detected.

  
`DATE` | Date.The metadata identifies the components of the date:

  * `year` \- Four digit year, if detected.
  * `month` \- Two digit month number, if detected.
  * `day` \- Two digit day number, if detected.

  
`NUMBER` | Number.The metadata is the number itself.  
`PRICE` | Price.The metadata identifies the `value` and `currency`.  
  
### ConversationLevelSentiment

One channel of conversation-level sentiment data.

JSON representation  
---  
      
    
    {
      "channelTag": integer,
      "sentimentData": {
        object ([SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData))
      }
    }  
  
Fields  
---  
`channelTag` |  `integer` The channel of the audio that the data applies to.  
`sentimentData` |  `object (`[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData)`)` Data specifying sentiment.  
  
### ConversationLevelSilence

Conversation-level silence data.

JSON representation  
---  
      
    
    {
      "silenceDuration": string,
      "silencePercentage": number
    }  
  
Fields  
---  
`silenceDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Amount of time calculated to be in silence.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`silencePercentage` |  `number` Percentage of the total conversation spent in silence.  
  
### Intent

The data for an intent. Represents a detected intent in the conversation, for example MAKES_PROMISE.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string
    }  
  
Fields  
---  
`id` |  `string` The unique identifier of the intent.  
`displayName` |  `string` The human-readable name of the intent.  
  
### IssueModelResult

Issue Modeling result on a conversation.

JSON representation  
---  
      
    
    {
      "issueModel": string,
      "issues": [
        {
          object ([IssueAssignment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IssueAssignment))
        }
      ]
    }  
  
Fields  
---  
`issueModel` |  `string` Issue model that generates the result. Format: projects/{project}/locations/{location}/issueModels/{issueModel}  
`issues[]` |  `object (`[IssueAssignment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.IssueAssignment)`)` All the matched issues.  
  
### QaScorecardResult

The results of scoring a single conversation against a QaScorecard. Contains a collection of QaAnswers and aggregate score.

JSON representation  
---  
      
    
    {
      "name": string,
      "qaScorecardRevision": string,
      "conversation": string,
      "createTime": string,
      "agentId": string,
      "qaAnswers": [
        {
          object ([QaAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaAnswer))
        }
      ],
      "qaTagResults": [
        {
          object ([QaTagResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaTagResult))
        }
      ],
      "scoreSources": [
        {
          object ([ScoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.ScoreSource))
        }
      ],
      "score": number,
      "potentialScore": number,
      "normalizedScore": number
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the scorecard result. Format: projects/{project}/locations/{location}/qaScorecardResults/{qa_scorecard_result}  
`qaScorecardRevision` |  `string` The QaScorecardRevision scored by this result.  
`conversation` |  `string` The conversation scored by this result.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp that the revision was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`agentId` |  `string` ID of the agent that handled the conversation.  
`qaAnswers[]` |  `object (`[QaAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaAnswer)`)` Set of QaAnswers represented in the result.  
`qaTagResults[]` |  `object (`[QaTagResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaTagResult)`)` Collection of tags and their scores.  
`scoreSources[]` |  `object (`[ScoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.ScoreSource)`)` List of all individual score sets.  
`score` |  `number` The overall numerical score of the result, incorporating any manual edits if they exist.  
`potentialScore` |  `number` The maximum potential overall score of the scorecard. Any questions answered using `naValue` are excluded from this calculation.  
`normalizedScore` |  `number` The normalized score, which is the score divided by the potential score. Any manual edits are included if they exist.  
  
### QaAnswer

An answer to a QaQuestion.

JSON representation  
---  
      
    
    {
      "qaQuestion": string,
      "conversation": string,
      "questionBody": string,
      "answerValue": {
        object ([AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnswerValue))
      },
      "tags": [
        string
      ],
      "answerSources": [
        {
          object ([AnswerSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.AnswerSource))
        }
      ]
    }  
  
Fields  
---  
`qaQuestion` |  `string` The QaQuestion answered by this answer.  
`conversation` |  `string` The conversation the answer applies to.  
`questionBody` |  `string` Question text. E.g., "Did the agent greet the customer?"  
`answerValue` |  `object (`[AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnswerValue)`)` The main answer value, incorporating any manual edits if they exist.  
`tags[]` |  `string` User-defined list of arbitrary tags. Matches the value from QaScorecard.ScorecardQuestion.tags. Used for grouping/organization and for weighting the score of each answer.  
`answerSources[]` |  `object (`[AnswerSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.AnswerSource)`)` List of all individual answers given to the question.  
  
### AnswerSource

A question may have multiple answers from varying sources, one of which becomes the "main" answer above. AnswerSource represents each individual answer.

JSON representation  
---  
      
    
    {
      "sourceType": enum ([SourceType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.SourceType)),
      "answerValue": {
        object ([AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnswerValue))
      }
    }  
  
Fields  
---  
`sourceType` |  `enum (`[SourceType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.SourceType)`)` What created the answer.  
`answerValue` |  `object (`[AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnswerValue)`)` The answer value from this source.  
  
### SourceType

What created the answer.

Enums  
---  
`SOURCE_TYPE_UNSPECIFIED` | Source type is unspecified.  
`SYSTEM_GENERATED` | Answer was system-generated; created during an Insights analysis.  
`MANUAL_EDIT` | Answer was created by a human via manual edit.  
  
### QaTagResult

Tags and their corresponding results.

JSON representation  
---  
      
    
    {
      "tag": string,
      "score": number,
      "potentialScore": number,
      "normalizedScore": number
    }  
  
Fields  
---  
`tag` |  `string` The tag the score applies to.  
`score` |  `number` The score the tag applies to.  
`potentialScore` |  `number` The potential score the tag applies to.  
`normalizedScore` |  `number` The normalized score the tag applies to.  
  
### ScoreSource

A scorecard result may have multiple sets of scores from varying sources, one of which becomes the "main" answer above. A ScoreSource represents each individual set of scores.

JSON representation  
---  
      
    
    {
      "sourceType": enum ([SourceType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.SourceType_1)),
      "qaTagResults": [
        {
          object ([QaTagResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaTagResult))
        }
      ],
      "score": number,
      "potentialScore": number,
      "normalizedScore": number
    }  
  
Fields  
---  
`sourceType` |  `enum (`[SourceType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.SourceType_1)`)` What created the score.  
`qaTagResults[]` |  `object (`[QaTagResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaTagResult)`)` Collection of tags and their scores.  
`score` |  `number` The overall numerical score of the result.  
`potentialScore` |  `number` The maximum potential overall score of the scorecard. Any questions answered using `naValue` are excluded from this calculation.  
`normalizedScore` |  `number` The normalized score, which is the score divided by the potential score.  
  
### SourceType

What created the score.

Enums  
---  
`SOURCE_TYPE_UNSPECIFIED` | Source type is unspecified.  
`SYSTEM_GENERATED_ONLY` | Score is derived only from system-generated answers.  
`INCLUDES_MANUAL_EDITS` | Score is derived from both system-generated answers, and includes any manual edits if they exist.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/create)`

|  Creates an analysis.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/delete)`

|  Deletes an analysis.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/get)`

|  Gets an analysis.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/list)`

|  Lists analyses.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
