---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions
title: REST Resource: projects.locations.qaScorecards.revisions.qaQuestions \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:46:19.916383+00:00
---

# REST Resource: projects.locations.qaScorecards.revisions.qaQuestions  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.qaScorecards.revisions.qaQuestions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: QaQuestion
    * JSON representation
  * QaQuestionType
  * PredefinedQuestionConfig
    * JSON representation
  * PredefinedQuestionType
  * AnswerChoice
    * JSON representation
  * Metrics
    * JSON representation
  * TuningMetadata
    * JSON representation
  * DatasetValidationWarning
  * Methods



## Resource: QaQuestion

A single question to be scored by the Insights QA feature.

JSON representation  
---  
      
    
    {
      "name": string,
      "abbreviation": string,
      "createTime": string,
      "updateTime": string,
      "questionType": enum ([QaQuestionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#QaQuestionType)),
      "predefinedQuestionConfig": {
        object ([PredefinedQuestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#PredefinedQuestionConfig))
      },
      "questionBody": string,
      "answerInstructions": string,
      "answerChoices": [
        {
          object ([AnswerChoice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#AnswerChoice))
        }
      ],
      "tags": [
        string
      ],
      "order": integer,
      "metrics": {
        object ([Metrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#Metrics))
      },
      "tuningMetadata": {
        object ([TuningMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#TuningMetadata))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the question. Format: projects/{project}/locations/{location}/qaScorecards/{qaScorecard}/revisions/{revision}/qaQuestions/{qaQuestion}  
`abbreviation` |  `string` Short, descriptive string, used in the UI where it's not practical to display the full question body. E.g., "Greeting".  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this question was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time at which the question was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`questionType` |  `enum (`[QaQuestionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#QaQuestionType)`)` The type of question.  
`predefinedQuestionConfig` |  `object (`[PredefinedQuestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#PredefinedQuestionConfig)`)` The configuration of the predefined question. This field will only be set if the Question Type is predefined.  
`questionBody` |  `string` Question text. E.g., "Did the agent greet the customer?"  
`answerInstructions` |  `string` Instructions describing how to determine the answer.  
`answerChoices[]` |  `object (`[AnswerChoice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#AnswerChoice)`)` A list of valid answers to the question, which the LLM must choose from.  
`tags[]` |  `string` Questions are tagged for categorization and scoring. Tags can either be: - Default Tags: These are predefined categories. They are identified by their string value (e.g., "BUSINESS", "COMPLIANCE", and "CUSTOMER"). - Custom Tags: These are user-defined categories. They are identified by their full resource name (e.g., projects/{project}/locations/{location}/qaQuestionTags/{qaQuestionTag}). Both default and custom tags are used to group questions and to influence the scoring of each question.  
`order` |  `integer` Defines the order of the question within its parent scorecard revision.  
`metrics` |  `object (`[Metrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#Metrics)`)` Metrics of the underlying tuned LLM over a holdout/test set while fine tuning the underlying LLM for the given question. This field will only be populated if and only if the question is part of a scorecard revision that has been tuned.  
`tuningMetadata` |  `object (`[TuningMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#TuningMetadata)`)` Metadata about the tuning operation for the question.This field will only be populated if and only if the question is part of a scorecard revision that has been tuned.  
  
## QaQuestionType

Enum representing the type of the question.

Enums  
---  
`QA_QUESTION_TYPE_UNSPECIFIED` | The type of the question is unspecified.  
`CUSTOMIZABLE` | The default question type. The question is fully customizable by the user.  
`PREDEFINED` | The question type is using a predefined model provided by CCAI teams. Users are not allowed to edit the questionBody, answerChoices, upload feedback labels for the question nor fine-tune the question. However, users may edit other fields like question tags, question order, etc.  
  
## PredefinedQuestionConfig

Configuration for a predefined question. This field will only be set if the Question Type is predefined.

JSON representation  
---  
      
    
    {
      "type": enum ([PredefinedQuestionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#PredefinedQuestionType))
    }  
  
Fields  
---  
`type` |  `enum (`[PredefinedQuestionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#PredefinedQuestionType)`)` The type of the predefined question.  
  
## PredefinedQuestionType

Enum representing the type of the predefined question.

Enums  
---  
`PREDEFINED_QUESTION_TYPE_UNSPECIFIED` | The type of the predefined question is unspecified.  
`CONVERSATION_OUTCOME` | A prebuilt classifier classfying the outcome of the conversation. For example, if the customer issue mentioned in a conversation has been resolved or not.  
`CONVERSATION_OUTCOME_ESCALATION_INITIATOR_ROLE` | A prebuilt classifier classfying the initiator of the conversation escalation. For example, if it was initiated by the customer or the agent.  
  
## AnswerChoice

Message representing a possible answer to the question.

JSON representation  
---  
      
    
    {
      "key": string,
    
      // Union field value can be only one of the following:
      "strValue": string,
      "numValue": number,
      "boolValue": boolean,
      "naValue": boolean
      // End of list of possible types for union field value.
      "score": number
    }  
  
Fields  
---  
`key` |  `string` A short string used as an identifier.  
Union field `value`. The answer value may be one of a few different types. `value` can be only one of the following:  
`strValue` |  `string` String value.  
`numValue` |  `number` Numerical value.  
`boolValue` |  `boolean` Boolean value.  
`naValue` |  `boolean` A value of "Not Applicable (N/A)". If provided, this field may only be set to `true`. If a question receives this answer, it will be excluded from any score calculations.  
`score` |  `number` Numerical score of the answer, used for generating the overall score of a QaScorecardResult. If the answer uses naValue, this field is unused.  
  
## Metrics

A wrapper representing metrics calculated against a test-set on a LLM that was fine tuned for this question.

JSON representation  
---  
      
    
    {
      "accuracy": number
    }  
  
Fields  
---  
`accuracy` |  `number` Output only. Accuracy of the model. Measures the percentage of correct answers the model gave on the test set.  
  
## TuningMetadata

Metadata about the tuning operation for the question. Will only be set if a scorecard containing this question has been tuned.

JSON representation  
---  
      
    
    {
      "totalValidLabelCount": string,
      "datasetValidationWarnings": [
        enum ([DatasetValidationWarning](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#DatasetValidationWarning))
      ],
      "tuningError": string
    }  
  
Fields  
---  
`totalValidLabelCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of valid labels provided for the question at the time of tuining.  
`datasetValidationWarnings[]` |  `enum (`[DatasetValidationWarning](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions#DatasetValidationWarning)`)` A list of any applicable data validation warnings about the question's feedback labels.  
`tuningError` |  `string` Error status of the tuning operation for the question. Will only be set if the tuning operation failed.  
  
## DatasetValidationWarning

Enum for the different types of issues a tuning dataset can have. These warnings are currentlyraised when trying to validate a dataset for tuning a scorecard.

Enums  
---  
`DATASET_VALIDATION_WARNING_UNSPECIFIED` | Unspecified data validation warning.  
`TOO_MANY_INVALID_FEEDBACK_LABELS` | A non-trivial percentage of the feedback labels are invalid.  
`INSUFFICIENT_FEEDBACK_LABELS` | The quantity of valid feedback labels provided is less than the recommended minimum.  
`INSUFFICIENT_FEEDBACK_LABELS_PER_ANSWER` | One or more of the answers have less than the recommended minimum of feedback labels.  
`ALL_FEEDBACK_LABELS_HAVE_THE_SAME_ANSWER` | All the labels in the dataset come from a single answer choice.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/create)`

|  Create a QaQuestion.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/delete)`

|  Deletes a QaQuestion.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/get)`

|  Gets a QaQuestion.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/list)`

|  Lists QaQuestions.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/patch)`

|  Updates a QaQuestion.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
