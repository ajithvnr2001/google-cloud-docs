---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/summary_class/
title: Package Classes (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:16.172367+00:00
---

# Package Classes (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 

Summary of entries of Classes for automl.

## Classes 

### [AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient)

AutoML Server API.

The resource names are assigned by the server. The server never reuses names that it has created after the resources with those names are deleted.

An ID of a resource is the last element of the item's resource name. For `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then the id for the item is `{dataset_id}`.

Currently the only supported `location_id` is "us-central1".

On any input that is documented to expect a string parameter in snake_case or dash-case, either of those cases is accepted.

### [AutoMlClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient)

AutoML Server API.

The resource names are assigned by the server. The server never reuses names that it has created after the resources with those names are deleted.

An ID of a resource is the last element of the item's resource name. For `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then the id for the item is `{dataset_id}`.

Currently the only supported `location_id` is "us-central1".

On any input that is documented to expect a string parameter in snake_case or dash-case, either of those cases is accepted.

### [ListDatasetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsAsyncPager)

A pager for iterating through `list_datasets` requests.

This class thinly wraps an initial [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListDatasetsResponse) object, and provides an `__aiter__` method to iterate through its `datasets` field.

If there are more pages, the `__aiter__` method will make additional `ListDatasets` requests and continue to iterate through the `datasets` field on the corresponding responses.

All the usual [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListDatasetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatasetsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsPager)

A pager for iterating through `list_datasets` requests.

This class thinly wraps an initial [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListDatasetsResponse) object, and provides an `__iter__` method to iterate through its `datasets` field.

If there are more pages, the `__iter__` method will make additional `ListDatasets` requests and continue to iterate through the `datasets` field on the corresponding responses.

All the usual [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListDatasetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager)

A pager for iterating through `list_model_evaluations` requests.

This class thinly wraps an initial [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelEvaluationsResponse) object, and provides an `__aiter__` method to iterate through its `model_evaluation` field.

If there are more pages, the `__aiter__` method will make additional `ListModelEvaluations` requests and continue to iterate through the `model_evaluation` field on the corresponding responses.

All the usual [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelEvaluationsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsPager)

A pager for iterating through `list_model_evaluations` requests.

This class thinly wraps an initial [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelEvaluationsResponse) object, and provides an `__iter__` method to iterate through its `model_evaluation` field.

If there are more pages, the `__iter__` method will make additional `ListModelEvaluations` requests and continue to iterate through the `model_evaluation` field on the corresponding responses.

All the usual [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListModelsAsyncPager)

A pager for iterating through `list_models` requests.

This class thinly wraps an initial [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelsResponse) object, and provides an `__aiter__` method to iterate through its `model` field.

If there are more pages, the `__aiter__` method will make additional `ListModels` requests and continue to iterate through the `model` field on the corresponding responses.

All the usual [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListModelsPager)

A pager for iterating through `list_models` requests.

This class thinly wraps an initial [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelsResponse) object, and provides an `__iter__` method to iterate through its `model` field.

If there are more pages, the `__iter__` method will make additional `ListModels` requests and continue to iterate through the `model` field on the corresponding responses.

All the usual [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [PredictionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient)

AutoML Prediction API.

On any input that is documented to expect a string parameter in snake_case or dash-case, either of those cases is accepted.

### [PredictionServiceClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient)

AutoML Prediction API.

On any input that is documented to expect a string parameter in snake_case or dash-case, either of those cases is accepted.

### [AnnotationPayload](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.AnnotationPayload)

Contains annotation information that is relevant to AutoML.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotationSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.AnnotationSpec)

A definition of an annotation spec.

### [BatchPredictInputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictInputConfig)

Input configuration for BatchPredict Action.

The format of input depends on the ML problem of the model used for prediction. As input source the gcs_source is expected, unless specified otherwise.

The formats are represented in EBNF with commas being literal and with non-terminal symbols defined near the end of this comment. The formats are:

AutoML Vision ^^^^^^^^^^^^^

Classification ''''''''''''''

One or more CSV files where each line is a single column:

::
    
    
    GCS_FILE_PATH
    

The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. This path is treated as the ID in the batch predict output.

Sample rows:

::
    
    
    gs://folder/image1.jpeg
    gs://folder/image2.gif
    gs://folder/image3.png
    

Object Detection ''''''''''''''''

One or more CSV files where each line is a single column:

::
    
    
    GCS_FILE_PATH
    

The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. This path is treated as the ID in the batch predict output.

Sample rows:

::
    
    
    gs://folder/image1.jpeg
    gs://folder/image2.gif
    gs://folder/image3.png
    

AutoML Video Intelligence ^^^^^^^^^^^^^^^^^^^^^^^^^

Classification ''''''''''''''

One or more CSV files where each line is a single column:

::
    
    
    GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END
    

`GCS_FILE_PATH` is the Google Cloud Storage location of video up to 50GB in size and up to 3h in duration duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI.

`TIME_SEGMENT_START` and `TIME_SEGMENT_END` must be within the length of the video, and the end time must be after the start time.

Sample rows:

::
    
    
    gs://folder/video1.mp4,10,40
    gs://folder/video1.mp4,20,60
    gs://folder/vid2.mov,0,inf
    

Object Tracking '''''''''''''''

One or more CSV files where each line is a single column:

::
    
    
    GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END
    

`GCS_FILE_PATH` is the Google Cloud Storage location of video up to 50GB in size and up to 3h in duration duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI.

`TIME_SEGMENT_START` and `TIME_SEGMENT_END` must be within the length of the video, and the end time must be after the start time.

Sample rows:

::
    
    
    gs://folder/video1.mp4,10,40
    gs://folder/video1.mp4,20,60
    gs://folder/vid2.mov,0,inf
    

AutoML Natural Language ^^^^^^^^^^^^^^^^^^^^^^^

Classification ''''''''''''''

One or more CSV files where each line is a single column:

::
    
    
    GCS_FILE_PATH
    

`GCS_FILE_PATH` is the Google Cloud Storage location of a text file. Supported file extensions: .TXT, .PDF, .TIF, .TIFF

Text files can be no larger than 10MB in size.

Sample rows:

::
    
    
    gs://folder/text1.txt
    gs://folder/text2.pdf
    gs://folder/text3.tif
    

Sentiment Analysis ''''''''''''''''''

One or more CSV files where each line is a single column:

::
    
    
    GCS_FILE_PATH
    

`GCS_FILE_PATH` is the Google Cloud Storage location of a text file. Supported file extensions: .TXT, .PDF, .TIF, .TIFF

Text files can be no larger than 128kB in size.

Sample rows:

::
    
    
    gs://folder/text1.txt
    gs://folder/text2.pdf
    gs://folder/text3.tif
    

Entity Extraction '''''''''''''''''

One or more JSONL (JSON Lines) files that either provide inline text or documents. You can only use one format, either inline text or documents, for a single call to [AutoMl.BatchPredict].

Each JSONL file contains a per line a proto that wraps a temporary user-assigned TextSnippet ID (string up to 2000 characters long) called "id", a TextSnippet proto (in JSON representation) and zero or more TextFeature protos. Any given text snippet content must have 30,000 characters or less, and also be UTF-8 NFC encoded (ASCII already is). The IDs provided should be unique.

Each document JSONL file contains, per line, a proto that wraps a Document proto with `input_config` set. Each document cannot exceed 2MB in size.

Supported document extensions: .PDF, .TIF, .TIFF

Each JSONL file must not exceed 100MB in size, and no more than 20 JSONL files may be passed.

Sample inline JSONL file (Shown with artificial line breaks. Actual line breaks are denoted by "\n".):

::
    
    
    {
       "id": "my_first_id",
       "text_snippet": { "content": "dog car cat"},
       "text_features": [
         {
           "text_segment": {"start_offset": 4, "end_offset": 6},
           "structural_type": PARAGRAPH,
           "bounding_poly": {
             "normalized_vertices": [
               {"x": 0.1, "y": 0.1},
               {"x": 0.1, "y": 0.3},
               {"x": 0.3, "y": 0.3},
               {"x": 0.3, "y": 0.1},
             ]
           },
         }
       ],
     }\n
     {
       "id": "2",
       "text_snippet": {
         "content": "Extended sample content",
         "mime_type": "text/plain"
       }
     }
    

Sample document JSONL file (Shown with artificial line breaks. Actual line breaks are denoted by "\n".):

::
    
    
     {
       "document": {
         "input_config": {
           "gcs_source": { "input_uris": [ "gs://folder/document1.pdf" ]
           }
         }
       }
     }\n
     {
       "document": {
         "input_config": {
           "gcs_source": { "input_uris": [ "gs://folder/document2.tif" ]
           }
         }
       }
     }
    

AutoML Tables ^^^^^^^^^^^^^

See `Preparing your training data <https://cloud.google.com/automl-tables/docs/predict-batch>`__ for more information.

You can use either gcs_source or `bigquery_source][BatchPredictInputConfig.bigquery_source]`.

**For gcs_source:**

CSV file(s), each by itself 10GB or smaller and total size must be 100GB or smaller, where first file must have a header containing column names. If the first row of a subsequent file is the same as the header, then it is also treated as a header. All other rows contain values for the corresponding columns.

The column names must contain the model's [input_feature_column_specs'][google.cloud.automl.v1.TablesModelMetadata.input_feature_column_specs] display_name-s (order doesn't matter). The columns corresponding to the model's input feature column specs must contain values compatible with the column spec's data types. Prediction on all the rows, i.e. the CSV lines, will be attempted.

Sample rows from a CSV file:

.. raw:: html
    
    
    <pre>
    "First Name","Last Name","Dob","Addresses"
    "John","Doe","1968-01-22","[{"status":"current","address":"123_First_Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456_Main_Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]"
    "Jane","Doe","1980-10-16","[{"status":"current","address":"789_Any_Avenue","city":"Albany","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321_Main_Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]}
    </pre>
    

**For bigquery_source:**

The URI of a BigQuery table. The user data size of the BigQuery table must be 100GB or smaller.

The column names must contain the model's [input_feature_column_specs'][google.cloud.automl.v1.TablesModelMetadata.input_feature_column_specs] display_name-s (order doesn't matter). The columns corresponding to the model's input feature column specs must contain values compatible with the column spec's data types. Prediction on all the rows of the table will be attempted.

**Input field definitions:**

`GCS_FILE_PATH` : The path to a file on Google Cloud Storage. For example, "gs://folder/video.avi".

`TIME_SEGMENT_START` : (`TIME_OFFSET`) Expresses a beginning, inclusive, of a time segment within an example that has a time dimension (e.g. video).

`TIME_SEGMENT_END` : (`TIME_OFFSET`) Expresses an end, exclusive, of a time segment within n example that has a time dimension (e.g. video).

`TIME_OFFSET` : A number of seconds as measured from the start of an example (e.g. video). Fractions are allowed, up to a microsecond precision. "inf" is allowed, and it means the end of the example.

**Errors:**

If any of the provided CSV files can't be parsed or if more than certain percent of CSV rows cannot be processed then the operation fails and prediction does not happen. Regardless of overall success or failure the per-row failures, up to a certain count cap, will be listed in Operation.metadata.partial_failures.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchPredictOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictOperationMetadata)

Details of BatchPredict operation.

### [BatchPredictOutputInfo](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictOperationMetadata.BatchPredictOutputInfo)

Further describes this batch predict's output. Supplements BatchPredictOutputConfig.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchPredictOutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictOutputConfig)

Output configuration for BatchPredict Action.

As destination the gcs_destination must be set unless specified otherwise for a domain. If gcs_destination is set then in the given directory a new directory is created. Its name will be "prediction--", where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. The contents of it depends on the ML problem the predictions are made for.

  * For Image Classification: In the created directory files `image_classification_1.jsonl`, `image_classification_2.jsonl`,...,\ `image_classification_N.jsonl` will be created, where N may be 1, and depends on the total number of the successfully predicted images and annotations. A single image will be listed only once with all its annotations, and its annotations will never be split across files. Each .JSONL file will contain, per line, a JSON representation of a proto that wraps image's "ID" : "<id_value>" followed by a list of zero or more AnnotationPayload protos (called annotations), which have classification detail populated. If prediction for any image failed (partially or completely), then an additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps the same "ID" : "<id_value>" but here followed by exactly one ``google.rpc.Status` <https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto>`__ containing only`code`and`message`\ fields.

  * For Image Object Detection: In the created directory files `image_object_detection_1.jsonl`, `image_object_detection_2.jsonl`,...,\ `image_object_detection_N.jsonl` will be created, where N may be 1, and depends on the total number of the successfully predicted images and annotations. Each .JSONL file will contain, per line, a JSON representation of a proto that wraps image's "ID" : "<id_value>" followed by a list of zero or more AnnotationPayload protos (called annotations), which have image_object_detection detail populated. A single image will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any image failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps the same "ID" : "<id_value>" but here followed by exactly one ``google.rpc.Status` <https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto>`__ containing only`code`and`message`\ fields.

  * For Video Classification: In the created directory a video_classification.csv file, and a .JSON file per each video classification requested in the input (i.e. each line in given CSV(s)), will be created.

::

The format of video_classification.csv is: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END,JSON_FILE_NAME,STATUS where: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END = matches 1 to 1 the prediction input lines (i.e. video_classification.csv has precisely the same number of lines as the prediction input had.) JSON_FILE_NAME = Name of .JSON file in the output directory, which contains prediction responses for the video time segment. STATUS = "OK" if prediction completed successfully, or an error code with message otherwise. If STATUS is not "OK" then the .JSON file for that line may not exist or be empty.

Each .JSON file, assuming STATUS is "OK", will contain a list of AnnotationPayload protos in JSON format, which are the predictions for the video time segment the file is assigned to in the video_classification.csv. All AnnotationPayload protos will have video_classification field set, and will be sorted by video_classification.type field (note that the returned types are governed by `classifaction_types` parameter in [PredictService.BatchPredictRequest.params][]).

  * For Video Object Tracking: In the created directory a video_object_tracking.csv file will be created, and multiple files video_object_trackinng_1.json, video_object_trackinng_2.json,..., video_object_trackinng_N.json, where N is the number of requests in the input (i.e. the number of lines in given CSV(s)).

::

The format of video_object_tracking.csv is: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END,JSON_FILE_NAME,STATUS where: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END = matches 1 to 1 the prediction input lines (i.e. video_object_tracking.csv has precisely the same number of lines as the prediction input had.) JSON_FILE_NAME = Name of .JSON file in the output directory, which contains prediction responses for the video time segment. STATUS = "OK" if prediction completed successfully, or an error code with message otherwise. If STATUS is not "OK" then the .JSON file for that line may not exist or be empty.

Each .JSON file, assuming STATUS is "OK", will contain a list of AnnotationPayload protos in JSON format, which are the predictions for each frame of the video time segment the file is assigned to in video_object_tracking.csv. All AnnotationPayload protos will have video_object_tracking field set.

  * For Text Classification: In the created directory files `text_classification_1.jsonl`, `text_classification_2.jsonl`,...,\ `text_classification_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found.

::

Each .JSONL file will contain, per line, a JSON representation of a proto that wraps input text file (or document) in the text snippet (or document) proto and a list of zero or more AnnotationPayload protos (called annotations), which have classification detail populated. A single text file (or document) will be listed only once with all its annotations, and its annotations will never be split across files.

If prediction for any input file (or document) failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps input file followed by exactly one [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) containing only `code` and `message`.

  * For Text Sentiment: In the created directory files `text_sentiment_1.jsonl`, `text_sentiment_2.jsonl`,...,\ `text_sentiment_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found.

::

Each .JSONL file will contain, per line, a JSON representation of a proto that wraps input text file (or document) in the text snippet (or document) proto and a list of zero or more AnnotationPayload protos (called annotations), which have text_sentiment detail populated. A single text file (or document) will be listed only once with all its annotations, and its annotations will never be split across files.

If prediction for any input file (or document) failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps input file followed by exactly one [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) containing only `code` and `message`.

  * For Text Extraction: In the created directory files `text_extraction_1.jsonl`, `text_extraction_2.jsonl`,...,\ `text_extraction_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found. The contents of these .JSONL file(s) depend on whether the input used inline text, or documents. If input was inline, then each .JSONL file will contain, per line, a JSON representation of a proto that wraps given in request text snippet's "id" (if specified), followed by input text snippet, and a list of zero or more AnnotationPayload protos (called annotations), which have text_extraction detail populated. A single text snippet will be listed only once with all its annotations, and its annotations will never be split across files. If input used documents, then each .JSONL file will contain, per line, a JSON representation of a proto that wraps given in request document proto, followed by its OCR-ed representation in the form of a text snippet, finally followed by a list of zero or more AnnotationPayload protos (called annotations), which have text_extraction detail populated and refer, via their indices, to the OCR-ed text snippet. A single document (and its text snippet) will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any text snippet failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps either the "id" : "<id_value>" (in case of inline) or the document proto (in case of document) but here followed by exactly one ``google.rpc.Status` <https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto>`__ containing only`code`and`message`.

  * For Tables: Output depends on whether gcs_destination or bigquery_destination is set (either is allowed). Google Cloud Storage case: In the created directory files `tables_1.csv`, `tables_2.csv`,..., `tables_N.csv` will be created, where N may be 1, and depends on the total number of the successfully predicted rows. For all CLASSIFICATION prediction_type-s: Each .csv file will contain a header, listing all columns' display_name-s given on input followed by M target column names in the format of "<target_column_specs display_name>\ _\ score" where M is the number of distinct target values, i.e. number of distinct values in the target column of the table used to train the model. Subsequent lines will contain the respective values of successfully predicted rows, with the last, i.e. the target, columns having the corresponding prediction scores. For REGRESSION and FORECASTING prediction_type-s: Each .csv file will contain a header, listing all columns' display_name-s given on input followed by the predicted target column with name in the format of "predicted\ <target_column_specs display_name>" Subsequent lines will contain the respective values of successfully predicted rows, with the last, i.e. the target, column having the predicted target value. If prediction for any rows failed, then an additional `errors_1.csv`, `errors_2.csv`,..., `errors_N.csv` will be created (N depends on total number of failed rows). These files will have analogous format as `tables__.csv`, but always with a single target column having*\ ```google.rpc.Status`` <https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto>`**\_represented as a JSON string, and containing only`code` and `message`. BigQuery case: bigquery_destination pointing to a BigQuery project must be set. In the given project a new dataset will be created with name `prediction_<model-display-name>_<timestamp-of-prediction-call>` where will be made BigQuery-dataset-name compatible (e.g. most special characters will become underscores), and timestamp will be in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset two tables will be created, `predictions`, and `errors`. The `predictions` table's column names will be the input columns' display_name-s followed by the target column with name in the format of "predicted_\ <target_column_specs display_name>" The input feature columns will contain the respective values of successfully predicted rows, with the target column having an ARRAY of AnnotationPayloads, represented as STRUCT-s, containing TablesAnnotation. The `errors` table contains rows for which the prediction has failed, it has analogous input columns while the target column name is in the format of "errors_<target_column_specs display_name>", and as a value has ``google.rpc.Status` <https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto>`** represented as a STRUCT, and containing only `code` and `message`.




.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchPredictRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictRequest)

Request message for PredictionService.BatchPredict.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictRequest.ParamsEntry)

The abstract base class for a message.

### [BatchPredictResult](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictResult)

Result of the Batch Predict. This message is returned in `response][google.longrunning.Operation.response]` of the operation returned by the PredictionService.BatchPredict.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictResult.MetadataEntry)

The abstract base class for a message.

### [BoundingBoxMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BoundingBoxMetricsEntry)

Bounding box matching model metrics for a single intersection-over-union threshold and multiple label match confidence thresholds.

### [ConfidenceMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BoundingBoxMetricsEntry.ConfidenceMetricsEntry)

Metrics for a single confidence threshold.

### [BoundingPoly](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BoundingPoly)

A bounding polygon of a detected object on a plane. On output both vertices and normalized_vertices are provided. The polygon is formed by connecting vertices in the order they are listed.

### [ClassificationAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationAnnotation)

Contains annotation details specific to classification.

### [ClassificationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics)

Model evaluation metrics for classification problems. Note: For Video Classification this metrics only describe quality of the Video Classification predictions of "segment_classification" type.

### [ConfidenceMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)

Metrics for a single confidence threshold.

### [ConfusionMatrix](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfusionMatrix)

Confusion matrix of the model running the classification.

### [Row](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfusionMatrix.Row)

Output only. A row in the confusion matrix.

### [ClassificationType](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationType)

Type of the classification problem.

### [CreateDatasetOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.CreateDatasetOperationMetadata)

Details of CreateDataset operation.

### [CreateDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.CreateDatasetRequest)

Request message for AutoMl.CreateDataset.

### [CreateModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.CreateModelOperationMetadata)

Details of CreateModel operation.

### [CreateModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.CreateModelRequest)

Request message for AutoMl.CreateModel.

### [Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Dataset)

A workspace for solving a single, particular machine learning (ML) problem. A workspace contains examples that may be annotated.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Dataset.LabelsEntry)

The abstract base class for a message.

### [DeleteDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DeleteDatasetRequest)

Request message for AutoMl.DeleteDataset.

### [DeleteModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DeleteModelRequest)

Request message for AutoMl.DeleteModel.

### [DeleteOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DeleteOperationMetadata)

Details of operations that perform deletes of any entities.

### [DeployModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DeployModelOperationMetadata)

Details of DeployModel operation.

### [DeployModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DeployModelRequest)

Request message for AutoMl.DeployModel.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Document](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Document)

A structured text document e.g. a PDF.

### [Layout](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Document.Layout)

Describes the layout information of a text_segment in the document.

### [TextSegmentType](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Document.Layout.TextSegmentType)

The type of TextSegment in the context of the original document.

### [DocumentDimensions](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DocumentDimensions)

Message that describes dimension of a document.

### [DocumentDimensionUnit](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DocumentDimensions.DocumentDimensionUnit)

Unit of the document dimension.

### [DocumentInputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DocumentInputConfig)

Input configuration of a Document.

### [ExamplePayload](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExamplePayload)

Example data used for training or prediction.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportDataOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExportDataOperationMetadata)

Details of ExportData operation.

### [ExportDataOutputInfo](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExportDataOperationMetadata.ExportDataOutputInfo)

Further describes this export data's output. Supplements OutputConfig.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportDataRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExportDataRequest)

Request message for AutoMl.ExportData.

### [ExportModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExportModelOperationMetadata)

Details of ExportModel operation.

### [ExportModelOutputInfo](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExportModelOperationMetadata.ExportModelOutputInfo)

Further describes the output of model export. Supplements ModelExportOutputConfig.

### [ExportModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExportModelRequest)

Request message for AutoMl.ExportModel. Models need to be enabled for exporting, otherwise an error code will be returned.

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.GcsDestination)

The Google Cloud Storage location where the output is to be written to.

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.GcsSource)

The Google Cloud Storage location for the input content.

### [GetAnnotationSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.GetAnnotationSpecRequest)

Request message for AutoMl.GetAnnotationSpec.

### [GetDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.GetDatasetRequest)

Request message for AutoMl.GetDataset.

### [GetModelEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.GetModelEvaluationRequest)

Request message for AutoMl.GetModelEvaluation.

### [GetModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.GetModelRequest)

Request message for AutoMl.GetModel.

### [Image](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Image)

A representation of an image. Only images up to 30MB in size are supported.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImageClassificationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageClassificationDatasetMetadata)

Dataset metadata that is specific to image classification.

### [ImageClassificationModelDeploymentMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageClassificationModelDeploymentMetadata)

Model deployment metadata specific to Image Classification.

### [ImageClassificationModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageClassificationModelMetadata)

Model metadata for image classification.

### [ImageObjectDetectionAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionAnnotation)

Annotation details for image object detection.

### [ImageObjectDetectionDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionDatasetMetadata)

Dataset metadata specific to image object detection.

### [ImageObjectDetectionEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionEvaluationMetrics)

Model evaluation metrics for image object detection problems. Evaluates prediction quality of labeled bounding boxes.

### [ImageObjectDetectionModelDeploymentMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionModelDeploymentMetadata)

Model deployment metadata specific to Image Object Detection.

### [ImageObjectDetectionModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionModelMetadata)

Model metadata specific to image object detection.

### [ImportDataOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImportDataOperationMetadata)

Details of ImportData operation.

### [ImportDataRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImportDataRequest)

Request message for AutoMl.ImportData.

### [InputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.InputConfig)

Input configuration for AutoMl.ImportData action.

The format of input depends on dataset_metadata the Dataset into which the import is happening has. As input source the gcs_source is expected, unless specified otherwise. Additionally any input .CSV file by itself must be 100MB or smaller, unless specified otherwise. If an "example" file (that is, image, video etc.) with identical content (even if it had different `GCS_FILE_PATH`) is mentioned multiple times, then its label, bounding boxes etc. are appended. The same file should be always provided with the same `ML_USE` and `GCS_FILE_PATH`, if it is not, then these values are nondeterministically selected from the given ones.

The formats are represented in EBNF with commas being literal and with non-terminal symbols defined near the end of this comment. The formats are:

AutoML Vision ^^^^^^^^^^^^^

Classification ''''''''''''''

See `Preparing your training data <https://cloud.google.com/vision/automl/docs/prepare>`__ for more information.

CSV file(s) with each line in format:

::
    
    
    ML_USE,GCS_FILE_PATH,LABEL,LABEL,...
    

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:

    * `TRAIN` \- Rows in this file are used to train the model.
    * `TEST` \- Rows in this file are used to test the model during training.
    * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing.
  * `GCS_FILE_PATH` \- The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG, .WEBP, .BMP, .TIFF, .ICO.

  * `LABEL` \- A label that identifies the object in the image.




For the `MULTICLASS` classification type, at most one `LABEL` is allowed per image. If an image has not yet been labeled, then it should be mentioned just once with no `LABEL`.

Some sample rows:

::
    
    
    TRAIN,gs://folder/image1.jpg,daisy
    TEST,gs://folder/image2.jpg,dandelion,tulip,rose
    UNASSIGNED,gs://folder/image3.jpg,daisy
    UNASSIGNED,gs://folder/image4.jpg
    

Object Detection ''''''''''''''''

See `Preparing your training data <https://cloud.google.com/vision/automl/object-detection/docs/prepare>`__ for more information.

A CSV file(s) with each line in format:

::
    
    
    ML_USE,GCS_FILE_PATH,[LABEL],(BOUNDING_BOX | ,,,,,,,)
    

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:

    * `TRAIN` \- Rows in this file are used to train the model.
    * `TEST` \- Rows in this file are used to test the model during training.
    * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing.
  * `GCS_FILE_PATH` \- The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. Each image is assumed to be exhaustively labeled.

  * `LABEL` \- A label that identifies the object in the image specified by the `BOUNDING_BOX`.

  * `BOUNDING BOX` \- The vertices of an object in the example image. The minimum allowed `BOUNDING_BOX` edge length is 0.01, and no more than 500 `BOUNDING_BOX` instances per image are allowed (one `BOUNDING_BOX` per line). If an image has no looked for objects then it should be mentioned just once with no LABEL and the ",,,,,,," in place of the `BOUNDING_BOX`.




**Four sample rows:**

::
    
    
    TRAIN,gs://folder/image1.png,car,0.1,0.1,,,0.3,0.3,,
    TRAIN,gs://folder/image1.png,bike,.7,.6,,,.8,.9,,
    UNASSIGNED,gs://folder/im2.png,car,0.1,0.1,0.2,0.1,0.2,0.3,0.1,0.3
    TEST,gs://folder/im3.png,,,,,,,,,
    

.. raw:: html
    
    
      </section>
    </div>
    

AutoML Video Intelligence ^^^^^^^^^^^^^^^^^^^^^^^^^

Classification ''''''''''''''

See `Preparing your training data <https://cloud.google.com/video-intelligence/automl/docs/prepare>`__ for more information.

CSV file(s) with each line in format:

::
    
    
    ML_USE,GCS_FILE_PATH
    

For `ML_USE`, do not use `VALIDATE`.

`GCS_FILE_PATH` is the path to another .csv file that describes training example for a given `ML_USE`, using the following row format:

::
    
    
    GCS_FILE_PATH,(LABEL,TIME_SEGMENT_START,TIME_SEGMENT_END | ,,)
    

Here `GCS_FILE_PATH` leads to a video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI.

`TIME_SEGMENT_START` and `TIME_SEGMENT_END` must be within the length of the video, and the end time must be after the start time. Any segment of a video which has one or more labels on it, is considered a hard negative for all other labels. Any segment with no labels on it is considered to be unknown. If a whole video is unknown, then it should be mentioned just once with ",," in place of `LABEL, TIME_SEGMENT_START,TIME_SEGMENT_END`.

Sample top level CSV file:

::
    
    
    TRAIN,gs://folder/train_videos.csv
    TEST,gs://folder/test_videos.csv
    UNASSIGNED,gs://folder/other_videos.csv
    

Sample rows of a CSV file for a particular ML_USE:

::
    
    
    gs://folder/video1.avi,car,120,180.000021
    gs://folder/video1.avi,bike,150,180.000021
    gs://folder/vid2.avi,car,0,60.5
    gs://folder/vid3.avi,,,
    

Object Tracking '''''''''''''''

See `Preparing your training data </video-intelligence/automl/object-tracking/docs/prepare>`__ for more information.

CSV file(s) with each line in format:

::
    
    
    ML_USE,GCS_FILE_PATH
    

For `ML_USE`, do not use `VALIDATE`.

`GCS_FILE_PATH` is the path to another .csv file that describes training example for a given `ML_USE`, using the following row format:

::
    
    
    GCS_FILE_PATH,LABEL,[INSTANCE_ID],TIMESTAMP,BOUNDING_BOX
    

or

::
    
    
    GCS_FILE_PATH,,,,,,,,,,
    

Here `GCS_FILE_PATH` leads to a video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. Providing `INSTANCE_ID`\ s can help to obtain a better model. When a specific labeled entity leaves the video frame, and shows up afterwards it is not required, albeit preferable, that the same `INSTANCE_ID` is given to it.

`TIMESTAMP` must be within the length of the video, the `BOUNDING_BOX` is assumed to be drawn on the closest video's frame to the `TIMESTAMP`. Any mentioned by the `TIMESTAMP` frame is expected to be exhaustively labeled and no more than 500 `BOUNDING_BOX`-es per frame are allowed. If a whole video is unknown, then it should be mentioned just once with ",,,,,,,,,," in place of `LABEL, [INSTANCE_ID],TIMESTAMP,BOUNDING_BOX`.

Sample top level CSV file:

::
    
    
     TRAIN,gs://folder/train_videos.csv
     TEST,gs://folder/test_videos.csv
     UNASSIGNED,gs://folder/other_videos.csv
    

Seven sample rows of a CSV file for a particular ML_USE:

::
    
    
     gs://folder/video1.avi,car,1,12.10,0.8,0.8,0.9,0.8,0.9,0.9,0.8,0.9
     gs://folder/video1.avi,car,1,12.90,0.4,0.8,0.5,0.8,0.5,0.9,0.4,0.9
     gs://folder/video1.avi,car,2,12.10,.4,.2,.5,.2,.5,.3,.4,.3
     gs://folder/video1.avi,car,2,12.90,.8,.2,,,.9,.3,,
     gs://folder/video1.avi,bike,,12.50,.45,.45,,,.55,.55,,
     gs://folder/video2.avi,car,1,0,.1,.9,,,.9,.1,,
     gs://folder/video2.avi,,,,,,,,,,,
    

AutoML Natural Language ^^^^^^^^^^^^^^^^^^^^^^^

Entity Extraction '''''''''''''''''

See `Preparing your training data </natural-language/automl/entity-analysis/docs/prepare>`__ for more information.

One or more CSV file(s) with each line in the following format:

::
    
    
    ML_USE,GCS_FILE_PATH
    

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:

    * `TRAIN` \- Rows in this file are used to train the model.
    * `TEST` \- Rows in this file are used to test the model during training.
    * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing..
  * `GCS_FILE_PATH` \- a Identifies JSON Lines (.JSONL) file stored in Google Cloud Storage that contains in-line text in-line as documents for model training.




After the training data set has been determined from the `TRAIN` and `UNASSIGNED` CSV files, the training data is divided into train and validation data sets. 70% for training and 30% for validation.

For example:

::
    
    
    TRAIN,gs://folder/file1.jsonl
    VALIDATE,gs://folder/file2.jsonl
    TEST,gs://folder/file3.jsonl
    

**In-line JSONL files**

In-line .JSONL files contain, per line, a JSON document that wraps a [`text_snippet`][google.cloud.automl.v1.TextSnippet] field followed by one or more [`annotations`][google.cloud.automl.v1.AnnotationPayload] fields, which have `display_name` and `text_extraction` fields to describe the entity from the text snippet. Multiple JSON documents can be separated using line breaks (\n).

The supplied text must be annotated exhaustively. For example, if you include the text "horse", but do not label it as "animal", then "horse" is assumed to not be an "animal".

Any given text snippet content must have 30,000 characters or less, and also be UTF-8 NFC encoded. ASCII is accepted as it is UTF-8 NFC encoded.

For example:

::
    
    
    {
      "text_snippet": {
        "content": "dog car cat"
      },
      "annotations": [
         {
           "display_name": "animal",
           "text_extraction": {
             "text_segment": {"start_offset": 0, "end_offset": 2}
          }
         },
         {
          "display_name": "vehicle",
           "text_extraction": {
             "text_segment": {"start_offset": 4, "end_offset": 6}
           }
         },
         {
           "display_name": "animal",
           "text_extraction": {
             "text_segment": {"start_offset": 8, "end_offset": 10}
           }
         }
     ]
    }\n
    {
       "text_snippet": {
         "content": "This dog is good."
       },
       "annotations": [
          {
            "display_name": "animal",
            "text_extraction": {
              "text_segment": {"start_offset": 5, "end_offset": 7}
            }
          }
       ]
    }
    

**JSONL files that reference documents**

.JSONL files contain, per line, a JSON document that wraps a `input_config` that contains the path to a source document. Multiple JSON documents can be separated using line breaks (\n).

Supported document extensions: .PDF, .TIF, .TIFF

For example:

::
    
    
    {
      "document": {
        "input_config": {
          "gcs_source": { "input_uris": [ "gs://folder/document1.pdf" ]
          }
        }
      }
    }\n
    {
      "document": {
        "input_config": {
          "gcs_source": { "input_uris": [ "gs://folder/document2.tif" ]
          }
        }
      }
    }
    

**In-line JSONL files with document layout information**

**Note:** You can only annotate documents using the UI. The format described below applies to annotated documents exported using the UI or `exportData`.

In-line .JSONL files for documents contain, per line, a JSON document that wraps a `document` field that provides the textual content of the document and the layout information.

For example:

::
    
    
    {
      "document": {
              "document_text": {
                "content": "dog car cat"
              }
              "layout": [
                {
                  "text_segment": {
                    "start_offset": 0,
                    "end_offset": 11,
                   },
                   "page_number": 1,
                   "bounding_poly": {
                      "normalized_vertices": [
                        {"x": 0.1, "y": 0.1},
                        {"x": 0.1, "y": 0.3},
                        {"x": 0.3, "y": 0.3},
                        {"x": 0.3, "y": 0.1},
                      ],
                    },
                    "text_segment_type": TOKEN,
                }
              ],
              "document_dimensions": {
                "width": 8.27,
                "height": 11.69,
                "unit": INCH,
              }
              "page_count": 3,
            },
            "annotations": [
              {
                "display_name": "animal",
                "text_extraction": {
                  "text_segment": {"start_offset": 0, "end_offset": 3}
                }
              },
              {
                "display_name": "vehicle",
                "text_extraction": {
                  "text_segment": {"start_offset": 4, "end_offset": 7}
                }
              },
              {
                "display_name": "animal",
                "text_extraction": {
                  "text_segment": {"start_offset": 8, "end_offset": 11}
                }
              },
            ],
    

Classification ''''''''''''''

See `Preparing your training data <https://cloud.google.com/natural-language/automl/docs/prepare>`__ for more information.

One or more CSV file(s) with each line in the following format:

::
    
    
    ML_USE,(TEXT_SNIPPET | GCS_FILE_PATH),LABEL,LABEL,...
    

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:

    * `TRAIN` \- Rows in this file are used to train the model.
    * `TEST` \- Rows in this file are used to test the model during training.
    * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing.
  * `TEXT_SNIPPET` and `GCS_FILE_PATH` are distinguished by a pattern. If the column content is a valid Google Cloud Storage file path, that is, prefixed by "gs://", it is treated as a `GCS_FILE_PATH`. Otherwise, if the content is enclosed in double quotes (""), it is treated as a `TEXT_SNIPPET`. For `GCS_FILE_PATH`, the path must lead to a file with supported extension and UTF-8 encoding, for example, "gs://folder/content.txt" AutoML imports the file content as a text snippet. For `TEXT_SNIPPET`, AutoML imports the column content excluding quotes. In both cases, size of the content must be 10MB or less in size. For zip files, the size of each file inside the zip must be 10MB or less in size.

For the `MULTICLASS` classification type, at most one `LABEL` is allowed.

The `ML_USE` and `LABEL` columns are optional. Supported file extensions: .TXT, .PDF, .TIF, .TIFF, .ZIP




A maximum of 100 unique labels are allowed per CSV row.

Sample rows:

::
    
    
    TRAIN,"They have bad food and very rude",RudeService,BadFood
    gs://folder/content.txt,SlowService
    TEST,gs://folder/document.pdf
    VALIDATE,gs://folder/text_files.zip,BadFood
    

Sentiment Analysis ''''''''''''''''''

See `Preparing your training data <https://cloud.google.com/natural-language/automl/docs/prepare>`__ for more information.

CSV file(s) with each line in format:

::
    
    
    ML_USE,(TEXT_SNIPPET | GCS_FILE_PATH),SENTIMENT
    

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:

    * `TRAIN` \- Rows in this file are used to train the model.
    * `TEST` \- Rows in this file are used to test the model during training.
    * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing.
  * `TEXT_SNIPPET` and `GCS_FILE_PATH` are distinguished by a pattern. If the column content is a valid Google Cloud Storage file path, that is, prefixed by "gs://", it is treated as a `GCS_FILE_PATH`. Otherwise, if the content is enclosed in double quotes (""), it is treated as a `TEXT_SNIPPET`. For `GCS_FILE_PATH`, the path must lead to a file with supported extension and UTF-8 encoding, for example, "gs://folder/content.txt" AutoML imports the file content as a text snippet. For `TEXT_SNIPPET`, AutoML imports the column content excluding quotes. In both cases, size of the content must be 128kB or less in size. For zip files, the size of each file inside the zip must be 128kB or less in size.

The `ML_USE` and `SENTIMENT` columns are optional. Supported file extensions: .TXT, .PDF, .TIF, .TIFF, .ZIP

  * `SENTIMENT` \- An integer between 0 and Dataset.text_sentiment_dataset_metadata.sentiment_max (inclusive). Describes the ordinal of the sentiment - higher value means a more positive sentiment. All the values are completely relative, i.e. neither 0 needs to mean a negative or neutral sentiment nor sentiment_max needs to mean a positive one - it is just required that 0 is the least positive sentiment in the data, and sentiment_max is the most positive one. The SENTIMENT shouldn't be confused with "score" or "magnitude" from the previous Natural Language Sentiment Analysis API. All SENTIMENT values between 0 and sentiment_max must be represented in the imported data. On prediction the same 0 to sentiment_max range will be used. The difference between neighboring sentiment values needs not to be uniform, e.g. 1 and 2 may be similar whereas the difference between 2 and 3 may be large.




Sample rows:

::
    
    
    TRAIN,"@freewrytin this is way too good for your product",2
    gs://folder/content.txt,3
    TEST,gs://folder/document.pdf
    VALIDATE,gs://folder/text_files.zip,2
    

AutoML Tables ^^^^^^^^^^^^^

See `Preparing your training data <https://cloud.google.com/automl-tables/docs/prepare>`__ for more information.

You can use either gcs_source or bigquery_source. All input is concatenated into a single primary_table_spec_id

**For gcs_source:**

CSV file(s), where the first row of the first file is the header, containing unique column names. If the first row of a subsequent file is the same as the header, then it is also treated as a header. All other rows contain values for the corresponding columns.

Each .CSV file by itself must be 10GB or smaller, and their total size must be 100GB or smaller.

First three sample rows of a CSV file:

.. raw:: html
    
    
    <pre>
    "Id","First Name","Last Name","Dob","Addresses"
    "1","John","Doe","1968-01-22","[{"status":"current","address":"123_First_Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456_Main_Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]"
    "2","Jane","Doe","1980-10-16","[{"status":"current","address":"789_Any_Avenue","city":"Albany","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321_Main_Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]}
    </pre>
    

