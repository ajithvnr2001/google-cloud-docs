---
url: https://docs.cloud.google.com/speech-to-text/docs/batch-recognize/
title: Transcribe long audio files into text \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:39.393451+00:00
---

# Transcribe long audio files into text  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/batch-recognize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Transcribe long audio files into text Stay organized with collections  Save and categorize content based on your preferences. 

This page demonstrates how to transcribe long audio files (longer than one minute) to text using the Speech-to-Text API and asynchronous speech recognition.

## About asynchronous speech recognition

_Batch speech recognition_ starts a long-running audio processing operation. Use asynchronous speech recognition to transcribe audio that is longer than 60 seconds. For shorter audio, [synchronous speech recognition](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize) is faster and simpler. The upper limit for asynchronous speech recognition is 480 minutes (8 hours).

Batch speech recognition is only able to transcribe audio stored in Cloud Storage. The transcription output can be either provided inline in the response (for single-file batch recognition requests) or written to Cloud Storage.

The batch recognition request returns an [`Operation`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.longrunning#google.longrunning.Operation) that contains information about the ongoing recognition processing of your request. You can [poll the operation](https://docs.cloud.google.com/speech-to-text/docs/operations) to know when the operation is complete and transcripts are available.

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

## Enable access to Cloud Storage

Speech-to-Text uses a service account to access your files in Cloud Storage. By default, the service account has access to Cloud Storage files in the same project.

The service account email address is the following:
    
    
    service-PROJECT_NUMBER@gcp-sa-speech.iam.gserviceaccount.com
    

In order to transcribe Cloud Storage files in another project, you can give this service account the [Speech-to-Text Service Agent][speech-service-agent] role in the other project:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-speech.iam.gserviceaccount.com \
        --role=roles/speech.serviceAgent

More information about project IAM policy is available at [Manage access to projects, folders, and organizations][manage-access].

You can also give the service account more granular access by giving it permission to a specific Cloud Storage bucket:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-speech.iam.gserviceaccount.com \
        --role=roles/storage.admin

More information about managing access to Cloud Storage is available at [Create and Manage access control lists][buckets-manage-acl] in the Cloud Storage documentation.

## Perform batch recognition with inline results

Here is an example of performing batch speech recognition on an audio file in Cloud Storage and reading the transcription results inline from the response:

### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    def transcribe_batch_gcs_input_inline_output_v2(
        audio_uri: str,
    ) -> cloud_speech.BatchRecognizeResults:
        """Transcribes audio from a Google Cloud Storage URI using the Google Cloud Speech-to-Text API.
            The transcription results are returned inline in the response.
        Args:
            audio_uri (str): The Google Cloud Storage URI of the input audio file.
                Such as gs://[BUCKET]/[FILE]
        Returns:
            cloud_speech.BatchRecognizeResults: The response containing the transcription results.
        """
        # Instantiates a client
        client = SpeechClient()
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            language_codes=["en-US"],
            model="chirp_3",
        )
    
        file_metadata = cloud_speech.BatchRecognizeFileMetadata(uri=audio_uri)
    
        request = cloud_speech.BatchRecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            config=config,
            files=[file_metadata],
            recognition_output_config=cloud_speech.RecognitionOutputConfig(
                inline_response_config=cloud_speech.InlineOutputConfig(),
            ),
        )
    
        # Transcribes the audio into text
        operation = client.batch_recognize(request=request)
    
        print("Waiting for operation to complete...")
        response = operation.result(timeout=120)
    
        for result in response.results[audio_uri].transcript.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response.results[audio_uri].transcript
    

## Perform batch recognition and write results to Cloud Storage

