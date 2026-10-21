---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/file-format-conversion/
title: File Format Conversion (Avro, Parquet, CSV) template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:30:59.329952+00:00
---

# File Format Conversion (Avro, Parquet, CSV) template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/file-format-conversion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  File Format Conversion (Avro, Parquet, CSV) template Stay organized with collections  Save and categorize content based on your preferences. 

The File Format Conversion template is a batch pipeline that converts files stored on Cloud Storage from one supported format to another.

**The following format conversions are supported:**

  * CSV to Avro
  * CSV to Parquet
  * Avro to Parquet
  * Parquet to Avro



## Pipeline requirements

  * The output Cloud Storage bucket must exist before running the pipeline.



## Template parameters

Parameter | Description  
---|---  
`inputFileFormat` | The input file format. Must be one of `[csv, avro, parquet]`.  
`outputFileFormat` | The output file format. Must be one of `[avro, parquet]`.  
`inputFileSpec` | The Cloud Storage path pattern for input files. For example, `gs://bucket-name/path/*.csv`  
`outputBucket` | The Cloud Storage folder to write output files. This path must end with a slash. For example, `gs://bucket-name/output/`  
`schema` | The Cloud Storage path to the Avro schema file. For example, `gs://bucket-name/schema/my-schema.avsc`  
`containsHeaders` | (Optional) The input CSV files contain a header record (true/false). The default value is `false`. Only required when reading CSV files.  
`csvFormat` | (Optional) The CSV format specification to use for parsing records. The default value is `Default`. See [Apache Commons CSV Format](https://commons.apache.org/proper/commons-csv/apidocs/org/apache/commons/csv/CSVFormat.html) for more details.  
`delimiter` | (Optional) The field delimiter used by the input CSV files.  
`outputFilePrefix` | (Optional) The output file prefix. The default value is `output`.  
`numShards` | (Optional) The number of output file shards.  
  
## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Convert file formats** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/File_Format_Conversion \
        --parameters \
    inputFileFormat=INPUT_FORMAT,\
    outputFileFormat=OUTPUT_FORMAT,\
    inputFileSpec=INPUT_FILES,\
    schema=SCHEMA,\
    outputBucket=OUTPUT_FOLDER

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `INPUT_FORMAT`: the file format of the input file; must be one of `[csv, avro, parquet]`
  * `OUTPUT_FORMAT`: the file format of the output files; must be one of `[avro, parquet]`
  * `INPUT_FILES`: the path pattern for input files
  * `OUTPUT_FOLDER`: your Cloud Storage folder for output files
  * `SCHEMA`: the path to the Avro schema file



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "inputFileFormat": "INPUT_FORMAT",
              "outputFileFormat": "OUTPUT_FORMAT",
              "inputFileSpec": "INPUT_FILES",
              "schema": "SCHEMA",
              "outputBucket": "OUTPUT_FOLDER"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/File_Format_Conversion",
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
  * `INPUT_FORMAT`: the file format of the input file; must be one of `[csv, avro, parquet]`
  * `OUTPUT_FORMAT`: the file format of the output files; must be one of `[avro, parquet]`
  * `INPUT_FILES`: the path pattern for input files
  * `OUTPUT_FOLDER`: your Cloud Storage folder for output files
  * `SCHEMA`: the path to the Avro schema file



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2019 Google LLC
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
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.metadata.TemplateParameter.TemplateEnumOption;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.templates.FileFormatConversion.FileFormatConversionOptions;
    import com.google.cloud.teleport.v2.transforms.AvroConverters.AvroOptions;
    import com.google.cloud.teleport.v2.transforms.CsvConverters.CsvPipelineOptions;
    import com.google.cloud.teleport.v2.transforms.ParquetConverters.ParquetOptions;
    import java.util.EnumMap;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link FileFormatConversion} pipeline takes in an input file, converts it to a desired format
     * and saves it to Cloud Storage. Supported file transformations are:
     *
     * <ul>
     *   <li>Csv to Avro
     *   <li>Csv to Parquet
     *   <li>Avro to Parquet
     *   <li>Parquet to Avro
     * </ul>
     *
     * <p><b>Pipeline Requirements</b>
     *
     * <ul>
     *   <li>Input file exists in Google Cloud Storage.
     *   <li>Google Cloud Storage output bucket exists.
     * </ul>
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/file-format-conversion/README_File_Format_Conversion.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "File_Format_Conversion",
        category = TemplateCategory.UTILITIES,
        displayName = "Convert file formats between Avro, Parquet & CSV",
        description = {
          "The File Format Conversion template is a batch pipeline that converts files stored on Cloud Storage from one supported format to another.\n",
          "The following format conversions are supported:\n"
              + "- CSV to Avro\n"
              + "- CSV to Parquet\n"
              + "- Avro to Parquet\n"
              + "- Parquet to Avro"
        },
        optionsClass = FileFormatConversionOptions.class,
        optionalOptions = {"deadletterTable"},
        flexContainerName = "file-format-conversion",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/file-format-conversion",
        contactInformation = "https://cloud.google.com/support",
        requirements = {"The output Cloud Storage bucket must exist before running the pipeline."})
    public class FileFormatConversion {
    
      /** Logger for class. */
      private static final Logger LOG = LoggerFactory.getLogger(FileFormatConversionFactory.class);
    
      private static EnumMap<ValidFileFormats, String> validFileFormats =
          new EnumMap<ValidFileFormats, String>(ValidFileFormats.class);
    
      /**
       * The {@link FileFormatConversionOptions} provides the custom execution options passed by the
       * executor at the command-line.
       */
      public interface FileFormatConversionOptions
          extends PipelineOptions, CsvPipelineOptions, AvroOptions, ParquetOptions {
        @TemplateParameter.Enum(
            order = 1,
            enumOptions = {
              @TemplateEnumOption("avro"),
              @TemplateEnumOption("csv"),
              @TemplateEnumOption("parquet")
            },
            description = "File format of the input files.",
            helpText = "File format of the input files. Needs to be either avro, parquet or csv.")
        @Required
        String getInputFileFormat();
    
        void setInputFileFormat(String inputFileFormat);
    
        @TemplateParameter.Enum(
            order = 2,
            enumOptions = {@TemplateEnumOption("avro"), @TemplateEnumOption("parquet")},
            description = "File format of the output files.",
            helpText = "File format of the output files. Needs to be either avro or parquet.")
        @Required
        String getOutputFileFormat();
    
        void setOutputFileFormat(String outputFileFormat);
      }
    
      /** The {@link ValidFileFormats} enum contains all valid file formats. */
      public enum ValidFileFormats {
        CSV,
        AVRO,
        PARQUET
      }
    
      /**
       * Main entry point for pipeline execution.
       *
       * @param args Command line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        FileFormatConversionOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(FileFormatConversionOptions.class);
    
        run(options);
      }
    
      /**
       * Runs the pipeline to completion with the specified options.
       *
       * @param options The execution options.
       * @return The pipeline result.
       * @throws RuntimeException thrown if incorrect file formats are passed.
       */
      public static PipelineResult run(FileFormatConversionOptions options) {
        String inputFileFormat = options.getInputFileFormat().toUpperCase();
        String outputFileFormat = options.getOutputFileFormat().toUpperCase();
    
        validFileFormats.put(ValidFileFormats.CSV, "CSV");
        validFileFormats.put(ValidFileFormats.AVRO, "AVRO");
        validFileFormats.put(ValidFileFormats.PARQUET, "PARQUET");
    
        if (!validFileFormats.containsValue(inputFileFormat)) {
          throw new IllegalArgumentException("Invalid input file format.");
        }
        if (!validFileFormats.containsValue(outputFileFormat)) {
          throw new IllegalArgumentException("Invalid output file format.");
        }
        if (inputFileFormat.equals(outputFileFormat)) {
          throw new IllegalArgumentException("Input and output file format cannot be the same.");
        }
    
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        pipeline.apply(
            inputFileFormat + " to " + outputFileFormat,
            FileFormatConversionFactory.FileFormat.newBuilder()
                .setOptions(options)
                .setInputFileFormat(inputFileFormat)
                .setOutputFileFormat(outputFileFormat)
                .build());
    
        return pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
