---
url: https://docs.cloud.google.com/speech-to-text/docs/adaptation-model/
title: Improve transcription results with model adaptation \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:28.911155+00:00
---

# Improve transcription results with model adaptation  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/adaptation-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Improve transcription results with model adaptation Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

You can use the **model adaptation** feature to help Speech-to-Text recognize specific words or phrases more frequently than other options that might otherwise be suggested. For example, suppose that your audio data often includes the word "weather." When Speech-to-Text encounters the word "weather," you want it to transcribe the word as "weather" more often than "whether." In this case, you might use model adaptation to bias Speech-to-Text toward recognizing "weather."

Model adaptation is particularly helpful in the following use cases:

  * Improving the accuracy of words and phrases that occur frequently in your audio data. For example, you can alert the recognition model to voice commands that are typically spoken by your users.

    * Expanding the vocabulary of words recognized by Speech-to-Text. Speech-to-Text includes a very large vocabulary. However, if your audio data often contains words that are rare in general language use (such as proper names or domain-specific words), you can add them using model adaptation.

    * Improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear.




Optionally, you can fine-tune the biasing of the recognition model using the [model adaptation boost feature](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model#fine-tune_transcription_results_using_boost).

## Improve recognition of words and phrases

To increase the probability that Speech-to-Text recognizes the word "weather" when it transcribes your audio data, you can pass the single word "weather" in the [`PhraseSet`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#phraseset) object in a [SpeechAdaptation](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#speechadaptation) resource.

When you provide a multi-word phrase, Speech-to-Text is more likely to recognize those words in sequence. Providing a phrase also increases the probability of recognizing portions of the phrase, including individual words. See the [content limits](https://docs.cloud.google.com/speech-to-text/quotas) page for limits on the number and size of these phrases.

## Improve recognition using classes

**Classes** represent common concepts that occur in natural language, such as monetary units and calendar dates. A class helps you improve transcription accuracy for large groups of words that map to a common concept, but that don't always include identical words or phrases.

For example, suppose that your audio data includes recordings of people saying their street address. You might have an audio recording of someone saying "My house is 123 Main Street, the fourth house on the left." In this case, you want Speech-to-Text to recognize the first sequence of numerals ("123") as an address rather than as an ordinal ("one-hundred twenty-third"). However, not all people live at "123 Main Street." It's impractical to list every possible street address in a `PhraseSet` resource. Instead, you can use a class to indicate that a street number should be recognized no matter what the number actually is. In this example, Speech-to-Text could then more accurately transcribe phrases like "123 Main Street" and "987 Grand Boulevard" because they are both recognized as address numbers.

### Class tokens

To use a class in model adaptation, include a **class token** in the `phrases` field of a `PhraseSet` resource. Refer to the [list of supported class tokens](https://docs.cloud.google.com/speech-to-text/docs/class-tokens) to see which tokens are available for your language. For example, to improve the transcription of address numbers from your source audio, provide the value `$ADDRESSNUM` within a phrase in a `PhraseSet.`

You can use classes as standalone items in the `phrases` array or embed one or more class tokens in longer multi-word phrases. For example, you can indicate an address number in a larger phrase by including the class token in a string: `["my address is $ADDRESSNUM"]`. However, this phrase will not help in cases where the audio contains a similar but non-identical phrase, such as "I am at 123 Main Street". To aid recognition of similar phrases, it's important to additionally include the class token by itself: `["my address is $ADDRESSNUM", "$ADDRESSNUM"]`. If you use an invalid or malformed class token, Speech-to-Text ignores the token without triggering an error but still uses the rest of the phrase for context.

**Note:** Class availability varies by [transcription model](https://docs.cloud.google.com/speech-to-text/docs/transcription-model) and language.

### Custom classes

You can also create your own `CustomClass`, a class composed of your own custom list of related items or values. For example, you want to transcribe audio data that is likely to include the name of any one of several hundred regional restaurants. Restaurant names are relatively rare in general speech and therefore less likely to be chosen as the "correct" answer by the recognition model. You can bias the recognition model toward correctly identifying these names when they appear in your audio using a custom class.

To use a custom class, create a [`CustomClass`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#customclass) resource that includes each restaurant name as a `ClassItem`. Custom classes function in the same way as the [pre-built class tokens](https://docs.cloud.google.com/speech-to-text/docs/class-tokens). A `phrase` can include both prebuilt class tokens and custom classes.

## Fine-tune transcription results using boost

By default model adaptation provides a relatively small effect, especially for one-word phrases. The model adaptation [**boost** feature](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.PhraseSet.FIELDS.float.google.cloud.speech.v2.PhraseSet.boost) lets you increase the recognition model bias by assigning more weight to some phrases than others. We recommend that you implement boost if all of the following are true:

  1. You have already implemented model adaptation.
  2. You would like to further adjust the strength of model adaptation effects on your transcription results. To see whether the boost feature is available for your language, see the [language support page](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages).



For example, you have many recordings of people asking about the "fare to get into the county fair," with the word "fair" occurring more frequently than "fare." In this case, you can use model adaptation to increase the probability of the model recognizing both "fair" and "fare" by adding them as `phrases` in a `PhraseSet` resource. This will tell Speech-to-Text to recognize "fair" and "fare" more often than, for example, "hare" or "lair."

However, "fair" should be recognized more often than "fare" due to its more frequent appearances in the audio. You might have already transcribed your audio using the Speech-to-Text API and found a high number of errors recognizing the correct word ("fair"). In this case, you might want to use the **boost** feature to assign a higher boost value to "fair" than "fare". The higher weighted value assigned to "fair" biases the Speech-to-Text API toward picking "fair" more frequently than "fare". Without boost values, the recognition model will recognize "fair" and "fare" with equal probability.

### Boost basics

When you use boost, you assign a weighted value to `phrase` items in a `PhraseSet` resource. Speech-to-Text refers to this weighted value when selecting a possible transcription for words in your audio data. The higher the value, the higher the likelihood that Speech-to-Text chooses that word or phrase from the possible alternatives.

If you assign a boost value to a multi-word phrase, boost is applied to the entire phrase and only the entire phrase. For example, you want to assign a boost value to the phrase "My favorite exhibit at the American Museum of Natural History is the blue whale". If you add that phrase to a `phrase` object and assign a boost value, the recognition model will be more likely to recognize that phrase in its entirety, word-for-word.

If you don't get the results you're looking for by boosting a multi-word phrase, we suggest that you add all bigrams (2-words, in order) that make up the phrase as additional `phrase` items and assign boost values to each. Continuing the previous example, you could investigate adding additional bigrams and endgrams (more than two words), such as "my favorite", "my favorite exhibit", "favorite exhibit", "my favorite exhibit at the American Museum of Natural History", "American Museum of Natural History", and "blue whale". The STT recognition model is then more likely to recognize related phrases in your audio that contain parts of the original boosted phrase but don't match it word-for-word.

### Set boost values

Boost values must be a float value greater than 0. The practical maximum limit for boost values is 20. For best results, experiment with your transcription results by adjusting your boost values up or down until you get accurate transcription results.

Higher boost values can result in fewer false negatives, which are cases where the word or phrase occurred in the audio but wasn't correctly recognized by Speech-to-Text. However, boost can also increase the likelihood of false positives; that is, cases where the word or phrase appears in the transcription even though it didn't occur in the audio.

## Example use case using model adaptation

The following example walks you through the process of using model adaptation to transcribe an audio recording of someone saying "The word is fare". In this case, without speech adaptation, Speech-to-Text identifies the word "fair." Using speech adaptation Speech-to-Text can identify the word "fare" instead.

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

### Improve transcription using a `PhraseSet`

  1. The following sample builds a `PhraseSet` with the phrase "fare" and adds it as an `inline_phrase_set` in a recognition request:



### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def adaptation_v2_inline_phrase_set(audio_file: str) -> cloud_speech.RecognizeResponse:
        """Enhances speech recognition accuracy using an inline phrase set.
        The inline custom phrase set helps the recognizer produce more accurate transcriptions for specific terms.
        Phrases are given a boost to increase their chances of being recognized correctly.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
        Returns:
            cloud_speech.RecognizeResponse: The full response object which includes the transcription results.
        """
    
        # Instantiates a client
        client = SpeechClient()
    
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        # Build inline phrase set to produce a more accurate transcript
        phrase_set = cloud_speech.PhraseSet(
            phrases=[{"value": "fare", "boost": 10}, {"value": "word", "boost": 20}]
        )
        adaptation = cloud_speech.SpeechAdaptation(
            phrase_sets=[
                cloud_speech.SpeechAdaptation.AdaptationPhraseSet(
                    inline_phrase_set=phrase_set
                )
            ]
        )
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            adaptation=adaptation,
            language_codes=["en-US"],
            model="short",
        )
    
        # Prepare the request which includes specifying the recognizer, configuration, and the audio content
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
    
    

  1. This sample creates a `PhraseSet` resource with the same phrase and then references it in a recognition request:



### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def adaptation_v2_phrase_set_reference(
        audio_file: str,
        phrase_set_id: str,
    ) -> cloud_speech.RecognizeResponse:
        """Transcribe audio files using a PhraseSet.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
            phrase_set_id (str): The unique ID of the PhraseSet to use.
        Returns:
            cloud_speech.RecognizeResponse: The full response object which includes the transcription results.
        """
    
        # Instantiates a client
        client = SpeechClient()
    
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        # Creating operation of creating the PhraseSet on the cloud.
        operation = client.[create_phrase_set](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.services.speech.SpeechClient.html#google_cloud_speech_v2_services_speech_SpeechClient_create_phrase_set)(
            parent=f"projects/{PROJECT_ID}/locations/global",
            phrase_set_id=phrase_set_id,
            phrase_set=cloud_speech.PhraseSet(phrases=[{"value": "fare", "boost": 10}]),
        )
        phrase_set = operation.result()
    
        # Add a reference of the PhraseSet into the recognition request
        adaptation = cloud_speech.SpeechAdaptation(
            phrase_sets=[
                cloud_speech.SpeechAdaptation.[AdaptationPhraseSet](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.SpeechAdaptation.AdaptationPhraseSet.html)(
                    phrase_set=phrase_set.name
                )
            ]
        )
    
        # Automatically detect audio encoding. Use "short" model for short utterances.
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
            adaptation=adaptation,
            language_codes=["en-US"],
            model="short",
        )
        #  Prepare the request which includes specifying the recognizer, configuration, and the audio content
        request = cloud_speech.RecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            config=config,
            content=audio_content,
        )
        # Transcribes the audio into text
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(request=request)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response
    
    

### Improve transcription results using a `CustomClass`

  1. The following sample builds a `CustomClass` with an item "fare" and name "fare". It then references the `CustomClass` within an `inline_phrase_set` in a recognition request:



### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def adaptation_v2_inline_custom_class(
        audio_file: str,
    ) -> cloud_speech.RecognizeResponse:
        """Transcribe audio file using inline custom class.
        The inline custom class helps the recognizer produce more accurate transcriptions for specific terms.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
        Returns:
            cloud_speech.RecognizeResponse: The response object which includes the transcription results.
        """
        # Instantiates a client
        client = SpeechClient()
    
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        # Define an inline custom class to enhance recognition accuracy with specific items like "fare" etc.
        custom_class_name = "your-class-name"
        custom_class = cloud_speech.CustomClass(
            name=custom_class_name,
            items=[{"value": "fare"}],
        )
    
        # Build inline phrase set to produce a more accurate transcript
        phrase_set = cloud_speech.PhraseSet(
            phrases=[{"value": custom_class_name, "boost": 20}]
        )
        adaptation = cloud_speech.SpeechAdaptation(
            phrase_sets=[
                cloud_speech.SpeechAdaptation.AdaptationPhraseSet(
                    inline_phrase_set=phrase_set
                )
            ],
            custom_classes=[custom_class],
        )
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            adaptation=adaptation,
            language_codes=["en-US"],
            model="short",
        )
    
        # Prepare the request which includes specifying the recognizer, configuration, and the audio content
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
    
    

  1. This sample creates a `CustomClass` resource with the same item. It then creates a `PhraseSet` resource with a phrase referencing the `CustomClass` resource name. It then references the`PhraseSet` resource in a recognition request:



### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def adaptation_v2_custom_class_reference(
        audio_file: str, phrase_set_id: str, custom_class_id: str
    ) -> cloud_speech.RecognizeResponse:
        """Transcribe audio file using a custom class.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
            phrase_set_id (str): The unique ID of the phrase set to use.
            custom_class_id (str): The unique ID of the custom class to use.
        Returns:
            cloud_speech.RecognizeResponse: The full response object which includes the transcription results.
        """
        # Instantiates a speech client
        client = SpeechClient()
    
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        # Create a custom class to improve recognition accuracy for specific terms
        custom_class = cloud_speech.CustomClass(items=[{"value": "fare"}])
        operation = client.[create_custom_class](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.services.speech.SpeechClient.html#google_cloud_speech_v2_services_speech_SpeechClient_create_custom_class)(
            parent=f"projects/{PROJECT_ID}/locations/global",
            custom_class_id=custom_class_id,
            custom_class=custom_class,
        )
        custom_class = operation.result()
    
        # Create a persistent PhraseSet to reference in a recognition request
        created_phrase_set = cloud_speech.PhraseSet(
            phrases=[
                {
                    "value": f"${{{custom_class.name}}}",
                    "boost": 20,
                },  # Using custom class reference
            ]
        )
        operation = client.[create_phrase_set](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.services.speech.SpeechClient.html#google_cloud_speech_v2_services_speech_SpeechClient_create_phrase_set)(
            parent=f"projects/{PROJECT_ID}/locations/global",
            phrase_set_id=phrase_set_id,
            phrase_set=created_phrase_set,
        )
        phrase_set = operation.result()
    
        # Add a reference of the PhraseSet into the recognition request
        adaptation = cloud_speech.SpeechAdaptation(
            phrase_sets=[
                cloud_speech.SpeechAdaptation.[AdaptationPhraseSet](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.SpeechAdaptation.AdaptationPhraseSet.html)(
                    phrase_set=phrase_set.name
                )
            ]
        )
        # Automatically detect the audio's encoding with short audio model
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
            adaptation=adaptation,
            language_codes=["en-US"],
            model="short",
        )
    
        # Create a custom class to reference in a PhraseSet
        request = cloud_speech.RecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            config=config,
            content=audio_content,
        )
    
        # Transcribes the audio into text
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(request=request)
    
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

  * Review the [list of supported class tokens](https://docs.cloud.google.com/speech-to-text/docs/class-tokens). 
  * Learn how to [transcribe short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
  * Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize). 
  * Learn how to [transcribe long audio files](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
