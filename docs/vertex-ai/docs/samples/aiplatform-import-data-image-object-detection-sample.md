---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-import-data-image-object-detection-sample/
title: Import data for image object detection \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:55.800380+00:00
---

# Import data for image object detection  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-import-data-image-object-detection-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Import data for image object detection Stay organized with collections  Save and categorize content based on your preferences. 

Imports data for image object detection using the import_data method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a dataset for training image object detection models](https://docs.cloud.google.com/vertex-ai/docs/image-data/object-detection/create-dataset)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[DatasetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetName.html);
    import com.google.cloud.aiplatform.v1.[DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html);
    import com.google.cloud.aiplatform.v1.[DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html);
    import com.google.cloud.aiplatform.v1.[ImportDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataConfig.html);
    import com.google.cloud.aiplatform.v1.[ImportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataResponse.html);
    import java.io.IOException;
    import java.util.Collections;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ImportDataImageObjectDetectionSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String datasetId = "YOUR_DATASET_ID";
        String gcsSourceUri =
            "gs://YOUR_GCS_SOURCE_BUCKET/path_to_your_image_source/[file.csv/file.jsonl]";
        importDataImageObjectDetectionSample(project, datasetId, gcsSourceUri);
      }
    
      static void importDataImageObjectDetectionSample(
          String project, String datasetId, String gcsSourceUri)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        [DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html) datasetServiceSettings =
            [DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html) datasetServiceClient =
            [DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html).create(datasetServiceSettings)) {
          String location = "us-central1";
          String importSchemaUri =
              "gs://google-cloud-aiplatform/schema/dataset/ioformat/"
                  + "image_bounding_box_io_format_1.0.0.yaml";
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html).Builder gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html).newBuilder();
          gcsSource.[addUris](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.Builder.html#com_google_cloud_aiplatform_v1_GcsSource_Builder_addUris_java_lang_String_)(gcsSourceUri);
          [DatasetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetName.html) datasetName = [DatasetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetName.html).of(project, location, datasetId);
    
          List<ImportDataConfig> importDataConfigList =
              Collections.singletonList(
                  [ImportDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataConfig.html).newBuilder()
                      .setGcsSource(gcsSource)
                      .[setImportSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataConfig.Builder.html#com_google_cloud_aiplatform_v1_ImportDataConfig_Builder_setImportSchemaUri_java_lang_String_)(importSchemaUri)
                      .build());
    
          OperationFuture<ImportDataResponse, ImportDataOperationMetadata> importDataResponseFuture =
              datasetServiceClient.[importDataAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html#com_google_cloud_aiplatform_v1_DatasetServiceClient_importDataAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_DatasetName_java_util_List_com_google_cloud_aiplatform_v1_ImportDataConfig__)(datasetName, importDataConfigList);
          System.out.format(
              "Operation name: %s\n", importDataResponseFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataResponse.html) importDataResponse = importDataResponseFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(300, TimeUnit.SECONDS);
    
          System.out.format(
              "Import Data Image Object Detection Response: %s\n", importDataResponse.toString());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const datasetId = "YOUR_DATASET_ID";
    // const gcsSourceUri = "YOUR_GCS_SOURCE_URI";
    // eg. "gs://<your-gcs-bucket>/<import_source_path>/[file.csv/file.jsonl]"
    // const project = "YOUR_PROJECT_ID";
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Dataset Service Client library
    const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    const datasetServiceClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function importDataImageObjectDetection() {
      const name = datasetServiceClient.datasetPath(project, location, datasetId);
      // Here we use only one import config with one source
      const importConfigs = [
        {
          gcsSource: {uris: [gcsSourceUri]},
          importSchemaUri:
            'gs://google-cloud-aiplatform/schema/dataset/ioformat/image_bounding_box_io_format_1.0.0.yaml',
        },
      ];
      const request = {
        name,
        importConfigs,
      };
    
      // Create Import Data Request
      const [response] = await datasetServiceClient.importData(request);
      console.log(`Long running operation : ${response.name}`);
    
      // Wait for operation to complete
      await response.promise();
    
      console.log(
        `Import data image object detection response : \
          ${JSON.stringify(response.result)}`
      );
    }
    importDataImageObjectDetection();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def import_data_image_object_detection_sample(
        project: str,
        dataset_id: str,
        gcs_source_uri: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
        timeout: int = 1800,
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[DatasetServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.dataset_service.DatasetServiceClient.html)(client_options=client_options)
        import_configs = [
            {
                "gcs_source": {"uris": [gcs_source_uri]},
                "import_schema_uri": "gs://google-cloud-aiplatform/schema/dataset/ioformat/image_bounding_box_io_format_1.0.0.yaml",
            }
        ]
        name = client.[dataset_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.dataset_service.DatasetServiceClient.html#google_cloud_aiplatform_v1_services_dataset_service_DatasetServiceClient_dataset_path)(project=project, location=location, dataset=dataset_id)
        response = client.[import_data](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.dataset_service.DatasetServiceClient.html#google_cloud_aiplatform_v1_services_dataset_service_DatasetServiceClient_import_data)(name=name, import_configs=import_configs)
        print("Long running operation:", response.operation.name)
        import_data_response = response.result(timeout=timeout)
        print("import_data_response:", import_data_response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
