---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pubsub-notifications/
title: Skip Pub/Sub notifications for empty suggestions \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:45.866459+00:00
---

# Skip Pub/Sub notifications for empty suggestions  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pubsub-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Skip Pub/Sub notifications for empty suggestions Stay organized with collections  Save and categorize content based on your preferences. 

By default, event-based suggestion features like [proactive generative knowledge assist (PGKA)](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka) send a [Pub/Sub notification](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka#pubsub-suggestion-notifications) for every suggestion attempt. This means Agent Assist sends a notification even when the feature determines there is no relevant suggestion to provide, resulting in an empty response. This can create unnecessary Pub/Sub traffic and processing overhead. You can suppress empty notifications with a single code field: `skip_empty_event_based_suggestion`.

## Basics

The `skip_empty_event_based_suggestion` field is part of `SuggestionConfig` within `HumanAgentAssistantConfig` of your conversation profile. When you set its value to `true`, Agent Assist only sends a Pub/Sub notification when it generates a valid suggestion that isn't empty.

The `skip_empty_event_based_suggestion` field is designed for features that generate suggestions asynchronously with event based triggers and delivers them through Pub/Sub. Features that don't rely on Pub/Sub for suggestion delivery, or are not event based, are not affected.

The `skip_empty_event_based_suggestion` field has the following two possible values.

  * **False** : Agent Assist sends a Pub/Sub notification for every suggestion attempt. If Agent Assist doesn't find a suggestion for an event, you still receive a notification indicating an empty result.
  * **True** : Agent Assist sends a Pub/Sub notification only if the suggestion result is valid and not empty. If Agent Assist doesn't find a suggestion, it doesn't publish a Pub/Sub message for that event, reducing noise in your notification topic.



## Configuration

To suppress empty notifications, update your conversation profile and set `skip_empty_event_based_suggestion` to `true` as follows.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/conversationProfiles/PROFILE_ID",
      "human_agent_assistant_config": {
        "human_agent_suggestion_config": {
          "feature_configs": [
            {
              "suggestion_feature": {
                "type": "KNOWLEDGE_ASSIST"
              },
              "enable_event_based_suggestion": true
            },
          ],
          "skip_empty_event_based_suggestion": true
        }
      }
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