**For bigquery_source:**

An URI of a BigQuery table. The user data size of the BigQuery table must be 100GB or smaller.

An imported table must have between 2 and 1,000 columns, inclusive, and between 1000 and 100,000,000 rows, inclusive. There are at most 5 import data running in parallel.

**Input field definitions:**

`ML_USE` : ("TRAIN" | "VALIDATE" | "TEST" | "UNASSIGNED") Describes how the given example (file) should be used for model training. "UNASSIGNED" can be used when user has no preference.

`GCS_FILE_PATH` : The path to a file on Google Cloud Storage. For example, "gs://folder/image1.png".

`LABEL` : A display name of an object on an image, video etc., e.g. "dog". Must be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores(_), and ASCII digits 0-9. For each label an AnnotationSpec is created which display_name becomes the label; AnnotationSpecs are given back in predictions.

`INSTANCE_ID` : A positive integer that identifies a specific instance of a labeled entity on an example. Used e.g. to track two cars on a video while being able to tell apart which one is which.

`BOUNDING_BOX` : (`VERTEX,VERTEX,VERTEX,VERTEX` | `VERTEX,,,VERTEX,,`) A rectangle parallel to the frame of the example (image, video). If 4 vertices are given they are connected by edges in the order provided, if 2 are given they are recognized as diagonally opposite vertices of the rectangle.

