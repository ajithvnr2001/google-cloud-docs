---
url: https://docs.cloud.google.com/text-to-speech/docs/libraries/
title: Cloud TTS client libraries \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:20.849037+00:00
---

# Cloud TTS client libraries  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Reference ](https://docs.cloud.google.com/text-to-speech/docs/apis)



Send feedback 

#  Cloud TTS client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Cloud Text-to-Speech API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### C#

If you are using Visual Studio 2017 or higher, open nuget package manager window and type the following: 
    
    
    Install-Package Google.Apis

If you are using .NET Core command-line interface tools to install your dependencies, run the following command:
    
    
    dotnet add package Google.Apis

For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    go get cloud.google.com/go/texttospeech/apiv1

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

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

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install @google-cloud/text-to-speech

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/apiclient

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python
    
    
    pip install --upgrade google-cloud-texttospeech

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

### Ruby
    
    
    gem install google-api-client

For more information, see [Setting Up a Ruby Development Environment](https://docs.cloud.google.com/ruby/docs/setup).

## Set up authentication

To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

For production environments, the way you set up ADC depends on the service and context. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

For a local development environment, you can set up ADC with the credentials that are associated with your Google Account:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




## Use the client library

The following example shows how to use the client library. 

### C++
    
    
    #include "google/cloud/texttospeech/v1/text_to_speech_client.h"
    #include <iostream>
    
    auto constexpr kText = R"""(
    Four score and seven years ago our fathers brought forth on this
    continent, a new nation, conceived in Liberty, and dedicated to
    the proposition that all men are created equal.)""";
    
    int main(int argc, char* argv[]) try {
      if (argc != 1) {
        std::cerr << "Usage: " << argv[0] << "\n";
        return 1;
      }
    
      namespace texttospeech = ::google::cloud::texttospeech_v1;
      auto client = texttospeech::TextToSpeechClient(
          texttospeech::MakeTextToSpeechConnection());
    
      google::cloud::texttospeech::v1::SynthesisInput input;
      input.set_text(kText);
      google::cloud::texttospeech::v1::VoiceSelectionParams voice;
      voice.set_language_code("en-US");
      google::cloud::texttospeech::v1::AudioConfig audio;
      audio.set_audio_encoding(google::cloud::texttospeech::v1::LINEAR16);
    
      auto response = client.SynthesizeSpeech(input, voice, audio);
      if (!response) throw std::move(response).status();
      // Normally one would play the results (response->audio_content()) over some
      // audio device. For this quickstart, we just print some information.
      auto constexpr kWavHeaderSize = 48;
      auto constexpr kBytesPerSample = 2;  // we asked for LINEAR16
      auto const sample_count =
          (response->audio_content().size() - kWavHeaderSize) / kBytesPerSample;
      std::cout << "The audio has " << sample_count << " samples\n";
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

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

## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference/texttospeech/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-cloud-speech` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-speech%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://developers.google.com/api-client-library/dotnet)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-dotnet-client/issues)
  * [`google-cloud-speech` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-speech%5D+%5Bc%23%5D)
  * [Source code](https://github.com/google/google-api-dotnet-client)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://godoc.org/cloud.google.com/go/texttospeech/apiv1)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-cloud-speech` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-speech%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [`google-cloud-speech` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-speech%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://github.com/googleapis/nodejs-text-to-speech)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/nodejs-text-to-speech/issues)
  * [`google-cloud-speech` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-speech%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/nodejs-text-to-speech)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://developers.google.com/api-client-library/php/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-php-client/issues)
  * [`google-cloud-speech` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-speech%5D+%5Bphp%5D)
  * [Source code](https://github.com/google/google-api-php-client)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://cloud.google.com/python/docs/reference/texttospeech/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-python/issues)
  * [`google-cloud-speech` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-speech%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/google-cloud-python)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://developers.google.com/api-client-library/ruby/apis/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-ruby-client/issues)
  * [`google-cloud-speech` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-speech%5D+%5Bruby%5D)
  * [Source code](https://github.com/google/google-api-ruby-client)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
