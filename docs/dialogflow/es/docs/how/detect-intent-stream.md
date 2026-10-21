---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-stream/
title: Detect intent with audio input stream \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:48.059733+00:00
---

# Detect intent with audio input stream  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Detect intent with audio input stream Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to stream audio input to a detect intent request by using the API. Dialogflow processes the audio and converts it to text before it attempts an intent match. This process is called _audio input_ , _speech recognition_ , _speech-to-text_ , or _STT_.

**Note:** Streaming is supported by the RPC API and client libraries, but it's not supported by the REST API.

## Before you begin

This feature is only applicable when using the API for [end-user interactions](https://docs.cloud.google.com/dialogflow/docs/api-overview). If you are using an [integration](https://docs.cloud.google.com/dialogflow/docs/integrations), you can skip this guide. 

Complete the following tasks before you read this guide:

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



## Streaming basics

The [`Session`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#sessions) type's `streamingDetectIntent` method returns a bidirectional gRPC streaming object. The available methods for this object vary by language, so see the reference documentation for your client library for details.

The streaming object is used to send and receive data concurrently. Using this object, your client streams audio content to Dialogflow, while concurrently listening for a `StreamingDetectIntentResponse`.

The `streamingDetectIntent` method has a `query_input.audio_config.single_utterance` parameter that affects speech recognition:

  * If `false` (default), speech recognition does not cease until the client closes the stream.
  * If `true`, Dialogflow will detect a single spoken utterance in input audio. When Dialogflow detects the audio's voice has stopped or paused, it ceases speech recognition and sends a `StreamingDetectIntentResponse` with a recognition result of `END_OF_SINGLE_UTTERANCE` to your client. Any audio sent to Dialogflow on the stream after receipt of `END_OF_SINGLE_UTTERANCE` is ignored by Dialogflow.



In bidirectional streaming, a client can _half-close_ the stream object to signal to the server that it won't send more data. For example, in Java and Go, this method is called `closeSend`.

It's important to half-close (but not abort) streams in the following situations:

  * Your client has finished sending data.
  * Your client is configured with `single_utterance` set to `true`, and it receives a `StreamingDetectIntentResponse` with a recognition result of `END_OF_SINGLE_UTTERANCE`.



After closing a stream, your client should start a new request with a new stream as needed.

## Streaming detect intent

The following samples use the [`Session`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#sessions) type's `streamingDetectIntent` method to stream audio.

### Go

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func DetectIntentStream(projectID, sessionID, audioFile, languageCode string) (string, error) {
    	ctx := context.Background()
    
    	sessionClient, err := dialogflow.NewSessionsClient(ctx)
    	if err != nil {
    		return "", err
    	}
    	defer sessionClient.Close()
    
    	if projectID == "" || sessionID == "" {
    		return "", fmt.Errorf("detect.DetectIntentStream empty project (%s) or session (%s)", projectID, sessionID)
    	}
    
    	sessionPath := fmt.Sprintf("projects/%s/agent/sessions/%s", projectID, sessionID)
    
    	// In this example, we hard code the encoding and sample rate for simplicity.
    	audioConfig := dialogflowpb.InputAudioConfig{AudioEncoding: dialogflowpb.AudioEncoding_AUDIO_ENCODING_LINEAR_16, SampleRateHertz: 16000, LanguageCode: languageCode}
    
    	queryAudioInput := dialogflowpb.QueryInput_AudioConfig{AudioConfig: &audioConfig}
    
    	queryInput := dialogflowpb.QueryInput{Input: &queryAudioInput}
    
    	streamer, err := sessionClient.StreamingDetectIntent(ctx)
    	if err != nil {
    		return "", err
    	}
    
    	f, err := os.Open(audioFile)
    	if err != nil {
    		return "", err
    	}
    
    	defer f.Close()
    
    	go func() {
    		audioBytes := make([]byte, 1024)
    
    		request := dialogflowpb.StreamingDetectIntentRequest{Session: sessionPath, QueryInput: &queryInput}
    		err = streamer.Send(&request)
    		if err != nil {
    			log.Fatal(err)
    		}
    
    		for {
    			_, err := f.Read(audioBytes)
    			if err == io.EOF {
    				streamer.CloseSend()
    				break
    			}
    			if err != nil {
    				log.Fatal(err)
    			}
    
    			request = dialogflowpb.StreamingDetectIntentRequest{InputAudio: audioBytes}
    			err = streamer.Send(&request)
    			if err != nil {
    				log.Fatal(err)
    			}
    		}
    	}()
    
    	var queryResult *dialogflowpb.QueryResult
    
    	for {
    		response, err := streamer.Recv()
    		if err == io.EOF {
    			break
    		}
    		if err != nil {
    			log.Fatal(err)
    		}
    
    		recognitionResult := response.GetRecognitionResult()
    		transcript := recognitionResult.GetTranscript()
    		log.Printf("Recognition transcript: %s\n", transcript)
    
    		queryResult = response.GetQueryResult()
    	}
    
    	fulfillmentText := queryResult.GetFulfillmentText()
    	return fulfillmentText, nil
    }
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[BidiStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream.html);
    import com.google.cloud.dialogflow.v2.[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AudioEncoding.html);
    import com.google.cloud.dialogflow.v2.[InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.InputAudioConfig.html);
    import com.google.cloud.dialogflow.v2.[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html);
    import com.google.cloud.dialogflow.v2.[QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html);
    import com.google.cloud.dialogflow.v2.[SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html);
    import com.google.cloud.dialogflow.v2.[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html);
    import com.google.cloud.dialogflow.v2.[StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingDetectIntentRequest.html);
    import com.google.cloud.dialogflow.v2.[StreamingDetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingDetectIntentResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    
    class DetectIntentStream {
    
      // DialogFlow API Detect Intent sample with audio files processes as an audio stream.
      static void detectIntentStream(String projectId, String audioFilePath, String sessionId)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
        // String projectId = "YOUR_PROJECT_ID";
        // String audioFilePath = "path_to_your_audio_file";
        // Using the same `sessionId` between requests allows continuation of the conversation.
        // String sessionId = "Identifier of the DetectIntent session";
    
        // Instantiates a client
        try ([SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html) sessionsClient = [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html).create()) {
          // Set the session name using the sessionId (UUID) and projectID (my-project-id)
          [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html) session = [SessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html).of(projectId, sessionId);
    
          // Instructs the speech recognizer how to process the audio content.
          // Note: hard coding audioEncoding and sampleRateHertz for simplicity.
          // Audio encoding of the audio content sent in the query request.
          [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.InputAudioConfig.html) inputAudioConfig =
              [InputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.InputAudioConfig.html).newBuilder()
                  .setAudioEncoding([AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AudioEncoding.html).AUDIO_ENCODING_LINEAR_16)
                  .setLanguageCode("en-US") // languageCode = "en-US"
                  .setSampleRateHertz(16000) // sampleRateHertz = 16000
                  .build();
    
          // Build the query with the InputAudioConfig
          [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html) queryInput = [QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryInput.html).newBuilder().setAudioConfig(inputAudioConfig).build();
    
          // Create the Bidirectional stream
          BidiStream<StreamingDetectIntentRequest, StreamingDetectIntentResponse> bidiStream =
              sessionsClient.[streamingDetectIntentCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionsClient.html#com_google_cloud_dialogflow_v2_SessionsClient_streamingDetectIntentCallable__)().call();
    
          // The first request must **only** contain the audio configuration:
          bidiStream.send(
              [StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingDetectIntentRequest.html).newBuilder()
                  .setSession(session.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionName.html#com_google_cloud_dialogflow_v2_SessionName_toString__)())
                  .setQueryInput(queryInput)
                  .build());
    
          try (FileInputStream audioStream = new FileInputStream(audioFilePath)) {
            // Subsequent requests must **only** contain the audio data.
            // Following messages: audio chunks. We just read the file in fixed-size chunks. In reality
            // you would split the user input by time.
            byte[] buffer = new byte[4096];
            int bytes;
            while ((bytes = audioStream.read(buffer)) != -1) {
              bidiStream.send(
                  [StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingDetectIntentRequest.html).newBuilder()
                      .setInputAudio([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(buffer, 0, bytes))
                      .build());
            }
          }
    
          // Tell the service you are done sending data
          bidiStream.closeSend();
    
          for ([StreamingDetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingDetectIntentResponse.html) response : bidiStream) {
            [QueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html) queryResult = response.getQueryResult();
            System.out.println("====================");
            System.out.format("Intent Display Name: %s\n", queryResult.[getIntent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getIntent__)().getDisplayName());
            System.out.format("Query Text: '%s'\n", queryResult.[getQueryText](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getQueryText__)());
            System.out.format(
                "Detected Intent: %s (confidence: %f)\n",
                queryResult.[getIntent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getIntent__)().getDisplayName(), queryResult.[getIntentDetectionConfidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getIntentDetectionConfidence__)());
            System.out.format(
                "Fulfillment Text: '%s'\n",
                queryResult.[getFulfillmentMessagesCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getFulfillmentMessagesCount__)() > 0
                    ? queryResult.[getFulfillmentMessages](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResult.html#com_google_cloud_dialogflow_v2_QueryResult_getFulfillmentMessages_int_)(0).getText()
                    : "Triggered Default Fallback Intent");
          }
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    const util = require('util');
    const {Transform, pipeline} = require('stream');
    const {struct} = require('pb-util');
    
    const pump = util.promisify(pipeline);
    // Imports the Dialogflow library
    const dialogflow = require('[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)');
    
    // Instantiates a session client
    const sessionClient = new dialogflow.[SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    // The path to the local file on which to perform speech recognition, e.g.
    // /path/to/audio.raw const filename = '/path/to/audio.raw';
    
    // The encoding of the audio file, e.g. 'AUDIO_ENCODING_LINEAR_16'
    // const encoding = 'AUDIO_ENCODING_LINEAR_16';
    
    // The sample rate of the audio file in hertz, e.g. 16000
    // const sampleRateHertz = 16000;
    
    // The BCP-47 language code to use, e.g. 'en-US'
    // const languageCode = 'en-US';
    const sessionPath = sessionClient.projectAgentSessionPath(
      projectId,
      sessionId
    );
    
    const initialStreamRequest = {
      session: sessionPath,
      queryInput: {
        audioConfig: {
          audioEncoding: encoding,
          sampleRateHertz: sampleRateHertz,
          languageCode: languageCode,
        },
      },
    };
    
    // Create a stream for the streaming request.
    const detectStream = sessionClient
      .streamingDetectIntent()
      .on('error', console.error)
      .on('data', data => {
        if (data.recognitionResult) {
          console.log(
            `Intermediate transcript: ${data.recognitionResult.transcript}`
          );
        } else {
          console.log('Detected intent:');
    
          const result = data.queryResult;
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
        }
      });
    
    // Write the initial stream request to config for audio input.
    detectStream.write(initialStreamRequest);
    
    // Stream an audio file from disk to the Conversation API, e.g.
    // "./resources/audio.raw"
    await pump(
      fs.createReadStream(filename),
      // Format the audio stream into the request format.
      new Transform({
        objectMode: true,
        transform: (obj, _, next) => {
          next(null, {inputAudio: obj});
        },
      }),
      detectStream
    );

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_intent_stream(project_id, session_id, audio_file_path, language_code):
        """Returns the result of detect intent with streaming audio as input.
    
        Using the same `session_id` between requests allows continuation
        of the conversation."""
        from google.cloud import dialogflow
    
        session_client = dialogflow.SessionsClient()
    
        # Note: hard coding audio_encoding and sample_rate_hertz for simplicity.
        audio_encoding = dialogflow.AudioEncoding.AUDIO_ENCODING_LINEAR_16
        sample_rate_hertz = 16000
    
        session_path = session_client.[session_path](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsClient.html#google_cloud_dialogflow_v2_services_sessions_SessionsClient_session_path)(project_id, session_id)
        print("Session path: {}\n".format(session_path))
    
        def request_generator(audio_config, audio_file_path):
            query_input = dialogflow.[QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryInput.html)(audio_config=audio_config)
    
            # The first request contains the configuration.
            yield dialogflow.[StreamingDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingDetectIntentRequest.html)(
                session=session_path, query_input=query_input
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
                    yield dialogflow.[StreamingDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingDetectIntentRequest.html)(input_audio=chunk)
    
        audio_config = dialogflow.[InputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InputAudioConfig.html)(
            audio_encoding=audio_encoding,
            language_code=language_code,
            sample_rate_hertz=sample_rate_hertz,
        )
    
        requests = request_generator(audio_config, audio_file_path)
        responses = session_client.[streaming_detect_intent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsClient.html#google_cloud_dialogflow_v2_services_sessions_SessionsClient_streaming_detect_intent)(requests=requests)
    
        print("=" * 20)
        for response in responses:
            print(
                'Intermediate transcript: "{}".'.format(
                    response.recognition_result.transcript
                )
            )
            # Note: Since Python gRPC doesn't have closeSend method, to stop processing the audio after result is recognized,
            # you may close the channel manually to prevent further iteration.
            # Keep in mind that if there is a silence chunk in the audio, part after it might be missed because of early teardown.
            # https://cloud.google.com/dialogflow/es/docs/how/detect-intent-stream#streaming_basics
            if response.recognition_result.is_final:
                session_client.transport.close()
                break
    
        # Note: The result from the last response is the final transcript along
        # with the detected content.
        query_result = response.query_result
    
        print("=" * 20)
        print("Query text: {}".format(query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                query_result.intent.display_name, query_result.intent_detection_confidence
            )
        )
        print("Fulfillment text: {}\n".format(query_result.fulfillment_text))
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/dialogflow/docs/reference/libraries) on the client libraries page and then visit the [Dialogflow CX reference documentation for .NET.](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/dialogflow/docs/reference/libraries) on the client libraries page and then visit the [Dialogflow CX reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-dialogflow/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/dialogflow/docs/reference/libraries) on the client libraries page and then visit the [Dialogflow CX reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-dialogflow/latest/Google/Cloud/Dialogflow.html)

## Samples

For more information about best practices on streaming from a browser microphone to Dialogflow, see the [Samples page](https://docs.cloud.google.com/dialogflow/docs/tutorials/samples).

[ Previous arrow_back  Detect intent with audio input file  ](https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-audio)

[ Next Detect intent with audio output  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-tts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
