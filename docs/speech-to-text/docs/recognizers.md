---
url: https://docs.cloud.google.com/speech-to-text/docs/recognizers/
title: Recognizers \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:41.668017+00:00
---

# Recognizers  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/recognizers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Recognizers Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Speech-to-Text API V2 supports a Google Cloud resource called [recognizers](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#recognizer). Recognizers represent stored and reusable recognition configuration. You can use them to logically group together transcriptions or traffic for your application.

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

## Understand recognizers

Recognizers are configurable, reusable recognition configurations. Creating recognizers with frequently used recognition configuration helps to simplify and reduce the size of recognition requests.

The core element of a recognizer is its [default configuration](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.Recognizer.FIELDS.google.cloud.speech.v2.RecognitionConfig.google.cloud.speech.v2.Recognizer.default_recognition_config). This is the configuration for every recognition request that this recognizer performs. You can override this default per request. Keep the default configuration for features you need across requests for a given recognizer, while overriding specific features for specific requests.

Reuse recognizers as often as possible. Creating one for each request dramatically increases the latency of your application and consumes your [resource quotas](https://docs.cloud.google.com/speech-to-text/quotas). Create them infrequently during integration and setup, then reuse them for recognition requests.

## Create recognizers

Here is an example of creating a recognizer that can be used to send recognition requests:

### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def create_recognizer(recognizer_id: str) -> cloud_speech.Recognizer:
        """Сreates a recognizer with an unique ID and default recognition configuration.
        Args:
            recognizer_id (str): The unique identifier for the recognizer to be created.
        Returns:
            cloud_speech.Recognizer: The created recognizer object with configuration.
        """
        # Instantiates a client
        client = SpeechClient()
    
        request = cloud_speech.CreateRecognizerRequest(
            parent=f"projects/{PROJECT_ID}/locations/global",
            recognizer_id=recognizer_id,
            recognizer=cloud_speech.Recognizer(
                default_recognition_config=cloud_speech.RecognitionConfig(
                    language_codes=["en-US"], model="long"
                ),
            ),
        )
        # Sends the request to create a recognizer and waits for the operation to complete
        operation = client.create_recognizer(request=request)
        recognizer = operation.result()
    
        print("Created Recognizer:", recognizer.name)
        return recognizer
    
    

## Use an existing recognizer to send requests

Here is an example of sending multiple recognition requests using the same recognizer:

### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def transcribe_reuse_recognizer(
        audio_file: str,
        recognizer_id: str,
    ) -> cloud_speech.RecognizeResponse:
        """Transcribe an audio file using an existing recognizer.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
                Example: "resources/audio.wav"
            recognizer_id (str): The ID of the existing recognizer to be used for transcription.
        Returns:
            cloud_speech.RecognizeResponse: The response containing the transcription results.
        """
        # Instantiates a client
        client = SpeechClient()
    
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        request = cloud_speech.RecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/{recognizer_id}",
            content=audio_content,
        )
    
        # Transcribes the audio into text
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(request=request)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response
    
    

## Enable features in a recognizer

Recognizers can be used to enable various features in recognition, such as [automatic punctuation](https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation) or [profanity filtering](https://docs.cloud.google.com/speech-to-text/docs/profanity-filter).

Here is an example of enabling automatic punctuation in a recognizer, which enables automatic punctuation in the recognition request using this recognizer:

**Note:** Samples throughout the documentation repeatedly illustrate creating recognizers. However, you should create them infrequently and reuse them often.

### Python
    
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    from google.api_core.exceptions import NotFound
    
    # Instantiates a client
    client = SpeechClient()
    
    # TODO(developer): Update and un-comment below line
    # PROJECT_ID = "your-project-id"
    # recognizer_id = "id-recognizer"
    recognizer_name = (
        f"projects/{PROJECT_ID}/locations/global/recognizers/{recognizer_id}"
    )
    try:
        # Use an existing recognizer
        recognizer = client.[get_recognizer](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.services.speech.SpeechClient.html#google_cloud_speech_v2_services_speech_SpeechClient_get_recognizer)(name=recognizer_name)
        print("Using existing Recognizer:", recognizer.name)
    except NotFound:
        # Create a new recognizer
        request = cloud_speech.[CreateRecognizerRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.CreateRecognizerRequest.html)(
            parent=f"projects/{PROJECT_ID}/locations/global",
            recognizer_id=recognizer_id,
            recognizer=cloud_speech.[Recognizer](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.Recognizer.html)(
                default_recognition_config=cloud_speech.RecognitionConfig(
                    auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
                    language_codes=["en-US"],
                    model="latest_long",
                    features=cloud_speech.[RecognitionFeatures](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionFeatures.html)(
                        enable_automatic_punctuation=True,
                    ),
                ),
            ),
        )
        operation = client.[create_recognizer](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.services.speech.SpeechClient.html#google_cloud_speech_v2_services_speech_SpeechClient_create_recognizer)(request=request)
        recognizer = operation.result()
        print("Created Recognizer:", recognizer.name)
    
    # Reads a file as bytes
    with open(audio_file, "rb") as f:
        audio_content = f.read()
    
    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/{recognizer_id}",
        content=audio_content,
    )
    
    # Transcribes the audio into text
    response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(request=request)
    
    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")
    

## Override recognizer features in recognition requests

Here is an example of enabling multiple features in a recognizer, but disabling automatic punctuation for this recognition request:

### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    from google.protobuf.field_mask_pb2 import FieldMask
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def transcribe_override_recognizer(
        audio_file: str,
        recognizer_id: str,
    ) -> cloud_speech.RecognizeResponse:
        """Transcribe an audio file using an existing recognizer with overridden settings for the recognition request.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
                Example: "resources/audio.wav"
            recognizer_id (str): The unique ID of the recognizer to be used for transcription.
        Returns:
            cloud_speech.RecognizeResponse: The response containing the transcription results.
        """
        # Instantiates a client
        client = SpeechClient()
    
        request = cloud_speech.[CreateRecognizerRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.CreateRecognizerRequest.html)(
            parent=f"projects/{PROJECT_ID}/locations/global",
            recognizer_id=recognizer_id,
            recognizer=cloud_speech.[Recognizer](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.Recognizer.html)(
                default_recognition_config=cloud_speech.RecognitionConfig(
                    auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
                    language_codes=["en-US"],
                    model="latest_long",
                    features=cloud_speech.[RecognitionFeatures](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionFeatures.html)(
                        enable_automatic_punctuation=True,
                        enable_word_time_offsets=True,
                    ),
                ),
            ),
        )
    
        operation = client.[create_recognizer](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.services.speech.SpeechClient.html#google_cloud_speech_v2_services_speech_SpeechClient_create_recognizer)(request=request)
        recognizer = operation.result()
    
        print("Created Recognizer:", recognizer.name)
    
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        request = cloud_speech.RecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/{recognizer_id}",
            config=cloud_speech.RecognitionConfig(
                features=cloud_speech.[RecognitionFeatures](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionFeatures.html)(
                    enable_word_time_offsets=False,
                ),
            ),
            config_mask=FieldMask(paths=["features.enable_word_time_offsets"]),
            content=audio_content,
        )
    
        # Transcribes the audio into text
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(request=request)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response
    
    

## Send requests without recognizers

Recognizers are optional in recognition requests. To make a request without a recognizer, use the recognizer resource ID `_` in the location you are making a request. Here is an example:

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
