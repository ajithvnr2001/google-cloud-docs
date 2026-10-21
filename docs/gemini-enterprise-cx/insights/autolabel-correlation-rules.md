---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/autolabel-correlation-rules/
title: Autolabeling and correlation rules \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:49.938461+00:00
---

# Autolabeling and correlation rules  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/autolabel-correlation-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Autolabeling and correlation rules Stay organized with collections  Save and categorize content based on your preferences. 

Customer Experience Insights introduces two rule-based features to enhance [conversation](https://docs.cloud.google.com/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.Conversation) processing:

  * **Autolabeling rules:** Automatically apply key-value labels to conversations based on defined conditions.
  * **Correlation rules:** Define how to link related conversation segments together to form complete customer interaction views.



Both rule types use the [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md) to provide flexible and dynamic rule definitions. CEL is fundamental to both autolabeling and correlation rules. You can configure these rules with the API or the CX Insights console.

## Autolabeling rules

Autolabeling rules automatically enrich only conversations with custom key-value labels during import. These labels improve filtering, categorization, and integration with other analyses and workflows. You can perform the following actions with autolabeling rules:

  * Categorize conversations by topic, customer type, product, or outcome.
  * Extract key data points from conversation metadata or Dialogflow parameters, such as `callId`, `isAuthenticated`, and `intent` names, into labels.
  * Flag conversations requiring specific attention, such as `high_escalation_risk`.



### Labels

Each autolabeling rule defines a label and contains ordered condition messages. Each label uses the following CEL expressions:

  * **Condition** : evaluates whether a conversation is true or false. An empty condition defaults to true.
  * **Value** : produces the string value for a label if the condition is true.



The first `LabelingCondition` that matches determines the label's value.

### Default rules

CX Insights automatically applies default rules for the following labels.

#### `sessionEscalated`

This label combines Dialogflow and default escalation signals to identify whether the end user or agent escalated the conversation. The value of this label informs the escalation rate metric on a [configurable dashboard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/configurable-dashboards). You can configure your own rule to overwrite this label if you use a custom escalation tool call.

#### `sessionContained`

This label identifies when no escalation occurred. When the value is `true`, the Quality AI conversation outcome can't be escalated. You can configure your own rule to overwrite this label.

#### `isRepeatedCallerConversation`

This label calculates the how often a user calls back within 24 hours, and relies on the `userIdentifier` label to determine whether a callback is from the same user. You can configure your own rule to overwrite this label.

#### `userIdentifier`

This label determine if the same user calls back within a specified number of hours. To do so, it uses the `obfuscated_external_user_id` variable from either `session_params` in Dialogflow and Customer Experience Agent Studio, or the `CreateParticipant` request in Agent Assist. If you use different session parameter variables for user identification, you must use `get_session_params()` to overwrite this label.\

#### `lastTransferSubAgentNames`

This label provides the name of the final Customer Experience Agent Studio subagent before someone escalates a conversation. The default value uses `get_last_subagent([entry_subagent])`, which assumes your named subagent handles the escalation. If you have a specific escalation agent, you must configure your own rule to overwrite the default value with `get_last_subagent([escalation_agent_name])`.

### Configure rules

You can also configure your own autolabeling rules with either the API or the CX Insights console.

### API

  1. Use the `Create` operation to configure an `AutoLabelingRule`. Sample request body: 
         
         {
           "displayName": "$DISPLAY_NAME",
           "labelKey": "$UNIQUE_KEY_NAME",
           "labelKeyType": LABEL_KEY_TYPE_CUSTOM 
         "conditions": [
             {
               "condition": "conversation.turn_count > 10 && conversation.duration > "60s"",
               "value": "'long_call'"
             },
             {
               "condition": "conversation.agent_id == "agent_007"",
               "value": "'special_agent'"
             }
           ],
         "active": true
         }

Curl command, if the request is saved in `auto_labeling_rule.json`: 
         
         curl-X POST   
         
               -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)"   
         
               -H "Content-Type: application/json; charset=utf-8"   
         
               -d @auto_labeling_rule.json   
         
           "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/autoLabelingRules?auto_labeling_rule_id=$RULE_ID"

  2. Give your rule a name in the following format: `projects/[project-id]/locations/[location-id]/autoLabelingRules/[auto_labeling_rule]`. The `[auto_labeling_rule]` ID is the `label_key` for custom rules.




