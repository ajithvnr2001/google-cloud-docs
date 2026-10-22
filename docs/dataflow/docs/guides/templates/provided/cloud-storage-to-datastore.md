---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-datastore/
title: Cloud Storage Text to Datastore template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:33.207287+00:00
---

# Cloud Storage Text to Datastore template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-datastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage Text to Datastore template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Cloud Storage Text to Datastore template is deprecated and was removed in Q3 2023. You should migrate to the [Cloud Storage Text to Firestore](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-firestore) template instead. 

This template is a batch pipeline that reads text files from Cloud Storage and writes JSON-encoded entities to Datastore. Each line in the input text files must be in the [specified JSON format](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#Entity).

## Pipeline requirements

  * Datastore must be enabled in the destination project.



## Template parameters

### Required parameters

  * **textReadPattern** : A Cloud Storage path pattern that specifies the location of your text data files. For example, `gs://mybucket/somepath/*.json`.
  * **datastoreWriteProjectId** : The ID of the Google Cloud project to write the Datastore entities to.
  * **errorWritePath** : The error log output file to use for write failures that occur during processing. For example, `gs://your-bucket/errors/`.



### Optional parameters

  * **javascriptTextTransformGcsPath** : The Cloud Storage URI of the .js file that defines the JavaScript user-defined function (UDF) to use. For example, `gs://my-bucket/my-udfs/my_file.js`.
  * **javascriptTextTransformFunctionName** : The name of the JavaScript user-defined function (UDF) to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see UDF Examples (<https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples>).
  * **datastoreHintNumWorkers** : Hint for the expected number of workers in the Datastore ramp-up throttling step. Defaults to `500`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Text Files on Cloud Storage to Datastore** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/GCS_Text_to_Datastore \
        --region REGION_NAME \
        --parameters \
    textReadPattern=PATH_TO_INPUT_TEXT_FILES,\
    javascriptTextTransformGcsPath=PATH_TO_JAVASCRIPT_UDF_FILE,\
    javascriptTextTransformFunctionName=JAVASCRIPT_FUNCTION,\
    datastoreWriteProjectId=PROJECT_ID,\
    errorWritePath=ERROR_FILE_WRITE_PATH

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `PATH_TO_INPUT_TEXT_FILES`: the input files pattern on Cloud Storage
  * `JAVASCRIPT_FUNCTION`: the name of the JavaScript user-defined function (UDF) that you want to use 

For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see [UDF Examples](https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples). 

  * `PATH_TO_JAVASCRIPT_UDF_FILE`: the Cloud Storage URI of the `.js` file that defines the JavaScript user-defined function (UDF) you want to use—for example, `gs://my-bucket/my-udfs/my_file.js`
  * `ERROR_FILE_WRITE_PATH`: your desired path to error file on Cloud Storage



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/GCS_Text_to_Datastore
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "textReadPattern": "PATH_TO_INPUT_TEXT_FILES",
           "javascriptTextTransformGcsPath": "PATH_TO_JAVASCRIPT_UDF_FILE",
           "javascriptTextTransformFunctionName": "JAVASCRIPT_FUNCTION",
           "datastoreWriteProjectId": "PROJECT_ID",
           "errorWritePath": "ERROR_FILE_WRITE_PATH"
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
  * `PATH_TO_INPUT_TEXT_FILES`: the input files pattern on Cloud Storage
  * `JAVASCRIPT_FUNCTION`: the name of the JavaScript user-defined function (UDF) that you want to use 

For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see [UDF Examples](https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples). 

  * `PATH_TO_JAVASCRIPT_UDF_FILE`: the Cloud Storage URI of the `.js` file that defines the JavaScript user-defined function (UDF) you want to use—for example, `gs://my-bucket/my-udfs/my_file.js`
  * `ERROR_FILE_WRITE_PATH`: your desired path to error file on Cloud Storage



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
    
    import com.google.cloud.teleport.metadata.MultiTemplate;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.templates.TextToDatastore.TextToDatastoreOptions;
    import com.google.cloud.teleport.templates.common.DatastoreConverters.DatastoreWriteOptions;
    import com.google.cloud.teleport.templates.common.DatastoreConverters.WriteJsonEntities;
    import com.google.cloud.teleport.templates.common.ErrorConverters.ErrorWriteOptions;
    import com.google.cloud.teleport.templates.common.ErrorConverters.LogErrors;
    import com.google.cloud.teleport.templates.common.FirestoreNestedValueProvider;
    import com.google.cloud.teleport.templates.common.JavascriptTextTransformer.JavascriptTextTransformerOptions;
    import com.google.cloud.teleport.templates.common.JavascriptTextTransformer.TransformTextViaJavascript;
    import com.google.cloud.teleport.templates.common.TextConverters.FilesystemReadOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.values.TupleTag;
    
    /**
     * Dataflow template which reads from a Text Source and writes JSON encoded Entities into Datastore.
     * The JSON is expected to be in the format of: <a
     * href="https://cloud.google.com/datastore/docs/reference/rest/v1/Entity">Entity</a>
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_GCS_Text_to_Datastore.md">README
     * Datastore</a> or <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_GCS_Text_to_Firestore.md">README
     * Firestore</a> for instructions on how to use or modify this template.
     */
    @MultiTemplate({
      @Template(
          name = "GCS_Text_to_Datastore",
          category = TemplateCategory.LEGACY,
          displayName = "Text Files on Cloud Storage to Datastore [Deprecated]",
          description =
              "The Cloud Storage Text to Datastore template is a batch pipeline that reads from text files stored in "
                  + "Cloud Storage and writes JSON encoded Entities to Datastore. "
                  + "Each line in the input text files must be in the <a href=\"https://cloud.google.com/datastore/docs/reference/rest/v1/Entity\">specified JSON format</a>.",
          optionsClass = TextToDatastoreOptions.class,
          skipOptions = {
            "firestoreWriteProjectId",
            "firestoreWriteEntityKind",
            "firestoreWriteNamespace",
            "firestoreHintNumWorkers",
            "javascriptTextTransformReloadIntervalMinutes",
            // This template doesn't use neither firestoreWriteEntityKind/Namespace
            // nor datastoreWriteEntityKind/Namespace pipeline options.
            "datastoreWriteEntityKind",
            "datastoreWriteNamespace"
          },
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-datastore",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {"Datastore must be enabled in the destination project."}),
      @Template(
          name = "GCS_Text_to_Firestore",
          category = TemplateCategory.BATCH,
          displayName = "Text Files on Cloud Storage to Firestore (Datastore mode)",
          description =
              "The Cloud Storage Text to Firestore template is a batch pipeline that reads from text files stored in "
                  + "Cloud Storage and writes JSON encoded Entities to Firestore. "
                  + "Each line in the input text files must be in the <a href=\"https://cloud.google.com/datastore/docs/reference/rest/v1/Entity\">specified JSON format</a>.",
          optionsClass = TextToDatastoreOptions.class,
          skipOptions = {
            "datastoreWriteProjectId",
            "datastoreWriteEntityKind",
            "datastoreWriteNamespace",
            "datastoreHintNumWorkers",
            "javascriptTextTransformReloadIntervalMinutes",
            // This template doesn't use neither firestoreWriteEntityKind/Namespace
            // nor datastoreWriteEntityKind/Namespace pipeline options.
            "firestoreWriteEntityKind",
            "firestoreWriteNamespace"
          },
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-firestore",
          contactInformation = "https://cloud.google.com/support",
          requirements = {"Firestore must be enabled in the destination project."})
    })
    public class TextToDatastore {
    
      public static <T> ValueProvider<T> selectProvidedInput(
          ValueProvider<T> datastoreInput, ValueProvider<T> firestoreInput) {
        return new FirestoreNestedValueProvider(datastoreInput, firestoreInput);
      }
    
      /** TextToDatastore Pipeline Options. */
      public interface TextToDatastoreOptions
          extends PipelineOptions,
              FilesystemReadOptions,
              JavascriptTextTransformerOptions,
              DatastoreWriteOptions,
              ErrorWriteOptions {}
    
      /**
       * Runs a pipeline which reads from a Text Source, passes the Text to a Javascript UDF, writes the
       * JSON encoded Entities to a TextIO sink.
       *
       * <p>If your Text Source does not contain JSON encoded Entities, then you'll need to supply a
       * Javascript UDF which transforms your data to be JSON encoded Entities.
       *
       * @param args arguments to the pipeline
       */
      public static void main(String[] args) {
        TextToDatastoreOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(TextToDatastoreOptions.class);
    
        TupleTag<String> errorTag = new TupleTag<String>("errors") {};
    
        Pipeline pipeline = Pipeline.create(options);
    
        pipeline
            .apply(TextIO.read().from(options.getTextReadPattern()))
            .apply(
                TransformTextViaJavascript.newBuilder()
                    .setFileSystemPath(options.getJavascriptTextTransformGcsPath())
                    .setFunctionName(options.getJavascriptTextTransformFunctionName())
                    .build())
            .apply(
                WriteJsonEntities.newBuilder()
                    .setProjectId(
                        selectProvidedInput(
                            options.getDatastoreWriteProjectId(), options.getFirestoreWriteProjectId()))
                    .setHintNumWorkers(
                        selectProvidedInput(
                            options.getDatastoreHintNumWorkers(), options.getFirestoreHintNumWorkers()))
                    .setErrorTag(errorTag)
                    .build())
            .apply(
                LogErrors.newBuilder()
                    .setErrorWritePath(options.getErrorWritePath())
                    .setErrorTag(errorTag)
                    .build());
    
        pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
