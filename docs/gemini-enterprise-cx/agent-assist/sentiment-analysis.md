---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sentiment-analysis/
title: Analyze message sentiment \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:51.719267+00:00
---

# Analyze message sentiment  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sentiment-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Analyze message sentiment Stay organized with collections  Save and categorize content based on your preferences. 

Sentiment analysis analyzes messages during a conversation between a human agent and an end user to determine the end user's emotional intent. It analyzes individual messages with the conversation context and can even analyze an audio stream to provide precise end user sentiment scores.

## Enable sentiment analysis

You can enable sentiment analysis during conversation profile creation or editing. If you edit an existing conversation profile, you only see the effects in conversations after the conversation profile updates. You can also enable sentiment analysis when you [create a conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) using the Agent Assist console.

Follow these steps to enable sentiment analysis and view the results.

  1. Set `enableSentimentAnalysisV3` to `true` in [`MessageAnalysisConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#messageanalysisconfig).
  2. Send a [`createConversation`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/create) request using a [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) with this feature enabled.
  3. View sentiment results in [`AnalyzeContentResponse.message.sentimentAnalysis`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Message).
  4. If you enabled [Pub/Sub](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pub-sub) integration in Agent Assist, you can also view sentiment results in the `NewMessagePayload`.



## Interpret sentiment analysis results

Sentiment is represented by `score` and `magnitude` values, metrics that are returned in the response. The `score` of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and corresponds to the overall emotional leaning of the text or audio. The `magnitude` value indicates the overall strength of emotion (both positive and negative) within the given text or audio and ranges between `0.0` and `1.0`. For more information about interpreting these metrics, see the [Natural language sentiment analysis documentation](https://docs.cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values).

The following are two examples of sentiment analysis output from the [Natural Language API demo feature](https://cloud.google.com/natural-language). Follow these steps to use the demo to test sentiment analysis on sample text.

  1. Paste sample text into the field.
  2. Click **Analyze** > **Sentiment**.



### Example 1

Text: _I'm not happy._

The returned `score` is -0.9, and the `magnitude` is 0.9. This indicates a very strong negative emotional leaning, with low-to-moderate strength of emotion.

### Example 2

Text: _Google Cloud is the cloud service from Google._

The returned values of both `score` and `magnitude` is 0, which means that the text does not show any emotion or strength of feelings.

### Example 3

Text: _I'm extremely angry and disappointed for the result. On the other hand, I'm happy to see our team was working very hard and show professional attitude._

Unlike Example 1, this text contains two sentences. The output includes metrics for the entire document as well as metrics for each individual sentence. Entire document values represent the metrics of both sentences combined, not one or the other. Each individual sentence is also listed with its corresponding `magnitude` and `score` value.

The returned sentiment `score` for the entire document is 0, while the `magnitude` is 1.0. A `score` of 0 in a multi-sentence document can mean that it's truly emotionally neutral, or that positive and negative emotional leanings at various points in the text canceled each other out. Text with a truly neutral sentiment will also have a `magnitude` equal to or close to 0. In this case, the relatively high `magnitude` of 1.0 means that the sentiment of the two sentences is not truly neutral, but mixed (for example angry, disappointed and happy at various points in the text). Looking at the `score` values for each sentence, one is strongly positive (0.8) and the other is strongly negative (-0.8), which made the entire document `score` average to 0.

## Legacy model

You might still be using the legacy version of Agent Assist's sentiment analysis. The legacy version differs in the following ways:

  * Set `enableSentimentAnalysis` to `true` in `MessageAnalysisConfig` to enable sentiment analysis.
  * Analyze sentiment for both human agents and end users.
  * Use only the conversation transcript from audio files for analysis.
  * See `Magnitude` scores that range from 0.0 to +inf.

**Note:** Agent Assist manages `AnalyzeSentiment` quotas on a per-version basis. A quota increase for one version doesn't transfer to another version. If you switch versions, you must request a new quota increase.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