You can also use any of the following operations with autolabeling rules. An autolabeling rule can have a maximum of 100 labels per conversation with a maximum of 256 characters per entry.

  * `Get`. 
        
        curl  -X GET   
        
          -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)"   
        
          -H "Content-Type: application/json; charset=utf-8" \ "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/autoLabelingRules/$RULE_ID"

  * `List`. 
        
        curl  -X GET   
        
          -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)"   
        
          -H "Content-Type: application/json; charset=utf-8" \ "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/autoLabelingRules"

  * `Update`. Depending on what fields to update, specify the `update_mask`. 
        
        curl  -X PATCH   
        
          -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)"   
        
          -H "Content-Type: application/json; charset=utf-8"   
        
          -d @update_payload.json \ "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/autoLabelingRules/$RULE_ID?update_mask=displayName,active"

  * `TestAutoLabelingRule`. Your payload should contain the rule to test and a sample conversation the rule will be evaluated on. Example: 
        
        {
        "conversation": {
        "agentId": "agent_007",
        "turnCount": 15,
        "duration": "75s"
        /# Add other conversation fields relevant to the rule
        },
        "autoLabelingRule": {
        "displayName": "Test Rule",
        "labelKey": "test_category",
        "conditions": [
          {
           "condition": "conversation.turn_count > 10 && conversation.duration > "60s"",
            "value": "'long_call_test'"
          }
        ],
        "active": true
        }
        }




### Console

  1. Navigate to the CX Insights console, sign in, and select your project. [CX Insights console](https://ccai.cloud.google.com/insights/projects)
  2. Click settings**Settings** > **Auto Labeling Rules**.
  3. Enter CEL expressions with a Monaco editor.
  4. Click **Save**.



### CEL examples

  * Label by agent ID: 
        
        label_key: "agent_category"
        conditions {
        condition: "conversation.agent_id == '007'"
        value: "'special_agent'"
        }
        conditions {
        condition: "conversation.agent_id.startsWith('team_a')"
        value: "'tier_1_support'"
        }
        conditions {
        condition: "" // Default
        value: "'standard'"
        }

  * Flag negative sentiment: 
        
        label_key: "needs_review"
        conditions {
        // This example assumes sentiment scores are present in the conversation's latest_analysis
        condition: "has(conversation.latest_analysis.analysis_result.call_analysis_metadata.sentiments) && conversation.latest_analysis. analysis_result.call_analysis_metadata.sentiments.exists(s, s.    sentiment_data.score < -0.5)"
        value: "'true'"
        }

  * Extract a Dialogflow parameter: 
        
        label_key: "df_session_outcome"
        conditions {
        condition: "" // Always try to extract
        value: "conversation.runtime_annotations.map(a, a.dialogflow_interaction.detect_intent_response_v3.query_result.parameters).filter(p, has(p.outcome)).map(p, p.outcome).first_element_or_empty_string()"
        }




### Use autolabels in analysis rule filters

Autolabeling rules can apply labels that control which conversations the main analysis rules process. The `conversation_filter` field in an analysis rule can reference labels using the labels map.

Example:
    
    
    // AnalysisRule to run detailed analysis on conversations labeled 'needs_review: true'
    display_name: "Detailed Analysis for Reviewed Conversations"
    conversation_filter: "labels.needs_review = \"true\""
    annotator_selector: {
      run_summarization_annotator: true
      // ... other annotators
    }
    analysis_percentage: 1.0
    active: true
    

## Correlation rules

Correlation rules define how Customer Experience Insights identifies and links related conversation segments. A conversation segment represents a single piece of a conversation, as it was ingested, such as a Dialogflow session or a single agent interaction. A full conversation represents a complete, linked conversation composed of one or more segments. By default, all new conversations start as segments. Correlation rules help you create a complete history of a customer's interaction, even when it spans multiple agents, channels, or sessions.

Correlation rules provide the following benefits for customer service conversation analysis.

  * **Unified transcript:** View a single, chronological transcript that combines utterances from multiple sources, such as a chatbot session followed by a live agent call.
  * **Cross-channel analysis:** Link interactions across different channels, such as chat and voice, to analyze sentiment trends and topic progression throughout an entire conversation journey.
  * **Metric accuracy:** Calculate metrics like total handling time or resolution rate for the full interaction rather than only individual parts.
  * **Context for agents:** Provide human agents with the full history of previous automated interactions.



### Correlation process

When correlation rules match multiple conversation segments, CX Insights groups them together. CX Insights then creates a new entry to represent the full conversation with its own unique conversation ID. CX Insights sets a full conversation's correlation ID to the common key that links the segments, and its type to `FULL`. CX Insights sets the original segments' correlation IDs to the common key and their types to `SEGMENT`. If a segment is not correlated with any other segments, CX Insights gives it both `SEGMENT` and `FULL` correlation types. 

#### Link messages

Correlation rules link related conversation segments from different sources and channels. CX Insights follows these steps to link conversation segments:

  1. **Group by join key:** CX Insights evaluates a CEL join key expression to extract a common identifier from the conversation, such as `callId`. Conversations sharing the same join key are potential candidates for linking. Join keys must be specific. If a key matches more than 20 conversations, the correlation might be rejected to prevent performance issues.
  2. **Refine with constraints:** The CEL constraint expression is an optional boolean check evaluated pairwise between candidates. This expression helps confirm if two segments sharing a key should actually be linked. This check is bidirectional, so it could include segment A linked to segment B and segment B linked to segment A.
  3. **Transitive link:** Linking is transitive. If conversation A is linked to B, and B is linked to C, then A, B, and C are merged into a single `FULL` conversation group.



A merged conversation can contain a maximum of five segments.

### Configure correlation rules

You can configure correlation rules using either the API or the CX Insights console.

### API

  1. Run the following code to set up a `CorrelationConfig`. 
         
         curl  -X PATCH   
         
           -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)"   
         
           -H "Content-Type: application/json; charset=utf-8"   
         
           -d @update_corr_config.json   
         
         "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/correlationConfig?update_mask=fullConversationConfig"

  2. Give your rule a name with the following format: `projects/{project-id}/locations/{location-id}/correlationConfig`.
  3. View the result in the `Conversation.CorrelationInfo` field.



