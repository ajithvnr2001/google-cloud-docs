---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-to-cloud-storage/
title: Spanner to Cloud Storage Text template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:34.894779+00:00
---

# Spanner to Cloud Storage Text template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-to-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Spanner to Cloud Storage Text template Stay organized with collections  Save and categorize content based on your preferences. 

The Spanner to Cloud Storage Text template is a batch pipeline that reads in data from a Spanner table, and writes it to Cloud Storage as CSV text files.

## Pipeline requirements

  * The input Spanner table must exist before running the pipeline.



## Template parameters

### Required parameters

  * **spannerTable** : The Spanner table to read the data from.
  * **spannerProjectId** : The ID of the Google Cloud project that contains the Spanner database to read data from.
  * **spannerInstanceId** : The instance ID of the requested table.
  * **spannerDatabaseId** : The database ID of the requested table.
  * **textWritePrefix** : The Cloud Storage path prefix that specifies where the data is written. For example, `gs://mybucket/somefolder/`.



### Optional parameters

  * **csvTempDirectory** : The Cloud Storage path where temporary CSV files are written. For example, `gs://your-bucket/your-path`.
  * **spannerPriority** : The request priority (<https://cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions>) for Spanner calls. Possible values are `HIGH`, `MEDIUM`, `LOW`. The default value is `MEDIUM`.
  * **spannerHost** : The Cloud Spanner endpoint to call in the template. Only used for testing. For example, `https://batch-spanner.googleapis.com`. Defaults to: <https://batch-spanner.googleapis.com>.
  * **spannerSnapshotTime** : The timestamp that corresponds to the version of the Spanner database that you want to read from. The timestamp must be specified in the RFC 3339 (<https://tools.ietf.org/html/rfc3339>) UTC Zulu Time format. The timestamp must be in the past and maximum timestamp staleness (<https://cloud.google.com/spanner/docs/timestamp-bounds#maximum_timestamp_staleness>) applies. For example, `1990-12-31T23:59:60Z`. Defaults to empty.
  * **dataBoostEnabled** : Set to `true` to use the compute resources of Spanner Data Boost to run the job with near-zero impact on Spanner OLTP workflows. When true, requires the `spanner.databases.useDataBoost` Identity and Access Management (IAM) permission. For more information, see Data Boost overview (<https://cloud.google.com/spanner/docs/databoost/databoost-overview>). Defaults to: false.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Cloud Spanner to Text Files on Cloud Storage** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/Spanner_to_GCS_Text \
        --region REGION_NAME \
        --parameters \
    spannerProjectId=SPANNER_PROJECT_ID,\
    spannerDatabaseId=DATABASE_ID,\
    spannerInstanceId=INSTANCE_ID,\
    spannerTable=TABLE_ID,\
    textWritePrefix=gs://BUCKET_NAME/output/

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `SPANNER_PROJECT_ID`: the Google Cloud project ID of the Spanner database from which you want to read data
  * `DATABASE_ID`: the Spanner database ID
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `INSTANCE_ID`: the Spanner instance ID
  * `TABLE_ID`: the Spanner table ID



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Spanner_to_GCS_Text
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "spannerProjectId": "SPANNER_PROJECT_ID",
           "spannerDatabaseId": "DATABASE_ID",
           "spannerInstanceId": "INSTANCE_ID",
           "spannerTable": "TABLE_ID",
           "textWritePrefix": "gs://BUCKET_NAME/output/"
       },
       "environment": { "zone": "us-central1-f" }
    }

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `SPANNER_PROJECT_ID`: the Google Cloud project ID of the Spanner database from which you want to read data
  * `DATABASE_ID`: the Spanner database ID
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `INSTANCE_ID`: the Spanner instance ID
  * `TABLE_ID`: the Spanner table ID



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
    package com.google.cloud.teleport.templates;
    
    import static com.google.cloud.teleport.util.ValueProviderUtils.eitherOrValueProvider;
    
    import com.google.cloud.spanner.Options.RpcPriority;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.metadata.TemplateParameter.TemplateEnumOption;
    import com.google.cloud.teleport.spanner.spannerio.ReadOperation;
    import com.google.cloud.teleport.spanner.spannerio.SpannerConfig;
    import com.google.cloud.teleport.spanner.spannerio.SpannerIO;
    import com.google.cloud.teleport.spanner.spannerio.Transaction;
    import com.google.cloud.teleport.templates.SpannerToText.SpannerToTextOptions;
    import com.google.cloud.teleport.templates.common.SpannerConverters;
    import com.google.cloud.teleport.templates.common.SpannerConverters.CreateTransactionFnWithTimestamp;
    import com.google.cloud.teleport.templates.common.SpannerConverters.SpannerReadOptions;
    import com.google.cloud.teleport.templates.common.TextConverters.FilesystemWriteOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.FileSystems;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.fs.ResourceId;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.Create;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.PTransform;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    import org.apache.beam.sdk.transforms.View;
    import org.apache.beam.sdk.values.PBegin;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionView;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * Dataflow template which copies a Spanner table to a Text sink. It exports a Spanner table using
     * <a href="https://cloud.google.com/spanner/docs/reads#read_data_in_parallel">Batch API</a>, which
     * creates multiple workers in parallel for better performance. The result is written to a CSV file
     * in Google Cloud Storage. The table schema file is saved in json format along with the exported
     * table.
     *
     * <p>Schema file sample: { "id":"INT64", "name":"STRING(MAX)" }
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Spanner_to_GCS_Text.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Spanner_to_GCS_Text",
        category = TemplateCategory.BATCH,
        displayName = "Cloud Spanner to Text Files on Cloud Storage",
        description =
            "The Cloud Spanner to Cloud Storage Text template is a batch pipeline that reads in data from a Cloud Spanner "
                + "table, and writes it to Cloud Storage as CSV text files.",
        optionsClass = SpannerToTextOptions.class,
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-to-cloud-storage",
        contactInformation = "https://cloud.google.com/support",
        requirements = {"The input Spanner table must exist before running the pipeline."})
    public class SpannerToText {
    
      private static final Logger LOG = LoggerFactory.getLogger(SpannerToText.class);
    
      /** Custom PipelineOptions. */
      public interface SpannerToTextOptions
          extends PipelineOptions, SpannerReadOptions, FilesystemWriteOptions {
    
        @TemplateParameter.GcsWriteFolder(
            order = 1,
            groupName = "Target",
            optional = true,
            description = "Cloud Storage temp directory for storing CSV files",
            helpText = "The Cloud Storage path where temporary CSV files are written.",
            example = "gs://your-bucket/your-path")
        ValueProvider<String> getCsvTempDirectory();
    
        @SuppressWarnings("unused")
        void setCsvTempDirectory(ValueProvider<String> value);
    
        @TemplateParameter.Enum(
            order = 2,
            groupName = "Source",
            enumOptions = {
              @TemplateEnumOption("LOW"),
              @TemplateEnumOption("MEDIUM"),
              @TemplateEnumOption("HIGH")
            },
            optional = true,
            description = "Priority for Spanner RPC invocations",
            helpText =
                "The request priority (https://cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions)"
                    + " for Spanner calls. Possible values are `HIGH`, `MEDIUM`, `LOW`. The default value is `MEDIUM`.")
        ValueProvider<RpcPriority> getSpannerPriority();
    
        void setSpannerPriority(ValueProvider<RpcPriority> value);
      }
    
      /**
       * Runs a pipeline which reads in Records from Spanner, and writes the CSV to TextIO sink.
       *
       * @param args arguments to the pipeline
       */
      public static void main(String[] args) {
        LOG.info("Starting pipeline setup");
        PipelineOptionsFactory.register(SpannerToTextOptions.class);
        SpannerToTextOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(SpannerToTextOptions.class);
    
        FileSystems.setDefaultPipelineOptions(options);
        Pipeline pipeline = Pipeline.create(options);
    
        SpannerConfig spannerConfig =
            SpannerConfig.create()
                .withHost(options.getSpannerHost())
                .withProjectId(options.getSpannerProjectId())
                .withInstanceId(options.getSpannerInstanceId())
                .withDatabaseId(options.getSpannerDatabaseId())
                .withRpcPriority(options.getSpannerPriority())
                .withDataBoostEnabled(options.getDataBoostEnabled());
    
        PTransform<PBegin, PCollection<ReadOperation>> spannerExport =
            SpannerConverters.ExportTransformFactory.create(
                options.getSpannerTable(),
                spannerConfig,
                options.getTextWritePrefix(),
                options.getSpannerSnapshotTime());
    
        /* CreateTransaction and CreateTransactionFn classes in SpannerIO
         * only take a timestamp object for exact staleness which works when
         * parameters are provided during template compile time. They do not work with
         * a Timestamp valueProvider which can take parameters at runtime. Hence a new
         * ParDo class CreateTransactionFnWithTimestamp had to be created for this
         * purpose.
         */
        PCollectionView<Transaction> tx =
            pipeline
                .apply("Setup for Transaction", Create.of(1))
                .apply(
                    "Create transaction",
                    ParDo.of(
                        new CreateTransactionFnWithTimestamp(
                            spannerConfig, options.getSpannerSnapshotTime())))
                .apply("As PCollectionView", View.asSingleton());
    
        PCollection<String> csv =
            pipeline
                .apply("Create export", spannerExport)
                // We need to use SpannerIO.readAll() instead of SpannerIO.read()
                // because ValueProvider parameters such as table name required for
                // SpannerIO.read() can be read only inside DoFn but SpannerIO.read() is of
                // type PTransform<PBegin, Struct>, which prevents prepending it with DoFn that reads
                // these parameters at the pipeline execution time.
                .apply(
                    "Read all records",
                    SpannerIO.readAll().withTransaction(tx).withSpannerConfig(spannerConfig))
                .apply(
                    "Struct To Csv",
                    MapElements.into(TypeDescriptors.strings())
                        .via(struct -> (new SpannerConverters.StructCsvPrinter()).print(struct)));
    
        ValueProvider<ResourceId> tempDirectoryResource =
            ValueProvider.NestedValueProvider.of(
                eitherOrValueProvider(options.getCsvTempDirectory(), options.getTextWritePrefix()),
                (SerializableFunction<String, ResourceId>) s -> FileSystems.matchNewResource(s, true));
    
        csv.apply(
            "Write to storage",
            TextIO.write()
                .to(options.getTextWritePrefix())
                .withSuffix(".csv")
                .withTempDirectory(tempDirectoryResource));
    
        pipeline.run();
        LOG.info("Completed pipeline setup");
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
