---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-sync-gcs/
title: Synchronously transcribe a Cloud Storage file \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:58.425685+00:00
---

# Synchronously transcribe a Cloud Storage file  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-sync-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Synchronously transcribe a Cloud Storage file Stay organized with collections  Save and categorize content based on your preferences. 

Perform a synchronous transcription on an audio file stored in Cloud Storage

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transcribe short audio files](https://docs.cloud.google.com/speech-to-text/docs/v1/sync-recognize)



## Code sample

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func recognizeGCS(w io.Writer, gcsURI string) error {
    	ctx := context.Background()
    
    	client, err := speech.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	// Send the request with the URI (gs://...)
    	// and sample rate information to be transcripted.
    	resp, err := client.Recognize(ctx, &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:        speechpb.RecognitionConfig_LINEAR16,
    			SampleRateHertz: 16000,
    			LanguageCode:    "en-US",
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Uri{Uri: gcsURI},
    		},
    	})
    
    	// Print the results.
    	for _, result := range resp.Results {
    		for _, alt := range result.Alternatives {
    			fmt.Fprintf(w, "\"%v\" (confidence=%3f)\n", alt.Transcript, alt.Confidence)
    		}
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs speech recognition on remote FLAC file and prints the transcription.
     *
     * @param gcsUri the path to the remote FLAC audio file to transcribe.
     */
    public static void syncRecognizeGcs(String gcsUri) throws Exception {
      // Instantiates a client with GOOGLE_APPLICATION_CREDENTIALS
      try (SpeechClient speech = SpeechClient.create()) {
        // Builds the request for remote FLAC file
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.FLAC)
                .setLanguageCode("en-US")
                .setSampleRateHertz(16000)
                .build();
        RecognitionAudio audio = RecognitionAudio.newBuilder().setUri(gcsUri).build();
    
        // Use blocking call for getting audio transcript
        RecognizeResponse response = speech.recognize(config, audio);
        List<SpeechRecognitionResult> results = response.getResultsList();
    
        for (SpeechRecognitionResult result : results) {
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
          System.out.printf("Transcription: %s%n", alternative.getTranscript());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const gcsUri = 'gs://my-bucket/audio.raw';
    // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    const config = {
      encoding: encoding,
      sampleRateHertz: sampleRateHertz,
      languageCode: languageCode,
    };
    const audio = {
      uri: gcsUri,
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
    use Google\Cloud\Speech\V2\RecognitionConfig;
    use Google\Cloud\Speech\V2\ExplicitDecodingConfig;
    use Google\Cloud\Speech\V2\ExplicitDecodingConfig\AudioEncoding;
    use Google\Cloud\Speech\V2\RecognizeRequest;
    
    /**
     * @param string $projectId The Google Cloud project ID.
     * @param string $location The location of the recognizer.
     * @param string $recognizerId The ID of the recognizer to use.
     * @param string $uri The Cloud Storage object to transcribe (gs://your-bucket-name/your-object-name)
     */
    function transcribe_sync_gcs(string $projectId, string $location, string $recognizerId, string $uri)
    {
        // create the speech client
        $apiEndpoint = $location === 'global' ? null : sprintf('%s-speech.googleapis.com', $location);
        $speech = new SpeechClient(['apiEndpoint' => $apiEndpoint]);
    
        $recognizerName = SpeechClient::recognizerName($projectId, $location, $recognizerId);
    
        $config = (new RecognitionConfig())
            // Can also use {@see Google\Cloud\Speech\V2\AutoDetectDecodingConfig}
            // ->setAutoDecodingConfig(new AutoDetectDecodingConfig());
    
            ->setExplicitDecodingConfig(new ExplicitDecodingConfig([
                // change these variables if necessary
                'encoding' => AudioEncoding::LINEAR16,
                'sample_rate_hertz' => 16000,
                'audio_channel_count' => 1,
            ]));
    
        $request = (new RecognizeRequest())
            ->setRecognizer($recognizerName)
            ->setConfig($config)
            ->setUri($uri);
    
        try {
            $response = $speech->recognize($request);
            foreach ($response->getResults() as $result) {
                $alternatives = $result->getAlternatives();
                $mostLikely = $alternatives[0];
                $transcript = $mostLikely->getTranscript();
                $confidence = $mostLikely->getConfidence();
                printf('Transcript: %s' . PHP_EOL, $transcript);
                printf('Confidence: %s' . PHP_EOL, $confidence);
            }
        } finally {
            $speech->close();
        }
    }

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def transcribe_gcs(audio_uri: str) -> speech.RecognizeResponse:
        """Transcribes the audio file specified by the gcs_uri.
        Args:
            audio_uri (str): The Google Cloud Storage URI of the input audio file.
                E.g., gs://cloud-samples-data/speech/audio.flac
        Returns:
            cloud_speech.RecognizeResponse: The response containing the transcription results
        """
        from google.cloud import speech
    
        client = speech.SpeechClient()
    
        audio = speech.RecognitionAudio(uri=audio_uri)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
    
        response = client.recognize(config=config, audio=audio)
    
        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # storage_path = "Path to file in Cloud Storage, eg. gs://bucket/audio.raw"
    
    require "google/cloud/speech"
    
    speech = Google::Cloud::[Speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html).[speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html) version: :v1
    
    config = { encoding:          :LINEAR16,
               sample_rate_hertz: 16_000,
               language_code:     "en-US" }
    audio  = { uri: storage_path }
    
    response = speech.recognize config: config, audio: audio
    
    results = response.results
    
    alternatives = results.first.alternatives
    alternatives.each do |alternative|
      puts "Transcription: #{alternative.transcript}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