`VERTEX` : (`COORDINATE,COORDINATE`) First coordinate is horizontal (x), the second is vertical (y).

`COORDINATE` : A float in 0 to 1 range, relative to total length of image or video in given dimension. For fractions the leading non-decimal 0 can be omitted (i.e. 0.3 = .3). Point 0,0 is in top left.

`TIME_SEGMENT_START` : (`TIME_OFFSET`) Expresses a beginning, inclusive, of a time segment within an example that has a time dimension (e.g. video).

`TIME_SEGMENT_END` : (`TIME_OFFSET`) Expresses an end, exclusive, of a time segment within n example that has a time dimension (e.g. video).

`TIME_OFFSET` : A number of seconds as measured from the start of an example (e.g. video). Fractions are allowed, up to a microsecond precision. "inf" is allowed, and it means the end of the example.

`TEXT_SNIPPET` : The content of a text snippet, UTF-8 encoded, enclosed within double quotes ("").

`DOCUMENT` : A field that provides the textual content with document and the layout information.

**Errors:**

If any of the provided CSV files can't be parsed or if more than certain percent of CSV rows cannot be processed then the operation fails and nothing is imported. Regardless of overall success or failure the per-row failures, up to a certain count cap, is listed in Operation.metadata.partial_failures.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.InputConfig.ParamsEntry)

