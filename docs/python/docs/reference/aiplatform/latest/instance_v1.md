---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/instance_v1/
title: Types for Google Cloud Aiplatform V1 Schema Predict Instance v1 API \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:11.555884+00:00
---

# Types for Google Cloud Aiplatform V1 Schema Predict Instance v1 API  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/instance_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Types for Google Cloud Aiplatform V1 Schema Predict Instance v1 API Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.ImageClassificationPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Image Classification.

#### content()

The image bytes or Cloud Storage URI to make the prediction on.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the content of the image. Only the images in below listed MIME types are supported.

  * image/jpeg
  * image/gif
  * image/png
  * image/webp
  * image/bmp
  * image/tiff
  * image/vnd.microsoft.icon

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.ImageObjectDetectionPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Image Object Detection.

#### content()

The image bytes or Cloud Storage URI to make the prediction on.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the content of the image. Only the images in below listed MIME types are supported.

  * image/jpeg
  * image/gif
  * image/png
  * image/webp
  * image/bmp
  * image/tiff
  * image/vnd.microsoft.icon

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.ImageSegmentationPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Image Segmentation.

#### content()

The image bytes to make the predictions on.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the content of the image. Only the images in below listed MIME types are supported.

  * image/jpeg
  * image/png

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.TextClassificationPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Text Classification.

#### content()

The text snippet to make the predictions on.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the text snippet. The supported MIME types are listed below.

  * text/plain

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.TextExtractionPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Text Extraction.

#### content()

The text snippet to make the predictions on.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the text snippet. The supported MIME types are listed below.

  * text/plain

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### key()

This field is only used for batch prediction. If a key is provided, the batch prediction result will by mapped to this key. If omitted, then the batch prediction result will contain the entire input instance. Vertex AI will not check if keys in the request are duplicates, so it is up to the caller to ensure the keys are unique.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### key(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.TextSentimentPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Text Sentiment.

#### content()

The text snippet to make the predictions on.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the text snippet. The supported MIME types are listed below.

  * text/plain

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.VideoActionRecognitionPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Video Action Recognition.

#### content()

The Google Cloud Storage location of the video on which to perform the prediction.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the content of the video. Only the following are supported: video/mp4 video/avi video/quicktime

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_start()

The beginning, inclusive, of the video’s time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with “s” appended at the end. Fractions are allowed, up to a microsecond precision.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_end()

The end, exclusive, of the video’s time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with “s” appended at the end. Fractions are allowed, up to a microsecond precision, and “inf” or “Infinity” is allowed, which means the end of the video.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_end(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_start(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.VideoClassificationPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Video Classification.

#### content()

The Google Cloud Storage location of the video on which to perform the prediction.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the content of the video. Only the following are supported: video/mp4 video/avi video/quicktime

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_start()

The beginning, inclusive, of the video’s time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with “s” appended at the end. Fractions are allowed, up to a microsecond precision.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_end()

The end, exclusive, of the video’s time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with “s” appended at the end. Fractions are allowed, up to a microsecond precision, and “inf” or “Infinity” is allowed, which means the end of the video.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_end(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_start(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1.schema.predict.instance_v1.types.VideoObjectTrackingPredictionInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Prediction input format for Video Object Tracking.

#### content()

The Google Cloud Storage location of the video on which to perform the prediction.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### mime_type()

The MIME type of the content of the video. Only the following are supported: video/mp4 video/avi video/quicktime

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_start()

The beginning, inclusive, of the video’s time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with “s” appended at the end. Fractions are allowed, up to a microsecond precision.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_segment_end()

The end, exclusive, of the video’s time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with “s” appended at the end. Fractions are allowed, up to a microsecond precision, and “inf” or “Infinity” is allowed, which means the end of the video.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### content(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### mime_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_end(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_segment_start(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
