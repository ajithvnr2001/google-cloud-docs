---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/multiple-voices/
title: Detect different speakers in an audio recording \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:40.631570+00:00
---

# Detect different speakers in an audio recording  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/multiple-voices/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Detect different speakers in an audio recording Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to get labels for different speakers in audio data transcribed by Cloud Speech-to-Text.

Sometimes, audio data contains samples of more than one person talking. For example, audio from a telephone call usually features voices from two or more people. A transcription of the call ideally includes who speaks at which times.

## Speaker diarization

Cloud Speech-to-Text can recognize multiple speakers in the same audio clip. When you send an audio transcription request to Cloud Speech-to-Text, you can include a parameter telling Cloud Speech-to-Text to identify the different speakers in the audio sample. This feature, called _speaker diarization_ , detects when speakers change and labels by number the individual voices detected in the audio.

When you enable speaker diarization in your transcription request, Cloud Speech-to-Text attempts to distinguish the different voices included in the audio sample. The transcription result tags each word with a number assigned to individual speakers. Words spoken by the same speaker bear the same number. A transcription result can include numbers up to as many speakers as Cloud Speech-to-Text can uniquely identify in the audio sample.

When you use speaker diarization, Cloud Speech-to-Text produces a running aggregate of all the results provided in the transcription. Each result includes the words from the previous result. Thus, the `words` array in the final result provides the complete, diarized results of the transcription.

Review the [language support page](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) to see if this feature is available for your language.

## Enable speaker diarization in a request

To enable speaker diarization, you need to set the `enableSpeakerDiarization` field to `true` in the [`SpeakerDiarizationConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeakerDiarizationConfig) parameters for the request. To improve your transcription results, you should also specify the number of speakers present in the audio clip by setting the `diarizationSpeakerCount` field in the [`SpeakerDiarizationConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeakerDiarizationConfig) parameters. Cloud Speech-to-Text uses a default value if you do not provide a value for `diarizationSpeakerCount`.

