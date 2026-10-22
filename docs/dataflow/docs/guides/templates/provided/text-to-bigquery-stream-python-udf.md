---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/text-to-bigquery-stream-python-udf/
title: Cloud Storage Text to BigQuery (Stream) with Python UDF template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:30.359368+00:00
---

# Cloud Storage Text to BigQuery (Stream) with Python UDF template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/text-to-bigquery-stream-python-udf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage Text to BigQuery (Stream) with Python UDF template Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage Text to BigQuery pipeline is a streaming pipeline that streams text files stored in Cloud Storage, transforms them using a Python user-defined function (UDF) that you provide, and appends the result to BigQuery. 

The pipeline runs indefinitely and needs to be terminated manually via a [cancel](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel) and not a [drain](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain), due to its use of the `Watch` transform, which is a splittable `DoFn` that does not support draining. 

This template is impacted by [Beam Issue 18459](https://github.com/apache/beam/issues/18459) and will likely have memory issues on large buckets (observed on buckets with 5 million files). Here are some known workarounds: 

  1. Split the files into two or more buckets and use this template.
  2. Create a custom template, possibly forked from this one, that streams file names through Pub/Sub and processes those files.



## Pipeline requirements

  * Create a JSON file that describes the schema of your output table in BigQuery. 

Ensure that there is a top-level JSON array titled `fields` and that its contents follow the pattern `{"name": "COLUMN_NAME", "type": "DATA_TYPE"}`. For example: 
        
        {
          "fields": [
            {
              "name": "name",
              "type": "STRING"
            },
            {
              "name": "age",
              "type": "INTEGER"
            }
          ]
        }

  * Create a Python (`.py`) file with your UDF function that supplies the logic to transform the lines of text. Your function must return a JSON string. 

The following example splits each line of a CSV file, creates a JSON object with the values, and returns a JSON string:
        
        import json
        def process(value):
          data = value.split(',')
          obj = { 'name': data[0], 'age': int(data[1]) }
          return json.dumps(obj)




## Template parameters

### Required parameters

  * **inputFilePattern** : The gs:// path to the text in Cloud Storage you'd like to process. For example, `gs://your-bucket/your-file.txt`.
  * **JSONPath** : The gs:// path to the JSON file that defines your BigQuery schema, stored in Cloud Storage. For example, `gs://your-bucket/your-schema.json`.
  * **outputTable** : The location of the BigQuery table to use to store the processed data. If you reuse an existing table, it is overwritten. For example, `<PROJECT_ID>:<DATASET_NAME>.<TABLE_NAME>`.
  * **bigQueryLoadingTemporaryDirectory** : Temporary directory for BigQuery loading process. For example, `gs://your-bucket/your-files/temp-dir`.



### Optional parameters

  * **outputDeadletterTable** : Table for messages that failed to reach the output table. If a table doesn't exist, it is created during pipeline execution. If not specified, `<outputTableSpec>_error_records` is used. For example, `<PROJECT_ID>:<DATASET_NAME>.<TABLE_NAME>`.
  * **useStorageWriteApiAtLeastOnce** : This parameter takes effect only if `Use BigQuery Storage Write API` is enabled. If enabled the at-least-once semantics will be used for Storage Write API, otherwise exactly-once semantics will be used. Defaults to: false.
  * **useStorageWriteApi** : If true, the pipeline uses the BigQuery Storage Write API (<https://cloud.google.com/bigquery/docs/write-api>). The default value is `false`. For more information, see Using the Storage Write API (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api>).
  * **numStorageWriteApiStreams** : When using the Storage Write API, specifies the number of write streams. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter. Defaults to: 0.
  * **storageWriteApiTriggeringFrequencySec** : When using the Storage Write API, specifies the triggering frequency, in seconds. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter.
  * **pythonExternalTextTransformGcsPath** : The Cloud Storage path pattern for the Python code containing your user-defined functions. For example, `gs://your-bucket/your-function.py`.
  * **pythonExternalTextTransformFunctionName** : The name of the function to call from your Python file. Use only letters, digits, and underscores. For example, `'transform' or 'transform_udf1'`.



## User-defined function

This template requires a UDF that parses the input files, as described in Pipeline requirements. The template calls the UDF for every line of text in each input file. For more information about creating UDFs, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Function specification

The UDF has the following specification:

  * **Input** : a single line of text from an input file.
  * **Output** : a JSON string that matches the schema of the BigQuery destination table.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Cloud Storage Text to BigQuery (Stream) with Python UDF** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location gs://dataflow-templates/VERSION/flex/Stream_GCS_Text_to_BigQuery_Xlang \
        --region REGION_NAME \
        --staging-location STAGING_LOCATION \
        --parameters \
    pythonExternalTextTransformGcsPath=PATH_TO_PYTHON_UDF_FILE,\
    pythonExternalTextTransformFunctionName=PYTHON_FUNCTION,\
    JSONPath=PATH_TO_BIGQUERY_SCHEMA_JSON,\
    inputFilePattern=PATH_TO_TEXT_DATA,\
    outputTable=BIGQUERY_TABLE,\
    outputDeadletterTable=BIGQUERY_UNPROCESSED_TABLE,\
    bigQueryLoadingTemporaryDirectory=PATH_TO_TEMP_DIR_ON_GCS

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `PYTHON_FUNCTION`: The name of the Python user-defined function (UDF) that you want to use. 
  * `PATH_TO_BIGQUERY_SCHEMA_JSON`: the Cloud Storage path to the JSON file containing the schema definition
  * `PATH_TO_PYTHON_UDF_FILE`: The Cloud Storage URI of the Python code file that defines the user-defined function (UDF) you want to use. For example, `gs://my-bucket/my-udfs/my_file.py`. 
  * `PATH_TO_TEXT_DATA`: the Cloud Storage path to your text dataset
  * `BIGQUERY_TABLE`: your BigQuery table name
  * `BIGQUERY_UNPROCESSED_TABLE`: the name of your BigQuery table for unprocessed messages
  * `PATH_TO_TEMP_DIR_ON_GCS`: the Cloud Storage path to the temp directory



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
           "pythonExternalTextTransformFunctionName": "PYTHON_FUNCTION",
           "JSONPath": "PATH_TO_BIGQUERY_SCHEMA_JSON",
           "pythonExternalTextTransformGcsPath": "PATH_TO_PYTHON_UDF_FILE",
           "inputFilePattern":"PATH_TO_TEXT_DATA",
           "outputTable":"BIGQUERY_TABLE",
           "outputDeadletterTable":"BIGQUERY_UNPROCESSED_TABLE",
           "bigQueryLoadingTemporaryDirectory": "PATH_TO_TEMP_DIR_ON_GCS"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Stream_GCS_Text_to_BigQuery_Xlang",
       }
    }

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `PYTHON_FUNCTION`: The name of the Python user-defined function (UDF) that you want to use. 
  * `PATH_TO_BIGQUERY_SCHEMA_JSON`: the Cloud Storage path to the JSON file containing the schema definition
  * `PATH_TO_PYTHON_UDF_FILE`: The Cloud Storage URI of the Python code file that defines the user-defined function (UDF) you want to use. For example, `gs://my-bucket/my-udfs/my_file.py`. 
  * `PATH_TO_TEXT_DATA`: the Cloud Storage path to your text dataset
  * `BIGQUERY_TABLE`: your BigQuery table name
  * `BIGQUERY_UNPROCESSED_TABLE`: the name of your BigQuery table for unprocessed messages
  * `PATH_TO_TEMP_DIR_ON_GCS`: the Cloud Storage path to the temp directory



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2018 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License"); you may not
     * use this file except in compliance with the License. You may obtain a copy of
     * the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
     * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
     * License for the specific language governing permissions and limitations under
     * the License.
     */
    package com.google.cloud.teleport.v2.templates;
    
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.services.bigquery.model.TableRow;
    import com.google.cloud.teleport.metadata.MultiTemplate;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.BigQueryStorageApiStreamingOptions;
    import com.google.cloud.teleport.v2.templates.TextToBigQueryStreaming.TextToBigQueryStreamingOptions;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters.FailsafeJsonToTableRow;
    import com.google.cloud.teleport.v2.transforms.ErrorConverters.WriteStringMessageErrors;
    import com.google.cloud.teleport.v2.transforms.JavascriptTextTransformer.FailsafeJavascriptUdf;
    import com.google.cloud.teleport.v2.transforms.PythonExternalTextTransformer;
    import com.google.cloud.teleport.v2.transforms.PythonExternalTextTransformer.RowToStringFailsafeElementFn;
    import com.google.cloud.teleport.v2.utils.BigQueryIOUtils;
    import com.google.cloud.teleport.v2.utils.GCSUtils;
    import com.google.cloud.teleport.v2.utils.ResourceUtils;
    import com.google.cloud.teleport.v2.[values](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonToken.html#com_google_api_client_json_JsonToken_values__).FailsafeElement;
    import com.google.common.base.Strings;
    import com.google.common.collect.ImmutableList;
    import java.io.IOException;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.CoderRegistry;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.extensions.gcp.util.Transport;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.WriteDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryInsertError;
    import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
    import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider.StaticValueProvider;
    import org.apache.beam.sdk.transforms.Flatten;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.Watch.Growth;
    import org.apache.beam.sdk.[values](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonToken.html#com_google_api_client_json_JsonToken_values__).PCollection;
    import org.apache.beam.sdk.[values](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonToken.html#com_google_api_client_json_JsonToken_values__).PCollectionList;
    import org.apache.beam.sdk.[values](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonToken.html#com_google_api_client_json_JsonToken_values__).PCollectionTuple;
    import org.apache.beam.sdk.[values](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonToken.html#com_google_api_client_json_JsonToken_values__).TupleTag;
    import org.apache.beam.sdk.[values](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonToken.html#com_google_api_client_json_JsonToken_values__).TupleTagList;
    import org.apache.commons.lang3.StringUtils;
    import org.joda.time.Duration;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link TextToBigQueryStreaming} is a streaming version of {@link TextIOToBigQuery} pipeline
     * that reads text files, applies a JavaScript UDF and writes the output to BigQuery. The pipeline
     * continuously polls for new files, reads them row-by-row and processes each record into BigQuery.
     * The polling interval is set at 10 seconds.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-googlecloud/README_Stream_GCS_Text_to_BigQuery_Flex.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @MultiTemplate({
      @Template(
          name = "Stream_GCS_Text_to_BigQuery_Flex",
          category = TemplateCategory.STREAMING,
          displayName = "Cloud Storage Text to BigQuery (Stream)",
          description = {
            "The Text Files on Cloud Storage to BigQuery pipeline is a streaming pipeline that allows you to stream text files stored in Cloud Storage, transform them using a JavaScript User Defined Function (UDF) that you provide, and append the result to BigQuery.\n",
            "The pipeline runs indefinitely and needs to be terminated manually via a\n"
                + "    <a href=\"https://cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel\">cancel</a> and not a\n"
                + "    <a href=\"https://cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain\">drain</a>, due to its use of the\n"
                + "    <code>Watch</code> transform, which is a splittable <code>DoFn</code> that does not support\n"
                + "    draining."
          },
          skipOptions = {
            "pythonExternalTextTransfromGcsPath",
            "pythonExternalTextTransformFunctionName"
          },
          optionsClass = TextToBigQueryStreamingOptions.class,
          flexContainerName = "googlecloud-to-googlecloud",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/text-to-bigquery-stream",
          contactInformation = "https://cloud.google.com/support",
          requirements = {
            "Create a JSON file that describes the schema of your output table in BigQuery.\n"
                + "    <p>\n"
                + "      Ensure that there is a top-level JSON array titled <code>fields</code> and that its\n"
                + "      contents follow the pattern <code>{\"name\": \"COLUMN_NAME\", \"type\": \"DATA_TYPE\"}</code>.\n"
                + "      For example:\n"
                + "    </p>\n"
                + "<pre class=\"prettyprint lang-json\">\n"
                + "{\n"
                + "  \"fields\": [\n"
                + "    {\n"
                + "      \"name\": \"location\",\n"
                + "      \"type\": \"STRING\"\n"
                + "    },\n"
                + "    {\n"
                + "      \"name\": \"name\",\n"
                + "      \"type\": \"STRING\"\n"
                + "    },\n"
                + "    {\n"
                + "      \"name\": \"age\",\n"
                + "      \"type\": \"STRING\"\n"
                + "    },\n"
                + "    {\n"
                + "      \"name\": \"color\",\n"
                + "      \"type\": \"STRING\",\n"
                + "      \"mode\": \"REQUIRED\"\n"
                + "    },\n"
                + "    {\n"
                + "      \"name\": \"coffee\",\n"
                + "      \"type\": \"STRING\",\n"
                + "      \"mode\": \"REQUIRED\"\n"
                + "    }\n"
                + "  ]\n"
                + "}\n"
                + "</pre>",
            "Create a JavaScript (<code>.js</code>) file with your UDF function that supplies the logic\n"
                + "    to transform the lines of text. Note that your function must return a JSON string.\n"
                + "    <p>For example, this function splits each line of a CSV file and returns a JSON string after\n"
                + "      transforming the values.</p>\n"
                + "<pre class=\"prettyprint\" suppresswarning>\n"
                + "function transform(line) {\n"
                + "var values = line.split(',');\n"
                + "\n"
                + "var obj = new Object();\n"
                + "obj.location = values[0];\n"
                + "obj.name = values[1];\n"
                + "obj.age = values[2];\n"
                + "obj.color = values[3];\n"
                + "obj.coffee = values[4];\n"
                + "var jsonString = JSON.stringify(obj);\n"
                + "\n"
                + "return jsonString;\n"
                + "}\n"
                + "</pre>"
          },
          streaming = true,
          supportsAtLeastOnce = true),
      @Template(
          name = "Stream_GCS_Text_to_BigQuery_Xlang",
          category = TemplateCategory.STREAMING,
          displayName = "Cloud Storage Text to BigQuery (Stream) with Python UDF",
          type = Template.TemplateType.XLANG,
          description = {
            "The Text Files on Cloud Storage to BigQuery pipeline is a streaming pipeline that allows you to stream text files stored in Cloud Storage, transform them using a Python User Defined Function (UDF) that you provide, and append the result to BigQuery.\n",
            "The pipeline runs indefinitely and needs to be terminated manually via a\n"
                + "    <a href=\"https://cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel\">cancel</a> and not a\n"
                + "    <a href=\"https://cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain\">drain</a>, due to its use of the\n"
                + "    <code>Watch</code> transform, which is a splittable <code>DoFn</code> that does not support\n"
                + "    draining."
          },
          skipOptions = {
            "javascriptTextTransformGcsPath",
            "javascriptTextTransformFunctionName",
            "javascriptTextTransformReloadIntervalMinutes"
          },
          optionsClass = TextToBigQueryStreamingOptions.class,
          flexContainerName = "googlecloud-to-googlecloud-xlang",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/text-to-bigquery-stream",
          contactInformation = "https://cloud.google.com/support",
          requirements = {
            "Create a JSON file that describes the schema of your output table in BigQuery.\n"
                + "    <p>\n"
                + "      Ensure that there is a top-level JSON array titled <code>fields</code> and that its\n"
                + "      contents follow the pattern <code>{\"name\": \"COLUMN_NAME\", \"type\": \"DATA_TYPE\"}</code>.\n"
                + "      For example:\n"
                + "    </p>\n"
                + "<pre class=\"prettyprint lang-json\">\n"
                + "{\n"
                + "  \"fields\": [\n"
                + "    {\n"
                + "      \"name\": \"location\",\n"
                + "      \"type\": \"STRING\"\n"
                + "    },\n"
                + "    {\n"
                + "      \"name\": \"name\",\n"
                + "      \"type\": \"STRING\"\n"
                + "    },\n"
                + "    {\n"
                + "      \"name\": \"age\",\n"
                + "      \"type\": \"STRING\"\n"
                + "    },\n"
                + "    {\n"
                + "      \"name\": \"color\",\n"
                + "      \"type\": \"STRING\",\n"
                + "      \"mode\": \"REQUIRED\"\n"
                + "    },\n"
                + "    {\n"
                + "      \"name\": \"coffee\",\n"
                + "      \"type\": \"STRING\",\n"
                + "      \"mode\": \"REQUIRED\"\n"
                + "    }\n"
                + "  ]\n"
                + "}\n"
                + "</pre>",
            "Create a Python (<code>.js</code>) file with your UDF function that supplies the logic\n"
                + "    to transform the lines of text. Note that your function must return a JSON string.\n"
                + "    <p>For example, this function splits each line of a CSV file and returns a JSON string after\n"
                + "      transforming the values.</p>\n"
                + "<pre class=\"prettyprint\" suppresswarning>\n"
                + "import json\n"
                + "def transform(line): \n"
                + "  values = line.split(',')\n"
                + "\n"
                + "  obj = {\n"
                + "     'location' : values[0],\n"
                + "     'name' : values[1],\n"
                + "     'age' : values[2],\n"
                + "     'color' : values[3],\n"
                + "     'coffee' : values[4]\n"
                + "  }\n"
                + "  jsonString = JSON.dumps(obj);\n"
                + "\n"
                + "  return jsonString;\n"
                + "\n"
                + "</pre>"
          },
          streaming = true,
          supportsAtLeastOnce = true)
    })
    public class TextToBigQueryStreaming {
    
      private static final Logger LOG = LoggerFactory.getLogger(TextToBigQueryStreaming.class);
    
      /** The tag for the main output for the UDF. */
      private static final TupleTag<FailsafeElement<String, String>> UDF_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /** The tag for the dead-letter output of the udf. */
      private static final TupleTag<FailsafeElement<String, String>> UDF_DEADLETTER_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /** The tag for the main output of the json transformation. */
      private static final TupleTag<TableRow> TRANSFORM_OUT = new TupleTag<TableRow>() {};
    
      /** The tag for the dead-letter output of the json to table row transform. */
      private static final TupleTag<FailsafeElement<String, String>> TRANSFORM_DEADLETTER_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /** The default suffix for error tables if dead letter table is not specified. */
      private static final String DEFAULT_DEADLETTER_TABLE_SUFFIX = "_error_records";
    
      /** Default interval for polling files in GCS. */
      private static final Duration DEFAULT_POLL_INTERVAL = Duration.standardSeconds(10);
    
      /** Coder for FailsafeElement. */
      private static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      private static final [JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html) JSON_FACTORY = Transport.getJsonFactory();
    
      /**
       * Main entry point for executing the pipeline. This will run the pipeline asynchronously. If
       * blocking execution is required, use the {@link
       * TextToBigQueryStreaming#run(TextToBigQueryStreamingOptions)} method to start the pipeline and
       * invoke {@code result.waitUntilFinish()} on the {@link PipelineResult}
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        // Parse the user options passed from the command-line
        TextToBigQueryStreamingOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(TextToBigQueryStreamingOptions.class);
        BigQueryIOUtils.validateBQStorageApiOptionsStreaming(options);
    
        run(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static PipelineResult run(TextToBigQueryStreamingOptions options) {
    
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        // Register the coder for pipeline
        FailsafeElementCoder<String, String> coder =
            FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
        CoderRegistry coderRegistry = pipeline.getCoderRegistry();
        coderRegistry.registerCoderForType(coder.getEncodedTypeDescriptor(), coder);
    
        // Determine if we are using Python UDFs or JS UDFs based on the provided options.
        boolean useJavascriptUdf = !Strings.isNullOrEmpty(options.getJavascriptTextTransformGcsPath());
        boolean usePythonUdf = !Strings.isNullOrEmpty(options.getPythonExternalTextTransformGcsPath());
        if (useJavascriptUdf && usePythonUdf) {
          throw new IllegalArgumentException(
              "Either javascript or Python gcs path must be provided, but not both.");
        }
    
        /*
         * Steps:
         *  1) Read from the text source continuously.
         *  2) Convert to FailsafeElement.
         *  3) Apply Javascript udf transformation.
         *    - Tag records that were successfully transformed and those
         *      that failed transformation.
         *  4) Convert records to TableRow.
         *    - Tag records that were successfully converted and those
         *      that failed conversion.
         *  5) Insert successfully converted records into BigQuery.
         *    - Errors encountered while streaming will be sent to deadletter table.
         *  6) Insert records that failed into deadletter table.
         */
    
        PCollection<String> sourceRead =
            pipeline.apply(
                TextIO.read()
                    .from(options.getInputFilePattern())
                    .watchForNewFiles(DEFAULT_POLL_INTERVAL, Growth.never()));
        PCollectionTuple transformedOutput;
        if (usePythonUdf) {
          transformedOutput =
              sourceRead
                  .apply(
                      "MapToRecord",
                      PythonExternalTextTransformer.FailsafeRowPythonExternalUdf
                          .stringMappingFunction())
                  .setRowSchema(PythonExternalTextTransformer.FailsafeRowPythonExternalUdf.ROW_SCHEMA)
                  .apply(
                      "InvokeUDF",
                      PythonExternalTextTransformer.FailsafePythonExternalUdf.newBuilder()
                          .setFileSystemPath(options.getPythonExternalTextTransformGcsPath())
                          .setFunctionName(options.getPythonExternalTextTransformFunctionName())
                          .build())
                  .apply(
                      ParDo.of(new RowToStringFailsafeElementFn(UDF_OUT, UDF_DEADLETTER_OUT))
                          .withOutputTags(UDF_OUT, TupleTagList.of(UDF_DEADLETTER_OUT)));
    
        } else {
          transformedOutput =
              pipeline
    
                  // 1) Read from the text source continuously.
                  .apply(
                      "ReadFromSource",
                      TextIO.read()
                          .from(options.getInputFilePattern())
                          .watchForNewFiles(DEFAULT_POLL_INTERVAL, Growth.never()))
    
                  // 2) Convert to FailsafeElement.
                  .apply(
                      "ConvertToFailsafeElement",
                      MapElements.into(FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor())
                          .via(input -> FailsafeElement.of(input, input)))
    
                  // 3) Apply Javascript udf transformation.
                  .apply(
                      "ApplyUDFTransformation",
                      FailsafeJavascriptUdf.<String>newBuilder()
                          .setFileSystemPath(options.getJavascriptTextTransformGcsPath())
                          .setFunctionName(options.getJavascriptTextTransformFunctionName())
                          .setReloadIntervalMinutes(
                              options.getJavascriptTextTransformReloadIntervalMinutes())
                          .setSuccessTag(UDF_OUT)
                          .setFailureTag(UDF_DEADLETTER_OUT)
                          .build());
        }
    
        PCollectionTuple convertedTableRows =
            transformedOutput
    
                // 4) Convert records to TableRow.
                .get(UDF_OUT)
                .apply(
                    "ConvertJSONToTableRow",
                    FailsafeJsonToTableRow.<String>newBuilder()
                        .setSuccessTag(TRANSFORM_OUT)
                        .setFailureTag(TRANSFORM_DEADLETTER_OUT)
                        .build());
    
        WriteResult writeResult =
            convertedTableRows
    
                // 5) Insert successfully converted records into BigQuery.
                .get(TRANSFORM_OUT)
                .apply(
                    "InsertIntoBigQuery",
                    BigQueryIO.writeTableRows()
                        .withJsonSchema(GCSUtils.getGcsFileAsString(options.getJSONPath()))
                        .to(options.getOutputTable())
                        .withExtendedErrorInfo()
                        .withoutValidation()
                        .withCreateDisposition(CreateDisposition.CREATE_IF_NEEDED)
                        .withWriteDisposition(WriteDisposition.WRITE_APPEND)
                        .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors())
                        .withCustomGcsTempLocation(
                            StaticValueProvider.of(options.getBigQueryLoadingTemporaryDirectory())));
    
        // Elements that failed inserts into BigQuery are extracted and converted to FailsafeElement
        PCollection<FailsafeElement<String, String>> failedInserts =
            BigQueryIOUtils.writeResultToBigQueryInsertErrors(writeResult, options)
                .apply(
                    "WrapInsertionErrors",
                    MapElements.into(FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor())
                        .via(TextToBigQueryStreaming::wrapBigQueryInsertError));
    
        // 6) Insert records that failed transformation or conversion into deadletter table
        PCollectionList.of(
                ImmutableList.of(
                    transformedOutput.get(UDF_DEADLETTER_OUT),
                    convertedTableRows.get(TRANSFORM_DEADLETTER_OUT),
                    failedInserts))
            .apply("Flatten", Flatten.pCollections())
            .apply(
                "WriteFailedRecords",
                WriteStringMessageErrors.newBuilder()
                    .setErrorRecordsTable(
                        StringUtils.isNotEmpty(options.getOutputDeadletterTable())
                            ? options.getOutputDeadletterTable()
                            : options.getOutputTable() + DEFAULT_DEADLETTER_TABLE_SUFFIX)
                    .setErrorRecordsTableSchema(ResourceUtils.getDeadletterTableSchemaJson())
                    .build());
    
        return pipeline.run();
      }
    
      /**
       * Method to wrap a {@link BigQueryInsertError} into a {@link FailsafeElement}.
       *
       * @param insertError BigQueryInsert error.
       * @return FailsafeElement object.
       * @throws IOException
       */
      static FailsafeElement<String, String> wrapBigQueryInsertError(BigQueryInsertError insertError) {
    
        FailsafeElement<String, String> failsafeElement;
        try {
    
          String rowPayload = JSON_FACTORY.[toString](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html#com_google_api_client_json_JsonFactory_toString_java_lang_Object_)(insertError.getRow());
          String errorMessage = JSON_FACTORY.[toString](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html#com_google_api_client_json_JsonFactory_toString_java_lang_Object_)(insertError.getError());
    
          failsafeElement = FailsafeElement.of(rowPayload, rowPayload);
          failsafeElement.setErrorMessage(errorMessage);
    
        } catch (IOException e) {
          throw new RuntimeException(e);
        }
    
        return failsafeElement;
      }
    
      /**
       * The {@link TextToBigQueryStreamingOptions} class provides the custom execution options passed
       * by the executor at the command-line.
       */
      public interface TextToBigQueryStreamingOptions
          extends TextIOToBigQuery.Options, BigQueryStorageApiStreamingOptions {
        @TemplateParameter.BigQueryTable(
            order = 1,
            optional = true,
            description = "The dead-letter table name to output failed messages to BigQuery",
            helpText =
                "Table for messages that failed to reach the output table. If a table doesn't exist, it is created during "
                    + "pipeline execution. If not specified, `<outputTableSpec>_error_records` is used.",
            example = "<PROJECT_ID>:<DATASET_NAME>.<TABLE_NAME>")
        String getOutputDeadletterTable();
    
        void setOutputDeadletterTable(String value);
    
        // Hide the UseStorageWriteApiAtLeastOnce in the UI, because it will automatically be turned
        // on when pipeline is running on ALO mode and using the Storage Write API
        @TemplateParameter.Boolean(
            order = 2,
            optional = true,
            parentName = "useStorageWriteApi",
            parentTriggerValues = {"true"},
            description = "Use at at-least-once semantics in BigQuery Storage Write API",
            helpText =
                "This parameter takes effect only if `Use BigQuery Storage Write API` is enabled. If"
                    + " enabled the at-least-once semantics will be used for Storage Write API, otherwise"
                    + " exactly-once semantics will be used.",
            hiddenUi = true)
        @Default.Boolean(false)
        @Override
        Boolean getUseStorageWriteApiAtLeastOnce();
    
        void setUseStorageWriteApiAtLeastOnce(Boolean value);
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
