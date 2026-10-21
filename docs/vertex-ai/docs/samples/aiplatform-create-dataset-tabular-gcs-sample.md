---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-dataset-tabular-gcs-sample/
title: Create a dataset for tabular Cloud Storage \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:14.400189+00:00
---

# Create a dataset for tabular Cloud Storage  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-dataset-tabular-gcs-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a dataset for tabular Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Creates a dataset for tabular Cloud Storage using the create_dataset method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a dataset for training classification and regression models](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/classification-regression/create-dataset)
  * [Create a dataset for training forecast models](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/forecasting/create-dataset)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[CreateDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset.html);
    import com.google.cloud.aiplatform.v1.[DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html);
    import com.google.cloud.aiplatform.v1.[DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDatasetTabularGcsSample {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String datasetDisplayName = "YOUR_DATASET_DISPLAY_NAME";
        String gcsSourceUri = "gs://YOUR_GCS_SOURCE_BUCKET/path_to_your_gcs_table/file.csv";
        ;
        createDatasetTableGcs(project, datasetDisplayName, gcsSourceUri);
      }
    
      static void createDatasetTableGcs(String project, String datasetDisplayName, String gcsSourceUri)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        [DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html) settings =
            [DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html) datasetServiceClient = [DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html).create(settings)) {
          String location = "us-central1";
          String metadataSchemaUri =
              "gs://google-cloud-aiplatform/schema/dataset/metadata/tables_1.0.0.yaml";
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
    
          String jsonString =
              "{\"input_config\": {\"gcs_source\": {\"uri\": [\"" + gcsSourceUri + "\"]}}}";
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder metaData = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
          [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(jsonString, metaData);
    
          [Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset.html) dataset =
              [Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset.html).newBuilder()
                  .setDisplayName(datasetDisplayName)
                  .setMetadataSchemaUri(metadataSchemaUri)
                  .setMetadata(metaData)
                  .build();
    
          OperationFuture<Dataset, CreateDatasetOperationMetadata> datasetFuture =
              datasetServiceClient.[createDatasetAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html#com_google_cloud_aiplatform_v1_DatasetServiceClient_createDatasetAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_LocationName_com_google_cloud_aiplatform_v1_Dataset_)(locationName, dataset);
          System.out.format("Operation name: %s\n", datasetFuture.getInitialFuture().get().getName());
          System.out.println("Waiting for operation to finish...");
          [Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset.html) datasetResponse = datasetFuture.get(300, TimeUnit.SECONDS);
    
          System.out.println("Create Dataset Table GCS sample");
          System.out.format("Name: %s\n", datasetResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset.html#com_google_cloud_aiplatform_v1_Dataset_getName__)());
          System.out.format("Display Name: %s\n", datasetResponse.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset.html#com_google_cloud_aiplatform_v1_Dataset_getDisplayName__)());
          System.out.format("Metadata Schema Uri: %s\n", datasetResponse.[getMetadataSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset.html#com_google_cloud_aiplatform_v1_Dataset_getMetadataSchemaUri__)());
          System.out.format("Metadata: %s\n", datasetResponse.[getMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset.html#com_google_cloud_aiplatform_v1_Dataset_getMetadata__)());
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
    
    // const datasetDisplayName = 'YOUR_DATASET_DISPLAY_NAME';
    // const gcsSourceUri = 'YOUR_GCS_SOURCE_URI';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Dataset Service Client library
    const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const datasetServiceClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function createDatasetTabularGcs() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
      const metadata = {
        structValue: {
          fields: {
            inputConfig: {
              structValue: {
                fields: {
                  gcsSource: {
                    structValue: {
                      fields: {
                        uri: {
                          listValue: {
                            values: [{stringValue: gcsSourceUri}],
                          },
                        },
                      },
                    },
                  },
                },
              },
            },
          },
        },
      };
      // Configure the dataset resource
      const dataset = {
        displayName: datasetDisplayName,
        metadataSchemaUri:
          'gs://google-cloud-aiplatform/schema/dataset/metadata/tabular_1.0.0.yaml',
        metadata: metadata,
      };
      const request = {
        parent,
        dataset,
      };
    
      // Create dataset request
      const [response] = await datasetServiceClient.createDataset(request);
      console.log(`Long running operation : ${response.name}`);
    
      // Wait for operation to complete
      await response.promise();
      const result = response.result;
    
      console.log('Create dataset tabular gcs response');
      console.log(`\tName : ${result.name}`);
      console.log(`\tDisplay name : ${result.displayName}`);
      console.log(`\tMetadata schema uri : ${result.metadataSchemaUri}`);
      console.log(`\tMetadata : ${JSON.stringify(result.metadata)}`);
    }
    createDatasetTabularGcs();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def create_dataset_tabular_gcs_sample(
        project: str,
        display_name: str,
        gcs_uri: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
        timeout: int = 300,
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[DatasetServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.dataset_service.DatasetServiceClient.html)(client_options=client_options)
        metadata_dict = {"input_config": {"gcs_source": {"uri": [gcs_uri]}}}
        metadata = json_format.ParseDict(metadata_dict, Value())
    
        dataset = {
            "display_name": display_name,
            "metadata_schema_uri": "gs://google-cloud-aiplatform/schema/dataset/metadata/tabular_1.0.0.yaml",
            "metadata": metadata,
        }
        parent = f"projects/{project}/locations/{location}"
        response = client.[create_dataset](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.dataset_service.DatasetServiceClient.html#google_cloud_aiplatform_v1_services_dataset_service_DatasetServiceClient_create_dataset)(parent=parent, dataset=dataset)
        print("Long running operation:", response.operation.name)
        create_dataset_response = response.result(timeout=timeout)
        print("create_dataset_response:", create_dataset_response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
