---
url: https://docs.cloud.google.com/food-ai/ordering-integration/
title: Build a multimodal ordering experience using the streaming API \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:59.483710+00:00
---

# Build a multimodal ordering experience using the streaming API  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/ordering-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Guides ](https://docs.cloud.google.com/food-ai/concepts)



Send feedback 

#  Build a multimodal ordering experience using the streaming API Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides instructions and best practices for engineers building food ordering experiences with the `FoodOrderingService.BidiProcessOrder` RPC method. This real-time, bidirectional streaming API is the core of the Food Ordering AI Agent, enabling dynamic, conversational order-taking in various applications such as mobile apps, voice assistants, drive-thrus, and kiosks.

## Overview of BidiProcessOrder

The `BidiProcessOrder` method establishes a persistent, two-way communication channel between your client application and the Food Ordering AI Agent. Unlike standard unary request and response RPCs, this streaming approach allows for:

  * **Low-latency interaction:** Continuous exchange of information without the overhead of repeated HTTP requests.
  * **Multimodal input:** Handling of audio streams (for voice ordering), text inputs, and client-side events.
  * **Real-time responses:** The agent can send back audio, text, order updates, and other signals as the conversation unfolds.



`BidiProcessOrder` **cannot** be invoked using REST. Integrations must use a connection-oriented protocol:

  * **gRPC (Recommended):** Provides a robust and efficient framework for bidirectional streaming.
  * **WebSocket:** Suitable for clients or environments where gRPC isn't a fit due to programming language or network constraints.



Refer to the [BidiProcessOrder API Reference](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.FoodOrderingService.BidiProcessOrder) for detailed type definitions. WebSocket integrations use JSON representations of these types, as described in the WebSocket section.

## Prerequisites

