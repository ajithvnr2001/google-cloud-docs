---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/datastore-to-cloud-storage/
title: Datastore to Cloud Storage Text template [Deprecated] \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:24:35.585726+00:00
---

# Datastore to Cloud Storage Text template [Deprecated]  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/datastore-to-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Datastore to Cloud Storage Text template [Deprecated] Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This template is **deprecated** and will be removed in Q3 2023. Please migrate to [ Firestore to Cloud Storage Text](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/firestore-to-cloud-storage) template. 

The Datastore to Cloud Storage Text template is a batch pipeline that reads Datastore entities and writes them to Cloud Storage as text files. You can provide a function to process each entity as a JSON string. If you don't provide such a function, every line in the output file will be a JSON-serialized entity.

## Pipeline requirements

Datastore must be set up in the project before running the pipeline.

## Template parameters

### Required parameters

  * **datastoreReadGqlQuery** : A GQL (<https://cloud.google.com/datastore/docs/reference/gql_reference>) query that specifies which entities to grab. For example, `SELECT * FROM MyKind`.
  * **datastoreReadProjectId** : The ID of the Google Cloud project that contains the Datastore instance that you want to read data from.
  * **textWritePrefix** : The Cloud Storage path prefix that specifies where the data is written. For example, `gs://mybucket/somefolder/`.



### Optional parameters

  * **datastoreReadNamespace** : The namespace of the requested entities. To use the default namespace, leave this parameter blank.
  * **javascriptTextTransformGcsPath** : The Cloud Storage URI of the .js file that defines the JavaScript user-defined function (UDF) to use. For example, `gs://my-bucket/my-udfs/my_file.js`.
  * **javascriptTextTransformFunctionName** : The name of the JavaScript user-defined function (UDF) to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see UDF Examples (<https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples>).



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Datastore to Text Files on Cloud Storage** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/Datastore_to_GCS_Text \
        --region REGION_NAME \
        --parameters \
    datastoreReadGqlQuery="SELECT * FROM DATASTORE_KIND",\
    datastoreReadProjectId=DATASTORE_PROJECT_ID,\
    datastoreReadNamespace=DATASTORE_NAMESPACE,\
    javascriptTextTransformGcsPath=PATH_TO_JAVASCRIPT_UDF_FILE,\
    javascriptTextTransformFunctionName=JAVASCRIPT_FUNCTION,\
    textWritePrefix=gs://BUCKET_NAME/output/

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `DATASTORE_PROJECT_ID`: the Google Cloud project ID where the Datastore instance exists
  * `DATASTORE_KIND`: the type of your Datastore entities
  * `DATASTORE_NAMESPACE`: the namespace of your Datastore entities
  * `JAVASCRIPT_FUNCTION`: the name of the JavaScript user-defined function (UDF) that you want to use 

For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see [UDF Examples](https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples). 

  * `PATH_TO_JAVASCRIPT_UDF_FILE`: the Cloud Storage URI of the `.js` file that defines the JavaScript user-defined function (UDF) you want to use—for example, `gs://my-bucket/my-udfs/my_file.js`



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Datastore_to_GCS_Text
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "datastoreReadGqlQuery": "SELECT * FROM DATASTORE_KIND"
           "datastoreReadProjectId": "DATASTORE_PROJECT_ID",
           "datastoreReadNamespace": "DATASTORE_NAMESPACE",
           "javascriptTextTransformGcsPath": "PATH_TO_JAVASCRIPT_UDF_FILE",
           "javascriptTextTransformFunctionName": "JAVASCRIPT_FUNCTION",
           "textWritePrefix": "gs://BUCKET_NAME/output/"
       },
       "environment": { "zone": "us-central1-f" }
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
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `DATASTORE_PROJECT_ID`: the Google Cloud project ID where the Datastore instance exists
  * `DATASTORE_KIND`: the type of your Datastore entities
  * `DATASTORE_NAMESPACE`: the namespace of your Datastore entities
  * `JAVASCRIPT_FUNCTION`: the name of the JavaScript user-defined function (UDF) that you want to use 

