---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig/
title: SynthesizeSpeechConfig \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:32.870054+00:00
---

# SynthesizeSpeechConfig  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  SynthesizeSpeechConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * VoiceSelectionParams
    * JSON representation
  * SsmlVoiceGender
  * CustomPronunciationParams
    * JSON representation
  * PhoneticEncoding



Configuration of how speech should be synthesized.

JSON representation  
---  
      
    
    {
      "speakingRate": number,
      "pitch": number,
      "volumeGainDb": number,
      "effectsProfileId": [
        string
      ],
      "voice": {
        object ([VoiceSelectionParams](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#VoiceSelectionParams))
      },
      "pronunciations": [
        {
          object ([CustomPronunciationParams](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#CustomPronunciationParams))
        }
      ]
    }  
  
Fields  
---  
`speakingRate` |  `number` Optional. Speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values < 0.25 or > 4.0 will return an error.  
`pitch` |  `number` Optional. Speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the original pitch. -20 means decrease 20 semitones from the original pitch.  
`volumeGainDb` |  `number` Optional. Volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. We strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.  
`effectsProfileId[]` |  `string` Optional. An identifier which selects 'audio effects' profiles that are applied on (post synthesized) text to speech. Effects are applied on top of each other in the order they are given.  
`voice` |  `object (`[VoiceSelectionParams](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#VoiceSelectionParams)`)` Optional. The desired voice of the synthesized audio.  
`pronunciations[]` |  `object (`[CustomPronunciationParams](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#CustomPronunciationParams)`)` Optional. The custom pronunciations for the synthesized audio.  
  
## VoiceSelectionParams

Description of which voice to use for speech synthesis.

JSON representation  
---  
      
    
    {
      "name": string,
      "ssmlGender": enum ([SsmlVoiceGender](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#SsmlVoiceGender))
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode and `[ssmlGender](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#VoiceSelectionParams.FIELDS.ssml_gender)`.For the list of available voices, please refer to [Supported voices and languages](https://cloud.google.com/text-to-speech/docs/voices).  
`ssmlGender` |  `enum (`[SsmlVoiceGender](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#SsmlVoiceGender)`)` Optional. The preferred gender of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode and `[name](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#VoiceSelectionParams.FIELDS.name)`. Note that this is only a preference, not requirement. If a voice of the appropriate gender is not available, the synthesizer should substitute a voice with a different gender rather than failing the request.  
  
## SsmlVoiceGender

Gender of the voice as described in [SSML voice element](https://www.w3.org/TR/speech-synthesis11/#edef_voice).

Enums  
---  
`SSML_VOICE_GENDER_UNSPECIFIED` | An unspecified gender, which means that the client doesn't care which gender the selected voice will have.  
`SSML_VOICE_GENDER_MALE` | A male voice.  
`SSML_VOICE_GENDER_FEMALE` | A female voice.  
`SSML_VOICE_GENDER_NEUTRAL` | A gender-neutral voice.  
  
## CustomPronunciationParams

Pronunciation customization for a phrase.

JSON representation  
---  
      
    
    {
      "phrase": string,
      "phoneticEncoding": enum ([PhoneticEncoding](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#PhoneticEncoding)),
      "pronunciation": string
    }  
  
Fields  
---  
`phrase` |  `string` The phrase to which the customization is applied. The phrase can be multiple words, such as proper nouns, but shouldn't span the length of the sentence.  
`phoneticEncoding` |  `enum (`[PhoneticEncoding](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SynthesizeSpeechConfig#PhoneticEncoding)`)` The phonetic encoding of the phrase.  
`pronunciation` |  `string` The pronunciation of the phrase. This must be in the phonetic encoding specified above.  
  
## PhoneticEncoding

The phonetic encoding of the phrase.

Enums  
---  
`PHONETIC_ENCODING_UNSPECIFIED` | Not specified.  
`PHONETIC_ENCODING_IPA` | IPA, such as apple -> ˈæpəl. <https://en.wikipedia.org/wiki/International_Phonetic_Alphabet>  
`PHONETIC_ENCODING_X_SAMPA` | X-SAMPA, such as apple -> "{[p@l"](mailto:p@l"). <https://en.wikipedia.org/wiki/X-SAMPA>  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
