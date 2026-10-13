---
url: https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1
title: Package google.cloud.speech.v1p1beta1 \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:35.331190+00:00
---

# Package google.cloud.speech.v1p1beta1  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Reference ](https://docs.cloud.google.com/speech-to-text/docs/apis)



Send feedback 

#  Package google.cloud.speech.v1p1beta1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Adaptation](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.Adaptation)` (interface)
  * `[Speech](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.Speech)` (interface)
  * `[CreateCustomClassRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CreateCustomClassRequest)` (message)
  * `[CreatePhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CreatePhraseSetRequest)` (message)
  * `[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass)` (message)
  * `[CustomClass.ClassItem](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass.ClassItem)` (message)
  * `[CustomClass.State](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass.State)` (enum)
  * `[DeleteCustomClassRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.DeleteCustomClassRequest)` (message)
  * `[DeletePhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.DeletePhraseSetRequest)` (message)
  * `[GetCustomClassRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.GetCustomClassRequest)` (message)
  * `[GetPhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.GetPhraseSetRequest)` (message)
  * `[ListCustomClassesRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.ListCustomClassesRequest)` (message)
  * `[ListCustomClassesResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.ListCustomClassesResponse)` (message)
  * `[ListPhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.ListPhraseSetRequest)` (message)
  * `[ListPhraseSetResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.ListPhraseSetResponse)` (message)
  * `[LongRunningRecognizeMetadata](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.LongRunningRecognizeMetadata)` (message)
  * `[LongRunningRecognizeRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.LongRunningRecognizeRequest)` (message)
  * `[LongRunningRecognizeResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.LongRunningRecognizeResponse)` (message)
  * `[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet)` (message)
  * `[PhraseSet.Phrase](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet.Phrase)` (message)
  * `[PhraseSet.State](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet.State)` (enum)
  * `[RecognitionAudio](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionAudio)` (message)
  * `[RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig)` (message)
  * `[RecognitionConfig.AudioEncoding](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig.AudioEncoding)` (enum)
  * `[RecognitionMetadata](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata)` (message) **(deprecated)**
  * `[RecognitionMetadata.InteractionType](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata.InteractionType)` (enum)
  * `[RecognitionMetadata.MicrophoneDistance](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata.MicrophoneDistance)` (enum)
  * `[RecognitionMetadata.OriginalMediaType](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata.OriginalMediaType)` (enum)
  * `[RecognitionMetadata.RecordingDeviceType](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata.RecordingDeviceType)` (enum)
  * `[RecognizeRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognizeRequest)` (message)
  * `[RecognizeResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognizeResponse)` (message)
  * `[SpeakerDiarizationConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeakerDiarizationConfig)` (message)
  * `[SpeechAdaptation](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechAdaptation)` (message)
  * `[SpeechAdaptation.ABNFGrammar](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechAdaptation.ABNFGrammar)` (message)
  * `[SpeechAdaptationInfo](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechAdaptationInfo)` (message)
  * `[SpeechContext](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechContext)` (message)
  * `[SpeechRecognitionAlternative](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechRecognitionAlternative)` (message)
  * `[SpeechRecognitionResult](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechRecognitionResult)` (message)
  * `[StreamingRecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognitionConfig)` (message)
  * `[StreamingRecognitionConfig.VoiceActivityTimeout](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognitionConfig.VoiceActivityTimeout)` (message)
  * `[StreamingRecognitionResult](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognitionResult)` (message)
  * `[StreamingRecognizeRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeRequest)` (message)
  * `[StreamingRecognizeResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeResponse)` (message)
  * `[StreamingRecognizeResponse.SpeechEventType](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeResponse.SpeechEventType)` (enum)
  * `[TranscriptNormalization](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.TranscriptNormalization)` (message)
  * `[TranscriptNormalization.Entry](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.TranscriptNormalization.Entry)` (message)
  * `[TranscriptOutputConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.TranscriptOutputConfig)` (message)
  * `[UpdateCustomClassRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.UpdateCustomClassRequest)` (message)
  * `[UpdatePhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.UpdatePhraseSetRequest)` (message)
  * `[WordInfo](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.WordInfo)` (message)



## Adaptation

Service that implements Google Cloud Speech Adaptation API.

