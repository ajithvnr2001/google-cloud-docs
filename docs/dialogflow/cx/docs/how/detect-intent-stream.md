---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/detect-intent-stream/
title: Detect intent \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:58.223347+00:00
---

# Detect intent  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/detect-intent-stream/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Detect intent Stay organized with collections  Save and categorize content based on your preferences. 

There are basic samples that show how to detect intent in the [quickstart](https://docs.cloud.google.com/dialogflow/cx/docs/quick/api#detect-intent). This guide provides additional samples for advanced scenarios.

## Detect intent with audio input

The following samples show how to detect intent with audio input.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.cx.v3.[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioEncoding.html);
    import com.google.cloud.dialogflow.cx.v3.[AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.cx.v3.[InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    
    public class DetectIntentAudioInput {
    
      // DialogFlow API Detect Intent sample with Audio input.
      public static void main(String[] args) throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        /** TODO (developer): replace these values with your own values */
        String projectId = "my-project-id";
        String locationId = "global";
        String agentId = "my-agent-id";
        String audioFileName = "resources/book_a_room.wav";
        int sampleRateHertz = 16000;
        /*
         * A session ID is a string of at most 36 bytes in size.
         * Your system is responsible for generating unique session IDs.
         * They can be random numbers, hashed end-user identifiers,
         * or any other values that are convenient for you to generate.
         */
        String sessionId = "my-UUID";
        String languageCode = "en";
    
        detectIntent(
            projectId, locationId, agentId, audioFileName, sampleRateHertz, sessionId, languageCode);
      }
    
      public static void detectIntent(
          String projectId,
          String locationId,
          String agentId,
          String audioFileName,
          int sampleRateHertz,
          String sessionId,
          String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
    
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).Builder sessionsSettingsBuilder = [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).newBuilder();
        if (locationId.equals("global")) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html) sessionsSettings = sessionsSettingsBuilder.build();
    
        // Instantiates a client by setting the session name.
        // Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>`
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html).create(sessionsSettings)) {
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html) session =
              [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html).[ofProjectLocationAgentSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_ofProjectLocationAgentSessionName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, agentId, sessionId);
    
          // TODO : Uncomment if you want to print session path
          // System.out.println("Session Path: " + session.toString());
          [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html) inputAudioConfig =
              [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html).newBuilder()
                  .setAudioEncoding([AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioEncoding.html).AUDIO_ENCODING_LINEAR_16)
                  .setSampleRateHertz(sampleRateHertz)
                  .build();
    
          try (FileInputStream audioStream = new FileInputStream(audioFileName)) {
            // Subsequent requests must **only** contain the audio data.
            // Following messages: audio chunks. We just read the file in fixed-size chunks. In reality
            // you would split the user input by time.
            byte[] buffer = new byte[4096];
            int bytes = audioStream.read(buffer);
            [AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html) audioInput =
                [AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html).newBuilder()
                    .setAudio([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(buffer, 0, bytes))
                    .[setConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.Builder.html#com_google_cloud_dialogflow_cx_v3_AudioInput_Builder_setConfig_com_google_cloud_dialogflow_cx_v3_InputAudioConfig_)(inputAudioConfig)
                    .build();
            [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html) queryInput =
                [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html).newBuilder()
                    .setAudio(audioInput)
                    .setLanguageCode("en-US") // languageCode = "en-US"
                    .build();
    
            [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html) request =
                [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html).newBuilder()
                    .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_toString__)())
                    .setQueryInput(queryInput)
                    .build();
    
            // Performs the detect intent request.
            [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html) response = sessionsClient.detectIntent(request);
    
            // Display the query result.
            [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html) queryResult = response.[getQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html#com_google_cloud_dialogflow_cx_v3_DetectIntentResponse_getQueryResult__)();
    
            System.out.println("====================");
            System.out.format(
                "Detected Intent: %s (confidence: %f)\n",
                queryResult.[getTranscript](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html#com_google_cloud_dialogflow_cx_v3_QueryResult_getTranscript__)(), queryResult.[getIntentDetectionConfidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html#com_google_cloud_dialogflow_cx_v3_QueryResult_getIntentDetectionConfidence__)());
          }
        }
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
    // const audioFileName = '/path/to/audio.raw';
    // const encoding = 'AUDIO_ENCODING_LINEAR_16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'en'
    
    // Imports the Google Cloud Some API library
    const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    /**
     * Example for regional endpoint:
     *   const location = 'us-central1'
     *   const client = new SessionsClient({apiEndpoint: 'us-central1-dialogflow.googleapis.com'})
     */
    const client = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    const fs = require('fs');
    const util = require('util');
    
    async function detectIntentAudio() {
      const sessionId = Math.random().toString(36).substring(7);
      const sessionPath = client.projectLocationAgentSessionPath(
        projectId,
        location,
        agentId,
        sessionId
      );
      console.info(sessionPath);
    
      // Read the content of the audio file and send it as part of the request.
      const readFile = util.promisify(fs.readFile);
      const inputAudio = await readFile(audioFileName);
    
      const request = {
        session: sessionPath,
        queryInput: {
          audio: {
            config: {
              audioEncoding: encoding,
              sampleRateHertz: sampleRateHertz,
            },
            audio: inputAudio,
          },
          languageCode,
        },
      };
      const [response] = await client.detectIntent(request);
      console.log(`User Query: ${response.queryResult.transcript}`);
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
    
    detectIntentAudio();

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
        session_id = str(uuid.uuid4())
        audio_file_path = "YOUR-AUDIO-FILE-PATH"
        # For more supported languages see https://cloud.google.com/dialogflow/es/docs/reference/language
        language_code = "en-us"
    
        detect_intent_audio(agent, session_id, audio_file_path, language_code)
    
    
    def detect_intent_audio(agent, session_id, audio_file_path, language_code):
        """Returns the result of detect intent with an audio file as input.
    
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
    
        input_audio_config = audio_config.InputAudioConfig(
            audio_encoding=audio_config.AudioEncoding.AUDIO_ENCODING_LINEAR_16,
            sample_rate_hertz=24000,
        )
    
        with open(audio_file_path, "rb") as audio_file:
            input_audio = audio_file.read()
    
        audio_input = session.AudioInput(config=input_audio_config, audio=input_audio)
        query_input = session.QueryInput(audio=audio_input, language_code=language_code)
        request = session.DetectIntentRequest(session=session_path, query_input=query_input)
        response = session_client.detect_intent(request=request)
    
        print("=" * 20)
        print(f"Query text: {response.query_result.transcript}")
        response_messages = [
            " ".join(msg.text.text) for msg in response.query_result.response_messages
        ]
        print(f"Response text: {' '.join(response_messages)}\n")
    
    

## Detect intent with event invocation

The following samples show how to detect intent with event invocation.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.cx.v3.[EventInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EventInput.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html);
    import java.io.IOException;
    
    public class DetectIntentEventInput {
    
      // DialogFlow API Detect Intent sample with Event input.
      public static void main(String[] args) throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        String projectId = "my-project-id";
        String locationId = "global";
        String agentId = "my-agent-id";
        String sessionId = "my-UUID";
        String event = "my-event-id";
        String languageCode = "en";
    
        detectIntent(projectId, locationId, agentId, sessionId, event, languageCode);
      }
    
      public static void detectIntent(
          String projectId,
          String locationId,
          String agentId,
          String sessionId,
          String event,
          String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
    
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).Builder sessionsSettingsBuilder = [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).newBuilder();
        if (locationId.equals("global")) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html) sessionsSettings = sessionsSettingsBuilder.build();
    
        // Instantiates a client by setting the session name.
        // Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>`
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html).create(sessionsSettings)) {
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html) session =
              [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html).[ofProjectLocationAgentSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_ofProjectLocationAgentSessionName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, agentId, sessionId);
    
          // TODO : Uncomment if you want to print session path
          // System.out.println("Session Path: " + session.toString());
    
          [EventInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EventInput.html).Builder eventInput = [EventInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EventInput.html).newBuilder().setEvent(event);
    
          // Build the query with the EventInput and language code (en-US).
          [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html) queryInput =
              [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html).newBuilder().setEvent(eventInput).setLanguageCode(languageCode).build();
    
          // Build the DetectIntentRequest with the SessionName and QueryInput.
          [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html) request =
              [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html).newBuilder()
                  .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_toString__)())
                  .setQueryInput(queryInput)
                  .build();
    
          // Performs the detect intent request.
          [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html) response = sessionsClient.detectIntent(request);
    
          // Display the query result.
          [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html) queryResult = response.[getQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html#com_google_cloud_dialogflow_cx_v3_DetectIntentResponse_getQueryResult__)();
    
          // TODO : Uncomment if you want to print queryResult
          System.out.println("====================");
          System.out.format("Triggering Event: %s \n", queryResult.[getTriggerEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html#com_google_cloud_dialogflow_cx_v3_QueryResult_getTriggerEvent__)());
        }
      }
    }
    

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The name of the session this query is sent to.
     *  Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
     *  ID>/sessions/<Session ID>` or `projects/<Project ID>/locations/<Location
     *  ID>/agents/<Agent ID>/environments/<Environment ID>/sessions/<Session ID>`.
     *  If `Environment ID` is not specified, we assume default 'draft'
     *  environment.
     *  It's up to the API caller to choose an appropriate `Session ID`. It can be
     *  a random number or some type of session identifiers (preferably hashed).
     *  The length of the `Session ID` must not exceed 36 characters.
     *  For more information, see the sessions
     *  guide (https://cloud.google.com/dialogflow/cx/docs/concept/session).
     *  Note: Always use agent versions for production traffic.
     *  See Versions and
     *  environments (https://cloud.google.com/dialogflow/cx/docs/concept/version).
     */
    
    /**
     * Optional. The parameters of this query.
     */
    // const queryParams = {}
    /**
     *  Required. The input specification. See https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ConversationTurn#QueryInput for information about query inputs.
     */
    // const event = 'name-of-event-to-trigger';
    
    // Imports the Cx library
    const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    /**
     * Example for regional endpoint:
     *   const location = 'us-central1'
     *   const client = new SessionsClient({apiEndpoint: 'us-central1-dialogflow.googleapis.com'})
     */
    // Instantiates a client
    const cxClient = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    async function detectIntentWithEventInput() {
      const sessionId = Math.random().toString(36).substring(7);
      const sessionPath = cxClient.projectLocationAgentSessionPath(
        projectId,
        location,
        agentId,
        sessionId
      );
    
      // Construct detect intent request
      const request = {
        session: sessionPath,
        queryInput: {
          event: {
            event: event,
          },
          languageCode,
        },
      };
    
      // Send request and receive response
      const [response] = await cxClient.detectIntent(request);
      console.log(`Event Name: ${event}`);
    
      // Response message from the triggered event
      console.log('Agent Response: \n');
      console.log(response.queryResult.responseMessages[0].text.text[0]);
    }
    
    detectIntentWithEventInput();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import uuid
    
    from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
    from google.cloud.dialogflowcx_v3.types import session
    
    
    def run_sample():
        # TODO(developer): Update these values when running the function
        # project_id = "YOUR-PROJECT-ID"
        # location = "YOUR-LOCATION-ID"
        # agent_id = "YOUR-AGENT-ID"
        # event = "YOUR-EVENT"
        # language_code = "YOUR-LANGUAGE-CODE"
    
        project_id = "dialogflow-cx-demo-1-348717"
        location = "global"
        agent_id = "8caa6b47-5dd7-4380-b86e-ea4301d565b0"
        event = "sys.no-match-default"
        language_code = "en-us"
    
        detect_intent_with_event_input(
            project_id,
            location,
            agent_id,
            event,
            language_code,
        )
    
    
    def detect_intent_with_event_input(
        project_id,
        location,
        agent_id,
        event,
        language_code,
    ):
        """Detects intent using EventInput"""
        client_options = None
        if location != "global":
            api_endpoint = f"{location}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        session_client = SessionsClient(client_options=client_options)
        session_id = str(uuid.uuid4())
        session_path = session_client.session_path(
            project=project_id,
            location=location,
            agent=agent_id,
            session=session_id,
        )
    
        # Construct detect intent request:
        event = session.EventInput(event=event)
        query_input = session.QueryInput(event=event, language_code=language_code)
        request = session.DetectIntentRequest(
            session=session_path,
            query_input=query_input,
        )
    
        response = session_client.detect_intent(request=request)
        response_text = response.query_result.response_messages[0].text.text[0]
        print(f"Response: {response_text}")
        return response_text
    
    

## Detect intent with caller-triggered intent match

The following samples show how to detect intent with a caller-triggered intent match.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.cx.v3.[IntentInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentInput.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html);
    import java.io.IOException;
    
    public class DetectIntentIntentInput {
    
      // DialogFlow API Detect Intent sample with Intent input.
      public static void main(String[] args) throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        String projectId = "my-project-id";
        String locationId = "global";
        String agentId = "my-agent-id";
        String sessionId = "my-UUID";
        String intent = "my-intent-id";
        String languageCode = "en";
    
        detectIntent(projectId, locationId, agentId, sessionId, intent, languageCode);
      }
    
      public static void detectIntent(
          String projectId,
          String locationId,
          String agentId,
          String sessionId,
          String intent,
          String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
    
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).Builder sessionsSettingsBuilder = [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).newBuilder();
        if (locationId.equals("global")) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html) sessionsSettings = sessionsSettingsBuilder.build();
    
        // Instantiates a client by setting the session name.
        // Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>`
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html).create(sessionsSettings)) {
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html) session =
              [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html).[ofProjectLocationAgentSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_ofProjectLocationAgentSessionName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, agentId, sessionId);
    
          // TODO : Uncomment if you want to print session path
          // System.out.println("Session Path: " + session.toString());
    
          [IntentInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentInput.html).Builder intentInput = [IntentInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentInput.html).newBuilder().setIntent(intent);
    
          // Build the query with the IntentInput and language code (en-US).
          [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html) queryInput =
              [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html).newBuilder().setIntent(intentInput).setLanguageCode(languageCode).build();
    
          // Build the DetectIntentRequest with the SessionName and QueryInput.
          [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html) request =
              [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html).newBuilder()
                  .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_toString__)())
                  .setQueryInput(queryInput)
                  .build();
    
          // Performs the detect intent request.
          [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html) response = sessionsClient.detectIntent(request);
    
          // Display the query result.
          [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html) queryResult = response.[getQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html#com_google_cloud_dialogflow_cx_v3_DetectIntentResponse_getQueryResult__)();
    
          // TODO : Uncomment if you want to print queryResult
          System.out.println("====================");
          System.out.format(
              "Detected Intent: %s (confidence: %f)\n",
              queryResult.[getIntent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html#com_google_cloud_dialogflow_cx_v3_QueryResult_getIntent__)().getDisplayName(), queryResult.[getIntentDetectionConfidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html#com_google_cloud_dialogflow_cx_v3_QueryResult_getIntentDetectionConfidence__)());
        }
      }
    }
    

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    
    /**
     * const projectId = 'your-project-id';
     * const location = 'location';
     * const agentId = 'your-agent-id';
     * const languageCode = 'your-language-code';
     */
    
    /**
     * The input specification. See https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ConversationTurn#QueryInput for information about query inputs.
     */
    // const intentId = 'unique-identifier-of-the-intent-to-trigger';
    
    // Imports the Cx library
    const {
      SessionsClient,
      IntentsClient,
    } = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    /**
     * Example for regional endpoint:
     *   const location = 'us-central1'
     *   const client = new SessionsClient({apiEndpoint: 'us-central1-dialogflow.googleapis.com'})
     */
    // Instantiates a Sessions client
    const sessionsClient = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    // Instantiates an Intents client
    const intentsClient = new [IntentsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    async function detectIntentWithIntentInput() {
      const sessionId = Math.random().toString(36).substring(7);
    
      // Creates session path
      const sessionPath = sessionsClient.projectLocationAgentSessionPath(
        projectId,
        location,
        agentId,
        sessionId
      );
    
      // Creates intent path. Format: projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/intents/<Intent ID>
      const intentPath = intentsClient.intentPath(
        projectId,
        location,
        agentId,
        intentId
      );
    
      // Construct detectIntent request
      const request = {
        session: sessionPath,
        queryInput: {
          intent: {
            intent: intentPath,
          },
          languageCode,
        },
      };
    
      // Send request and receive response
      const [response] = await sessionsClient.detectIntent(request);
    
      // Display the name of the detected intent
      console.log('Intent Name: \n');
      console.log(response.queryResult.intent.displayName);
    
      // Agent responds with fulfillment message of the detected intent
      console.log('Agent Response: \n');
      console.log(response.queryResult.responseMessages[0].text.text[0]);
    }
    
    detectIntentWithIntentInput();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import uuid
    
    from google.cloud.dialogflowcx_v3.services.intents import IntentsClient
    from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
    from google.cloud.dialogflowcx_v3.types import session
    
    
    def run_sample():
        # TODO(developer): Update these values when running the function
        project_id = "YOUR-PROJECT-ID"
        location = "YOUR-LOCATION-ID"
        agent_id = "YOUR-AGENT-ID"
        intent_id = "YOUR-INTENT-ID"
        language_code = "en-us"
    
        detect_intent_with_intent_input(
            project_id,
            location,
            agent_id,
            intent_id,
            language_code,
        )
    
    
    def detect_intent_with_intent_input(
        project_id,
        location,
        agent_id,
        intent_id,
        language_code,
    ):
        """Returns the result of detect intent with sentiment analysis"""
        client_options = None
        if location != "global":
            api_endpoint = f"{location}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        session_client = SessionsClient(client_options=client_options)
        session_id = str(uuid.uuid4())
        intents_client = IntentsClient()
    
        session_path = session_client.session_path(
            project=project_id,
            location=location,
            agent=agent_id,
            session=session_id,
        )
        intent_path = intents_client.intent_path(
            project=project_id,
            location=location,
            agent=agent_id,
            intent=intent_id,
        )
    
        intent = session.IntentInput(intent=intent_path)
        query_input = session.QueryInput(intent=intent, language_code=language_code)
        request = session.DetectIntentRequest(
            session=session_path,
            query_input=query_input,
        )
    
        response = session_client.detect_intent(request=request)
        response_text = []
        for response_message in response.query_result.response_messages:
            response_text.append(response_message.text.text)
            print(response_message.text.text)
        return response_text
    
    

## Detect intent with sentiment analysis enabled

The following samples show how to detect intent with sentiment analysis enabled.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html);
    import com.google.cloud.dialogflow.cx.v3.[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TextInput.html);
    import com.google.common.collect.Maps;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Map;
    
    public class DetectIntentSentimentAnalysis {
    
      public static void main(String[] args) throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        String projectId = "my-project-id";
        String locationId = "global";
        String agentId = "my-agent-id";
        String sessionId = "my-UUID";
        List<String> texts = new ArrayList<>(List.of("my-list", "of-texts"));
        String languageCode = "en";
    
        detectIntent(projectId, locationId, agentId, sessionId, texts, languageCode);
      }
    
      // DialogFlow API Detect Intent sample with sentiment analysis.
      public static Map<String, QueryResult> detectIntent(
          String projectId,
          String locationId,
          String agentId,
          String sessionId,
          List<String> texts,
          String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).Builder sessionsSettingsBuilder = [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).newBuilder();
        if (locationId.equals("global")) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html) sessionsSettings = sessionsSettingsBuilder.build();
    
        Map<String, QueryResult> queryResults = Maps.newHashMap();
    
        // Instantiates a client by setting the session name.
        // Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>`
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html).create(sessionsSettings)) {
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html) session =
              [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html).[ofProjectLocationAgentSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_ofProjectLocationAgentSessionName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, agentId, sessionId);
    
          // TODO : Uncomment if you want to print session path
          // System.out.println("Session Path: " + session.toString());
    
          // Detect intents for each text input.
          for (String text : texts) {
            // Set the text (hello) for the query.
            [TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TextInput.html).Builder textInput = [TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TextInput.html).newBuilder().setText(text);
    
            // Build the query with the TextInput and language code (en-US).
            [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html) queryInput =
                [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html).newBuilder().setText(textInput).setLanguageCode(languageCode).build();
    
            // Build the query parameters to analyze the sentiment of the query.
            [QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.html) queryParameters =
                [QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.html).newBuilder().[setAnalyzeQueryTextSentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.Builder.html#com_google_cloud_dialogflow_cx_v3_QueryParameters_Builder_setAnalyzeQueryTextSentiment_boolean_)(true).build();
    
            // Build the DetectIntentRequest with the SessionName, QueryInput, and QueryParameters.
            [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html) request =
                [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html).newBuilder()
                    .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_toString__)())
                    .setQueryInput(queryInput)
                    .setQueryParams(queryParameters)
                    .build();
    
            // Performs the detect intent request.
            [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html) response = sessionsClient.detectIntent(request);
    
            // Display the query result.
            [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html) queryResult = response.[getQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html#com_google_cloud_dialogflow_cx_v3_DetectIntentResponse_getQueryResult__)();
    
            // TODO : Uncomment if you want to print queryResult
            // System.out.println("====================");
            // SentimentAnalysisResult sentimentAnalysisResult =
            //     queryResult.getSentimentAnalysisResult();
            // Float score = sentimentAnalysisResult.getScore();
    
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
    /**
     *  Required. The name of the session this query is sent to.
     *  Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
     *  ID>/sessions/<Session ID>` or `projects/<Project ID>/locations/<Location
     *  ID>/agents/<Agent ID>/environments/<Environment ID>/sessions/<Session ID>`.
     *  If `Environment ID` is not specified, we assume default 'draft'
     *  environment.
     *  It's up to the API caller to choose an appropriate `Session ID`. It can be
     *  a random number or some type of session identifiers (preferably hashed).
     *  The length of the `Session ID` must not exceed 36 characters.
     *  For more information, see the sessions
     *  guide (https://cloud.google.com/dialogflow/cx/docs/concept/session).
     *  Note: Always use agent versions for production traffic.
     *  See Versions and
     *  environments (https://cloud.google.com/dialogflow/cx/docs/concept/version).
     */
    
    /**
     * Optional. The parameters of this query.
     */
    // const queryParams = {}
    /**
     *  Required. The input specification. See https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ConversationTurn#QueryInput for information about query inputs.
     */
    // const text = 'text-of-your-query';
    
    // Imports the Cx library
    const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    /**
     * Example for regional endpoint:
     *   const location = 'us-central1'
     *   const client = new SessionsClient({apiEndpoint: 'us-central1-dialogflow.googleapis.com'})
     */
    // Instantiates a client
    const cxClient = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    // Configures whether sentiment analysis should be performed. If not provided, sentiment analysis is not performed.
    const analyzeQueryTextSentiment = true;
    
    async function detectIntentWithSentimentAnalysis() {
      const sessionId = Math.random().toString(36).substring(7);
      const sessionPath = cxClient.projectLocationAgentSessionPath(
        projectId,
        location,
        agentId,
        sessionId
      );
    
      // Construct detect intent request
      const request = {
        session: sessionPath,
        queryInput: {
          text: {
            text: query,
          },
          languageCode,
        },
        queryParams: {
          analyzeQueryTextSentiment: analyzeQueryTextSentiment,
        },
      };
    
      // Run request
      const [response] = await cxClient.detectIntent(request);
      console.log(`User Query: ${query}`);
    
      // Shows result of sentiment analysis (sentimentAnalysisResult)
      const sentimentAnalysis = response.queryResult.sentimentAnalysisResult;
    
      // Determines sentiment score of user query
      let sentiment;
      if (sentimentAnalysis.score < 0) {
        sentiment = 'negative';
      } else if (sentimentAnalysis.score > 0) {
        sentiment = 'positive';
      } else {
        sentiment = 'neutral';
      }
      console.log(
        `User input sentiment has a score of ${sentimentAnalysis.score}, which indicates ${sentiment} sentiment.`
      );
    }
    
    detectIntentWithSentimentAnalysis();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import uuid
    
    from google.cloud.dialogflowcx_v3beta1.services.sessions import SessionsClient
    from google.cloud.dialogflowcx_v3beta1.types import session
    
    
    def run_sample():
        # TODO(developer): Update these values when running the function
        project_id = "YOUR-PROJECT-ID"
        location = "YOUR-LOCATION-ID"
        agent_id = "YOUR-AGENT-ID"
        text = "Perfect!"
        language_code = "en-us"
    
        detect_intent_with_sentiment_analysis(
            project_id,
            location,
            agent_id,
            text,
            language_code,
        )
    
    
    def detect_intent_with_sentiment_analysis(
        project_id,
        location,
        agent_id,
        text,
        language_code,
    ):
        """Returns the result of detect intent with sentiment analysis"""
    
        client_options = None
        if location != "global":
            api_endpoint = f"{location}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        session_client = SessionsClient(client_options=client_options)
        session_id = str(uuid.uuid4())
    
        session_path = session_client.session_path(
            project=project_id,
            location=location,
            agent=agent_id,
            session=session_id,
        )
    
        text_input = session.TextInput(text=text)
        query_input = session.QueryInput(text=text_input, language_code=language_code)
        query_params = session.QueryParameters(
            analyze_query_text_sentiment=True,
        )
        request = session.DetectIntentRequest(
            session=session_path,
            query_input=query_input,
            query_params=query_params,
        )
    
        response = session_client.detect_intent(request=request)
        score = response.query_result.sentiment_analysis_result.score
        print("Sentiment Score: {score}")
        return score
    
    

## Detect intent with text-to-speech response

The following samples show how to detect intent with a text-to-speech response.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.cx.v3.[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioEncoding.html);
    import com.google.cloud.dialogflow.cx.v3.[AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.cx.v3.[InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html);
    import com.google.cloud.dialogflow.cx.v3.[OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.html);
    import com.google.cloud.dialogflow.cx.v3.[OutputAudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioEncoding.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html);
    import com.google.cloud.dialogflow.cx.v3.[SynthesizeSpeechConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    
    public class DetectIntentSynthesizeTextToSpeechOutput {
    
      // DialogFlow API Detect Intent sample with synthesize TTS output.
      public static void main(String[] args) throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        String projectId = "my-project-id";
        String locationId = "my-location-id";
        String agentId = "my-agent-id";
        String audioFileName = "my-audio-file-name";
        int sampleRateHertz = 16000;
        String sessionId = "my-session-id";
        String languageCode = "my-language-code";
    
        detectIntent(
            projectId, locationId, agentId, audioFileName, sampleRateHertz, sessionId, languageCode);
      }
    
      public static void detectIntent(
          String projectId,
          String locationId,
          String agentId,
          String audioFileName,
          int sampleRateHertz,
          String sessionId,
          String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
    
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).Builder sessionsSettingsBuilder = [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).newBuilder();
        if (locationId.equals("global")) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html) sessionsSettings = sessionsSettingsBuilder.build();
    
        // Instantiates a client by setting the session name.
        // Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>`
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html).create(sessionsSettings)) {
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html) session =
              [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html).[ofProjectLocationAgentSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_ofProjectLocationAgentSessionName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, agentId, sessionId);
    
          // TODO : Uncomment if you want to print session path
          // System.out.println("Session Path: " + session.toString());
          [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html) inputAudioConfig =
              [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html).newBuilder()
                  .setAudioEncoding([AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioEncoding.html).AUDIO_ENCODING_LINEAR_16)
                  .setSampleRateHertz(sampleRateHertz)
                  .build();
    
          try (FileInputStream audioStream = new FileInputStream(audioFileName)) {
            // Subsequent requests must **only** contain the audio data.
            // Following messages: audio chunks. We just read the file in fixed-size chunks. In reality
            // you would split the user input by time.
            byte[] buffer = new byte[4096];
            int bytes = audioStream.read(buffer);
            [AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html) audioInput =
                [AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html).newBuilder()
                    .setAudio([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(buffer, 0, bytes))
                    .[setConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.Builder.html#com_google_cloud_dialogflow_cx_v3_AudioInput_Builder_setConfig_com_google_cloud_dialogflow_cx_v3_InputAudioConfig_)(inputAudioConfig)
                    .build();
            [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html) queryInput =
                [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html).newBuilder()
                    .setAudio(audioInput)
                    .setLanguageCode("en-US") // languageCode = "en-US"
                    .build();
    
            [SynthesizeSpeechConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.html) speechConfig =
                [SynthesizeSpeechConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.html).newBuilder().[setSpeakingRate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.Builder.html#com_google_cloud_dialogflow_cx_v3_SynthesizeSpeechConfig_Builder_setSpeakingRate_double_)(1.25).[setPitch](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.Builder.html#com_google_cloud_dialogflow_cx_v3_SynthesizeSpeechConfig_Builder_setPitch_double_)(10.0).build();
    
            [OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.html) outputAudioConfig =
                [OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.html).newBuilder()
                    .setAudioEncoding([OutputAudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioEncoding.html).OUTPUT_AUDIO_ENCODING_LINEAR_16)
                    .[setSynthesizeSpeechConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.Builder.html#com_google_cloud_dialogflow_cx_v3_OutputAudioConfig_Builder_setSynthesizeSpeechConfig_com_google_cloud_dialogflow_cx_v3_SynthesizeSpeechConfig_)(speechConfig)
                    .build();
    
            [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html) request =
                [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html).newBuilder()
                    .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_toString__)())
                    .setQueryInput(queryInput)
                    .setOutputAudioConfig(outputAudioConfig)
                    .build();
    
            // Performs the detect intent request.
            [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html) response = sessionsClient.detectIntent(request);
    
            // Display the output audio config retrieved from the response.
            [OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.html) audioConfigFromResponse = response.[getOutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html#com_google_cloud_dialogflow_cx_v3_DetectIntentResponse_getOutputAudioConfig__)();
    
            System.out.println("====================");
            System.out.format("Output Audio Config: %s \n", audioConfigFromResponse.toString());
          }
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Cx library
    const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'ID of GCP project associated with your Dialogflow agent';
    // const sessionId = `user specific ID of session, e.g. 12345`;
    // const query = `phrase(s) to pass to detect, e.g. I'd like to reserve a room for six people`;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    // const outputFile = `path for audio output file, e.g. ./resources/myOutput.wav`;
    
    // Instantiates a Sessions client
    const sessionsClient = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    // Define session path
    const sessionPath = sessionsClient.projectLocationAgentSessionPath(
      projectId,
      location,
      agentId,
      sessionId
    );
    const fs = require('fs');
    const util = require('util');
    
    async function detectIntentSynthesizeTTSResponse() {
      // Configuration of how speech should be synthesized. See https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig#SynthesizeSpeechConfig
      const synthesizeSpeechConfig = {
        speakingRate: 1.25,
        pitch: 10.0,
      };
    
      // Constructs the audio query request
      const request = {
        session: sessionPath,
        queryInput: {
          text: {
            text: query,
          },
          languageCode: languageCode,
        },
        outputAudioConfig: {
          audioEncoding: 'OUTPUT_AUDIO_ENCODING_LINEAR_16',
          synthesizeSpeechConfig: synthesizeSpeechConfig,
        },
      };
    
      // Sends the detectIntent request
      const [response] = await sessionsClient.detectIntent(request);
      // Output audio configurations
      console.log(
        `Speaking Rate: ${response.outputAudioConfig.synthesizeSpeechConfig.speakingRate}`
      );
      console.log(
        `Pitch: ${response.outputAudioConfig.synthesizeSpeechConfig.pitch}`
      );
    
      const audioFile = response.outputAudio;
      // Writes audio content to output file
      util.promisify(fs.writeFile)(outputFile, audioFile, 'binary');
      console.log(`Audio content written to file: ${outputFile}`);
    }
    detectIntentSynthesizeTTSResponse();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import uuid
    
    from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
    from google.cloud.dialogflowcx_v3.types import audio_config
    from google.cloud.dialogflowcx_v3.types import session
    
    
    def run_sample():
        # TODO(developer): Update these values when running the function
        project_id = "YOUR-PROJECT-ID"
        location = "YOUR-LOCATION-ID"
        agent_id = "YOUR-AGENT-ID"
        text = "YOUR-TEXT"
        audio_encoding = "YOUR-AUDIO-ENCODING"
        language_code = "YOUR-LANGUAGE-CODE"
        output_file = "YOUR-OUTPUT-FILE"
    
        detect_intent_synthesize_tts_response(
            project_id,
            location,
            agent_id,
            text,
            audio_encoding,
            language_code,
            output_file,
        )
    
    
    def detect_intent_synthesize_tts_response(
        project_id,
        location,
        agent_id,
        text,
        audio_encoding,
        language_code,
        output_file,
    ):
        """Returns the result of detect intent with synthesized response."""
        client_options = None
        if location != "global":
            api_endpoint = f"{location}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        session_client = SessionsClient(client_options=client_options)
        session_id = str(uuid.uuid4())
    
        # Constructs the audio query request
        session_path = session_client.session_path(
            project=project_id,
            location=location,
            agent=agent_id,
            session=session_id,
        )
        text_input = session.TextInput(text=text)
        query_input = session.QueryInput(text=text_input, language_code=language_code)
        synthesize_speech_config = audio_config.SynthesizeSpeechConfig(
            speaking_rate=1.25,
            pitch=10.0,
        )
        output_audio_config = audio_config.OutputAudioConfig(
            synthesize_speech_config=synthesize_speech_config,
            audio_encoding=audio_config.OutputAudioEncoding[audio_encoding],
        )
        request = session.DetectIntentRequest(
            session=session_path,
            query_input=query_input,
            output_audio_config=output_audio_config,
        )
    
        response = session_client.detect_intent(request=request)
        print(
            "Speaking Rate: "
            f"{response.output_audio_config.synthesize_speech_config.speaking_rate}"
        )
        print("Pitch: " f"{response.output_audio_config.synthesize_speech_config.pitch}")
        with open(output_file, "wb") as fout:
            fout.write(response.output_audio)
        print(f"Audio content written to file: {output_file}")
    
    

## Detect intent with webhook disabled

The following samples show how to detect intent with webhook calls disabled.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html);
    import com.google.cloud.dialogflow.cx.v3.[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TextInput.html);
    import com.google.common.collect.Maps;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Map;
    
    public class DetectIntentDisableWebhook {
    
      public static void main(String[] args) throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        String projectId = "my-project-id";
        String locationId = "global";
        String agentId = "my-agent-id";
        String sessionId = "my-UUID";
        List<String> texts = new ArrayList<>(List.of("my-list", "of-texts"));
        String languageCode = "en";
    
        detectIntent(projectId, locationId, agentId, sessionId, texts, languageCode);
      }
    
      // DialogFlow API Detect Intent sample with webhook disabled.
      public static Map<String, QueryResult> detectIntent(
          String projectId,
          String locationId,
          String agentId,
          String sessionId,
          List<String> texts,
          String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).Builder sessionsSettingsBuilder = [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).newBuilder();
        if (locationId.equals("global")) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html) sessionsSettings = sessionsSettingsBuilder.build();
    
        Map<String, QueryResult> queryResults = Maps.newHashMap();
    
        // Instantiates a client by setting the session name.
        // Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>`
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html).create(sessionsSettings)) {
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html) session =
              [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html).[ofProjectLocationAgentSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_ofProjectLocationAgentSessionName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, agentId, sessionId);
    
          // TODO : Uncomment if you want to print session path
          // System.out.println("Session Path: " + session.toString());
    
          // Detect intents for each text input.
          for (String text : texts) {
            // Set the text (hello) for the query.
            [TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TextInput.html).Builder textInput = [TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TextInput.html).newBuilder().setText(text);
    
            // Build the query with the TextInput and language code (en-US).
            [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html) queryInput =
                [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html).newBuilder().setText(textInput).setLanguageCode(languageCode).build();
    
            // Build the query parameters and setDisableWebhook to true.
            [QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.html) queryParameters =
                [QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.html).newBuilder().[setDisableWebhook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.Builder.html#com_google_cloud_dialogflow_cx_v3_QueryParameters_Builder_setDisableWebhook_boolean_)(true).build();
    
            // Build the DetectIntentRequest with the SessionName, QueryInput, and QueryParameters.
            [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html) request =
                [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest.html).newBuilder()
                    .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_toString__)())
                    .setQueryInput(queryInput)
                    .setQueryParams(queryParameters)
                    .build();
            System.out.println([request](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamController.html#com_google_api_gax_rpc_StreamController_request_int_).toString());
    
            // Performs the detect intent request.
            [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html) response = sessionsClient.detectIntent(request);
    
            // Display the query result.
            [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryResult.html) queryResult = response.[getQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse.html#com_google_cloud_dialogflow_cx_v3_DetectIntentResponse_getQueryResult__)();
    
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
      console.info(sessionPath);
    
      const request = {
        session: sessionPath,
        queryParams: {
          disableWebhook: true,
        },
        queryInput: {
          text: {
            text: query,
          },
          languageCode,
        },
      };
      const [response] = await client.detectIntent(request);
      console.log(`Detect Intent Request: ${request.queryParams.disableWebhook}`);
      for (const message of response.queryResult.responseMessages) {
        if (message.text) {
          console.log(`Agent Response: ${message.text.text}`);
        }
      }
    }
    
    detectIntentText();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import uuid
    
    from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
    from google.cloud.dialogflowcx_v3.types import session
    
    
    def run_sample():
        # TODO(developer): Update these values when running the function
        project_id = "YOUR-PROJECT-ID"
        location = "YOUR-LOCATION-ID"
        agent_id = "YOUR-AGENT-ID"
        text = "Perfect!"
        language_code = "en-us"
    
        detect_intent_disabled_webhook(
            project_id,
            location,
            agent_id,
            text,
            language_code,
        )
    
    
    def detect_intent_disabled_webhook(
        project_id,
        location,
        agent_id,
        text,
        language_code,
    ):
        """Returns the result of detect intent with sentiment analysis"""
    
        client_options = None
        if location != "global":
            api_endpoint = f"{location}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        session_client = SessionsClient(client_options=client_options)
        session_id = str(uuid.uuid4())
        session_path = session_client.session_path(
            project=project_id,
            location=location,
            agent=agent_id,
            session=session_id,
        )
    
        # Prepare request
        text_input = session.TextInput(text=text)
        query_input = session.QueryInput(text=text_input, language_code=language_code)
        query_params = session.QueryParameters(
            disable_webhook=True,
        )
        request = session.DetectIntentRequest(
            session=session_path,
            query_input=query_input,
            query_params=query_params,
        )
    
        response = session_client.detect_intent(request=request)
        print(f"Detect Intent Request: {request.query_params.disable_webhook}")
        response_text = []
        for message in response.query_result.response_messages:
            if message.text:
                curr_response_text = message.text.text
                print(f"Agent Response: {curr_response_text}")
                response_text.append(curr_response_text)
        return response_text
    
    

## Streaming detect intent with audio file input

The following samples show how to stream audio input to a streaming detect intent request.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[BidiStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream.html);
    import com.google.cloud.dialogflow.cx.v3beta1.AudioEncoding;
    import com.google.cloud.dialogflow.cx.v3beta1.AudioInput;
    import com.google.cloud.dialogflow.cx.v3beta1.InputAudioConfig;
    import com.google.cloud.dialogflow.cx.v3beta1.OutputAudioConfig;
    import com.google.cloud.dialogflow.cx.v3beta1.OutputAudioEncoding;
    import com.google.cloud.dialogflow.cx.v3beta1.QueryInput;
    import com.google.cloud.dialogflow.cx.v3beta1.QueryResult;
    import com.google.cloud.dialogflow.cx.v3beta1.SessionName;
    import com.google.cloud.dialogflow.cx.v3beta1.SessionsClient;
    import com.google.cloud.dialogflow.cx.v3beta1.SessionsSettings;
    import com.google.cloud.dialogflow.cx.v3beta1.SsmlVoiceGender;
    import com.google.cloud.dialogflow.cx.v3beta1.StreamingDetectIntentRequest;
    import com.google.cloud.dialogflow.cx.v3beta1.StreamingDetectIntentResponse;
    import com.google.cloud.dialogflow.cx.v3beta1.SynthesizeSpeechConfig;
    import com.google.cloud.dialogflow.cx.v3beta1.VoiceSelectionParams;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    
    public abstract class DetectIntentStream {
    
      // DialogFlow API Detect Intent sample with audio files processes as an audio stream.
      public static void detectIntentStream(
          String projectId, String locationId, String agentId, String sessionId, String audioFilePath)
          throws [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), IOException {
        SessionsSettings.Builder sessionsSettingsBuilder = SessionsSettings.newBuilder();
        if ("global".equals(locationId)) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        SessionsSettings sessionsSettings = sessionsSettingsBuilder.build();
    
        // Instantiates a client by setting the session name.
        // Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>`
        // Using the same `sessionId` between requests allows continuation of the conversation.
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try (SessionsClient sessionsClient = SessionsClient.create(sessionsSettings)) {
          SessionName session = SessionName.of(projectId, locationId, agentId, sessionId);
    
          // Instructs the speech recognizer how to process the audio content.
          // Note: hard coding audioEncoding and sampleRateHertz for simplicity.
          // Audio encoding of the audio content sent in the query request.
          InputAudioConfig inputAudioConfig =
              InputAudioConfig.newBuilder()
                  .setAudioEncoding(AudioEncoding.AUDIO_ENCODING_LINEAR_16)
                  .setSampleRateHertz(16000) // sampleRateHertz = 16000
                  .build();
    
          // Build the AudioInput with the InputAudioConfig.
          AudioInput audioInput = AudioInput.newBuilder().setConfig(inputAudioConfig).build();
    
          // Build the query with the InputAudioConfig.
          QueryInput queryInput =
              QueryInput.newBuilder()
                  .setAudio(audioInput)
                  .setLanguageCode("en-US") // languageCode = "en-US"
                  .build();
    
          // Create the Bidirectional stream
          BidiStream<StreamingDetectIntentRequest, StreamingDetectIntentResponse> bidiStream =
              sessionsClient.streamingDetectIntentCallable().call();
    
          // Specify sssml name and gender
          VoiceSelectionParams voiceSelection =
              // Voices that are available https://cloud.google.com/text-to-speech/docs/voices
              VoiceSelectionParams.newBuilder()
                  .setName("en-US-Standard-F")
                  .setSsmlGender(SsmlVoiceGender.SSML_VOICE_GENDER_FEMALE)
                  .build();
    
          SynthesizeSpeechConfig speechConfig =
              SynthesizeSpeechConfig.newBuilder().setVoice(voiceSelection).build();
    
          // Setup audio config
          OutputAudioConfig audioConfig =
              // Output enconding explanation
              // https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#outputaudioencoding
              OutputAudioConfig.newBuilder()
                  .setAudioEncoding(OutputAudioEncoding.OUTPUT_AUDIO_ENCODING_UNSPECIFIED)
                  .setAudioEncodingValue(1)
                  .setSynthesizeSpeechConfig(speechConfig)
                  .build();
    
          // The first request must **only** contain the audio configuration:
          bidiStream.send(
              StreamingDetectIntentRequest.newBuilder()
                  .setSession(session.toString())
                  .setQueryInput(queryInput)
                  .setOutputAudioConfig(audioConfig)
                  .build());
    
          try (FileInputStream audioStream = new FileInputStream(audioFilePath)) {
            // Subsequent requests must **only** contain the audio data.
            // Following messages: audio chunks. We just read the file in fixed-size chunks. In reality
            // you would split the user input by time.
            byte[] buffer = new byte[4096];
            int bytes;
            while ((bytes = audioStream.read(buffer)) != -1) {
              AudioInput subAudioInput =
                  AudioInput.newBuilder().setAudio([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(buffer, 0, bytes)).build();
              QueryInput subQueryInput =
                  QueryInput.newBuilder()
                      .setAudio(subAudioInput)
                      .setLanguageCode("en-US") // languageCode = "en-US"
                      .build();
              bidiStream.send(
                  StreamingDetectIntentRequest.newBuilder().setQueryInput(subQueryInput).build());
            }
          }
    
          // Tell the service you are done sending data.
          bidiStream.closeSend();
    
          for (StreamingDetectIntentResponse response : bidiStream) {
            QueryResult queryResult = response.getDetectIntentResponse().getQueryResult();
            System.out.println("====================");
            System.out.format("Query Text: '%s'\n", queryResult.getTranscript());
            System.out.format(
                "Detected Intent: %s (confidence: %f)\n",
                queryResult.getMatch().getIntent().getDisplayName(),
                queryResult.getMatch().getConfidence());
          }
        }
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
    // const audioFileName = '/path/to/audio.raw';
    // const encoding = 'AUDIO_ENCODING_LINEAR_16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'en'
    
    // Imports the Google Cloud Some API library
    const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    /**
     * Example for regional endpoint:
     *   const location = 'us-central1'
     *   const client = new SessionsClient({apiEndpoint: 'us-central1-dialogflow.googleapis.com'})
     */
    const client = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    const fs = require('fs');
    const util = require('util');
    const {Transform, pipeline} = require('stream');
    const pump = util.promisify(pipeline);
    
    async function detectIntentAudio() {
      const sessionId = Math.random().toString(36).substring(7);
      const sessionPath = client.projectLocationAgentSessionPath(
        projectId,
        location,
        agentId,
        sessionId
      );
      console.info(sessionPath);
    
      // Create a stream for the streaming request.
      const detectStream = client
        .streamingDetectIntent()
        .on('error', console.error)
        .on('data', data => {
          if (data.recognitionResult) {
            console.log(
              `Intermediate Transcript: ${data.recognitionResult.transcript}`
            );
          } else {
            console.log('Detected Intent:');
            const result = data.detectIntentResponse.queryResult;
    
            console.log(`User Query: ${result.transcript}`);
            for (const message of result.responseMessages) {
              if (message.text) {
                console.log(`Agent Response: ${message.text.text}`);
              }
            }
            if (result.match.intent) {
              console.log(`Matched Intent: ${result.match.intent.displayName}`);
            }
            console.log(`Current Page: ${result.currentPage.displayName}`);
          }
        });
    
      // Write the initial stream request to config for audio input.
      const initialStreamRequest = {
        session: sessionPath,
        queryInput: {
          audio: {
            config: {
              audioEncoding: encoding,
              sampleRateHertz: sampleRateHertz,
              synthesize_speech_config: {
                voice: {
                  // Set's the name and gender of the ssml voice
                  name: 'en-GB-Standard-A',
                  ssml_gender: 'SSML_VOICE_GENDER_FEMALE',
                },
              },
              singleUtterance: true,
            },
          },
          languageCode: languageCode,
        },
      };
      detectStream.write(initialStreamRequest);
    
      // Stream the audio from audio file to Dialogflow.
      await pump(
        fs.createReadStream(audioFileName),
        // Format the audio stream into the request format.
        new Transform({
          objectMode: true,
          transform: (obj, _, next) => {
            next(null, {queryInput: {audio: {audio: obj}}});
          },
        }),
        detectStream
      );
    }
    
    detectIntentAudio();

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
        audio_file_path = "YOUR-AUDIO-FILE-PATH"
        # For more supported languages see https://cloud.google.com/dialogflow/es/docs/reference/language
        language_code = "en-us"
    
        detect_intent_stream(agent, session_id, audio_file_path, language_code)
    
    
    def detect_intent_stream(agent, session_id, audio_file_path, language_code):
        """Returns the result of detect intent with streaming audio as input.
    
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
    
        input_audio_config = audio_config.InputAudioConfig(
            audio_encoding=audio_config.AudioEncoding.AUDIO_ENCODING_LINEAR_16,
            sample_rate_hertz=24000,
        )
    
        def request_generator():
            audio_input = session.AudioInput(config=input_audio_config)
            query_input = session.QueryInput(audio=audio_input, language_code=language_code)
            voice_selection = audio_config.VoiceSelectionParams()
            synthesize_speech_config = audio_config.SynthesizeSpeechConfig()
            output_audio_config = audio_config.OutputAudioConfig()
    
            # Sets the voice name and gender
            voice_selection.name = "en-GB-Standard-A"
            voice_selection.ssml_gender = (
                audio_config.SsmlVoiceGender.SSML_VOICE_GENDER_FEMALE
            )
    
            synthesize_speech_config.voice = voice_selection
    
            # Sets the audio encoding
            output_audio_config.audio_encoding = (
                audio_config.OutputAudioEncoding.OUTPUT_AUDIO_ENCODING_UNSPECIFIED
            )
            output_audio_config.synthesize_speech_config = synthesize_speech_config
    
            # The first request contains the configuration.
            yield session.StreamingDetectIntentRequest(
                session=session_path,
                query_input=query_input,
                output_audio_config=output_audio_config,
            )
    
            # Here we are reading small chunks of audio data from a local
            # audio file.  In practice these chunks should come from
            # an audio input device.
            with open(audio_file_path, "rb") as audio_file:
                while True:
                    chunk = audio_file.read(4096)
                    if not chunk:
                        break
                    # The later requests contains audio data.
                    audio_input = session.AudioInput(audio=chunk)
                    query_input = session.QueryInput(audio=audio_input)
                    yield session.StreamingDetectIntentRequest(query_input=query_input)
    
        responses = session_client.streaming_detect_intent(requests=request_generator())
    
        print("=" * 20)
        for response in responses:
            print(f'Intermediate transcript: "{response.recognition_result.transcript}".')
    
        # Note: The result from the last response is the final transcript along
        # with the detected content.
        response = response.detect_intent_response
        print(f"Query text: {response.query_result.transcript}")
        response_messages = [
            " ".join(msg.text.text) for msg in response.query_result.response_messages
        ]
        print(f"Response text: {' '.join(response_messages)}\n")
    
    

## Streaming detect intent with microphone audio

The following sample implements a real-time streaming audio interface with Dialogflow CX. It captures audio from the user's microphone, streams it to Dialogflow CX for audio transcription, intent detection and plays back the synthesized audio responses from Dialogflow CX through the user's speakers.

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    import argparse
    import asyncio
    from collections.abc import AsyncGenerator
    import logging
    import os
    import signal
    import struct
    import sys
    import time
    import uuid
    
    from google.api_core import retry as retries
    from google.api_core.client_options import ClientOptions
    from google.api_core.exceptions import GoogleAPIError, ServiceUnavailable
    from google.cloud import dialogflowcx_v3
    from google.protobuf.json_format import MessageToDict
    
    import pyaudio
    from termcolor import colored
    
    # TODO: Remove once GRPC log spam is gone see https://github.com/grpc/grpc/issues/37642
    os.environ["GRPC_VERBOSITY"] = "NONE"
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)
    
    CHUNK_SECONDS = 0.1
    DEFAULT_LANGUAGE_CODE = "en-US"
    DEFAULT_SAMPLE_RATE = 16000
    DEFAULT_DIALOGFLOW_TIMEOUT = 60.0
    
    
    def get_current_time() -> int:
        """Return Current Time in MS."""
        return int(round(time.time() * 1000))
    
    
    class AudioIO:
        """Audio Input / Output"""
    
        def __init__(
            self,
            rate: int,
            chunk_size: int,
        ) -> None:
            self._rate = rate
            self.chunk_size = chunk_size
            self._buff = asyncio.Queue()
            self.closed = False
            self.start_time = None  # only set when first audio received
            self.audio_input = []
            self._audio_interface = pyaudio.PyAudio()
            self._input_audio_stream = None
            self._output_audio_stream = None
    
            # Get default input device info
            try:
                input_device_info = self._audio_interface.get_default_input_device_info()
                self.input_device_name = input_device_info["name"]
                logger.info(f"Using input device: {self.input_device_name}")
            except IOError:
                logger.error("Could not get default input device info. Exiting.")
                sys.exit(1)
    
            # Get default output device info
            try:
                output_device_info = self._audio_interface.get_default_output_device_info()
                self.output_device_name = output_device_info["name"]
                logger.info(f"Using output device: {self.output_device_name}")
            except IOError:
                logger.error("Could not get default output device info. Exiting.")
                sys.exit(1)
    
            # setup input audio stream
            try:
                self._input_audio_stream = self._audio_interface.open(
                    format=pyaudio.paInt16,
                    channels=1,
                    rate=self._rate,
                    input=True,
                    frames_per_buffer=self.chunk_size,
                    stream_callback=self._fill_buffer,
                )
            except OSError as e:
                logger.error(f"Could not open input stream: {e}. Exiting.")
                sys.exit(1)
    
            # setup output audio stream
            try:
                self._output_audio_stream = self._audio_interface.open(
                    format=pyaudio.paInt16,
                    channels=1,
                    rate=self._rate,
                    output=True,
                    frames_per_buffer=self.chunk_size,
                )
                self._output_audio_stream.stop_stream()
            except OSError as e:
                logger.error(f"Could not open output stream: {e}. Exiting.")
                sys.exit(1)
    
        def __enter__(self) -> "AudioIO":
            """Opens the stream."""
            self.closed = False
            return self
    
        def __exit__(self, *args: any) -> None:
            """Closes the stream and releases resources."""
            self.closed = True
            if self._input_audio_stream:
                self._input_audio_stream.stop_stream()
                self._input_audio_stream.close()
                self._input_audio_stream = None
    
            if self._output_audio_stream:
                self._output_audio_stream.stop_stream()
                self._output_audio_stream.close()
                self._output_audio_stream = None
    
            # Signal the generator to terminate
            self._buff.put_nowait(None)
            self._audio_interface.terminate()
    
        def _fill_buffer(
            self, in_data: bytes, frame_count: int, time_info: dict, status_flags: int
        ) -> tuple[None, int]:
            """Continuously collect data from the audio stream, into the buffer."""
    
            # Capture the true start time when the first chunk is received
            if self.start_time is None:
                self.start_time = get_current_time()
    
            # only capture microphone input when output audio stream is stopped
            if self._output_audio_stream and self._output_audio_stream.is_stopped():
                self._buff.put_nowait(in_data)
            self.audio_input.append(in_data)
    
            return None, pyaudio.paContinue
    
        async def generator(self) -> AsyncGenerator[bytes, None]:
            """Stream Audio from microphone to API and to local buffer."""
            while not self.closed:
                try:
                    chunk = await asyncio.wait_for(self._buff.get(), timeout=1)
    
                    if chunk is None:
                        logger.debug("[generator] Received None chunk, ending stream")
                        return
    
                    data = [chunk]
    
                    while True:
                        try:
                            chunk = self._buff.get_nowait()
                            if chunk is None:
                                logger.debug(
                                    "[generator] Received None chunk (nowait), ending stream"
                                )
                                return
                            data.append(chunk)
                        except asyncio.QueueEmpty:
                            break
    
                    combined_data = b"".join(data)
                    yield combined_data
    
                except asyncio.TimeoutError:
                    logger.debug(
                        "[generator] No audio chunk received within timeout, continuing..."
                    )
                    continue
    
        def play_audio(self, audio_data: bytes) -> None:
            """Plays audio from the given bytes data, removing WAV header if needed."""
            # Remove WAV header if present
            if audio_data.startswith(b"RIFF"):
                try:
                    # Attempt to unpack the WAV header to determine header size.
                    header_size = struct.calcsize("<4sI4s4sIHHIIHH4sI")
                    header = struct.unpack("<4sI4s4sIHHIIHH4sI", audio_data[:header_size])
                    logger.debug(f"WAV header detected: {header}")
                    audio_data = audio_data[header_size:]  # Remove the header
                except struct.error as e:
                    logger.error(f"Error unpacking WAV header: {e}")
                    # If header parsing fails, play the original data; may not be a valid WAV
    
            # Play the raw PCM audio
            try:
                self._output_audio_stream.start_stream()
                self._output_audio_stream.write(audio_data)
            finally:
                self._output_audio_stream.stop_stream()
    
    
    class DialogflowCXStreaming:
        """Manages the interaction with the Dialogflow CX Streaming API."""
    
        def __init__(
            self,
            agent_name: str,
            language_code: str,
            single_utterance: bool,
            model: str | None,
            voice: str | None,
            sample_rate: int,
            dialogflow_timeout: float,
            debug: bool,
        ) -> None:
            """Initializes the Dialogflow CX Streaming API client."""
            try:
                _, project, _, location, _, agent_id = agent_name.split("/")
            except ValueError:
                raise ValueError(
                    "Invalid agent name format. Expected format: projects/<project>/locations/<location>/agents/<agent_id>"
                )
            if location != "global":
                client_options = ClientOptions(
                    api_endpoint=f"{location}-dialogflow.googleapis.com",
                    quota_project_id=project,
                )
            else:
                client_options = ClientOptions(quota_project_id=project)
    
            self.client = dialogflowcx_v3.[SessionsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.sessions.SessionsAsyncClient.html)(client_options=client_options)
            self.agent_name = agent_name
            self.language_code = language_code
            self.single_utterance = single_utterance
            self.model = model
            self.session_id = str(uuid.uuid4())
            self.dialogflow_timeout = dialogflow_timeout
            self.debug = debug
            self.sample_rate = sample_rate
            self.voice = voice
    
            if self.debug:
                logger.setLevel(logging.DEBUG)
                logger.debug("Debug logging enabled")
    
        async def generate_streaming_detect_intent_requests(
            self, audio_queue: asyncio.Queue
        ) -> AsyncGenerator[dialogflowcx_v3.StreamingDetectIntentRequest, None]:
            """Generates the requests for the streaming API."""
            audio_config = dialogflowcx_v3.[InputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.InputAudioConfig.html)(
                audio_encoding=dialogflowcx_v3.[AudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AudioEncoding.html).AUDIO_ENCODING_LINEAR_16,
                sample_rate_hertz=self.sample_rate,
                model=self.model,
                single_utterance=self.single_utterance,
            )
            query_input = dialogflowcx_v3.[QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.QueryInput.html)(
                language_code=self.language_code,
                audio=dialogflowcx_v3.[AudioInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AudioInput.html)(config=audio_config),
            )
            output_audio_config = dialogflowcx_v3.[OutputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.OutputAudioConfig.html)(
                audio_encoding=dialogflowcx_v3.[OutputAudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.OutputAudioEncoding.html).OUTPUT_AUDIO_ENCODING_LINEAR_16,
                sample_rate_hertz=self.sample_rate,
                synthesize_speech_config=(
                    dialogflowcx_v3.[SynthesizeSpeechConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SynthesizeSpeechConfig.html)(
                        voice=dialogflowcx_v3.[VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.VoiceSelectionParams.html)(name=self.voice)
                    )
                    if self.voice
                    else None
                ),
            )
    
            # First request contains session ID, query input audio config, and output audio config
            request = dialogflowcx_v3.[StreamingDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.StreamingDetectIntentRequest.html)(
                session=f"{self.agent_name}/sessions/{self.session_id}",
                query_input=query_input,
                enable_partial_response=True,
                output_audio_config=output_audio_config,
            )
            if self.debug:
                logger.debug(f"Sending initial request: {request}")
            yield request
    
            # Subsequent requests contain audio only
            while True:
                try:
                    chunk = await audio_queue.get()
                    if chunk is None:
                        logger.debug(
                            "[generate_streaming_detect_intent_requests] Received None chunk, signaling end of utterance"
                        )
                        break  # Exit the generator
    
                    request = dialogflowcx_v3.[StreamingDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.StreamingDetectIntentRequest.html)(
                        query_input=dialogflowcx_v3.[QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.QueryInput.html)(
                            audio=dialogflowcx_v3.[AudioInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AudioInput.html)(audio=chunk)
                        )
                    )
                    yield request
    
                except asyncio.CancelledError:
                    logger.debug(
                        "[generate_streaming_detect_intent_requests] Audio queue processing was cancelled"
                    )
                    break
    
        async def streaming_detect_intent(
            self,
            audio_queue: asyncio.Queue,
        ) -> AsyncGenerator[dialogflowcx_v3.StreamingDetectIntentResponse, None]:
            """Transcribes the audio into text and yields each response."""
            requests_generator = self.generate_streaming_detect_intent_requests(audio_queue)
    
            retry_policy = retries.AsyncRetry(
                predicate=retries.if_exception_type(ServiceUnavailable),
                initial=0.5,
                maximum=60.0,
                multiplier=2.0,
                timeout=300.0,
                on_error=lambda e: logger.warning(f"Retrying due to error: {e}"),
            )
    
            async def streaming_request_with_retry() -> (
                AsyncGenerator[dialogflowcx_v3.StreamingDetectIntentResponse, None]
            ):
                async def api_call():
                    logger.debug("Initiating streaming request")
                    return await self.client.streaming_detect_intent(
                        requests=requests_generator
                    )
    
                response_stream = await retry_policy(api_call)()
                return response_stream
    
            try:
                responses = await streaming_request_with_retry()
    
                # Use async for to iterate over the responses, WITH timeout
                response_iterator = responses.__aiter__()  # Get the iterator
                while True:
                    try:
                        response = await asyncio.wait_for(
                            response_iterator.__anext__(), timeout=self.dialogflow_timeout
                        )
                        if self.debug and response:
                            response_copy = MessageToDict(response._pb)
                            if response_copy.get("detectIntentResponse"):
                                response_copy["detectIntentResponse"][
                                    "outputAudio"
                                ] = "REMOVED"
                            logger.debug(f"Received response: {response_copy}")
                        yield response
                    except StopAsyncIteration:
                        logger.debug("End of response stream")
                        break
                    except asyncio.TimeoutError:
                        logger.warning("Timeout waiting for response from Dialogflow.")
                        continue  # Continue to the next iteration, don't break
                    except GoogleAPIError as e:  # Keep error handling
                        logger.error(f"Error: {e}")
                        if e.code == 500:  # Consider making this more robust
                            logger.warning("Encountered a 500 error during iteration.")
    
            except GoogleAPIError as e:
                logger.error(f"Error: {e}")
                if e.code == 500:
                    logger.warning("Encountered a 500 error during iteration.")
    
    
    async def push_to_audio_queue(
        audio_generator: AsyncGenerator, audio_queue: asyncio.Queue
    ) -> None:
        """Pushes audio chunks from a generator to an asyncio queue."""
        try:
            async for chunk in audio_generator:
                await audio_queue.put(chunk)
        except Exception as e:
            logger.error(f"Error in push_to_audio_queue: {e}")
    
    
    async def listen_print_loop(
        responses: AsyncGenerator[dialogflowcx_v3.[StreamingDetectIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.StreamingDetectIntentResponse.html), None],
        audioIO: AudioIO,
        audio_queue: asyncio.Queue,
        dialogflow_timeout: float,
    ) -> bool:
        """Iterates through server responses and prints them."""
        response_iterator = responses.__aiter__()
        while True:
            try:
                response = await asyncio.wait_for(
                    response_iterator.__anext__(), timeout=dialogflow_timeout
                )
    
                if (
                    response
                    and response.detect_intent_response
                    and response.detect_intent_response.output_audio
                ):
                    audioIO.play_audio(response.detect_intent_response.output_audio)
    
                if (
                    response
                    and response.detect_intent_response
                    and response.detect_intent_response.query_result
                ):
                    query_result = response.detect_intent_response.query_result
                    # Check for end_interaction in response messages
                    if query_result.response_messages:
                        for message in query_result.response_messages:
                            if message.text:
                                logger.info(f"Dialogflow output: {message.text.text[0]}")
                            if message._pb.HasField("end_interaction"):
                                logger.info("End interaction detected.")
                                return False  # Signal to *not* restart the loop (exit)
    
                    if query_result.intent and query_result.intent.display_name:
                        logger.info(f"Detected intent: {query_result.intent.display_name}")
    
                    # ensure audio stream restarts
                    return True
                elif response and response.recognition_result:
                    transcript = response.recognition_result.transcript
                    if transcript:
                        if response.recognition_result.is_final:
                            logger.info(f"Final transcript: {transcript}")
                            await audio_queue.put(None)  # Signal end of input
                        else:
                            print(
                                colored(transcript, "yellow"),
                                end="\r",
                            )
                else:
                    logger.debug("No transcript in recognition result.")
    
            except StopAsyncIteration:
                logger.debug("End of response stream in listen_print_loop")
                break
            except asyncio.TimeoutError:
                logger.warning("Timeout waiting for response in listen_print_loop")
                continue  # Crucial: Continue, don't return, on timeout
            except Exception as e:
                logger.error(f"Error in listen_print_loop: {e}")
                return False  # Exit on any error within the loop
    
        return True  # Always return after the async for loop completes
    
    
    async def handle_audio_input_output(
        dialogflow_streaming: DialogflowCXStreaming,
        audioIO: AudioIO,
        audio_queue: asyncio.Queue,
    ) -> None:
        """Handles audio input and output concurrently."""
    
        async def cancel_push_task(push_task: asyncio.Task | None) -> None:
            """Helper function to cancel push task safely."""
            if push_task is not None and not push_task.done():
                push_task.cancel()
                try:
                    await push_task
                except asyncio.CancelledError:
                    logger.debug("Push task cancelled successfully")
    
        push_task = None
        try:
            push_task = asyncio.create_task(
                push_to_audio_queue(audioIO.generator(), audio_queue)
            )
            while True:  # restart streaming here.
                responses = dialogflow_streaming.streaming_detect_intent(audio_queue)
    
                should_continue = await listen_print_loop(
                    responses,
                    audioIO,
                    audio_queue,
                    dialogflow_streaming.dialogflow_timeout,
                )
                if not should_continue:
                    logger.debug(
                        "End interaction detected, exiting handle_audio_input_output"
                    )
                    await cancel_push_task(push_task)
                    break  # exit while loop
    
                logger.debug("Restarting audio streaming loop")
    
        except asyncio.CancelledError:
            logger.warning("Handling of audio input/output was cancelled.")
            await cancel_push_task(push_task)
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
    
    
    async def main(
        agent_name: str,
        language_code: str = DEFAULT_LANGUAGE_CODE,
        single_utterance: bool = False,
        model: str | None = None,
        voice: str | None = None,
        sample_rate: int = DEFAULT_SAMPLE_RATE,
        dialogflow_timeout: float = DEFAULT_DIALOGFLOW_TIMEOUT,
        debug: bool = False,
    ) -> None:
        """Start bidirectional streaming from microphone input to speech API"""
    
        chunk_size = int(sample_rate * CHUNK_SECONDS)
    
        audioIO = AudioIO(sample_rate, chunk_size)
        dialogflow_streaming = DialogflowCXStreaming(
            agent_name,
            language_code,
            single_utterance,
            model,
            voice,
            sample_rate,
            dialogflow_timeout,
            debug,
        )
    
        logger.info(f"Chunk size: {audioIO.chunk_size}")
        logger.info(f"Using input device: {audioIO.input_device_name}")
        logger.info(f"Using output device: {audioIO.output_device_name}")
    
        # Signal handler function
        def signal_handler(sig: int, frame: any) -> None:
            print(colored("\nExiting gracefully...", "yellow"))
            audioIO.closed = True  # Signal to stop the main loop
            sys.exit(0)
    
        # Set the signal handler for Ctrl+C (SIGINT)
        signal.signal(signal.SIGINT, signal_handler)
    
        with audioIO:
            logger.info(f"NEW REQUEST: {get_current_time() / 1000}")
            audio_queue = asyncio.Queue()
    
            try:
                # Apply overall timeout to the entire interaction
                await asyncio.wait_for(
                    handle_audio_input_output(dialogflow_streaming, audioIO, audio_queue),
                    timeout=dialogflow_streaming.dialogflow_timeout,
                )
            except asyncio.TimeoutError:
                logger.error(
                    f"Dialogflow interaction timed out after {dialogflow_streaming.dialogflow_timeout} seconds."
                )
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument("agent_name", help="Agent Name")
        parser.add_argument(
            "--language_code",
            type=str,
            default=DEFAULT_LANGUAGE_CODE,
            help="Specify the language code (default: en-US)",
        )
        parser.add_argument(
            "--single_utterance",
            action="store_true",
            help="Enable single utterance mode (default: False)",
        )
        parser.add_argument(
            "--model",
            type=str,
            default=None,
            help="Specify the speech recognition model to use (default: None)",
        )
        parser.add_argument(
            "--voice",
            type=str,
            default=None,
            help="Specify the voice for output audio (default: None)",
        )
        parser.add_argument(
            "--sample_rate",
            type=int,
            default=DEFAULT_SAMPLE_RATE,
            help="Specify the sample rate in Hz (default: 16000)",
        )
        parser.add_argument(
            "--dialogflow_timeout",
            type=float,
            default=DEFAULT_DIALOGFLOW_TIMEOUT,
            help="Specify the Dialogflow API timeout in seconds (default: 60)",
        )
        parser.add_argument(
            "--debug",
            action="store_true",
            help="Enable debug logging",
        )
    
        args = parser.parse_args()
        asyncio.run(
            main(
                args.agent_name,
                args.language_code,
                args.single_utterance,
                args.model,
                args.voice,
                args.sample_rate,
                args.dialogflow_timeout,
                args.debug,
            )
        )
    

## Streaming detect intent with partial response enabled

The following samples show how to use streaming detect intent with partial responses.

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[BidiStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream.html);
    import com.google.cloud.dialogflow.cx.v3.[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioEncoding.html);
    import com.google.cloud.dialogflow.cx.v3.[AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html);
    import com.google.cloud.dialogflow.cx.v3.[InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html);
    import com.google.cloud.dialogflow.cx.v3.[OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.html);
    import com.google.cloud.dialogflow.cx.v3.[OutputAudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioEncoding.html);
    import com.google.cloud.dialogflow.cx.v3.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html);
    import com.google.cloud.dialogflow.cx.v3.[SsmlVoiceGender](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SsmlVoiceGender.html);
    import com.google.cloud.dialogflow.cx.v3.[StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[StreamingDetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentResponse.html);
    import com.google.cloud.dialogflow.cx.v3.[SynthesizeSpeechConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.html);
    import com.google.cloud.dialogflow.cx.v3.[VoiceSelectionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.VoiceSelectionParams.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    
    public class DetectIntentStreamingPartialResponse {
    
      // DialogFlow API Detect Intent sample with audio files
      // that processes as an audio stream.
      public static void detectIntentStreamingPartialResponse(
          String projectId, String locationId, String agentId, String sessionId, String audioFilePath)
          throws [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), IOException {
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).Builder sessionsSettingsBuilder = [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html).newBuilder();
        if (locationId.equals("global")) {
          sessionsSettingsBuilder.setEndpoint("dialogflow.googleapis.com:443");
        } else {
          sessionsSettingsBuilder.setEndpoint(locationId + "-dialogflow.googleapis.com:443");
        }
        [SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings.html) sessionsSettings = sessionsSettingsBuilder.build();
    
        // Instantiates a client by setting the session name.
        // Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>`
        // Using the same `sessionId` between requests allows continuation of the conversation.
    
        // Note: close() needs to be called on the SessionsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html).create(sessionsSettings)) {
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html) session = [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html).of(projectId, locationId, agentId, sessionId);
    
          // Instructs the speech recognizer how to process the audio content.
          // Note: hard coding audioEncoding and sampleRateHertz for simplicity.
          // Audio encoding of the audio content sent in the query request.
          [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html) inputAudioConfig =
              [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.InputAudioConfig.html).newBuilder()
                  .setAudioEncoding([AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioEncoding.html).AUDIO_ENCODING_LINEAR_16)
                  .setSampleRateHertz(16000) // sampleRateHertz = 16000
                  .build();
    
          // Build the AudioInput with the InputAudioConfig.
          [AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html) audioInput = [AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html).newBuilder().[setConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.Builder.html#com_google_cloud_dialogflow_cx_v3_AudioInput_Builder_setConfig_com_google_cloud_dialogflow_cx_v3_InputAudioConfig_)(inputAudioConfig).build();
    
          // Build the query with the InputAudioConfig.
          [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html) queryInput =
              [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html).newBuilder()
                  .setAudio(audioInput)
                  .setLanguageCode("en-US") // languageCode = "en-US"
                  .build();
    
          // Create the Bidirectional stream
          BidiStream<StreamingDetectIntentRequest, StreamingDetectIntentResponse> bidiStream =
              sessionsClient.[streamingDetectIntentCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.html#com_google_cloud_dialogflow_cx_v3_SessionsClient_streamingDetectIntentCallable__)().call();
    
          // Specify sssml name and gender
          [VoiceSelectionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.VoiceSelectionParams.html) voiceSelection =
              // Voices that are available https://cloud.google.com/text-to-speech/docs/voices
              [VoiceSelectionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.VoiceSelectionParams.html).newBuilder()
                  .setName("en-GB-Standard-A")
                  .[setSsmlGender](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.VoiceSelectionParams.Builder.html#com_google_cloud_dialogflow_cx_v3_VoiceSelectionParams_Builder_setSsmlGender_com_google_cloud_dialogflow_cx_v3_SsmlVoiceGender_)([SsmlVoiceGender](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SsmlVoiceGender.html).SSML_VOICE_GENDER_FEMALE)
                  .build();
    
          [SynthesizeSpeechConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.html) speechConfig =
              [SynthesizeSpeechConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.html).newBuilder().[setVoice](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig.Builder.html#com_google_cloud_dialogflow_cx_v3_SynthesizeSpeechConfig_Builder_setVoice_com_google_cloud_dialogflow_cx_v3_VoiceSelectionParams_)(voiceSelection).build();
    
          // Setup audio config
          [OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.html) audioConfig =
              // Output encoding explanation
              // https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#outputaudioencoding
              [OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.html).newBuilder()
                  .setAudioEncoding([OutputAudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioEncoding.html).OUTPUT_AUDIO_ENCODING_UNSPECIFIED)
                  .setAudioEncodingValue(1)
                  .[setSynthesizeSpeechConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.Builder.html#com_google_cloud_dialogflow_cx_v3_OutputAudioConfig_Builder_setSynthesizeSpeechConfig_com_google_cloud_dialogflow_cx_v3_SynthesizeSpeechConfig_)(speechConfig)
                  .build();
    
          [StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.html) streamingDetectIntentRequest =
              [StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.html).newBuilder()
                  .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionName.html#com_google_cloud_dialogflow_cx_v3_SessionName_toString__)())
                  .setQueryInput(queryInput)
                  .[setEnablePartialResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder.html#com_google_cloud_dialogflow_cx_v3_StreamingDetectIntentRequest_Builder_setEnablePartialResponse_boolean_)(true)
                  .setOutputAudioConfig(audioConfig)
                  .build();
          System.out.println(streamingDetectIntentRequest.toString());
    
          // The first request must **only** contain the audio configuration:
          bidiStream.send(streamingDetectIntentRequest);
    
          try (FileInputStream audioStream = new FileInputStream(audioFilePath)) {
            // Subsequent requests must **only** contain the audio data.
            // Following messages: audio chunks. We just read the file in fixed-size chunks. In reality
            // you would split the user input by time.
            byte[] buffer = new byte[4096];
            int bytes;
            while ((bytes = audioStream.read(buffer)) != -1) {
              [AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html) subAudioInput =
                  [AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AudioInput.html).newBuilder().setAudio([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(buffer, 0, bytes)).build();
              [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html) subQueryInput =
                  [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.html).newBuilder()
                      .setAudio(subAudioInput)
                      .setLanguageCode("en-US") // languageCode = "en-US"
                      .build();
              bidiStream.send(
                  [StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.html).newBuilder().setQueryInput(subQueryInput).build());
            }
          }
    
          // Tell the service you are done sending data.
          bidiStream.closeSend();
    
          // TODO: Uncomment to print detectIntentResponse.
    
          //   for (StreamingDetectIntentResponse response : bidiStream) {
          //     QueryResult queryResult = response.getDetectIntentResponse().getQueryResult();
          //     System.out.println("====================");
          //     System.out.format("Query Text: '%s'\n", queryResult.getTranscript());
          //     System.out.format(
          //         "Detected Intent: %s (confidence: %f)\n",
          //         queryResult.getIntent()
          //         .getDisplayName(), queryResult.getIntentDetectionConfidence());
          //   }
        }
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
    // const audioFileName = '/path/to/audio.raw';
    // const encoding = 'AUDIO_ENCODING_LINEAR_16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'en';
    
    const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    /**
     * Example for regional endpoint:
     *   const location = 'us-central1'
     *   const client = new SessionsClient({apiEndpoint: 'us-central1-dialogflow.googleapis.com'})
     */
    const client = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    const fs = require('fs');
    const util = require('util');
    const {Transform, pipeline} = require('stream');
    const pump = util.promisify(pipeline);
    
    async function streamingDetectIntentPartialResponse() {
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
          audio: {
            config: {
              audio_encoding: encoding,
              sampleRateHertz: sampleRateHertz,
              singleUtterance: true,
            },
          },
          languageCode: languageCode,
        },
        enablePartialResponse: true,
      };
    
      const stream = await client.streamingDetectIntent();
      stream.on('data', data => {
        if (data.detectIntentResponse) {
          const result = data.detectIntentResponse.queryResult;
    
          for (const message of result.responseMessages) {
            if (message.text) {
              console.log(`Agent Response: ${message.text.text}`);
            }
          }
        }
      });
      stream.on('error', err => {
        console.log(err);
      });
      stream.on('end', () => {
        /* API call completed */
      });
      stream.write(request);
    
      // Stream the audio from audio file to Dialogflow.
      await pump(
        fs.createReadStream(audioFileName),
        // Format the audio stream into the request format.
        new Transform({
          objectMode: true,
          transform: (obj, _, next) => {
            next(null, {queryInput: {audio: {audio: obj}}});
          },
        }),
        stream
      );
    }
    streamingDetectIntentPartialResponse();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import uuid
    
    from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
    from google.cloud.dialogflowcx_v3.types import audio_config
    from google.cloud.dialogflowcx_v3.types import InputAudioConfig
    from google.cloud.dialogflowcx_v3.types import session
    
    
    def run_sample():
        """
        TODO(developer): Modify these variables before running the sample.
        """
        project_id = "YOUR-PROJECT-ID"
        location = "YOUR-LOCATION-ID"
        agent_id = "YOUR-AGENT-ID"
        audio_file_name = "YOUR-AUDIO-FILE-PATH"
        encoding = "AUDIO_ENCODING_LINEAR_16"
        sample_rate_hertz = 16000
        language_code = "en"
    
        streaming_detect_intent_partial_response(
            project_id,
            location,
            agent_id,
            audio_file_name,
            encoding,
            sample_rate_hertz,
            language_code,
        )
    
    
    def streaming_detect_intent_partial_response(
        project_id,
        location,
        agent_id,
        audio_file_name,
        encoding,
        sample_rate_hertz,
        language_code,
    ):
        client_options = None
        if location != "global":
            api_endpoint = f"{location}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        session_client = SessionsClient(client_options=client_options)
        session_id = str(uuid.uuid4())
    
        session_path = session_client.session_path(
            project=project_id,
            location=location,
            agent=agent_id,
            session=session_id,
        )
    
        def request_generator():
            audio_encoding = audio_config.AudioEncoding[encoding]
            config = InputAudioConfig(
                audio_encoding=audio_encoding,
                sample_rate_hertz=sample_rate_hertz,
                single_utterance=True,
            )
            audio_input = session.AudioInput(config=config)
            query_input = session.QueryInput(audio=audio_input, language_code=language_code)
            yield session.StreamingDetectIntentRequest(
                session=session_path,
                query_input=query_input,
                enable_partial_response=True,
            )
            # Here we are reading small chunks of audio data from a local
            # audio file.  In practice these chunks should come from
            # an audio input device.
            with open(audio_file_name, "rb") as audio_file:
                while True:
                    chunk = audio_file.read(4096)
                    if not chunk:
                        break
                    # The later requests contains audio data.
                    audio_input = session.AudioInput(audio=chunk, config=config)
                    query_input = session.QueryInput(
                        audio=audio_input, language_code=language_code
                    )
                    yield session.StreamingDetectIntentRequest(
                        session=session_path,
                        query_input=query_input,
                        enable_partial_response=True,
                    )
    
        responses = session_client.streaming_detect_intent(requests=request_generator())
    
        print("=" * 20)
        for response in responses:
            print(f'Intermediate transcript: "{response.recognition_result.transcript}".')
    
        # Note: The result from the last response is the final transcript along
        # with the detected content.
        response = response.detect_intent_response
        print(f"Query text: {response.query_result.transcript}")
        response_messages = [
            " ".join(msg.text.text) for msg in response.query_result.response_messages
        ]
        print(f"Response text: {' '.join(response_messages)}\n")
    
    

[ Previous arrow_back  Data application levels  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-level)

[ Next Implement webhooks  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/webhook)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
