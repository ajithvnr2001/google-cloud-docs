---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-deploy-model-custom-trained-model-sample/
title: Deploy a model for custom trained model \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:40.592292+00:00
---

# Deploy a model for custom trained model  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-deploy-model-custom-trained-model-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Deploy a model for custom trained model Stay organized with collections  Save and categorize content based on your preferences. 

Deploys a model for custom trained model using the deploy_model method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Deploy a model by using the gcloud CLI or Vertex AI API](https://docs.cloud.google.com/vertex-ai/docs/predictions/deploy-model-api)
  * [Get online inferences and explanations](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/e2e-automl-online-predictions)
  * [Get online inferences for AutoML models](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/classification-regression/get-online-predictions)
  * [Get TabNet online inferences](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-online-predictions)
  * [Get Wide & Deep online inferences](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/wide-and-deep-online-predictions)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[DedicatedResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DedicatedResources.html);
    import com.google.cloud.aiplatform.v1.[DeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[DeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse.html);
    import com.google.cloud.aiplatform.v1.[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html);
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html);
    import com.google.cloud.aiplatform.v1.[EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html);
    import com.google.cloud.aiplatform.v1.[ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    
    public class DeployModelCustomTrainedModelSample {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "PROJECT";
        String endpointId = "ENDPOINT_ID";
        String modelName = "MODEL_NAME";
        String deployedModelDisplayName = "DEPLOYED_MODEL_DISPLAY_NAME";
        deployModelCustomTrainedModelSample(project, endpointId, modelName, deployedModelDisplayName);
      }
    
      static void deployModelCustomTrainedModelSample(
          String project, String endpointId, String model, String deployedModelDisplayName)
          throws IOException, ExecutionException, InterruptedException {
        [EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html) settings =
            [EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html) client = [EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html).create(settings)) {
          [MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html) machineSpec = [MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html).newBuilder().[setMachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.Builder.html#com_google_cloud_aiplatform_v1_MachineSpec_Builder_setMachineType_java_lang_String_)("n1-standard-2").build();
          [DedicatedResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DedicatedResources.html) dedicatedResources =
              [DedicatedResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DedicatedResources.html).newBuilder().setMinReplicaCount(1).setMachineSpec(machineSpec).build();
    
          String modelName = [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html).of(project, location, model).toString();
          [DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html) deployedModel =
              [DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html).newBuilder()
                  .setModel(modelName)
                  .setDisplayName(deployedModelDisplayName)
                  // `dedicated_resources` must be used for non-AutoML models
                  .setDedicatedResources(dedicatedResources)
                  .build();
          // key '0' assigns traffic for the newly deployed model
          // Traffic percentage values must add up to 100
          // Leave dictionary empty if endpoint should not accept any traffic
          Map<String, Integer> trafficSplit = new HashMap<>();
          trafficSplit.put("0", 100);
          [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html) endpoint = [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html).of(project, location, endpointId);
          OperationFuture<DeployModelResponse, DeployModelOperationMetadata> response =
              client.[deployModelAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html#com_google_cloud_aiplatform_v1_EndpointServiceClient_deployModelAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_EndpointName_com_google_cloud_aiplatform_v1_DeployedModel_java_util_Map_java_lang_String_java_lang_Integer__)(endpoint, deployedModel, trafficSplit);
    
          // You can use OperationFuture.getInitialFuture to get a future representing the initial
          // response to the request, which contains information while the operation is in progress.
          System.out.format("Operation name: %s\n", response.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
    
          // OperationFuture.get() will block until the operation is finished.
          [DeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse.html) deployModelResponse = response.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.format("deployModelResponse: %s\n", deployModelResponse);
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def deploy_model_custom_trained_model_sample(
        project: str,
        endpoint_id: str,
        model_name: str,
        deployed_model_display_name: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
        timeout: int = 7200,
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[EndpointServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.endpoint_service.EndpointServiceClient.html)(client_options=client_options)
        deployed_model = {
            # format: 'projects/{project}/locations/{location}/models/{model}'
            "model": model_name,
            "display_name": deployed_model_display_name,
            # `dedicated_resources` must be used for non-AutoML models
            "dedicated_resources": {
                "min_replica_count": 1,
                "machine_spec": {
                    "machine_type": "n1-standard-2",
                    # Accelerators can be used only if the model specifies a GPU image.
                    # 'accelerator_type': aiplatform.gapic.AcceleratorType.NVIDIA_TESLA_K80,
                    # 'accelerator_count': 1,
                },
            },
        }
        # key '0' assigns traffic for the newly deployed model
        # Traffic percentage values must add up to 100
        # Leave dictionary empty if endpoint should not accept any traffic
        traffic_split = {"0": 100}
        endpoint = client.[endpoint_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.endpoint_service.EndpointServiceClient.html#google_cloud_aiplatform_v1_services_endpoint_service_EndpointServiceClient_endpoint_path)(
            project=project, location=location, endpoint=endpoint_id
        )
        response = client.[deploy_model](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.endpoint_service.EndpointServiceClient.html#google_cloud_aiplatform_v1_services_endpoint_service_EndpointServiceClient_deploy_model)(
            endpoint=endpoint, deployed_model=deployed_model, traffic_split=traffic_split
        )
        print("Long running operation:", response.operation.name)
        deploy_model_response = response.result(timeout=timeout)
        print("deploy_model_response:", deploy_model_response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