CreateCustomClass  
---  
` rpc CreateCustomClass(`[CreateCustomClassRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CreateCustomClassRequest)`) returns (`[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass)`) ` Create a custom class.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreatePhraseSet  
---  
` rpc CreatePhraseSet(`[CreatePhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CreatePhraseSetRequest)`) returns (`[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet)`) ` Create a set of phrase hints. Each item in the set can be a single word or a multi-word phrase. The items in the PhraseSet are favored by the recognition model when you send a call that includes the PhraseSet.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteCustomClass  
---  
` rpc DeleteCustomClass(`[DeleteCustomClassRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.DeleteCustomClassRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete a custom class.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeletePhraseSet  
---  
` rpc DeletePhraseSet(`[DeletePhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.DeletePhraseSetRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete a phrase set.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetCustomClass  
---  
` rpc GetCustomClass(`[GetCustomClassRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.GetCustomClassRequest)`) returns (`[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass)`) ` Get a custom class.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetPhraseSet  
---  
` rpc GetPhraseSet(`[GetPhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.GetPhraseSetRequest)`) returns (`[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet)`) ` Get a phrase set.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListCustomClasses  
---  
` rpc ListCustomClasses(`[ListCustomClassesRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.ListCustomClassesRequest)`) returns (`[ListCustomClassesResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.ListCustomClassesResponse)`) ` List custom classes.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListPhraseSet  
---  
` rpc ListPhraseSet(`[ListPhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.ListPhraseSetRequest)`) returns (`[ListPhraseSetResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.ListPhraseSetResponse)`) ` List phrase sets.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateCustomClass  
---  
` rpc UpdateCustomClass(`[UpdateCustomClassRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.UpdateCustomClassRequest)`) returns (`[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass)`) ` Update a custom class.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdatePhraseSet  
---  
` rpc UpdatePhraseSet(`[UpdatePhraseSetRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.UpdatePhraseSetRequest)`) returns (`[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet)`) ` Update a phrase set.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Speech

Service that implements Google Cloud Speech API.

LongRunningRecognize  
---  
` rpc LongRunningRecognize(`[LongRunningRecognizeRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.LongRunningRecognizeRequest)`) returns (`[Operation](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface. Returns either an `Operation.error` or an `Operation.response` which contains a `LongRunningRecognizeResponse` message. For more information on asynchronous speech recognition, see the [how-to](https://cloud.google.com/speech-to-text/docs/async-recognize).

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
Recognize  
---  
` rpc Recognize(`[RecognizeRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognizeRequest)`) returns (`[RecognizeResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognizeResponse)`) ` Performs synchronous speech recognition: receive results after all audio has been sent and processed.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
StreamingRecognize  
---  
` rpc StreamingRecognize(`[StreamingRecognizeRequest](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeRequest)`) returns (`[StreamingRecognizeResponse](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeResponse)`) ` Performs bidirectional streaming speech recognition: receive results while sending audio. This method is only available via the gRPC API (not REST).

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## CreateCustomClassRequest

Message sent by the client for the `CreateCustomClass` method.

Fields  
---  
`parent` |  `string` Required. The parent resource where this custom class will be created. Format:`projects/{project}/locations/{location}/customClasses`Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `speech.customClasses.create`

  
`custom_class_id` |  `string` Required. The ID to use for the custom class, which will become the final component of the custom class' resource name.This value should restrict to letters, numbers, and hyphens, with the first character a letter, the last a letter or a number, and be 4-63 characters.  
`custom_class` |  `[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass)` Required. The custom class to create.  
  
## CreatePhraseSetRequest

Message sent by the client for the `CreatePhraseSet` method.

Fields  
---  
`parent` |  `string` Required. The parent resource where this phrase set will be created. Format:`projects/{project}/locations/{location}`Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `speech.phraseSets.create`

  
`phrase_set_id` |  `string` Required. The ID to use for the phrase set, which will become the final component of the phrase set's resource name.This value should restrict to letters, numbers, and hyphens, with the first character a letter, the last a letter or a number, and be 4-63 characters.  
`phrase_set` |  `[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet)` Required. The phrase set to create.  
  
## CustomClass

A set of words or phrases that represents a common concept likely to appear in your audio, for example a list of passenger ship names. CustomClass items can be substituted into placeholders that you set in PhraseSet phrases.

Fields  
---  
`name` |  `string` The resource name of the custom class.  
`custom_class_id` |  `string` If this custom class is a resource, the custom_class_id is the resource id of the CustomClass. Case sensitive.  
`items[]` |  `[ClassItem](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass.ClassItem)` A collection of class items.  
`kms_key_name` |  `string` Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the ClassItem is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.  
`kms_key_version_name` |  `string` Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the ClassItem is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`.  
`uid` |  `string` Output only. System-assigned unique identifier for the CustomClass. This field is not used.  
`display_name` |  `string` Output only. User-settable, human-readable name for the CustomClass. Must be 63 characters or less. This field is not used.  
`state` |  `[State](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass.State)` Output only. The CustomClass lifecycle state. This field is not used.  
`delete_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this resource was requested for deletion. This field is not used.  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this resource will be purged. This field is not used.  
`annotations` |  `map<string, string>` Output only. Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations. This field is not used.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. This field is not used.  
`reconciling` |  `bool` Output only. Whether or not this CustomClass is in the process of being updated. This field is not used.  
  
## ClassItem

An item of the class.

Fields  
---  
`value` |  `string` The class item's value.  
  
## State

Set of states that define the lifecycle of a CustomClass.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state. This is only used/useful for distinguishing unset values.  
`ACTIVE` | The normal and active state.  
`DELETED` | This CustomClass has been deleted.  
  
## DeleteCustomClassRequest

Message sent by the client for the `DeleteCustomClass` method.

Fields  
---  
`name` |  `string` Required. The name of the custom class to delete. Format:`projects/{project}/locations/{location}/customClasses/{custom_class}`Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `speech.customClasses.delete`

  
  
## DeletePhraseSetRequest

Message sent by the client for the `DeletePhraseSet` method.

Fields  
---  
`name` |  `string` Required. The name of the phrase set to delete. Format:`projects/{project}/locations/{location}/phraseSets/{phrase_set}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `speech.phraseSets.delete`

  
  
## GetCustomClassRequest

Message sent by the client for the `GetCustomClass` method.

Fields  
---  
`name` |  `string` Required. The name of the custom class to retrieve. Format:`projects/{project}/locations/{location}/customClasses/{custom_class}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `speech.customClasses.get`

  
  
## GetPhraseSetRequest

Message sent by the client for the `GetPhraseSet` method.

Fields  
---  
`name` |  `string` Required. The name of the phrase set to retrieve. Format:`projects/{project}/locations/{location}/phraseSets/{phrase_set}`Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `speech.phraseSets.get`

  
  
## ListCustomClassesRequest

Message sent by the client for the `ListCustomClasses` method.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of custom classes. Format:`projects/{project}/locations/{location}/customClasses`Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `speech.customClasses.list`

  
`page_size` |  `int32` The maximum number of custom classes to return. The service may return fewer than this value. If unspecified, at most 50 custom classes will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` A page token, received from a previous `ListCustomClass` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListCustomClass` must match the call that provided the page token.  
  
## ListCustomClassesResponse

Message returned to the client by the `ListCustomClasses` method.

Fields  
---  
`custom_classes[]` |  `[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass)` The custom classes.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListPhraseSetRequest

Message sent by the client for the `ListPhraseSet` method.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of phrase set. Format:`projects/{project}/locations/{location}`Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `speech.phraseSets.list`

  
`page_size` |  `int32` The maximum number of phrase sets to return. The service may return fewer than this value. If unspecified, at most 50 phrase sets will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` A page token, received from a previous `ListPhraseSet` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListPhraseSet` must match the call that provided the page token.  
  
## ListPhraseSetResponse

Message returned to the client by the `ListPhraseSet` method.

Fields  
---  
`phrase_sets[]` |  `[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet)` The phrase set.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## LongRunningRecognizeMetadata

Describes the progress of a long-running `LongRunningRecognize` call. It is included in the `metadata` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

Fields  
---  
`progress_percent` |  `int32` Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time when the request was received.  
`last_update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time of the most recent processing update.  
`uri` |  `string` Output only. The URI of the audio file being transcribed. Empty if the audio was sent as byte content.  
`output_config` |  `[TranscriptOutputConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.TranscriptOutputConfig)` Output only. A copy of the TranscriptOutputConfig if it was set in the request.  
  
## LongRunningRecognizeRequest

The top-level message sent by the client for the `LongRunningRecognize` method.

Fields  
---  
`config` |  `[RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig)` Required. Provides information to the recognizer that specifies how to process the request.  
`audio` |  `[RecognitionAudio](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionAudio)` Required. The audio data to be recognized.  
`output_config` |  `[TranscriptOutputConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.TranscriptOutputConfig)` Optional. Specifies an optional destination for the recognition results.  
  
## LongRunningRecognizeResponse

The only message returned to the client by the `LongRunningRecognize` method. It contains the result as zero or more sequential `SpeechRecognitionResult` messages. It is included in the `result.response` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

Fields  
---  
`results[]` |  `[SpeechRecognitionResult](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechRecognitionResult)` Sequential list of transcription results corresponding to sequential portions of audio.  
`total_billed_time` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` When available, billed audio seconds for the corresponding request.  
`output_config` |  `[TranscriptOutputConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.TranscriptOutputConfig)` Original output config if present in the request.  
`output_error` |  `[Status](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.rpc#google.rpc.Status)` If the transcript output fails this field contains the relevant error.  
`speech_adaptation_info` |  `[SpeechAdaptationInfo](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechAdaptationInfo)` Provides information on speech adaptation behavior in response  
`request_id` |  `int64` The ID associated with the request. This is a unique ID specific only to the given request.  
  
## PhraseSet

Provides "hints" to the speech recognizer to favor specific words and phrases in the results.

Fields  
---  
`name` |  `string` The resource name of the phrase set.  
`phrases[]` |  `[Phrase](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet.Phrase)` A list of word and phrases.  
`boost` |  `float` Hint Boost. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost values would correspond to anti-biasing. Anti-biasing is not enabled, so negative boost will simply be ignored. Though `boost` can accept a wide range of positive values, most use cases are best served with values between 0 (exclusive) and 20. We recommend using a binary search approach to finding the optimal value for your use case as well as adding phrases both with and without boost to your requests.  
`kms_key_name` |  `string` Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the PhraseSet is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.  
`kms_key_version_name` |  `string` Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the PhraseSet is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`.  
`uid` |  `string` Output only. System-assigned unique identifier for the PhraseSet. This field is not used.  
`display_name` |  `string` Output only. User-settable, human-readable name for the PhraseSet. Must be 63 characters or less. This field is not used.  
`state` |  `[State](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet.State)` Output only. The CustomClass lifecycle state. This field is not used.  
`delete_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this resource was requested for deletion. This field is not used.  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this resource will be purged. This field is not used.  
`annotations` |  `map<string, string>` Output only. Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations. This field is not used.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. This field is not used.  
`reconciling` |  `bool` Output only. Whether or not this PhraseSet is in the process of being updated. This field is not used.  
  
## Phrase

A phrases containing words and phrase "hints" so that the speech recognition is more likely to recognize them. This can be used to improve the accuracy for specific words and phrases, for example, if specific commands are typically spoken by the user. This can also be used to add additional words to the vocabulary of the recognizer. See [usage limits](https://cloud.google.com/speech-to-text/quotas#content).

List items can also include pre-built or custom classes containing groups of words that represent common concepts that occur in natural language. For example, rather than providing a phrase hint for every month of the year (e.g. "i was born in january", "i was born in febuary", ...), use the pre-built `$MONTH` class improves the likelihood of correctly transcribing audio that includes months (e.g. "i was born in $month"). To refer to pre-built classes, use the class' symbol prepended with `$` e.g. `$MONTH`. To refer to custom classes that were defined inline in the request, set the class's `custom_class_id` to a string unique to all class resources and inline classes. Then use the class' id wrapped in $`{...}` e.g. "${my-months}". To refer to custom classes resources, use the class' id wrapped in `${}` (e.g. `${my-months}`).

Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value.

Fields  
---  
`value` |  `string` The phrase itself.  
`boost` |  `float` Hint Boost. Overrides the boost set at the phrase set level. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost will simply be ignored. Though `boost` can accept a wide range of positive values, most use cases are best served with values between 0 and 20. We recommend using a binary search approach to finding the optimal value for your use case as well as adding phrases both with and without boost to your requests.  
  
## State

Set of states that define the lifecycle of a CustomClass.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state. This is only used/useful for distinguishing unset values.  
`ACTIVE` | The normal and active state.  
`DELETED` | This CustomClass has been deleted.  
  
## RecognitionAudio

Contains audio data in the encoding specified in the `RecognitionConfig`. Either `content` or `uri` must be supplied. Supplying both or neither returns `[google.rpc.Code.INVALID_ARGUMENT](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)`. See [content limits](https://cloud.google.com/speech-to-text/quotas#content).

Fields  
---  
Union field `audio_source`. The audio source, which is either inline content or a Google Cloud Storage uri. `audio_source` can be only one of the following:  
`content` |  `bytes` The audio data bytes encoded as specified in `RecognitionConfig`. Note: as with all bytes fields, proto buffers use a pure binary representation, whereas JSON representations use base64.  
`uri` |  `string` URI that points to a file that contains audio data bytes as specified in `RecognitionConfig`. The file must not be compressed (for example, gzip). Currently, only Google Cloud Storage URIs are supported, which must be specified in the following format: `gs://bucket_name/object_name` (other URI formats return `[google.rpc.Code.INVALID_ARGUMENT](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)`). For more information, see [Request URIs](https://cloud.google.com/storage/docs/reference-uris).  
  
## RecognitionConfig

Provides information to the recognizer that specifies how to process the request.

Fields  
---  
`encoding` |  `[AudioEncoding](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig.AudioEncoding)` Encoding of audio data sent in all `RecognitionAudio` messages. This field is optional for `FLAC` and `WAV` audio files and required for all other audio formats. For details, see `[AudioEncoding](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig.AudioEncoding)`.  
`sample_rate_hertz` |  `int32` Sample rate in Hertz of the audio data sent in all `RecognitionAudio` messages. Valid values are: 8000-48000. 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that's not possible, use the native sample rate of the audio source (instead of re-sampling). This field is optional for FLAC and WAV audio files, but is required for all other audio formats. For details, see `[AudioEncoding](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig.AudioEncoding)`.  
`audio_channel_count` |  `int32` The number of channels in the input audio data. ONLY set this for MULTI-CHANNEL recognition. Valid values for LINEAR16, OGG_OPUS and FLAC are `1`-`8`. Valid value for MULAW, AMR, AMR_WB and SPEEX_WITH_HEADER_BYTE is only `1`. If `0` or omitted, defaults to one channel (mono). Note: We only recognize the first channel by default. To perform independent recognition on each channel set `enable_separate_recognition_per_channel` to 'true'.  
`enable_separate_recognition_per_channel` |  `bool` This needs to be set to `true` explicitly and `audio_channel_count` > 1 to get each channel recognized separately. The recognition result will contain a `channel_tag` field to state which channel that result belongs to. If this is not true, we will only recognize the first channel. The request is billed cumulatively for all channels recognized: `audio_channel_count` multiplied by the length of the audio.  
`language_code` |  `string` Required. The language of the supplied audio as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US". See [Language Support](https://cloud.google.com/speech-to-text/docs/languages) for a list of the currently supported language codes.  
`alternative_language_codes[]` |  `string` A list of up to 3 additional [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tags, listing possible alternative languages of the supplied audio. See [Language Support](https://cloud.google.com/speech-to-text/docs/languages) for a list of the currently supported language codes. If alternative languages are listed, recognition result will contain recognition in the most likely language detected including the main language_code. The recognition result will include the language tag of the language detected in the audio. Note: This feature is only supported for Voice Command and Voice Search use cases and performance may vary for other use cases (e.g., phone call transcription).  
`max_alternatives` |  `int32` Maximum number of recognition hypotheses to be returned. Specifically, the maximum number of `SpeechRecognitionAlternative` messages within each `SpeechRecognitionResult`. The server may return fewer than `max_alternatives`. Valid values are `0`-`30`. A value of `0` or `1` will return a maximum of one. If omitted, will return a maximum of one.  
`profanity_filter` |  `bool` If set to `true`, the server will attempt to filter out profanities, replacing all but the initial character in each filtered word with asterisks, e.g. "f***". If set to `false` or omitted, profanities won't be filtered out.  
`adaptation` |  `[SpeechAdaptation](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechAdaptation)` Speech adaptation configuration improves the accuracy of speech recognition. For more information, see the [speech adaptation](https://cloud.google.com/speech-to-text/docs/adaptation) documentation. When speech adaptation is set it supersedes the `speech_contexts` field.  
`transcript_normalization` |  `[TranscriptNormalization](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.TranscriptNormalization)` Optional. Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing. For StreamingRecognize, this normalization only applies to stable partial transcripts (stability > 0.8) and final transcripts.  
`speech_contexts[]` |  `[SpeechContext](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechContext)` Array of `[SpeechContext](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechContext)`. A means to provide context to assist the speech recognition. For more information, see [speech adaptation](https://cloud.google.com/speech-to-text/docs/adaptation).  
`enable_word_time_offsets` |  `bool` If `true`, the top result includes a list of words and the start and end time offsets (timestamps) for those words. If `false`, no word-level time offset information is returned. The default is `false`.  
`enable_word_confidence` |  `bool` If `true`, the top result includes a list of words and the confidence for those words. If `false`, no word-level confidence information is returned. The default is `false`.  
`enable_automatic_punctuation` |  `bool` If 'true', adds punctuation to recognition result hypotheses. This feature is only available in select languages. Setting this for requests in other languages has no effect at all. The default 'false' value does not add punctuation to result hypotheses.  
`enable_spoken_punctuation` |  `[BoolValue](https://protobuf.dev/reference/protobuf/google.protobuf/#bool-value)` The spoken punctuation behavior for the call If not set, uses default behavior based on model of choice e.g. command_and_search will enable spoken punctuation by default If 'true', replaces spoken punctuation with the corresponding symbols in the request. For example, "how are you question mark" becomes "how are you?". See <https://cloud.google.com/speech-to-text/docs/spoken-punctuation> for support. If 'false', spoken punctuation is not replaced.  
`enable_spoken_emojis` |  `[BoolValue](https://protobuf.dev/reference/protobuf/google.protobuf/#bool-value)` The spoken emoji behavior for the call If not set, uses default behavior based on model of choice If 'true', adds spoken emoji formatting for the request. This will replace spoken emojis with the corresponding Unicode symbols in the final transcript. If 'false', spoken emojis are not replaced.  
`enable_speaker_diarization  
**(deprecated)**` |  `bool` This item is deprecated!If 'true', enables speaker detection for each recognized word in the top alternative of the recognition result using a speaker_label provided in the WordInfo. Note: Use diarization_config instead.  
`diarization_speaker_count  
**(deprecated)**` |  `int32` This item is deprecated!If set, specifies the estimated number of speakers in the conversation. Defaults to '2'. Ignored unless enable_speaker_diarization is set to true. Note: Use diarization_config instead.  
`diarization_config` |  `[SpeakerDiarizationConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeakerDiarizationConfig)` Config to enable speaker diarization and set additional parameters to make diarization better suited for your application. Note: When this is enabled, we send all the words from the beginning of the audio for the top alternative in every consecutive STREAMING responses. This is done in order to improve our speaker tags as our models learn to identify the speakers in the conversation over time. For non-streaming requests, the diarization results will be provided only in the top alternative of the FINAL SpeechRecognitionResult.  
`metadata` |  `[RecognitionMetadata](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata)` Metadata regarding this request.  
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
`use_enhanced` |  `bool` Set to true to use an enhanced model for speech recognition. If `use_enhanced` is set to true and the `model` field is not set, then an appropriate enhanced model is chosen if an enhanced model exists for the audio.If `use_enhanced` is true and an enhanced version of the specified model does not exist, then the speech is recognized using the standard version of the specified model.  
  
## AudioEncoding

The encoding of the audio data sent in the request.

All encodings support only 1 channel (mono) audio, unless the `audio_channel_count` and `enable_separate_recognition_per_channel` fields are set.

For best results, the audio source should be captured and transmitted using a lossless encoding (`FLAC` or `LINEAR16`). The accuracy of the speech recognition can be reduced if lossy codecs are used to capture or transmit audio, particularly if background noise is present. Lossy codecs include `MULAW`, `AMR`, `AMR_WB`, `OGG_OPUS`, `SPEEX_WITH_HEADER_BYTE`, `MP3`, and `WEBM_OPUS`.

The `FLAC` and `WAV` audio file formats include a header that describes the included audio content. You can request recognition for `WAV` files that contain either `LINEAR16` or `MULAW` encoded audio. If you send `FLAC` or `WAV` audio file format in your request, you do not need to specify an `AudioEncoding`; the audio encoding format is determined from the file header. If you specify an `AudioEncoding` when you send send `FLAC` or `WAV` audio, the encoding configuration must match the encoding described in the audio header; otherwise the request returns an `[google.rpc.Code.INVALID_ARGUMENT](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)` error code.

Enums  
---  
`ENCODING_UNSPECIFIED` | Not specified.  
`LINEAR16` | Uncompressed 16-bit signed little-endian samples (Linear PCM).  
`FLAC` | `FLAC` (Free Lossless Audio Codec) is the recommended encoding because it is lossless--therefore recognition is not compromised--and requires only about half the bandwidth of `LINEAR16`. `FLAC` stream encoding supports 16-bit and 24-bit samples, however, not all fields in `STREAMINFO` are supported.  
`MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`AMR` | Adaptive Multi-Rate Narrowband codec. `sample_rate_hertz` must be 8000.  
`AMR_WB` | Adaptive Multi-Rate Wideband codec. `sample_rate_hertz` must be 16000.  
`OGG_OPUS` | Opus encoded audio frames in Ogg container ([OggOpus](https://wiki.xiph.org/OggOpus)). `sample_rate_hertz` must be one of 8000, 12000, 16000, 24000, or 48000.  
`SPEEX_WITH_HEADER_BYTE` | Although the use of lossy encodings is not recommended, if a very low bitrate encoding is required, `OGG_OPUS` is highly preferred over Speex encoding. The [Speex](https://speex.org/) encoding supported by Cloud Speech API has a header byte in each block, as in MIME type `audio/x-speex-with-header-byte`. It is a variant of the RTP Speex encoding defined in [RFC 5574](https://tools.ietf.org/html/rfc5574). The stream is a sequence of blocks, one block per RTP packet. Each block starts with a byte containing the length of the block, in bytes, followed by one or more frames of Speex data, padded to an integral number of bytes (octets) as specified in RFC 5574. In other words, each RTP header is replaced with a single byte containing the block length. Only Speex wideband is supported. `sample_rate_hertz` must be 16000.  
`MP3` | MP3 audio. MP3 encoding is a Beta feature and only available in v1p1beta1. Support all standard MP3 bitrates (which range from 32-320 kbps). When using this encoding, `sample_rate_hertz` has to match the sample rate of the file being used.  
`WEBM_OPUS` | Opus encoded audio frames in WebM container ([WebM](https://www.webmproject.org/docs/container/)). `sample_rate_hertz` must be one of 8000, 12000, 16000, 24000, or 48000.  
`ALAW` | 8-bit samples that compand 13-bit audio samples using G.711 PCMU/a-law.  
  
## RecognitionMetadata

This item is deprecated!

Description of audio data to be recognized.

Fields  
---  
`interaction_type` |  `[InteractionType](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata.InteractionType)` The use case most closely describing the audio content to be recognized.  
`industry_naics_code_of_audio` |  `uint32` The industry vertical to which this speech recognition request most closely applies. This is most indicative of the topics contained in the audio. Use the 6-digit NAICS code to identify the industry vertical - see <https://www.naics.com/search/>.  
`microphone_distance` |  `[MicrophoneDistance](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata.MicrophoneDistance)` The audio type that most closely describes the audio being recognized.  
`original_media_type` |  `[OriginalMediaType](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata.OriginalMediaType)` The original media the speech was recorded on.  
`recording_device_type` |  `[RecordingDeviceType](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionMetadata.RecordingDeviceType)` The type of device the speech was recorded with.  
`recording_device_name` |  `string` The device used to make the recording. Examples 'Nexus 5X' or 'Polycom SoundStation IP 6000' or 'POTS' or 'VoIP' or 'Cardioid Microphone'.  
`original_mime_type` |  `string` Mime type of the original audio file. For example `audio/m4a`, `audio/x-alaw-basic`, `audio/mp3`, `audio/3gpp`. A list of possible audio mime types is maintained at <http://www.iana.org/assignments/media-types/media-types.xhtml#audio>  
`obfuscated_id  
**(deprecated)**` |  `int64` This item is deprecated!Obfuscated (privacy-protected) ID of the user, to identify number of unique users using the service.  
`audio_topic` |  `string` Description of the content. Eg. "Recordings of federal supreme court hearings from 2012".  
  
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
  
## RecognizeRequest

The top-level message sent by the client for the `Recognize` method.

Fields  
---  
`config` |  `[RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig)` Required. Provides information to the recognizer that specifies how to process the request.  
`audio` |  `[RecognitionAudio](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionAudio)` Required. The audio data to be recognized.  
  
## RecognizeResponse

The only message returned to the client by the `Recognize` method. It contains the result as zero or more sequential `SpeechRecognitionResult` messages.

Fields  
---  
`results[]` |  `[SpeechRecognitionResult](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechRecognitionResult)` Sequential list of transcription results corresponding to sequential portions of audio.  
`total_billed_time` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` When available, billed audio seconds for the corresponding request.  
`speech_adaptation_info` |  `[SpeechAdaptationInfo](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechAdaptationInfo)` Provides information on adaptation behavior in response  
`request_id` |  `int64` The ID associated with the request. This is a unique ID specific only to the given request.  
`using_legacy_models` |  `bool` Whether request used legacy asr models (was not automatically migrated to use conformer models).  
  
## SpeakerDiarizationConfig

Config to enable speaker diarization.

Fields  
---  
`enable_speaker_diarization` |  `bool` If 'true', enables speaker detection for each recognized word in the top alternative of the recognition result using a speaker_label provided in the WordInfo.  
`min_speaker_count` |  `int32` Minimum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 2.  
`max_speaker_count` |  `int32` Maximum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 6.  
`speaker_tag  
**(deprecated)**` |  `int32` This item is deprecated!Output only. Unused.  
  
## SpeechAdaptation

Speech adaptation configuration.

Fields  
---  
`phrase_sets[]` |  `[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet)` A collection of phrase sets. To specify the hints inline, leave the phrase set's `name` blank and fill in the rest of its fields. Any phrase set can use any custom class.  
`phrase_set_references[]` |  `string` A collection of phrase set resource names to use.  
`custom_classes[]` |  `[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass)` A collection of custom classes. To specify the classes inline, leave the class' `name` blank and fill in the rest of its fields, giving it a unique `custom_class_id`. Refer to the inline defined class in phrase hints by its `custom_class_id`.  
`abnf_grammar` |  `[ABNFGrammar](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechAdaptation.ABNFGrammar)` Augmented Backus-Naur form (ABNF) is a standardized grammar notation comprised by a set of derivation rules. See specifications: <https://www.w3.org/TR/speech-grammar>  
  
## ABNFGrammar

Fields  
---  
`abnf_strings[]` |  `string` All declarations and rules of an ABNF grammar broken up into multiple strings that will end up concatenated.  
  
## SpeechAdaptationInfo

Information on speech adaptation use in results

Fields  
---  
`adaptation_timeout` |  `bool` Whether there was a timeout when applying speech adaptation. If true, adaptation had no effect in the response transcript.  
`timeout_message` |  `string` If set, returns a message specifying which part of the speech adaptation request timed out.  
  
## SpeechContext

Provides "hints" to the speech recognizer to favor specific words and phrases in the results.

Fields  
---  
`phrases[]` |  `string` A list of strings containing words and phrases "hints" so that the speech recognition is more likely to recognize them. This can be used to improve the accuracy for specific words and phrases, for example, if specific commands are typically spoken by the user. This can also be used to add additional words to the vocabulary of the recognizer. See [usage limits](https://cloud.google.com/speech-to-text/quotas#content).List items can also be set to classes for groups of words that represent common concepts that occur in natural language. For example, rather than providing phrase hints for every month of the year, using the $MONTH class improves the likelihood of correctly transcribing audio that includes months.  
`boost` |  `float` Hint Boost. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost values would correspond to anti-biasing. Anti-biasing is not enabled, so negative boost will simply be ignored. Though `boost` can accept a wide range of positive values, most use cases are best served with values between 0 and 20. We recommend using a binary search approach to finding the optimal value for your use case.  
  
## SpeechRecognitionAlternative

Alternative hypotheses (a.k.a. n-best list).

Fields  
---  
`transcript` |  `string` Transcript text representing the words that the user spoke. In languages that use spaces to separate words, the transcript might have a leading space if it isn't the first result. You can concatenate each result to obtain the full transcript without using a separator.  
`confidence` |  `float` The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative of a non-streaming result or, of a streaming result where `is_final=true`. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating `confidence` was not set.  
`words[]` |  `[WordInfo](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.WordInfo)` A list of word-specific information for each recognized word. Note: When `enable_speaker_diarization` is true, you will see all the words from the beginning of the audio.  
  
## SpeechRecognitionResult

A speech recognition result corresponding to a portion of the audio.

Fields  
---  
`alternatives[]` |  `[SpeechRecognitionAlternative](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechRecognitionAlternative)` May contain one or more recognition hypotheses (up to the maximum specified in `max_alternatives`). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer.  
`channel_tag` |  `int32` For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For audio_channel_count = N, its output values can range from '1' to 'N'.  
`result_end_time` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Time offset of the end of this result relative to the beginning of the audio.  
`language_code` |  `string` Output only. The [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag of the language in this result. This language code was detected to have the most likelihood of being spoken in the audio.  
  
## StreamingRecognitionConfig

Provides information to the recognizer that specifies how to process the request.

Fields  
---  
`config` |  `[RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig)` Required. Provides information to the recognizer that specifies how to process the request.  
`single_utterance` |  `bool` If `false` or omitted, the recognizer will perform continuous recognition (continuing to wait for and process audio even if the user pauses speaking) until the client closes the input stream (gRPC API) or until the maximum time limit has been reached. May return multiple `StreamingRecognitionResult`s with the `is_final` flag set to `true`.If `true`, the recognizer will detect a single spoken utterance. When it detects that the user has paused or stopped speaking, it will return an `END_OF_SINGLE_UTTERANCE` event and cease recognition. It will return no more than one `StreamingRecognitionResult` with the `is_final` flag set to `true`.The `single_utterance` field can only be used with specified models, otherwise an error is thrown. The `model` field in `[RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.RecognitionConfig)` must be set to:

  * `command_and_search`
  * `phone_call` AND additional field `useEnhanced`=`true`
  * The `model` field is left undefined. In this case the API auto-selects a model based on any other parameters that you set in `RecognitionConfig`.

  
`interim_results` |  `bool` If `true`, interim results (tentative hypotheses) may be returned as they become available (these interim results are indicated with the `is_final=false` flag). If `false` or omitted, only `is_final=true` result(s) are returned.  
`enable_voice_activity_events` |  `bool` If `true`, responses with voice activity speech events will be returned as they are detected.  
`voice_activity_timeout` |  `[VoiceActivityTimeout](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognitionConfig.VoiceActivityTimeout)` If set, the server will automatically close the stream after the specified duration has elapsed after the last VOICE_ACTIVITY speech event has been sent. The field `voice_activity_events` must also be set to true.  
  
## VoiceActivityTimeout

Events that a timeout can be set on for voice activity.

Fields  
---  
`speech_start_timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Duration to timeout the stream if no speech begins.  
`speech_end_timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Duration to timeout the stream after speech ends.  
  
## StreamingRecognitionResult

A streaming speech recognition result corresponding to a portion of the audio that is currently being processed.

Fields  
---  
`alternatives[]` |  `[SpeechRecognitionAlternative](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechRecognitionAlternative)` May contain one or more recognition hypotheses (up to the maximum specified in `max_alternatives`). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer.  
`is_final` |  `bool` If `false`, this `StreamingRecognitionResult` represents an interim result that may change. If `true`, this is the final time the speech service will return this particular `StreamingRecognitionResult`, the recognizer will not return any further hypotheses for this portion of the transcript and corresponding audio.  
`stability` |  `float` An estimate of the likelihood that the recognizer will not change its guess about this interim result. Values range from 0.0 (completely unstable) to 1.0 (completely stable). This field is only provided for interim results (`is_final=false`). The default of 0.0 is a sentinel value indicating `stability` was not set.  
`result_end_time` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Time offset of the end of this result relative to the beginning of the audio.  
`channel_tag` |  `int32` For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For audio_channel_count = N, its output values can range from '1' to 'N'.  
`language_code` |  `string` Output only. The [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag of the language in this result. This language code was detected to have the most likelihood of being spoken in the audio.  
  
## StreamingRecognizeRequest

The top-level message sent by the client for the `StreamingRecognize` method. Multiple `StreamingRecognizeRequest` messages are sent. The first message must contain a `streaming_config` message and must not contain `audio_content`. All subsequent messages must contain `audio_content` and must not contain a `streaming_config` message.

Fields  
---  
Union field `streaming_request`. The streaming request, which is either a streaming config or audio content. `streaming_request` can be only one of the following:  
`streaming_config` |  `[StreamingRecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognitionConfig)` Provides information to the recognizer that specifies how to process the request. The first `StreamingRecognizeRequest` message must contain a `streaming_config` message.  
`audio_content` |  `bytes` The audio data to be recognized. Sequential chunks of audio data are sent in sequential `StreamingRecognizeRequest` messages. The first `StreamingRecognizeRequest` message must not contain `audio_content` data and all subsequent `StreamingRecognizeRequest` messages must contain `audio_content` data. The audio bytes must be encoded as specified in `RecognitionConfig`. Note: as with all bytes fields, proto buffers use a pure binary representation (not base64). See [content limits](https://cloud.google.com/speech-to-text/quotas#content).  
  
## StreamingRecognizeResponse

`StreamingRecognizeResponse` is the only message returned to the client by `StreamingRecognize`. A series of zero or more `StreamingRecognizeResponse` messages are streamed back to the client. If there is no recognizable audio, and `single_utterance` is set to false, then no messages are streamed back to the client.

Here's an example of a series of `StreamingRecognizeResponse`s that might be returned while processing audio:

  1. results { alternatives { transcript: "tube" } stability: 0.01 }

  2. results { alternatives { transcript: "to be a" } stability: 0.01 }

  3. results { alternatives { transcript: "to be" } stability: 0.9 } results { alternatives { transcript: " or not to be" } stability: 0.01 }

  4. results { alternatives { transcript: "to be or not to be" confidence: 0.92 } alternatives { transcript: "to bee or not to bee" } is_final: true }

  5. results { alternatives { transcript: " that's" } stability: 0.01 }

  6. results { alternatives { transcript: " that is" } stability: 0.9 } results { alternatives { transcript: " the question" } stability: 0.01 }

  7. results { alternatives { transcript: " that is the question" confidence: 0.98 } alternatives { transcript: " that was the question" } is_final: true }




Notes:

  * Only two of the above responses #4 and #7 contain final results; they are indicated by `is_final: true`. Concatenating these together generates the full transcript: "to be or not to be that is the question".

  * The others contain interim `results`. #3 and #6 contain two interim `results`: the first portion has a high stability and is less likely to change; the second portion has a low stability and is very likely to change. A UI designer might choose to show only high stability `results`.

  * The specific `stability` and `confidence` values shown above are only for illustrative purposes. Actual values may vary.

  * In each response, only one of these fields will be set: `error`, `speech_event_type`, or one or more (repeated) `results`.


Fields  
---  
`error` |  `[Status](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.rpc#google.rpc.Status)` If set, returns a `[google.rpc.Status](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.rpc#google.rpc.Status)` message that specifies the error for the operation.  
`results[]` |  `[StreamingRecognitionResult](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognitionResult)` This repeated list contains zero or more results that correspond to consecutive portions of the audio currently being processed. It contains zero or one `is_final=true` result (the newly settled portion), followed by zero or more `is_final=false` results (the interim results).  
`speech_event_type` |  `[SpeechEventType](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeResponse.SpeechEventType)` Indicates the type of speech event.  
`speech_event_time` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Time offset between the beginning of the audio and event emission.  
`total_billed_time` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` When available, billed audio seconds for the stream. Set only if this is the last response in the stream.  
`speech_adaptation_info` |  `[SpeechAdaptationInfo](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.SpeechAdaptationInfo)` Provides information on adaptation behavior in response  
`request_id` |  `int64` The ID associated with the request. This is a unique ID specific only to the given request.  
  
## SpeechEventType

Indicates the type of speech event.

Enums  
---  
`SPEECH_EVENT_UNSPECIFIED` | No speech event specified.  
`END_OF_SINGLE_UTTERANCE` | This event indicates that the server has detected the end of the user's speech utterance and expects no additional speech. Therefore, the server will not process additional audio (although it may subsequently return additional results). The client should stop sending additional audio data, half-close the gRPC connection, and wait for any additional results until the server closes the gRPC connection. This event is only sent if `single_utterance` was set to `true`, and is not used otherwise.  
`SPEECH_ACTIVITY_BEGIN` | This event indicates that the server has detected the beginning of human voice activity in the stream. This event can be returned multiple times if speech starts and stops repeatedly throughout the stream. This event is only sent if `voice_activity_events` is set to true.  
`SPEECH_ACTIVITY_END` | This event indicates that the server has detected the end of human voice activity in the stream. This event can be returned multiple times if speech starts and stops repeatedly throughout the stream. This event is only sent if `voice_activity_events` is set to true.  
`SPEECH_ACTIVITY_TIMEOUT` | This event indicates that the user-set timeout for speech activity begin or end has exceeded. Upon receiving this event, the client is expected to send a half close. Further audio will not be processed.  
  
## TranscriptNormalization

Transcription normalization configuration. Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing. For StreamingRecognize, this normalization only applies to stable partial transcripts (stability > 0.8) and final transcripts.

Fields  
---  
`entries[]` |  `[Entry](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.TranscriptNormalization.Entry)` A list of replacement entries. We will perform replacement with one entry at a time. For example, the second entry in ["cat" => "dog", "mountain cat" => "mountain dog"] will never be applied because we will always process the first entry before it. At most 100 entries.  
  
## Entry

A single replacement configuration.

Fields  
---  
`search` |  `string` What to replace. Max length is 100 characters.  
`replace` |  `string` What to replace with. Max length is 100 characters.  
`case_sensitive` |  `bool` Whether the search is case sensitive.  
  
## TranscriptOutputConfig

Specifies an optional destination for the recognition results.

Fields  
---  
Union field `output_type`.`output_type` can be only one of the following:  
`gcs_uri` |  `string` Specifies a Cloud Storage URI for the recognition results. Must be specified in the format: `gs://bucket_name/object_name`, and the bucket must already exist.  
  
## UpdateCustomClassRequest

Message sent by the client for the `UpdateCustomClass` method.

Fields  
---  
`custom_class` |  `[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.CustomClass)` Required. The custom class to update.The custom class's `name` field is used to identify the custom class to be updated. Format:`projects/{project}/locations/{location}/customClasses/{custom_class}`Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `customClass`:

  * `speech.customClasses.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The list of fields to be updated.  
  
## UpdatePhraseSetRequest

Message sent by the client for the `UpdatePhraseSet` method.

Fields  
---  
`phrase_set` |  `[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.PhraseSet)` Required. The phrase set to update.The phrase set's `name` field is used to identify the set to be updated. Format:`projects/{project}/locations/{location}/phraseSets/{phrase_set}`Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `phraseSet`:

  * `speech.phraseSets.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The list of fields to be updated.  
  
## WordInfo

Word-specific information for recognized words.

Fields  
---  
`start_time` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This field is only set if `enable_word_time_offsets=true` and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary.  
`end_time` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This field is only set if `enable_word_time_offsets=true` and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary.  
`word` |  `string` The word corresponding to this set of information.  
`confidence` |  `float` The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative of a non-streaming result or, of a streaming result where `is_final=true`. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating `confidence` was not set.  
`speaker_tag  
**(deprecated)**` |  `int32` This item is deprecated!Output only. A distinct integer value is assigned for every speaker within the audio. This field specifies which one of those speakers was detected to have spoken this word. Value ranges from '1' to diarization_speaker_count. speaker_tag is set if enable_speaker_diarization = 'true' and only for the top alternative. Note: Use speaker_label instead.  
`speaker_label` |  `string` Output only. A label value assigned for every unique speaker within the audio. This field specifies which speaker was detected to have spoken this word. For some models, like medical_conversation this can be actual speaker role, for example "patient" or "provider", but generally this would be a number identifying a speaker. This field is only set if enable_speaker_diarization = 'true' and only for the top alternative.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
