---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-tts/
title: Detect intent with audio output \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:25.035463+00:00
---

# Detect intent with audio output  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-tts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Detect intent with audio output Stay organized with collections  Save and categorize content based on your preferences. 

Applications often need a bot to talk back to the end-user. Dialogflow Applications often need a bot to talk back to the end user. Dialogflow lets you use [Cloud Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs) powered by [DeepMind WaveNet](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) to generate speech responses from your agent. This conversion from intent text responses to audio is called _audio output_ , _speech synthesis_ ,

You can use audio for both input and output when detecting an intent. This is common when developing apps that communicate with users using a purely audio interface.

For a list of supported languages, see the **TTS** column on the [Languages](https://docs.cloud.google.com/dialogflow/docs/reference/language) page.

## Before you begin

This feature is only applicable when using the API for [end-user interactions](https://docs.cloud.google.com/dialogflow/docs/api-overview). If you are using an [integration](https://docs.cloud.google.com/dialogflow/docs/integrations), you can skip this guide. 

Before you begin, complete the following steps:

  * Read [Dialogflow basics](https://docs.cloud.google.com/dialogflow/docs/basics).
  * Perform [setup steps](https://docs.cloud.google.com/dialogflow/docs/quick/setup).



## Create an agent

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com). 
  2. Sign in to the console if prompted. For more information, see the [Dialogflow console overview](https://docs.cloud.google.com/dialogflow/docs/console). 
  3. In the sidebar menu, expand **Loading agents**. 
  4. Click **Create new agent**. 
  5. Enter the agent name, default language, and default time zone. 
  6. Enter an existing project. To let the Dialogflow console create a project, select **Create a new Google project**. 
  7. Click **Create**. 



## Detect intent

To detect intent, call the `detectIntent` method on the [`Sessions`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#sessions) type.

### REST

### 1\. Prepare audio content

Download the [`book-a-room.wav`](https://docs.cloud.google.com/static/dialogflow/es/docs/data/book-a-room.wav) sample input_audio file, which says "book a room." The audio file must be base64-encoded for this example, so it can be provided in the JSON request below.

Here is a Linux example:
    
    
    wget https://cloud.google.com/dialogflow/es/docs/data/book-a-room.wav
    base64 -w 0 book-a-room.wav > book-a-room.b64

For examples on other platforms, see [Embedding Base64-encoded audio](https://docs.cloud.google.com/speech/docs/base64-encoding) in the Cloud Speech API documentation.

### 2\. Make detect intent request

Call the `detectIntent` method on the [`Sessions`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#sessions) type and specify base64-encoded audio.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * SESSION_ID: a session ID
  * BASE64_AUDIO: the base64 content from the output file above



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/SESSION_ID:detectIntent

Request JSON body: 
    
    
    {
      "queryInput": {
        "audioConfig": {
          "languageCode": "en-US"
        }
      },
      "outputAudioConfig" : {
        "audioEncoding": "OUTPUT_AUDIO_ENCODING_LINEAR_16"
      },
      "inputAudio": "BASE64_AUDIO"
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/SESSION_ID:detectIntent"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/sessions/SESSION_ID:detectIntent" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "responseId": "b7405848-2a3a-4e26-b9c6-c4cf9c9a22ee",
      "queryResult": {
        "queryText": "book a room",
        "speechRecognitionConfidence": 0.8616504,
        **"action"** : "room.reservation",
        "parameters": {
          "time": "",
          "date": "",
          "duration": "",
          "guests": "",
          "location": ""
        },
        "fulfillmentText": "I can help with that. Where would you like to reserve a room?",
        **"fulfillmentMessages"** : [
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
      },
      **"outputAudio"** : "UklGRs6vAgBXQVZFZm10IBAAAAABAAEAwF0AAIC7AA..."
    }
    

Notice that the value of the `queryResult.action` field is `room.reservation` and the `outputAudio` field contains a large base64 audio string.

### 3\. Play output audio

Copy the text from the `outputAudio` field and save it in a file named `output_audio.b64`. This file needs to be converted to audio.

Here is a Linux example:
    
    
    base64 -d output_audio.b64 > output_audio.wav

For examples on other platforms, see [Decoding Base64-Encoded Audio Content](https://docs.cloud.google.com/text-to-speech/docs/base64-decoding) in the text-to-speech API documentation.

You can now play the `output_audio.wav` audio file and hear that it matches the text from the `queryResult.fulfillmentMessages[1].text.text[0]` field above. The second `fulfillmentMessages` element is chosen because it's the text response for the default platform. 

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.v2.[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html);
    import com.google.cloud.dialogflow.v2.[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentResponse.html);
    import com.google.cloud.dialogflow.v2.[OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.OutputAudioConfig.html);
    import com.google.cloud.dialogflow.v2.[OutputAudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.OutputAudioEncoding.html);
    import com.google.cloud.dialogflow.v2.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html);
    import com.google.cloud.dialogflow.v2.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html);
    import com.google.cloud.dialogflow.v2.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html);
    import com.google.cloud.dialogflow.v2.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html);
    import com.google.cloud.dialogflow.v2.[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.TextInput.html);
    import com.google.common.collect.Maps;
    import java.io.IOException;
    import java.util.List;
    import java.util.Map;
    
    public class DetectIntentWithTextToSpeechResponse {
    
      public static Map<String, QueryResult> detectIntentWithTexttoSpeech(
          String projectId, List<String> texts, String sessionId, String languageCode)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        Map<String, QueryResult> queryResults = Maps.newHashMap();
        // Instantiates a client
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html).create()) {
          // Set the session name using the sessionId (UUID) and projectID (my-project-id)
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html) session = [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html).of(projectId, sessionId);
          System.out.println("Session Path: " + session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html#com_google_cloud_dialogflow_v2_SessionName_toString__)());
    
          // Detect intents for each text input
          for (String text : texts) {
            // Set the text (hello) and language code (en-US) for the query
            [TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.TextInput.html).Builder textInput =
                [TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.TextInput.html).newBuilder().setText(text).setLanguageCode(languageCode);
    
            // Build the query with the TextInput
            [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html) queryInput = [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html).newBuilder().setText(textInput).build();
    
            //
            [OutputAudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.OutputAudioEncoding.html) audioEncoding = [OutputAudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.OutputAudioEncoding.html).OUTPUT_AUDIO_ENCODING_LINEAR_16;
            int sampleRateHertz = 16000;
            [OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.OutputAudioConfig.html) outputAudioConfig =
                [OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.OutputAudioConfig.html).newBuilder()
                    .setAudioEncoding(audioEncoding)
                    .setSampleRateHertz(sampleRateHertz)
                    .build();
    
            [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html) dr =
                [DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentRequest.html).newBuilder()
                    .setQueryInput(queryInput)
                    .setOutputAudioConfig(outputAudioConfig)
                    .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html#com_google_cloud_dialogflow_v2_SessionName_toString__)())
                    .build();
    
            // Performs the detect intent request
            [DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DetectIntentResponse.html) response = sessionsClient.detectIntent(dr);
    
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
    
            queryResults.put(text, queryResult);
          }
        }
        return queryResults;
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Dialogflow client library
    const dialogflow = require('[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)').v2;
    
    // Instantiate a DialogFlow client.
    const sessionClient = new dialogflow.[SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'ID of GCP project associated with your Dialogflow agent';
    // const sessionId = `user specific ID of session, e.g. 12345`;
    // const query = `phrase(s) to pass to detect, e.g. I'd like to reserve a room for six people`;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    // const outputFile = `path for audio output file, e.g. ./resources/myOutput.wav`;
    
    // Define session path
    const sessionPath = sessionClient.projectAgentSessionPath(
      projectId,
      sessionId
    );
    const fs = require('fs');
    const util = require('util');
    
    async function detectIntentwithTTSResponse() {
      // The audio query request
      const request = {
        session: sessionPath,
        queryInput: {
          text: {
            text: query,
            languageCode: languageCode,
          },
        },
        outputAudioConfig: {
          audioEncoding: 'OUTPUT_AUDIO_ENCODING_LINEAR_16',
        },
      };
      sessionClient.detectIntent(request).then(responses => {
        console.log('Detected intent:');
        const audioFile = responses[0].outputAudio;
        util.promisify(fs.writeFile)(outputFile, audioFile, 'binary');
        console.log(`Audio content written to file: ${outputFile}`);
      });
    }
    detectIntentwithTTSResponse();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_intent_with_texttospeech_response(
        project_id, session_id, texts, language_code
    ):
        """Returns the result of detect intent with texts as inputs and includes
        the response in an audio format.
    
        Using the same `session_id` between requests allows continuation
        of the conversation."""
        from google.cloud import dialogflow
    
        session_client = dialogflow.SessionsClient()
    
        session_path = session_client.[session_path](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsClient.html#google_cloud_dialogflow_v2_services_sessions_SessionsClient_session_path)(project_id, session_id)
        print("Session path: {}\n".format(session_path))
    
        for text in texts:
            text_input = dialogflow.[TextInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TextInput.html)(text=text, language_code=language_code)
    
            query_input = dialogflow.[QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryInput.html)(text=text_input)
    
            # Set the query parameters with sentiment analysis
            output_audio_config = dialogflow.[OutputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.OutputAudioConfig.html)(
                audio_encoding=dialogflow.OutputAudioEncoding.OUTPUT_AUDIO_ENCODING_LINEAR_16
            )
    
            request = dialogflow.[DetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DetectIntentRequest.html)(
                session=session_path,
                query_input=query_input,
                output_audio_config=output_audio_config,
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
            # The response's audio_content is binary.
            with open("output.wav", "wb") as out:
                out.write(response.output_audio)
                print('Audio content written to file "output.wav"')
    
    

For more information about the relevant response fields, see the Detect intent responses section.

## Detect intent responses

The response for a detect intent request is a `DetectIntentResponse` type.

Normal detect intent processing controls the content of the `DetectIntentResponse.queryResult.fulfillmentMessages` field.

The `DetectIntentResponse.outputAudio` field is populated with audio based on the values of _default_ platform _text_ responses found in the `DetectIntentResponse.queryResult.fulfillmentMessages` field:

  * If multiple default text responses exist, they are concatenated when generating audio.
  * If no default platform text responses exist, the generated audio content is empty.



The `DetectIntentResponse.outputAudioConfig` field is populated with audio settings used to generate the output audio.

## Detect intent from a stream

When detecting intent from a stream, you send requests similar to the example that does not use output audio: [Detecting Intent from a Stream](https://docs.cloud.google.com/dialogflow/docs/how/detect-intent-stream). However, you supply an [OutputAudioConfig](https://docs.cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.OutputAudioConfig) field to the request. The `output_audio` and `output_audio_config` fields are populated in the final streaming response that you get from the Dialogflow API server. For more information, see [StreamingDetectIntentRequest](https://docs.cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.StreamingDetectIntentRequest) and [StreamingDetectIntentResponse](https://docs.cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#streamingdetectintentresponse).

## Agent settings for speech

You can control various aspects of speech synthesis. See the [Agent speech settings](https://docs.cloud.google.com/dialogflow/docs/agents-settings#speech).

**Note:** API calls that provide output audio config override all existing text-to-speech settings applied to the agent.

## Use the Dialogflow simulator

You can interact with the agent and receive audio responses using the [Dialogflow simulator](https://docs.cloud.google.com/dialogflow/docs/console#simulator):

  1. Enable automatic text-to-speech by following the instructions in Agent speech settings.
  2. Type or say "book a room" in the simulator.
  3. View the **output audio** section in the simulator.



[ Previous arrow_back  Detect intent with audio input stream  ](https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-stream)

[ Next Detect intent with sentiment analysis  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/how/sentiment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
