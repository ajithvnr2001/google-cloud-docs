---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-multichannel-beta/
title: Transcribe a local multi-channel file (beta) \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:40.726765+00:00
---

# Transcribe a local multi-channel file (beta)  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-multichannel-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe a local multi-channel file (beta) Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe a local audio file that includes more than one channel.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transcribe audio with multiple channels](https://docs.cloud.google.com/speech-to-text/docs/v1/multi-channel)



## Code sample

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // transcribeMultichannel generates a transcript from a multichannel speech file and tags the speech from each channel.
    func transcribeMultichannel(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := speech.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	data, err := os.ReadFile("../testdata/commercial_stereo.wav")
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	resp, err := client.Recognize(ctx, &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:                            speechpb.RecognitionConfig_LINEAR16,
    			SampleRateHertz:                     44100,
    			LanguageCode:                        "en-US",
    			AudioChannelCount:                   2,
    			EnableSeparateRecognitionPerChannel: true,
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Content{Content: data},
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("Recognize: %w", err)
    	}
    
    	// Print the results.
    	for _, result := range resp.Results {
    		for _, alt := range result.Alternatives {
    			fmt.Fprintf(w, "Channel %v: %v\n", result.ChannelTag, alt.Transcript)
    		}
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe a local audio file with multi-channel recognition
     *
     * @param fileName the path to local audio file
     */
    public static void transcribeMultiChannel(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      byte[] content = Files.readAllBytes(path);
    
      try (SpeechClient speechClient = SpeechClient.create()) {
        // Get the contents of the local audio file
        RecognitionAudio recognitionAudio =
            RecognitionAudio.newBuilder().setContent(ByteString.copyFrom(content)).build();
    
        // Configure request to enable multiple channels
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                .setSampleRateHertz(44100)
                .setAudioChannelCount(2)
                .setEnableSeparateRecognitionPerChannel(true)
                .build();
    
        // Perform the transcription request
        RecognizeResponse recognizeResponse = speechClient.recognize(config, recognitionAudio);
    
        // Print out the results
        for (SpeechRecognitionResult result : recognizeResponse.getResultsList()) {
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternatives(0);
          System.out.format("Transcript : %s\n", alternative.getTranscript());
          System.out.printf("Channel Tag : %s\n\n", result.getChannelTag());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const fileName = 'Local path to audio file, e.g. /path/to/audio.raw';
    
    const config = {
      encoding: 'LINEAR16',
      languageCode: 'en-US',
      audioChannelCount: 2,
      enableSeparateRecognitionPerChannel: true,
    };
    
    const audio = {
      content: fs.readFileSync(fileName).toString('base64'),
    };
    
    const request = {
      config: config,
      audio: audio,
    };
    
    const [response] = await client.recognize(request);
    const transcription = response.results
      .map(
        result =>
          ` Channel Tag: ${result.channelTag} ${result.alternatives[0].transcript}`
      )
      .join('\n');
    console.log(`Transcription: \n${transcription}`);

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    
    client = speech.SpeechClient()
    
    speech_file = "resources/Google_Gnome.wav"
    
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        audio_channel_count=1,
        enable_separate_recognition_per_channel=True,
    )
    
    response = client.recognize(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
        print(f"Channel Tag: {result.channel_tag}")
    
    return response.results

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