You can use any of the following operations with correlation rules.

  * `GetCorrelationConfig`. 
        
        curl-X GET   
        
        -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)"   
        
        -H "Content-Type: application/json; charset=utf-8"   
        
        "https://$ENDPOINT/v1/projects/$PROJECT/locations/$LOCATION/correlationConfig"

  * `UpdateCorrelationConfig`. Sample body request, if it is saved in a `updated_corr_config.json`: 
        
        {
        "fullConversationConfig": {
        "correlationRules": [
          {
            "joinKeyExpression": "conversation.labels.uui",
            "active": true
          }
        ]
        }
        }

  * `TestCorrelationConfig`. Your payload should specify the sample conversation details besides the correlation rule to test. Example: 
        
        {
        "correlationConfig": {
        "fullConversationConfig": {
          "correlationRules": [
           {
              "joinKeyExpression": "conversation.agent_id",
             "active": true
            }
          ]
        }
        },
        "filter": "agent_id="agent_007"",
        "maxSampleCount": 100
        }




### Console

  1. Navigate to the CX Insights console, sign in, and select your project. [CX Insights console](https://ccai.cloud.google.com/insights/projects)
  2. Click settings**Settings** > **Correlation Config**.
  3. Click **Save**.



Administrators can define and manage `CorrelationRule` entries within the `CorrelationConfig`. You can test your correlation rules by selecting conversations. Test results are added to a dataset for review.

### CEL example

Link by `callId` from Dialogflow:
    
    
    join_key_expression:
    // Extracts 'callId' from Dialogflow parameters, falls back to conversation name.
    default(conversation.runtime_annotations.map(a,
      a.dialogflow_interaction.detect_intent_response_v3.query_result.parameters)
      .filter(p, has(p.callId))
      .map(p, p.callId)
      .first_element_or_empty_string(), conversation.name)
    

## CEL utility functions

CX Insights provides several utility functions that you can use in CEL expressions to evaluate conversations.

Function signature | Description  
---|---  
`get_label(string key)` | Returns the string value of the label associated with the given `key` from the current conversation.  
`exists_call_back_conversation(  
string filter)` | Returns `true` if a "call back" conversation exists matching the provided `filter`. It searches for conversations with the same user ID (obfuscated user ID or predefined user ID label) within a default future window (24 hours). The provided `filter` is appended to this criteria.  
`has_same_caller_conversation_in_n_hours(  
int hours)`  
  
`has_same_caller_conversation_in_n_hours(  
int hours, string filter)` | Returns `true` if there are conversations from the same caller/user within the specified number of `hours` (positive for future, negative for past). An optional `filter` can be provided to further restrict the search.  
`get_same_caller_conversations_in_n_hours(  
int hours)`  
  
`get_same_caller_conversations_in_n_hours(  
int hours, string filter)` | Returns a list of conversations from the same caller/user within the specified number of `hours`. An optional `filter` can be provided.  
`get_session_params(string key)` | Retrieves the string value of a session parameter (from Dialogflow or CES) associated with the given `key`. It searches through runtime annotations and CES turn annotations in reverse chronological order. Returns empty string if not found.  
`get_last_subagent()`  
  
`get_last_subagent(list excludes)` | Returns the display name of the last subagent involved in the conversation. Can optionally exclude subagents listed in the `excludes` list (which typically include the subagent specifically handling escalation) unless it is the only subagent.  
`get_last_subagent_id()`  
  
`get_last_subagent_id(list excludes)` | Returns the ID of the last subagent involved in the conversation. Can optionally exclude subagents listed in the `excludes` list (which typically include the subagent specifically handling escalation) unless it is the only subagent.  
`list.first_element_or_empty_string()` | Available on lists of strings. Returns the first element of the list if it is a string; otherwise (or if empty), returns an empty string.  
  
## Segment and conversation-level analysis

With CX Insights you can analyze conversations at different granularities, including both per-segment and per-conversation analysis for all features. The **Conversation Hub** and **Quality AI** pages in the console compare conversation- and segment-level data, indicating the multisegment structure of linked conversations.

To target specific levels of analysis, use the following [filters](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering) with an [analysis rule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/analysis-rule#create_a_rule).

### Segment-level view

The goal of this view is to analyze specific parts of an interaction, such as a single agent's turn. Use the `correlation_info.correlation_types:SEGMENT` parameter to filter the segment level view.

### Full conversation view

Use this view to analyze the complete customer journey, whether it consists of linked or standalone conversations. Use the `correlation_info.correlation_types:FULL` parameter to filter the full conversation view.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
