---
url: https://docs.cloud.google.com/text-to-speech/docs/samples/tts-synthesize-text-audio-profile/
title: Synthesize text with audio profiles \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:23.557241+00:00
---

# Synthesize text with audio profiles  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/samples/tts-synthesize-text-audio-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Samples ](https://docs.cloud.google.com/text-to-speech/docs/samples)



#  Synthesize text with audio profiles Stay organized with collections  Save and categorize content based on your preferences. 

Synthesize text, specifying an audio profile to optimize the synthetic speech for playback on different types of hardware.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use device profiles for generated audio](https://docs.cloud.google.com/text-to-speech/docs/audio-profiles)



## Code sample

### Go

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"fmt"
    	"io"
    	"os"
    
    	"context"
    
    	texttospeech "cloud.google.com/go/texttospeech/apiv1"
    	"cloud.google.com/go/texttospeech/apiv1/texttospeechpb"
    )
    
    // audioProfile generates audio from text using a custom synthesizer like a telephone call.
    func audioProfile(w io.Writer, text string, outputFile string) error {
    	// text := "hello"
    	// outputFile := "out.mp3"
    
    	ctx := context.Background()
    
    	client, err := texttospeech.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1.html#cloud_google_com_go_texttospeech_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &texttospeechpb.SynthesizeSpeechRequest{
    		Input: &texttospeechpb.SynthesisInput{
    			InputSource: &texttospeechpb.SynthesisInput_Text{Text: text},
    		},
    		Voice: &texttospeechpb.VoiceSelectionParams{LanguageCode: "en-US"},
    		AudioConfig: &texttospeechpb.AudioConfig{
    			AudioEncoding:    texttospeechpb.[AudioEncoding_MP3](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1/texttospeechpb.html#cloud_google_com_go_texttospeech_apiv1_texttospeechpb_AudioEncoding_AUDIO_ENCODING_UNSPECIFIED_AudioEncoding_LINEAR16_AudioEncoding_MP3_AudioEncoding_OGG_OPUS_AudioEncoding_MULAW_AudioEncoding_ALAW_AudioEncoding_PCM_AudioEncoding_M4A),
    			EffectsProfileId: []string{"telephony-class-application"},
    		},
    	}
    
    	resp, err := client.SynthesizeSpeech(ctx, req)
    	if err != nil {
    		return fmt.Errorf("SynthesizeSpeech: %w", err)
    	}
    
    	if err = os.WriteFile(outputFile, resp.AudioContent, 0644); err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Audio content written to file: %v\n", outputFile)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/overview). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Demonstrates using the Text to Speech client with audio profiles to synthesize text or ssml
     *
     * @param text the raw text to be synthesized. (e.g., "Hello there!")
     * @param effectsProfile audio profile to be used for synthesis. (e.g.,
     *     "telephony-class-application")
     * @throws Exception on TextToSpeechClient Errors.
     */
    public static ByteString synthesizeTextWithAudioProfile(String text, String effectsProfile)
        throws Exception {
      // Instantiates a client
      try (TextToSpeechClient textToSpeechClient = TextToSpeechClient.create()) {
        // Set the text input to be synthesized
        SynthesisInput input = SynthesisInput.newBuilder().setText(text).build();
    
        // Build the voice request
        VoiceSelectionParams voice =
            VoiceSelectionParams.newBuilder()
                .setLanguageCode("en-US") // languageCode = "en_us"
                .setSsmlGender(SsmlVoiceGender.FEMALE) // ssmlVoiceGender = SsmlVoiceGender.FEMALE
                .build();
    
        // Select the type of audio file you want returned and the audio profile
        AudioConfig audioConfig =
            AudioConfig.newBuilder()
                .setAudioEncoding(AudioEncoding.MP3) // MP3 audio.
                .addEffectsProfileId(effectsProfile) // audio profile
                .build();
    
        // Perform the text-to-speech request
        SynthesizeSpeechResponse response =
            textToSpeechClient.synthesizeSpeech(input, voice, audioConfig);
    
        // Get the audio contents from the response
        ByteString audioContents = response.getAudioContent();
    
        // Write the response to the output file.
        try (OutputStream out = new FileOutputStream("output.mp3")) {
          out.write(audioContents.toByteArray());
          System.out.println("Audio content written to file \"output.mp3\"");
          return audioContents;
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const text = 'Text you want to vocalize';
    // const outputFile = 'YOUR_OUTPUT_FILE_LOCAtION;
    // const languageCode = 'LANGUAGE_CODE_FOR_OUTPUT';
    // const ssmlGender = 'SSML_GENDER_OF_SPEAKER';
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)');
    const fs = require('fs');
    const util = require('util');
    
    // Creates a client
    const client = new speech.[TextToSpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)();
    
    async function synthesizeWithEffectsProfile() {
      // Add one or more effects profiles to array.
      // Refer to documentation for more details:
      // https://cloud.google.com/text-to-speech/docs/audio-profiles
      const effectsProfileId = ['telephony-class-application'];
    
      const request = {
        input: {text: text},
        voice: {languageCode: languageCode, ssmlGender: ssmlGender},
        audioConfig: {audioEncoding: 'MP3', effectsProfileId: effectsProfileId},
      };
    
      const [response] = await client.synthesizeSpeech(request);
      const writeFile = util.promisify(fs.writeFile);
      await writeFile(outputFile, response.audioContent, 'binary');
      console.log(`Audio content written to file: ${outputFile}`);
    }

### PHP

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\TextToSpeech\V1\AudioConfig;
    use Google\Cloud\TextToSpeech\V1\AudioEncoding;
    use Google\Cloud\TextToSpeech\V1\Client\TextToSpeechClient;
    use Google\Cloud\TextToSpeech\V1\SsmlVoiceGender;
    use Google\Cloud\TextToSpeech\V1\SynthesisInput;
    use Google\Cloud\TextToSpeech\V1\SynthesizeSpeechRequest;
    use Google\Cloud\TextToSpeech\V1\VoiceSelectionParams;
    
    /**
     * @param string $text Text to synthesize
     * @param string $effectsProfileId Audio Profile ID
     */
    function synthesize_text_effects_profile(string $text, string $effectsProfileId): void
    {
        // create client object
        $client = new TextToSpeechClient();
    
        $inputText = (new SynthesisInput())
            ->setText($text);
    
        // note: the voice can also be specified by name
        // names of voices can be retrieved with $client->listVoices()
        $voice = (new VoiceSelectionParams())
            ->setLanguageCode('en-US')
            ->setSsmlGender(SsmlVoiceGender::FEMALE);
    
        // define effects profile id.
        $audioConfig = (new AudioConfig())
            ->setAudioEncoding(AudioEncoding::MP3)
            ->setEffectsProfileId(array($effectsProfileId));
        $request = (new SynthesizeSpeechRequest())
            ->setInput($inputText)
            ->setVoice($voice)
            ->setAudioConfig($audioConfig);
    
        $response = $client->synthesizeSpeech($request);
        $audioContent = $response->getAudioContent();
    
        file_put_contents('output.mp3', $audioContent);
        print('Audio content written to "output.mp3"' . PHP_EOL);
    
        $client->close();
    }

### Python

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def synthesize_text_with_audio_profile():
        """Synthesizes speech from the input string of text."""
        from google.cloud import texttospeech
    
        text = "hello"
        output = "output.mp3"
        effects_profile_id = "telephony-class-application"
        client = texttospeech.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html)()
    
        input_text = texttospeech.[SynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesisInput.html)(text=text)
    
        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.[VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceSelectionParams.html)(language_code="en-US")
    
        # Note: you can pass in multiple effects_profile_id. They will be applied
        # in the same order they are provided.
        audio_config = texttospeech.[AudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioConfig.html)(
            audio_encoding=texttospeech.[AudioEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioEncoding.html).MP3,
            effects_profile_id=[effects_profile_id],
        )
    
        response = client.[synthesize_speech](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_synthesize_speech)(
            input=input_text, voice=voice, audio_config=audio_config
        )
    
        # The response's audio_content is binary.
        with open(output, "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "%s"' % output)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=texttospeech). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
