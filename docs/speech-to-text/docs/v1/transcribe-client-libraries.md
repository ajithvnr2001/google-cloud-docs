---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-client-libraries/
title: Quickstart: Transcribe speech to text by using client libraries \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:32.619965+00:00
---

# Quickstart: Transcribe speech to text by using client libraries  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Transcribe speech to text by using client libraries

This page shows you how to send a speech recognition request to Cloud Speech-to-Text in your favorite programming language using the Google Cloud Client Libraries.

Cloud Speech-to-Text enables easy integration of Google speech recognition technologies into developer applications. You can send audio data to the Cloud Speech-to-Text API, which then returns a text transcription of that audio file. For more information about the service, see [Cloud STT basics](https://docs.cloud.google.com/speech-to-text/docs/basics). 

## Before you begin

Before you can send a request to the Cloud Speech-to-Text API, you must have completed the following actions. See the [before you begin](https://docs.cloud.google.com/speech-to-text/docs/before-you-begin) page for details.

  * Enable Cloud Speech-to-Text on a Google Cloud project.
  * Make sure billing is enabled for Cloud Speech-to-Text.
  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
        
        gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * If you're using a local shell, then create local authentication credentials for your user account: 
        
        gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * Verify that you have the permissions required to complete this guide. If you created a new project for this guide, then you already have the required permissions.
  * (Optional) Create a new Cloud Storage bucket to store your audio data.



### Required roles

To get the permissions that you need to transcribe speech to text, ask your administrator to grant you the [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Install the client library

### Go
    
    
    go get cloud.google.com/go/speech/apiv1

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
        <artifactId>google-cloud-speech</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-speech'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-speech" % "4.94.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### Node.js

Before installing the library, make sure you've [prepared your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    npm install @google-cloud/speech

### Python

Before installing the library, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-cloud-speech

## Make an audio transcription request

Now you can use Cloud STT to transcribe an audio file to text. Use the following code to send a [`recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize) request to the Cloud Speech-to-Text API.

### Go
    
    
    // Sample speech-quickstart uses the Google Cloud Speech API to transcribe
    // audio.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	speech "cloud.google.com/go/speech/apiv1"
    	"cloud.google.com/go/speech/apiv1/speechpb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := speech.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1.html#cloud_google_com_go_speech_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// The path to the remote audio file to transcribe.
    	fileURI := "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    
    	// Detects speech in the audio file.
    	resp, err := client.Recognize(ctx, &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:        speechpb.[RecognitionConfig_LINEAR16](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1/speechpb.html#cloud_google_com_go_speech_apiv1_speechpb_RecognitionConfig_ENCODING_UNSPECIFIED_RecognitionConfig_LINEAR16_RecognitionConfig_FLAC_RecognitionConfig_MULAW_RecognitionConfig_AMR_RecognitionConfig_AMR_WB_RecognitionConfig_OGG_OPUS_RecognitionConfig_SPEEX_WITH_HEADER_BYTE_RecognitionConfig_MP3_RecognitionConfig_WEBM_OPUS),
    			SampleRateHertz: 16000,
    			LanguageCode:    "en-US",
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Uri{Uri: fileURI},
    		},
    	})
    	if err != nil {
    		log.Fatalf("failed to recognize: %v", err)
    	}
    
    	// Prints the results.
    	for _, result := range resp.Results {
    		for _, alt := range result.Alternatives {
    			fmt.Printf("\"%v\" (confidence=%3f)\n", alt.Transcript, alt.Confidence)
    		}
    	}
    }
    

### Java
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.speech.v1.[RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html);
    import com.google.cloud.speech.v1.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html);
    import com.google.cloud.speech.v1.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html).[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.AudioEncoding.html);
    import com.google.cloud.speech.v1.[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html);
    import com.google.cloud.speech.v1.[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html);
    import com.google.cloud.speech.v1.[SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html);
    import com.google.cloud.speech.v1.[SpeechRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionResult.html);
    import java.util.List;
    
    public class QuickstartSample {
    
      /** Demonstrates using the Speech API to transcribe an audio file. */
      public static void main(String... args) throws Exception {
        // Instantiates a client
        try ([SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html) speechClient = [SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html).create()) {
    
          // The path to the audio file to transcribe
          String gcsUri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw";
    
          // Builds the sync recognize request
          [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html) config =
              [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html).newBuilder()
                  .[setEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setEncoding_com_google_cloud_speech_v1_RecognitionConfig_AudioEncoding_)([AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.AudioEncoding.html).LINEAR16)
                  .[setSampleRateHertz](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setSampleRateHertz_int_)(16000)
                  .setLanguageCode("en-US")
                  .build();
          [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html) audio = [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html).newBuilder().setUri(gcsUri).build();
    
          // Performs speech recognition on the audio file
          [RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html) response = speechClient.recognize(config, audio);
          List<SpeechRecognitionResult> results = response.[getResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html#com_google_cloud_speech_v1_RecognizeResponse_getResultsList__)();
    
          for ([SpeechRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionResult.html) result : results) {
            // There can be several alternative transcripts for a given chunk of speech. Just use the
            // first (most likely) one here.
            [SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html) alternative = result.getAlternativesList().get(0);
            System.out.printf("Transcription: %s%n", alternative.[getTranscript](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html#com_google_cloud_speech_v1_SpeechRecognitionAlternative_getTranscript__)());
          }
        }
      }
    }

### Node.js

Before running the example, make sure you've [prepared your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    async function quickstart() {
      // The path to the remote LINEAR16 file
      const gcsUri = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw';
    
      // The audio file's encoding, sample rate in hertz, and BCP-47 language code
      const audio = {
        uri: gcsUri,
      };
      const config = {
        encoding: 'LINEAR16',
        sampleRateHertz: 16000,
        languageCode: 'en-US',
      };
      const request = {
        audio: audio,
        config: config,
      };
    
      // Detects speech in the audio file
      const [response] = await client.recognize(request);
      const transcription = response.results
        .map(result => result.alternatives[0].transcript)
        .join('\n');
      console.log(`Transcription: ${transcription}`);
    }
    quickstart();

### Python

Before running the example, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    # Imports the Google Cloud client library
    
    
    from google.cloud import speech
    
    
    
    def run_quickstart() -> speech.RecognizeResponse:
        # Instantiates a client
        client = speech.SpeechClient()
    
        # The name of the audio file to transcribe
        gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    
        audio = speech.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionAudio.html)(uri=gcs_uri)
    
        config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
    
        # Detects speech in the audio file
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(config=config, audio=audio)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")

Congratulations! You've sent your first request to Cloud STT.

If you receive an error or an empty response from Cloud STT, take a look at the [troubleshooting](https://docs.cloud.google.com/speech-to-text/docs/troubleshooting) and [error mitigation](https://docs.cloud.google.com/speech-to-text/docs/error-messages) steps. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  * Use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you do not need it.



## What's next

  * Practice [transcribing short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
  * Learn how to [batch long audio files for speech recognition](https://docs.cloud.google.com/speech-to-text/docs/async-recognize). 
  * Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize) like from a microphone. 
  * Get started with the Cloud STT in your language of choice by using a [Cloud STT client library](https://docs.cloud.google.com/speech-to-text/docs/reference/libraries). 
  * Work through the [sample applications](https://docs.cloud.google.com/speech-to-text/docs/samples). 
  * For best performance, accuracy, and other tips, see the [best practices](https://docs.cloud.google.com/speech-to-text/docs/best-practices) documentation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
