---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-model-selection/
title: Transcribe a local file using a transcription model \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:03.192203+00:00
---

# Transcribe a local file using a transcription model  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-model-selection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe a local file using a transcription model Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe a local audio file using a trained transcription model.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Select a transcription model](https://docs.cloud.google.com/speech-to-text/docs/v1/transcription-model)
  * [Transcribe audio from a video file using Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-audio-from-video-speech-to-text)



## Code sample

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func modelSelection(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := speech.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	data, err := os.ReadFile("../testdata/Google_Gnome.wav")
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	req := &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:        speechpb.RecognitionConfig_LINEAR16,
    			SampleRateHertz: 16000,
    			LanguageCode:    "en-US",
    			Model:           "video",
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Content{Content: data},
    		},
    	}
    
    	resp, err := client.Recognize(ctx, req)
    	if err != nil {
    		return fmt.Errorf("recognize: %w", err)
    	}
    
    	for i, result := range resp.Results {
    		fmt.Fprintf(w, "%s\n", strings.Repeat("-", 20))
    		fmt.Fprintf(w, "Result %d\n", i+1)
    		for j, alternative := range result.Alternatives {
    			fmt.Fprintf(w, "Alternative %d: %s\n", j+1, alternative.Transcript)
    		}
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs transcription of the given audio file synchronously with the selected model.
     *
     * @param fileName the path to a audio file to transcribe
     */
    public static void transcribeModelSelection(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      byte[] content = Files.readAllBytes(path);
    
      try (SpeechClient speech = SpeechClient.create()) {
        // Configure request with video media type
        RecognitionConfig recConfig =
            RecognitionConfig.newBuilder()
                // encoding may either be omitted or must match the value in the file header
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                // sample rate hertz may be either be omitted or must match the value in the file
                // header
                .setSampleRateHertz(16000)
                .setModel("video")
                .build();
    
        RecognitionAudio recognitionAudio =
            RecognitionAudio.newBuilder().setContent(ByteString.copyFrom(content)).build();
    
        RecognizeResponse recognizeResponse = speech.recognize(recConfig, recognitionAudio);
        // Just print the first result here.
        SpeechRecognitionResult result = recognizeResponse.getResultsList().get(0);
        // There can be several alternative transcripts for a given chunk of speech. Just use the
        // first (most likely) one here.
        SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
        System.out.printf("Transcript : %s\n", alternative.getTranscript());
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library for Beta API
    /**
     * TODO(developer): Update client library import to use new
     * version of API when desired features become available
     */
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    const fs = require('fs');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const filename = 'Local path to audio file, e.g. /path/to/audio.raw';
    // const model = 'Model to use, e.g. phone_call, video, default';
    // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    const config = {
      encoding: encoding,
      sampleRateHertz: sampleRateHertz,
      languageCode: languageCode,
      model: model,
    };
    const audio = {
      content: fs.readFileSync(filename).toString('base64'),
    };
    
    const request = {
      config: config,
      audio: audio,
    };
    
    // Detects speech in the audio file
    const [response] = await client.recognize(request);
    const transcription = response.results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    console.log('Transcription: ', transcription);

### PHP

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Speech\V2\Client\SpeechClient;
    use Google\Cloud\Speech\V2\RecognizeRequest;
    use Google\Cloud\Speech\V2\RecognitionConfig;
    use Google\Cloud\Speech\V2\AutoDetectDecodingConfig;
    
    /**
     * @param string $projectId The Google Cloud project ID.
     * @param string $location The location of the recognizer.
     * @param string $recognizerId The ID of the recognizer to use.
     * @param string $audioFile path to an audio file.
     * @param string $model The recognition model to use.
     */
    function transcribe_model_selection(string $projectId, string $location, string $recognizerId, string $audioFile, string $model)
    {
        // create the speech client
        $apiEndpoint = $location === 'global' ? null : sprintf('%s-speech.googleapis.com', $location);
        $speech = new SpeechClient(['apiEndpoint' => $apiEndpoint]);
    
        // get contents of a file into a string
        $content = file_get_contents($audioFile);
    
        $recognizerName = SpeechClient::recognizerName($projectId, $location, $recognizerId);
    
        // set config
        $config = (new RecognitionConfig())
            ->setModel($model)
    
            // Can also use {@see Google\Cloud\Speech\V2\ExplicitDecodingConfig}
            // ->setExplicitDecodingConfig(new ExplicitDecodingConfig([...]);
    
            ->setAutoDecodingConfig(new AutoDetectDecodingConfig());
    
        $request = (new RecognizeRequest())
            ->setRecognizer($recognizerName)
            ->setConfig($config)
            ->setContent($content);
    
        // make the API call
        $response = $speech->recognize($request);
        $results = $response->getResults();
    
        // print results
        foreach ($results as $result) {
            $alternatives = $result->getAlternatives();
            $mostLikely = $alternatives[0];
            $transcript = $mostLikely->getTranscript();
            $confidence = $mostLikely->getConfidence();
            printf('Transcript: %s' . PHP_EOL, $transcript);
            printf('Confidence: %s' . PHP_EOL, $confidence);
        }
    
        $speech->close();
    }

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    
    # Instantiates a client
    client = speech.SpeechClient()
    # Reads a file as bytes
    with open("resources/Google_Gnome.wav", "rb") as f:
        audio_content = f.read()
    
    audio = speech.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionAudio.html)(content=audio_content)
    
    config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        model="video",  # Chosen model
    )
    
    response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
    

### Ruby

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # file_path = "path/to/audio.wav"
    
    require "google/cloud/speech"
    
    speech = Google::Cloud::[Speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html).[speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html) version: :v1
    
    config = {
      encoding:          :LINEAR16,
      sample_rate_hertz: 16_000,
      language_code:     "en-US",
      model:             model
    }
    
    file  = File.binread file_path
    audio = { content: file }
    
    operation = speech.long_running_recognize config: config, audio: audio
    
    puts "Operation started"
    
    operation.wait_until_done!
    
    raise operation.results.message if operation.error?
    
    results = operation.response.results
    
    results.each_with_index do |result, i|
      alternative = result.alternatives.first
      puts "-" * 20
      puts "First alternative of result #{i}"
      puts "Transcript: #{alternative.transcript}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
