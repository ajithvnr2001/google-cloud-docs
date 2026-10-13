---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder
title: Class InputConfig.Builder (2.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:51.976630+00:00
---

# Class InputConfig.Builder (2.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InputConfig.Builder (2.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.95.0 (latest)  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.18  2.2.3  2.1.23 
    
    
    public static final class InputConfig.Builder extends GeneratedMessage.Builder<InputConfig.Builder> implements InputConfigOrBuilder

Input configuration for AutoMl.ImportData action.

The format of input depends on dataset_metadata the Dataset into which the import is happening has. As input source the gcs_source is expected, unless specified otherwise. Additionally any input .CSV file by itself must be 100MB or smaller, unless specified otherwise. If an "example" file (that is, image, video etc.) with identical content (even if it had different `GCS_FILE_PATH`) is mentioned multiple times, then its label, bounding boxes etc. are appended. The same file should be always provided with the same `ML_USE` and `GCS_FILE_PATH`, if it is not, then these values are nondeterministically selected from the given ones.

The formats are represented in EBNF with commas being literal and with non-terminal symbols defined near the end of this comment. The formats are:

#### AutoML Vision

##### Classification

See [Preparing your training data](https://cloud.google.com/vision/automl/docs/prepare) for more information.

CSV file(s) with each line in format:

ML_USE,GCS_FILE_PATH,LABEL,LABEL,...

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:
  * `TRAIN` \- Rows in this file are used to train the model.
  * `TEST` \- Rows in this file are used to test the model during training.
  * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing.

  * `GCS_FILE_PATH` \- The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG, .WEBP, .BMP, .TIFF, .ICO.

  * `LABEL` \- A label that identifies the object in the image.

For the `MULTICLASS` classification type, at most one `LABEL` is allowed per image. If an image has not yet been labeled, then it should be mentioned just once with no `LABEL`.

Some sample rows:

TRAIN,gs://folder/image1.jpg,daisy TEST,gs://folder/image2.jpg,dandelion,tulip,rose UNASSIGNED,gs://folder/image3.jpg,daisy UNASSIGNED,gs://folder/image4.jpg




##### Object Detection

See [Preparing your training data](https://cloud.google.com/vision/automl/object-detection/docs/prepare) for more information.

A CSV file(s) with each line in format:

ML_USE,GCS_FILE_PATH,[LABEL],(BOUNDING_BOX | ,,,,,,,)

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:
  * `TRAIN` \- Rows in this file are used to train the model.
  * `TEST` \- Rows in this file are used to test the model during training.
  * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing.

  * `GCS_FILE_PATH` \- The Google Cloud Storage location of an image of up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG. Each image is assumed to be exhaustively labeled.

  * `LABEL` \- A label that identifies the object in the image specified by the `BOUNDING_BOX`.

  * `BOUNDING BOX` \- The vertices of an object in the example image. The minimum allowed `BOUNDING_BOX` edge length is 0.01, and no more than 500 `BOUNDING_BOX` instances per image are allowed (one `BOUNDING_BOX` per line). If an image has no looked for objects then it should be mentioned just once with no LABEL and the ",,,,,,," in place of the `BOUNDING_BOX`.

**Four sample rows:**

TRAIN,gs://folder/image1.png,car,0.1,0.1,,,0.3,0.3,, TRAIN,gs://folder/image1.png,bike,.7,.6,,,.8,.9,, UNASSIGNED,gs://folder/im2.png,car,0.1,0.1,0.2,0.1,0.2,0.3,0.1,0.3 TEST,gs://folder/im3.png,,,,,,,,, </section> </div>




#### AutoML Video Intelligence

##### Classification

See [Preparing your training data](https://cloud.google.com/video-intelligence/automl/docs/prepare) for more information.

CSV file(s) with each line in format:

ML_USE,GCS_FILE_PATH

For `ML_USE`, do not use `VALIDATE`.

`GCS_FILE_PATH` is the path to another .csv file that describes training example for a given `ML_USE`, using the following row format:

GCS_FILE_PATH,(LABEL,TIME_SEGMENT_START,TIME_SEGMENT_END | ,,)

Here `GCS_FILE_PATH` leads to a video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI.

`TIME_SEGMENT_START` and `TIME_SEGMENT_END` must be within the length of the video, and the end time must be after the start time. Any segment of a video which has one or more labels on it, is considered a hard negative for all other labels. Any segment with no labels on it is considered to be unknown. If a whole video is unknown, then it should be mentioned just once with ",," in place of `LABEL, TIME_SEGMENT_START,TIME_SEGMENT_END`.

Sample top level CSV file:

TRAIN,gs://folder/train_videos.csv TEST,gs://folder/test_videos.csv UNASSIGNED,gs://folder/other_videos.csv

Sample rows of a CSV file for a particular ML_USE:

gs://folder/video1.avi,car,120,180.000021 gs://folder/video1.avi,bike,150,180.000021 gs://folder/vid2.avi,car,0,60.5 gs://folder/vid3.avi,,,

##### Object Tracking

See [Preparing your training data](https://docs.cloud.google.com/video-intelligence/automl/object-tracking/docs/prepare) for more information.

CSV file(s) with each line in format:

ML_USE,GCS_FILE_PATH

For `ML_USE`, do not use `VALIDATE`.

`GCS_FILE_PATH` is the path to another .csv file that describes training example for a given `ML_USE`, using the following row format:

GCS_FILE_PATH,LABEL,[INSTANCE_ID],TIMESTAMP,BOUNDING_BOX

or

GCS_FILE_PATH,,,,,,,,,,

Here `GCS_FILE_PATH` leads to a video of up to 50GB in size and up to 3h duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI. Providing `INSTANCE_ID`s can help to obtain a better model. When a specific labeled entity leaves the video frame, and shows up afterwards it is not required, albeit preferable, that the same `INSTANCE_ID` is given to it.

`TIMESTAMP` must be within the length of the video, the `BOUNDING_BOX` is assumed to be drawn on the closest video's frame to the `TIMESTAMP`. Any mentioned by the `TIMESTAMP` frame is expected to be exhaustively labeled and no more than 500 `BOUNDING_BOX`-es per frame are allowed. If a whole video is unknown, then it should be mentioned just once with ",,,,,,,,,," in place of `LABEL, [INSTANCE_ID],TIMESTAMP,BOUNDING_BOX`.

Sample top level CSV file:

TRAIN,gs://folder/train_videos.csv TEST,gs://folder/test_videos.csv UNASSIGNED,gs://folder/other_videos.csv

Seven sample rows of a CSV file for a particular ML_USE:

gs://folder/video1.avi,car,1,12.10,0.8,0.8,0.9,0.8,0.9,0.9,0.8,0.9 gs://folder/video1.avi,car,1,12.90,0.4,0.8,0.5,0.8,0.5,0.9,0.4,0.9 gs://folder/video1.avi,car,2,12.10,.4,.2,.5,.2,.5,.3,.4,.3 gs://folder/video1.avi,car,2,12.90,.8,.2,,,.9,.3,, gs://folder/video1.avi,bike,,12.50,.45,.45,,,.55,.55,, gs://folder/video2.avi,car,1,0,.1,.9,,,.9,.1,, gs://folder/video2.avi,,,,,,,,,,,

#### AutoML Natural Language

##### Entity Extraction

See [Preparing your training data](https://docs.cloud.google.com/natural-language/automl/entity-analysis/docs/prepare) for more information.

One or more CSV file(s) with each line in the following format:

ML_USE,GCS_FILE_PATH

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:
  * `TRAIN` \- Rows in this file are used to train the model.
  * `TEST` \- Rows in this file are used to test the model during training.
  * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing..

  * `GCS_FILE_PATH` \- a Identifies JSON Lines (.JSONL) file stored in Google Cloud Storage that contains in-line text in-line as documents for model training.

After the training data set has been determined from the `TRAIN` and `UNASSIGNED` CSV files, the training data is divided into train and validation data sets. 70% for training and 30% for validation.

For example:

TRAIN,gs://folder/file1.jsonl VALIDATE,gs://folder/file2.jsonl TEST,gs://folder/file3.jsonl

**In-line JSONL files**

In-line .JSONL files contain, per line, a JSON document that wraps a `text_snippet` field followed by one or more `annotations` fields, which have `display_name` and `text_extraction` fields to describe the entity from the text snippet. Multiple JSON documents can be separated using line breaks (\n).

The supplied text must be annotated exhaustively. For example, if you include the text "horse", but do not label it as "animal", then "horse" is assumed to not be an "animal".

Any given text snippet content must have 30,000 characters or less, and also be UTF-8 NFC encoded. ASCII is accepted as it is UTF-8 NFC encoded.

For example:

{ "text_snippet": { "content": "dog car cat" }, "annotations": [ { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 0, "end_offset": 2} } }, { "display_name": "vehicle", "text_extraction": { "text_segment": {"start_offset": 4, "end_offset": 6} } }, { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 8, "end_offset": 10} } } ] }\n { "text_snippet": { "content": "This dog is good." }, "annotations": [ { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 5, "end_offset": 7} } } ] }

