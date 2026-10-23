---
url: https://docs.cloud.google.com/text-to-speech/docs/samples/tts-synthesize-text/
title: Pass text to the Text-to-Speech API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:44.887191+00:00
---

# Pass text to the Text-to-Speech API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/samples/tts-synthesize-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Samples ](https://docs.cloud.google.com/text-to-speech/docs/samples)



#  Pass text to the Text-to-Speech API Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to pass text to the Text-to-Speech API to synthesize audio.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Chirp 3: HD voices](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd)
  * [Create voice audio files](https://docs.cloud.google.com/text-to-speech/docs/create-audio)



## Code sample

### Go

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // SynthesizeText synthesizes plain text and saves the output to outputFile.
    func SynthesizeText(w io.Writer, text, outputFile string) error {
    	ctx := context.Background()
    
    	client, err := texttospeech.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	req := texttospeechpb.SynthesizeSpeechRequest{
    		Input: &texttospeechpb.SynthesisInput{
    			InputSource: &texttospeechpb.SynthesisInput_Text{Text: text},
    		},
    		// Note: the voice can also be specified by name.
    		// Names of voices can be retrieved with client.ListVoices().
    		Voice: &texttospeechpb.VoiceSelectionParams{
    			LanguageCode: "en-US",
    			SsmlGender:   texttospeechpb.SsmlVoiceGender_FEMALE,
    		},
    		AudioConfig: &texttospeechpb.AudioConfig{
    			AudioEncoding: texttospeechpb.AudioEncoding_MP3,
    		},
    	}
    
    	resp, err := client.SynthesizeSpeech(ctx, &req)
    	if err != nil {
    		return err
    	}
    
    	err = os.WriteFile(outputFile, resp.AudioContent, 0644)
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Audio content written to file: %v\n", outputFile)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/overview). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Demonstrates using the Text to Speech client to synthesize text or ssml.
     *
     * @param text the raw text to be synthesized. (e.g., "Hello there!")
     * @throws Exception on TextToSpeechClient Errors.
     */
    public static ByteString synthesizeText(String text) throws Exception {
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
    
        // Select the type of audio file you want returned
        AudioConfig audioConfig =
            AudioConfig.newBuilder()
                .setAudioEncoding(AudioEncoding.MP3) // MP3 audio.
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
    
    
    const textToSpeech = require('[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)');
    const fs = require('fs');
    const util = require('util');
    
    const client = new textToSpeech.[TextToSpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const text = 'Text to synthesize, eg. hello';
    // const outputFile = 'Local path to save audio file to, e.g. output.mp3';
    
    const request = {
      input: {text: text},
      voice: {languageCode: 'en-US', ssmlGender: 'FEMALE'},
      audioConfig: {audioEncoding: 'MP3'},
    };
    const [response] = await client.synthesizeSpeech(request);
    const writeFile = util.promisify(fs.writeFile);
    await writeFile(outputFile, response.audioContent, 'binary');
    console.log(`Audio content written to file: ${outputFile}`);

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
     */
    function synthesize_text(string $text): void
    {
        // create client object
        $client = new TextToSpeechClient();
    
        $input_text = (new SynthesisInput())
            ->setText($text);
    
        // note: the voice can also be specified by name
        // names of voices can be retrieved with $client->listVoices()
        $voice = (new VoiceSelectionParams())
            ->setLanguageCode('en-US')
            ->setSsmlGender(SsmlVoiceGender::FEMALE);
    
        $audioConfig = (new AudioConfig())
            ->setAudioEncoding(AudioEncoding::MP3);
        $request = (new SynthesizeSpeechRequest())
            ->setInput($input_text)
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
    
    
    def synthesize_text():
        """Synthesizes speech from the input string of text."""
        from google.cloud import texttospeech
    
        text = "Hello there."
        client = texttospeech.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html)()
    
        input_text = texttospeech.[SynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesisInput.html)(text=text)
    
        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.[VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceSelectionParams.html)(
            language_code="en-US",
            name="en-US-Chirp3-HD-Charon",
        )
    
        audio_config = texttospeech.[AudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioConfig.html)(
            audio_encoding=texttospeech.[AudioEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioEncoding.html).MP3
        )
    
        response = client.[synthesize_speech](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_synthesize_speech)(
            input=input_text,
            voice=voice,
            audio_config=audio_config,
        )
    
        # The response's audio_content is binary.
        with open("output.mp3", "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=texttospeech). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