Here is an example of performing batch speech recognition on an audio file in Cloud Storage and reading the transcription results from the output file in Cloud Storage. Note that the file written to Cloud Storage is a [`BatchRecognizeResults`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#batchrecognizeresults) message in JSON format:

### Python
    
    
    import os
    
    import re
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    def transcribe_batch_gcs_input_gcs_output_v2(
        audio_uri: str,
        gcs_output_path: str,
    ) -> cloud_speech.BatchRecognizeResults:
        """Transcribes audio from a Google Cloud Storage URI using the Google Cloud Speech-to-Text API.
        The transcription results are stored in another Google Cloud Storage bucket.
        Args:
            audio_uri (str): The Google Cloud Storage URI of the input audio file.
                E.g., gs://[BUCKET]/[FILE]
            gcs_output_path (str): The Google Cloud Storage bucket URI where the output transcript will be stored.
                E.g., gs://[BUCKET]
        Returns:
            cloud_speech.BatchRecognizeResults: The response containing the URI of the transcription results.
        """
        # Instantiates a client
        client = SpeechClient()
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
            language_codes=["en-US"],
            model="chirp_3",
        )
    
        file_metadata = cloud_speech.[BatchRecognizeFileMetadata](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.BatchRecognizeFileMetadata.html)(uri=audio_uri)
    
        request = cloud_speech.[BatchRecognizeRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.BatchRecognizeRequest.html)(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            config=config,
            files=[file_metadata],
            recognition_output_config=cloud_speech.[RecognitionOutputConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionOutputConfig.html)(
                gcs_output_config=cloud_speech.[GcsOutputConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.GcsOutputConfig.html)(
                    uri=gcs_output_path,
                ),
            ),
        )
    
        # Transcribes the audio into text
        operation = client.[batch_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.services.speech.SpeechClient.html#google_cloud_speech_v2_services_speech_SpeechClient_batch_recognize)(request=request)
    
        print("Waiting for operation to complete...")
        response = operation.result(timeout=120)
    
        file_results = response.results[audio_uri]
    
        print(f"Operation finished. Fetching results from {file_results.uri}...")
        output_bucket, output_object = re.match(
            r"gs://([^/]+)/(.*)", file_results.uri
        ).[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1, 2)
    
        # Instantiates a Cloud Storage client
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        # Fetch results from Cloud Storage
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(output_bucket)
        blob = bucket.blob(output_object)
        results_bytes = blob.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)()
        batch_recognize_results = cloud_speech.[BatchRecognizeResults](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.BatchRecognizeResults.html).from_json(
            results_bytes, ignore_unknown_fields=True
        )
    
        for result in batch_recognize_results.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return batch_recognize_results
    

## Perform batch recognition on multiple files

Here is an example of performing batch speech recognition on multiple audio files in Cloud Storage and reading the transcription results from the output files in Cloud Storage:

