---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-bigtable/
title: BigQuery to Bigtable template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:06.393255+00:00
---

# BigQuery to Bigtable template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  BigQuery to Bigtable template Stay organized with collections  Save and categorize content based on your preferences. 

The BigQuery to Bigtable template is a batch pipeline that copies data from a BigQuery table into an existing Bigtable table. The template can either read the entire table or read specific records using a supplied query. 

## Pipeline requirements

  * The source BigQuery table must exist.
  * The Bigtable table must exist.
  * The [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) needs the `roles/bigquery.datasets.create` permission. For more information, see [Introduction to IAM](https://docs.cloud.google.com/bigquery/docs/access-control). 



## Template parameters

### Required parameters

  * **readIdColumn** : The name of the BigQuery column storing the unique identifier of the row.
  * **bigtableWriteInstanceId** : The ID of the Bigtable instance that contains the table.
  * **bigtableWriteTableId** : The ID of the Bigtable table to write to.
  * **bigtableWriteColumnFamily** : The name of the column family of the Bigtable table to write data into.



### Optional parameters

  * **timestampColumn** : The name of the BigQuery column to be used as the timestamp for the column's cell in Bigtable. The value must be millisecond precision, e.g. INT64 / Long. If a row does not contain the field, the default write timestamp will be used. The column specified will not be included as part of the row in Bigtable as a separate column.
  * **skipNullValues** : Flag to indicate whether nulls may propagate as an empty value or column skipped completely to adhere to Bigtable sparse table format. In cases where this leads to an empty row, e.g. a valid rowkey, but no columns, the row cannot be written to bigtable and the row will be skipped. Defaults to: false.
  * **inputTableSpec** : The BigQuery table to read from. If you specify `inputTableSpec`, the template reads the data directly from BigQuery storage by using the BigQuery Storage Read API (<https://cloud.google.com/bigquery/docs/reference/storage>). For information about limitations in the Storage Read API, see <https://cloud.google.com/bigquery/docs/reference/storage#limitations>. You must specify either `inputTableSpec` or `query`. If you set both parameters, the template uses the `query` parameter. For example, `<BIGQUERY_PROJECT>:<DATASET_NAME>.<INPUT_TABLE>`.
  * **outputDeadletterTable** : The BigQuery table for messages that failed to reach the output table. If a table doesn't exist, it is created during pipeline execution. If not specified, `<outputTableSpec>_error_records` is used. For example, `<PROJECT_ID>:<DATASET_NAME>.<DEADLETTER_TABLE>`.
  * **query** : The SQL query to use to read data from BigQuery. If the BigQuery dataset is in a different project than the Dataflow job, specify the full dataset name in the SQL query, for example: <PROJECT_ID>.<DATASET_NAME>.<TABLE_NAME>. By default, the `query` parameter uses GoogleSQL (<https://cloud.google.com/bigquery/docs/introduction-sql>), unless `useLegacySql` is `true`. You must specify either `inputTableSpec` or `query`. If you set both parameters, the template uses the `query` parameter. For example, `select * from sampledb.sample_table`.
  * **useLegacySql** : Set to `true` to use legacy SQL. This parameter only applies when using the `query` parameter. Defaults to `false`.
  * **queryLocation** : Needed when reading from an authorized view without underlying table's permission. For example, `US`.
  * **queryTempDataset** : With this option, you can set an existing dataset to create the temporary table to store the results of the query. For example, `temp_dataset`.
  * **KMSEncryptionKey** : If reading from BigQuery using query source, use this Cloud KMS key to encrypt any temporary tables created. For example, `projects/your-project/locations/global/keyRings/your-keyring/cryptoKeys/your-key`.
  * **bigtableRpcAttemptTimeoutMs** : The timeout for each Bigtable RPC attempt in milliseconds.
  * **bigtableRpcTimeoutMs** : The total timeout for a Bigtable RPC operation in milliseconds.
  * **bigtableAdditionalRetryCodes** : The additional retry codes. For example, `RESOURCE_EXHAUSTED,DEADLINE_EXCEEDED`.
  * **bigtableWriteAppProfile** : The ID of the Bigtable application profile to use for the export. If you do not specify an app profile, Bigtable uses the default app profile (<https://cloud.google.com/bigtable/docs/app-profiles#default-app-profile>) of the instance.
  * **bigtableWriteProjectId** : The ID of the Google Cloud project that contains the Bigtable instanceto write data to.
  * **bigtableBulkWriteLatencyTargetMs** : The latency target of Bigtable in milliseconds for latency-based throttling.
  * **bigtableBulkWriteMaxRowKeyCount** : The maximum number of row keys in a Bigtable batch write operation.
  * **bigtableBulkWriteMaxRequestSizeBytes** : The maximum bytes to include per Bigtable batch write operation.
  * **bigtableBulkWriteFlowControl** : When set to true, enables bulk write flow control which will useserver's signal to throttle the writes. Defaults to: false.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **BigQuery to Bigtable** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/BigQuery_to_Bigtable \
        --parameters \
    readIdColumn=READ_COLUMN_ID,\
    inputTableSpec=INPUT_TABLE_SPEC,\
    bigtableWriteInstanceId=BIGTABLE_INSTANCE_ID,\
    bigtableWriteTableId=BIGTABLE_TABLE_ID,\
    bigtableWriteColumnFamily=BIGTABLE_COLUMN_FAMILY

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `READ_COLUMN_ID`: your BigQuery unique id column.
  * `INPUT_TABLE_SPEC`: your BigQuery table name.
  * `BIGTABLE_INSTANCE_ID`: your Bigtable instance id.
  * `BIGTABLE_TABLE_ID`: your Bigtable table id.
  * `BIGTABLE_COLUMN_FAMILY`: your Bigtable table column family.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "readIdColumn": "READ_COLUMN_ID",
              "inputTableSpec": "INPUT_TABLE_SPEC",
              "bigtableWriteInstanceId": "BIGTABLE_INSTANCE_ID",
              "bigtableWriteTableId": "BIGTABLE_TABLE_ID",
              "bigtableWriteColumnFamily": "BIGTABLE_COLUMN_FAMILY"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/BigQuery_to_Bigtable",
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
  * `READ_COLUMN_ID`: your BigQuery unique id column.
  * `INPUT_TABLE_SPEC`: your BigQuery table name.
  * `BIGTABLE_INSTANCE_ID`: your Bigtable instance id.
  * `BIGTABLE_TABLE_ID`: your Bigtable table id.
  * `BIGTABLE_COLUMN_FAMILY`: your Bigtable table column family.



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2021 Google LLC
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
    
    import static com.google.cloud.teleport.v2.bigtable.utils.BigtableConfig.generateCloudBigtableWriteConfiguration;
    
    import com.google.cloud.bigtable.beam.CloudBigtableIO;
    import com.google.cloud.bigtable.beam.CloudBigtableTableConfiguration;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.bigtable.options.BigtableCommonOptions;
    import com.google.cloud.teleport.v2.bigtable.transforms.BigtableConverters;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.templates.BigQueryToBigtable.BigQueryToBigtableOptions;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.extensions.gcp.options.GcpOptions;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.hadoop.hbase.client.Mutation;
    import org.apache.hadoop.hbase.client.Put;
    import org.apache.hadoop.hbase.util.Bytes;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * Dataflow template which reads BigQuery data and writes it to Bigtable. The source data can be
     * either a BigQuery table or an SQL query.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/bigquery-to-bigtable/README_BigQuery_to_Bigtable.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "BigQuery_to_Bigtable",
        category = TemplateCategory.BATCH,
        displayName = "BigQuery to Bigtable",
        description = "A pipeline to export a BigQuery table into Bigtable.",
        optionsClass = BigQueryToBigtableOptions.class,
        optionsOrder = {
          BigQueryToBigtableOptions.class,
          BigQueryConverters.BigQueryReadOptions.class,
          BigtableCommonOptions.class,
          BigtableCommonOptions.WriteOptions.class
        },
        optionalOptions = {"inputTableSpec", "timestampColumn", "skipNullValues"},
        flexContainerName = "bigquery-to-bigtable",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-bigtable",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The source BigQuery table must exist.",
          "The Bigtable table must exist.",
          "The <a href=\"https://cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account\">worker service account</a>"
              + " needs the <code>roles/bigquery.datasets.create</code> permission. For"
              + " more information, see <a href=\"https://cloud.google.com/bigquery/docs/access-control\">Introduction to IAM</a>."
        })
    public class BigQueryToBigtable {
    
      /**
       * The {@link BigQueryToBigtableOptions} class provides the custom execution options passed by the
       * executor at the command-line.
       */
      public interface BigQueryToBigtableOptions
          extends BigQueryConverters.BigQueryReadOptions,
              BigtableCommonOptions.WriteOptions,
              GcpOptions {
    
        @TemplateParameter.Text(
            order = 1,
            regexes = {"[A-Za-z_][A-Za-z_0-9]*"},
            description = "Unique identifier column",
            helpText = "The name of the BigQuery column storing the unique identifier of the row.")
        @Required
        String getReadIdColumn();
    
        void setReadIdColumn(String value);
    
        @TemplateParameter.Text(
            order = 2,
            optional = true,
            regexes = {"[A-Za-z_][A-Za-z_0-9]*"},
            description = "Timestamp column identifier",
            helpText =
                "The name of the BigQuery column to be used as the timestamp for the column's cell in Bigtable. The value"
                    + " must be millisecond precision, e.g. INT64 / Long. If a row does not contain the field, the default write"
                    + " timestamp will be used. The column specified will not be included as part of the row in Bigtable as"
                    + " a separate column.")
        @Default.String("")
        String getTimestampColumn();
    
        void setTimestampColumn(String value);
    
        @TemplateParameter.Boolean(
            order = 3,
            optional = true,
            description = "Flag to skip null values",
            helpText =
                "Flag to indicate whether nulls may propagate as an empty value or column skipped completely to adhere to "
                    + " Bigtable sparse table format. In cases where this leads to an empty row, e.g. a valid rowkey, but no "
                    + " columns, the row cannot be written to bigtable and the row will be skipped.")
        @Default.Boolean(false)
        Boolean getSkipNullValues();
    
        void setSkipNullValues(Boolean value);
      }
    
      /**
       * Runs a pipeline which reads data from BigQuery and writes it to Bigtable.
       *
       * @param args arguments to the pipeline
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        BigQueryToBigtableOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(BigQueryToBigtableOptions.class);
    
        CloudBigtableTableConfiguration bigtableTableConfig =
            generateCloudBigtableWriteConfiguration(options);
    
        Pipeline pipeline = Pipeline.create(options);
    
        pipeline
            .apply(
                "AvroToMutation",
                BigQueryConverters.ReadBigQuery.<Mutation>newBuilder()
                    .setOptions(options.as(BigQueryToBigtableOptions.class))
                    .setReadFunction(
                        BigQueryIO.read(
                            BigtableConverters.AvroToMutation.newBuilder()
                                .setColumnFamily(options.getBigtableWriteColumnFamily())
                                .setRowkey(options.getReadIdColumn())
                                .setSkipNullValues(options.getSkipNullValues())
                                .setTimestampColumn(options.getTimestampColumn())
                                .build()))
                    .build())
            .apply("VerifyAndFilterMutations", ParDo.of((new VerifyAndFilterMutationsFn())))
            .apply("WriteToTable", CloudBigtableIO.writeToTable(bigtableTableConfig));
    
        pipeline.run();
      }
    
      /**
       * Filter out invalid Bigtable Mutations, additional validations/filters may be applied e.g. An
       * empty mutation is one that contains no actual cell set.
       */
      static class VerifyAndFilterMutationsFn extends DoFn<Mutation, Mutation> {
        private static final Logger LOG = LoggerFactory.getLogger(VerifyAndFilterMutationsFn.class);
    
        @ProcessElement
        public void processElement(@Element Mutation mutation, OutputReceiver<Mutation> receiver) {
          if (mutation instanceof Put && mutation.isEmpty()) {
            LOG.warn("Skipping empty mutation for rowkey: {}", Bytes.toStringBinary(mutation.getRow()));
          } else {
            receiver.output(mutation);
          }
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
