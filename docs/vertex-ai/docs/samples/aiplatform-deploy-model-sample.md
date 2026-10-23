---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-deploy-model-sample/
title: Deploy a model \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:27:01.356581+00:00
---

# Deploy a model  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-deploy-model-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Deploy a model Stay organized with collections  Save and categorize content based on your preferences. 

Deploys a model using the deploy_model method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get inferences from a image object detection model](https://docs.cloud.google.com/vertex-ai/docs/image-data/object-detection/get-predictions)
  * [Get inferences from an image classification model](https://docs.cloud.google.com/vertex-ai/docs/image-data/classification/get-predictions)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.api.gax.longrunning.[OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.aiplatform.v1.[AutomaticResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AutomaticResources.html);
    import com.google.cloud.aiplatform.v1.[DedicatedResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DedicatedResources.html);
    import com.google.cloud.aiplatform.v1.[DeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[DeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse.html);
    import com.google.cloud.aiplatform.v1.[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html);
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html);
    import com.google.cloud.aiplatform.v1.[EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html);
    import com.google.cloud.aiplatform.v1.[ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html);
    import com.google.cloud.aiplatform.v1.stub.EndpointServiceStubSettings;
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import org.threeten.bp.Duration;
    
    public class DeployModelSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String deployedModelDisplayName = "YOUR_DEPLOYED_MODEL_DISPLAY_NAME";
        String endpointId = "YOUR_ENDPOINT_NAME";
        String modelId = "YOUR_MODEL_ID";
        int timeout = 900;
        deployModelSample(project, deployedModelDisplayName, endpointId, modelId, timeout);
      }
    
      static void deployModelSample(
          String project,
          String deployedModelDisplayName,
          String endpointId,
          String modelId,
          int timeout)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
    
        // Set long-running operations (LROs) timeout
        final [OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html) operationTimedPollAlgorithm =
            [OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html).create(
                [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                    .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(5000L))
                    .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(1.5)
                    .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(45000L))
                    .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(Duration.ZERO)
                    .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(1.0)
                    .[setMaxRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRpcTimeout_org_threeten_bp_Duration_)(Duration.ZERO)
                    .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.ofSeconds(timeout))
                    .build());
    
        EndpointServiceStubSettings.Builder endpointServiceStubSettingsBuilder =
            EndpointServiceStubSettings.newBuilder();
        endpointServiceStubSettingsBuilder
            .deployModelOperationSettings()
            .setPollingAlgorithm(operationTimedPollAlgorithm);
        EndpointServiceStubSettings endpointStubSettings = endpointServiceStubSettingsBuilder.build();
        [EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html) endpointServiceSettings =
            [EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html).create(endpointStubSettings);
        endpointServiceSettings =
            endpointServiceSettings.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html#com_google_cloud_aiplatform_v1_EndpointServiceSettings_toBuilder__)()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html) endpointServiceClient =
            [EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html).create(endpointServiceSettings)) {
          String location = "us-central1";
          [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html) endpointName = [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html).of(project, location, endpointId);
          // key '0' assigns traffic for the newly deployed model
          // Traffic percentage values must add up to 100
          // Leave dictionary empty if endpoint should not accept any traffic
          Map<String, Integer> trafficSplit = new HashMap<>();
          trafficSplit.put("0", 100);
          [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html) modelName = [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html).of(project, location, modelId);
          [AutomaticResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AutomaticResources.html) automaticResourcesInput =
              [AutomaticResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AutomaticResources.html).newBuilder().setMinReplicaCount(1).setMaxReplicaCount(1).build();
          [DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html) deployedModelInput =
              [DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html).newBuilder()
                  .setModel(modelName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html#com_google_cloud_aiplatform_v1_ModelName_toString__)())
                  .setDisplayName(deployedModelDisplayName)
                  .setAutomaticResources(automaticResourcesInput)
                  .build();
    
          OperationFuture<DeployModelResponse, DeployModelOperationMetadata> deployModelResponseFuture =
              endpointServiceClient.[deployModelAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html#com_google_cloud_aiplatform_v1_EndpointServiceClient_deployModelAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_EndpointName_com_google_cloud_aiplatform_v1_DeployedModel_java_util_Map_java_lang_String_java_lang_Integer__)(endpointName, deployedModelInput, trafficSplit);
          System.out.format(
              "Operation name: %s\n", deployModelResponseFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [DeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse.html) deployModelResponse = deployModelResponseFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(20, TimeUnit.MINUTES);
    
          System.out.println("Deploy Model Response");
          [DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html) deployedModel = deployModelResponse.[getDeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse.html#com_google_cloud_aiplatform_v1_DeployModelResponse_getDeployedModel__)();
          System.out.println("\tDeployed Model");
          System.out.format("\t\tid: %s\n", deployedModel.[getId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html#com_google_cloud_aiplatform_v1_DeployedModel_getId__)());
          System.out.format("\t\tmodel: %s\n", deployedModel.[getModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html#com_google_cloud_aiplatform_v1_DeployedModel_getModel__)());
          System.out.format("\t\tDisplay Name: %s\n", deployedModel.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html#com_google_cloud_aiplatform_v1_DeployedModel_getDisplayName__)());
          System.out.format("\t\tCreate Time: %s\n", deployedModel.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html#com_google_cloud_aiplatform_v1_DeployedModel_getCreateTime__)());
    
          [DedicatedResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DedicatedResources.html) dedicatedResources = deployedModel.[getDedicatedResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html#com_google_cloud_aiplatform_v1_DeployedModel_getDedicatedResources__)();
          System.out.println("\t\tDedicated Resources");
          System.out.format("\t\t\tMin Replica Count: %s\n", dedicatedResources.[getMinReplicaCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DedicatedResources.html#com_google_cloud_aiplatform_v1_DedicatedResources_getMinReplicaCount__)());
    
          [MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html) machineSpec = dedicatedResources.[getMachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DedicatedResources.html#com_google_cloud_aiplatform_v1_DedicatedResources_getMachineSpec__)();
          System.out.println("\t\t\tMachine Spec");
          System.out.format("\t\t\t\tMachine Type: %s\n", machineSpec.[getMachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html#com_google_cloud_aiplatform_v1_MachineSpec_getMachineType__)());
          System.out.format("\t\t\t\tAccelerator Type: %s\n", machineSpec.[getAcceleratorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html#com_google_cloud_aiplatform_v1_MachineSpec_getAcceleratorType__)());
          System.out.format("\t\t\t\tAccelerator Count: %s\n", machineSpec.[getAcceleratorCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html#com_google_cloud_aiplatform_v1_MachineSpec_getAcceleratorCount__)());
    
          [AutomaticResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AutomaticResources.html) automaticResources = deployedModel.[getAutomaticResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.html#com_google_cloud_aiplatform_v1_DeployedModel_getAutomaticResources__)();
          System.out.println("\t\tAutomatic Resources");
          System.out.format("\t\t\tMin Replica Count: %s\n", automaticResources.[getMinReplicaCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AutomaticResources.html#com_google_cloud_aiplatform_v1_AutomaticResources_getMinReplicaCount__)());
          System.out.format("\t\t\tMax Replica Count: %s\n", automaticResources.[getMaxReplicaCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AutomaticResources.html#com_google_cloud_aiplatform_v1_AutomaticResources_getMaxReplicaCount__)());
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
    
    // const modelId = "YOUR_MODEL_ID";
    // const endpointId = 'YOUR_ENDPOINT_ID';
    // const deployedModelDisplayName = 'YOUR_DEPLOYED_MODEL_DISPLAY_NAME';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    const modelName = `projects/${project}/locations/${location}/models/${modelId}`;
    const endpoint = `projects/${project}/locations/${location}/endpoints/${endpointId}`;
    // Imports the Google Cloud Endpoint Service Client library
    const {EndpointServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint:
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const endpointServiceClient = new [EndpointServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function deployModel() {
      // Configure the parent resource
      // key '0' assigns traffic for the newly deployed model
      // Traffic percentage values must add up to 100
      // Leave dictionary empty if endpoint should not accept any traffic
      const trafficSplit = {0: 100};
      const deployedModel = {
        // format: 'projects/{project}/locations/{location}/models/{model}'
        model: modelName,
        displayName: deployedModelDisplayName,
        automaticResources: {minReplicaCount: 1, maxReplicaCount: 1},
      };
      const request = {
        endpoint,
        deployedModel,
        trafficSplit,
      };
    
      // Get and print out a list of all the endpoints for this resource
      const [response] = await endpointServiceClient.deployModel(request);
      console.log(`Long running operation : ${response.name}`);
    
      // Wait for operation to complete
      await response.promise();
      const result = response.result;
    
      console.log('Deploy model response');
      const modelDeployed = result.deployedModel;
      console.log('\tDeployed model');
      if (!modelDeployed) {
        console.log('\t\tId : {}');
        console.log('\t\tModel : {}');
        console.log('\t\tDisplay name : {}');
        console.log('\t\tCreate time : {}');
    
        console.log('\t\tDedicated resources');
        console.log('\t\t\tMin replica count : {}');
        console.log('\t\t\tMachine spec {}');
        console.log('\t\t\t\tMachine type : {}');
        console.log('\t\t\t\tAccelerator type : {}');
        console.log('\t\t\t\tAccelerator count : {}');
    
        console.log('\t\tAutomatic resources');
        console.log('\t\t\tMin replica count : {}');
        console.log('\t\t\tMax replica count : {}');
      } else {
        console.log(`\t\tId : ${modelDeployed.id}`);
        console.log(`\t\tModel : ${modelDeployed.model}`);
        console.log(`\t\tDisplay name : ${modelDeployed.displayName}`);
        console.log(`\t\tCreate time : ${modelDeployed.createTime}`);
    
        const dedicatedResources = modelDeployed.dedicatedResources;
        console.log('\t\tDedicated resources');
        if (!dedicatedResources) {
          console.log('\t\t\tMin replica count : {}');
          console.log('\t\t\tMachine spec {}');
          console.log('\t\t\t\tMachine type : {}');
          console.log('\t\t\t\tAccelerator type : {}');
          console.log('\t\t\t\tAccelerator count : {}');
        } else {
          console.log(
            `\t\t\tMin replica count : \
              ${dedicatedResources.minReplicaCount}`
          );
          const machineSpec = dedicatedResources.machineSpec;
          console.log('\t\t\tMachine spec');
          console.log(`\t\t\t\tMachine type : ${machineSpec.machineType}`);
          console.log(
            `\t\t\t\tAccelerator type : ${machineSpec.acceleratorType}`
          );
          console.log(
            `\t\t\t\tAccelerator count : ${machineSpec.acceleratorCount}`
          );
        }
    
        const automaticResources = modelDeployed.automaticResources;
        console.log('\t\tAutomatic resources');
        if (!automaticResources) {
          console.log('\t\t\tMin replica count : {}');
          console.log('\t\t\tMax replica count : {}');
        } else {
          console.log(
            `\t\t\tMin replica count : \
              ${automaticResources.minReplicaCount}`
          );
          console.log(
            `\t\t\tMax replica count : \
              ${automaticResources.maxReplicaCount}`
          );
        }
      }
    }
    deployModel();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def deploy_model_sample(
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
            # AutoML Vision models require `automatic_resources` field
            # Other model types may require `dedicated_resources` field instead
            "automatic_resources": {"min_replica_count": 1, "max_replica_count": 1},
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
