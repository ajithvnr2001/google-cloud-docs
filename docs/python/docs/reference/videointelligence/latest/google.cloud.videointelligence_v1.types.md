---
url: https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types
title: Package types (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:19.597236+00:00
---

# Package types (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.2  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.1  2.6.1  2.5.1  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.16.3  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0 

API documentation for `videointelligence_v1.types` package.

## Classes 

### [AnnotateVideoProgress](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.AnnotateVideoProgress)

Video annotation progress. Included in the `metadata` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

### [AnnotateVideoRequest](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.AnnotateVideoRequest)

Video annotation request.

### [AnnotateVideoResponse](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.AnnotateVideoResponse)

Video annotation response. Included in the `response` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

### [DetectedAttribute](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.DetectedAttribute)

A generic detected attribute represented by name in string format.

### [DetectedLandmark](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.DetectedLandmark)

A generic detected landmark represented by name in string format and a 2D location.

### [Entity](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Entity)

Detected entity from video analysis.

### [ExplicitContentAnnotation](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.ExplicitContentAnnotation)

Explicit content annotation (based on per-frame visual signals only). If no explicit content has been detected in a frame, no annotations are present for that frame.

### [ExplicitContentDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.ExplicitContentDetectionConfig)

Config for EXPLICIT_CONTENT_DETECTION.

### [ExplicitContentFrame](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.ExplicitContentFrame)

Video frame level annotation results for explicit content.

### [FaceAnnotation](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.FaceAnnotation)

Deprecated. No effect.

### [FaceDetectionAnnotation](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.FaceDetectionAnnotation)

Face detection annotation.

### [FaceDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.FaceDetectionConfig)

Config for FACE_DETECTION.

### [FaceFrame](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.FaceFrame)

Deprecated. No effect.

### [FaceSegment](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.FaceSegment)

Video segment level annotation results for face detection.

### [Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature)

Video annotation feature.

### [LabelAnnotation](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.LabelAnnotation)

Label annotation.

### [LabelDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.LabelDetectionConfig)

Config for LABEL_DETECTION.

### [LabelDetectionMode](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.LabelDetectionMode)

Label detection mode.

### [LabelFrame](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.LabelFrame)

Video frame level annotation results for label detection.

### [LabelSegment](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.LabelSegment)

Video segment level annotation results for label detection.

### [Likelihood](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Likelihood)

Bucketized representation of likelihood.

### [LogoRecognitionAnnotation](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.LogoRecognitionAnnotation)

Annotation corresponding to one detected, tracked and recognized logo class.

### [NormalizedBoundingBox](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.NormalizedBoundingBox)

Normalized bounding box. The normalized vertex coordinates are relative to the original image. Range: [0, 1].

### [NormalizedBoundingPoly](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.NormalizedBoundingPoly)

Normalized bounding polygon for text (that might not be aligned with axis). Contains list of the corner points in clockwise order starting from top-left corner. For example, for a rectangular bounding box: When the text is horizontal it might look like: 0----1 | | 3----2

When it's clockwise rotated 180 degrees around the top-left corner it becomes: 2----3 | | 1----0

and the vertex order will still be (0, 1, 2, 3). Note that values can be less than 0, or greater than 1 due to trignometric calculations for location of the box.

### [NormalizedVertex](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.NormalizedVertex)

A vertex represents a 2D point in the image. NOTE: the normalized vertex coordinates are relative to the original image and range from 0 to 1.

### [ObjectTrackingAnnotation](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.ObjectTrackingAnnotation)

Annotations corresponding to one tracked object.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ObjectTrackingConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.ObjectTrackingConfig)

Config for OBJECT_TRACKING.

### [ObjectTrackingFrame](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.ObjectTrackingFrame)

Video frame level annotations for object detection and tracking. This field stores per frame location, time offset, and confidence.

### [PersonDetectionAnnotation](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.PersonDetectionAnnotation)

Person detection annotation per video.

### [PersonDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.PersonDetectionConfig)

Config for PERSON_DETECTION.

### [ShotChangeDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.ShotChangeDetectionConfig)

Config for SHOT_CHANGE_DETECTION.

### [SpeechContext](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.SpeechContext)

Provides "hints" to the speech recognizer to favor specific words and phrases in the results.

### [SpeechRecognitionAlternative](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.SpeechRecognitionAlternative)

Alternative hypotheses (a.k.a. n-best list).

### [SpeechTranscription](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.SpeechTranscription)

A speech recognition result corresponding to a portion of the audio.

### [SpeechTranscriptionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.SpeechTranscriptionConfig)

Config for SPEECH_TRANSCRIPTION.

### [TextAnnotation](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.TextAnnotation)

Annotations related to one detected OCR text snippet. This will contain the corresponding text, confidence value, and frame level information for each detection.

### [TextDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.TextDetectionConfig)

Config for TEXT_DETECTION.

### [TextFrame](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.TextFrame)

Video frame level annotation results for text annotation (OCR). Contains information regarding timestamp and bounding box locations for the frames containing detected OCR text snippets.

### [TextSegment](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.TextSegment)

Video segment level annotation results for text detection.

### [TimestampedObject](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.TimestampedObject)

For tracking related features. An object at time_offset with attributes, and located with normalized_bounding_box.

### [Track](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Track)

A track of an object instance.

### [VideoAnnotationProgress](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.VideoAnnotationProgress)

Annotation progress for a single video.

### [VideoAnnotationResults](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.VideoAnnotationResults)

Annotation results for a single video.

### [VideoContext](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.VideoContext)

Video context and/or feature-specific parameters.

### [VideoSegment](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.VideoSegment)

Video segment.

### [WordInfo](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.WordInfo)

Word-specific information for recognized words. Word information is only included in the response when certain request parameters are set, such as `enable_word_time_offsets`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
