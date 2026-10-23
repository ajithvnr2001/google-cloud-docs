---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation-model/
title: Introduction to model adaptation \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:06.783396+00:00
---

# Introduction to model adaptation  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation-model/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Introduction to model adaptation Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

You can use _model adaptation_ feature to help Cloud Speech-to-Text recognize specific words or phrases more frequently than other options that might otherwise be suggested. For example, suppose that your audio data often includes the word "weather". When Cloud STT encounters the word "weather," you want it to transcribe the word as "weather" more often than "whether." In this case, you might use model adaptation to bias Cloud STT toward recognizing "weather."

Model adaptation is particularly helpful in the following use cases:

  * Improving the accuracy of words and phrases that occur frequently in your audio data. For example, you can alert the recognition model to voice commands that are typically spoken by your users.

  * Expanding the vocabulary of words recognized by Cloud STT. Cloud STT includes a very large vocabulary. However, if your audio data often contains words that are rare in general language use (such as proper names or domain-specific words), you can add them using model adaptation.

  * Improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear.




To see whether the model adaptation feature is available for your language, see the [language support page](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages).

## Improve recognition of words and phrases

To increase the probability that Cloud STT recognizes the word "weather" when it transcribes your audio data, you can pass the single word "weather" in the [`PhraseSet`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.phraseSets) object in a [SpeechAdaptation](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#speechadaptation) resource.

When you provide a multi-word phrase, Cloud STT is more likely to recognize those words in sequence. Providing a phrase also increases the probability of recognizing portions of the phrase, including individual words. See the [content limits](https://docs.cloud.google.com/speech-to-text/docs/v1/quotas#content) page for limits on the number and size of these phrases.

Optionally, you can fine-tune the strength of model adaptation using the [model adaptation boost feature](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation-model#fine-tune_transcription_results_using_boost).

## Improve recognition using classes

**Classes** represent common concepts that occur in natural language, such as monetary units and calendar dates. A class lets you improve transcription accuracy for large groups of words that map to a common concept, but that don't always include identical words or phrases.

For example, suppose that your audio data includes recordings of people saying their street address. You might have an audio recording of someone saying "My house is 123 Main Street, the fourth house on the left." In this case, you want Cloud STT to recognize the first sequence of numerals ("123") as an address rather than as an ordinal ("one-hundred twenty-third"). However, not all people live at "123 Main Street." It's impractical to list every possible street address in a `PhraseSet` resource. Instead, you can use a class to indicate that a street number should be recognized no matter what the number actually is. In this example, Cloud STT could then more accurately transcribe phrases like "123 Main Street" and "987 Grand Boulevard" because they are both recognized as address numbers.

### Class tokens

To use a class in model adaptation, include a **class token** in the `phrases` field of a `PhraseSet` resource. Refer to the [list of supported class tokens](https://docs.cloud.google.com/speech-to-text/docs/v1/class-tokens) to see which tokens are available for your language. For example, to improve the transcription of address numbers from your source audio, provide the value `$ADDRESSNUM` in your `SpeechContext` object.

You can use classes either as stand-alone items in the `phrases` array or embed one or more class tokens in longer multi-word phrases. For example, you can indicate an address number in a larger phrase by including the class token in a string: `["my address is $ADDRESSNUM"]`. However, this phrase will not help in cases where the audio contains a similar but non-identical phrase, such as "I am at 123 Main Street". To aid recognition of similar phrases, it's important to additionally include the class token by itself: `["my address is $ADDRESSNUM", "$ADDRESSNUM"]`. If you use an invalid or malformed class token, Cloud STT ignores the token without triggering an error but still uses the rest of the phrase for context.

**Note:** Class availability varies by [transcription model](https://docs.cloud.google.com/speech-to-text/docs/v1/transcription-model) and language.

### Custom classes

You can also create your own `CustomClass`, a class composed of your own custom list of related items or values. For example, you want to transcribe audio data that is likely to include the name of any one of several hundred regional restaurants. Restaurant names are relatively rare in general speech and therefore less likely to be chosen as the "correct" answer by the recognition model. You can bias the recognition model toward correctly identifying these names when they appear in your audio using a custom class.

To use a custom class, create a [`CustomClass`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses) resource that includes each restaurant name as a `ClassItem`. Custom classes function in the same way as the [pre-built class tokens](https://docs.cloud.google.com/speech-to-text/docs/v1/class-tokens). A `phrase` can include both prebuilt class tokens and custom classes.

### ABNF Grammars

You can also use grammars in _augmented Backus–Naur form (ABNF)_ to specify patterns of words. Including an ABNF grammar in the request's model adaptation will increase the probability that Cloud STT recognizes all words that match the specified grammar.

To use this feature, include an [`ABNF grammar`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#ABNFGrammar) object in your request's `SpeechAdaptation` field. ABNF grammars can also include references to [`CustomClass`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses) and [`PhraseSet`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.phraseSets) resources. To learn more about the syntax for this field, see the [`Speech Recognition Grammar Specification`](https://www.w3.org/TR/speech-grammar/) and our [`code sample`](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation-model#improve_transcription_results_using_an_abnf_grammar) in the following section.

## Fine-tune transcription results using boost

By default [model adaptation](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation) should already provide a sufficient effect in most of the cases. The model adaptation [**boost** feature](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.phraseSets#PhraseSet) lets you increase the recognition model bias by assigning more weight to some phrases than others. We recommend that you implement boost only if 1) you have already implemented model adaptation, and 2) you would like to further adjust the strength of model adaptation effects on your transcription results.

**Note:** For best results we recommend providing phrases both with and without boost in your requests.

For example, you have many recordings of people asking about the "fare to get into the county fair," with the word "fair" occurring more frequently than "fare." In this case, you can use model adaptation to increase the probability of the model recognizing both "fair" and "fare" by adding them as `phrases` in a `PhraseSet` resource. This will tell Cloud STT to recognize "fair" and "fare" more often than, for example, "hare" or "lair."

However, "fair" should be recognized more often than "fare" due to its more frequent appearances in the audio. You might have already transcribed your audio using the Cloud Speech-to-Text API and found a high number of errors recognizing the correct word ("fair"). In this case, you might want to additionally use the phrases with **boost** to assign a higher boost value to "fair" than "fare". The higher weighted value assigned to "fair" biases the Cloud Speech-to-Text API toward picking "fair" more frequently than "fare". Without boost values, the recognition model will recognize "fair" and "fare" with equal probability.

### Boost basics

When you use boost, you assign a weighted value to `phrase` items in a `PhraseSet` resource. Cloud STT refers to this weighted value when selecting a possible transcription for words in your audio data. The higher the value, the higher the likelihood that Cloud STT chooses that word or phrase from the possible alternatives.

**Note:** If you assign a boost value to a multi-word phrase, boost is applied to the entire phrase and only the entire phrase.

For example, you want to assign a boost value to the phrase "My favorite exhibit at the American Museum of Natural History is the blue whale". If you add that phrase to a `phrase` object and assign a boost value, the recognition model will be more likely to recognize that phrase in its entirety, word-for-word.

If you don't get the results you're looking for by boosting a multi-word phrase, we suggest that you add all bigrams (2-words, in order) that make up the phrase as additional `phrase` items and assign boost values to each. Continuing the preceding example, you could investigate adding additional bigrams and N-grams (more than 2 words) such as "my favorite", "my favorite exhibit", "favorite exhibit", "my favorite exhibit at the American Museum of Natural History", "American Museum of Natural History", or "blue whale." The Cloud STT recognition model is then more likely to recognize related phrases in your audio that contain parts of the original boosted phrase but don't match it word-for-word.

### Set boost values

Boost values must be a float value greater than 0. The practical maximum limit for boost values is 20. For best results, experiment with your transcription results by adjusting your boost values up or down until you get accurate transcription results.

Higher boost values can result in fewer false negatives, which are cases where the word or phrase occurred in the audio but wasn't correctly recognized by Cloud STT. However, boost can also increase the likelihood of false positives; that is, cases where the word or phrase appears in the transcription even though it didn't occur in the audio.

### Get timeout notifications

Cloud STT responses include a [`SpeechAdaptationInfo`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize#speechadaptationinfo) field, which provides information on model adaptation behavior during recognition. If a timeout related to model adaptation occurred, `adaptationTimeout` will be `true` and `timeoutMessage` will specify which adaptation configuration caused the timeout. When a timeout occurs, model adaptation has no effect on the returned transcript.

## Example use case using model adaptation

The following example walks you through the process of using model adaptation to transcribe an audio recording of someone saying "call me fionity and oh my gosh what do we have here ionity". In this case it is important that the model identify "fionity" and "ionity" correctly.

The following command performs recognition on the audio without model adaptation. The resulting transcription is _incorrect_ : "call me Fiona tea and oh my gosh what do we have here I own a day".
    
    
       curl -H "Authorization: Bearer $(gcloud auth
       --impersonate-service-account=$SA_EMAIL print-access-token)" -H
       "Content-Type: application/json; charset=utf-8"
       "https://speech.googleapis.com/v1p1beta1/speech:recognize" -d '{"config":
       {"languageCode": "en-US"}, "audio":
       {"uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"}}'
       

Example request: 
    
    
         {
           "config":{
           "languageCode":"en-US"
           },
           "audio":{
              "uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"
           }
         }
       

### Improve transcription using a `PhraseSet`

  1. Create a `PhraseSet`:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/projects/project_id/locations/global/phraseSets"
         -d '{"phraseSetId": "test-phrase-set-1"}'

Example request:
         
         {
            "phraseSetId":"test-phrase-set-1"
         }

  2. Get the `PhraseSet`:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/projects/project_id>/locations/global/phraseSets/test-phrase-set-1"\

  3. Add the phrases "fionity" and "ionity" to the `PhraseSet` and assign a `boost` value of 10 to each:
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/projects/project_id/locations/global/phraseSets/test-phrase-set-1?updateMask=phrases"\
         -d '{"phrases": [{"value": "ionity", "boost": 10}, {"value": "fionity", "boost": 10}]}'

The `PhraseSet` is now updated to:
         
         {
           "phrases":[
              {
                   "value":"ionity",
                   "boost":10
                },
                {
                   "value":"fionity",
                   "boost":10
                }
             ]
          }

  4. Recognize the audio again, this time using model adaptation and the `PhraseSet`created previously. The transcribed results are now correct: "call me fionity and oh my gosh what do we have here ionity".
         
         curl -H "Authorization: Bearer $(gcloud auth --impersonate-service-account=$SA_EMAIL print-access-token)"
         -H "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/speech:recognize" -d '{"config":
         {"adaptation": {"phrase_set_references": ["projects/project_id/locations/global/phraseSets/test-phrase-set-1"]},
         "languageCode": "en-US"}, "audio": {"uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"}}'

Example request:
         
         {
            "config":{
               "adaptation":{
                  "phrase_set_references":[
                     "projects/project_id/locations/global/phraseSets/test-phrase-set-1"
                  ]
               },
               "languageCode":"en-US"
            },
            "audio":{
               "uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"
            }
         }




### Improve transcription results using a `CustomClass`

  1. Create a `CustomClass`:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/projects/project_id/locations/global/customClasses"
         -d '{"customClassId": "test-custom-class-1"}'

Example request:
         
         {
            "customClassId": "test-custom-class-1"
         }

  2. Get the `CustomClass`:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth
          --impersonate-service-account=$SA_EMAIL print-access-token)" -H
          "Content-Type: application/json; charset=utf-8"
          "https://speech.googleapis.com/v1p1beta1/projects/project_id/locations/global/customClasses/test-custom-class-1"
          

  3. Recognize the test audio clip. The `CustomClass` is empty, so the returned transcript is still incorrect: "call me Fiona tea and oh my gosh what do we have here I own a day":
         
         curl -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/speech:recognize" -d '{"config":
         {"adaptation": {"phraseSets": [{"phrases": [{"value":
         "${projects/project_idlocations/global/customClasses/test-custom-class-1}",
         "boost": "10"}]}]}, "languageCode": "en-US"}, "audio":
         {"uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"}}'

Example request:
         
         {
            "config":{
               "adaptation":{
                  "phraseSets":[
                     {
                        "phrases":[
                           {
                              "value":"${projects/project_id/locations/global/customClasses/test-custom-class-1}",
                              "boost":"10"
                           }
                        ]
                     }
                  ]
               },
               "languageCode":"en-US"
            },
            "audio":{
               "uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"
            }
          }

  4. Add the phrases "fionity" and "ionity" to the custom class:
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/projects/project_id/locations/global/customClasses/test-custom-class-1?updateMask=items"
         -d '{"items": [{"value": "ionity"}, {"value": "fionity"}]}'

This updates the custom class to the following:
         
         {
            "items":[
               {
                  "value":"ionity"
               },
               {
                  "value":"fionity"
               }
            ]
         }

  5. Recognize the sample audio again, this time with "fionity" and "ionity" in the `CustomClass`. The transcript is now correct: "call me fionity and oh my gosh what do we have here ionity".
         
         curl -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/speech:recognize" -d '{"config":
         {"adaptation": {"phraseSets": [{"phrases": [{"value":
         "${projects/project_id/locations/global/customClasses/test-custom-class-1}",
         "boost": "10"}]}]}, "languageCode": "en-US"}, "audio":
         {"uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"}}'

Example request: 
         
         {
            "config":{
               "adaptation":{
                  "phraseSets":[
                     {
                        "phrases":[
                           {
         "value":"${projects/project_id/locations/global/customClasses/test-custom-class-1}",
                              "boost":"10"
                           }
                        ]
                     }
                  ]
               },
               "languageCode":"en-US"
            },
            "audio":{
               "uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"
            }
         }




### Refer to a `CustomClass` in a `PhraseSet`

  1. Update the `PhraseSet` resource created earlier to refer to the `CustomClass`:
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/projects/project_id/locations/global/phraseSets/test-phrase-set-1?updateMask=phrases"
         -d '{"phrases": [{"value": "${projects/project_id/locations/global/customClasses/test-custom-class-1}", "boost": 10}]}'

Example request:
         
         {
            "config":{
               "adaptation":{
                  "phraseSets":[
                     {
                        "phrases":[
                           {
                              "value":"${projects/project_id/locations/global/customClasses/test-custom-class-1}",
                              "boost":"10"
                           }
                        ]
                     }
                  ]
               },
               "languageCode":"en-US"
            },
            "audio":{
               "uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"
            }
         }

  2. Recognize the audio using the `PhraseSet` resource (which refers to the `CustomClass`). The transcript is correct: "call me fionity and oh my gosh what do we have here ionity".
         
         curl -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/speech:recognize" -d '{"config":
         {"adaptation": {"phrase_set_references":
         ["projects/project_id/locations/global/phraseSets/test-phrase-set-1"]},
         "languageCode": "en-US"}, "audio":
         {"uri":"gs://biasing-resources-test-audio/call_me_fionity_and_ionity.wav"}}'

Example request:
         
         {
            "phrases":[
               {
                  "value":"${projects/project_id/locations/global/customClasses/test-custom-class-1}",
                  "boost":10
               }
            ]
         }




### Delete the `CustomClass` and `PhraseSet`

  1. Delete the `PhraseSet`:
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/projects/project_id/locations/global/phraseSets/test-phrase-set-1"

  2. Delete the `CustomClass`:
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth
         --impersonate-service-account=$SA_EMAIL print-access-token)" -H
         "Content-Type: application/json; charset=utf-8"
         "https://speech.googleapis.com/v1p1beta1/projects/project_id/locations/global/customClasses/test-custom-class-1"




### Improve transcription results using an `ABNF Grammar`

  1. Recognize the audio using the an `abnf_grammar`. This example refers to a `CustomClass` resource: projects/project_id/locations/global/customClasses/test-custom-class-1, an inlined `CustomClass`: test-custom-class-2, class token: ADDRESSNUM, and a `PhraseSet` resource: projects/project_id/locations/global/phraseSets/test-phrase-set-1. The first rule in the strings (after external declarations) will be treated as the root.

Example request:
         
         {
            "config":{
               "adaptation":{
                  "abnf_grammar":{
                     "abnf_strings": [
                       "external ${projects/project_id/locations/global/phraseSets/test-phrase-set-1}" ,
                       "external ${projects/project_id/locations/global/customClasses/test-custom-class-1}" ,
                       "external ${test-custom-class-2}" ,
                       "external $ADDRESSNUM" ,
                       "$root = $test-phrase-set-1 $name lives in $ADDRESSNUM;" ,
                       "$name = $title $test-custom-class-1 $test-custom-class-2" ,
                       "$title = Mr | Mrs | Miss | Dr | Prof ;"
                     ]
                  }
               }
            }
         }




## What's next

  * Learn how to [use model adaptation in a request to Cloud STT](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation).
  * Review the [list of supported class tokens](https://docs.cloud.google.com/speech-to-text/docs/v1/class-tokens).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
