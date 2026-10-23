---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/sentiment-analysis/
title: Sentiment analysis \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:38.048052+00:00
---

# Sentiment analysis  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/sentiment-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Sentiment analysis Stay organized with collections  Save and categorize content based on your preferences. 

The sentiment analysis feature analyzes messages during a conversation between a human agent and an end user to determine emotional intent. Customer Experience Insights only measures the sentiments of end users in contact center conversations. Sentiment is represented by a numerical score and a corresponding text label. The score lies in the range (-1, 1), neither values included.

## Turn-level sentiment

Customer Experience Insights calculates the sentiment scores for individual user turns within a conversation as follows:

Score | Magnitude | Fine-grained sentiment | Sentiment  
---|---|---|---  
-1 | 1.0 | `negative` | Negative  
-0.5 | 0.5 | `somewhat_negative` | Negative  
-0.25 | 0.75 | `mixed_more_negative` | Negative  
0 | 0 | `neutral` | Neutral  
0 | 0.75 | `mixed_balanced` | Neutral  
0.25 | 0.75 | `mixed_more_positive` | Positive  
0.5 | 0.5 | `somewhat_positive` | Positive  
1 | 1.0 | `positive` | Positive  
  
### View turn-level sentiments scores

View the sentiment scores for each turn within a specific conversation as follows:

### Conversation Hub

  1. Go to the Customer Experience Insights console, and choose your project.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Click **Conversation Hub**.

  3. Select a conversation. If you have not yet analyzed the conversation, click **Analyze**.

  4. Navigate to the **Conversation spotlight** section.




The two playback bars indicate when each participant speaks throughout the conversation. Customer Experience Insights highlights the top positive and negative sentiment moments. Positive sentiments are blue and negative sentiments are red.

### Quality AI

  1. Go to the Customer Experience Insights console, and choose your project.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Click **Quality AI** > **Conversations**.

  3. Select a conversation. If you have not yet analyzed the conversation, click **Analyze**.

  4. Navigate to the **Conversation spotlight** section.




The two playback bars indicate when each participant speaks throughout the conversation. Customer Experience Insights highlights the top positive and negative sentiment moments. Positive sentiments are blue and negative sentiments are red.

## Conversation-level sentiment

Customer Experience Insights calculates the sentiment scores over entire conversations as follows:

  * **Positive** : Greater than or equal to 0.5
  * **Neutral** : Between -0.5 and 0.5
  * **Negative** : Less than or equal to -0.5

**Note:** When viewing a conversation, click the **Information** tab to view the rationale for the overall sentiment of the conversation.

### View conversation-level sentiment scores

For each agent in your contact center, you can view the sentiment score for each of their conversations or the average sentiment score over all their conversations.

You can also view sentiment scores for individual conversations from your full contact center conversation list.

### For each agent

Follow these steps to view the sentiment scores for each conversation that a single agent handled.

  1. Within the [Customer Experience Insights console](https://ccai.cloud.google.com/insights/projects), choose your project and click **Quality AI** > **Agents**.
  2. Choose an option:
     * In the last column, view an agent's **Sentiment Score**.
     * Click an agent's name and view the overall **Sentiment** of that agent's conversations in the last column.



### For individual conversations

Follow these steps to view the sentiment score for each individual contact center conversation.

  1. Within the [Customer Experience Insights console](https://ccai.cloud.google.com/insights/projects), choose your project and click **Quality AI** > **Conversations**.
  2. Select a conversation then navigate to **Information**.



## What's next

  * For more details on interpreting sentiment analysis results, see the [Natural Language sentiment analysis documentation](https://docs.cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values).
  * For examples, see the [Agent Assist sentiment analysis documentation](https://docs.cloud.google.com/agent-assist/docs/sentiment-analysis#interpret_sentiment_analysis_results).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