**JSONL files that reference documents**

.JSONL files contain, per line, a JSON document that wraps a `input_config` that contains the path to a source document. Multiple JSON documents can be separated using line breaks (\n).

Supported document extensions: .PDF, .TIF, .TIFF

For example:

{ "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document1.pdf" ] } } } }\n { "document": { "input_config": { "gcs_source": { "input_uris": [ "gs://folder/document2.tif" ] } } } }

**In-line JSONL files with document layout information**

**Note:** You can only annotate documents using the UI. The format described below applies to annotated documents exported using the UI or `exportData`.

In-line .JSONL files for documents contain, per line, a JSON document that wraps a `document` field that provides the textual content of the document and the layout information.

For example:

{ "document": { "document_text": { "content": "dog car cat" } "layout": [ { "text_segment": { "start_offset": 0, "end_offset": 11, }, "page_number": 1, "bounding_poly": { "normalized_vertices": [ {"x": 0.1, "y": 0.1}, {"x": 0.1, "y": 0.3}, {"x": 0.3, "y": 0.3}, {"x": 0.3, "y": 0.1}, ], }, "text_segment_type": TOKEN, } ], "document_dimensions": { "width": 8.27, "height": 11.69, "unit": INCH, } "page_count": 3, }, "annotations": [ { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 0, "end_offset": 3} } }, { "display_name": "vehicle", "text_extraction": { "text_segment": {"start_offset": 4, "end_offset": 7} } }, { "display_name": "animal", "text_extraction": { "text_segment": {"start_offset": 8, "end_offset": 11} } }, ],