Before integrating with `BidiProcessOrder`:

  1. **Enable the API:** Ensure the Food Ordering AI Agent API is enabled in your Google Cloud project. `bash gcloud services enable foodorderingaiagent.googleapis.com --project=PROJECT_ID`

  2. **Authentication:** Decide your authentication approach and setup any necessary service accounts and IAM roles, as described in Authentication.

  3. **Menu Ingestion:** A valid [Menu](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#menu) must be ingested and associated with a `Store`. See [Integrating Menu Data](https://docs.cloud.google.com/food-ai/menu-integration) for details.




## Authentication

To securely connect to the `BidiProcessOrder` RPC, your application must authenticate using a Google Cloud Service Account.

### 1\. Configure a Service Account

  * **Create a Service Account:** In your Google Cloud project, create a Service Account that your application will use to authenticate to the Food Ordering AI Agent API. See [Creating and managing service accounts](https://cloud.google.com/iam/docs/service-accounts-create).
  * **Grant IAM Roles:** Grant the necessary IAM roles to this service account. The primary role required to call `BidiProcessOrder` is:

    * **Food Ordering Agent User** (`roles/foodorderingaiagent.agentUser`): Allows the service account to connect to the ordering service and process sessions.

You can grant this role using the Google Cloud console or `gcloud`: `bash gcloud projects add-iam-policy-binding PROJECT_ID \ --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \ --role="roles/foodorderingaiagent.agentUser"`




### 2\. Application Authentication Flow

The exact authentication flow depends on your application architecture, especially whether the client application (e.g., mobile app, kiosk software) connects directly or through your own backend.

#### Common Scenario: Authenticating a consumer-facing client application

This is a typical pattern for mobile or web applications:

  1. **Client-to-YourAuth:** The end-user client app (mobile, web) authenticates with _your_ existing user authentication system (this could be Firebase Authentication, your own OAuth server, etc.).
  2. **Token Exchange:** The client app, after authenticating the user, requests a short-lived token from a secure backend service _you_ control (e.g., an "API Token Service").
  3. **Access Token Generation:** Your backend service, using the credentials of the Google Cloud Service Account principal configured in Step 1, generates a standard OAuth 2.0 access token for the `https://www.googleapis.com/auth/cloud-platform` scope. This can be done using the [Google Cloud Authentication client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

     * **Security:** Service account keys or credentials used to generate these tokens must be securely stored and managed on your backend. Never expose service account private keys directly to end-user client applications. See [Best practices for managing service account keys](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).
**Note:** The access token provided to clients **must** be associated with a principal with _minimal_ IAM permissions (i.e. _only_ the `Food Ordering AI Agent User` role). Public users can trivially abuse the access token to invoke arbitrary Google Cloud APIs on behalf of the service account, so it's critical that IAM is configured correctly to reject such calls.
  4. **Token to Client:** Your backend service returns the generated Google access token to the client app.

  5. **API Call:** The client app uses this Google access token to authenticate its gRPC or WebSocket connection to the `BidiProcessOrder` RPC.


**Tip:** If your `BidiProcessOrder` client runs in a secure environment that can be configured with service account credentials (such as Compute Engine, Google Kubernetes Engine, or your on-premise servers), it can use [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/application-default-credentials) to authenticate its calls to the Food Ordering AI Agent API. This guidance typically applies for use cases where audio and events are streamed from an on-premise edge server or a cloud-based application acting as a server-side proxy for browser-based clients.

### 3\. Using the Token

  * **gRPC:** The Google gRPC client libraries typically handle token refreshing and inclusion in the call metadata when provided with service account credentials.
  * **WebSocket (Non-Browser):** Include the token in the `Authorization: Bearer TOKEN` header.
  * **WebSocket (Browser):** As noted in the WebSocket section, direct browser WebSocket connections cannot use Authorization headers. A server-side streaming proxy is needed to authenticate your clients connection to Google Cloud.



## Connecting to the API

You can establish a stream using gRPC client libraries or a WebSocket connection.

### gRPC

Using gRPC is the recommended approach. You'll use the client libraries for your language of choice (e.g., Node.js) which are based on the [BidiProcessOrder API Reference](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.FoodOrderingService.BidiProcessOrder).

**Note:** The Google Cloud client libraries automatically authenticate using Application Default Credentials (ADC). If you have set up ADC in your environment, you do not need to manually generate or provide an OAuth 2.0 access token in your code; the client library handles token generation and refreshing for you during initialization.

The basic steps involve:

  1. Create a gRPC channel to the Food Ordering AI Agent API endpoint (e.g., `foodorderingaiagent.googleapis.com`).
  2. Obtain a client stub for `FoodOrderingService`.
  3. Invoke the `BidiProcessOrder` method, which returns a stream object for both sending requests and receiving responses.
  4. Implement business logic according to your use case which concurrently: 
     * Sends audio, text, and event input from the end user.
     * Handles messages from the agent including audio, text, and events.



### Node.js
    
    
    const {FoodOrderingServiceClient} = require('@google-cloud/foodorderingaiagent');
    
    const client = new FoodOrderingServiceClient();
    
    // The stream is initialized immediately. You can now write commands and attach listeners.
    
    const stream = client.bidiProcessOrder();
    
    

### WebSocket

For WebSocket connections, the URL path is:

`wss://foodorderingaiagent.googleapis.com/ws/google.cloud.foodorderingaiagent.v1beta.FoodOrderingService/BidiProcessOrder/locations/LOCATION`

  * `LOCATION`: e.g., `us`



**Required Headers:**

  * `Authorization`: `Bearer TOKEN` \- Where `TOKEN` is an OAuth 2.0 access token obtained for your service account.

**Note:** Web browsers **do not allow** JavaScript to set custom headers on WebSocket connection requests. Therefore, a WebSocket connection cannot be directly authenticated from within a browser. To securely integrate with the `BidiProcessOrder` API using WebSocket from a web application, you will need to use a server-side intermediary or proxy. This intermediary server can establish the WebSocket connection to the Food Ordering AI Agent API, including the necessary authentication headers, and then relay messages between the browser client and the API. See Authentication for more details about authentication options.

**Message Format:**

  * **Client to Server:** Messages sent to the API (e.g., `Config`, `AudioInput`, `TextInput`, `EventInput`) must be JSON representations of the `BidiProcessOrderRequest` proto, sent as `websocket.TextMessage`.
  * **Server to Client:** Messages received from the API (`BidiProcessOrderResponse`) will be sent as `websocket.BinaryMessage`, but the content of these binary messages is a JSON payload.
  * **Binary Data:** Binary data within the JSON payloads (e.g., `customerAudio` in `AudioInput`, `agentAudio` in `AgentAudio`) must be base64 encoded.



#### Node.js WebSocket Example

Here is an example of how to connect and interact with the API using WebSockets in Node.js with the `ws` library:
    
    
    const WebSocket = require('ws');
    
    // Replace with your actual values
    const location = 'LOCATION';
    const projectId = 'PROJECT_ID';
    const sessionId = 'SESSION_ID';
    const brandId = 'BRAND_ID';
    const storeId = 'STORE_ID';
    const token = 'OAUTH_TOKEN';
    
    const wsUrl = `wss://foodorderingaiagent.googleapis.com/ws/google.cloud.foodorderingaiagent.v1beta.FoodOrderingService/BidiProcessOrder/locations/${location}`;
    
    const ws = new WebSocket(wsUrl, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    
    ws.on('open', () => {
      console.log('Connected to WebSocket');
    
      // 1. Send the required initial Config message
      const configRequest = {
        config: {
          session: `projects/${projectId}/locations/${location}/sessions/${sessionId}`,
          store: `projects/${projectId}/locations/${location}/brands/${brandId}/stores/${storeId}`
        }
      };
    
      // Client-to-server messages are sent as TextMessage
      ws.send(JSON.stringify(configRequest));
      console.log('Sent Config message');
    });
    
    ws.on('message', (data, isBinary) => {
      // The documentation specifies that server-to-client messages
      // are sent as BinaryMessage containing a JSON payload.
      if (isBinary) {
        try {
          const response = JSON.parse(data.toString('utf8'));
          console.log('Received response:', response);
    
          if (response.agentText) {
            console.log(`Agent: ${response.agentText.text}`);
          }
    
          if (response.agentAudio) {
            const audioBytes = Buffer.from(response.agentAudio.agentAudio, 'base64');
            console.log(`Received ${audioBytes.length} bytes of agent audio.`);
            // Play or process the audio bytes here
          }
    
          if (response.endSession) {
            console.log('Session ended by agent.');
            ws.close();
          }
        } catch (e) {
          console.error('Failed to parse JSON response:', e);
        }
      }
    });
    
    ws.on('close', () => {
      console.log('Connection closed');
    });
    

## Session Lifecycle

Each call to `BidiProcessOrder` initiates a session. The session remains active as long as the stream is open.

### 1\. Initiation (Config Message)

  * Upon establishing the connection, the **first message** sent by the client **must** be a `BidiProcessOrderRequest` containing the [`Config`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#config) message.
  * **Required Fields in`Config`:**
    * `session`: A unique client-generated session identifier. Format: `projects/PROJECT/locations/LOCATION/sessions/SESSION_ID`.
    * `store`: The resource name of the `Store`. Format: `projects/PROJECT/locations/LOCATION/brands/BRAND/stores/STORE`. 
      * The agent uses the `store` to load the appropriate menu and configuration.
    * `mode` (Optional for `BidiProcessOrder`): Defaults to `HYBRID` (voice and text). Note that if you are using the unary REST or gRPC `ProcessOrder` API instead of `BidiProcessOrder`, `mode` must be explicitly set to `TEXT`.



### Node.js
    
    
    // Send the first message containing Config
    stream.write({
      config: {
        session: client.sessionPath(projectId, location, sessionId),
        store: client.storePath(projectId, location, brandId, storeId),
      }
    });
    

**Tip:** If the stream disconnects unexpectedly, you can resume the session by reconnecting and sending the _same_ `Config` message with the same `session` ID.

### 2\. Sending Inputs

  * After the initial `Config`, the client can send a stream of `BidiProcessOrderRequest` messages containing one of the following inputs: 
    * [`AudioInput`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#audioinput): Raw audio data (typically 16-bit linear PCM at 16000 Hz, no headers). Used for voice interactions.
    * [`TextInput`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#textinput): Text messages from the user.
    * [`EventInput`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#eventinput): Signals for events such as `DriveOffEvent` (for drive-thru use cases when the vehicle departs), `CrewInterjectionEvent` (for any situation wherein a human takes over the order taking role mid-conversation), or `OrderStateUpdateEvent` (if the order is modified on the client-side, e.g., using a touch interface).



### Node.js
    
    
    // Stream user inputs over the active connection
    stream.write({textInput: {text: 'Hi, I\'d like to order a cheeseburger.'}});
    

### 3\. Receiving Responses

  * Concurrently, the agent sends back a stream of `BidiProcessOrderResponse` messages. Your client must be prepared to handle various response types within the `oneof response` field: 
    * [`AgentAudio`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#agentaudio): Synthesized audio bytes to be played to the user, used for voice interactions.
    * [`AgentText`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#agenttext): Text version of the agent's response.
    * [`SpeechRecognition`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#speechrecognition): Transcript of the recognized user speech.
    * [`UpdatedOrderState`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#updatedorderstate): Contains the complete current state of the customer's [`Order`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#order) whenever it's updated by the agent. Use this to update your application's order representation. This should typically result in an update to a user interface or a system of record for order state information, such as a point of sale system.
    * [`InterruptionSignal`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#interruptionsignal): Indicates the user interrupted the agent's speech. The client should immediately stop playing any outgoing `AgentAudio`.
    * [`AgentEvent`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#agentevent): Special events, such as [`RestartOrder`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#restartorder), requiring client action.
    * [`SuggestedOptions`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#suggestedoptions): Provides contextually relevant options a user might select next, useful for display on a screen.
    * [`EndSession`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#endsession): Signals the session has been terminated by the agent (e.g., order complete, user drive-off, or agent escalation).



### Node.js
    
    
    // Attach event listeners to handle responses sequentially
    stream.on('data', (response) => {
      if (response.agentAudio) {
        console.log(`Received ${response.agentAudio.agentAudio.length} bytes of agent audio.`);
      } else if (response.agentText) {
        console.log(`Agent: ${response.agentText.text}`);
      } else if (response.speechRecognition) {
        console.log(`Recognized User Speech: ${response.speechRecognition.transcript}`);
      } else if (response.updatedOrderState) {
        console.log('Order updated.');
      } else if (response.interruptionSignal) {
        console.log('User interrupted the agent. Stop playing audio!');
      } else if (response.endSession) {
        console.log(`Session ended. Type: ${response.endSession.type}, Reason: ${response.endSession.reason}`);
        stream.end();
      }
    });
    
    stream.on('error', (err) => {
      console.error('Stream error:', err);
    });
    

### 4\. Closing the Stream

  * The stream can be closed by the client or the server. Typically, the server signals the end of a conversation using an `EndSession` message. The client should close the stream when this message is received.



## Handling Specific Message Types

The following sections describe how to handle specific response types that your client will receive when calling `BidiProcessOrder`.

### `AudioInput`

  * Stream audio in chunks as it becomes available.
  * Format: 16-bit linear PCM, 16000 Hz sample rate.
  * Audio chunks _do not_ include the audio headers that typically prefix a WAV file.
  * For drive-thru scenarios with echo cancellation enabled (`enable_echo_cancellation` in `Config`), provide both `customer_audio` and `crew_audio`.



### `UpdatedOrderState`

  * This message provides the _full_ state of the order each time it's sent. Replace any local cache of the order with the contents of the `Order` message received.
  * Use the `custom_integration_attributes` within the `Order` items and modifiers to map the `Order` content into equivalent entities within your application's system of record.



### `InterruptionSignal`

  * Upon receiving, immediately halt playback of any `AgentAudio` and clear any buffered agent audio. This ensures a natural conversational flow when the user interrupts the agent's speech.



### `EndSession`

  * Check the `EndType` (e.g., `DRIVE_OFF`, `AGENT_ESCALATION`).
  * Your application should gracefully close the connection and transition the user appropriately (e.g., notify a human supervisor in the case of `AGENT_ESCALATION`, or transition to an order confirmation state).



## Best Practices

  * **Handle Messages Asynchronously:** Minimize latency by using threads or non-blocking I/O to concurrently send requests and process incoming responses.
  * **Reconnection Logic:** Implement robust reconnection logic in case of network issues, remembering to send the initial `Config` message with the same session ID to attempt resumption.
  * **Error Handling:** Monitor the stream for errors. gRPC and WebSocket libraries provide mechanisms to detect stream closure or transport errors. Log these events and handle them gracefully.
  * **Audio Buffering:** Manage audio buffers carefully, implementing buffering if necessary, to ensure smooth playback of `AgentAudio` and timely delivery of `AudioInput`. Carefully consider the tradeoff between latency and playback quality when deciding your buffering scheme.
  * **Session ID Management:** Ensure session IDs are unique for each distinct order/conversation.
  * **Resource Management:** Close streams and release resources when the session is complete or if unrecoverable errors occur.
  * **Timeouts:** While the stream itself can be long-lived (up to 15 minutes by default), consider application-level timeouts for specific states if needed.



## Example Integration Flow (Conceptual)

  1. Client App (e.g., Mobile App) initiates an order.
  2. Establish gRPC/WebSocket connection to `BidiProcessOrder`.
  3. Send `BidiProcessOrderRequest` with `Config` (session ID, store ID).
  4. Receive initial `AgentAudio` (e.g., welcome message) and play it.
  5. User speaks: Capture audio, stream it in `AudioInput` messages.
  6. Receive `SpeechRecognition` (display transcript), `AgentAudio` (play response), and potentially `UpdatedOrderState` (update UI cart).
  7. If user interrupts, receive `InterruptionSignal`, stop playback.
  8. Continue exchange of audio or text inputs and agent responses.
  9. User confirms order: Agent sends final `UpdatedOrderState`.
  10. Agent sends `EndSession`: Client closes the stream and finalizes the order in the POS system using data from the last `UpdatedOrderState`.



## End-to-end Example

While the instructions above break down the streaming concepts piece-by-piece, here is what a complete end-to-end integration flow looks like.

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Food Ordering AI Agent quickstart using client libraries](https://docs.cloud.google.com/food-ai/quickstart-client-libraries). 

To authenticate to Food Ordering AI Agent, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {FoodOrderingServiceClient} = require('@google-cloud/foodorderingaiagent');
    
    async function bidiProcessOrderSample(projectId, location, brand, store, sessionId) {
      const client = new FoodOrderingServiceClient();
    
      // Create the resource names
      const sessionPath = client.sessionPath(projectId, location, sessionId);
      const storePath = client.storePath(projectId, location, brand, store);
    
      // Initialize the stream using gRPC. See the WebSocket section for the equivalent WebSocket implementation.
      const stream = client.bidiProcessOrder();
    
      // Attach event listeners to handle responses sequentially
      stream.on('data', (response) => {
        if (response.agentAudio) {
          console.log(`Received ${response.agentAudio.agentAudio.length} bytes of agent audio.`);
        } else if (response.agentText) {
          console.log(`Agent: ${response.agentText.text}`);
        } else if (response.speechRecognition) {
          console.log(`Recognized User Speech: ${response.speechRecognition.transcript}`);
        } else if (response.updatedOrderState) {
          console.log('Order updated.');
        } else if (response.interruptionSignal) {
          console.log('User interrupted the agent. Stop playing audio!');
        } else if (response.endSession) {
          console.log(`Session ended. Type: ${response.endSession.type}, Reason: ${response.endSession.reason}`);
          stream.end();
        }
      });
    
      stream.on('error', (err) => {
        console.error('Stream error:', err);
      });
    
      // 1. Send the first message containing Config
      stream.write({
        config: {
          session: sessionPath,
          store: storePath,
        }
      });
    
      // 2. Stream user inputs over the active connection
      stream.write({textInput: {text: 'Hi, I\'d like to order a cheeseburger.'}});
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
