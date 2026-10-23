---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-diarization-beta/
title: Transcription of a local file with diarization \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:00.116915+00:00
---

# Transcription of a local file with diarization  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-diarization-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcription of a local file with diarization Stay organized with collections  Save and categorize content based on your preferences. 

Recognize multiple speakers in a local audio file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect different speakers in an audio recording](https://docs.cloud.google.com/speech-to-text/docs/multiple-voices)
  * [Detect different speakers in an audio recording](https://docs.cloud.google.com/speech-to-text/docs/v1/multiple-voices)



## Code sample

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    	"strings"
    
    	speech "cloud.google.com/go/speech/apiv1"
    	"cloud.google.com/go/speech/apiv1/speechpb"
    )
    
    // transcribe_diarization_gcs_beta Transcribes a remote audio file using speaker diarization.
    func transcribe_diarization(w io.Writer) error {
    
    	ctx := context.Background()
    	client, err := speech.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1.html#cloud_google_com_go_speech_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	diarizationConfig := &speechpb.SpeakerDiarizationConfig{
    		EnableSpeakerDiarization: true,
    		MinSpeakerCount:          2,
    		MaxSpeakerCount:          2,
    	}
    
    	recognitionConfig := &speechpb.RecognitionConfig{
    		Encoding:          speechpb.[RecognitionConfig_LINEAR16](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1/speechpb.html#cloud_google_com_go_speech_apiv1_speechpb_RecognitionConfig_ENCODING_UNSPECIFIED_RecognitionConfig_LINEAR16_RecognitionConfig_FLAC_RecognitionConfig_MULAW_RecognitionConfig_AMR_RecognitionConfig_AMR_WB_RecognitionConfig_OGG_OPUS_RecognitionConfig_SPEEX_WITH_HEADER_BYTE_RecognitionConfig_MP3_RecognitionConfig_WEBM_OPUS),
    		SampleRateHertz:   8000,
    		LanguageCode:      "en-US",
    		DiarizationConfig: diarizationConfig,
    	}
    
    	// Get the contents of the local audio file
    	content, err := os.ReadFile("../resources/commercial_mono.wav")
    	if err != nil {
    		return fmt.Errorf("error reading file %w", err)
    	}
    	audio := &speechpb.RecognitionAudio{
    		AudioSource: &speechpb.RecognitionAudio_Content{Content: content},
    	}
    
    	longRunningRecognizeRequest := &speechpb.LongRunningRecognizeRequest{
    		Config: recognitionConfig,
    		Audio:  audio,
    	}
    
    	operation, err := client.LongRunningRecognize(ctx, longRunningRecognizeRequest)
    	if err != nil {
    		return fmt.Errorf("error running recognize %w", err)
    	}
    
    	response, err := operation.[Wait](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1.html#cloud_google_com_go_speech_apiv1_LongRunningRecognizeOperation_Wait)(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Speaker Tags are only included in the last result object, which has only one
    	// alternative.
    	alternative := response.Results[len(response.Results)-1].Alternatives[0]
    
    	wordInfo := alternative.GetWords()[0]
    	currentSpeakerTag := wordInfo.GetSpeakerTag()
    
    	var speakerWords strings.Builder
    
    	speakerWords.WriteString(fmt.Sprintf("Speaker %d: %s", wordInfo.GetSpeakerTag(), wordInfo.GetWord()))
    
    	// For each word, get all the words associated with one speaker, once the speaker changes,
    	// add a new line with the new speaker and their spoken words.
    	for i := 1; i < len(alternative.Words); i++ {
    		wordInfo := alternative.Words[i]
    		if currentSpeakerTag == wordInfo.GetSpeakerTag() {
    			speakerWords.WriteString(" ")
    			speakerWords.WriteString(wordInfo.GetWord())
    		} else {
    			speakerWords.WriteString(fmt.Sprintf("\nSpeaker %d: %s",
    				wordInfo.GetSpeakerTag(), wordInfo.GetWord()))
    			currentSpeakerTag = wordInfo.GetSpeakerTag()
    		}
    	}
    	fmt.Fprint(w, speakerWords.String())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe the given audio file using speaker diarization.
     *
     * @param fileName the path to an audio file.
     */
    public static void transcribeDiarization(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      byte[] content = Files.readAllBytes(path);
    
      try (SpeechClient speechClient = SpeechClient.create()) {
        // Get the contents of the local audio file
        RecognitionAudio recognitionAudio =
            RecognitionAudio.newBuilder().setContent(ByteString.copyFrom(content)).build();
    
        SpeakerDiarizationConfig speakerDiarizationConfig =
            SpeakerDiarizationConfig.newBuilder()
                .setEnableSpeakerDiarization(true)
                .setMinSpeakerCount(2)
                .setMaxSpeakerCount(2)
                .build();
    
        // Configure request to enable Speaker diarization
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                .setSampleRateHertz(8000)
                .setDiarizationConfig(speakerDiarizationConfig)
                .build();
    
        // Perform the transcription request
        RecognizeResponse recognizeResponse = speechClient.recognize(config, recognitionAudio);
    
        // Speaker Tags are only included in the last result object, which has only one alternative.
        SpeechRecognitionAlternative alternative =
            recognizeResponse.getResults(recognizeResponse.getResultsCount() - 1).getAlternatives(0);
    
        // The alternative is made up of WordInfo objects that contain the speaker_tag.
        WordInfo wordInfo = alternative.getWords(0);
        int currentSpeakerTag = wordInfo.getSpeakerTag();
    
        // For each word, get all the words associated with one speaker, once the speaker changes,
        // add a new line with the new speaker and their spoken words.
        StringBuilder speakerWords =
            new StringBuilder(
                String.format("Speaker %d: %s", wordInfo.getSpeakerTag(), wordInfo.getWord()));
    
        for (int i = 1; i < alternative.getWordsCount(); i++) {
          wordInfo = alternative.getWords(i);
          if (currentSpeakerTag == wordInfo.getSpeakerTag()) {
            speakerWords.append(" ");
            speakerWords.append(wordInfo.getWord());
          } else {
            speakerWords.append(
                String.format("\nSpeaker %d: %s", wordInfo.getSpeakerTag(), wordInfo.getWord()));
            currentSpeakerTag = wordInfo.getSpeakerTag();
          }
        }
    
        System.out.println(speakerWords.toString());
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
      sampleRateHertz: 8000,
      languageCode: 'en-US',
      enableSpeakerDiarization: true,
      minSpeakerCount: 2,
      maxSpeakerCount: 2,
      model: 'phone_call',
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
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    console.log(`Transcription: ${transcription}`);
    console.log('Speaker Diarization:');
    const result = response.results[response.results.length - 1];
    const wordsInfo = result.alternatives[0].words;
    // Note: The transcript within each result is separate and sequential per result.
    // However, the words list within an alternative includes all the words
    // from all the results thus far. Thus, to get all the words with speaker
    // tags, you only have to take the words list from the last result:
    wordsInfo.forEach(a =>
      console.log(` word: ${a.word}, speakerTag: ${a.speakerTag}`)
    );

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    
    client = speech.SpeechClient()
    
    speech_file = "resources/commercial_mono.wav"
    
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    
    diarization_config = speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,
        min_speaker_count=2,
        max_speaker_count=10,
    )
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code="en-US",
        diarization_config=diarization_config,
    )
    
    print("Waiting for operation to complete...")
    response = client.recognize(config=config, audio=audio)
    
    # The transcript within each result is separate and sequential per result.
    # However, the words list within an alternative includes all the words
    # from all the results thus far. Thus, to get all the words with speaker
    # tags, you only have to take the words list from the last result:
    result = response.results[-1]
    
    words_info = result.alternatives[0].words
    
    # Printing out the output:
    for word_info in words_info:
        print(f"word: '{word_info.word}', speaker_tag: {word_info.speaker_tag}")
    
    return result

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