The abstract base class for a message.

### [ListDatasetsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListDatasetsRequest)

Request message for AutoMl.ListDatasets.

### [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListDatasetsResponse)

Response message for AutoMl.ListDatasets.

### [ListModelEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelEvaluationsRequest)

Request message for AutoMl.ListModelEvaluations.

### [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelEvaluationsResponse)

Response message for AutoMl.ListModelEvaluations.

### [ListModelsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelsRequest)

Request message for AutoMl.ListModels.

### [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ListModelsResponse)

Response message for AutoMl.ListModels.

### [Model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Model)

API proto representing a trained machine learning model.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeploymentState](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Model.DeploymentState)

Deployment state of the model.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Model.LabelsEntry)

The abstract base class for a message.

### [ModelEvaluation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ModelEvaluation)

Evaluation results of a model.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ModelExportOutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ModelExportOutputConfig)

Output configuration for ModelExport Action.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ModelExportOutputConfig.ParamsEntry)

The abstract base class for a message.

### [NormalizedVertex](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.NormalizedVertex)

A vertex represents a 2D point in the image. The normalized vertex coordinates are between 0 to 1 fractions relative to the original plane (image, video). E.g. if the plane (e.g. whole image) would have size 10 x 20 then a point with normalized coordinates (0.1, 0.3) would be at the position (1, 6) on that plane.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.OperationMetadata)

Metadata used across all long running operations returned by AutoML API.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [OutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.OutputConfig)

  * For Translation: CSV file `translation.csv`, with each line in format: ML_USE,GCS_FILE_PATH GCS_FILE_PATH leads to a .TSV file which describes examples that have given ML_USE, using the following row format per line: TEXT_SNIPPET (in source language) \t TEXT_SNIPPET (in target language)

    * For Tables: Output depends on whether the dataset was imported from Google Cloud Storage or BigQuery. Google Cloud Storage case: gcs_destination must be set. Exported are CSV file(s) `tables_1.csv`, `tables_2.csv`,...,\ `tables_N.csv` with each having as header line the table's column names, and all other lines contain values for the header columns. BigQuery case: bigquery_destination pointing to a BigQuery project must be set. In the given project a new dataset will be created with name `export_data_<automl-dataset-display-name>_<timestamp-of-export-call>` where will be made BigQuery-dataset-name compatible (e.g. most special characters will become underscores), and timestamp will be in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In that dataset a new table called `primary_table` will be created, and filled with precisely the same data as this obtained on import.



.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PredictRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.PredictRequest)

Request message for PredictionService.Predict.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.PredictRequest.ParamsEntry)

The abstract base class for a message.

### [PredictResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.PredictResponse)

Response message for PredictionService.Predict.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.PredictResponse.MetadataEntry)

The abstract base class for a message.

### [TextClassificationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextClassificationDatasetMetadata)

Dataset metadata for classification.

### [TextClassificationModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextClassificationModelMetadata)

Model metadata that is specific to text classification.

### [TextExtractionAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextExtractionAnnotation)

Annotation for identifying spans of text.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TextExtractionDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextExtractionDatasetMetadata)

Dataset metadata that is specific to text extraction

### [TextExtractionEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextExtractionEvaluationMetrics)

Model evaluation metrics for text extraction problems.

### [ConfidenceMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry)

Metrics for a single confidence threshold.

### [TextExtractionModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextExtractionModelMetadata)

Model metadata that is specific to text extraction.

### [TextSegment](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSegment)

A contiguous part of a text (string), assuming it has an UTF-8 NFC encoding.

### [TextSentimentAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSentimentAnnotation)

Contains annotation details specific to text sentiment.

### [TextSentimentDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSentimentDatasetMetadata)

Dataset metadata for text sentiment.

### [TextSentimentEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSentimentEvaluationMetrics)

Model evaluation metrics for text sentiment problems.

### [TextSentimentModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSentimentModelMetadata)

Model metadata that is specific to text sentiment.

### [TextSnippet](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSnippet)

A representation of a text snippet.

### [TranslationAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TranslationAnnotation)

Annotation details specific to translation.

### [TranslationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TranslationDatasetMetadata)

Dataset metadata that is specific to translation.

### [TranslationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TranslationEvaluationMetrics)

Evaluation metrics for the dataset.

### [TranslationModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TranslationModelMetadata)

Model metadata that is specific to translation.

### [UndeployModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.UndeployModelOperationMetadata)

Details of UndeployModel operation.

### [UndeployModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.UndeployModelRequest)

Request message for AutoMl.UndeployModel.

### [UpdateDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.UpdateDatasetRequest)

Request message for AutoMl.UpdateDataset

### [UpdateModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.UpdateModelRequest)

Request message for AutoMl.UpdateModel

### [AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient)

AutoML Server API.

The resource names are assigned by the server. The server never reuses names that it has created after the resources with those names are deleted.

An ID of a resource is the last element of the item's resource name. For `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then the id for the item is `{dataset_id}`.

Currently the only supported `location_id` is "us-central1".

On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted.

### [AutoMlClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient)

AutoML Server API.

The resource names are assigned by the server. The server never reuses names that it has created after the resources with those names are deleted.

An ID of a resource is the last element of the item's resource name. For `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then the id for the item is `{dataset_id}`.

Currently the only supported `location_id` is "us-central1".

On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted.

### [ListColumnSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager)

A pager for iterating through `list_column_specs` requests.

This class thinly wraps an initial [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse) object, and provides an `__aiter__` method to iterate through its `column_specs` field.

If there are more pages, the `__aiter__` method will make additional `ListColumnSpecs` requests and continue to iterate through the `column_specs` field on the corresponding responses.

All the usual [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListColumnSpecsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsPager)