### Python
    
    
    import os
    import re
    from typing import List
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    def transcribe_batch_multiple_files_v2(
        audio_uris: List[str],
        gcs_output_path: str,
    ) -> cloud_speech.BatchRecognizeResponse:
        """Transcribes audio from multiple Google Cloud Storage URIs using the Google Cloud Speech-to-Text API.
        The transcription results are stored in another Google Cloud Storage bucket.
        Args:
            audio_uris (List[str]): The list of Google Cloud Storage URIs of the input audio files.
                Such as ["gs://[BUCKET]/[FILE]", "gs://[BUCKET]/[FILE]"]
            gcs_output_path (str): The Google Cloud Storage bucket URI where the output transcript is stored.
                Such as gs://[BUCKET]
        Returns:
            cloud_speech.BatchRecognizeResponse: The response containing the URIs of the transcription results.
        """
        # Instantiates a client
        client = SpeechClient()
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
            language_codes=["en-US"],
            model="chirp_3",
        )
    
        files = [cloud_speech.[BatchRecognizeFileMetadata](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.BatchRecognizeFileMetadata.html)(uri=uri) for uri in audio_uris]
    
        request = cloud_speech.[BatchRecognizeRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.BatchRecognizeRequest.html)(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            config=config,
            files=files,
            recognition_output_config=cloud_speech.[RecognitionOutputConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionOutputConfig.html)(
                gcs_output_config=cloud_speech.[GcsOutputConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.GcsOutputConfig.html)(
                    uri=gcs_output_path,
                ),
            ),
        )
    
        # Transcribes the audio into text
        operation = client.[batch_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.services.speech.SpeechClient.html#google_cloud_speech_v2_services_speech_SpeechClient_batch_recognize)(request=request)
    
        print("Waiting for operation to complete...")
        response = operation.result(timeout=120)
    
        print("Operation finished. Fetching results from:")
        for uri in audio_uris:
            file_results = response.results[uri]
            print(f"  {file_results.uri}...")
            output_bucket, output_object = re.match(
                r"gs://([^/]+)/(.*)", file_results.uri
            ).[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1, 2)
    
            # Instantiates a Cloud Storage client
            storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
            # Fetch results from Cloud Storage
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(output_bucket)
            blob = bucket.blob(output_object)
            results_bytes = blob.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)()
            batch_recognize_results = cloud_speech.[BatchRecognizeResults](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.BatchRecognizeResults.html).from_json(
                results_bytes, ignore_unknown_fields=True
            )
    
            for result in batch_recognize_results.results:
                print(f"     Transcript: {result.alternatives[0].transcript}")
    
        return response
    

## Enable dynamic batching on batch recognition

Dynamic batching enables lower cost transcription for higher latency. This feature is only available for batch recognition.

Here is an example of performing batch recognition on an audio file in Cloud Storage with dynamic batching enabled:

### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    def transcribe_batch_dynamic_batching_v2(
        audio_uri: str,
    ) -> cloud_speech.BatchRecognizeResults:
        """Transcribes audio from a Google Cloud Storage URI using dynamic batching.
        Args:
            audio_uri (str): The Cloud Storage URI of the input audio.
            E.g., gs://[BUCKET]/[FILE]
        Returns:
            cloud_speech.BatchRecognizeResults: The response containing the transcription results.
        """
        # Instantiates a client
        client = SpeechClient()
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            language_codes=["en-US"],
            model="chirp_3",
        )
    
        file_metadata = cloud_speech.BatchRecognizeFileMetadata(uri=audio_uri)
    
        request = cloud_speech.BatchRecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            config=config,
            files=[file_metadata],
            recognition_output_config=cloud_speech.RecognitionOutputConfig(
                inline_response_config=cloud_speech.InlineOutputConfig(),
            ),
            processing_strategy=cloud_speech.BatchRecognizeRequest.ProcessingStrategy.DYNAMIC_BATCHING,
        )
    
        # Transcribes the audio into text
        operation = client.batch_recognize(request=request)
    
        print("Waiting for operation to complete...")
        response = operation.result(timeout=120)
    
        for result in response.results[audio_uri].transcript.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response.results[audio_uri].transcript
    

## Override recognition features per file

Batch recognition by default uses the same recognition configuration for each file in the batch recognition request. If different files require different configuration or features, configuration can be overridden per file using the [`config`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.BatchRecognizeFileMetadata.FIELDS.google.cloud.speech.v2.RecognitionConfig.google.cloud.speech.v2.BatchRecognizeFileMetadata.config) field in the [`BatchRecognizeFileMetadata`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.BatchRecognizeFileMetadata.FIELDS.google.cloud.speech.v2.RecognitionConfig.google.cloud.speech.v2.BatchRecognizeFileMetadata.config) message. See the [recognizers documentation](https://docs.cloud.google.com/speech-to-text/docs/recognizers#override) for an example overriding recognition features.

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

* See the [reference documentation](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.Speech.BatchRecognize) for batch recognition. 
* Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize). 
* Learn how to [transcribe short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
* For best performance, accuracy, and other tips, see the [best practices](https://docs.cloud.google.com/speech-to-text/docs/best-practices) documentation. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
