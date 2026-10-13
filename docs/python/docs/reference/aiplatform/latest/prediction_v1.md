---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/prediction_v1/
title: Types for Google Cloud Aiplatform V1 Schema Predict Prediction v1 API \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:13.203314+00:00
---

# Types for Google Cloud Aiplatform V1 Schema Predict Prediction v1 API  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/prediction_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Types for Google Cloud Aiplatform V1 Schema Predict Prediction v1 API Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.ClassificationPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Image and Text Classification.

#### ids()

The resource IDs of the AnnotationSpecs that had been identified.

  * **Type**

MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)]




#### display_names()

The display names of the AnnotationSpecs that had been identified, order matches the IDs.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### confidences()

The Model’s confidences in correctness of the predicted IDs, higher value means higher confidence. Order matches the Ids.

  * **Type**

MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)]




#### confidences(_: MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)_ )

#### display_names(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### ids(_: MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.ImageObjectDetectionPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Image Object Detection.

#### ids()

The resource IDs of the AnnotationSpecs that had been identified, ordered by the confidence score descendingly.

  * **Type**

MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)]




#### display_names()

The display names of the AnnotationSpecs that had been identified, order matches the IDs.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### confidences()

The Model’s confidences in correctness of the predicted IDs, higher value means higher confidence. Order matches the Ids.

  * **Type**

MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)]




#### bboxes()

Bounding boxes, i.e. the rectangles over the image, that pinpoint the found AnnotationSpecs. Given in order that matches the IDs. Each bounding box is an array of 4 numbers `xMin`, `xMax`, `yMin`, and `yMax`, which represent the extremal coordinates of the box. They are relative to the image size, and the point 0,0 is in the top left of the image.

  * **Type**

MutableSequence[[google.protobuf.struct_pb2.ListValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/struct_pb2.html#google.protobuf.struct_pb2.ListValue)]




#### bboxes(_: MutableSequence[[google.protobuf.struct_pb2.ListValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/struct_pb2.html#google.protobuf.struct_pb2.ListValue)_ )

#### confidences(_: MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)_ )

#### display_names(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### ids(_: MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.ImageSegmentationPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Image Segmentation.

#### category_mask()

A PNG image where each pixel in the mask represents the category in which the pixel in the original image was predicted to belong to. The size of this image will be the same as the original image. The mapping between the AnntoationSpec and the color can be found in model’s metadata. The model will choose the most likely category and if none of the categories reach the confidence threshold, the pixel will be marked as background.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### confidence_mask()

A one channel image which is encoded as an 8bit lossless PNG. The size of the image will be the same as the original image. For a specific pixel, darker color means less confidence in correctness of the cateogry in the categoryMask for the corresponding pixel. Black means no confidence and white means complete confidence.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### category_mask(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### confidence_mask(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.TabularClassificationPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Tabular Classification.

#### classes()

The name of the classes being classified, contains all possible values of the target column.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### scores()

The model’s confidence in each class being correct, higher value means higher confidence. The N-th score corresponds to the N-th class in classes.

  * **Type**

MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)]




#### classes(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### scores(_: MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.TabularRegressionPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Tabular Regression.

#### value()

The regression value.

  * **Type**

[float](https://docs.python.org/3/builtins/functions.html#float)




#### lower_bound()

The lower bound of the prediction interval.

  * **Type**

[float](https://docs.python.org/3/builtins/functions.html#float)




#### upper_bound()

The upper bound of the prediction interval.

  * **Type**

[float](https://docs.python.org/3/builtins/functions.html#float)




#### lower_bound(_: [float](<https://docs.python.org/3/builtins/functions.html#float>_ )

#### upper_bound(_: [float](<https://docs.python.org/3/builtins/functions.html#float>_ )

#### value(_: [float](<https://docs.python.org/3/builtins/functions.html#float>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.TextExtractionPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Text Extraction.

#### ids()

The resource IDs of the AnnotationSpecs that had been identified, ordered by the confidence score descendingly.

  * **Type**

MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)]




#### display_names()

The display names of the AnnotationSpecs that had been identified, order matches the IDs.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### text_segment_start_offsets()

The start offsets, inclusive, of the text segment in which the AnnotationSpec has been identified. Expressed as a zero-based number of characters as measured from the start of the text snippet.

  * **Type**

MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)]




#### text_segment_end_offsets()

The end offsets, inclusive, of the text segment in which the AnnotationSpec has been identified. Expressed as a zero-based number of characters as measured from the start of the text snippet.

  * **Type**

MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)]




#### confidences()

The Model’s confidences in correctness of the predicted IDs, higher value means higher confidence. Order matches the Ids.

  * **Type**

MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)]




#### confidences(_: MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)_ )

#### display_names(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### ids(_: MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)_ )

#### text_segment_end_offsets(_: MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)_ )

#### text_segment_start_offsets(_: MutableSequence[[int](https://docs.python.org/3/builtins/functions.html#int)_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.TextSentimentPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Text Sentiment

#### sentiment()

The integer sentiment labels between 0 (inclusive) and sentimentMax label (inclusive), while 0 maps to the least positive sentiment and sentimentMax maps to the most positive one. The higher the score is, the more positive the sentiment in the text snippet is. Note: sentimentMax is an integer value between 1 (inclusive) and 10 (inclusive).

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### sentiment(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.VideoActionRecognitionPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Video Action Recognition.

#### id()

The resource ID of the AnnotationSpec that had been identified.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### display_name()

The display name of the AnnotationSpec that had been identified.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_start()

The beginning, inclusive, of the video’s time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with “s” appended at the end.

  * **Type**