A pager for iterating through `list_column_specs` requests.

This class thinly wraps an initial [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse) object, and provides an `__iter__` method to iterate through its `column_specs` field.

If there are more pages, the `__iter__` method will make additional `ListColumnSpecs` requests and continue to iterate through the `column_specs` field on the corresponding responses.

All the usual [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatasetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager)

A pager for iterating through `list_datasets` requests.

This class thinly wraps an initial [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse) object, and provides an `__aiter__` method to iterate through its `datasets` field.

If there are more pages, the `__aiter__` method will make additional `ListDatasets` requests and continue to iterate through the `datasets` field on the corresponding responses.

All the usual [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatasetsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsPager)

A pager for iterating through `list_datasets` requests.

This class thinly wraps an initial [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse) object, and provides an `__iter__` method to iterate through its `datasets` field.

If there are more pages, the `__iter__` method will make additional `ListDatasets` requests and continue to iterate through the `datasets` field on the corresponding responses.

All the usual [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager)

A pager for iterating through `list_model_evaluations` requests.

This class thinly wraps an initial [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse) object, and provides an `__aiter__` method to iterate through its `model_evaluation` field.

If there are more pages, the `__aiter__` method will make additional `ListModelEvaluations` requests and continue to iterate through the `model_evaluation` field on the corresponding responses.

All the usual [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelEvaluationsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsPager)

A pager for iterating through `list_model_evaluations` requests.

This class thinly wraps an initial [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse) object, and provides an `__iter__` method to iterate through its `model_evaluation` field.

If there are more pages, the `__iter__` method will make additional `ListModelEvaluations` requests and continue to iterate through the `model_evaluation` field on the corresponding responses.

All the usual [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager)

A pager for iterating through `list_models` requests.

This class thinly wraps an initial [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse) object, and provides an `__aiter__` method to iterate through its `model` field.

If there are more pages, the `__aiter__` method will make additional `ListModels` requests and continue to iterate through the `model` field on the corresponding responses.

All the usual [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsPager)

A pager for iterating through `list_models` requests.

This class thinly wraps an initial [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse) object, and provides an `__iter__` method to iterate through its `model` field.

If there are more pages, the `__iter__` method will make additional `ListModels` requests and continue to iterate through the `model` field on the corresponding responses.

All the usual [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTableSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager)

A pager for iterating through `list_table_specs` requests.

This class thinly wraps an initial [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse) object, and provides an `__aiter__` method to iterate through its `table_specs` field.

If there are more pages, the `__aiter__` method will make additional `ListTableSpecs` requests and continue to iterate through the `table_specs` field on the corresponding responses.

All the usual [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTableSpecsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsPager)

A pager for iterating through `list_table_specs` requests.

This class thinly wraps an initial [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse) object, and provides an `__iter__` method to iterate through its `table_specs` field.

If there are more pages, the `__iter__` method will make additional `ListTableSpecs` requests and continue to iterate through the `table_specs` field on the corresponding responses.

All the usual [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [PredictionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient)

AutoML Prediction API.

On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted.

### [PredictionServiceClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient)

AutoML Prediction API.

On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted.

### [GcsClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient)

Uploads Pandas DataFrame to a bucket in Google Cloud Storage.

### [TablesClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient)

AutoML Tables API helper.

This is intended to simplify usage of the auto-generated python client, in particular for the `AutoML Tables product <https://cloud.google.com/automl-tables/>`_.

### [AnnotationPayload](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.AnnotationPayload)

Contains annotation information that is relevant to AutoML.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotationSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.AnnotationSpec)

A definition of an annotation spec.

### [ArrayStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ArrayStats)

The data statistics of a series of ARRAY values.

### [BatchPredictInputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictInputConfig)

Input configuration for BatchPredict Action.

The format of input depends on the ML problem of the model used for prediction. As input source the gcs_source is expected, unless specified otherwise.

The formats are represented in EBNF with commas being literal and with non-terminal symbols defined near the end of this comment. The formats are:

  * For Image Classification: CSV file(s) with each line having just a single column: GCS_FILE_PATH which leads to image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. This path is treated as the ID in the Batch predict output. Three sample rows: gs://folder/image1.jpeg gs://folder/image2.gif gs://folder/image3.png

  * For Image Object Detection: CSV file(s) with each line having just a single column: GCS_FILE_PATH which leads to image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. This path is treated as the ID in the Batch predict output. Three sample rows: gs://folder/image1.jpeg gs://folder/image2.gif gs://folder/image3.png

  * For Video Classification: CSV file(s) with each line in format: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END GCS_FILE_PATH leads to video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. TIME_SEGMENT_START and TIME_SEGMENT_END must be within the length of the video, and end has to be after the start. Three sample rows: gs://folder/video1.mp4,10,40 gs://folder/video1.mp4,20,60 gs://folder/vid2.mov,0,inf

  * For Video Object Tracking: CSV file(s) with each line in format: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END GCS_FILE_PATH leads to video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. TIME_SEGMENT_START and TIME_SEGMENT_END must be within the length of the video, and end has to be after the start. Three sample rows: gs://folder/video1.mp4,10,240 gs://folder/video1.mp4,300,360 gs://folder/vid2.mov,0,inf

  * For Text Classification: CSV file(s) with each line having just a single column: GCS_FILE_PATH | TEXT_SNIPPET Any given text file can have size upto 128kB. Any given text snippet content must have 60,000 characters or less. Three sample rows: gs://folder/text1.txt "Some text content to predict" gs://folder/text3.pdf Supported file extensions: .txt, .pdf

  * For Text Sentiment: CSV file(s) with each line having just a single column: GCS_FILE_PATH | TEXT_SNIPPET Any given text file can have size upto 128kB. Any given text snippet content must have 500 characters or less. Three sample rows: gs://folder/text1.txt "Some text content to predict" gs://folder/text3.pdf Supported file extensions: .txt, .pdf

  * For Text Extraction .JSONL (i.e. JSON Lines) file(s) which either provide text in-line or as documents (for a single BatchPredict call only one of the these formats may be used). The in-line .JSONL file(s) contain per line a proto that wraps a temporary user-assigned TextSnippet ID (string up to 2000 characters long) called "id", a TextSnippet proto (in json representation) and zero or more TextFeature protos. Any given text snippet content must have 30,000 characters or less, and also be UTF-8 NFC encoded (ASCII already is). The IDs provided should be unique. The document .JSONL file(s) contain, per line, a proto that wraps a Document proto with input_config set. Only PDF documents are supported now, and each document must be up to 2MB large. Any given .JSONL file must be 100MB or smaller, and no more than 20 files may be given. Sample in-line JSON Lines file (presented here with artificial line breaks, but the only actual line break is denoted by \n): { "id": "my_first_id", "text_snippet": { "content": "dog car cat"}, "text_features": [ { "text_segment": {"start_offset": 4, "end_offset": 6}, "structural_type": PARAGRAPH, "bounding_poly": { "normalized_vertices": [ {"x": 0.1, "y": 0.1}, {"x": 0.1, "y": 0.3}, {"x": 0.3, "y": 0.3}, {"x": 0.3, "y": 0.1}, ] }, } ], }\n { "id": "2", "text_snippet": { "content": "An elaborate content", "mime_type": "text/plain" } } Sample document JSON Lines file (presented here with artificial line breaks, but the only actual line break is denoted by \n).: { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document1.pdf" ] } } } }\n { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document2.pdf" ] } } } }

  * For Tables: Either gcs_source or




bigquery_source. GCS case: CSV file(s), each by itself 10GB or smaller and total size must be 100GB or smaller, where first file must have a header containing column names. If the first row of a subsequent file is the same as the header, then it is also treated as a header. All other rows contain values for the corresponding columns. The column names must contain the model's

[input_feature_column_specs'][google.cloud.automl.v1beta1.TablesModelMetadata.input_feature_column_specs]

display_name-s (order doesn't matter). The columns corresponding to the model's input feature column specs must contain values compatible with the column spec's data types. Prediction on all the rows, i.e. the CSV lines, will be attempted. For FORECASTING

prediction_type: all columns having

TIME_SERIES_AVAILABLE_PAST_ONLY type will be ignored. First three sample rows of a CSV file: "First Name","Last Name","Dob","Addresses"

"John","Doe","1968-01-22","[{"status":"current","address":"123_First_Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456_Main_Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]"

"Jane","Doe","1980-10-16","[{"status":"current","address":"789_Any_Avenue","city":"Albany","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321_Main_Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]} BigQuery case: An URI of a BigQuery table. The user data size of the BigQuery table must be 100GB or smaller. The column names must contain the model's

