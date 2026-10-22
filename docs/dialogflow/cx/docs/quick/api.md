---
url: https://docs.cloud.google.com/dialogflow/cx/docs/quick/api/
title: Interactions with the API \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:19.612989+00:00
---

# Interactions with the API  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/quick/api/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Interactions with the API Stay organized with collections  Save and categorize content based on your preferences. 

For each conversational turn, an _interaction_ takes place. During an interaction, an end-user sends input to Dialogflow CX, and Dialogflow CX sends a response. You have two options when implementing your system to handle interactions: using the API or using an integration.

When using the API, your system needs to handle the following:

  * Build an agent.
  * Provide a user interface for end-users.
  * Call the Dialogflow API for each conversational turn to send end-user input to the API.
  * Unless your agent responses are purely static (uncommon), you need to host a [webhook service](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) to handle webhook-enabled [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment).



When using an [integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration), your system only needs to handle the following:

  * Build an agent.
  * Optionally implement a webhook service.



The following diagram shows the steps that take place for one conversational turn of a session.

**Note:** Communications between your systems and integrations, and Dialogflow CX are [encrypted in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit). Also, Google internal component communications are encrypted using [Application Layer Transport Security (ALTS)](https://docs.cloud.google.com/docs/security/encryption-in-transit/application-layer-transport-security).

![API flow diagram.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-interaction-sequence.svg)

  1. The end-user types or says something, known as _end-user input_.
  2. Your user interface or integration system receives the input and forwards it to the Dialogflow API in a detect intent request.
  3. The Dialogflow API receives the detect intent request. It matches the input to an intent or form parameter, sets parameters as needed, and updates session state. If it needs to call a webhook-enabled fulfillment, it sends a webhook request to your webhook service, otherwise, go to step 6.
  4. Your webhook service receives the webhook request. Your service takes any actions necessary, like calling external APIs, querying or updating a database, etc.
  5. Your webhook service builds a response and sends a webhook response back to Dialogflow CX.
  6. Dialogflow CX creates a detect intent response. If a webhook was called, it uses the response provided in the webhook response. If no webhook was called, it uses the static response defined in the agent. Dialogflow CX sends a detect intent response to your user interface or integration system.
  7. Your user interface or integration system receives the detect intent response and forwards the text or audio response to the end-user.
  8. The end-user sees or hears the response.



## Purpose

Learn how to call the API for one conversation turn for an agent without using an integration. This guide doesn't show you how to implement a user interface for your end-user.

## Before you begin

Before you read this guide, do the following:

  * Read [flow basics](https://docs.cloud.google.com/dialogflow/cx/docs/basics).
  * Perform [setup steps](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup).
  * Create an agent or continue using the agent you created in [Build an agent using flows](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent) or [Build an agent using playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent-playbook).



## Collect IDs

The following samples require several IDs as input. Find your project ID, region ID, and agent ID by using one of these methods:

###  Dialogflow CX console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project.
  3. Click the option _more_vert_ menu for an agent in the list.
  4. Click the copy name _filter_none_ button.
  5. This copies the full identifying name of your agent, which includes your project ID, region ID, and agent ID in the form:  
projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID



###  Generative AI App Builder 

  1. Go to the Generative AI App Builder:

[Generative AI App Builder](https://console.cloud.google.com/gen-app-builder/)

  2. Your project ID is shown at the top of the console.

  3. The **Location** column shows region IDs.

  4. Select an app.

  5. The browser URL path segment after `agents/` contains the agent app ID.




You also need a session ID. A [session](https://docs.cloud.google.com/dialogflow/cx/docs/concept/session) represents a conversation between a Dialogflow CX agent and an end-user. Create a unique session ID at the beginning of a conversation and use it for each turn of the conversation. To test the API, you can use any string ID that is at most 36 bytes, such as `test-session-123`.

## Call detect intent

The following samples call the `Sessions.detectIntent` method. Go to the Session API reference

**Select a protocol and version for the Session reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions) |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.sessions)  
RPC |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Sessions) |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Sessions)  
C++ |  [SessionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1SessionsClient.html) |  Not available   
C# |  [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient) |  Not available   
Go |  [SessionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_SessionsClient) |  Not available   
Java |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SessionsClient)  
Node.js |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.SessionsClient.html) |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.SessionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.sessions.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.sessions.SessionsClient)  
Ruby |  Not available  |  Not available   
  
