---
url: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognizeRequest
title: Class RecognizeRequest (2.41.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:42.497412+00:00
---

# Class RecognizeRequest (2.41.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognizeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RecognizeRequest (2.41.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.41.0 (latest)  2.40.0  2.39.0  2.38.0  2.37.0  2.36.1  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.1  2.25.1  2.24.1  2.23.0  2.22.0  2.21.1  2.20.1  2.19.0  2.18.0  2.17.3  2.16.2  2.15.1  2.14.1  2.13.1  2.12.0  2.11.1  2.10.0  2.9.3  2.8.0  2.7.0  2.6.0  2.5.1  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.4  1.2.0  1.1.0 
    
    
    RecognizeRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for the Recognize method. Either `content` or `uri` must be supplied. Supplying both or neither returns `INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]`. See `content limits <https://cloud.google.com/speech-to-text/quotas#content>`__.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`recognizer` |  `str`   
Required. The name of the Recognizer to use during recognition. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`. The {recognizer} segment may be set to `_` to use an empty implicit Recognizer.   
`config` |  `[google.cloud.speech_v2.types.RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionConfig)`   
Features and audio metadata to use for the Automatic Speech Recognition. This field in combination with the config_mask field can be used to override parts of the default_recognition_config of the Recognizer resource.   
`config_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields in config that override the values in the default_recognition_config of the recognizer during this recognition request. If no mask is provided, all non-default valued fields in config override the values in the recognizer for this recognition request. If a mask is provided, only the fields listed in the mask override the config in the recognizer for this recognition request. If a wildcard (`*`) is provided, config completely overrides and replaces the config in the recognizer for this recognition request.   
`content` |  `bytes`   
The audio data bytes encoded as specified in RecognitionConfig. As with all bytes fields, proto buffers use a pure binary representation, whereas JSON representations use base64. This field is a member of `oneof`_ `audio_source`.   
`uri` |  `str`   
URI that points to a file that contains audio data bytes as specified in RecognitionConfig. The file must not be compressed (for example, gzip). Currently, only Google Cloud Storage URIs are supported, which must be specified in the following format: `gs://bucket_name/object_name` (other URI formats return `INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]`). For more information, see `Request URIs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