[input_feature_column_specs'][google.cloud.automl.v1beta1.TablesModelMetadata.input_feature_column_specs]

display_name-s (order doesn't matter). The columns corresponding to the model's input feature column specs must contain values compatible with the column spec's data types. Prediction on all the rows of the table will be attempted. For FORECASTING

prediction_type: all columns having

TIME_SERIES_AVAILABLE_PAST_ONLY type will be ignored.

Definitions: GCS_FILE_PATH = A path to file on GCS, e.g. "gs://folder/video.avi". TEXT_SNIPPET = A content of a text snippet, UTF-8 encoded, enclosed within double quotes ("") TIME_SEGMENT_START = TIME_OFFSET Expresses a beginning, inclusive, of a time segment within an example that has a time dimension (e.g. video). TIME_SEGMENT_END = TIME_OFFSET Expresses an end, exclusive, of a time segment within an example that has a time dimension (e.g. video). TIME_OFFSET = A number of seconds as measured from the start of an example (e.g. video). Fractions are allowed, up to a microsecond precision. "inf" is allowed and it means the end of the example.

Errors: If any of the provided CSV files can't be parsed or if more than certain percent of CSV rows cannot be processed then the operation fails and prediction does not happen. Regardless of overall success or failure the per-row failures, up to a certain count cap, will be listed in Operation.metadata.partial_failures.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchPredictOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictOperationMetadata)

Details of BatchPredict operation.

### [BatchPredictOutputInfo](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictOperationMetadata.BatchPredictOutputInfo)

Further describes this batch predict's output. Supplements

BatchPredictOutputConfig.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchPredictOutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictOutputConfig)

Output configuration for BatchPredict Action.

As destination the

gcs_destination must be set unless specified otherwise for a domain. If gcs_destination is set then in the given directory a new directory is created. Its name will be "prediction--", where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. The contents of it depends on the ML problem the predictions are made for. \- For Image Classification: In the created directory files `image_classification_1.jsonl`, `image_classification_2.jsonl`,...,\ `image_classification_N.jsonl` will be created, where N may be 1, and depends on the total number of the successfully predicted images and annotations. A single image will be listed only once with all its annotations, and its annotations will never be split across files. Each .JSONL file will contain, per line, a JSON representation of a proto that wraps image's "ID" : "<id_value>" followed by a list of zero or more AnnotationPayload protos (called annotations), which have classification detail populated. If prediction for any image failed (partially or completely), then an additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps the same "ID" : "<id_value>" but here followed by exactly one [`google.rpc.Status`](https: //github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) containing only `code` and `message`\ fields. \- For Image Object Detection: In the created directory files `image_object_detection_1.jsonl`, `image_object_detection_2.jsonl`,...,\ `image_object_detection_N.jsonl` will be created, where N may be 1, and depends on the total number of the successfully predicted images and annotations. Each .JSONL file will contain, per line, a JSON representation of a proto that wraps image's "ID" : "<id_value>" followed by a list of zero or more AnnotationPayload protos (called annotations), which have image_object_detection detail populated. A single image will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any image failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps the same "ID" : "<id_value>" but here followed by exactly one [`google.rpc.Status`](https: //github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) containing only `code` and `message`\ fields. \- For Video Classification: In the created directory a video_classification.csv file, and a .JSON file per each video classification requested in the input (i.e. each line in given CSV(s)), will be created. :: The format of video_classification.csv is: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END,JSON_FILE_NAME,STATUS where: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END = matches 1 to 1 the prediction input lines (i.e. video_classification.csv has precisely the same number of lines as the prediction input had.) JSON_FILE_NAME = Name of .JSON file in the output directory, which contains prediction responses for the video time segment. STATUS = "OK" if prediction completed successfully, or an error code with message otherwise. If STATUS is not "OK" then the .JSON file for that line may not exist or be empty. :: Each .JSON file, assuming STATUS is "OK", will contain a list of AnnotationPayload protos in JSON format, which are the predictions for the video time segment the file is assigned to in the video_classification.csv. All AnnotationPayload protos will have video_classification field set, and will be sorted by video_classification.type field (note that the returned types are governed by `classifaction_types` parameter in [PredictService.BatchPredictRequest.params][]). \- For Video Object Tracking: In the created directory a video_object_tracking.csv file will be created, and multiple files video_object_trackinng_1.json, video_object_trackinng_2.json,..., video_object_trackinng_N.json, where N is the number of requests in the input (i.e. the number of lines in given CSV(s)). :: The format of video_object_tracking.csv is: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END,JSON_FILE_NAME,STATUS where: GCS_FILE_PATH,TIME_SEGMENT_START,TIME_SEGMENT_END = matches 1 to 1 the prediction input lines (i.e. video_object_tracking.csv has precisely the same number of lines as the prediction input had.) JSON_FILE_NAME = Name of .JSON file in the output directory, which contains prediction responses for the video time segment. STATUS = "OK" if prediction completed successfully, or an error code with message otherwise. If STATUS is not "OK" then the .JSON file for that line may not exist or be empty. :: Each .JSON file, assuming STATUS is "OK", will contain a list of AnnotationPayload protos in JSON format, which are the predictions for each frame of the video time segment the file is assigned to in video_object_tracking.csv. All AnnotationPayload protos will have video_object_tracking field set. \- For Text Classification: In the created directory files `text_classification_1.jsonl`, `text_classification_2.jsonl`,...,\ `text_classification_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found. :: Each .JSONL file will contain, per line, a JSON representation of a proto that wraps input text snippet or input text file and a list of zero or more AnnotationPayload protos (called annotations), which have classification detail populated. A single text snippet or file will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any text snippet or file failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps input text snippet or input text file followed by exactly one [`google.rpc.Status`](https: //github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) containing only `code` and `message`. \- For Text Sentiment: In the created directory files `text_sentiment_1.jsonl`, `text_sentiment_2.jsonl`,...,\ `text_sentiment_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found. :: Each .JSONL file will contain, per line, a JSON representation of a proto that wraps input text snippet or input text file and a list of zero or more AnnotationPayload protos (called annotations), which have text_sentiment detail populated. A single text snippet or file will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any text snippet or file failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps input text snippet or input text file followed by exactly one [`google.rpc.Status`](https: //github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) containing only `code` and `message`. \- For Text Extraction: In the created directory files `text_extraction_1.jsonl`, `text_extraction_2.jsonl`,...,\ `text_extraction_N.jsonl` will be created, where N may be 1, and depends on the total number of inputs and annotations found. The contents of these .JSONL file(s) depend on whether the input used inline text, or documents. If input was inline, then each .JSONL file will contain, per line, a JSON representation of a proto that wraps given in request text snippet's "id" (if specified), followed by input text snippet, and a list of zero or more AnnotationPayload protos (called annotations), which have text_extraction detail populated. A single text snippet will be listed only once with all its annotations, and its annotations will never be split across files. If input used documents, then each .JSONL file will contain, per line, a JSON representation of a proto that wraps given in request document proto, followed by its OCR-ed representation in the form of a text snippet, finally followed by a list of zero or more AnnotationPayload protos (called annotations), which have text_extraction detail populated and refer, via their indices, to the OCR-ed text snippet. A single document (and its text snippet) will be listed only once with all its annotations, and its annotations will never be split across files. If prediction for any text snippet failed (partially or completely), then additional `errors_1.jsonl`, `errors_2.jsonl`,..., `errors_N.jsonl` files will be created (N depends on total number of failed predictions). These files will have a JSON representation of a proto that wraps either the "id" : "<id_value>" (in case of inline) or the document proto (in case of document) but here followed by exactly one [`google.rpc.Status`](https: //github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) containing only `code` and `message`. \- For Tables: Output depends on whether gcs_destination or bigquery_destination is set (either is allowed). GCS case: In the created directory files `tables_1.csv`, `tables_2.csv`,..., `tables_N.csv` will be created, where N may be 1, and depends on the total number of the successfully predicted rows. For all CLASSIFICATION prediction_type-s: Each .csv file will contain a header, listing all columns' display_name-s given on input followed by M target column names in the format of "<target_column_specs display_name>__score" where M is the number of distinct target values, i.e. number of distinct values in the target column of the table used to train the model. Subsequent lines will contain the respective values of successfully predicted rows, with the last, i.e. the target, columns having the corresponding prediction scores. For REGRESSION and FORECASTING prediction_type-s: Each .csv file will contain a header, listing all columns' display_name-s given on input followed by the predicted target column with name in the format of "predicted_<target_column_specs display_name>" Subsequent lines will contain the respective values of successfully predicted rows, with the last, i.e. the target, column having the predicted target value. If prediction for any rows failed, then an additional `errors_1.csv`, `errors_2.csv`,..., `errors_N.csv` will be created (N depends on total number of failed rows). These files will have analogous format as `tables_*.csv`, but always with a single target column having [`google.rpc.Status`](https: //github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) represented as a JSON string, and containing only `code` and `message`. BigQuery case: bigquery_destination pointing to a BigQuery project must be set. In the given project a new dataset will be created with name `prediction_<model-display-name>_<timestamp-of-prediction-call>` where will be made BigQuery-dataset-name compatible (e.g. most special characters will become underscores), and timestamp will be in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset two tables will be created, `predictions`, and `errors`. The `predictions` table's column names will be the input columns' display_name-s followed by the target column with name in the format of "predicted_<target_column_specs display_name>" The input feature columns will contain the respective values of successfully predicted rows, with the target column having an ARRAY of AnnotationPayloads, represented as STRUCT-s, containing TablesAnnotation. The `errors` table contains rows for which the prediction has failed, it has analogous input columns while the target column name is in the format of "errors_<target_column_specs

display_name>", and as a value has

[`google.rpc.Status`](https: //github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) represented as a STRUCT, and containing only `code` and `message`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchPredictRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictRequest)

Request message for PredictionService.BatchPredict.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictRequest.ParamsEntry)

The abstract base class for a message.

### [BatchPredictResult](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictResult)

Result of the Batch Predict. This message is returned in `response][google.longrunning.Operation.response]` of the operation returned by the PredictionService.BatchPredict.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictResult.MetadataEntry)

The abstract base class for a message.

### [BigQueryDestination](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BigQueryDestination)

The BigQuery location for the output content.

### [BigQuerySource](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BigQuerySource)

The BigQuery location for the input content.

### [BoundingBoxMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BoundingBoxMetricsEntry)

Bounding box matching model metrics for a single intersection-over-union threshold and multiple label match confidence thresholds.

### [ConfidenceMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BoundingBoxMetricsEntry.ConfidenceMetricsEntry)

Metrics for a single confidence threshold.

### [BoundingPoly](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BoundingPoly)

A bounding polygon of a detected object on a plane. On output both vertices and normalized_vertices are provided. The polygon is formed by connecting vertices in the order they are listed.

### [CategoryStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CategoryStats)

The data statistics of a series of CATEGORY values.

### [SingleCategoryStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CategoryStats.SingleCategoryStats)

The statistics of a single CATEGORY value.

### [ClassificationAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ClassificationAnnotation)

Contains annotation details specific to classification.

### [ClassificationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ClassificationEvaluationMetrics)

Model evaluation metrics for classification problems. Note: For Video Classification this metrics only describe quality of the Video Classification predictions of "segment_classification" type.

### [ConfidenceMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)

Metrics for a single confidence threshold.

### [ConfusionMatrix](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ClassificationEvaluationMetrics.ConfusionMatrix)

Confusion matrix of the model running the classification.

### [Row](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ClassificationEvaluationMetrics.ConfusionMatrix.Row)

Output only. A row in the confusion matrix.

### [ClassificationType](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ClassificationType)

Type of the classification problem.

### [ColumnSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ColumnSpec)

A representation of a column in a relational table. When listing them, column specs are returned in the same order in which they were given on import . Used by:

  * Tables



### [CorrelatedColumn](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ColumnSpec.CorrelatedColumn)

Identifies the table's column, and its correlation with the column this ColumnSpec describes.

### [CorrelationStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CorrelationStats)

A correlation statistics between two series of DataType values. The series may have differing DataType-s, but within a single series the DataType must be the same.

### [CreateDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CreateDatasetRequest)

Request message for AutoMl.CreateDataset.

### [CreateModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CreateModelOperationMetadata)

Details of CreateModel operation.

### [CreateModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CreateModelRequest)

Request message for AutoMl.CreateModel.

### [DataStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DataStats)

The data statistics of a series of values that share the same DataType.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataType](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DataType)

Indicated the type of data that can be stored in a structured data entity (e.g. a table).

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Dataset)

A workspace for solving a single, particular machine learning (ML) problem. A workspace contains examples that may be annotated.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeleteDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeleteDatasetRequest)

Request message for AutoMl.DeleteDataset.

### [DeleteModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeleteModelRequest)

Request message for AutoMl.DeleteModel.

### [DeleteOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeleteOperationMetadata)

Details of operations that perform deletes of any entities.

### [DeployModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeployModelOperationMetadata)

Details of DeployModel operation.

### [DeployModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeployModelRequest)

Request message for AutoMl.DeployModel.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Document](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Document)

A structured text document e.g. a PDF.

### [Layout](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Document.Layout)

Describes the layout information of a text_segment in the document.

### [TextSegmentType](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Document.Layout.TextSegmentType)

The type of TextSegment in the context of the original document.

### [DocumentDimensions](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DocumentDimensions)

Message that describes dimension of a document.

### [DocumentDimensionUnit](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DocumentDimensions.DocumentDimensionUnit)

Unit of the document dimension.

### [DocumentInputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DocumentInputConfig)

Input configuration of a Document.

### [DoubleRange](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DoubleRange)

A range between two double numbers.

### [ExamplePayload](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExamplePayload)

Example data used for training or prediction.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportDataOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportDataOperationMetadata)

Details of ExportData operation.

### [ExportDataOutputInfo](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportDataOperationMetadata.ExportDataOutputInfo)

Further describes this export data's output. Supplements OutputConfig.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportDataRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportDataRequest)

Request message for AutoMl.ExportData.

### [ExportEvaluatedExamplesOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesOperationMetadata)

Details of EvaluatedExamples operation.

### [ExportEvaluatedExamplesOutputInfo](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesOperationMetadata.ExportEvaluatedExamplesOutputInfo)

Further describes the output of the evaluated examples export. Supplements

ExportEvaluatedExamplesOutputConfig.

### [ExportEvaluatedExamplesOutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesOutputConfig)

Output configuration for ExportEvaluatedExamples Action. Note that this call is available only for 30 days since the moment the model was evaluated. The output depends on the domain, as follows (note that only examples from the TEST set are exported):

  * For Tables:



bigquery_destination pointing to a BigQuery project must be set. In the given project a new dataset will be created with name

`export_evaluated_examples_<model-display-name>_<timestamp-of-export-call>` where will be made BigQuery-dataset-name compatible (e.g. most special characters will become underscores), and timestamp will be in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset an `evaluated_examples` table will be created. It will have all the same columns as the

primary_table of the dataset from which the model was created, as they were at the moment of model's evaluation (this includes the target column with its ground truth), followed by a column called "predicted_<target_column>". That last column will contain the model's prediction result for each respective row, given as ARRAY of AnnotationPayloads, represented as STRUCT-s, containing TablesAnnotation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportEvaluatedExamplesRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesRequest)

Request message for AutoMl.ExportEvaluatedExamples.

### [ExportModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportModelOperationMetadata)

Details of ExportModel operation.

### [ExportModelOutputInfo](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportModelOperationMetadata.ExportModelOutputInfo)

Further describes the output of model export. Supplements

ModelExportOutputConfig.

### [ExportModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportModelRequest)

Request message for AutoMl.ExportModel. Models need to be enabled for exporting, otherwise an error code will be returned.

### [Float64Stats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Float64Stats)

The data statistics of a series of FLOAT64 values.

### [HistogramBucket](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Float64Stats.HistogramBucket)

A bucket of a histogram.

### [GcrDestination](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GcrDestination)

The GCR location where the image must be pushed to.

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GcsDestination)

The Google Cloud Storage location where the output is to be written to.

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GcsSource)

The Google Cloud Storage location for the input content.

### [GetAnnotationSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetAnnotationSpecRequest)

Request message for AutoMl.GetAnnotationSpec.