For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see [UDF Examples](https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples). 

  * `PATH_TO_JAVASCRIPT_UDF_FILE`: the Cloud Storage URI of the `.js` file that defines the JavaScript user-defined function (UDF) you want to use—for example, `gs://my-bucket/my-udfs/my_file.js`



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
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.templates.DatastoreToText.DatastoreToTextOptions;
    import com.google.cloud.teleport.templates.common.DatastoreConverters.DatastoreReadOptions;
    import com.google.cloud.teleport.templates.common.DatastoreConverters.ReadJsonEntities;
    import com.google.cloud.teleport.templates.common.FirestoreNestedValueProvider;
    import com.google.cloud.teleport.templates.common.JavascriptTextTransformer.JavascriptTextTransformerOptions;
    import com.google.cloud.teleport.templates.common.JavascriptTextTransformer.TransformTextViaJavascript;
    import com.google.cloud.teleport.templates.common.TextConverters.FilesystemWriteOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    
    /**
     * Dataflow template which copies Datastore Entities to a Text sink. Text is encoded using JSON
     * encoded entity in the v1/Entity rest format: <a
     * href="https://cloud.google.com/datastore/docs/reference/rest/v1/Entity">Entity</a>
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Datastore_to_GCS_Text.md">README_Datastore_to_GCS_Text</a>
     * or <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Firestore_to_GCS_Text.md">README_Firestore_to_GCS_Text</a>
     * for instructions on how to use or change this template.
     */
    @Template(
        name = "Datastore_to_GCS_Text",
        category = TemplateCategory.LEGACY,
        displayName = "Datastore to Text Files on Cloud Storage [Deprecated]",
        description =
            "The Datastore to Cloud Storage Text template is a batch pipeline that reads Datastore entities and writes them "
                + "to Cloud Storage as text files. You can provide a function to process each entity as a JSON string. "
                + "If you don't provide such a function, every line in the output file will be a JSON-serialized entity.",
        optionsClass = DatastoreToTextOptions.class,
        skipOptions = {
          "firestoreReadNamespace",
          "firestoreReadGqlQuery",
          "firestoreReadProjectId",
          "javascriptTextTransformReloadIntervalMinutes"
        },
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/datastore-to-cloud-storage",
        contactInformation = "https://cloud.google.com/support",
        requirements = {"Datastore must be set up in the project before running the pipeline."})
    @Template(
        name = "Firestore_to_GCS_Text",
        category = TemplateCategory.BATCH,
        displayName = "Firestore (Datastore mode) to Text Files on Cloud Storage",
        description =
            "The Firestore to Cloud Storage Text template is a batch pipeline that reads Firestore entities and writes them "
                + "to Cloud Storage as text files. You can provide a function to process each entity as a JSON string. "
                + "If you don't provide such a function, every line in the output file will be a JSON-serialized entity.",
        optionsClass = DatastoreToTextOptions.class,
        skipOptions = {
          "datastoreReadNamespace",
          "datastoreReadGqlQuery",
          "datastoreReadProjectId",
          "javascriptTextTransformReloadIntervalMinutes"
        },
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/firestore-to-cloud-storage",
        contactInformation = "https://cloud.google.com/support",
        requirements = {"Firestore must be set up in the project before running the pipeline."})
    public class DatastoreToText {
    
      public static ValueProvider<String> selectProvidedInput(
          ValueProvider<String> datastoreInput, ValueProvider<String> firestoreInput) {
        return new FirestoreNestedValueProvider(datastoreInput, firestoreInput);
      }
    
      /** Custom PipelineOptions. */
      public interface DatastoreToTextOptions
          extends PipelineOptions,
              DatastoreReadOptions,
              JavascriptTextTransformerOptions,
              FilesystemWriteOptions {}
    
      /**
       * Runs a pipeline which reads in Entities from Datastore, passes in the JSON encoded Entities to
       * a Javascript UDF, and writes the JSON to TextIO sink.
       *
       * @param args arguments to the pipeline
       */
      public static void main(String[] args) {
        DatastoreToTextOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(DatastoreToTextOptions.class);
    
        Pipeline pipeline = Pipeline.create(options);
    
        pipeline
            .apply(
                ReadJsonEntities.newBuilder()
                    .setGqlQuery(
                        selectProvidedInput(
                            options.getDatastoreReadGqlQuery(), options.getFirestoreReadGqlQuery()))
                    .setProjectId(
                        selectProvidedInput(
                            options.getDatastoreReadProjectId(), options.getFirestoreReadProjectId()))
                    .setNamespace(
                        selectProvidedInput(
                            options.getDatastoreReadNamespace(), options.getFirestoreReadNamespace()))
                    .build())
            .apply(
                TransformTextViaJavascript.newBuilder()
                    .setFileSystemPath(options.getJavascriptTextTransformGcsPath())
                    .setFunctionName(options.getJavascriptTextTransformFunctionName())
                    .build())
            .apply(TextIO.write().to(options.getTextWritePrefix()).withSuffix(".json"));
    
        pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
