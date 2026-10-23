---
url: https://docs.cloud.google.com/text-to-speech/docs/samples/tts-quickstart/
title: Synthesize from a string of text \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:45.368801+00:00
---

# Synthesize from a string of text  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/samples/tts-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Samples ](https://docs.cloud.google.com/text-to-speech/docs/samples)



#  Synthesize from a string of text Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates synthesizing from a string of text.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries)
  * [Quickstart: Create audio from text by using client libraries](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries)



## Code sample

### Go

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Command quickstart generates an audio file with the content "Hello, World!".
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    
    	texttospeech "cloud.google.com/go/texttospeech/apiv1"
    	"cloud.google.com/go/texttospeech/apiv1/texttospeechpb"
    )
    
    func main() {
    	// Instantiates a client.
    	ctx := context.Background()
    
    	client, err := texttospeech.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1.html#cloud_google_com_go_texttospeech_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatal(err)
    	}
    	defer client.Close()
    
    	// Perform the text-to-speech request on the text input with the selected
    	// voice parameters and audio file type.
    	req := texttospeechpb.SynthesizeSpeechRequest{
    		// Set the text input to be synthesized.
    		Input: &texttospeechpb.SynthesisInput{
    			InputSource: &texttospeechpb.SynthesisInput_Text{Text: "Hello, World!"},
    		},
    		// Build the voice request, select the language code ("en-US") and the SSML
    		// voice gender ("neutral").
    		Voice: &texttospeechpb.VoiceSelectionParams{
    			LanguageCode: "en-US",
    			SsmlGender:   texttospeechpb.[SsmlVoiceGender_NEUTRAL](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1/texttospeechpb.html#cloud_google_com_go_texttospeech_apiv1_texttospeechpb_SsmlVoiceGender_SSML_VOICE_GENDER_UNSPECIFIED_SsmlVoiceGender_MALE_SsmlVoiceGender_FEMALE_SsmlVoiceGender_NEUTRAL),
    		},
    		// Select the type of audio file you want returned.
    		AudioConfig: &texttospeechpb.AudioConfig{
    			AudioEncoding: texttospeechpb.[AudioEncoding_MP3](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1/texttospeechpb.html#cloud_google_com_go_texttospeech_apiv1_texttospeechpb_AudioEncoding_AUDIO_ENCODING_UNSPECIFIED_AudioEncoding_LINEAR16_AudioEncoding_MP3_AudioEncoding_OGG_OPUS_AudioEncoding_MULAW_AudioEncoding_ALAW_AudioEncoding_PCM_AudioEncoding_M4A),
    		},
    	}
    
    	resp, err := client.SynthesizeSpeech(ctx, &req)
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	// The resp's AudioContent is binary.
    	filename := "output.mp3"
    	err = os.WriteFile(filename, resp.AudioContent, 0644)
    	if err != nil {
    		log.Fatal(err)
    	}
    	fmt.Printf("Audio content written to file: %v\n", filename)
    }
    

### Java

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/overview). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.texttospeech.v1.[AudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.AudioConfig.html);
    import com.google.cloud.texttospeech.v1.[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.AudioEncoding.html);
    import com.google.cloud.texttospeech.v1.[SsmlVoiceGender](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SsmlVoiceGender.html);
    import com.google.cloud.texttospeech.v1.[SynthesisInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.html);
    import com.google.cloud.texttospeech.v1.[SynthesizeSpeechResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesizeSpeechResponse.html);
    import com.google.cloud.texttospeech.v1.[TextToSpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.TextToSpeechClient.html);
    import com.google.cloud.texttospeech.v1.[VoiceSelectionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.VoiceSelectionParams.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileOutputStream;
    import java.io.OutputStream;
    
    /**
     * Google Cloud TextToSpeech API sample application. Example usage: mvn package exec:java
     * -Dexec.mainClass='com.example.texttospeech.QuickstartSample'
     */
    public class QuickstartSample {
    
      /** Demonstrates using the Text-to-Speech API. */
      public static void main(String... args) throws Exception {
        // Instantiates a client
        try ([TextToSpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.TextToSpeechClient.html) textToSpeechClient = [TextToSpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.TextToSpeechClient.html).create()) {
          // Set the text input to be synthesized
          [SynthesisInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.html) input = [SynthesisInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.html).newBuilder().setText("Hello, World!").build();
    
          // Build the voice request, select the language code ("en-US") and the ssml voice gender
          // ("neutral")
          [VoiceSelectionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.VoiceSelectionParams.html) voice =
              [VoiceSelectionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.VoiceSelectionParams.html).newBuilder()
                  .setLanguageCode("en-US")
                  .setSsmlGender([SsmlVoiceGender](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SsmlVoiceGender.html).NEUTRAL)
                  .build();
    
          // Select the type of audio file you want returned
          [AudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.AudioConfig.html) audioConfig =
              [AudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.AudioConfig.html).newBuilder().setAudioEncoding([AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.AudioEncoding.html).MP3).build();
    
          // Perform the text-to-speech request on the text input with the selected voice parameters and
          // audio file type
          [SynthesizeSpeechResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesizeSpeechResponse.html) response =
              textToSpeechClient.synthesizeSpeech(input, voice, audioConfig);
    
          // Get the audio contents from the response
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) audioContents = response.[getAudioContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesizeSpeechResponse.html#com_google_cloud_texttospeech_v1_SynthesizeSpeechResponse_getAudioContent__)();
    
          // Write the response to the output file.
          try (OutputStream out = new FileOutputStream("output.mp3")) {
            out.write(audioContents.[toByteArray](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_toByteArray__)());
            System.out.println("Audio content written to file \"output.mp3\"");
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const textToSpeech = require('[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)');
    
    // Import other required libraries
    const {writeFile} = require('node:fs/promises');
    
    // Creates a client
    const client = new textToSpeech.[TextToSpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)();
    
    async function quickStart() {
      // The text to synthesize
      const text = 'hello, world!';
    
      // Construct the request
      const request = {
        input: {text: text},
        // Select the language and SSML voice gender (optional)
        voice: {languageCode: 'en-US', ssmlGender: 'NEUTRAL'},
        // select the type of audio encoding
        audioConfig: {audioEncoding: 'MP3'},
      };
    
      // Performs the text-to-speech request
      const [response] = await client.synthesizeSpeech(request);
    
      // Save the generated binary audio content to a local file
      await writeFile('output.mp3', response.audioContent, 'binary');
      console.log('Audio content written to file: output.mp3');
    }
    
    await quickStart();

### PHP

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    // Imports the Cloud Client Library
    use Google\Cloud\TextToSpeech\V1\AudioConfig;
    use Google\Cloud\TextToSpeech\V1\AudioEncoding;
    use Google\Cloud\TextToSpeech\V1\Client\TextToSpeechClient;
    use Google\Cloud\TextToSpeech\V1\SsmlVoiceGender;
    use Google\Cloud\TextToSpeech\V1\SynthesisInput;
    use Google\Cloud\TextToSpeech\V1\SynthesizeSpeechRequest;
    use Google\Cloud\TextToSpeech\V1\VoiceSelectionParams;
    
    // instantiates a client
    $client = new TextToSpeechClient();
    
    // sets text to be synthesised
    $synthesisInputText = (new SynthesisInput())
        ->setText('Hello, world!');
    
    // build the voice request, select the language code ("en-US") and the ssml
    // voice gender
    $voice = (new VoiceSelectionParams())
        ->setLanguageCode('en-US')
        ->setSsmlGender(SsmlVoiceGender::FEMALE);
    
    // Effects profile
    $effectsProfileId = 'telephony-class-application';
    
    // select the type of audio file you want returned
    $audioConfig = (new AudioConfig())
        ->setAudioEncoding(AudioEncoding::MP3)
        ->setEffectsProfileId(array($effectsProfileId));
    
    // perform text-to-speech request on the text input with selected voice
    // parameters and audio file type
    $request = (new SynthesizeSpeechRequest())
        ->setInput($synthesisInputText)
        ->setVoice($voice)
        ->setAudioConfig($audioConfig);
    $response = $client->synthesizeSpeech($request);
    $audioContent = $response->getAudioContent();
    
    // the response's audioContent is binary
    file_put_contents('output.mp3', $audioContent);
    echo 'Audio content written to "output.mp3"' . PHP_EOL;
    

### Python

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """Synthesizes speech from the input string of text or ssml.
    Make sure to be working in a virtual environment.
    
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech
    
    # Instantiates a client
    client = texttospeech.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html)()
    
    # Set the text input to be synthesized
    synthesis_input = texttospeech.[SynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesisInput.html)(text="Hello, World!")
    
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.[VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceSelectionParams.html)(
        language_code="en-US", ssml_gender=texttospeech.[SsmlVoiceGender](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SsmlVoiceGender.html).NEUTRAL
    )
    
    # Select the type of audio file you want returned
    audio_config = texttospeech.[AudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioConfig.html)(
        audio_encoding=texttospeech.[AudioEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioEncoding.html).MP3
    )
    
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.[synthesize_speech](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_synthesize_speech)(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    
    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=texttospeech). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