### [GetColumnSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetColumnSpecRequest)

Request message for AutoMl.GetColumnSpec.

### [GetDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetDatasetRequest)

Request message for AutoMl.GetDataset.

### [GetModelEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetModelEvaluationRequest)

Request message for AutoMl.GetModelEvaluation.

### [GetModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetModelRequest)

Request message for AutoMl.GetModel.

### [GetTableSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetTableSpecRequest)

Request message for AutoMl.GetTableSpec.

### [Image](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Image)

A representation of an image. Only images up to 30MB in size are supported.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImageClassificationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageClassificationDatasetMetadata)

Dataset metadata that is specific to image classification.

### [ImageClassificationModelDeploymentMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageClassificationModelDeploymentMetadata)

Model deployment metadata specific to Image Classification.

### [ImageClassificationModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageClassificationModelMetadata)

Model metadata for image classification.

### [ImageObjectDetectionAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageObjectDetectionAnnotation)

Annotation details for image object detection.

### [ImageObjectDetectionDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageObjectDetectionDatasetMetadata)

Dataset metadata specific to image object detection.

### [ImageObjectDetectionEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageObjectDetectionEvaluationMetrics)

Model evaluation metrics for image object detection problems. Evaluates prediction quality of labeled bounding boxes.

### [ImageObjectDetectionModelDeploymentMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageObjectDetectionModelDeploymentMetadata)

Model deployment metadata specific to Image Object Detection.

### [ImageObjectDetectionModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageObjectDetectionModelMetadata)

Model metadata specific to image object detection.

### [ImportDataOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImportDataOperationMetadata)

Details of ImportData operation.

### [ImportDataRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImportDataRequest)

Request message for AutoMl.ImportData.

### [InputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.InputConfig)

Input configuration for ImportData Action.

The format of input depends on dataset_metadata the Dataset into which the import is happening has. As input source the gcs_source is expected, unless specified otherwise. Additionally any input .CSV file by itself must be 100MB or smaller, unless specified otherwise. If an "example" file (that is, image, video etc.) with identical content (even if it had different GCS_FILE_PATH) is mentioned multiple times, then its label, bounding boxes etc. are appended. The same file should be always provided with the same ML_USE and GCS_FILE_PATH, if it is not, then these values are nondeterministically selected from the given ones.

The formats are represented in EBNF with commas being literal and with non-terminal symbols defined near the end of this comment. The formats are:

  * For Image Classification: CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH,LABEL,LABEL,... GCS_FILE_PATH leads to image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG, .WEBP, .BMP, .TIFF, .ICO For MULTICLASS classification type, at most one LABEL is allowed per image. If an image has not yet been labeled, then it should be mentioned just once with no LABEL. Some sample rows: TRAIN,gs://folder/image1.jpg,daisy TEST,gs://folder/image2.jpg,dandelion,tulip,rose UNASSIGNED,gs://folder/image3.jpg,daisy UNASSIGNED,gs://folder/image4.jpg

  * For Image Object Detection: CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH,(LABEL,BOUNDING_BOX | ,,,,,,,) GCS_FILE_PATH leads to image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. Each image is assumed to be exhaustively labeled. The minimum allowed BOUNDING_BOX edge length is 0.01, and no more than 500 BOUNDING_BOX-es per image are allowed (one BOUNDING_BOX is defined per line). If an image has not yet been labeled, then it should be mentioned just once with no LABEL and the ",,,,,,," in place of the BOUNDING_BOX. For images which are known to not contain any bounding boxes, they should be labelled explictly as "NEGATIVE_IMAGE", followed by ",,,,,,," in place of the BOUNDING_BOX. Sample rows: TRAIN,gs://folder/image1.png,car,0.1,0.1,,,0.3,0.3,, TRAIN,gs://folder/image1.png,bike,.7,.6,,,.8,.9,, UNASSIGNED,gs://folder/im2.png,car,0.1,0.1,0.2,0.1,0.2,0.3,0.1,0.3 TEST,gs://folder/im3.png,,,,,,,,, TRAIN,gs://folder/im4.png,NEGATIVE_IMAGE,,,,,,,,,

  * For Video Classification: CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH where ML_USE VALIDATE value should not be used. The GCS_FILE_PATH should lead to another .csv file which describes examples that have given ML_USE, using the following row format: GCS_FILE_PATH,(LABEL,TIME_SEGMENT_START,TIME_SEGMENT_END | ,,) Here GCS_FILE_PATH leads to a video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. TIME_SEGMENT_START and TIME_SEGMENT_END must be within the length of the video, and end has to be after the start. Any segment of a video which has one or more labels on it, is considered a hard negative for all other labels. Any segment with no labels on it is considered to be unknown. If a whole video is unknown, then it shuold be mentioned just once with ",," in place of LABEL, TIME_SEGMENT_START,TIME_SEGMENT_END. Sample top level CSV file: TRAIN,gs://folder/train_videos.csv TEST,gs://folder/test_videos.csv UNASSIGNED,gs://folder/other_videos.csv Sample rows of a CSV file for a particular ML_USE: gs://folder/video1.avi,car,120,180.000021 gs://folder/video1.avi,bike,150,180.000021 gs://folder/vid2.avi,car,0,60.5 gs://folder/vid3.avi,,,

  * For Video Object Tracking: CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH where ML_USE VALIDATE value should not be used. The GCS_FILE_PATH should lead to another .csv file which describes examples that have given ML_USE, using one of the following row format: GCS_FILE_PATH,LABEL,[INSTANCE_ID],TIMESTAMP,BOUNDING_BOX or GCS_FILE_PATH,,,,,,,,,, Here GCS_FILE_PATH leads to a video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. Providing INSTANCE_IDs can help to obtain a better model. When a specific labeled entity leaves the video frame, and shows up afterwards it is not required, albeit preferable, that the same INSTANCE_ID is given to it. TIMESTAMP must be within the length of the video, the BOUNDING_BOX is assumed to be drawn on the closest video's frame to the TIMESTAMP. Any mentioned by the TIMESTAMP frame is expected to be exhaustively labeled and no more than 500 BOUNDING_BOX-es per frame are allowed. If a whole video is unknown, then it should be mentioned just once with ",,,,,,,,,," in place of LABEL, [INSTANCE_ID],TIMESTAMP,BOUNDING_BOX. Sample top level CSV file: TRAIN,gs://folder/train_videos.csv TEST,gs://folder/test_videos.csv UNASSIGNED,gs://folder/other_videos.csv Seven sample rows of a CSV file for a particular ML_USE: gs://folder/video1.avi,car,1,12.10,0.8,0.8,0.9,0.8,0.9,0.9,0.8,0.9 gs://folder/video1.avi,car,1,12.90,0.4,0.8,0.5,0.8,0.5,0.9,0.4,0.9 gs://folder/video1.avi,car,2,12.10,.4,.2,.5,.2,.5,.3,.4,.3 gs://folder/video1.avi,car,2,12.90,.8,.2,,,.9,.3,, gs://folder/video1.avi,bike,,12.50,.45,.45,,,.55,.55,, gs://folder/video2.avi,car,1,0,.1,.9,,,.9,.1,, gs://folder/video2.avi,,,,,,,,,,,

  * For Text Extraction: CSV file(s) with each line in format: ML_USE,GCS_FILE_PATH GCS_FILE_PATH leads to a .JSONL (that is, JSON Lines) file which either imports text in-line or as documents. Any given .JSONL file must be 100MB or smaller. The in-line .JSONL file contains, per line, a proto that wraps a TextSnippet proto (in json representation) followed by one or more AnnotationPayload protos (called annotations), which have display_name and text_extraction detail populated. The given text is expected to be annotated exhaustively, for example, if you look for animals and text contains "dolphin" that is not labeled, then "dolphin" is assumed to not be an animal. Any given text snippet content must be 10KB or smaller, and also be UTF-8 NFC encoded (ASCII already is). The document .JSONL file contains, per line, a proto that wraps a Document proto. The Document proto must have either document_text or input_config set. In document_text case, the Document proto may also contain the spatial information of the document, including layout, document dimension and page number. In input_config case, only PDF documents are supported now, and each document may be up to 2MB large. Currently, annotations on documents cannot be specified at import. Three sample CSV rows: TRAIN,gs://folder/file1.jsonl VALIDATE,gs://folder/file2.jsonl TEST,gs://folder/file3.jsonl Sample in-line JSON Lines file for entity extraction (presented here with artificial line breaks, but the only actual line break is denoted by \n).: { "document": { "document_text": {"content": "dog cat"} "layout": [ { "text_segment": { "start_offset": 0, "end_offset": 3, }, "page_number": 1, "bounding_poly": { "normalized_vertices": [ {"x": 0.1, "y": 0.1}, {"x": 0.1, "y": 0.3}, {"x": 0.3, "y": 0.3}, {"x": 0.3, "y": 0.1}, ], }, "text_segment_type": TOKEN, }, { "text_segment": { "start_offset": 4, "end_offset": 7, }, "page_number": 1, "bounding_poly": { "normalized_vertices": [ {"x": 0.4, "y": 0.1}, {"x": 0.4, "y": 0.3}, {"x": 0.8, "y": 0.3}, {"x": 0.8, "y": 0.1}, ], }, "text_segment_type": TOKEN, }

::
        
        ],
             "document_dimensions": {
               "width": 8.27,
               "height": 11.69,
               "unit": INCH,
             }
             "page_count": 1,
           },
           "annotations": [
             {
               "display_name": "animal",
               "text_extraction": {"text_segment": {"start_offset": 0,
               "end_offset": 3}}
             },
             {
               "display_name": "animal",
               "text_extraction": {"text_segment": {"start_offset": 4,
               "end_offset": 7}}
             }
           ],
         }\n
         {
            "text_snippet": {
              "content": "This dog is good."
            },
            "annotations": [
              {
                "display_name": "animal",
                "text_extraction": {
                  "text_segment": {"start_offset": 5, "end_offset": 8}
                }
              }
            ]
         }
        

Sample document JSON Lines file (presented here with artificial line breaks, but the only actual line break is denoted by \n).: { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document1.pdf" ] } } } }\n { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document2.pdf" ] } } } }

  * For Text Classification: CSV file(s) with each line in format: ML_USE,(TEXT_SNIPPET | GCS_FILE_PATH),LABEL,LABEL,... TEXT_SNIPPET and GCS_FILE_PATH are distinguished by a pattern. If the column content is a valid gcs file path, i.e. prefixed by "gs://", it will be treated as a GCS_FILE_PATH, else if the content is enclosed within double quotes (""), it is treated as a TEXT_SNIPPET. In the GCS_FILE_PATH case, the path must lead to a .txt file with UTF-8 encoding, for example, "gs://folder/content.txt", and the content in it is extracted as a text snippet. In TEXT_SNIPPET case, the column content excluding quotes is treated as to be imported text snippet. In both cases, the text snippet/file size must be within 128kB. Maximum 100 unique labels are allowed per CSV row. Sample rows: TRAIN,"They have bad food and very rude",RudeService,BadFood TRAIN,gs://folder/content.txt,SlowService TEST,"Typically always bad service there.",RudeService VALIDATE,"Stomach ache to go.",BadFood

  * For Text Sentiment: CSV file(s) with each line in format: ML_USE,(TEXT_SNIPPET | GCS_FILE_PATH),SENTIMENT TEXT_SNIPPET and GCS_FILE_PATH are distinguished by a pattern. If the column content is a valid gcs file path, that is, prefixed by "gs://", it is treated as a GCS_FILE_PATH, otherwise it is treated as a TEXT_SNIPPET. In the GCS_FILE_PATH case, the path must lead to a .txt file with UTF-8 encoding, for example, "gs://folder/content.txt", and the content in it is extracted as a text snippet. In TEXT_SNIPPET case, the column content itself is treated as to be imported text snippet. In both cases, the text snippet must be up to 500 characters long. Sample rows: TRAIN,"@freewrytin this is way too good for your product",2 TRAIN,"I need this product so bad",3 TEST,"Thank you for this product.",4 VALIDATE,gs://folder/content.txt,2

  * For Tables: Either gcs_source or




bigquery_source can be used. All inputs is concatenated into a single

primary_table For gcs_source: CSV file(s), where the first row of the first file is the header, containing unique column names. If the first row of a subsequent file is the same as the header, then it is also treated as a header. All other rows contain values for the corresponding columns. Each .CSV file by itself must be 10GB or smaller, and their total size must be 100GB or smaller. First three sample rows of a CSV file: "Id","First Name","Last Name","Dob","Addresses"

