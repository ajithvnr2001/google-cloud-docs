---
url: https://docs.cloud.google.com/text-to-speech/docs/samples/tts-list-voices/
title: List available voices \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:23.718460+00:00
---

# List available voices  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/samples/tts-list-voices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Samples ](https://docs.cloud.google.com/text-to-speech/docs/samples)



#  List available voices Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to list the available voices.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Supported voices and languages](https://docs.cloud.google.com/text-to-speech/docs/list-voices-and-types)



## Code sample

### Go

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/texttospeech/latest/apiv1). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // ListVoices lists the available text to speech voices.
    func ListVoices(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := texttospeech.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	// Performs the list voices request.
    	resp, err := client.ListVoices(ctx, &texttospeechpb.ListVoicesRequest{})
    	if err != nil {
    		return err
    	}
    
    	for _, voice := range resp.Voices {
    		// Display the voice's name. Example: tpc-vocoded
    		fmt.Fprintf(w, "Name: %v\n", voice.Name)
    
    		// Display the supported language codes for this voice. Example: "en-US"
    		for _, languageCode := range voice.LanguageCodes {
    			fmt.Fprintf(w, "  Supported language: %v\n", languageCode)
    		}
    
    		// Display the SSML Voice Gender.
    		fmt.Fprintf(w, "  SSML Voice Gender: %v\n", voice.SsmlGender.String())
    
    		// Display the natural sample rate hertz for this voice. Example: 24000
    		fmt.Fprintf(w, "  Natural Sample Rate Hertz: %v\n",
    			voice.NaturalSampleRateHertz)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/overview). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Demonstrates using the Text to Speech client to list the client's supported voices.
     *
     * @throws Exception on TextToSpeechClient Errors.
     */
    public static List<Voice> listAllSupportedVoices() throws Exception {
      // Instantiates a client
      try (TextToSpeechClient textToSpeechClient = TextToSpeechClient.create()) {
        // Builds the text to speech list voices request
        ListVoicesRequest request = ListVoicesRequest.getDefaultInstance();
    
        // Performs the list voices request
        ListVoicesResponse response = textToSpeechClient.listVoices(request);
        List<Voice> voices = response.getVoicesList();
    
        for (Voice voice : voices) {
          // Display the voice's name. Example: tpc-vocoded
          System.out.format("Name: %s\n", voice.getName());
    
          // Display the supported language codes for this voice. Example: "en-us"
          List<ByteString> languageCodes = voice.getLanguageCodesList().asByteStringList();
          for (ByteString languageCode : languageCodes) {
            System.out.format("Supported Language: %s\n", languageCode.toStringUtf8());
          }
    
          // Display the SSML Voice Gender
          System.out.format("SSML Voice Gender: %s\n", voice.getSsmlGender());
    
          // Display the natural sample rate hertz for this voice. Example: 24000
          System.out.format("Natural Sample Rate Hertz: %s\n\n", voice.getNaturalSampleRateHertz());
        }
        return voices;
      }
    }

### Node.js

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const textToSpeech = require('[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)');
    
    const client = new textToSpeech.[TextToSpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)();
    
    const [result] = await client.listVoices({});
    const voices = [result](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.operation.html).voices;
    
    console.log('Voices:');
    voices.forEach(voice => {
      console.log(`Name: ${voice.name}`);
      console.log(`  SSML Voice Gender: ${voice.ssmlGender}`);
      console.log(`  Natural Sample Rate Hertz: ${voice.naturalSampleRateHertz}`);
      console.log('  Supported languages:');
      voice.languageCodes.forEach(languageCode => {
        console.log(`    ${languageCode}`);
      });
    });

### PHP

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\TextToSpeech\V1\Client\TextToSpeechClient;
    use Google\Cloud\TextToSpeech\V1\ListVoicesRequest;
    
    function list_voices(): void
    {
        // create client object
        $client = new TextToSpeechClient();
    
        // perform list voices request
        $request = (new ListVoicesRequest());
        $response = $client->listVoices($request);
        $voices = $response->getVoices();
    
        foreach ($voices as $voice) {
            // display the voice's name. example: tpc-vocoded
            printf('Name: %s' . PHP_EOL, $voice->getName());
    
            // display the supported language codes for this voice. example: 'en-US'
            foreach ($voice->getLanguageCodes() as $languageCode) {
                printf('Supported language: %s' . PHP_EOL, $languageCode);
            }
    
            // SSML voice gender values from TextToSpeech\V1\SsmlVoiceGender
            $ssmlVoiceGender = ['SSML_VOICE_GENDER_UNSPECIFIED', 'MALE', 'FEMALE',
            'NEUTRAL'];
    
            // display the SSML voice gender
            $gender = $voice->getSsmlGender();
            printf('SSML voice gender: %s' . PHP_EOL, $ssmlVoiceGender[$gender]);
    
            // display the natural hertz rate for this voice
            printf('Natural Sample Rate Hertz: %d' . PHP_EOL,
                $voice->getNaturalSampleRateHertz());
        }
    
        $client->close();
    }

### Python

To learn how to install and use the client library for Cloud TTS, see [Cloud TTS client libraries](https://docs.cloud.google.com/text-to-speech/docs/libraries). For more information, see the [Cloud TTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest). 

To authenticate to Cloud TTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_voices():
        """Lists the available voices."""
        from google.cloud import texttospeech
    
        client = texttospeech.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html)()
    
        # Performs the list voices request
        voices = client.[list_voices](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_list_voices)()
    
        for voice in voices.voices:
            # Display the voice's name. Example: tpc-vocoded
            print(f"Name: {voice.name}")
    
            # Display the supported language codes for this voice. Example: "en-US"
            for language_code in voice.language_codes:
                print(f"Supported language: {language_code}")
    
            ssml_gender = texttospeech.[SsmlVoiceGender](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SsmlVoiceGender.html)(voice.ssml_gender)
    
            # Display the SSML Voice Gender
            print(f"SSML Voice Gender: {ssml_gender.name}")
    
            # Display the natural sample rate hertz for this voice. Example: 24000
            print(f"Natural Sample Rate Hertz: {voice.natural_sample_rate_hertz}\n")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=texttospeech). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
