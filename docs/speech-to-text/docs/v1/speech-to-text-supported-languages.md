---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages/
title: Cloud Speech-to-Text V1 supported languages \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:26.489087+00:00
---

# Cloud Speech-to-Text V1 supported languages  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Cloud Speech-to-Text V1 supported languages Stay organized with collections  Save and categorize content based on your preferences. 

This page lists all languages supported by Cloud Speech-to-Text. Language is specified within a recognition request's [`languageCode`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig) parameter. For more information about sending a recognition request and specifying the language of the transcription, see the [how-to guides](https://docs.cloud.google.com/speech-to-text/docs/v1/how-to) about performing speech recognition. For more information about the [class tokens](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation-model#classes) available for each language, see the [class tokens page](https://docs.cloud.google.com/speech-to-text/docs/v1/class-tokens).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud STT performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud STT free ](https://console.cloud.google.com/freetrial)

The table below lists the models available for each language. Cloud Speech-to-Text offers multiple [recognition models](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-requests#select-model), each tuned to different audio types. The `default` and `command_and_search` recognition models support all available languages. The `command_and_search` model is optimized for short audio clips, such as voice commands or voice searches. The `default` model can be used to transcribe any audio type.

Some languages are supported by additional models, optimized for additional audio types: `enhanced` `phone_call`, and `enhanced` `video`. These models can recognize speech captured from these audio sources more accurately than the `default` model. See the [enhanced models](https://docs.cloud.google.com/speech-to-text/docs/v1/enhanced-models) page for more information. If any of these additional models are available for your language, they will be listed with the `default` and `command_and_search` models for your language. If only the `default` and `command_and_search` models are listed with your language, no additional models are currently available.

Use only the language codes shown in the following table. The following language codes are officially maintained and monitored externally by Google. Using other language codes can result in breaking changes.

Filter by supported feature: 

All

[Single utterance](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#google.cloud.speech.v1.StreamingRecognitionConfig.FIELDS.bool.google.cloud.speech.v1.StreamingRecognitionConfig.single_utterance)

[Automatic punctuation](https://docs.cloud.google.com/speech-to-text/docs/v1/automatic-punctuation)

[Speaker diarization](https://docs.cloud.google.com/speech-to-text/docs/v1/multiple-voices) (Preview)

[Model adaptation](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation-model) (Preview)

[Word-level confidence](https://docs.cloud.google.com/speech-to-text/docs/v1/word-confidence) (Preview)

[Profanity filter](https://docs.cloud.google.com/speech-to-text/docs/v1/profanity-filter)

[Spoken punctuation](https://docs.cloud.google.com/speech-to-text/docs/v1/spoken-punctuation-emojis)

[Spoken emoji](https://docs.cloud.google.com/speech-to-text/docs/v1/spoken-punctuation-emojis)

Filter by language: 

Name | BCP-47 | Model | Single utterance | Automatic punctuation | Diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
---|---|---|---|---|---|---|---|---|---|---  
Afrikaans (South Africa) | af-ZA | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Afrikaans (South Africa) | af-ZA | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Afrikaans (South Africa) | af-ZA | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Albanian (Albania) | sq-AL | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Albanian (Albania) | sq-AL | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Albanian (Albania) | sq-AL | `default` | False |  |  |  |  | Profanity filter |  |   
Amharic (Ethiopia) | am-ET | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Amharic (Ethiopia) | am-ET | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Amharic (Ethiopia) | am-ET | `default` | False |  |  |  |  | Profanity filter |  |   
Arabic (Algeria) | ar-DZ | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Arabic (Algeria) | ar-DZ | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Arabic (Algeria) | ar-DZ | `default` | False |  |  |  |  | Profanity filter |  |   
Arabic (Algeria) | ar-DZ | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Algeria) | ar-DZ | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Algeria) | ar-DZ | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Algeria) | ar-DZ | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Bahrain) | ar-BH | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Bahrain) | ar-BH | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Bahrain) | ar-BH | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Bahrain) | ar-BH | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Bahrain) | ar-BH | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Bahrain) | ar-BH | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Bahrain) | ar-BH | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Egypt) | ar-EG | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Egypt) | ar-EG | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Egypt) | ar-EG | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Egypt) | ar-EG | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Egypt) | ar-EG | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Egypt) | ar-EG | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Egypt) | ar-EG | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Iraq) | ar-IQ | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Iraq) | ar-IQ | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Iraq) | ar-IQ | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Iraq) | ar-IQ | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Iraq) | ar-IQ | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Iraq) | ar-IQ | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Iraq) | ar-IQ | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Israel) | ar-IL | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Israel) | ar-IL | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Israel) | ar-IL | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Israel) | ar-IL | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Israel) | ar-IL | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Israel) | ar-IL | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Israel) | ar-IL | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Jordan) | ar-JO | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Jordan) | ar-JO | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Jordan) | ar-JO | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Jordan) | ar-JO | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Jordan) | ar-JO | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Jordan) | ar-JO | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Jordan) | ar-JO | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Kuwait) | ar-KW | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Kuwait) | ar-KW | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Kuwait) | ar-KW | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Kuwait) | ar-KW | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Kuwait) | ar-KW | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Kuwait) | ar-KW | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Kuwait) | ar-KW | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Lebanon) | ar-LB | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Lebanon) | ar-LB | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Lebanon) | ar-LB | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Lebanon) | ar-LB | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Lebanon) | ar-LB | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Lebanon) | ar-LB | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Lebanon) | ar-LB | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Mauritania) | ar-MR | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Arabic (Mauritania) | ar-MR | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Arabic (Mauritania) | ar-MR | `default` | False |  |  |  |  | Profanity filter |  |   
Arabic (Mauritania) | ar-MR | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Mauritania) | ar-MR | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Mauritania) | ar-MR | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Mauritania) | ar-MR | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Morocco) | ar-MA | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Arabic (Morocco) | ar-MA | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Arabic (Morocco) | ar-MA | `default` | False |  |  |  |  | Profanity filter |  |   
Arabic (Morocco) | ar-MA | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Morocco) | ar-MA | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Morocco) | ar-MA | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Morocco) | ar-MA | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Oman) | ar-OM | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Oman) | ar-OM | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Oman) | ar-OM | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Oman) | ar-OM | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Oman) | ar-OM | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Oman) | ar-OM | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Oman) | ar-OM | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Qatar) | ar-QA | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Qatar) | ar-QA | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Qatar) | ar-QA | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Qatar) | ar-QA | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Qatar) | ar-QA | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Qatar) | ar-QA | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Qatar) | ar-QA | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Saudi Arabia) | ar-SA | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Saudi Arabia) | ar-SA | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Saudi Arabia) | ar-SA | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Saudi Arabia) | ar-SA | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Saudi Arabia) | ar-SA | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Saudi Arabia) | ar-SA | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Saudi Arabia) | ar-SA | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (State of Palestine) | ar-PS | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (State of Palestine) | ar-PS | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (State of Palestine) | ar-PS | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (State of Palestine) | ar-PS | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (State of Palestine) | ar-PS | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (State of Palestine) | ar-PS | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (State of Palestine) | ar-PS | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Syria) | ar-SY | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Syria) | ar-SY | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Syria) | ar-SY | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Tunisia) | ar-TN | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Arabic (Tunisia) | ar-TN | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Arabic (Tunisia) | ar-TN | `default` | False |  |  |  |  | Profanity filter |  |   
Arabic (Tunisia) | ar-TN | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Tunisia) | ar-TN | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Tunisia) | ar-TN | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Tunisia) | ar-TN | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (United Arab Emirates) | ar-AE | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (United Arab Emirates) | ar-AE | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (United Arab Emirates) | ar-AE | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (United Arab Emirates) | ar-AE | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (United Arab Emirates) | ar-AE | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (United Arab Emirates) | ar-AE | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (United Arab Emirates) | ar-AE | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Yemen) | ar-YE | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Yemen) | ar-YE | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Yemen) | ar-YE | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Arabic (Yemen) | ar-YE | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Arabic (Yemen) | ar-YE | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Yemen) | ar-YE | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Arabic (Yemen) | ar-YE | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Armenian (Armenia) | hy-AM | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Armenian (Armenia) | hy-AM | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Armenian (Armenia) | hy-AM | `default` | False |  |  |  |  | Profanity filter |  |   
Azerbaijani (Azerbaijan) | az-AZ | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Azerbaijani (Azerbaijan) | az-AZ | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Azerbaijani (Azerbaijan) | az-AZ | `default` | False |  |  |  |  | Profanity filter |  |   
Basque (Spain) | eu-ES | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Basque (Spain) | eu-ES | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Basque (Spain) | eu-ES | `default` | False |  |  |  |  | Profanity filter |  |   
Bengali (Bangladesh) | bn-BD | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Bengali (Bangladesh) | bn-BD | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Bengali (Bangladesh) | bn-BD | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Bengali (Bangladesh) | bn-BD | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Bengali (Bangladesh) | bn-BD | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Bengali (Bangladesh) | bn-BD | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Bengali (Bangladesh) | bn-BD | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Bengali (India) | bn-IN | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Bengali (India) | bn-IN | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Bengali (India) | bn-IN | `default` | False |  |  |  |  | Profanity filter |  |   
Bosnian (Bosnia and Herzegovina) | bs-BA | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Bosnian (Bosnia and Herzegovina) | bs-BA | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Bosnian (Bosnia and Herzegovina) | bs-BA | `default` | False |  |  |  |  | Profanity filter |  |   
Bulgarian (Bulgaria) | bg-BG | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Bulgarian (Bulgaria) | bg-BG | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Bulgarian (Bulgaria) | bg-BG | `default` | False |  |  |  |  | Profanity filter |  |   
Bulgarian (Bulgaria) | bg-BG | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Bulgarian (Bulgaria) | bg-BG | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Bulgarian (Bulgaria) | bg-BG | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Bulgarian (Bulgaria) | bg-BG | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Burmese (Myanmar) | my-MM | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Burmese (Myanmar) | my-MM | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Burmese (Myanmar) | my-MM | `default` | False |  |  |  |  | Profanity filter |  |   
Catalan (Spain) | ca-ES | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Catalan (Spain) | ca-ES | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Catalan (Spain) | ca-ES | `default` | False |  |  |  |  | Profanity filter |  |   
Chinese (Simplified, China) | cmn-Hans-CN | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Chinese (Simplified, China) | cmn-Hans-CN | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Chinese (Simplified, China) | cmn-Hans-CN | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Chinese (Simplified, Hong Kong) | cmn-Hans-HK | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Chinese (Simplified, Hong Kong) | cmn-Hans-HK | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Chinese (Simplified, Hong Kong) | cmn-Hans-HK | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Chinese, Cantonese (Traditional Hong Kong) | yue-Hant-HK | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Chinese, Cantonese (Traditional Hong Kong) | yue-Hant-HK | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Chinese, Cantonese (Traditional Hong Kong) | yue-Hant-HK | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Chinese, Mandarin (Traditional, Taiwan) | cmn-Hant-TW | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Chinese, Mandarin (Traditional, Taiwan) | cmn-Hant-TW | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Chinese, Mandarin (Traditional, Taiwan) | cmn-Hant-TW | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Croatian (Croatia) | hr-HR | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Croatian (Croatia) | hr-HR | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Croatian (Croatia) | hr-HR | `default` | False |  |  |  |  | Profanity filter |  |   
Czech (Czech Republic) | cs-CZ | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Czech (Czech Republic) | cs-CZ | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Czech (Czech Republic) | cs-CZ | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Czech (Czech Republic) | cs-CZ | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Czech (Czech Republic) | cs-CZ | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Czech (Czech Republic) | cs-CZ | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Czech (Czech Republic) | cs-CZ | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Danish (Denmark) | da-DK | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Danish (Denmark) | da-DK | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Danish (Denmark) | da-DK | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Danish (Denmark) | da-DK | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Danish (Denmark) | da-DK | `latest_long` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Danish (Denmark) | da-DK | `latest_short` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Danish (Denmark) | da-DK | `latest_short` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Belgium) | nl-BE | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Dutch (Belgium) | nl-BE | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Dutch (Belgium) | nl-BE | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Dutch (Belgium) | nl-BE | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Belgium) | nl-BE | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Belgium) | nl-BE | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Belgium) | nl-BE | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Dutch (Netherlands) | nl-NL | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
English (Australia) | en-AU | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `phone_call` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
English (Australia) | en-AU | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Australia) | en-AU | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Canada) | en-CA | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Canada) | en-CA | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Canada) | en-CA | `default` | False |  |  |  |  | Profanity filter |  |   
English (Canada) | en-CA | `telephony` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Canada) | en-CA | `telephony` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Canada) | en-CA | `telephony_short` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Canada) | en-CA | `telephony_short` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Ghana) | en-GH | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Ghana) | en-GH | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Ghana) | en-GH | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Hong Kong) | en-HK | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Hong Kong) | en-HK | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Hong Kong) | en-HK | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Hong Kong) | en-HK | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Hong Kong) | en-HK | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Hong Kong) | en-HK | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Hong Kong) | en-HK | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (India) | en-IN | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Ireland) | en-IE | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Ireland) | en-IE | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Ireland) | en-IE | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Ireland) | en-IE | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Ireland) | en-IE | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Ireland) | en-IE | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Ireland) | en-IE | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Kenya) | en-KE | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Kenya) | en-KE | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Kenya) | en-KE | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (New Zealand) | en-NZ | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (New Zealand) | en-NZ | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (New Zealand) | en-NZ | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (New Zealand) | en-NZ | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (New Zealand) | en-NZ | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (New Zealand) | en-NZ | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (New Zealand) | en-NZ | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Nigeria) | en-NG | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Nigeria) | en-NG | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Nigeria) | en-NG | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Pakistan) | en-PK | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Pakistan) | en-PK | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Pakistan) | en-PK | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (Pakistan) | en-PK | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Pakistan) | en-PK | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Pakistan) | en-PK | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Pakistan) | en-PK | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Philippines) | en-PH | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  | Spoken emoji  
English (Philippines) | en-PH | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  | Spoken emoji  
English (Philippines) | en-PH | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
English (Singapore) | en-SG | `command_and_search` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Singapore) | en-SG | `command_and_search` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Singapore) | en-SG | `default` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
English (Singapore) | en-SG | `telephony` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Singapore) | en-SG | `telephony` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Singapore) | en-SG | `telephony_short` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (Singapore) | en-SG | `telephony_short` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (South Africa) | en-ZA | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (South Africa) | en-ZA | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (South Africa) | en-ZA | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Tanzania) | en-TZ | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Tanzania) | en-TZ | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (Tanzania) | en-TZ | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
English (United Kingdom) | en-GB | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `phone_call` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United Kingdom) | en-GB | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `command_and_search` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `command_and_search` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `default` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter |  |   
English (United States) | en-US | `latest_long` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `latest_long` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `latest_short` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter |  | Spoken emoji  
English (United States) | en-US | `latest_short` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter |  | Spoken emoji  
English (United States) | en-US | `medical_conversation` | False | Automatic punctuation | Speaker diarization |  | Word-level confidence |  |  |   
English (United States) | en-US | `medical_dictation` | False | Automatic punctuation |  |  | Word-level confidence |  | Spoken punctuation |   
English (United States) | en-US | `phone_call` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter |  |   
English (United States) | en-US | `telephony` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `telephony` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `telephony_short` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `telephony_short` | True | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
English (United States) | en-US | `video` | False | Automatic punctuation | Speaker diarization | Model adaptation | Word-level confidence | Profanity filter |  |   
Estonian (Estonia) | et-EE | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Estonian (Estonia) | et-EE | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Estonian (Estonia) | et-EE | `default` | False |  |  |  |  | Profanity filter |  |   
Filipino (Philippines) | fil-PH | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Filipino (Philippines) | fil-PH | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Filipino (Philippines) | fil-PH | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Finnish (Finland) | fi-FI | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Finnish (Finland) | fi-FI | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Finnish (Finland) | fi-FI | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter |  |   
Finnish (Finland) | fi-FI | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Finnish (Finland) | fi-FI | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Finnish (Finland) | fi-FI | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Finnish (Finland) | fi-FI | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
French (Belgium) | fr-BE | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Belgium) | fr-BE | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Belgium) | fr-BE | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Belgium) | fr-BE | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (Belgium) | fr-BE | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (Belgium) | fr-BE | `telephony_short` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Belgium) | fr-BE | `telephony_short` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Canada) | fr-CA | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
French (Canada) | fr-CA | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
French (Canada) | fr-CA | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
French (Canada) | fr-CA | `latest_long` | False |  |  | Model adaptation | Word-level confidence |  | Spoken punctuation |   
French (Canada) | fr-CA | `latest_long` | True |  |  | Model adaptation | Word-level confidence |  | Spoken punctuation |   
French (Canada) | fr-CA | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
French (Canada) | fr-CA | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
French (Canada) | fr-CA | `phone_call` | False |  |  |  | Word-level confidence | Profanity filter |  |   
French (Canada) | fr-CA | `telephony` | False |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
French (Canada) | fr-CA | `telephony` | True |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
French (Canada) | fr-CA | `telephony_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
French (Canada) | fr-CA | `telephony_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
French (France) | fr-FR | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `phone_call` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `telephony_short` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (France) | fr-FR | `telephony_short` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Switzerland) | fr-CH | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Switzerland) | fr-CH | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Switzerland) | fr-CH | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Switzerland) | fr-CH | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (Switzerland) | fr-CH | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation | Spoken emoji  
French (Switzerland) | fr-CH | `telephony_short` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
French (Switzerland) | fr-CH | `telephony_short` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation | Spoken emoji  
Galician (Spain) | gl-ES | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Galician (Spain) | gl-ES | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Galician (Spain) | gl-ES | `default` | False |  |  |  |  | Profanity filter |  |   
Georgian (Georgia) | ka-GE | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Georgian (Georgia) | ka-GE | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Georgian (Georgia) | ka-GE | `default` | False |  |  |  |  | Profanity filter |  |   
German (Austria) | de-AT | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
German (Austria) | de-AT | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
German (Austria) | de-AT | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
German (Austria) | de-AT | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Austria) | de-AT | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Austria) | de-AT | `telephony_short` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
German (Austria) | de-AT | `telephony_short` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `phone_call` | False | Automatic punctuation |  |  |  | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `telephony_short` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
German (Germany) | de-DE | `telephony_short` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
German (Switzerland) | de-CH | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
German (Switzerland) | de-CH | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
German (Switzerland) | de-CH | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
German (Switzerland) | de-CH | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Switzerland) | de-CH | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
German (Switzerland) | de-CH | `telephony_short` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
German (Switzerland) | de-CH | `telephony_short` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Greek (Greece) | el-GR | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Greek (Greece) | el-GR | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Greek (Greece) | el-GR | `default` | False |  |  |  |  | Profanity filter |  |   
Gujarati (India) | gu-IN | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Gujarati (India) | gu-IN | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Gujarati (India) | gu-IN | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Hebrew (Israel) | iw-IL | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Hebrew (Israel) | iw-IL | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Hebrew (Israel) | iw-IL | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `latest_long` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Hindi (India) | hi-IN | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Hungarian (Hungary) | hu-HU | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Hungarian (Hungary) | hu-HU | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Hungarian (Hungary) | hu-HU | `default` | False |  |  |  |  | Profanity filter |  |   
Hungarian (Hungary) | hu-HU | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Hungarian (Hungary) | hu-HU | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Hungarian (Hungary) | hu-HU | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Hungarian (Hungary) | hu-HU | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Icelandic (Iceland) | is-IS | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Icelandic (Iceland) | is-IS | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Icelandic (Iceland) | is-IS | `default` | False |  |  |  |  | Profanity filter |  |   
Indonesian (Indonesia) | id-ID | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Indonesian (Indonesia) | id-ID | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Indonesian (Indonesia) | id-ID | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Indonesian (Indonesia) | id-ID | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Indonesian (Indonesia) | id-ID | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Indonesian (Indonesia) | id-ID | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Indonesian (Indonesia) | id-ID | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `phone_call` | False | Automatic punctuation |  |  |  | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Italy) | it-IT | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Switzerland) | it-CH | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Italian (Switzerland) | it-CH | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Italian (Switzerland) | it-CH | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Italian (Switzerland) | it-CH | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Switzerland) | it-CH | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Switzerland) | it-CH | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Italian (Switzerland) | it-CH | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `phone_call` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Japanese (Japan) | ja-JP | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Javanese (Indonesia) | jv-ID | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Javanese (Indonesia) | jv-ID | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Javanese (Indonesia) | jv-ID | `default` | False |  |  |  |  | Profanity filter |  |   
Kannada (India) | kn-IN | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Kannada (India) | kn-IN | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Kannada (India) | kn-IN | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Kannada (India) | kn-IN | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Kannada (India) | kn-IN | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Kannada (India) | kn-IN | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Kannada (India) | kn-IN | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Kazakh (Kazakhstan) | kk-KZ | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Kazakh (Kazakhstan) | kk-KZ | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Kazakh (Kazakhstan) | kk-KZ | `default` | False |  |  |  |  | Profanity filter |  |   
Khmer (Cambodia) | km-KH | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Khmer (Cambodia) | km-KH | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Khmer (Cambodia) | km-KH | `default` | False |  |  |  |  | Profanity filter |  |   
Khmer (Cambodia) | km-KH | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Khmer (Cambodia) | km-KH | `latest_long` | True |  |  |  | Word-level confidence | Profanity filter |  |   
Khmer (Cambodia) | km-KH | `latest_short` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Khmer (Cambodia) | km-KH | `latest_short` | True |  |  |  | Word-level confidence | Profanity filter |  |   
Kinyarwanda (Rwanda) | rw-RW | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Kinyarwanda (Rwanda) | rw-RW | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Kinyarwanda (Rwanda) | rw-RW | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Kinyarwanda (Rwanda) | rw-RW | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Korean (South Korea) | ko-KR | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `telephony_short` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Korean (South Korea) | ko-KR | `telephony_short` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Lao (Laos) | lo-LA | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Lao (Laos) | lo-LA | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Lao (Laos) | lo-LA | `default` | False |  |  |  |  | Profanity filter |  |   
Latvian (Latvia) | lv-LV | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Latvian (Latvia) | lv-LV | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Latvian (Latvia) | lv-LV | `default` | False |  |  |  |  | Profanity filter |  |   
Lithuanian (Lithuania) | lt-LT | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Lithuanian (Lithuania) | lt-LT | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Lithuanian (Lithuania) | lt-LT | `default` | False |  |  |  |  | Profanity filter |  |   
Macedonian (North Macedonia) | mk-MK | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Macedonian (North Macedonia) | mk-MK | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Macedonian (North Macedonia) | mk-MK | `default` | False |  |  |  |  | Profanity filter |  |   
Macedonian (North Macedonia) | mk-MK | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Macedonian (North Macedonia) | mk-MK | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Macedonian (North Macedonia) | mk-MK | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Macedonian (North Macedonia) | mk-MK | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Malay (Malaysia) | ms-MY | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Malay (Malaysia) | ms-MY | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Malay (Malaysia) | ms-MY | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Malayalam (India) | ml-IN | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Malayalam (India) | ml-IN | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Malayalam (India) | ml-IN | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Malayalam (India) | ml-IN | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Malayalam (India) | ml-IN | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Malayalam (India) | ml-IN | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Malayalam (India) | ml-IN | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Marathi (India) | mr-IN | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Marathi (India) | mr-IN | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Marathi (India) | mr-IN | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Marathi (India) | mr-IN | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Marathi (India) | mr-IN | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Marathi (India) | mr-IN | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Marathi (India) | mr-IN | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Mongolian (Mongolia) | mn-MN | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Mongolian (Mongolia) | mn-MN | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Mongolian (Mongolia) | mn-MN | `default` | False |  |  |  |  | Profanity filter |  |   
Nepali (Nepal) | ne-NP | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Nepali (Nepal) | ne-NP | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Nepali (Nepal) | ne-NP | `default` | False |  |  |  |  | Profanity filter |  |   
Norwegian Bokmål (Norway) | no-NO | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Norwegian Bokmål (Norway) | no-NO | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Norwegian Bokmål (Norway) | no-NO | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Norwegian Bokmål (Norway) | no-NO | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Norwegian Bokmål (Norway) | no-NO | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Norwegian Bokmål (Norway) | no-NO | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Norwegian Bokmål (Norway) | no-NO | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Persian (Iran) | fa-IR | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Persian (Iran) | fa-IR | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Persian (Iran) | fa-IR | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Polish (Poland) | pl-PL | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Polish (Poland) | pl-PL | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Polish (Poland) | pl-PL | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Polish (Poland) | pl-PL | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Polish (Poland) | pl-PL | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Polish (Poland) | pl-PL | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Polish (Poland) | pl-PL | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `phone_call` | False | Automatic punctuation |  |  |  | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Brazil) | pt-BR | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `telephony` | False |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `telephony` | True |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `telephony_short` | False |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Portuguese (Portugal) | pt-PT | `telephony_short` | True |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Punjabi (Gurmukhi India) | pa-Guru-IN | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Punjabi (Gurmukhi India) | pa-Guru-IN | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Punjabi (Gurmukhi India) | pa-Guru-IN | `default` | False |  |  |  |  | Profanity filter |  |   
Romanian (Romania) | ro-RO | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Romanian (Romania) | ro-RO | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Romanian (Romania) | ro-RO | `default` | False |  |  |  |  | Profanity filter |  |   
Romanian (Romania) | ro-RO | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Romanian (Romania) | ro-RO | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Romanian (Romania) | ro-RO | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Romanian (Romania) | ro-RO | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Russian (Russia) | ru-RU | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Russian (Russia) | ru-RU | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Russian (Russia) | ru-RU | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Russian (Russia) | ru-RU | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Russian (Russia) | ru-RU | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Russian (Russia) | ru-RU | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Russian (Russia) | ru-RU | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Russian (Russia) | ru-RU | `phone_call` | False | Automatic punctuation |  |  |  | Profanity filter | Spoken punctuation |   
Serbian (Serbia) | sr-RS | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Serbian (Serbia) | sr-RS | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Serbian (Serbia) | sr-RS | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Sinhala (Sri Lanka) | si-LK | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Sinhala (Sri Lanka) | si-LK | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Sinhala (Sri Lanka) | si-LK | `default` | False |  |  |  |  | Profanity filter |  |   
Slovak (Slovakia) | sk-SK | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Slovak (Slovakia) | sk-SK | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Slovak (Slovakia) | sk-SK | `default` | False |  |  |  |  | Profanity filter |  |   
Slovenian (Slovenia) | sl-SI | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Slovenian (Slovenia) | sl-SI | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Slovenian (Slovenia) | sl-SI | `default` | False |  |  |  |  | Profanity filter |  |   
Southern Sotho (South Africa) | st-ZA | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Southern Sotho (South Africa) | st-ZA | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Southern Sotho (South Africa) | st-ZA | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Southern Sotho (South Africa) | st-ZA | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Spanish (Argentina) | es-AR | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Argentina) | es-AR | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Argentina) | es-AR | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Argentina) | es-AR | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Argentina) | es-AR | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Argentina) | es-AR | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Argentina) | es-AR | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Bolivia) | es-BO | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Bolivia) | es-BO | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Bolivia) | es-BO | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Bolivia) | es-BO | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Bolivia) | es-BO | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Bolivia) | es-BO | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Bolivia) | es-BO | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Chile) | es-CL | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Chile) | es-CL | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Chile) | es-CL | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Chile) | es-CL | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Chile) | es-CL | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Chile) | es-CL | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Chile) | es-CL | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Colombia) | es-CO | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Colombia) | es-CO | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Colombia) | es-CO | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Colombia) | es-CO | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Colombia) | es-CO | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Colombia) | es-CO | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Colombia) | es-CO | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Costa Rica) | es-CR | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Costa Rica) | es-CR | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Costa Rica) | es-CR | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Costa Rica) | es-CR | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Costa Rica) | es-CR | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Costa Rica) | es-CR | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Costa Rica) | es-CR | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Dominican Republic) | es-DO | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Dominican Republic) | es-DO | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Dominican Republic) | es-DO | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Dominican Republic) | es-DO | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Dominican Republic) | es-DO | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Dominican Republic) | es-DO | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Dominican Republic) | es-DO | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Ecuador) | es-EC | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Ecuador) | es-EC | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Ecuador) | es-EC | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Ecuador) | es-EC | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Ecuador) | es-EC | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Ecuador) | es-EC | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Ecuador) | es-EC | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (El Salvador) | es-SV | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (El Salvador) | es-SV | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (El Salvador) | es-SV | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (El Salvador) | es-SV | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (El Salvador) | es-SV | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (El Salvador) | es-SV | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (El Salvador) | es-SV | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Guatemala) | es-GT | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Guatemala) | es-GT | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Guatemala) | es-GT | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Guatemala) | es-GT | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Guatemala) | es-GT | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Guatemala) | es-GT | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Guatemala) | es-GT | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Honduras) | es-HN | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Honduras) | es-HN | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Honduras) | es-HN | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Honduras) | es-HN | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Honduras) | es-HN | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Honduras) | es-HN | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Honduras) | es-HN | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Mexico) | es-MX | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Mexico) | es-MX | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Mexico) | es-MX | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Mexico) | es-MX | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Mexico) | es-MX | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Mexico) | es-MX | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Mexico) | es-MX | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Nicaragua) | es-NI | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Nicaragua) | es-NI | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Nicaragua) | es-NI | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Nicaragua) | es-NI | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Nicaragua) | es-NI | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Nicaragua) | es-NI | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Nicaragua) | es-NI | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Panama) | es-PA | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Panama) | es-PA | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Panama) | es-PA | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Panama) | es-PA | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Panama) | es-PA | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Panama) | es-PA | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Panama) | es-PA | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Paraguay) | es-PY | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Paraguay) | es-PY | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Paraguay) | es-PY | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Peru) | es-PE | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Peru) | es-PE | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Peru) | es-PE | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Peru) | es-PE | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Peru) | es-PE | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Peru) | es-PE | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Peru) | es-PE | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Puerto Rico) | es-PR | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Puerto Rico) | es-PR | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Puerto Rico) | es-PR | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Puerto Rico) | es-PR | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Puerto Rico) | es-PR | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Puerto Rico) | es-PR | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Puerto Rico) | es-PR | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `default` | False |  |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `phone_call` | False |  |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Spain) | es-ES | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `latest_long` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `phone_call` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (United States) | es-US | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Uruguay) | es-UY | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Uruguay) | es-UY | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Uruguay) | es-UY | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Uruguay) | es-UY | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Uruguay) | es-UY | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Uruguay) | es-UY | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Uruguay) | es-UY | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Venezuela) | es-VE | `command_and_search` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Venezuela) | es-VE | `command_and_search` | True |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Venezuela) | es-VE | `default` | False |  |  |  |  | Profanity filter | Spoken punctuation |   
Spanish (Venezuela) | es-VE | `telephony` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Venezuela) | es-VE | `telephony` | True | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Venezuela) | es-VE | `telephony_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Spanish (Venezuela) | es-VE | `telephony_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Sundanese (Indonesia) | su-ID | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Sundanese (Indonesia) | su-ID | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Sundanese (Indonesia) | su-ID | `default` | False |  |  |  |  | Profanity filter |  |   
Swahili (Kenya) | sw-KE | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Swahili (Kenya) | sw-KE | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Swahili (Kenya) | sw-KE | `default` | False |  |  |  |  | Profanity filter |  |   
Swahili (Tanzania) | sw-TZ | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Swahili (Tanzania) | sw-TZ | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Swahili (Tanzania) | sw-TZ | `default` | False |  |  |  |  | Profanity filter |  |   
Swati (Latin, South Africa) | ss-Latn-ZA | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Swati (Latin, South Africa) | ss-Latn-ZA | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Swati (Latin, South Africa) | ss-Latn-ZA | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Swati (Latin, South Africa) | ss-Latn-ZA | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Swedish (Sweden) | sv-SE | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Swedish (Sweden) | sv-SE | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Swedish (Sweden) | sv-SE | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Swedish (Sweden) | sv-SE | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Swedish (Sweden) | sv-SE | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Swedish (Sweden) | sv-SE | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Swedish (Sweden) | sv-SE | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Tamil (India) | ta-IN | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Tamil (India) | ta-IN | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Tamil (India) | ta-IN | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Tamil (India) | ta-IN | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Tamil (India) | ta-IN | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Tamil (India) | ta-IN | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Tamil (India) | ta-IN | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Tamil (Malaysia) | ta-MY | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Tamil (Malaysia) | ta-MY | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Tamil (Malaysia) | ta-MY | `default` | False |  |  |  |  | Profanity filter |  |   
Tamil (Singapore) | ta-SG | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Tamil (Singapore) | ta-SG | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Tamil (Singapore) | ta-SG | `default` | False |  |  |  |  | Profanity filter |  |   
Tamil (Sri Lanka) | ta-LK | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Tamil (Sri Lanka) | ta-LK | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Tamil (Sri Lanka) | ta-LK | `default` | False |  |  |  |  | Profanity filter |  |   
Telugu (India) | te-IN | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Telugu (India) | te-IN | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Telugu (India) | te-IN | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Telugu (India) | te-IN | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Telugu (India) | te-IN | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Telugu (India) | te-IN | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Telugu (India) | te-IN | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Thai (Thailand) | th-TH | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Thai (Thailand) | th-TH | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Thai (Thailand) | th-TH | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Thai (Thailand) | th-TH | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Thai (Thailand) | th-TH | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Thai (Thailand) | th-TH | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Thai (Thailand) | th-TH | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Tsonga (South Africa) | ts-ZA | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Tsonga (South Africa) | ts-ZA | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Tsonga (South Africa) | ts-ZA | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Tsonga (South Africa) | ts-ZA | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Tswana (Latin, South Africa) | tn-Latn-ZA | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Tswana (Latin, South Africa) | tn-Latn-ZA | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Tswana (Latin, South Africa) | tn-Latn-ZA | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Tswana (Latin, South Africa) | tn-Latn-ZA | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Turkish (Turkey) | tr-TR | `command_and_search` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Turkish (Turkey) | tr-TR | `command_and_search` | True | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Turkish (Turkey) | tr-TR | `default` | False | Automatic punctuation |  | Model adaptation |  | Profanity filter | Spoken punctuation |   
Turkish (Turkey) | tr-TR | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter | Spoken punctuation |   
Turkish (Turkey) | tr-TR | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Turkish (Turkey) | tr-TR | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Turkish (Turkey) | tr-TR | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter | Spoken punctuation |   
Ukrainian (Ukraine) | uk-UA | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Ukrainian (Ukraine) | uk-UA | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Ukrainian (Ukraine) | uk-UA | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Ukrainian (Ukraine) | uk-UA | `latest_long` | False |  |  |  | Word-level confidence | Profanity filter |  |   
Ukrainian (Ukraine) | uk-UA | `latest_long` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Ukrainian (Ukraine) | uk-UA | `latest_short` | False |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Ukrainian (Ukraine) | uk-UA | `latest_short` | True |  |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Urdu (India) | ur-IN | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Urdu (India) | ur-IN | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Urdu (India) | ur-IN | `default` | False |  |  |  |  | Profanity filter |  |   
Urdu (Pakistan) | ur-PK | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Urdu (Pakistan) | ur-PK | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Urdu (Pakistan) | ur-PK | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Uzbek (Uzbekistan) | uz-UZ | `command_and_search` | False |  |  |  |  | Profanity filter |  |   
Uzbek (Uzbekistan) | uz-UZ | `command_and_search` | True |  |  |  |  | Profanity filter |  |   
Uzbek (Uzbekistan) | uz-UZ | `default` | False |  |  |  |  | Profanity filter |  |   
Venda (South Africa) | ve-ZA | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Venda (South Africa) | ve-ZA | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Venda (South Africa) | ve-ZA | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Venda (South Africa) | ve-ZA | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Vietnamese (Vietnam) | vi-VN | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Vietnamese (Vietnam) | vi-VN | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Vietnamese (Vietnam) | vi-VN | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
Vietnamese (Vietnam) | vi-VN | `latest_long` | False | Automatic punctuation |  |  | Word-level confidence | Profanity filter |  |   
Vietnamese (Vietnam) | vi-VN | `latest_long` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Vietnamese (Vietnam) | vi-VN | `latest_short` | False | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Vietnamese (Vietnam) | vi-VN | `latest_short` | True | Automatic punctuation |  | Model adaptation | Word-level confidence | Profanity filter |  |   
Xhosa (South Africa) | xh-ZA | `latest_long` | False |  |  |  |  | Profanity filter |  |   
Xhosa (South Africa) | xh-ZA | `latest_long` | True |  |  |  |  | Profanity filter |  |   
Xhosa (South Africa) | xh-ZA | `latest_short` | False |  |  |  |  | Profanity filter |  |   
Xhosa (South Africa) | xh-ZA | `latest_short` | True |  |  |  |  | Profanity filter |  |   
Zulu (South Africa) | zu-ZA | `command_and_search` | False |  |  | Model adaptation |  | Profanity filter |  |   
Zulu (South Africa) | zu-ZA | `command_and_search` | True |  |  | Model adaptation |  | Profanity filter |  |   
Zulu (South Africa) | zu-ZA | `default` | False |  |  | Model adaptation |  | Profanity filter |  |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