"1","John","Doe","1968-01-22","[{"status":"current","address":"123_First_Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456_Main_Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]"

"2","Jane","Doe","1980-10-16","[{"status":"current","address":"789_Any_Avenue","city":"Albany","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321_Main_Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]} For bigquery_source: An URI of a BigQuery table. The user data size of the BigQuery table must be 100GB or smaller. An imported table must have between 2 and 1,000 columns, inclusive, and between 1000 and 100,000,000 rows, inclusive. There are at most 5 import data running in parallel. Definitions: ML_USE = "TRAIN" | "VALIDATE" | "TEST" | "UNASSIGNED" Describes how the given example (file) should be used for model training. "UNASSIGNED" can be used when user has no preference. GCS_FILE_PATH = A path to file on GCS, e.g. "gs://folder/image1.png". LABEL = A display name of an object on an image, video etc., e.g. "dog". Must be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores(_), and ASCII digits 0-9. For each label an AnnotationSpec is created which display_name becomes the label; AnnotationSpecs are given back in predictions. INSTANCE_ID = A positive integer that identifies a specific instance of a labeled entity on an example. Used e.g. to track two cars on a video while being able to tell apart which one is which. BOUNDING_BOX = VERTEX,VERTEX,VERTEX,VERTEX | VERTEX,,,VERTEX,, A rectangle parallel to the frame of the example (image, video). If 4 vertices are given they are connected by edges in the order provided, if 2 are given they are recognized as diagonally opposite vertices of the rectangle. VERTEX = COORDINATE,COORDINATE First coordinate is horizontal (x), the second is vertical (y). COORDINATE = A float in 0 to 1 range, relative to total length of image or video in given dimension. For fractions the leading non-decimal 0 can be omitted (i.e. 0.3 = .3). Point 0,0 is in top left. TIME_SEGMENT_START = TIME_OFFSET Expresses a beginning, inclusive, of a time segment within an example that has a time dimension (e.g. video). TIME_SEGMENT_END = TIME_OFFSET Expresses an end, exclusive, of a time segment within an example that has a time dimension (e.g. video). TIME_OFFSET = A number of seconds as measured from the start of an example (e.g. video). Fractions are allowed, up to a microsecond precision. "inf" is allowed, and it means the end of the example. TEXT_SNIPPET = A content of a text snippet, UTF-8 encoded, enclosed within double quotes (""). SENTIMENT = An integer between 0 and Dataset.text_sentiment_dataset_metadata.sentiment_max (inclusive). Describes the ordinal of the sentiment - higher value means a more positive sentiment. All the values are completely relative, i.e. neither 0 needs to mean a negative or neutral sentiment nor sentiment_max needs to mean a positive one - it is just required that 0 is the least positive sentiment in the data, and sentiment_max is the most positive one. The SENTIMENT shouldn't be confused with "score" or "magnitude" from the previous Natural Language Sentiment Analysis API. All SENTIMENT values between 0 and sentiment_max must be represented in the imported data. On prediction the same 0 to sentiment_max range will be used. The difference between neighboring sentiment values needs not to be uniform, e.g. 1 and 2 may be similar whereas the difference between 2 and 3 may be huge.

Errors: If any of the provided CSV files can't be parsed or if more than certain percent of CSV rows cannot be processed then the operation fails and nothing is imported. Regardless of overall success or failure the per-row failures, up to a certain count cap, is listed in Operation.metadata.partial_failures.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.InputConfig.ParamsEntry)

The abstract base class for a message.

### [ListColumnSpecsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsRequest)

Request message for AutoMl.ListColumnSpecs.

### [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse)

Response message for AutoMl.ListColumnSpecs.

### [ListDatasetsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsRequest)

Request message for AutoMl.ListDatasets.

### [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse)

Response message for AutoMl.ListDatasets.

### [ListModelEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsRequest)

Request message for AutoMl.ListModelEvaluations.

### [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse)

Response message for AutoMl.ListModelEvaluations.

### [ListModelsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsRequest)

Request message for AutoMl.ListModels.

### [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse)

Response message for AutoMl.ListModels.

### [ListTableSpecsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsRequest)

Request message for AutoMl.ListTableSpecs.

### [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse)

Response message for AutoMl.ListTableSpecs.

### [Model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Model)

API proto representing a trained machine learning model.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeploymentState](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Model.DeploymentState)

Deployment state of the model.

### [ModelEvaluation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ModelEvaluation)

Evaluation results of a model.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ModelExportOutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ModelExportOutputConfig)

Output configuration for ModelExport Action.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ModelExportOutputConfig.ParamsEntry)

The abstract base class for a message.

### [NormalizedVertex](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.NormalizedVertex)

A vertex represents a 2D point in the image. The normalized vertex coordinates are between 0 to 1 fractions relative to the original plane (image, video). E.g. if the plane (e.g. whole image) would have size 10 x 20 then a point with normalized coordinates (0.1, 0.3) would be at the position (1, 6) on that plane.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.OperationMetadata)

Metadata used across all long running operations returned by AutoML API.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [OutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.OutputConfig)

  * For Translation: CSV file `translation.csv`, with each line in format: ML_USE,GCS_FILE_PATH GCS_FILE_PATH leads to a .TSV file which describes examples that have given ML_USE, using the following row format per line: TEXT_SNIPPET (in source language) \t TEXT_SNIPPET (in target language)

    * For Tables: Output depends on whether the dataset was imported from GCS or BigQuery. GCS case:



gcs_destination must be set. Exported are CSV file(s) `tables_1.csv`, `tables_2.csv`,...,\ `tables_N.csv` with each having as header line the table's column names, and all other lines contain values for the header columns. BigQuery case:

bigquery_destination pointing to a BigQuery project must be set. In the given project a new dataset will be created with name

`export_data_<automl-dataset-display-name>_<timestamp-of-export-call>` where will be made BigQuery-dataset-name compatible (e.g. most special characters will become underscores), and timestamp will be in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In that dataset a new table called `primary_table` will be created, and filled with precisely the same data as this obtained on import.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PredictRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.PredictRequest)

Request message for PredictionService.Predict.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.PredictRequest.ParamsEntry)

The abstract base class for a message.

### [PredictResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.PredictResponse)

Response message for PredictionService.Predict.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.PredictResponse.MetadataEntry)

The abstract base class for a message.

### [RegressionEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.RegressionEvaluationMetrics)

Metrics for regression problems.

### [Row](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Row)

A representation of a row in a relational table.

### [StringStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.StringStats)

The data statistics of a series of STRING values.

### [UnigramStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.StringStats.UnigramStats)

The statistics of a unigram.

### [StructStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.StructStats)

The data statistics of a series of STRUCT values.

### [FieldStatsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.StructStats.FieldStatsEntry)

The abstract base class for a message.

### [StructType](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.StructType)

`StructType` defines the DataType-s of a STRUCT type.

### [FieldsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.StructType.FieldsEntry)

The abstract base class for a message.

### [TableSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TableSpec)

A specification of a relational table. The table's schema is represented via its child column specs. It is pre-populated as part of ImportData by schema inference algorithm, the version of which is a required parameter of ImportData InputConfig. Note: While working with a table, at times the schema may be inconsistent with the data in the table (e.g. string in a FLOAT64 column). The consistency validation is done upon creation of a model. Used by:

  * Tables



### [TablesAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TablesAnnotation)

Contains annotation details specific to Tables.

### [TablesDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TablesDatasetMetadata)

Metadata for a dataset used for AutoML Tables.

### [TargetColumnCorrelationsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TablesDatasetMetadata.TargetColumnCorrelationsEntry)

The abstract base class for a message.

### [TablesModelColumnInfo](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TablesModelColumnInfo)

An information specific to given column and Tables Model, in context of the Model and the predictions created by it.

### [TablesModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TablesModelMetadata)

Model metadata specific to AutoML Tables.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TextClassificationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextClassificationDatasetMetadata)

Dataset metadata for classification.

### [TextClassificationModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextClassificationModelMetadata)

Model metadata that is specific to text classification.

### [TextExtractionAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextExtractionAnnotation)

Annotation for identifying spans of text.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TextExtractionDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextExtractionDatasetMetadata)

Dataset metadata that is specific to text extraction

### [TextExtractionEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextExtractionEvaluationMetrics)

Model evaluation metrics for text extraction problems.

### [ConfidenceMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry)

Metrics for a single confidence threshold.

### [TextExtractionModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextExtractionModelMetadata)

Model metadata that is specific to text extraction.

### [TextSegment](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextSegment)

A contiguous part of a text (string), assuming it has an UTF-8 NFC encoding.

### [TextSentimentAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextSentimentAnnotation)

Contains annotation details specific to text sentiment.

### [TextSentimentDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextSentimentDatasetMetadata)

Dataset metadata for text sentiment.

### [TextSentimentEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextSentimentEvaluationMetrics)

Model evaluation metrics for text sentiment problems.

### [TextSentimentModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextSentimentModelMetadata)

Model metadata that is specific to text sentiment.

### [TextSnippet](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextSnippet)

A representation of a text snippet.

### [TimeSegment](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TimeSegment)

A time period inside of an example that has a time dimension (e.g. video).

### [TimestampStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TimestampStats)

The data statistics of a series of TIMESTAMP values.

### [GranularStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TimestampStats.GranularStats)

Stats split by a defined in context granularity.

### [BucketsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TimestampStats.GranularStats.BucketsEntry)

The abstract base class for a message.

### [GranularStatsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TimestampStats.GranularStatsEntry)

The abstract base class for a message.

### [TranslationAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TranslationAnnotation)

Annotation details specific to translation.

### [TranslationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TranslationDatasetMetadata)

Dataset metadata that is specific to translation.

### [TranslationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TranslationEvaluationMetrics)

Evaluation metrics for the dataset.

### [TranslationModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TranslationModelMetadata)

Model metadata that is specific to translation.

### [TypeCode](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TypeCode)

`TypeCode` is used as a part of DataType.
    
    
        <xref uid="google.cloud.automl.v1beta1.DataType.list_element_type">list_element_type</xref>.
    STRUCT (9):
        Encoded as `struct`, where field values are represented
        according to
        <xref uid="google.cloud.automl.v1beta1.DataType.struct_type">struct_type</xref>.
    CATEGORY (10):
        Values of this type are not further understood by AutoML,
        e.g. AutoML is unable to tell the order of values (as it
        could with FLOAT64), or is unable to say if one value
        contains another (as it could with STRING). Encoded as
        `string` (bytes should be base64-encoded, as described in
        RFC 4648, section 4).
    

### [UndeployModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UndeployModelOperationMetadata)

Details of UndeployModel operation.

### [UndeployModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UndeployModelRequest)

Request message for AutoMl.UndeployModel.

### [UpdateColumnSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateColumnSpecRequest)

Request message for AutoMl.UpdateColumnSpec

### [UpdateDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateDatasetRequest)

Request message for AutoMl.UpdateDataset

### [UpdateTableSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateTableSpecRequest)

Request message for AutoMl.UpdateTableSpec

### [VideoClassificationAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoClassificationAnnotation)

Contains annotation details specific to video classification.

### [VideoClassificationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoClassificationDatasetMetadata)

Dataset metadata specific to video classification. All Video Classification datasets are treated as multi label.

### [VideoClassificationModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoClassificationModelMetadata)

Model metadata specific to video classification.

### [VideoObjectTrackingAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoObjectTrackingAnnotation)

Annotation details for video object tracking.

### [VideoObjectTrackingDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoObjectTrackingDatasetMetadata)

Dataset metadata specific to video object tracking.

### [VideoObjectTrackingEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoObjectTrackingEvaluationMetrics)

Model evaluation metrics for video object tracking problems. Evaluates prediction quality of both labeled bounding boxes and labeled tracks (i.e. series of bounding boxes sharing same label and instance ID).

### [VideoObjectTrackingModelMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoObjectTrackingModelMetadata)

Model metadata specific to video object tracking.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers)

API documentation for `automl_v1.services.auto_ml.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers)

API documentation for `automl_v1beta1.services.auto_ml.pagers` module.

### [gcs_client](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.gcs_client)

Wraps the Google Cloud Storage client library for use in tables helper.

### [tables_client](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client)

A tables helper for the google.cloud.automl_v1beta1 AutoML API

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
