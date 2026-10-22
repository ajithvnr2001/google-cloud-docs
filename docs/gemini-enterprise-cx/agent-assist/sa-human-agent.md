---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sa-human-agent/
title: User guide: Supervisor assist for human agents \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:19.614425+00:00
---

# User guide: Supervisor assist for human agents  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sa-human-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  User guide: Supervisor assist for human agents Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature has limited access. Contact your Google Cloud representative to access private GA features.

With supervisor assist for human agents human supervisors can monitor conversations between end users and human agents. You define rules for when to escalate a conversation to a human supervisor. Then, supervisor assist automatically alerts the human supervisor when a conversation matches one of your rules.

For each end user turn in a conversation, you see sentiment scores and a transcript. Your rules can use either these sentiment scores or [AI coach](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ai-coach-overview) to determine when the human supervisor receives an alert.

**Note:** You can access this feature through a simulator in the Agent Assist console or the API and Pub/Sub payload.

## Before you begin

To use supervisor assist, you need an Agent Assist conversation profile and the following Identity and Access Management (IAM) roles.

  * `dialogflow.virtualAgentMonitoringSupervisor`
  * `dialogflow.processor`



## Step 1: Configure a conversation profile

A _conversation profile_ configures a set of parameters that control the suggestions made to an agent during a conversation. The following steps create a [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles) with a [`HumanAgentAssistantConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig) object. You can also perform these actions using the [Agent Assist console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) if you would prefer not to call the API directly.

### Create a conversation profile

To create a conversation profile, call the `create` method on the [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles) resource. Provide your knowledge base ID, document ID, project ID, and model ID. The response contains your new conversation profile ID.

The following is a JSON example: 
    
    
    {
      "displayName": "smart_compose_assist",
      "humanAgentAssistantConfig": {
        "humanAgentSuggestionConfig": {
          "featureConfigs": [
            {
              "suggestionFeature": {
                "type": "SMART_COMPOSE"
              },
              "queryConfig": {
                "documentQuerySource": {
                  "documents": "projects/project-id/knowledgeBases/knowledge-base-id/documents/document-id"
                },
               "maxResults": "1"
              },
             "conversationModelConfig": {
               "model": "projects/project-id/conversationModels/model-id"
             }
            }
          ]
        }
      }
    }
    

## Step 2: Choose sentiment or AI coach

Choose whether to use sentiment analysis, AI coach, or both to monitor conversations. Your escalation rules also reflect this choice.

### Sentiment

To analyze the end user's sentiment throughout a conversation, add sentiment analysis to your conversation profile.

### AI coach

To analyze conversations with AI coach, follow the instructions to [create an AI coach generator](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools#step_1_create_a_generator). You can only create one AI coach generator at a time for a single conversation profile. You can add an unlimited number of instructions to your AI coach generator, and each instruction must include at least a **Display title** and a **Condition**.

After your create a generator, copy your new generator ID and add it to your conversation profile.

## Step 3: Configure rules to monitor conversations

Update your conversation profile to enable and configure monitoring rules for your customer support conversations that use either sentiment or AI coach. Choose one of the following options to update your conversation profile with the API:

  * Call the `update` method on the `ConversationProfile` resource.
  * Set the interaction monitoring configuration with the [`UpdateConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#updateconversationprofilerequest) method. Your request to set the interaction monitoring configuration should look like the following example.
        
        conversation_profile {
          name: "projects/agent-assist-console-demo/locations/global/conversationProfiles/your_new_conv_profile_id"
          interaction_monitoring_config {
            event_notification_config = {
            notification_config = { # If you want to enable notifications on your custom pub/sub topic, add it here.
            topic = 'ADD_YOUR_CUSTOM_PUBSUB_TOPIC'
                message_format = 'JSON'
              }
          # Optional: Leave both empty for *Default Mode*.
          # Other supported configurations:
          # 1. **Default Mode:** Always publish alert events when they are triggered and publish metric events only when an alert is triggered,
          #   - Metric event: `METRIC_EVENT_PUBLISH_IF_ALERT_TRIGGERED`
          #   - Alert event: `ALERT_EVENT_ALWAYS_PUBLISH`
          # 2. **Pure Monitoring Mode:** Publish all metric events, but never publish alert events.
          #   - Metric event: `METRIC_EVENT_ALWAYS_PUBLISH`
          #   - Alert event: `ALERT_EVENT_NEVER_PUBLISH`
          # 3. **Publish All Events:** Always publish both metric and alert     events.
          #   - Metric event: `METRIC_EVENT_ALWAYS_PUBLISH`
          #   - Alert event: `ALERT_EVENT_ALWAYS_PUBLISH`
          # Note: Avoid setting `metric_event_notification_mode` to `METRIC_EVENT_PUBLISH_IF_ALERT_TRIGGERED` while `alert_event_notification_mode` is `ALERT_EVENT_NEVER_PUBLISH`, as this combination will result in no events being published.
        metric_event_notification_mode = 'ADD'
        alert_event_notification_mode = 'ADD'
            }
            alerting_config {
              # Required.
              rules {
                alert_rule_id: "rule_1"
                description: "rule_1_description"
                trigger_condition {
                ...
                }
          rules {
                alert_rule_id: "rule_2"
                description: "rule_2_description"
                trigger_condition {
                ...
                }
              }
              # Optional Tool config to retrieve customer name. If not    required, skip setting the metadata_config
              metadata_config = {
                tool_configs = [
            {
              display_name = 'Customer Name'
              toolset_tool = {
                toolset = 'ADD_CUSTOM_TOOLSET'
                operation_id = 'load_profile'
              }
              response_key_path = 'sessionInfo.customerProfile.customerName'
            },
                ]
              }
        
            }
          }
        }
        update_mask {
          paths: "interaction_monitoring_config"
        }
        }




Reach out to your Google Cloud representative for additional help.

### Example configurations

The following examples illustrate conversation profile configurations for a variety of monitoring rule combinations.

#### Example 1: AI coach rule matched
    
    
        conversation_profile     {
          name: "projects/agent-assist-console-demo/locations/global/conversationProfiles/your_new_conv_profile_id"
          interaction_monitoring_config {
            event_notification_config = {
                ...
            }
            alerting_config {
              rules {
                alert_rule_id: "agent coaching alert trigger rule(s) matched"
                description: "agent coaching alert trigger rule(s) matched"
                trigger_condition {
                  metric_condition {
                    metric_type: AGENT_COACHING_INSTRUCTIONS
                    agent_coaching_config {
                      generator_name:    "projects/agent-assist-console-demo/locations/global/generators/newly_created_generator_id"
                    }
                    display_name: "agent coaching alert trigger rule(s) matched"
                  }
                }
              }
              # Optional Tool config to retrieve customer name. If not required, skip setting the metadata_config.
              metadata_config = {
                ...
              }
            }
          }
        }
        update_mask {
          paths: "interaction_monitoring_config"
        }
        

#### Example 2: Sentiment score < -0.01
    
    
        conversation_profile     {
          name: "projects/agent-assist-console-demo/locations/global/conversationProfiles/your_new_conv_profile_id"
          interaction_monitoring_config {
            event_notification_config = {
                ...
            }
            alerting_config {
              rules {
                alert_rule_id: "customer sentiment negative"
                description: "negative sentiment"
                trigger_condition {
                  metric_condition {
                    metric_type: SENTIMENT
                    value_range {
                      max_threshold: -0.01
                    }
                    display_name: "negative sentiment"
                  }
                }
              }
              # Optional Tool config to retrieve customer name. If not required, skip setting the metadata_config.
              metadata_config = {
                ...
              }
            }
          }
        }
        update_mask {
          paths: "interaction_monitoring_config"
        }
        

#### Example 3: Sentiment score < -0.01 and AI coach rule matched
    
    
        conversation_profile     {
          name: "projects/agent-assist-console-demo/locations/global/conversationProfiles/your_new_conv_profile_id"
          interaction_monitoring_config {
            event_notification_config = {
                ...
            }
            alerting_config {
              # Required.
              rules {
                alert_rule_id: "sentiment is negative and agent coaching alert trigger rule(s) matched"
                description: "agent coaching alert trigger rule(s) matched and customer is unhappy"
                trigger_condition {
                  and_condition {
                    alert_conditions {
                      metric_condition {
                        metric_type: SENTIMENT_SCORE
                        value_range {
                          max_threshold: -0.01
                        }
                        display_name: "negative sentiment and agent coaching alert trigger rule(s) matched"
                      }
                    }
                    alert_conditions {
                      metric_condition {
                        metric_type: AGENT_COACHING_INSTRUCTIONS
                        agent_coaching_config {
                          generator_name: "projects/agent-assist-console-demo/locations/global/generators/newly_created_generator_id"
                        }
                        display_name: "negative sentiment and agent coaching alert trigger rule(s) matched"
                      }
                    }
                  }
                }
              }
              # Optional Tool config to retrieve customer name. If not required, skip setting the metadata_config.
              metadata_config = {
                ...
              }
            }
          }
        }
        update_mask {
          paths: "interaction_monitoring_config"
        }
        

#### Example 4: AI coach rule matched or Sentiment score < -0.01
    
    
        conversation_profile     {
          name: "projects/agent-assist-console-demo/locations/global/conversationProfiles/your_new_conv_profile_id"
          interaction_monitoring_config {
            event_notification_config = {
                ...
            }
            alerting_config {
              rules {
                alert_rule_id: "agent coaching alert trigger rule(s) matched"
                description: "agent coaching alert trigger rule(s) matched"
                trigger_condition {
                  metric_condition {
                    metric_type: AGENT_COACHING_INSTRUCTIONS
                    agent_coaching_config {
                      generator_name:    "projects/agent-assist-console-demo/locations/global/generators/newly_created_generator_id"
                    }
                    display_name: "agent coaching alert trigger rule(s) matched"
                  }
                }
              }
              rules {
                alert_rule_id: "customer sentiment negative"
                description: "negative sentiment"
                trigger_condition {
                  metric_condition {
                    metric_type: SENTIMENT
                    value_range {
                      max_threshold: -0.01
                    }
                    display_name: "negative sentiment"
                  }
                }
              }
              # Optional Tool config to retrieve customer name. If not required, skip setting the metadata_config.
              metadata_config = {
                ...
              }
            }
          }
        }
        update_mask {
          paths: "interaction_monitoring_config"
        }
        

## Step 4: Configure supervisor assist

  1. [Create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-console) to receive alerts. Agent Assist uses this Pub/Sub topic to receive alerts and metrics. Take a note of your topic ID.
  2. Submit your project and Pub/Sub topic ID to Google for allowlist.



The human-to-human monitoring service publishes the following event types:

  * Sentiment metrics are aggregated sentiment calculations for all end user turns in a conversation.
  * Alert events are notifications containing rule details that Agent Assist generates when sentiment breaches a configured threshold.



Supervisor assist supports the following standard configurations to address different integration requirements for these two events. You can include these settings in your interaction monitoring configuration.

  * **Default mode** : Alerts are published immediately when a condition is met. Sentiment metrics are published only after an alert has been initiated.
  * **Pure monitoring mode** : Sentiment metrics are published continuously for every turn. Alert events are ignored.
  * **Publish all mode behavior** : Both types of events are always published unconditionally.



## Step 5a: Test chat

Follow these steps to test supervisor assist with the chat simulator.

  1. Navigate to the monitoring simulator:
         
         https://agentassist.cloud.google.com/projects/project-id/locations/location-id/human-supervisor
         

  2. Click settings**Settings** and select **Human Agents**.

  3. Open another tab in your browser and navigate to the **Chat conversation simulator** using your conversation profile.

  4. Start the conversation in the conversation simulator, and notice that the monitoring simulator displays transcripts and sentiment scores.




## Step 5b: Test voice

Follow these steps to test supervisor assist with the voice simulator.

  1. Navigate to the monitoring simulator:
         
         https://agentassist.cloud.google.com/projects/project-id/locations/location-id/human-supervisor
         

  2. Click settings**Settings** , then select **Human agents** and **Only monitor phone calls**.

  3. Open another tab in your browser and navigate to the **Voice conversation simulator** using your conversation profile.

  4. Click call**Switch to voice**.

  5. Enter the phone number for an agent.

  6. Use another phone with a different number to call the new numbers displayed on the screen.


**Note:** For best speech recognition, use the [Chirp 3](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription-with-chirp3) model in your STT Configuration.

## Score maps

Supervisor assist provides two scores:

  * The per-turn sentiment score is a discrete floating point value from -1 to 1.
  * The up-to-the-point sentiment score is a continuous floating point value from -1 to 1.



You can map the continuous up-to-the-point sentiment scores to a custom score that is appropriate for different business units. The following example illustrates one mapping approach.

Example JavaScript Code for mapping:
    
    
    /**
     * Maps a score to a bucket index (1-10) based on 11 boundary points.
     * * @param {number} score - The input score (between -1 and 1)
     * @param {number[]} boundaries - An array of exactly 11 numbers sorted in ascending order.
     * @return{number} The bucket index (1 to 10).
     */
    function getBucketIndex(score, boundaries) {
      // 1. Validation: Ensure we have exactly 11 boundary points
      if (!Array.isArray(boundaries) || boundaries.length !== 11) {
        throw new Error("Boundaries must be an array of exactly 11 points.");
      }
    
      // 2. Validate Input Score Range 
      if (typeof score !== 'number' || score < -1 || score > 1) {
        throw new Error(`Input score ${score} is out of bounds. Must be between -1 and 1.`)
      }
    
      // 3. Iterate through boundaries to find the slot
      // We start checking from index 1 (the first upper bound)
      for (let i = 1; i < boundaries.length; i++) {
        // If the score is strictly less than the current boundary,
        // it belongs to the bucket corresponding to this index.
        if (score <= boundaries[i]) {
          return i;
        }
      }
    
      // Fallback (should be covered by step 2 validation, but ensures integer return)
      return -1;
    }
    
    
    // --- Example Usage ---
    
    // Create 11 boundary points from -1 to 1
    // [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    const boundaries = [];
    for (let i = 0; i <= 10; i++) {
      // Creating points: -1 + (i * 0.2)
      boundaries.push(parseFloat((-1 + (i * 0.2)).toFixed(1))); 
    }
    
    console.log("Boundaries:", boundaries);
    
    // Test Cases
    console.log(`Score -0.9 maps to Bucket: ${getBucketIndex(-0.9, boundaries)}`); // Expected: 1
    console.log(`Score -0.8 maps to Bucket: ${getBucketIndex(-0.8, boundaries)}`); // Expected: 2 (Inclusive lower)
    console.log(`Score 0.0 maps to Bucket: ${getBucketIndex(0.0, boundaries)}`);   // Expected: 6
    console.log(`Score 0.95 maps to Bucket: ${getBucketIndex(0.95, boundaries)}`); // Expected: 10
    console.log(`Score 1.0 maps to Bucket: ${getBucketIndex(1.0, boundaries)}`);   // Expected: 10 (Inclusive upper)
    
    

Optionally optimize the mapping using the following [code](https://colab.sandbox.google.com/drive/16Ovoy-aXDNhURa1XNX1s7L6ddtoAaHXg?resourcekey=0-X1B-EC2ntjQ_Vn8FWA7HIw&usp=sharing#scrollTo=OGCGaYP1VF1M) to automatically determine thresholds that maximize the correlation between mapped predictions and the CX score. After you perform this one-time optimization on your data, you can use the resulting data-driven boundaries rather than manually configuring them.

## Pub/Sub event notification

Both sentiment metrics and alerts are published to a single configured Pub/Sub topic. The payloads differ based on the event type.

Sentiment metrics Pub/Sub message payload:
    
    
    {
      "data": "{\"metric\":{\"metricType\":\"SENTIMENT_SCORE\",\"value\":{\"createTime\":\"2024-01-01T00:00:00.000Z\",\"sentiment\":{\"score\":0.5,\"magnitude\":0.5},\"advancedValues\":{\"exponentialMovingAverageValue\":0.5}},\"conversation\":\"projects/your-project-id/locations/global/conversations/conversation_id\",\"message\":{\"name\":\"projects/your-project-id/locations/global/conversations/conversation_id/messages/message_id\",\"content\":\"ok\",\"languageCode\":\"en-US\",\"participant\":\"projects/your-project-id/locations/global/conversations/conversation_id/participants/participant_id\",\"participantRole\":\"END_USER\",\"sendTime\":\"2024-01-01T00:00:00.000Z\"}}}",
      "attributes": {
        "conversation_id": "conversation_id"
      }
    }
    
    

Alter pubsub message payload example:
    
    
    {"data": "{\"alert\":{\"name\":\"projects/project_id/locations/location_id/interactionMonitoringAlerts/alert_id\",\"conversation\":\"projects/project_id/locations/location_id/conversations/conversation_id\",\"alertState\":\"CREATED\",\"alertMetadata\":{\"alertTriggerRules\":[{\"alertRuleId\":\"negative-sentiment\",\"description\":\"dummy_description\",\"Strong negative sentiment detected in last 30 seconds\":[{\"metricType\":\"SENTIMENT_SCORE\",\"values\":[{\"createTime\":\"2024-01-01T00:00:00.000Z\",\"sentiment\":{\"score\":0.0,\"magnitude\":0.0}}]}]}],\"channelType\":\"CHAT\"},\"createTime\":\"2024-01-01T00:00:00.000Z\"}}",
      "attributes": {
        "conversation_id": "conversation_id"
      }
    }
    

## API reference

[`AnalyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants/analyzeContent): 

  * Use case: Monitors chat conversations between an end-user and a human agent.
  * Testing methods: 
    * Console simulator: Use the Agent Assist console chat simulator.
    * API Integration: Send direct HTTP or RPC requests (see [[Example Code](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/dialogflow/participant_management.py#L52)]).



[`StreamingAnalyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent)

  * Use case: Monitors voice conversations between an end-user and a human agent.
  * Testing methods: 
    * Console simulator: Use the Agent Assist console voice simulator.
    * API integration: Send direct HTTP or RPC requests (see [[Example Code](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/dialogflow/participant_management.py#L52)]).



[`ListMessages`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.Conversations.ListMessages):

  * Retrieves the complete list of transcripts (both agent and customer turns) for a conversation.
  * Best practice: This API is particularly useful for voice conversations to verify the final, corrected transcripts for every turn after the stream has concluded.



`ListInteractionMonitoringMetrics`: Retrieves all sentiment metrics calculated and aggregated for a specific conversation.

Example request payload:
    
    
    {
      "parent": "projects/{project-id}/locations/{location-id}",
      "conversation":
    "projects/{project-id}/locations/{location-id}/conversations/{conversation-id}"
    }
    

Example response payload:
    
    
    {
      "interactionMonitoringMetrics": [{
        "metricType": "SENTIMENT_SCORE",
        "values": {
          "createTime": "2025-12-01T22:20:49.925Z",
          "sentiment": {
            "score": -1.0,
            "magnitude": 1.0
          },
          "advancedValues": {
            "movingAverageValue": -0.4994999999762513
          }
        }, {
          "createTime": "2025-12-01T22:20:21.027Z",
          "sentiment": {
            "score": 0.001,
            "magnitude": 0.001
          },
          "advancedValues": {
            "movingAverageValue": -0.4994999999762513
          }
        },
          "advancedValues": {
          }
        }]
    }
    

`ListInteractionMonitoringAlert`: Retrieves generated alerts. This can be scoped to an entire project or filtered to a specific conversation.

To query all alerts in a project:
    
    
    {
      "parent": "projects/{project-id}/locations/{location-id}"
    }
    

**To query alerts for a specific conversation id **
    
    
    {
      "parent": "projects/{project-id}/locations/{location-id}",
      "filter": "context_id=projects/{project-id}/locations/{location-id}/conversations/{conversation-id}"
    }
    

Filtering options. Users can apply additional filter criteria, such as alert status:
    
    
    alert_state=CREATED,alert_state=ACKNOWLEDGED
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