Cloud STT supports speaker diarization for all speech recognition methods: [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize) [`speech:longrunningrecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/longrunningrecognize), and [Streaming](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeRequest).

### Use a local file

The following code snippet demonstrates how to enable speaker diarization in a transcription request to Cloud Speech-to-Text using a local file

### Protocol

Refer to the [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 
    
    
    curl -s -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        https://speech.googleapis.com/v1p1beta1/speech:recognize \
        --data '{
        "config": {
            "encoding": "LINEAR16",
            "languageCode": "en-US",
    **"diarizationConfig": {**
    **"enableSpeakerDiarization": true,**
              "minSpeakerCount": 2,
              "maxSpeakerCount": 2
            },                    
            "model": "phone_call",
        }, 
        "audio": {
            "uri": "gs://cloud-samples-tests/speech/commercial_mono.wav"
        }
    }' > speaker-diarization.txt

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format, saved to a file named `speaker-diarization.txt`.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "hi I'd like to buy a Chromecast and I was wondering whether you could help me with that certainly which color would you like we have blue black and red uh let's go with the black one would you like the new Chromecast Ultra model or the regular Chrome Cast regular Chromecast is fine thank you okay sure we like to ship it regular or Express Express please terrific it's on the way thank you thank you very much bye",
              "confidence": 0.92142606,
              "words": [
                {
                  "startTime": "0s",
                  "endTime": "1.100s",
                  "word": "hi",
                  "speakerTag": 2
                },
                {
                  "startTime": "1.100s",
                  "endTime": "2s",
                  "word": "I'd",
                  "speakerTag": 2
                },
                {
                  "startTime": "2s",
                  "endTime": "2s",
                  "word": "like",
                  "speakerTag": 2
                },
                {
                  "startTime": "2s",
                  "endTime": "2.100s",
                  "word": "to",
                  "speakerTag": 2
                },
                ...
                {
                  "startTime": "6.500s",
                  "endTime": "6.900s",
                  "word": "certainly",
                  "speakerTag": 1
                },
                {
                  "startTime": "6.900s",
                  "endTime": "7.300s",
                  "word": "which",
                  "speakerTag": 1
                },
                {
                  "startTime": "7.300s",
                  "endTime": "7.500s",
                  "word": "color",
                  "speakerTag": 1
                },
                ...
              ]
            }
          ],
          "languageCode": "en-us"
        }
      ]
    }

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

### Use a Cloud Storage bucket

The following code snippet demonstrates how to enable speaker diarization in a transcription request to Cloud Speech-to-Text using a Cloud Storage file

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    
    	speech "cloud.google.com/go/speech/apiv1"
    	"cloud.google.com/go/speech/apiv1/speechpb"
    )
    
    // transcribe_diarization_gcs_beta Transcribes a remote audio file using speaker diarization.
    func transcribe_diarization_gcs_beta(w io.Writer) error {
    	// Google Cloud Storage URI pointing to the audio content.
    
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
    
    	// Set the remote path for the audio file
    	audio := &speechpb.RecognitionAudio{
    		AudioSource: &speechpb.RecognitionAudio_Uri{Uri: "gs://cloud-samples-tests/speech/commercial_mono.wav"},
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
     * Transcribe a remote audio file using speaker diarization.
     *
     * @param gcsUri the path to an audio file.
     */
    public static void transcribeDiarizationGcs(String gcsUri) throws Exception {
      try (SpeechClient speechClient = SpeechClient.create()) {
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
    
        // Set the remote path for the audio file
        RecognitionAudio audio = RecognitionAudio.newBuilder().setUri(gcsUri).build();
    
        // Use non-blocking call for getting file transcription
        OperationFuture<LongRunningRecognizeResponse, LongRunningRecognizeMetadata> response =
            speechClient.longRunningRecognizeAsync(config, audio);
    
        while (!response.isDone()) {
          System.out.println("Waiting for response...");
          Thread.sleep(10000);
        }
    
        // Speaker Tags are only included in the last result object, which has only one alternative.
        LongRunningRecognizeResponse longRunningRecognizeResponse = response.get();
        SpeechRecognitionAlternative alternative =
            longRunningRecognizeResponse
                .getResults(longRunningRecognizeResponse.getResultsCount() - 1)
                .getAlternatives(0);
    
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
    
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const uri = path to GCS audio file e.g. `gs:/bucket/audio.wav`;
    
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
      uri: gcsUri,
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
    
    
    from google.cloud import speech
    
    
    def transcribe_diarization_gcs_beta(audio_uri: str) -> bool:
        """Transcribe a remote audio file (stored in Google Cloud Storage) using speaker diarization.
        Args:
            audio_uri (str): The Google Cloud Storage path to an audio file.
                E.g., gs://[BUCKET]/[FILE]
        Returns:
            True if the operation successfully completed, False otherwise.
        """
    
        client = speech.SpeechClient()
        # Enhance diarization config with more speaker counts and details
        speaker_diarization_config = speech.[SpeakerDiarizationConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.SpeakerDiarizationConfig.html)(
            enable_speaker_diarization=True,
            min_speaker_count=2,  # Set minimum number of speakers
            max_speaker_count=2,  # Adjust max speakers based on expected number of speakers
        )
    
        # Configure recognition with enhanced audio settings
        recognition_config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="en-US",
            sample_rate_hertz=8000,
            diarization_config=speaker_diarization_config,
        )
    
        # Set the remote path for the audio file
        audio = speech.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionAudio.html)(
            uri=audio_uri,
        )
    
        # Use non-blocking call for getting file transcription
        response = client.[long_running_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_long_running_recognize)(
            config=recognition_config, audio=audio
        ).result(timeout=300)
    
        # The transcript within each result is separate and sequential per result.
        # However, the words list within an alternative includes all the words
        # from all the results thus far. Thus, to get all the words with speaker
        # tags, you only have to take the words list from the last result
        result = response.results[-1]
        words_info = result.alternatives[0].words
    
        # Print the output
        for word_info in words_info:
            print(f"word: '{word_info.word}', speaker_tag: {word_info.speaker_tag}")
        return True
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
