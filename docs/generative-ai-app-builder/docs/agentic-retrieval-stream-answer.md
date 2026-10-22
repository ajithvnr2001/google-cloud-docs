---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/agentic-retrieval-stream-answer/
title: Stream answers using agentic retrieval \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:33.915382+00:00
---

# Stream answers using agentic retrieval  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/agentic-retrieval-stream-answer/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Stream answers using agentic retrieval Stay organized with collections  Save and categorize content based on your preferences. 

**GA with allowlist:** Access to the agentic retrieval with the stream answers method is available to select Google Cloud customers. To find out more or to sign up to use this feature, contact your Google Cloud [sales representative](https://cloud.google.com/contact). 

This page introduces agentic retrieval and explains how to use it with the [stream answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/streamAnswer) method.

## About agentic retrieval

Agentic retrieval used with the stream answers method can obtain better results for certain use cases, for example, to enable multi-pass retrieval for apps with multiple data stores or to customize answer generation for different classes of queries.

Using agentic retrieval adds some complexity to your apps but in return, offers more control over the results.

Agent Search includes a predefined agent that you can use to customize the behavior of a search engine. This allows more customization than is available through the app Configurations UI or the [streaming answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/streamAnswer) method without agentic retrieval.

### Blended search with and without agentic retrieval

Agentic retrieval is particularly useful for blended search apps. Without agentic retrieval, search uses a single-pass fan-out that queries all your data stores at once. In contrast, agentic retrieval enables multi-pass searching. The agent plans and executes searches sequentially, choosing the best tools for each step. It can combine results from multiple Agent Search data stores and use tools like Google Search and Google Maps as well.

For example, you have separate data stores for global company policies and regional office details. A user asks: "What are the compliance rules for our Tokyo office?":

  * Without agentic retrieval: Queries both the policy store and the regional office store simultaneously with the full query string. This might return fragmented results.

  * With agentic retrieval: The agent plans the execution. It first retrieves details about the Tokyo office from the regional store. Then, using that specific context, it performs a second, targeted search in the policy store.

The agent synthesizes these findings into a single, coherent, and more accurate answer.




Agentic retrieval also lets you perform multi-turn search queries (follow-up questions) on blended search apps. Without agentic retrieval, multi-turn search works only with single data store apps. To persist conversation context across multiple turns, optionally pair agentic retrieval with a [Agent Platform session](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions).

### Custom query classification

The [answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/answer) and the [streaming answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/streamAnswer) methods provide two [query classification](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#query_classification) types: `ADVERSARIAL_QUERY` and `NON_ANSWER_SEEKING_QUERY`.

Agentic retrieval lets you define additional classification types to match your business workflows. The system uses a classifier to determine the user's intent and routes the request to the appropriate agent configuration.

For example, from the query, you determine that the intent of the query is to track an order and you have specified a `TRACK_ORDER` classification. Instead of running a generic search across all your data stores, the system loads a specialized agent equipped with the tools and data needed to retrieve shipping status.

## Ways to enable and use agentic retrieval

There are two ways to enable agentic retrieval:

  * **Predefined Google answer agent:** If you already have a search app in Agent Search, you can enable agentic retrieval by setting `enable_agent_invocation=true` in API requests when sending queries to the app. In this case, you keep the existing search serving config.

  * **Custom AI-mode app:** When you create an Agent Search app, you define a different type of serving config, the `default_agent_answer` serving config. This might also be referred to as the custom AI-mode engine because "app" and "engine" are used interchangeably in Agent Search.




## Before you begin

Before you can use agentic retrieval, do the following:

  * Set up a reasoning engine for multi-turn sessions

  * Optional: Set up a custom AI-mode app




### Set up a reasoning engine for multi-turn sessions

To persist conversation context across multiple turns, you need to create a Agent Runtime on Gemini Enterprise Agent Platform [engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) (also called a _reasoning engine_).

When you make a `streamAnswer` request, you pass the resource name of the Agent Runtime as the `reasoningEngine` field on the `streamAnswer` request.

  1. Enable the [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/cloud-environment) on your Google Cloud project.

  2. Create an Agent Runtime instance (also called the reasoning engine) using the [Agent Engine REST API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-api) (or the [Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-adk)). The instance hosts the sessions used by the `streamAnswer` method.

The instance resource name has the format:
         
         projects/PROJECT_NUMBER/locations/LOCATION_ID/reasoningEngines/REASONING_ENGINE_ID

  3. Grant the Discovery Engine service agent access to the reasoning engine by granting the role [`roles/aiplatform.reasoningEngineServiceAgent`](https://docs.cloud.google.com/iam/docs/understanding-roles#aiplatform.reasoningEngineServiceAgent) to the Discovery Engine service account:
         
         service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com

where `PROJECT_NUMBER` is the number of the project that hosts the reasoning engine. This permission lets the streaming answer backend create, read, and append events to sessions on your behalf.

  4. Review applicable quotas. Sessions backed by Agent Runtime consume quotas from the Agent Platform API. The quotas of interest are:

     * `aiplatform.googleapis.com/session_write_requests` — create, delete, or update Agent Runtime sessions per minute.

     * `aiplatform.googleapis.com/session_event_append_requests` — append event to Agent Runtime sessions per minute.

For more information, see [Gemini Enterprise Agent Platform Agent Engine quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/quotas#vertex-re).

  5. Note down the Agent Runtime resource name because you need to pass it as the `reasoningEngine` field on the `streamAnswer` request.




### Optional: Set up a custom AI-mode app

By default, agentic retrieval uses the predefined Google answer agent. This classifies queries into intents `DEFAULT_ANSWER_SEEKING` and `DO_NOT_ANSWER`. You can create a custom AI-mode app when you want to customize tools or add support for new classes of query intents. Each custom intent (or _frame_) declares the conditions under which the agent classifies a query into the intent and the instructions and tools the agent uses to handle it.

  1. Create the engine through the [`engines.create`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/create) REST method with an `engine_config.answer_agent` block.

The configuration is structured as follows:
         
         engine {
          name: "YOUR_AI_MODE_ENGINE"
          display_name: "YOUR_AI_MODE_ENGINE_DISPLAY_NAME"
          engine_config {
            answer_agent {
              frames {
                vertical_intent: "YOUR_CUSTOM_INTENT"
                vertical_intent_prompt {
                  instructions: "Instructions for when to classify a user query as YOUR_CUSTOM_INTENT."
                }
                initial_prompt {
                  instructions: "Instructions for the agent on how to process a user query classified as YOUR_CUSTOM_INTENT."
                  tools {
                    discovery_engine_search_tool_config {
                      serving_config: "YOUR_SEARCH_SERVING_CONFIG_1"
                      page_size: 10
                    }
                    tool_description: "This tool can help search corpus 1."
                  }
                  tools {
                    discovery_engine_search_tool_config {
                      serving_config: "YOUR_SEARCH_SERVING_CONFIG_2"
                      page_size: 10
                    }
                    tool_description: "This tool can help search corpus 2."
                  }
                }
              }
            }
          }
         }
         engine_id: "SAMPLE_MULTI_SEARCH_RETRIEVAL"

  2. After you create the engine, route requests through its `default_agent_answer` serving config:
         
         projects/*/locations/*/collections/*/engines/YOUR_AI_MODE_ENGINE/servingConfigs/default_agent_answer

  3. For help designing or registering a custom AI-mode app, contact [support](https://docs.cloud.google.com/support).




## Stream an answer using agentic retrieval

The following command shows how to call the [streaming answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/streamAnswer) method with agentic retrieval enabled. Similar to the output without agentic retrieval, this call streams a generated answer in the form of a series of JSON responses.

If you have set up a reasoning engine, include its resource name in the `reasoningEngine` field to persist the session across turns.

### REST

To search and get results with a streamed generated answer, do the following:

  1. Run the following curl command:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/SERVING_CONFIG_ID:streamAnswer" \
           -d '{
                 "query": { "text": "QUERY" },
                 "session": "SESSION",
                 "enableAgentInvocation": true,
                 "userPseudoId": "USER_PSEUDO_ID",
                 "reasoningEngine": "projects/PROJECT_NUMBER/locations/LOCATION_ID/reasoningEngines/REASONING_ENGINE_ID"
               }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `SERVING_CONFIG_ID`: to use a custom AI-mode app, set this to `default_agent_answer`. To use the predefined Google answer agent, set this to `default_search`. 
     * `PROJECT_NUMBER`: the number of the project that hosts the reasoning engine.
     * `QUERY`: a free-text string that contains the question or search query.
     * `SESSION`: if continuing a multi-turn conversation, this is the session resource name returned in the previous turn's response, for example, `projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions/SESSION_ID`. If not continuing a conversation, set this to `-`, a hyphen. 
     * `USER_PSEUDO_ID`: a unique identifier used for tracking the visitor.
     * `LOCATION_ID`: the location of your reasoning engine, for example `us-central1`.
     * `REASONING_ENGINE_ID`: the ID of the Agent Engine instance you created.

#### Example command and partial result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_serving_config:streamAnswer" \
      -d '{
            "query": { "text": "3 bedroom house in new haven" },
            "session": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/-",
            "enableAgentInvocation": true,
            "userPseudoId": "user-1",
            "reasoningEngine": "projects/123456/locations/us-central1/reasoningEngines/6732301450535239680"
          }'
    
    
    * * *
    
    
    answer  {
      name: "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/7813433670721451971/answers/7813433670721454054"
      state: SUCCEEDED
      answer_text: "I found several 3-bedroom properties in New Haven, CT, that might interest you. Here are the top three results along with their nearby schools:\n\n### 1. 37 Emerson Street, New Haven, CT\n*   **Price:** $415,061\n*   **Details:** 3 Bedrooms, 1.5 Bathrooms, 1,961 sq. ft.\n*   **Description:** An elegant multi-family residence with a two-car garage, offering classic charm and modern convenience near universities.\n*   **Nearby Schools:**\n    *   **Elementary:** Edgewood Magnet School (Rating: 3.9/5)\n    *   **Middle:** Betsy Ross Arts Magnet School (Rating: 4.1/5)\n    *   **High:** Hillhouse High School (Rating: 3.2/5)\n\n### 2. 248 West Hazel Street, New Haven, CT\n*   **Price:** $374,255\n*   **Details:** 3 Bedrooms, 2 Bathrooms, 1,835 sq. ft.\n*   **Description:** A meticulously maintained multi-family home with a two-car garage, ideal for investment or multi-generational living.\n*   **Nearby Schools:**\n    *   **Elementary:** Worthington Hooker School (Rating: 4.4/5)\n    *   **Middle:** Engineering - Science University Magnet School (Rating: 4.2/5)\n    *   **High:** Hillhouse High School (Rating: 3.2/5)\n\n### 3. 378 Central Avenue, New Haven, CT\n*   **Price:** $581,120\n*   **Details:** 3 Bedrooms, 2 Bathrooms, 1,966 sq. ft.\n*   **Description:** A distinguished three-family residence with a garage, located in a vibrant neighborhood with easy access to culinary and cultural spots.\n*   **Nearby Schools:**\n    *   **Elementary:** Edgewood Magnet School (Rating: 3.9/5)\n    *   **Middle:** Betsy Ross Arts Magnet School (Rating: 4.1/5)\n    *   **High:** Wilbur Cross High School (Rating: 3.5/5)\n\nWould you like more details on any of these listings, or would you like to schedule a tour?"
      references {
        structured_document_info {
          document: "projects/123456/locations/global/collections/default_collection/dataStores/housing-ct-20260406/branches/0/documents/34325"
          struct_data {
            fields {
              key: "address"
              value {
                string_value: "53 EMERSON STREET"
              }
            }
            fields {
              key: "bathrooms"
              value {
                number_value: 1.5
              }
            }
            fields {
              key: "bedrooms"
              value {
                number_value: 3.0
              }
            }
            fields {
              key: "garages"
              value {
                number_value: 2.0
              }
            }
            fields {
              key: "generated_description"
              value {
                string_value: "53 Emerson Street, New Haven, CT \342\200\223 An exceptional opportunity awaits in the heart of New Haven. This elegant three-family residence offers a rare blend of classic charm and modern convenience. Spanning 1,961 square feet, this property presents a versatile layout with 3 well-appointed bedrooms and 1.5 baths, catering to a variety of living arrangements or investment strategies. A coveted amenity in urban settings, a spacious two-car garage provides secure parking and additional storage. Situated in a desirable New Haven neighborhood, this address offers easy access to the city\'s vibrant cultural scene, esteemed universities, and burgeoning culinary landscape. Anticipate a 2025 valuation of $415,061. An astute investment for the discerning buyer."
              }
            }
            fields {
              key: "location"
              value {
                struct_value {
                  fields {
                    key: "latitude"
                    value {
                      number_value: 41.32836
                    }
                  }
                  fields {
                    key: "longitude"
                    value {
                      number_value: -72.96519
                    }
                  }
                }
              }
            }
            fields {
              key: "price"
              value {
                number_value: 415061.0
              }
            }
            fields {
              key: "residential_type"
              value {
                string_value: "Three Family"
              }
            }
            fields {
              key: "square_footage"
              value {
                number_value: 1961.0
              }
            }
            fields {
              key: "town"
              value {
                string_value: "New Haven"
              }
            }
          }
        }
        queries: "3 bedroom house in New Haven"
      }
      references {
      ...
      }
      references {
      ...
      }
      related_questions: "Schedule a tour for 248 West Hazel Street"
      related_questions: "Are there any 3 bedroom houses in New Haven under $350k?"
      related_questions: "What are the best-rated elementary schools in New Haven?"
      related_questions: "Find 4 bedroom houses in New Haven"
    }
    session {
      name: "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/7813433670721451971"
      state: IN_PROGRESS
      user_pseudo_id: "user-1"
      turns {
        query {
          text: "3 bedroom house in new haven"
        }
        answer: "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/7813433670721451971/answers/7813433670721454054"
      }
      start_time {
        seconds: 1778556129
        nanos: 731866398
      }
      metadata {
        key: "google.consumer_agent_session_id"
        value: "5099640345302401024"
      }
    }
    answer_query_token: "NMwKDAjeuYrQBhCq9aTMAhIkNmEwMzNjNjQtMDAwMC0yZjMzLWIxYzYtZjQwMzA0M2FlYmQ0"
    
    




### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

The following sample uses the [Discovery Engine Python client](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest) (`v1alpha`) to call `stream_answer_query` with agent invocation enabled. Pass the `reasoning_engine` field for multi-turn sessions.
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1alpha
    
    
    def run_stream_answer_query():
        PROJECT_ID = "YOUR_PROJECT_ID"
        LOCATION = "global"  # or a specific region
        COLLECTION_ID = "default_collection"
        ENGINE_ID = "YOUR_ENGINE_ID"
        # Use "default_search" for the predefined Google answer agent, or
        # "default_agent_answer" if you have configured a custom AI_MODE app.
        SERVING_CONFIG_ID = "default_search"
        USER_ID = "user-id"
        QUERY_TEXT = "YOUR_QUERY_TEXT"
        REASONING_ENGINE_ID = "YOUR_REASONING_ENGINE_ID"
        # Use "-" to start a new session, or pass the sessionId returned in
        # the previous turn's response to continue an existing session.
        SESSION_ID = "-"
    
        SESSION_REF = (
            f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/"
            f"{COLLECTION_ID}/engines/{ENGINE_ID}/sessions/{SESSION_ID}"
        )
        SERVING_CONFIG_ENGINE = (
            f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/"
            f"{COLLECTION_ID}/engines/{ENGINE_ID}/servingConfigs/{SERVING_CONFIG_ID}"
        )
        REASONING_ENGINE = (
            f"projects/{PROJECT_ID}/locations/{LOCATION}/"
            f"reasoningEngines/{REASONING_ENGINE_ID}"
        )
    
        client_options = ClientOptions(
            api_endpoint="discoveryengine.googleapis.com"
        )
    
        client = discoveryengine_v1alpha.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.conversational_search_service.ConversationalSearchServiceClient.html)(
            client_options=client_options
        )
    
        request = discoveryengine_v1alpha.[AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.html)(
            query=discoveryengine_v1alpha.[Query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Query.html)(text=QUERY_TEXT),
            serving_config=SERVING_CONFIG_ENGINE,
            user_pseudo_id=USER_ID,
            enable_agent_invocation=True,
            session=SESSION_REF,
            reasoning_engine=REASONING_ENGINE,
        )
    
        print(f"Starting StreamAnswerQuery agentic session with: {request}")
        stream = client.stream_answer_query(request)
    
        try:
            for response in stream:
                print(f"Received response: {response}")
        except Exception as e:
            print(f"Error during streaming: {e}")
    
    
    if __name__ == "__main__":
        run_stream_answer_query()

## Get the preview version of the Discovery Engine SDK

Discovery Engine SDK makes it easier to interact with Google Cloud services from your applications. The SDK helps with error handling and authentication, and provides features like automatic retries, pagination handling, and long-running operation management.

Because the agentic retrieval feature is on an allowlist, the SDK that you need to work with this feature is different from the generally available Discovery Engine client libraries.

To get the preview version of the Discovery Engine SDK, do the following:

  1. Contact [support](https://docs.cloud.google.com/support) to get access to the preview SDK Google Drive folder.

  2. Download the package for your language.




## API changes

Because this feature is on an allowlist, the API reference documentation on the [streaming answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/streamAnswer) method page doesn't show all the fields that are available and needed to use agentic retrieval with the stream answer method. The missing fields are documented as follows.

### Request body fields

  * `enableAgentInvocation` (boolean) — Set `true` to switch to agentic processing with existing search serving config. This field is optional if you are specifying an `answer_agent` serving config with a custom AI-mode app.

  * `reasoningEngine` (string) — The resource name of the [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) that hosts the agent sessions, formatted as `projects/*/locations/*/reasoningEngines/*`.




### Response fields

When agentic retrieval is enabled, each generated [`Answer.Reference`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.sessions.answers#reference) includes:

  * `queries` (repeated string) — The list of queries the agent issued in order to produce the reference.



#### Sessions service

The [Session service REST API](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.sessions) doesn't support the `create` or `update` methods. However, it does support the other methods: [`list`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.sessions/list), [`get`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.sessions/get), and [`delete`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.sessions/delete).

The [Session service RPC API](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#sessionservice) doesn't support the `Update` or the `Create` operations on session resources used for multi-turn conversations. However, it does support the other service: `List`, `Get`, and `Delete` operations on session resources used for multi-turn conversations.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
