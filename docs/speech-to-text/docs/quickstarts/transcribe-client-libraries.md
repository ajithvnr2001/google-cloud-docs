---
url: https://docs.cloud.google.com/speech-to-text/docs/quickstarts/transcribe-client-libraries/
title: Transcribe speech to text by using client libraries \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:23.348437+00:00
---

# Transcribe speech to text by using client libraries  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/quickstarts/transcribe-client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Transcribe speech to text by using client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to send a speech recognition request to Speech-to-Text in your favorite programming language using the Google Cloud Client Libraries.

Speech-to-Text enables easy integration of Google speech recognition technologies into developer applications. You can send audio data to the Speech-to-Text API, which then returns a text transcription of that audio file. For more information about the service, see [Cloud STT basics](https://docs.cloud.google.com/speech-to-text/docs/basics). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Speech-to-Text APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=speech.googleapis.com,)

  5. Make sure that you have the following role or roles on the project: Cloud Speech Administrator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the Speech-to-Text APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=speech.googleapis.com,)

  12. Make sure that you have the following role or roles on the project: Cloud Speech Administrator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

Client libraries can use [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to easily authenticate with Google APIs and send requests to those APIs. With Application Default Credentials, you can test your application locally and deploy it without changing the underlying code. For more information, see [ Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




Also ensure you have [installed the client library](https://docs.cloud.google.com/speech-to-text/docs/libraries).

## Make an audio transcription request

Use the following code to send a [`Recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.Speech.Recognize) request to the Speech-to-Text API.

### Java
    
    
    // Imports the Google Cloud client library
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.speech.v2.[AutoDetectDecodingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.AutoDetectDecodingConfig.html);
    import com.google.cloud.speech.v2.[CreateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateRecognizerRequest.html);
    import com.google.cloud.speech.v2.[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata.html);
    import com.google.cloud.speech.v2.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig.html);
    import com.google.cloud.speech.v2.[RecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeRequest.html);
    import com.google.cloud.speech.v2.[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse.html);
    import com.google.cloud.speech.v2.[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer.html);
    import com.google.cloud.speech.v2.[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.html);
    import com.google.cloud.speech.v2.[SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechRecognitionAlternative.html);
    import com.google.cloud.speech.v2.[SpeechRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechRecognitionResult.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    
    public class QuickstartSampleV2 {
    
      public static void main(String[] args) throws IOException, ExecutionException,
          InterruptedException {
        String projectId = "my-project-id";
        String filePath = "path/to/audioFile.raw";
        String recognizerId = "my-recognizer-id";
        quickstartSampleV2(projectId, filePath, recognizerId);
      }
    
      public static void quickstartSampleV2(String projectId, String filePath, String recognizerId)
          throws IOException, ExecutionException, InterruptedException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.html) speechClient = [SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.html).create()) {
          Path path = Paths.get(filePath);
          byte[] data = Files.readAllBytes(path);
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) audioBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(data);
    
          String parent = String.format("projects/%s/locations/global", projectId);
    
          // First, create a recognizer
          [Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer.html) recognizer = [Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer.html).newBuilder()
              .setModel("latest_long")
              .addLanguageCodes("en-US")
              .build();
    
          [CreateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateRecognizerRequest.html) createRecognizerRequest = [CreateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateRecognizerRequest.html).newBuilder()
              .setParent(parent)
              .[setRecognizerId](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateRecognizerRequest.Builder.html#com_google_cloud_speech_v2_CreateRecognizerRequest_Builder_setRecognizerId_java_lang_String_)(recognizerId)
              .setRecognizer(recognizer)
              .build();
    
          OperationFuture<Recognizer, OperationMetadata> operationFuture =
              speechClient.[createRecognizerAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.html#com_google_cloud_speech_v2_SpeechClient_createRecognizerAsync__org_jspecify_annotations_Nullable_com_google_cloud_speech_v2_LocationName_com_google_cloud_speech_v2_Recognizer_java_lang_String_)(createRecognizerRequest);
          recognizer = operationFuture.get();
    
          // Next, create the transcription request
          [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig.html) recognitionConfig = [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig.html).newBuilder()
              .[setAutoDecodingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig.Builder.html#com_google_cloud_speech_v2_RecognitionConfig_Builder_setAutoDecodingConfig_com_google_cloud_speech_v2_AutoDetectDecodingConfig_)([AutoDetectDecodingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.AutoDetectDecodingConfig.html).newBuilder().build())
              .build();
    
          [RecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeRequest.html) request = [RecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeRequest.html).newBuilder()
              .setConfig(recognitionConfig)
              .setRecognizer(recognizer.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer.html#com_google_cloud_speech_v2_Recognizer_getName__)())
              .setContent(audioBytes)
              .build();
    
          [RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse.html) response = speechClient.recognize(request);
          List<SpeechRecognitionResult> results = response.[getResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse.html#com_google_cloud_speech_v2_RecognizeResponse_getResultsList__)();
    
          for ([SpeechRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechRecognitionResult.html) result : results) {
            // There can be several alternative transcripts for a given chunk of speech. Just use the
            // first (most likely) one here.
            if (result.getAlternativesCount() > 0) {
              [SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechRecognitionAlternative.html) alternative = result.getAlternativesList().get(0);
              System.out.printf("Transcription: %s%n", alternative.[getTranscript](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechRecognitionAlternative.html#com_google_cloud_speech_v2_SpeechRecognitionAlternative_getTranscript__)());
            }
          }
        }
      }
    }

### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def quickstart_v2(audio_file: str) -> cloud_speech.RecognizeResponse:
        """Transcribe an audio file.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
        Returns:
            cloud_speech.RecognizeResponse: The response from the recognize request, containing
            the transcription results
        """
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        # Instantiates a client
        client = SpeechClient()
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            language_codes=["en-US"],
            model="long",
        )
    
        request = cloud_speech.RecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            config=config,
            content=audio_content,
        )
    
        # Transcribes the audio into text
        response = client.recognize(request=request)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response
    
    

You sent your first request to Speech-to-Text.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps.

  1. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  2. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




### Console

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

* In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

* In the project list, select the project that you want to delete, and then click **Delete**. 
* In the dialog, type the project ID, and then click **Shut down** to delete the project. 

### gcloud

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * Learn how to [transcribe short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
  * Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize). 
  * Learn how to [transcribe long audio files](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize). 
  * For best performance, accuracy, and other tips, see the [best practices](https://docs.cloud.google.com/speech-to-text/docs/best-practices) documentation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
