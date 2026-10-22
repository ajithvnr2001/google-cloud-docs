---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-api/
title: List conversations \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:08.539805+00:00
---

# List conversations  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  List conversations Stay organized with collections  Save and categorize content based on your preferences. 

When you [list conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/list) in Customer Experience Insights, you can filter them by one or more characteristics to narrow down the results. You can also sort the results on select conversation attributes.

## Sorting

Conversations returned by the `ListConversations` API can be sorted on one of the following values by passing this in the `order_by` field of the request:

  * `create_time {asc, desc}`
  * `customer_satisfaction_rating {asc, desc}`
  * `duration {asc, desc}`
  * `latest_analysis {asc, desc}`
  * `start_time {asc, desc}`
  * `turn_count {asc, desc}`



The default sort order is ascending, but sort order can be set by specifying `asc` or `desc`.

## Filtering

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.conversations.list`



Conversations can be filtered on one or more of the characteristics listed on the [Conversation Filtering](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering) page.

### Agent ID

Filter conversations that are handled by a specific agent ID. The only supported operator is equality.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * AGENT_ID: the agent ID.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=agent_id=\"AGENT_ID\"

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=agent_id=\"AGENT_ID\""

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=agent_id=\"AGENT_ID\"" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "conversations": [
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_1",
          "agentId": "AGENT_ID",
          ...
        },
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_2",
          "agentId": "AGENT_ID",
          ...
        },
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_3",
          "agentId": "AGENT_ID",
          ...
        },
      ]
    }
    

### Dialogflow conversation

Filter conversations that map to a Dialogflow conversation resource name. The only supported operator is equality. This filter is helpful if you create conversations in Dialogflow, enable [Dialogflow runtime integration](https://docs.cloud.google.com/gemini-enterprise-cx/insights/dialogflow-runtime-integration) and want to find out which conversations in Customer Experience Insights map to which conversations in Dialogflow.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * DIALOGFLOW_CONVERSATION: the Dialogflow conversation resource name. Its format is `projects/{project}/locations/{location}/conversations/{conversation}`

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=data_source.dialogflow_source.dialogflow_conversation=\"DIALOGFLOW_CONVERSATION\"

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=data_source.dialogflow_source.dialogflow_conversation=\"DIALOGFLOW_CONVERSATION\""

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=data_source.dialogflow_source.dialogflow_conversation=\"DIALOGFLOW_CONVERSATION\"" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "conversations": [
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_1",
          "dataSource": {
            "dialogflowSource": {
              "dialogflowConversation": "DIALOGFLOW_CONVERSATION",
            },
          },
          ...
        },
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_2",
          "dataSource": {
            "dialogflowSource": {
              "dialogflowConversation": "DIALOGFLOW_CONVERSATION",
            },
          },
          ...
        },
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_3",
          "dataSource": {
            "dialogflowSource": {
              "dialogflowConversation": "DIALOGFLOW_CONVERSATION",
            },
          },
          ...
        },
      ]
    }
    

### Dialogflow conversation profile ID

Filter conversations that map to a Dialogflow conversation profile ID. The only supported operator is equality. This filter is helpful if you configure [Dialogflow conversation profiles](https://docs.cloud.google.com/agent-assist/docs/conversation-profile) to create conversations in Dialogflow, enable [Dialogflow runtime integration](https://docs.cloud.google.com/gemini-enterprise-cx/insights/dialogflow-runtime-integration) and want to find out which conversations in Customer Experience Insights map to the conversations that were created by a specific Dialogflow conversation profile.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * DIALOGFLOW_CONVERSATION_PROFILE_ID: the Dialogflow conversation profile ID. Note that this is the ID only and not the resource path.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=dialogflow_conversation_profile_id=\"DIALOGFLOW_CONVERSATION_PROFILE_ID\"

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=dialogflow_conversation_profile_id=\"DIALOGFLOW_CONVERSATION_PROFILE_ID\""

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations?filter=dialogflow_conversation_profile_id=\"DIALOGFLOW_CONVERSATION_PROFILE_ID\"" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "conversations": [
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_1",
          "dialogflowConversationProfileId": "DIALOGFLOW_CONVERSATION_PROFILE_ID",
          ...
        },
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_2",
          "dialogflowConversationProfileId": "DIALOGFLOW_CONVERSATION_PROFILE_ID",
          ...
        },
        {
          "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID_3",
          "dialogflowConversationProfileId": "DIALOGFLOW_CONVERSATION_PROFILE_ID",
          ...
        },
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
