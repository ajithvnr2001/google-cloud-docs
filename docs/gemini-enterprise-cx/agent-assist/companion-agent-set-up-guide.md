---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-set-up-guide/
title: Companion agent set up guide \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:10.471996+00:00
---

# Companion agent set up guide  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-set-up-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Companion agent set up guide Stay organized with collections  Save and categorize content based on your preferences. 

Companion agent is a multi-agent system that uses the following core features to support your work:

  * **Guidance Agent** : Proactively provides information to a human agent during a conversation, such as next action suggestions and sample responses.
  * **On-demand Assistant** : An AI chatbot that the human agent can interact with.



## Before you begin

Before you create a companion agent, you must decide which resources and tools you want to use.

  * **Resources** : Companion agent can use a set of instructions, and tool definitions.

  * **Tools** : Companion agent connects to external [tools](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-tools#supported_tools_and_use_cases) such as Datastore tools, Google Search, and OpenAPI tools to fetch information during live conversations.




## Set up a companion agent

Follow these steps to set up your companion agent.

### Step 1: Create a companion agent

  1. Log into the [Agent Assist console](https://agentassist.cloud.google.com/).
  2. Navigate to **Companion agent** and click **Create**.
  3. Enter a **Display name**.
  4. Click **Save**.



### Step 2: Add tools to the companion agent

Empower the companion agent by adding web search and Datastore search tools. For Datastore search, you should already have a [Datastore](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store) setup.

#### Step 2.1: Create search tools

Follow these steps to create search tools, on the [Customer Experience Agent Studio console](https://ces.cloud.google.com/projects) :

  1. Select the same project and location where you created the companion agent.
  2. Click **Create Agent** , enter a **Name**.
  3. Click **Create** > **Add** in the root agent > **Add Tool**.
  4. Click **Add** in the tool management panel and select **Web Grounding** or **Data Store**.
  5. Enter a **Name** and a **Description** of the tool.
  6. For the Datastore tool, also select the data stores to connect.
  7. Click **Create**.
  8. To test the created tool, click the created tool in the Root Agent > **Test** to open the test window. Make sure you test the tool and verify that it works before adding to the companion agent.



#### Step 2.2: Add tools

Follow these steps to add tools to the companion agent, on the [Agent Assist console](https://agentassist.cloud.google.com/):

  1. Navigate to **Companion agent** and click the one you created.
  2. Click **Add** in the **Tools** section.
  3. Select the CX Agent Studio agent you created.
  4. Click **Tool Type** and select **Web Grounding** or **Data Store**.
  5. Click **Tool** and select the search tool you created.
  6. Check one of the following options for **Trigger** : 
     * **Reactive Suggestion** : Enables search tools for the reactive agent. 
     * **Proactive Suggestion** : Enables search tools for the guidance agent.
  7. Click **Add** > **Save**.



You can repeat the these steps to add both the web search tool and the Datastore search tool.

### Step 3: Add guidance to the companion agent

Companion agent instructions use configured tools, including datastore tools, and prioritize guidance instruction rules. These guidance instructions determine the conditions under which the companion agent supports human agents and activates configured tools. Follow these steps to add guidance to your companion agent.

  1. Open companion agent in the [Agent Assist console](https://agentassist.cloud.google.com/).
  2. Select a **Triggering event** from the menu. The triggering event determines when to initiate a guidance agent. Choose one of the following options: 
     * Customer message
     * Agent message
     * End of utterance
  3. Click **Add** in the **Guidance section**.
  4. Enter the following details: 
     * **Guidance title** : A name for your guidance agent.
     * **Description** : A description of what your guidance agent provides.
     * **Condition** : Determines the most appropriate guidance for the current situation.
  5. Click **Actions** and add your steps. The actions suggest the next steps a human agent can take.
  6. To add tools for guidance, follow the instructions in Step 2.2.
  7. Click **Add** > **Save**.

**Note:** Enabling the Google Search tool opts in to sending query data to Google Search.

### Step 4: Configure model guidance

You can set [overarching instructions](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ai-coach-best-practices#overarching-guidance) to determine the behaviour of the guidance agent. Follow these steps to configure model guidance.

  1. Open companion agent in the [Agent Assist console](https://agentassist.cloud.google.com/).
  2. Enter instructions in the **Model Guidance** box.
  3. Click **Save**.



### Step 5: Test Your Companion Agent

Before you begin using the agent, create a test profile to see it in action.

  1. In the [Agent Assist console](https://agentassist.cloud.google.com/), go to **Conversation profiles** and click **Create**.
  2. Enter a **Display name**.
  3. For **Suggestion types** , select **Companion agent** and choose the agent you created.
  4. Click **Save**.
  5. Navigate to your profile and click **Try it out** to start the simulation.



## Enable streaming reactive companion API

Streaming reactive companion API helps human agents build an on-demand assistant directly in the console. It enables agents to ask questions, search the web, and use tools.

Follow these steps to enable the streaming reactive companion API.

### Step 1: Establish a streaming connection

Before you begin, ensure you meet the following criteria:

  * Have the `dialogflow.participants.suggest` permission.
  * The target participant `Participant::AGENT` must represent the human agent.



To interact with reactive mode, your application should invoke the bidirectional streaming remote procedure call (RPC).

The following example shows the JSON structure required for the opening stream message. This example specifies both the target human agent participant resource path and the initial query text.
    
    
    RPC: google.cloud.dialogflow.v2.Participants.StreamingReactiveCompanionSuggestions
    (or v2beta1.Participants.StreamingReactiveCompanionSuggestions)
    

When you open the stream, your initial `StreamingReactiveCompanionSuggestionsRequest` request must include the following details in the `textInput`, as shown in the example.

  * Target human agent `participant` resource path 
  * Initial query text


    
    
    {
      "participant": "projects/my-project/locations/us-central1/conversations/conv-123/participants/agent-456",
      "textInput": "Can the customer return a laptop opened 25 days ago?"
    }
    

### Step 2: Send human agent queries

After you establish the stream, transmit messages with `textInput` to send subsequent human agent queries.
    
    
    {
      "textInput": "What was the ID for this customer?"
    }
    

The companion agent processes only one active query per conversation session at a time. This restriction prevents state corruption, conflicting tool runs, and out-of-order conversational turns. If you send a new `textInput` query while the reactive agent is actively generating a response or running a tool on a previous query, the server immediately rejects the new query with the `ABORTED` status code and the message `A request is already processing`.

### Step 3: Cancel an existing query

When a human agent wants to stop a running query, they can cancel the ongoing turn without closing the gRPC stream. Send a request containing `cancelReactiveQuery` as follows:
    
    
    {
      "cancelReactiveQuery": {}
    }
    

The server responds with a status message confirming cancellation (`ABORTED / CANCELLED: Reactive query successfully cancelled by client.`).

### Step 4: Final answer

When a companion agent finishes query processing, it sends its final complete response back to the interactive panel. Along with the final text, the response includes the following complete background details:

  * **Full answer** : The complete text reply generated by the companion agent.
  * **Tools used** : A record of any internal tools or external web searches used to look up facts.
  * **Source references** : Links, article titles, and web addresses for all reference materials used for the answer.
  * **Resource ID** : A unique resource ID of answer records and agent feedback.



The following example shows a final response message: 
    
    
    {
      "isFinal": true,
      "answerRecord": "projects/my-project/locations/us-central1/answerRecords/ar-789",
      "reactiveModeFinalResponse": {
        "response": "For SKU-104 laptops, the standard return window is 30 days from the date of delivery, provided the item is returned with all original packaging [1]. According to USPS holiday schedules, shipments may experience a 1-day delay on federal postal holidays [2].",
        "toolCalls": [
          {
            "toolCallInfo": {
              "toolCall": {
                "toolDisplayName": "DataStoreTool",
                "action": "searchKnowledgeBase"
              },
              "toolCallResult": {
                "action": "searchKnowledgeBase"
              }
            }
          },
          {
            "toolCallInfo": {
              "toolCall": {
                "toolDisplayName": "GoogleSearchTool",
                "action": "searchWeb"
              },
              "toolCallResult": {
                "action": "searchWeb"
              }
            }
          }
        ],
        "groundingMetadata": {
          "groundingChunks": [
            {
              "retrievedContext": {
                "uri": "https://internal-kb.company.com/policies/hardware-returns-30d",
                "title": "Hardware Return Window Policy (30 Days)"
              }
            },
            {
              "retrievedContext": {
                "uri": "https://www.usps.com/holiday/holiday-schedule.htm",
                "title": "USPS Federal Holiday Schedule"
              }
            }
          ],
          "groundingSupports": [
            {
              "segment": {
                "startIndex": 0,
                "endIndex": 127,
                "text": "For SKU-104 laptops, the standard return window is 30 days from the date of delivery, provided the item is returned with all original packaging [1]."
              },
              "groundingChunkIndices": [0]
            },
            {
              "segment": {
                "startIndex": 128,
                "endIndex": 242,
                "text": "According to USPS holiday schedules, shipments may experience a 1-day delay on federal postal holidays [2]."
              },
              "groundingChunkIndices": [1]
            }
          ]
        }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
