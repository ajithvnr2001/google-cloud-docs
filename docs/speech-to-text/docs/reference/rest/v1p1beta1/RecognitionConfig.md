---
url: https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig/
title: RecognitionConfig \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:02.586156+00:00
---

# RecognitionConfig  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Reference ](https://docs.cloud.google.com/speech-to-text/docs/apis)



Send feedback 

#  RecognitionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AudioEncoding
  * SpeechAdaptation
    * JSON representation
  * ABNFGrammar
    * JSON representation
  * TranscriptNormalization
    * JSON representation
  * Entry
    * JSON representation
  * SpeechContext
    * JSON representation
  * SpeakerDiarizationConfig
    * JSON representation
  * RecognitionMetadata
    * JSON representation
  * InteractionType
  * MicrophoneDistance
  * OriginalMediaType
  * RecordingDeviceType



Provides information to the recognizer that specifies how to process the request.

JSON representation  
---  
      
    
    {
      "encoding": enum ([AudioEncoding](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#AudioEncoding)),
      "sampleRateHertz": integer,
      "audioChannelCount": integer,
      "enableSeparateRecognitionPerChannel": boolean,
      "languageCode": string,
      "alternativeLanguageCodes": [
        string
      ],
      "maxAlternatives": integer,
      "profanityFilter": boolean,
      "adaptation": {
        object ([SpeechAdaptation](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeechAdaptation))
      },
      "transcriptNormalization": {
        object ([TranscriptNormalization](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#TranscriptNormalization))
      },
      "speechContexts": [
        {
          object ([SpeechContext](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeechContext))
        }
      ],
      "enableWordTimeOffsets": boolean,
      "enableWordConfidence": boolean,
      "enableAutomaticPunctuation": boolean,
      "enableSpokenPunctuation": boolean,
      "enableSpokenEmojis": boolean,
      "enableSpeakerDiarization": boolean,
      "diarizationSpeakerCount": integer,
      "diarizationConfig": {
        object ([SpeakerDiarizationConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeakerDiarizationConfig))
      },
      "metadata": {
        object ([RecognitionMetadata](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#RecognitionMetadata))
      },
      "model": string,
      "useEnhanced": boolean
    }  
  
Fields  
---  
`encoding` |  `enum (`[AudioEncoding](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#AudioEncoding)`)` Encoding of audio data sent in all `RecognitionAudio` messages. This field is optional for `FLAC` and `WAV` audio files and required for all other audio formats. For details, see `[AudioEncoding](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#AudioEncoding)`.  
`sampleRateHertz` |  `integer` Sample rate in Hertz of the audio data sent in all `RecognitionAudio` messages. Valid values are: 8000-48000. 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that's not possible, use the native sample rate of the audio source (instead of re-sampling). This field is optional for FLAC and WAV audio files, but is required for all other audio formats. For details, see `[AudioEncoding](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#AudioEncoding)`.  
`audioChannelCount` |  `integer` The number of channels in the input audio data. ONLY set this for MULTI-CHANNEL recognition. Valid values for LINEAR16, OGG_OPUS and FLAC are `1`-`8`. Valid value for MULAW, AMR, AMR_WB and SPEEX_WITH_HEADER_BYTE is only `1`. If `0` or omitted, defaults to one channel (mono). Note: We only recognize the first channel by default. To perform independent recognition on each channel set `enableSeparateRecognitionPerChannel` to 'true'.  
`enableSeparateRecognitionPerChannel` |  `boolean` This needs to be set to `true` explicitly and `audioChannelCount` > 1 to get each channel recognized separately. The recognition result will contain a `channelTag` field to state which channel that result belongs to. If this is not true, we will only recognize the first channel. The request is billed cumulatively for all channels recognized: `audioChannelCount` multiplied by the length of the audio.  
`languageCode` |  `string` Required. The language of the supplied audio as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US". See [Language Support](https://cloud.google.com/speech-to-text/docs/languages) for a list of the currently supported language codes.  
`alternativeLanguageCodes[]` |  `string` A list of up to 3 additional [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tags, listing possible alternative languages of the supplied audio. See [Language Support](https://cloud.google.com/speech-to-text/docs/languages) for a list of the currently supported language codes. If alternative languages are listed, recognition result will contain recognition in the most likely language detected including the main languageCode. The recognition result will include the language tag of the language detected in the audio. Note: This feature is only supported for Voice Command and Voice Search use cases and performance may vary for other use cases (e.g., phone call transcription).  
`maxAlternatives` |  `integer` Maximum number of recognition hypotheses to be returned. Specifically, the maximum number of `SpeechRecognitionAlternative` messages within each `SpeechRecognitionResult`. The server may return fewer than `maxAlternatives`. Valid values are `0`-`30`. A value of `0` or `1` will return a maximum of one. If omitted, will return a maximum of one.  
`profanityFilter` |  `boolean` If set to `true`, the server will attempt to filter out profanities, replacing all but the initial character in each filtered word with asterisks, e.g. "f***". If set to `false` or omitted, profanities won't be filtered out.  
`adaptation` |  `object (`[SpeechAdaptation](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeechAdaptation)`)` Speech adaptation configuration improves the accuracy of speech recognition. For more information, see the [speech adaptation](https://cloud.google.com/speech-to-text/docs/adaptation) documentation. When speech adaptation is set it supersedes the `speechContexts` field.  
`transcriptNormalization` |  `object (`[TranscriptNormalization](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#TranscriptNormalization)`)` Optional. Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing. For StreamingRecognize, this normalization only applies to stable partial transcripts (stability > 0.8) and final transcripts.  
`speechContexts[]` |  `object (`[SpeechContext](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeechContext)`)` Array of `[SpeechContext](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeechContext)`. A means to provide context to assist the speech recognition. For more information, see [speech adaptation](https://cloud.google.com/speech-to-text/docs/adaptation).  
`enableWordTimeOffsets` |  `boolean` If `true`, the top result includes a list of words and the start and end time offsets (timestamps) for those words. If `false`, no word-level time offset information is returned. The default is `false`.  
`enableWordConfidence` |  `boolean` If `true`, the top result includes a list of words and the confidence for those words. If `false`, no word-level confidence information is returned. The default is `false`.  
`enableAutomaticPunctuation` |  `boolean` If 'true', adds punctuation to recognition result hypotheses. This feature is only available in select languages. Setting this for requests in other languages has no effect at all. The default 'false' value does not add punctuation to result hypotheses.  
`enableSpokenPunctuation` |  `boolean` The spoken punctuation behavior for the call If not set, uses default behavior based on model of choice e.g. command_and_search will enable spoken punctuation by default If 'true', replaces spoken punctuation with the corresponding symbols in the request. For example, "how are you question mark" becomes "how are you?". See <https://cloud.google.com/speech-to-text/docs/spoken-punctuation> for support. If 'false', spoken punctuation is not replaced.  
`enableSpokenEmojis` |  `boolean` The spoken emoji behavior for the call If not set, uses default behavior based on model of choice If 'true', adds spoken emoji formatting for the request. This will replace spoken emojis with the corresponding Unicode symbols in the final transcript. If 'false', spoken emojis are not replaced.  
`enableSpeakerDiarization  
**(deprecated)**` |  `boolean` This item is deprecated!If 'true', enables speaker detection for each recognized word in the top alternative of the recognition result using a speakerLabel provided in the WordInfo. Note: Use diarizationConfig instead.  
`diarizationSpeakerCount  
**(deprecated)**` |  `integer` This item is deprecated!If set, specifies the estimated number of speakers in the conversation. Defaults to '2'. Ignored unless enableSpeakerDiarization is set to true. Note: Use diarizationConfig instead.  
`diarizationConfig` |  `object (`[SpeakerDiarizationConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#SpeakerDiarizationConfig)`)` Config to enable speaker diarization and set additional parameters to make diarization better suited for your application. Note: When this is enabled, we send all the words from the beginning of the audio for the top alternative in every consecutive STREAMING responses. This is done in order to improve our speaker tags as our models learn to identify the speakers in the conversation over time. For non-streaming requests, the diarization results will be provided only in the top alternative of the FINAL SpeechRecognitionResult.  
`metadata` |  `object (`[RecognitionMetadata](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#RecognitionMetadata)`)` Metadata regarding this request.  
`model` |  `string` Which model to select for the given request. Select the model best suited to your domain to get best results. If a model is not explicitly specified, then we auto-select a model based on the parameters in the RecognitionConfig. | **Model** | **Description**  
---|---  
`latest_long` | Best for long form content like media or conversation.  
`latest_short` | Best for short form content like commands or single shot directed speech.  
`command_and_search` | Best for short queries such as voice commands or voice search.  
`phone_call` | Best for audio that originated from a phone call (typically recorded at an 8khz sampling rate).  
`video` | Best for audio that originated from video or includes multiple speakers. Ideally the audio is recorded at a 16khz or greater sampling rate. This is a premium model that costs more than the standard rate.  
`default` | Best for audio that is not one of the specific audio models. For example, long-form audio. Ideally the audio is high-fidelity, recorded at a 16khz or greater sampling rate.  
`medical_conversation` | Best for audio that originated from a conversation between a medical provider and patient.  
`medical_dictation` | Best for audio that originated from dictation notes by a medical provider.  
`useEnhanced` |  `boolean` Set to true to use an enhanced model for speech recognition. If `useEnhanced` is set to true and the `model` field is not set, then an appropriate enhanced model is chosen if an enhanced model exists for the audio.If `useEnhanced` is true and an enhanced version of the specified model does not exist, then the speech is recognized using the standard version of the specified model.  
  
## AudioEncoding

The encoding of the audio data sent in the request.

All encodings support only 1 channel (mono) audio, unless the `audioChannelCount` and `enableSeparateRecognitionPerChannel` fields are set.

For best results, the audio source should be captured and transmitted using a lossless encoding (`FLAC` or `LINEAR16`). The accuracy of the speech recognition can be reduced if lossy codecs are used to capture or transmit audio, particularly if background noise is present. Lossy codecs include `MULAW`, `AMR`, `AMR_WB`, `OGG_OPUS`, `SPEEX_WITH_HEADER_BYTE`, `MP3`, and `WEBM_OPUS`.

The `FLAC` and `WAV` audio file formats include a header that describes the included audio content. You can request recognition for `WAV` files that contain either `LINEAR16` or `MULAW` encoded audio. If you send `FLAC` or `WAV` audio file format in your request, you do not need to specify an `AudioEncoding`; the audio encoding format is determined from the file header. If you specify an `AudioEncoding` when you send send `FLAC` or `WAV` audio, the encoding configuration must match the encoding described in the audio header; otherwise the request returns an `[google.rpc.Code.INVALID_ARGUMENT](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/Shared.Types/Code#ENUM_VALUES.INVALID_ARGUMENT)` error code.

Enums  
---  
`ENCODING_UNSPECIFIED` | Not specified.  
`LINEAR16` | Uncompressed 16-bit signed little-endian samples (Linear PCM).  
`FLAC` | `FLAC` (Free Lossless Audio Codec) is the recommended encoding because it is lossless--therefore recognition is not compromised--and requires only about half the bandwidth of `LINEAR16`. `FLAC` stream encoding supports 16-bit and 24-bit samples, however, not all fields in `STREAMINFO` are supported.  
`MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`AMR` | Adaptive Multi-Rate Narrowband codec. `sampleRateHertz` must be 8000.  
`AMR_WB` | Adaptive Multi-Rate Wideband codec. `sampleRateHertz` must be 16000.  
`OGG_OPUS` | Opus encoded audio frames in Ogg container ([OggOpus](https://wiki.xiph.org/OggOpus)). `sampleRateHertz` must be one of 8000, 12000, 16000, 24000, or 48000.  
`SPEEX_WITH_HEADER_BYTE` | Although the use of lossy encodings is not recommended, if a very low bitrate encoding is required, `OGG_OPUS` is highly preferred over Speex encoding. The [Speex](https://speex.org/) encoding supported by Cloud Speech API has a header byte in each block, as in MIME type `audio/x-speex-with-header-byte`. It is a variant of the RTP Speex encoding defined in [RFC 5574](https://tools.ietf.org/html/rfc5574). The stream is a sequence of blocks, one block per RTP packet. Each block starts with a byte containing the length of the block, in bytes, followed by one or more frames of Speex data, padded to an integral number of bytes (octets) as specified in RFC 5574. In other words, each RTP header is replaced with a single byte containing the block length. Only Speex wideband is supported. `sampleRateHertz` must be 16000.  
`MP3` | MP3 audio. MP3 encoding is a Beta feature and only available in v1p1beta1. Support all standard MP3 bitrates (which range from 32-320 kbps). When using this encoding, `sampleRateHertz` has to match the sample rate of the file being used.  
`WEBM_OPUS` | Opus encoded audio frames in WebM container ([WebM](https://www.webmproject.org/docs/container/)). `sampleRateHertz` must be one of 8000, 12000, 16000, 24000, or 48000.  
`ALAW` | 8-bit samples that compand 13-bit audio samples using G.711 PCMU/a-law.  
  
## SpeechAdaptation

Speech adaptation configuration.

JSON representation  
---  
      
    
    {
      "phraseSets": [
        {
          object ([PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.phraseSets#PhraseSet))
        }
      ],
      "phraseSetReferences": [
        string
      ],
      "customClasses": [
        {
          object ([CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses#CustomClass))
        }
      ],
      "abnfGrammar": {
        object ([ABNFGrammar](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#ABNFGrammar))
      }
    }  
  
Fields  
---  
`phraseSets[]` |  `object (`[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.phraseSets#PhraseSet)`)` A collection of phrase sets. To specify the hints inline, leave the phrase set's `name` blank and fill in the rest of its fields. Any phrase set can use any custom class.  
`phraseSetReferences[]` |  `string` A collection of phrase set resource names to use.  
`customClasses[]` |  `object (`[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses#CustomClass)`)` A collection of custom classes. To specify the classes inline, leave the class' `name` blank and fill in the rest of its fields, giving it a unique `customClassId`. Refer to the inline defined class in phrase hints by its `customClassId`.  
`abnfGrammar` |  `object (`[ABNFGrammar](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#ABNFGrammar)`)` Augmented Backus-Naur form (ABNF) is a standardized grammar notation comprised by a set of derivation rules. See specifications: <https://www.w3.org/TR/speech-grammar>  
  
## ABNFGrammar

JSON representation  
---  
      
    
    {
      "abnfStrings": [
        string
      ]
    }  
  
Fields  
---  
`abnfStrings[]` |  `string` All declarations and rules of an ABNF grammar broken up into multiple strings that will end up concatenated.  
  
## TranscriptNormalization

Transcription normalization configuration. Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing. For StreamingRecognize, this normalization only applies to stable partial transcripts (stability > 0.8) and final transcripts.

JSON representation  
---  
      
    
    {
      "entries": [
        {
          object ([Entry](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#Entry))
        }
      ]
    }  
  
Fields  
---  
`entries[]` |  `object (`[Entry](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#Entry)`)` A list of replacement entries. We will perform replacement with one entry at a time. For example, the second entry in ["cat" => "dog", "mountain cat" => "mountain dog"] will never be applied because we will always process the first entry before it. At most 100 entries.  
  
## Entry

A single replacement configuration.

JSON representation  
---  
      
    
    {
      "search": string,
      "replace": string,
      "caseSensitive": boolean
    }  
  
Fields  
---  
`search` |  `string` What to replace. Max length is 100 characters.  
`replace` |  `string` What to replace with. Max length is 100 characters.  
`caseSensitive` |  `boolean` Whether the search is case sensitive.  
  
## SpeechContext

Provides "hints" to the speech recognizer to favor specific words and phrases in the results.

JSON representation  
---  
      
    
    {
      "phrases": [
        string
      ],
      "boost": number
    }  
  
Fields  
---  
`phrases[]` |  `string` A list of strings containing words and phrases "hints" so that the speech recognition is more likely to recognize them. This can be used to improve the accuracy for specific words and phrases, for example, if specific commands are typically spoken by the user. This can also be used to add additional words to the vocabulary of the recognizer. See [usage limits](https://cloud.google.com/speech-to-text/quotas#content).List items can also be set to classes for groups of words that represent common concepts that occur in natural language. For example, rather than providing phrase hints for every month of the year, using the $MONTH class improves the likelihood of correctly transcribing audio that includes months.  
`boost` |  `number` Hint Boost. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost values would correspond to anti-biasing. Anti-biasing is not enabled, so negative boost will simply be ignored. Though `boost` can accept a wide range of positive values, most use cases are best served with values between 0 and 20. We recommend using a binary search approach to finding the optimal value for your use case.  
  
## SpeakerDiarizationConfig

Config to enable speaker diarization.

JSON representation  
---  
      
    
    {
      "enableSpeakerDiarization": boolean,
      "minSpeakerCount": integer,
      "maxSpeakerCount": integer,
      "speakerTag": integer
    }  
  
Fields  
---  
`enableSpeakerDiarization` |  `boolean` If 'true', enables speaker detection for each recognized word in the top alternative of the recognition result using a speakerLabel provided in the WordInfo.  
`minSpeakerCount` |  `integer` Minimum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 2.  
`maxSpeakerCount` |  `integer` Maximum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 6.  
`speakerTag  
**(deprecated)**` |  `integer` This item is deprecated!Output only. Unused.  
  
## RecognitionMetadata

This item is deprecated!

Description of audio data to be recognized.

JSON representation  
---  
      
    
    {
      "interactionType": enum ([InteractionType](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#InteractionType)),
      "industryNaicsCodeOfAudio": integer,
      "microphoneDistance": enum ([MicrophoneDistance](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#MicrophoneDistance)),
      "originalMediaType": enum ([OriginalMediaType](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#OriginalMediaType)),
      "recordingDeviceType": enum ([RecordingDeviceType](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#RecordingDeviceType)),
      "recordingDeviceName": string,
      "originalMimeType": string,
      "obfuscatedId": string,
      "audioTopic": string
    }  
  
Fields  
---  
`interactionType` |  `enum (`[InteractionType](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#InteractionType)`)` The use case most closely describing the audio content to be recognized.  
`industryNaicsCodeOfAudio` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The industry vertical to which this speech recognition request most closely applies. This is most indicative of the topics contained in the audio. Use the 6-digit NAICS code to identify the industry vertical - see <https://www.naics.com/search/>.  
`microphoneDistance` |  `enum (`[MicrophoneDistance](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#MicrophoneDistance)`)` The audio type that most closely describes the audio being recognized.  
`originalMediaType` |  `enum (`[OriginalMediaType](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#OriginalMediaType)`)` The original media the speech was recorded on.  
`recordingDeviceType` |  `enum (`[RecordingDeviceType](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig#RecordingDeviceType)`)` The type of device the speech was recorded with.  
`recordingDeviceName` |  `string` The device used to make the recording. Examples 'Nexus 5X' or 'Polycom SoundStation IP 6000' or 'POTS' or 'VoIP' or 'Cardioid Microphone'.  
`originalMimeType` |  `string` Mime type of the original audio file. For example `audio/m4a`, `audio/x-alaw-basic`, `audio/mp3`, `audio/3gpp`. A list of possible audio mime types is maintained at <http://www.iana.org/assignments/media-types/media-types.xhtml#audio>  
`obfuscatedId  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Obfuscated (privacy-protected) ID of the user, to identify number of unique users using the service.  
`audioTopic` |  `string` Description of the content. Eg. "Recordings of federal supreme court hearings from 2012".  
  
## InteractionType

Use case categories that the audio recognition request can be described by.

Enums  
---  
`INTERACTION_TYPE_UNSPECIFIED` | Use case is either unknown or is something other than one of the other values below.  
`DISCUSSION` | Multiple people in a conversation or discussion. For example in a meeting with two or more people actively participating. Typically all the primary people speaking would be in the same room (if not, see PHONE_CALL)  
`PRESENTATION` | One or more persons lecturing or presenting to others, mostly uninterrupted.  
`PHONE_CALL` | A phone-call or video-conference in which two or more people, who are not in the same room, are actively participating.  
`VOICEMAIL` | A recorded message intended for another person to listen to.  
`PROFESSIONALLY_PRODUCED` | Professionally produced audio (eg. TV Show, Podcast).  
`VOICE_SEARCH` | Transcribe spoken questions and queries into text.  
`VOICE_COMMAND` | Transcribe voice commands, such as for controlling a device.  
`DICTATION` | Transcribe speech to text to create a written document, such as a text-message, email or report.  
  
## MicrophoneDistance

Enumerates the types of capture settings describing an audio file.

Enums  
---  
`MICROPHONE_DISTANCE_UNSPECIFIED` | Audio type is not known.  
`NEARFIELD` | The audio was captured from a closely placed microphone. Eg. phone, dictaphone, or handheld microphone. Generally if there speaker is within 1 meter of the microphone.  
`MIDFIELD` | The speaker if within 3 meters of the microphone.  
`FARFIELD` | The speaker is more than 3 meters away from the microphone.  
  
## OriginalMediaType

The original media the speech was recorded on.

Enums  
---  
`ORIGINAL_MEDIA_TYPE_UNSPECIFIED` | Unknown original media type.  
`AUDIO` | The speech data is an audio recording.  
`VIDEO` | The speech data originally recorded on a video.  
  
## RecordingDeviceType

The type of device the speech was recorded with.

Enums  
---  
`RECORDING_DEVICE_TYPE_UNSPECIFIED` | The recording device is unknown.  
`SMARTPHONE` | Speech was recorded on a smartphone.  
`PC` | Speech was recorded using a personal computer or tablet.  
`PHONE_LINE` | Speech was recorded over a phone line.  
`VEHICLE` | Speech was recorded in a vehicle.  
`OTHER_OUTDOOR_DEVICE` | Speech was recorded outdoors.  
`OTHER_INDOOR_DEVICE` | Speech was recorded indoors.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
