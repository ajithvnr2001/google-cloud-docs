---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-audio/
title: Detect intent with audio input file \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:34.560142+00:00
---

# Detect intent with audio input file  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-audio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Detect intent with audio input file Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to send audio input to a detect intent request by using the API. Dialogflow processes the audio and converts it to text before it attempts an intent match.

## Before you begin

This feature is only applicable when using the API for [end-user interactions](https://docs.cloud.google.com/dialogflow/docs/api-overview). If you are using an [integration](https://docs.cloud.google.com/dialogflow/docs/integrations), you can skip this guide. 

Before you read this guide, complete the following tasks:

  * Read [Dialogflow basics](https://docs.cloud.google.com/dialogflow/es/docs/basics).
  * Complete the [setup steps](https://docs.cloud.google.com/dialogflow/es/docs/quick/setup).



## Create an agent

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com). 
  2. Sign in to the console if prompted. For more information, see the [Dialogflow console overview](https://docs.cloud.google.com/dialogflow/docs/console). 
  3. In the sidebar menu, expand **Loading agents**. 
  4. Click **Create new agent**. 
  5. Enter the agent name, default language, and default time zone. 
  6. Enter an existing project. To let the Dialogflow console create a project, select **Create a new Google project**. 
  7. Click **Create**. 



## Detect intent

To detect intent, call the `detectIntent` method on the [`Sessions`](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#sessions) type.

### REST

Download the [`book-a-room.wav`](https://docs.cloud.google.com/static/dialogflow/es/docs/data/book-a-room.wav) sample input audio file, which says "book a room." The audio file must be Base64-encoded for this example, so it can be provided in the following JSON request. 

To encode the audio file for the request, use the following commands on Linux:
    
    
    wget https://cloud.google.com/dialogflow/es/docs/data/book-a-room.wav
    base64 -w 0 book-a-room.wav > book-a-room.b64

For more information about encoding audio content, see [Base64-encoding audio content](https://docs.cloud.google.com/speech-to-text/docs/base64-encoding).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * AUDIO: the base64 encoded audio content



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/123456789:detectIntent

Request JSON body: 
    
    
    {
      "queryInput": {
        "audioConfig": {
          "languageCode": "en-US"
        }
      },
      "inputAudio": "AUDIO"
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/123456789:detectIntent"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/123456789:detectIntent" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/dialogflow/docs/reference/rest/v2/projects.agent.sessions/detectIntent). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "responseId": "3c1e5a89-75b9-4c3f-b63d-4b1351dd5e32",
      "queryResult": {
        "queryText": "book a room",
        "action": "room.reservation",
        "parameters": {
          "time": "",
          "date": "",
          "guests": "",
          "duration": "",
          "location": ""
        },
        "fulfillmentText": "I can help with that. Where would you like to reserve a room?",
        "fulfillmentMessages": [
          {
            "text": {
              "text": [
                "I can help with that. Where would you like to reserve a room?"
              ]
            }
          }
        ],
        "intent": {
          "name": "projects/PROJECT_ID/agent/intents/e8f6a63e-73da-4a1a-8bfc-857183f71228",
          "displayName": "room.reservation"
        },
        "intentDetectionConfidence": 1,
        "diagnosticInfo": {},
        "languageCode": "en-us"
      }
    }
    

The `queryResult.action` field value is "room.reservation", and the `queryResult.fulfillmentMessages[0|1].text.text[0]` field value asks the user for more information. 

### Go

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func DetectIntentAudio(projectID, sessionID, audioFile, languageCode string) (string, error) {
    	ctx := context.Background()
    
    	sessionClient, err := dialogflow.NewSessionsClient(ctx)
    	if err != nil {
    		return "", err
    	}
    	defer sessionClient.Close()
    
    	if projectID == "" || sessionID == "" {
    		return "", fmt.Errorf("detect.DetectIntentAudio empty project (%s) or session (%s)", projectID, sessionID)
    	}
    
    	sessionPath := fmt.Sprintf("projects/%s/agent/sessions/%s", projectID, sessionID)
    
    	// In this example, we hard code the encoding and sample rate for simplicity.
    	audioConfig := dialogflowpb.InputAudioConfig{AudioEncoding: dialogflowpb.AudioEncoding_AUDIO_ENCODING_LINEAR_16, SampleRateHertz: 16000, LanguageCode: languageCode}
    
    	queryAudioInput := dialogflowpb.QueryInput_AudioConfig{AudioConfig: &audioConfig}
    
    	audioBytes, err := os.ReadFile(audioFile)
    	if err != nil {
    		return "", err
    	}
    
    	queryInput := dialogflowpb.QueryInput{Input: &queryAudioInput}
    	request := dialogflowpb.DetectIntentRequest{Session: sessionPath, QueryInput: &queryInput, InputAudio: audioBytes}
    
    	response, err := sessionClient.DetectIntent(ctx, &request)
    	if err != nil {
    		return "", err
    	}
    
    	queryResult := response.GetQueryResult()
    	fulfillmentText := queryResult.GetFulfillmentText()
    	return fulfillmentText, nil
    }
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.v2.[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AudioEncoding.html);
    import com.google.cloud.dialogflow.v2.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.v2.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.v2.[InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.InputAudioConfig.html);
    import com.google.cloud.dialogflow.v2.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html);
    import com.google.cloud.dialogflow.v2.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html);
    import com.google.cloud.dialogflow.v2.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html);
    import com.google.cloud.dialogflow.v2.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    
    public class DetectIntentAudio {
    
      // DialogFlow API Detect Intent sample with audio files.
      public static [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html) detectIntentAudio(
          String projectId, String audioFilePath, String sessionId, String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        // Instantiates a client
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html).create()) {
          // Set the session name using the sessionId (UUID) and projectID (my-project-id)
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html) session = [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html).of(projectId, sessionId);
          System.out.println("Session Path: " + session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html#com_google_cloud_dialogflow_v2_SessionName_toString__)());
    
          // Note: hard coding audioEncoding and sampleRateHertz for simplicity.
          // Audio encoding of the audio content sent in the query request.
          [AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AudioEncoding.html) audioEncoding = [AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AudioEncoding.html).AUDIO_ENCODING_LINEAR_16;
          int sampleRateHertz = 16000;
    
          // Instructs the speech recognizer how to process the audio content.
          [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.InputAudioConfig.html) inputAudioConfig =
              [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.InputAudioConfig.html).newBuilder()
                  .setAudioEncoding(
                      audioEncoding) // audioEncoding = AudioEncoding.AUDIO_ENCODING_LINEAR_16
                  .setLanguageCode(languageCode) // languageCode = "en-US"
                  .setSampleRateHertz(sampleRateHertz) // sampleRateHertz = 16000
                  .build();
    
          // Build the query with the InputAudioConfig
          [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html) queryInput = [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html).newBuilder().setAudioConfig(inputAudioConfig).build();
    
          // Read the bytes from the audio file
          byte[] inputAudio = Files.readAllBytes(Paths.get(audioFilePath));
    
          // Build the DetectIntentRequest
          [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html) request =
              [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html).newBuilder()
                  .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html#com_google_cloud_dialogflow_v2_SessionName_toString__)())
                  .setQueryInput(queryInput)
                  .setInputAudio([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(inputAudio))
                  .build();
    
          // Performs the detect intent request
          [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentResponse.html) response = sessionsClient.detectIntent(request);
    
          // Display the query result
          [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html) queryResult = response.[getQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentResponse.html#com_google_cloud_dialogflow_v2_DetectIntentResponse_getQueryResult__)();
          System.out.println("====================");
          System.out.format("Query Text: '%s'\n", queryResult.[getQueryText](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getQueryText__)());
          System.out.format(
              "Detected Intent: %s (confidence: %f)\n",
              queryResult.[getIntent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getIntent__)().getDisplayName(), queryResult.[getIntentDetectionConfidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getIntentDetectionConfidence__)());
          System.out.format(
              "Fulfillment Text: '%s'\n",
              queryResult.[getFulfillmentMessagesCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getFulfillmentMessagesCount__)() > 0
                  ? queryResult.[getFulfillmentMessages](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getFulfillmentMessages_int_)(0).getText()
                  : "Triggered Default Fallback Intent");
    
          return queryResult;
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    const util = require('util');
    const {struct} = require('pb-util');
    // Imports the Dialogflow library
    const dialogflow = require('[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)');
    
    // Instantiates a session client
    const sessionClient = new dialogflow.[SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    // The path to identify the agent that owns the created intent.
    const sessionPath = sessionClient.projectAgentSessionPath(
      projectId,
      sessionId
    );
    
    // Read the content of the audio file and send it as part of the request.
    const readFile = util.promisify(fs.readFile);
    const inputAudio = await readFile(filename);
    const request = {
      session: sessionPath,
      queryInput: {
        audioConfig: {
          audioEncoding: encoding,
          sampleRateHertz: sampleRateHertz,
          languageCode: languageCode,
        },
      },
      inputAudio: inputAudio,
    };
    
    // Recognizes the speech in the audio and detects its intent.
    const [response] = await sessionClient.detectIntent(request);
    
    console.log('Detected intent:');
    const result = response.queryResult;
    // Instantiates a context client
    const contextClient = new dialogflow.[ContextsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)();
    
    console.log(`  Query: ${result.queryText}`);
    console.log(`  Response: ${result.fulfillmentText}`);
    if (result.intent) {
      console.log(`  Intent: ${result.intent.displayName}`);
    } else {
      console.log('  No intent matched.');
    }
    const parameters = JSON.stringify(struct.decode(result.parameters));
    console.log(`  Parameters: ${parameters}`);
    if (result.outputContexts && result.outputContexts.length) {
      console.log('  Output contexts:');
      result.outputContexts.forEach(context => {
        const contextId =
          contextClient.matchContextFromProjectAgentSessionContextName(
            context.name
          );
        const contextParameters = JSON.stringify(
          struct.decode(context.parameters)
        );
        console.log(`    ${contextId}`);
        console.log(`      lifespan: ${context.lifespanCount}`);
        console.log(`      parameters: ${contextParameters}`);
      });
    }

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_intent_audio(project_id, session_id, audio_file_path, language_code):
        """Returns the result of detect intent with an audio file as input.
    
        Using the same `session_id` between requests allows continuation
        of the conversation."""
        from google.cloud import dialogflow
    
        session_client = dialogflow.SessionsClient()
    
        # Note: hard coding audio_encoding and sample_rate_hertz for simplicity.
        audio_encoding = dialogflow.AudioEncoding.AUDIO_ENCODING_LINEAR_16
        sample_rate_hertz = 16000
    
        session = session_client.[session_path](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsClient.html#google_cloud_dialogflow_v2_services_sessions_SessionsClient_session_path)(project_id, session_id)
        print("Session path: {}\n".format(session))
    
        with open(audio_file_path, "rb") as audio_file:
            input_audio = audio_file.read()
    
        audio_config = dialogflow.[InputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InputAudioConfig.html)(
            audio_encoding=audio_encoding,
            language_code=language_code,
            sample_rate_hertz=sample_rate_hertz,
        )
        query_input = dialogflow.[QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryInput.html)(audio_config=audio_config)
    
        request = dialogflow.[DetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DetectIntentRequest.html)(
            session=session,
            query_input=query_input,
            input_audio=input_audio,
        )
        response = session_client.[detect_intent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsClient.html#google_cloud_dialogflow_v2_services_sessions_SessionsClient_detect_intent)(request=request)
    
        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/dialogflow/docs/reference/libraries) on the client libraries page and then visit the [Dialogflow CX reference documentation for .NET.](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/dialogflow/docs/reference/libraries) on the client libraries page and then visit the [Dialogflow CX reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-dialogflow/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/dialogflow/docs/reference/libraries) on the client libraries page and then visit the [Dialogflow CX reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-dialogflow/latest/Google/Cloud/Dialogflow.html)

[ Previous arrow_back  Update data with a FieldMask  ](https://docs.cloud.google.com/dialogflow/es/docs/how/field-mask)

[ Next Detect intent with audio input stream  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-stream)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
