---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback/
title: Method: projects.locations.agents.sessions.submitAnswerFeedback \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:18.277559+00:00
---

# Method: projects.locations.agents.sessions.submitAnswerFeedback  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.sessions.submitAnswerFeedback Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Rating
  * RatingReason
    * JSON representation
  * Try it!



Updates the feedback received from the user for a single turn of the bot response.

### HTTP request

`POST https://{endpoint}/v3/{session=projects/*/locations/*/agents/*/sessions/*}:submitAnswerFeedback`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The name of the session the feedback was sent to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `dialogflow.sessions.detectIntent`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "responseId": string,
      "answerFeedback": {
        object ([AnswerFeedback](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback#body.AnswerFeedback))
      },
      "updateMask": string
    }  
  
Fields  
---  
`responseId` |  `string` Required. ID of the response to update its feedback. This is the same as DetectIntentResponse.response_id.  
`answerFeedback` |  `object (`[AnswerFeedback](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback#body.AnswerFeedback)`)` Required. Feedback provided for a bot answer.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The mask to control which fields to update. If the mask is not present, all fields will be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

Stores information about feedback provided by users about a response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rating": enum ([Rating](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback#Rating)),
      "ratingReason": {
        object ([RatingReason](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback#RatingReason))
      },
      "customRating": string
    }  
  
Fields  
---  
`rating` |  `enum (`[Rating](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback#Rating)`)` Optional. Rating from user for the specific Dialogflow response.  
`ratingReason` |  `object (`[RatingReason](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback#RatingReason)`)` Optional. In case of thumbs down rating provided, users can optionally provide context about the rating.  
`customRating` |  `string` Optional. Custom rating from the user about the provided answer, with maximum length of 1024 characters. For example, client could use a customized JSON object to indicate the rating.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Rating

Represents thumbs up/down rating provided by user about a response.

Enums  
---  
`RATING_UNSPECIFIED` | Rating not specified.  
`THUMBS_UP` | Thumbs up feedback from user.  
`THUMBS_DOWN` | Thumbs down feedback from user.  
  
## RatingReason

Stores extra information about why users provided thumbs down rating.

JSON representation  
---  
      
    
    {
      "reasonLabels": [
        string
      ],
      "feedback": string
    }  
  
Fields  
---  
`reasonLabels[]` |  `string` Optional. Custom reason labels for thumbs down rating provided by the user. The maximum number of labels allowed is 10 and the maximum length of a single label is 128 characters.  
`feedback` |  `string` Optional. Additional feedback about the rating. This field can be populated without choosing a predefined `reason`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
