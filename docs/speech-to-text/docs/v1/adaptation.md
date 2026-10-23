---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation/
title: Improve transcription results with model adaptation \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:21.148729+00:00
---

# Improve transcription results with model adaptation  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Improve transcription results with model adaptation Stay organized with collections  Save and categorize content based on your preferences. 

You can improve the accuracy of the transcription results you get from Cloud Speech-to-Text by using _model adaptation_. Model adaptation lets you specify words and phrases that Cloud STT will recognize more frequently in your audio data than other alternatives that might otherwise be suggested. Model adaptation is particularly useful for improving transcription accuracy in the following use cases:

  * Your audio contains words or phrases that are likely to occur frequently.
  * Your audio is likely to contain words that are rare (such as proper names) or words that don't exist in general use.
  * Your audio contains noise or is otherwise not very clear.



Before reading this document, read [Introduction to model adaptation](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation-model) for a high-level overview of how this feature works. For information about phrase and character limits per model adaptation request, see [Quotas and limits](https://docs.cloud.google.com/speech-to-text/docs/v1/quotas).

**Note:** Not all Cloud Speech-to-Text models support speech adaptation. See [Language Support](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) to see which models support adaptation.

## Code sample

Model adaptation is an optional Cloud STT configuration that you can use to customize your transcription results according to your needs. See the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig) documentation for more information about configuring the recognition request body.

The following code sample shows how to improve transcription accuracy using a [SpeechAdaptation](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#speechadaptation) resource: [`PhraseSet`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.phraseSets), [`CustomClass`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses), and [model adaptation boost](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation-model#fine-tune_transcription_results_using_boost). To use a `PhraseSet` or `CustomClass` in future requests, make a note of its resource `name`, returned in the response when you create the resource.

For a list of the prebuilt classes available for your language, see [Supported class tokens](https://docs.cloud.google.com/speech-to-text/docs/v1/class-tokens).

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    from google.cloud import speech_v1p1beta1 as speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def transcribe_with_model_adaptation(
        audio_uri: str,
        custom_class_id: str,
        phrase_set_id: str,
    ) -> str:
        """Create `PhraseSet` and `CustomClasses` for custom item lists in input data.
        Args:
            audio_uri (str): The Cloud Storage URI of the input audio. e.g. gs://[BUCKET]/[FILE]
            custom_class_id (str): The unique ID of the custom class to create
            phrase_set_id (str): The unique ID of the PhraseSet to create.
        Returns:
            The transcript of the input audio.
        """
        # Specifies the location where the Speech API will be accessed.
        location = "global"
    
        # Audio object
        audio = speech.RecognitionAudio(uri=audio_uri)
    
        # Create the adaptation client
        adaptation_client = speech.AdaptationClient()
    
        # The parent resource where the custom class and phrase set will be created.
        parent = f"projects/{PROJECT_ID}/locations/{location}"
    
        # Create the custom class resource
        adaptation_client.create_custom_class(
            {
                "parent": parent,
                "custom_class_id": custom_class_id,
                "custom_class": {
                    "items": [
                        {"value": "sushido"},
                        {"value": "altura"},
                        {"value": "taneda"},
                    ]
                },
            }
        )
        custom_class_name = (
            f"projects/{PROJECT_ID}/locations/{location}/customClasses/{custom_class_id}"
        )
        # Create the phrase set resource
        phrase_set_response = adaptation_client.create_phrase_set(
            {
                "parent": parent,
                "phrase_set_id": phrase_set_id,
                "phrase_set": {
                    "boost": 10,
                    "phrases": [
                        {"value": f"Visit restaurants like ${{{custom_class_name}}}"}
                    ],
                },
            }
        )
        phrase_set_name = phrase_set_response.name
        # The next section shows how to use the newly created custom
        # class and phrase set to send a transcription request with speech adaptation
    
        # Speech adaptation configuration
        speech_adaptation = speech.SpeechAdaptation(phrase_set_references=[phrase_set_name])
    
        # speech configuration object
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=24000,
            language_code="en-US",
            adaptation=speech_adaptation,
        )
    
        # Create the speech client
        speech_client = speech.SpeechClient()
    
        response = speech_client.recognize(config=config, audio=audio)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
