---
url: https://docs.cloud.google.com/text-to-speech/docs/quickstarts/
title: Quickstart: Create audio from text by using client libraries \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:43.430754+00:00
---

# Quickstart: Create audio from text by using client libraries  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/quickstarts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Guides ](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create audio from text by using client libraries

This quickstart walks you through the process of using client libraries to make a request to Cloud TTS, creating audio from text.

To learn more about the fundamental concepts in Cloud Text-to-Speech, read [Cloud Text-to-Speech Basics](https://docs.cloud.google.com/text-to-speech/docs/basics). To see which synthetic voices are available for your language, see the [supported voices and languages page](https://docs.cloud.google.com/text-to-speech/docs/voices).

## Before you begin

Before you can send a request to the Cloud Text-to-Speech API, you must have completed the following actions. See the [before you begin](https://docs.cloud.google.com/text-to-speech/docs/before-you-begin) page for details.

  * Enable Cloud Text-to-Speech on a Google Cloud project.
  * Make sure billing is enabled for Cloud Text-to-Speech.
  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
        
        gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * If you're using a local shell, then create local authentication credentials for your user account: 
        
        gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




## Install the client library

### Go
    
    
    go get cloud.google.com/go/texttospeech/apiv1

### Java

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.90.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-texttospeech</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-texttospeech'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-texttospeech" % "2.100.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### Node.js

Before installing the library, make sure you've [prepared your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    npm install @google-cloud/text-to-speech

### Python

Before installing the library, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-cloud-texttospeech

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/text-to-speech/docs/libraries) on the client libraries page and then visit the [Cloud TTS reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.TextToSpeech.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/text-to-speech/docs/libraries) on the client libraries page and then visit the [Cloud TTS reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-text-to-speech/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/text-to-speech/docs/libraries) on the client libraries page and then visit the [Cloud TTS reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-text_to_speech/latest/Google/Cloud/TextToSpeech/V1.html)

## Create audio data

Now you can use Cloud TTS to create an audio file of synthetic human speech. Use the following code to send a [`synthesize`](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize) request to the Cloud Text-to-Speech API.

### Go
    
    
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

Before running the example, make sure you've [prepared your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
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

### Python

Before running the example, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
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

Congratulations! You've sent your first request to Cloud Text-to-Speech.

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  * Use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.



## What's next

  * Learn more about Cloud Text-to-Speech by reading the [basics](https://docs.cloud.google.com/text-to-speech/docs/basics). 
  * Review the list of [available voices](https://docs.cloud.google.com/text-to-speech/docs/voices) you can use for synthetic speech. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