Close

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * AGENT_ID: your agent ID
  * REGION_ID: your [region ID](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)
  * SESSION_ID: your [session ID](https://docs.cloud.google.com/dialogflow/cx/docs/concept/session)
  * END_USER_INPUT: the end-user input



HTTP method and URL: 
    
    
    POST https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/sessions/SESSION_ID:detectIntent

Request JSON body: 
    
    
    {
      "queryInput": {
        "text": {
          "text": "END_USER_INPUT"
        },
        "languageCode": "en"
      },
      "queryParams": {
        "timeZone": "America/Los_Angeles"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/sessions/SESSION_ID:detectIntent"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/sessions/SESSION_ID:detectIntent" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "responseId": "38e8f23d-eed2-445e-a3e7-149b242dd669",
      "queryResult": {
        "text": "I want to buy a shirt",
        "languageCode": "en",
        "responseMessages": [
          {
            "text": {
              "text": [
                "Ok, let's start a new order."
              ]
            }
          },
          {
            "text": {
              "text": [
                "I'd like to collect a bit more information from you."
              ]
            }
          },
          {
            "text": {
              "text": [
                "What color would you like?"
              ]
            }
          },
          {}
        ],
        "currentPage": {
          "name": "projects/PROJECT_ID/locations/us-central1/agents/133b0350-f2d2-4928-b0b3-5b332259d0f7/flows/00000000-0000-0000-0000-000000000000/pages/ce0b88c4-9292-455c-9c59-ec153dad94cc",
          "displayName": "New Order"
        },
        "intent": {
          "name": "projects/PROJECT_ID/locations/us-central1/agents/133b0350-f2d2-4928-b0b3-5b332259d0f7/intents/0adebb70-a727-4687-b8bc-fbbc2ac0b665",
          "displayName": "order.new"
        },
        "intentDetectionConfidence": 1,
        "diagnosticInfo": { ... },
        "match": {
          "intent": {
            "name": "projects/PROJECT_ID/locations/us-central1/agents/133b0350-f2d2-4928-b0b3-5b332259d0f7/intents/0adebb70-a727-4687-b8bc-fbbc2ac0b665",
            "displayName": "order.new"
          },
          "resolvedInput": "I want to buy a shirt",
          "matchType": "INTENT",
          "confidence": 1
        }
      }
    }
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.cx.v3beta1.DetectIntentRequest;
    import com.google.cloud.dialogflow.cx.v3beta1.DetectIntentResponse;
    import com.google.cloud.dialogflow.cx.v3beta1.QueryInput;
    import com.google.cloud.dialogflow.cx.v3beta1.QueryResult;
    import com.google.cloud.dialogflow.cx.v3beta1.SessionName;
    import com.google.cloud.dialogflow.cx.v3beta1.SessionsClient;
    import com.google.cloud.dialogflow.cx.v3beta1.SessionsSettings;
    import com.google.cloud.dialogflow.cx.v3beta1.TextInput;
    import com.google.common.collect.Maps;
    import java.io.IOException;
    import java.util.List;
    import java.util.Map;
    
    public class DetectIntent {
    
      // DialogFlow API Detect Intent sample with text inputs.
      public static Map<String, QueryResult> detectIntent(
          String projectId,
          String locationId,
          String agentId,
          String sessionId,
          List<String> texts,
          String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        SessionsSettings.Builder sessionsSettingsBuilder = SessionsSettings.newBuilder();
        if (locationId.[equals](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html#com_google_api_gax_rpc_UnaryCallSettings_equals__org_jspecify_annotations_Nullable_java_lang_Object_)("global")) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        SessionsSettings sessionsSettings = sessionsSettingsBuilder.build();
    
        Map<String, QueryResult> queryResults = Maps.newHashMap();
        // Instantiates a client.
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try (SessionsClient sessionsClient = SessionsClient.create(sessionsSettings)) {
          // Set the session name using the projectID (my-project-id), locationID (global), agentID
          // (UUID), and sessionId (UUID).
          SessionName session =
              SessionName.ofProjectLocationAgentSessionName(projectId, locationId, agentId, sessionId);
    
          // TODO : Uncomment if you want to print session path
          // System.out.println("Session Path: " + session.toString());
    
          // Detect intents for each text input.
          for (String text : texts) {
            // Set the text (hello) for the query.
            TextInput.Builder textInput = TextInput.newBuilder().setText(text);
    
            // Build the query with the TextInput and language code (en-US).
            QueryInput queryInput =
                QueryInput.newBuilder().setText(textInput).setLanguageCode(languageCode).build();
    
            // Build the DetectIntentRequest with the SessionName and QueryInput.
            DetectIntentRequest request =
                DetectIntentRequest.newBuilder()
                    .setSession(session.toString())
                    .setQueryInput(queryInput)
                    .build();
    
            // Performs the detect intent request.
            DetectIntentResponse response = sessionsClient.detectIntent(request);
    
            // Display the query result.
            QueryResult queryResult = response.getQueryResult();
    
            // TODO : Uncomment if you want to print queryResult
            // System.out.println("====================");
            // System.out.format("Query Text: '%s'\n", queryResult.getText());
            // System.out.format(
            //     "Detected Intent: %s (confidence: %f)\n",
            //     queryResult.getIntent().getDisplayName(),
            //         queryResult.getIntentDetectionConfidence());
    
            queryResults.put(text, queryResult);
          }
        }
        return queryResults;
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const location = 'global';
    // const agentId = 'my-agent';
    // const query = 'Hello';
    // const languageCode = 'en'
    
    // Imports the Google Cloud Some API library
    const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    /**
     * Example for regional endpoint:
     *   const location = 'us-central1'
     *   const client = new SessionsClient({apiEndpoint: 'us-central1-dialogflow.googleapis.com'})
     */
    const client = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    async function detectIntentText() {
      const sessionId = Math.random().toString(36).substring(7);
      const sessionPath = client.projectLocationAgentSessionPath(
        projectId,
        location,
        agentId,
        sessionId
      );
      const request = {
        session: sessionPath,
        queryInput: {
          text: {
            text: query,
          },
          languageCode,
        },
      };
      const [response] = await client.detectIntent(request);
      for (const message of response.queryResult.responseMessages) {
        if (message.text) {
          console.log(`Agent Response: ${message.text.text}`);
        }
      }
      if (response.queryResult.match.intent) {
        console.log(
          `Matched Intent: ${response.queryResult.match.intent.displayName}`
        );
      }
      console.log(
        `Current Page: ${response.queryResult.currentPage.displayName}`
      );
    }
    
    detectIntentText();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def run_sample():
        # TODO(developer): Replace these values when running the function
        project_id = "YOUR-PROJECT-ID"
        # For more information about regionalization see https://cloud.google.com/dialogflow/cx/docs/how/region
        location_id = "YOUR-LOCATION-ID"
        # For more info on agents see https://cloud.google.com/dialogflow/cx/docs/concept/agent
        agent_id = "YOUR-AGENT-ID"
        agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
        # For more information on sessions see https://cloud.google.com/dialogflow/cx/docs/concept/session
        session_id = uuid.uuid4()
        texts = ["Hello"]
        # For more supported languages see https://cloud.google.com/dialogflow/es/docs/reference/language
        language_code = "en-us"
    
        detect_intent_texts(agent, session_id, texts, language_code)
    
    
    def detect_intent_texts(agent, session_id, texts, language_code):
        """Returns the result of detect intent with texts as inputs.
    
        Using the same `session_id` between requests allows continuation
        of the conversation."""
        session_path = f"{agent}/sessions/{session_id}"
        print(f"Session path: {session_path}\n")
        client_options = None
        agent_components = AgentsClient.parse_agent_path(agent)
        location_id = agent_components["location"]
        if location_id != "global":
            api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        session_client = SessionsClient(client_options=client_options)
    
        for text in texts:
            text_input = session.TextInput(text=text)
            query_input = session.QueryInput(text=text_input, language_code=language_code)
            request = session.DetectIntentRequest(
                session=session_path, query_input=query_input
            )
            response = session_client.detect_intent(request=request)
    
            print("=" * 20)
            print(f"Query text: {response.query_result.text}")
            response_messages = [
                " ".join(msg.text.text) for msg in response.query_result.response_messages
            ]
            print(f"Response text: {' '.join(response_messages)}\n")
    
    

## Production

Before running your agent in production, follow the [Production best practices](https://docs.cloud.google.com/dialogflow/cx/docs/concept/best-practices#prod).

[ Previous arrow_back  Interactions with an integration  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/integration)

[ Next Important terms  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/important-terms)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