[google.protobuf.duration_pb2.Duration](https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration)




#### time_segment_end()

The end, exclusive, of the video’s time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with “s” appended at the end.

  * **Type**

[google.protobuf.duration_pb2.Duration](https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration)




#### confidence()

The Model’s confidence in correction of this prediction, higher value means higher confidence.

  * **Type**

[google.protobuf.wrappers_pb2.FloatValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue)




#### confidence(_: [google.protobuf.wrappers_pb2.FloatValue](<https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue>_ )

#### display_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### id(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_end(_: [google.protobuf.duration_pb2.Duration](<https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration>_ )

#### time_segment_start(_: [google.protobuf.duration_pb2.Duration](<https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.VideoClassificationPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Video Classification.

#### id()

The resource ID of the AnnotationSpec that had been identified.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### display_name()

The display name of the AnnotationSpec that had been identified.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### type_()

The type of the prediction. The requested types can be configured via parameters. This will be one of

  * segment-classification
  * shot-classification
  * one-sec-interval-classification

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_start()

The beginning, inclusive, of the video’s time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with “s” appended at the end. Note that for ‘segment-classification’ prediction type, this equals the original ‘timeSegmentStart’ from the input instance, for other types it is the start of a shot or a 1 second interval respectively.

  * **Type**

[google.protobuf.duration_pb2.Duration](https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration)




#### time_segment_end()

The end, exclusive, of the video’s time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with “s” appended at the end. Note that for ‘segment-classification’ prediction type, this equals the original ‘timeSegmentEnd’ from the input instance, for other types it is the end of a shot or a 1 second interval respectively.

  * **Type**

[google.protobuf.duration_pb2.Duration](https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration)




#### confidence()

The Model’s confidence in correction of this prediction, higher value means higher confidence.

  * **Type**

[google.protobuf.wrappers_pb2.FloatValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue)




#### confidence(_: [google.protobuf.wrappers_pb2.FloatValue](<https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue>_ )

#### display_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### id(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_end(_: [google.protobuf.duration_pb2.Duration](<https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration>_ )

#### time_segment_start(_: [google.protobuf.duration_pb2.Duration](<https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration>_ )

#### type_(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.VideoObjectTrackingPredictionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction output format for Video Object Tracking.

#### id()

The resource ID of the AnnotationSpec that had been identified.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### display_name()

The display name of the AnnotationSpec that had been identified.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_start()

The beginning, inclusive, of the video’s time segment in which the object instance has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with “s” appended at the end.

  * **Type**

[google.protobuf.duration_pb2.Duration](https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration)




#### time_segment_end()

The end, inclusive, of the video’s time segment in which the object instance has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with “s” appended at the end.

  * **Type**

[google.protobuf.duration_pb2.Duration](https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration)




#### confidence()

The Model’s confidence in correction of this prediction, higher value means higher confidence.

  * **Type**

[google.protobuf.wrappers_pb2.FloatValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue)




#### frames()

All of the frames of the video in which a single object instance has been detected. The bounding boxes in the frames identify the same object.

  * **Type**

MutableSequence[[google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.VideoObjectTrackingPredictionResult.Frame](https://docs.cloud.google.com/python/docs/reference/aiplatform/prediction_v1/types_.md#google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.VideoObjectTrackingPredictionResult.Frame)]




#### _class_ Frame(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

The fields `xMin`, `xMax`, `yMin`, and `yMax` refer to a bounding box, i.e. the rectangle over the video frame pinpointing the found AnnotationSpec. The coordinates are relative to the frame size, and the point 0,0 is in the top left of the frame.

#### time_offset()

A time (frame) of a video in which the object has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with “s” appended at the end.

  * **Type**

[google.protobuf.duration_pb2.Duration](https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration)




#### x_min()

The leftmost coordinate of the bounding box.

  * **Type**

[google.protobuf.wrappers_pb2.FloatValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue)




#### x_max()

The rightmost coordinate of the bounding box.

  * **Type**

[google.protobuf.wrappers_pb2.FloatValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue)




#### y_min()

The topmost coordinate of the bounding box.

  * **Type**

[google.protobuf.wrappers_pb2.FloatValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue)




#### y_max()

The bottommost coordinate of the bounding box.

  * **Type**

[google.protobuf.wrappers_pb2.FloatValue](https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue)




#### time_offset(_: [google.protobuf.duration_pb2.Duration](<https://googleapis.dev/python/protobuf/latest/google/protobuf/duration_pb2.html#google.protobuf.duration_pb2.Duration>_ )

#### x_max(_: [google.protobuf.wrappers_pb2.FloatValue](<https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue>_ )

#### x_min(_: [google.protobuf.wrappers_pb2.FloatValue](<https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue>_ )

#### y_max(_: [google.protobuf.wrappers_pb2.FloatValue](<https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue>_ )

#### y_min(_: [google.protobuf.wrappers_pb2.FloatValue](<https://googleapis.dev/python/protobuf/latest/google/protobuf/wrappers_pb2.html#google.protobuf.wrappers_pb2.FloatValue>_ )

#### confidence(_: wrappers_pb2.FloatValu_ )

#### display_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### frames(_: MutableSequence[[Frame](../prediction_v1/types_.md#google.cloud.aiplatform.v1.schema.predict.prediction_v1.types.VideoObjectTrackingPredictionResult.Frame)_ )

#### id(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_end(_: duration_pb2.Duratio_ )

#### time_segment_start(_: duration_pb2.Duratio_ )

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
