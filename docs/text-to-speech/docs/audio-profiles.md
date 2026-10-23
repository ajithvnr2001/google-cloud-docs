---
url: https://docs.cloud.google.com/text-to-speech/docs/audio-profiles/
title: Use device profiles for generated audio \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:55.052822+00:00
---

# Use device profiles for generated audio  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/audio-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Guides ](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries)



Send feedback 

#  Use device profiles for generated audio Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to select a device profile for audio created by Cloud Text-to-Speech.

You can optimize the [synthetic speech](https://docs.cloud.google.com/text-to-speech/docs/basics#speech_synthesis) produced by Cloud Text-to-Speech for playback on different types of hardware. For example, if your app runs primarily on smaller, 'wearable' types of devices, you can create synthetic speech from Cloud Text-to-Speech API that is optimized specifically for smaller speakers.

You can also apply multiple device profiles to the same synthetic speech. The Cloud Text-to-Speech API applies device profiles to the audio in the order provided in the request to the [`text:synthesize`](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize) endpoint. Avoid specifying the same profile more than once, as you can have undesirable results by applying the same profile multiple times.

Use of audio profiles is optional. If you choose to use one (or more), Cloud Text-to-Speech applies the profile(s) to your post-synthesized speech results. If you choose not to use an audio profile, you will receive your speech results without any post-synthesis modifications.

To hear the difference between audio generated from different profiles, compare the two clips below.

Your browser does not support the audio element.   
_Example 1. Audio generated with`handset-class-device` profile_

Your browser does not support the audio element.   
_Example 2. Audio generated with`telephony-class-application` profile_

Note: Each audio profile has been optimized for a specific device by adjusting a range of audio effects. However, the make and model of the device used to tune the profile may not match users' playback devices exactly. You may need to experiment with different profiles to find the best sound output for your application.

## Available audio profiles

The following table gives the IDs and examples of the device profiles available for use by the Cloud Text-to-Speech API.

Audio profile ID | Optimized for  
---|---  
`wearable-class-device` | Smart watches and other wearables, like Apple Watch, Wear OS watch  
`handset-class-device` | Smartphones, like Google Pixel, Samsung Galaxy, Apple iPhone  
`headphone-class-device` | Earbuds or headphones for audio playback, like Sennheiser headphones  
`small-bluetooth-speaker-class-device` | Small home speakers, like Google Home Mini  
`medium-bluetooth-speaker-class-device` | Smart home speakers, like Google Home  
`large-home-entertainment-class-device` | Home entertainment systems or smart TVs, like Google Home Max, LG TV  
`large-automotive-class-device` | Car speakers  
`telephony-class-application` | Interactive Voice Response (IVR) systems  
  
## Specify an audio profile to use

To specify an audio profile to use, set the [`effectsProfileId`](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize#audioconfig) field for the speech synthesis request.

### Protocol

To generate an audio file, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the Google Cloud CLI to retrieve an access token for the request. For instructions on installing the gcloud CLI, see [Authenticate to Cloud TTS](https://docs.cloud.google.com/text-to-speech/docs/authentication). 

The following example shows how to send a request to the [`text:synthesize`](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize) endpoint.
    
    
    curl \
      -H "Authorization: Bearer "$(gcloud auth print-access-token) \
      -H "Content-Type: application/json; charset=utf-8" \
      --data "{
        'input':{
          'text':'This is a sentence that helps test how audio profiles can change the way Cloud Text-to-Speech sounds.'
        },
        'voice':{
          'languageCode':'en-us',
        },
        'audioConfig':{
          'audioEncoding':'LINEAR16',
    **'effectsProfileId': ['telephony-class-application']**
        }
      }" "https://texttospeech.googleapis.com/v1beta1/text:synthesize" > audio-profile.txt

If the request is successful, the Cloud Text-to-Speech API returns the synthesized audio as base64-encoded data contained in the JSON output. The JSON output in the `audio-profiles.txt` file looks like the following:
    
    
    {
      "audioContent": "//NExAASCCIIAAhEAGAAEMW4kAYPnwwIKw/BBTpwTvB+IAxIfghUfW.."
    }

To decode the results from the Cloud Text-to-Speech API as an MP3 audio file, run the following command from the same directory as the `audio-profiles.txt` file.
    
    
    sed 's|audioContent| |' < audio-profile.txt > tmp-output.txt && \
    tr -d '\n ":{}' < tmp-output.txt > tmp-output-2.txt && \
    base64 tmp-output-2.txt --decode > audio-profile.wav && \
    rm tmp-output*.txt
    

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
    public static void synthesizeTextWithAudioProfile(String text, String effectsProfile)
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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/text-to-speech/docs/libraries) on the client libraries page and then visit the [Cloud TTS reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.TextToSpeech.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/text-to-speech/docs/libraries) on the client libraries page and then visit the [Cloud TTS reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-text-to-speech/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/text-to-speech/docs/libraries) on the client libraries page and then visit the [Cloud TTS reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-text_to_speech/latest/Google/Cloud/TextToSpeech/V1.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