##### Classification

See [Preparing your training data](https://cloud.google.com/natural-language/automl/docs/prepare) for more information.

One or more CSV file(s) with each line in the following format:

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

TRAIN,"They have bad food and very rude",RudeService,BadFood gs://folder/content.txt,SlowService TEST,gs://folder/document.pdf VALIDATE,gs://folder/text_files.zip,BadFood




##### Sentiment Analysis

See [Preparing your training data](https://cloud.google.com/natural-language/automl/docs/prepare) for more information.

CSV file(s) with each line in format:

ML_USE,(TEXT_SNIPPET | GCS_FILE_PATH),SENTIMENT

  * `ML_USE` \- Identifies the data set that the current row (file) applies to. This value can be one of the following:
  * `TRAIN` \- Rows in this file are used to train the model.
  * `TEST` \- Rows in this file are used to test the model during training.
  * `UNASSIGNED` \- Rows in this file are not categorized. They are Automatically divided into train and test data. 80% for training and 20% for testing.

  * `TEXT_SNIPPET` and `GCS_FILE_PATH` are distinguished by a pattern. If the column content is a valid Google Cloud Storage file path, that is, prefixed by "gs://", it is treated as a `GCS_FILE_PATH`. Otherwise, if the content is enclosed in double quotes (""), it is treated as a `TEXT_SNIPPET`. For `GCS_FILE_PATH`, the path must lead to a file with supported extension and UTF-8 encoding, for example, "gs://folder/content.txt" AutoML imports the file content as a text snippet. For `TEXT_SNIPPET`, AutoML imports the column content excluding quotes. In both cases, size of the content must be 128kB or less in size. For zip files, the size of each file inside the zip must be 128kB or less in size.

The `ML_USE` and `SENTIMENT` columns are optional. Supported file extensions: .TXT, .PDF, .TIF, .TIFF, .ZIP

  * `SENTIMENT` \- An integer between 0 and Dataset.text_sentiment_dataset_metadata.sentiment_max (inclusive). Describes the ordinal of the sentiment - higher value means a more positive sentiment. All the values are completely relative, i.e. neither 0 needs to mean a negative or neutral sentiment nor sentiment_max needs to mean a positive one - it is just required that 0 is the least positive sentiment in the data, and sentiment_max is the most positive one. The SENTIMENT shouldn't be confused with "score" or "magnitude" from the previous Natural Language Sentiment Analysis API. All SENTIMENT values between 0 and sentiment_max must be represented in the imported data. On prediction the same 0 to sentiment_max range will be used. The difference between neighboring sentiment values needs not to be uniform, e.g. 1 and 2 may be similar whereas the difference between 2 and 3 may be large.

Sample rows:

TRAIN,"@freewrytin this is way too good for your product",2 gs://folder/content.txt,3 TEST,gs://folder/document.pdf VALIDATE,gs://folder/text_files.zip,2




#### AutoML Tables

See [Preparing your training data](https://cloud.google.com/automl-tables/docs/prepare) for more information.

You can use either gcs_source or bigquery_source. All input is concatenated into a single primary_table_spec_id

**For gcs_source:**

CSV file(s), where the first row of the first file is the header, containing unique column names. If the first row of a subsequent file is the same as the header, then it is also treated as a header. All other rows contain values for the corresponding columns.

Each .CSV file by itself must be 10GB or smaller, and their total size must be 100GB or smaller.

First three sample rows of a CSV file: <pre> "Id","First Name","Last Name","Dob","Addresses" "1","John","Doe","1968-01-22","[{"status":"current","address":"123_First_Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456_Main_Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]" "2","Jane","Doe","1980-10-16","[{"status":"current","address":"789_Any_Avenue","city":"Albany","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321_Main_Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]} </pre> **For bigquery_source:**

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

Protobuf type `google.cloud.automl.v1.InputConfig`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > InputConfig.Builder

## Implements

[InputConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfigOrBuilder)

## Inherited Members

[AbstractMessage.Builder.findInitializationErrors()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_findInitializationErrors__)

[AbstractMessage.Builder.getInitializationErrorString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_getInitializationErrorString__)

[AbstractMessage.Builder.internalMergeFrom(AbstractMessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_internalMergeFrom_com_google_protobuf_AbstractMessageLite_)

[AbstractMessage.Builder.mergeFrom(byte[])](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___)

[AbstractMessage.Builder.mergeFrom(byte[],ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(byte[],int,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___int_int_)

[AbstractMessage.Builder.mergeFrom(byte[],int,int,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___int_int_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(ByteString)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_ByteString_)

[AbstractMessage.Builder.mergeFrom(ByteString,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_ByteString_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(CodedInputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_)

[AbstractMessage.Builder.mergeFrom(CodedInputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(Message)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

[AbstractMessage.Builder.mergeFrom(InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_java_io_InputStream_)

[AbstractMessage.Builder.mergeFrom(InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.newUninitializedMessageException(Message)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_newUninitializedMessageException_com_google_protobuf_Message_)

[AbstractMessage.Builder.toString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_toString__)

[AbstractMessageLite.Builder.<T>addAll(Iterable<T>,Collection<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder__T_addAll_java_lang_Iterable_T__java_util_Collection___super_T__)

[AbstractMessageLite.Builder.<T>addAll(Iterable<T>,List<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder__T_addAll_java_lang_Iterable_T__java_util_List___super_T__)

[AbstractMessageLite.Builder.internalMergeFrom(MessageType)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_internalMergeFrom_MessageType_)

[AbstractMessageLite.Builder.mergeDelimitedFrom(InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeDelimitedFrom_java_io_InputStream_)

[AbstractMessageLite.Builder.mergeDelimitedFrom(InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeDelimitedFrom_java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessageLite.Builder.mergeFrom(MessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeFrom_com_google_protobuf_MessageLite_)

[AbstractMessageLite.Builder.newUninitializedMessageException(MessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_newUninitializedMessageException_com_google_protobuf_MessageLite_)

[GeneratedMessage.Builder.addRepeatedField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessage.Builder.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

[GeneratedMessage.Builder.clearField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.clearOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.clone()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clone__)

[GeneratedMessage.Builder.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getAllFields__)

[GeneratedMessage.Builder.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

[GeneratedMessage.Builder.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.getFieldBuilder(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.getParentForChildren()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getParentForChildren__)

[GeneratedMessage.Builder.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.Builder.getRepeatedFieldBuilder(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.Builder.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

com.google.protobuf.GeneratedMessage.Builder.getUnknownFieldSetBuilder()

[GeneratedMessage.Builder.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getUnknownFields__)

[GeneratedMessage.Builder.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

[GeneratedMessage.Builder.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetMapField_int_)

com.google.protobuf.GeneratedMessage.Builder.internalGetMapFieldReflection(int)

[GeneratedMessage.Builder.internalGetMutableMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetMutableMapField_int_)

com.google.protobuf.GeneratedMessage.Builder.internalGetMutableMapFieldReflection(int)

[GeneratedMessage.Builder.isClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isClean__)

[GeneratedMessage.Builder.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

[GeneratedMessage.Builder.markClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_markClean__)

[GeneratedMessage.Builder.mergeUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

com.google.protobuf.GeneratedMessage.Builder.mergeUnknownLengthDelimitedField(int,com.google.protobuf.ByteString)

com.google.protobuf.GeneratedMessage.Builder.mergeUnknownVarintField(int,int)

[GeneratedMessage.Builder.newBuilderForField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_newBuilderForField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.onBuilt()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_onBuilt__)

[GeneratedMessage.Builder.onChanged()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_onChanged__)

com.google.protobuf.GeneratedMessage.Builder.parseUnknownField(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessage.Builder.setField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessage.Builder.setRepeatedField(Descriptors.FieldDescriptor,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

com.google.protobuf.GeneratedMessage.Builder.setUnknownFieldSetBuilder(com.google.protobuf.UnknownFieldSet.Builder)

[GeneratedMessage.Builder.setUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

com.google.protobuf.GeneratedMessage.Builder.setUnknownFieldsProto3(com.google.protobuf.UnknownFieldSet)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
## Methods 

### build()
    
    
    public InputConfig build()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig)` |   
  
### buildPartial()
    
    
    public InputConfig buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig)` |   
  
### clear()
    
    
    public InputConfig.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearGcsSource()
    
    
    public InputConfig.Builder clearGcsSource()

The Google Cloud Storage location for the input content. For AutoMl.ImportData, `gcs_source` points to a CSV file with a structure described in InputConfig.

`.google.cloud.automl.v1.GcsSource gcs_source = 1;`

**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### clearParams()
    
    
    public InputConfig.Builder clearParams()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### clearSource()
    
    
    public InputConfig.Builder clearSource()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### containsParams(String key)
    
    
    public boolean containsParams(String key)

Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long.

#### AutoML Tables

`schema_inference_version` : (integer) This value must be supplied. The version of the algorithm to use for the initial inference of the column data types of the imported table. Allowed values: "1".

`map<string, string> params = 2;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDefaultInstanceForType()
    
    
    public InputConfig getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getGcsSource()
    
    
    public GcsSource getGcsSource()

The Google Cloud Storage location for the input content. For AutoMl.ImportData, `gcs_source` points to a CSV file with a structure described in InputConfig.

`.google.cloud.automl.v1.GcsSource gcs_source = 1;`

**Returns**  
---  
**Type** | **Description**  
`[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GcsSource)` | The gcsSource.  
  
### getGcsSourceBuilder()
    
    
    public GcsSource.Builder getGcsSourceBuilder()

The Google Cloud Storage location for the input content. For AutoMl.ImportData, `gcs_source` points to a CSV file with a structure described in InputConfig.

`.google.cloud.automl.v1.GcsSource gcs_source = 1;`

**Returns**  
---  
**Type** | **Description**  
`[GcsSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GcsSource.Builder)` |   
  
### getGcsSourceOrBuilder()
    
    
    public GcsSourceOrBuilder getGcsSourceOrBuilder()

The Google Cloud Storage location for the input content. For AutoMl.ImportData, `gcs_source` points to a CSV file with a structure described in InputConfig.

`.google.cloud.automl.v1.GcsSource gcs_source = 1;`

**Returns**  
---  
**Type** | **Description**  
`[GcsSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GcsSourceOrBuilder)` |   
  
### getMutableParams() (deprecated)
    
    
    public Map<String,String> getMutableParams()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getParams() (deprecated)
    
    
    public Map<String,String> getParams()

Use [#getParamsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder#com_google_cloud_automl_v1_InputConfig_Builder_getParamsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getParamsCount()
    
    
    public int getParamsCount()

Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long.

#### AutoML Tables

`schema_inference_version` : (integer) This value must be supplied. The version of the algorithm to use for the initial inference of the column data types of the imported table. Allowed values: "1".

`map<string, string> params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getParamsMap()
    
    
    public Map<String,String> getParamsMap()

Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long.

#### AutoML Tables

`schema_inference_version` : (integer) This value must be supplied. The version of the algorithm to use for the initial inference of the column data types of the imported table. Allowed values: "1".

`map<string, string> params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getParamsOrDefault(String key, String defaultValue)
    
    
    public String getParamsOrDefault(String key, String defaultValue)

Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long.

#### AutoML Tables

`schema_inference_version` : (integer) This value must be supplied. The version of the algorithm to use for the initial inference of the column data types of the imported table. Allowed values: "1".

`map<string, string> params = 2;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getParamsOrThrow(String key)
    
    
    public String getParamsOrThrow(String key)

Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long.

#### AutoML Tables

`schema_inference_version` : (integer) This value must be supplied. The version of the algorithm to use for the initial inference of the column data types of the imported table. Allowed values: "1".

`map<string, string> params = 2;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSourceCase()
    
    
    public InputConfig.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[InputConfig.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.SourceCase)` |   
  
### hasGcsSource()
    
    
    public boolean hasGcsSource()

The Google Cloud Storage location for the input content. For AutoMl.ImportData, `gcs_source` points to a CSV file with a structure described in InputConfig.

`.google.cloud.automl.v1.GcsSource gcs_source = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsSource field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

### internalGetMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMapFieldReflection(int)

### internalGetMutableMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMutableMapFieldReflection(int)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeFrom(InputConfig other)
    
    
    public InputConfig.Builder mergeFrom(InputConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public InputConfig.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public InputConfig.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeGcsSource(GcsSource value)
    
    
    public InputConfig.Builder mergeGcsSource(GcsSource value)

The Google Cloud Storage location for the input content. For AutoMl.ImportData, `gcs_source` points to a CSV file with a structure described in InputConfig.

`.google.cloud.automl.v1.GcsSource gcs_source = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GcsSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### putAllParams(Map<String,String> values)
    
    
    public InputConfig.Builder putAllParams(Map<String,String> values)

Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long.

#### AutoML Tables

`schema_inference_version` : (integer) This value must be supplied. The version of the algorithm to use for the initial inference of the column data types of the imported table. Allowed values: "1".

`map<string, string> params = 2;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### putParams(String key, String value)
    
    
    public InputConfig.Builder putParams(String key, String value)

Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long.

#### AutoML Tables

`schema_inference_version` : (integer) This value must be supplied. The version of the algorithm to use for the initial inference of the column data types of the imported table. Allowed values: "1".

`map<string, string> params = 2;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### removeParams(String key)
    
    
    public InputConfig.Builder removeParams(String key)

Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long.

#### AutoML Tables

`schema_inference_version` : (integer) This value must be supplied. The version of the algorithm to use for the initial inference of the column data types of the imported table. Allowed values: "1".

`map<string, string> params = 2;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### setGcsSource(GcsSource value)
    
    
    public InputConfig.Builder setGcsSource(GcsSource value)

The Google Cloud Storage location for the input content. For AutoMl.ImportData, `gcs_source` points to a CSV file with a structure described in InputConfig.

`.google.cloud.automl.v1.GcsSource gcs_source = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GcsSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
### setGcsSource(GcsSource.Builder builderForValue)
    
    
    public InputConfig.Builder setGcsSource(GcsSource.Builder builderForValue)

The Google Cloud Storage location for the input content. For AutoMl.ImportData, `gcs_source` points to a CSV file with a structure described in InputConfig.

`.google.cloud.automl.v1.GcsSource gcs_source = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[GcsSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GcsSource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
