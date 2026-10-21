---
url: https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-online-predictions/
title: Get TabNet online inferences \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:31:23.613163+00:00
---

# Get TabNet online inferences  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-online-predictions/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Get TabNet online inferences Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to get online (real-time) inferences and explanations from your tabular classification or regression models using the Google Cloud console or the Vertex AI API. 

An online inference is a synchronous request as opposed to a [batch inference](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-batch-predictions), which is an asynchronous request. Use online inferences when you are making requests in response to application input or in other situations where you require timely inference.

You must deploy a model to an endpoint before that model can be used to serve online inferences. Deploying a model associates physical resources with the model so it can serve online inferences with low latency.

The topics covered are:

  1. Deploy a model to an endpoint
  2. Get an online inference using your deployed model



## Before you begin

Before you can get online inferences, you must first [train](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-train) a model.

## Deploy a model to an endpoint

You can deploy more than one model to an endpoint, and you can deploy a model to more than one endpoint. For more information about options and use cases for deploying models, see [About deploying models](https://docs.cloud.google.com/vertex-ai/docs/general/deployment).

Use one of the following methods to deploy a model:

###  Google Cloud console 

  1. In the Google Cloud console, in the Vertex AI section, go to the **Models** page.

[Go to the Models page](https://console.cloud.google.com/vertex-ai/models)

  2. Click the name of the model you want to deploy to open its details page.

  3. Select the **Deploy & Test** tab.

If your model is already deployed to any endpoints, they are listed in the **Deploy your model** section.

  4. Click **Deploy to endpoint**.

  5. In the **Define your endpoint** page, configure as follows:

     1. You can choose to deploy your model to a new endpoint or an existing endpoint.

        * To deploy your model to a new endpoint, select radio_button_checked**Create new endpoint** and provide a name for the new endpoint.
        * To deploy your model to an existing endpoint, select radio_button_checked**Add to existing endpoint** and select the endpoint from the drop-down list.
        * You can add more than one model to an endpoint, and you can add a model to more than one endpoint. [Learn more](https://docs.cloud.google.com/vertex-ai/docs/general/deployment).
     2. Click **Continue**.

  6. In the **Model settings** page, configure as follows:

     1. If you're deploying your model to a new endpoint, accept 100 for the **Traffic split**. If you're deploying your model to an existing endpoint that has one or more models deployed to it, you must update the **Traffic split** percentage for the model you are deploying and the already deployed models so that all of the percentages add up to 100%.

     2. Enter the **Minimum number of compute nodes** you want to provide for your model. 

This is the number of nodes available to this model at all times. You are charged for the nodes used, whether to handle inference load or for standby (minimum) nodes, even without inference traffic. See the [pricing page](https://docs.cloud.google.com/vertex-ai/pricing). 

     3. Select your **Machine type**.

Larger machine resources will increase your inference performance and increase costs. 

     4. Learn how to [change the default settings for inference logging](https://docs.cloud.google.com/vertex-ai/docs/predictions/online-prediction-logging#enabling-and-disabling). 

     5. Click **Continue**

  7. In the **Model monitoring** page, click **Continue**.

  8. In the **Monitoring objectives** page, configure as follows:

     1. Enter the location of your training data.
     2. Enter the name of the target column.
  9. Click **Deploy** to deploy your model to the endpoint. 




###  API 

When you deploy a model using the Vertex AI API, you complete the following steps:

  1. Create an endpoint if needed.
  2. Get the endpoint ID.
  3. Deploy the model to the endpoint.



### Create an endpoint

If you are deploying a model to an existing endpoint, you can skip this step.

### gcloud

The following example uses the [`gcloud ai endpoints create` command](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/create):
    
    
      gcloud ai endpoints create \
        --region=LOCATION \
        --display-name=ENDPOINT_NAME
    

Replace the following:

  * LOCATION_ID: The region where you are using Vertex AI. 
  * ENDPOINT_NAME: The display name for the endpoint. 

The Google Cloud CLI tool might take a few seconds to create the endpoint.




### REST

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Your region.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * ENDPOINT_NAME: The display name for the endpoint. 



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints

Request JSON body: 
    
    
    {
      "display_name": "ENDPOINT_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/endpoints/ENDPOINT_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.CreateEndpointOperationMetadata",
        "genericMetadata": {
          "createTime": "2020-11-05T17:45:42.812656Z",
          "updateTime": "2020-11-05T17:45:42.812656Z"
        }
      }
    }
    

You can poll for the status of the operation until the response includes `"done": true`. 

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[CreateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html);
    import com.google.cloud.aiplatform.v1.[EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html);
    import com.google.cloud.aiplatform.v1.[EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateEndpointSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String endpointDisplayName = "YOUR_ENDPOINT_DISPLAY_NAME";
        createEndpointSample(project, endpointDisplayName);
      }
    
      static void createEndpointSample(String project, String endpointDisplayName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        [EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html) endpointServiceSettings =
            [EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html) endpointServiceClient =
            [EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html).create(endpointServiceSettings)) {
          String location = "us-central1";
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
          [Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html) endpoint = [Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html).newBuilder().setDisplayName(endpointDisplayName).build();
    
          OperationFuture<Endpoint, CreateEndpointOperationMetadata> endpointFuture =
              endpointServiceClient.[createEndpointAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.html#com_google_cloud_aiplatform_v1_EndpointServiceClient_createEndpointAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_LocationName_com_google_cloud_aiplatform_v1_Endpoint_)(locationName, endpoint);
          System.out.format("Operation name: %s\n", endpointFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html) endpointResponse = endpointFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(300, TimeUnit.SECONDS);
    
          System.out.println("Create Endpoint Response");
          System.out.format("Name: %s\n", endpointResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html#com_google_cloud_aiplatform_v1_Endpoint_getName__)());
          System.out.format("Display Name: %s\n", endpointResponse.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html#com_google_cloud_aiplatform_v1_Endpoint_getDisplayName__)());
          System.out.format("Description: %s\n", endpointResponse.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html#com_google_cloud_aiplatform_v1_Endpoint_getDescription__)());
          System.out.format("Labels: %s\n", endpointResponse.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html#com_google_cloud_aiplatform_v1_Endpoint_getLabelsMap__)());
          System.out.format("Create Time: %s\n", endpointResponse.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html#com_google_cloud_aiplatform_v1_Endpoint_getCreateTime__)());
          System.out.format("Update Time: %s\n", endpointResponse.[getUpdateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.html#com_google_cloud_aiplatform_v1_Endpoint_getUpdateTime__)());
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
    
    // const endpointDisplayName = 'YOUR_ENDPOINT_DISPLAY_NAME';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Endpoint Service Client library
    const {EndpointServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const endpointServiceClient = new [EndpointServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function createEndpoint() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
      const endpoint = {
        displayName: endpointDisplayName,
      };
      const request = {
        parent,
        endpoint,
      };
    
      // Get and print out a list of all the endpoints for this resource
      const [response] = await endpointServiceClient.createEndpoint(request);
      console.log(`Long running operation : ${response.name}`);
    
      // Wait for operation to complete
      await response.promise();
      const result = response.result;
    
      console.log('Create endpoint response');
      console.log(`\tName : ${result.name}`);
      console.log(`\tDisplay name : ${result.displayName}`);
      console.log(`\tDescription : ${result.description}`);
      console.log(`\tLabels : ${JSON.stringify(result.labels)}`);
      console.log(`\tCreate time : ${JSON.stringify(result.createTime)}`);
      console.log(`\tUpdate time : ${JSON.stringify(result.updateTime)}`);
    }
    createEndpoint();

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    def create_endpoint_sample(
        project: str,
        display_name: str,
        location: str,
    ):
        aiplatform.init(project=project, location=location)
    
        endpoint = aiplatform.Endpoint.create(
            display_name=display_name,
            project=project,
            location=location,
        )
    
        print(endpoint.display_name)
        print(endpoint.resource_name)
        return endpoint
    
    

### Retrieve the endpoint ID

You need the endpoint ID to deploy the model.

### gcloud

The following example uses the [`gcloud ai endpoints list` command](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/list):
    
    
      gcloud ai endpoints list \
        --region=LOCATION \
        --filter=display_name=ENDPOINT_NAME
    

Replace the following:

  * LOCATION_ID: The region where you are using Vertex AI. 
  * ENDPOINT_NAME: The display name for the endpoint. 

Note the number that appears in the `ENDPOINT_ID` column. Use this ID in the following step.




### REST

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: The region where you are using Vertex AI. 
  * PROJECT_ID: .
  * ENDPOINT_NAME: The display name for the endpoint. 



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints?filter=display_name=ENDPOINT_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints?filter=display_name=ENDPOINT_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints?filter=display_name=ENDPOINT_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "endpoints": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/endpoints/ENDPOINT_ID",
          "displayName": "ENDPOINT_NAME",
          "etag": "AMEw9yPz5pf4PwBHbRWOGh0PcAxUdjbdX2Jm3QO_amguy3DbZGP5Oi_YUKRywIE-BtLx",
          "createTime": "2020-04-17T18:31:11.585169Z",
          "updateTime": "2020-04-17T18:35:08.568959Z"
        }
      ]
    }
    

Note the ENDPOINT_ID. 

### Deploy the model

Select the tab below for your language or environment:

### gcloud

The following examples use the [`gcloud ai endpoints deploy-model` command](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/deploy-model).

The following example deploys a `Model` to an `Endpoint` without using GPUs to accelerate prediction serving and without splitting traffic between multiple `DeployedModel` resources:

Before using any of the command data below, make the following replacements: 

  * ENDPOINT_ID: The ID for the endpoint. 
  * LOCATION_ID: The region where you are using Vertex AI. 
  * MODEL_ID: The ID for the model to be deployed. 
  * DEPLOYED_MODEL_NAME: A name for the `DeployedModel`. You can use the display name of the `Model` for the `DeployedModel` as well. 
  * MACHINE_TYPE: Optional. The machine resources used for each node of this deployment. Its default setting is `n1-standard-2`. [Learn more about machine types.](https://docs.cloud.google.com/vertex-ai/docs/predictions/configure-compute)
  * MIN_REPLICA_COUNT: The minimum number of nodes for this deployment. The node count can be increased or decreased as required by the inference load, up to the maximum number of nodes and never fewer than this number of nodes. This value must be greater than or equal to 1. If the `--min-replica-count` flag is omitted, the value defaults to 1. 
  * MAX_REPLICA_COUNT: The maximum number of nodes for this deployment. The node count can be increased or decreased as required by the inference load, up to this number of nodes and never fewer than the minimum number of nodes. If you omit the `--max-replica-count` flag, then maximum number of nodes is set to the value of `--min-replica-count`.



Execute the [gcloud ai endpoints deploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/deploy-model) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud ai endpoints deploy-model ENDPOINT_ID\
      --region=LOCATION_ID \
      --model=MODEL_ID \
      --display-name=DEPLOYED_MODEL_NAME \
      --machine-type=MACHINE_TYPE \
      --min-replica-count=MIN_REPLICA_COUNT \
      --max-replica-count=MAX_REPLICA_COUNT \
      --traffic-split=0=100

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud ai endpoints deploy-model ENDPOINT_ID`
      --region=LOCATION_ID `
      --model=MODEL_ID `
      --display-name=DEPLOYED_MODEL_NAME `
      --machine-type=MACHINE_TYPE `
      --min-replica-count=MIN_REPLICA_COUNT `
      --max-replica-count=MAX_REPLICA_COUNT `
      --traffic-split=0=100

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud ai endpoints deploy-model ENDPOINT_ID^
      --region=LOCATION_ID ^
      --model=MODEL_ID ^
      --display-name=DEPLOYED_MODEL_NAME ^
      --machine-type=MACHINE_TYPE ^
      --min-replica-count=MIN_REPLICA_COUNT ^
      --max-replica-count=MAX_REPLICA_COUNT ^
      --traffic-split=0=100

#### Splitting traffic

The `--traffic-split=0=100` flag in the preceding examples sends 100% of prediction traffic that the `Endpoint` receives to the new `DeployedModel`, which is represented by the temporary ID `0`. If your `Endpoint` already has other `DeployedModel` resources, then you can split traffic between the new `DeployedModel` and the old ones. For example, to send 20% of traffic to the new `DeployedModel` and 80% to an older one, run the following command. 

Before using any of the command data below, make the following replacements: 

  * OLD_DEPLOYED_MODEL_ID: the ID of the existing `DeployedModel`.



Execute the [gcloud ai endpoints deploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/deploy-model) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud ai endpoints deploy-model ENDPOINT_ID\
      --region=LOCATION_ID \
      --model=MODEL_ID \
      --display-name=DEPLOYED_MODEL_NAME \ 
      --machine-type=MACHINE_TYPE \
      --min-replica-count=MIN_REPLICA_COUNT \
      --max-replica-count=MAX_REPLICA_COUNT \
      **--traffic-split =0=20,OLD_DEPLOYED_MODEL_ID=80**

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud ai endpoints deploy-model ENDPOINT_ID`
      --region=LOCATION_ID `
      --model=MODEL_ID `
      --display-name=DEPLOYED_MODEL_NAME \ 
      --machine-type=MACHINE_TYPE `
      --min-replica-count=MIN_REPLICA_COUNT `
      --max-replica-count=MAX_REPLICA_COUNT `
      **--traffic-split =0=20,OLD_DEPLOYED_MODEL_ID=80**

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud ai endpoints deploy-model ENDPOINT_ID^
      --region=LOCATION_ID ^
      --model=MODEL_ID ^
      --display-name=DEPLOYED_MODEL_NAME \ 
      --machine-type=MACHINE_TYPE ^
      --min-replica-count=MIN_REPLICA_COUNT ^
      --max-replica-count=MAX_REPLICA_COUNT ^
      **--traffic-split =0=20,OLD_DEPLOYED_MODEL_ID=80**

### REST

You use the [endpoints.predict](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/predict) method to request an online inference. 

Deploy the model.

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: The region where you are using Vertex AI. 
  * PROJECT_ID: .
  * ENDPOINT_ID: The ID for the endpoint. 
  * MODEL_ID: The ID for the model to be deployed. 
  * DEPLOYED_MODEL_NAME: A name for the `DeployedModel`. You can use the display name of the `Model` for the `DeployedModel` as well. 
  * MACHINE_TYPE: Optional. The machine resources used for each node of this deployment. Its default setting is `n1-standard-2`. [Learn more about machine types.](https://docs.cloud.google.com/vertex-ai/docs/predictions/configure-compute)
  * ACCELERATOR_TYPE: The type of accelerator to be attached to the machine. Optional if ACCELERATOR_COUNT is not specified or is zero. Not recommended for AutoML models or custom-trained models that are using non-GPU images. [Learn more](https://docs.cloud.google.com/vertex-ai/docs/predictions/configure-compute#gpus). 
  * ACCELERATOR_COUNT: The number of accelerators for each replica to use. Optional. Should be zero or unspecified for AutoML models or custom-trained models that are using non-GPU images. 
  * MIN_REPLICA_COUNT: The minimum number of nodes for this deployment. The node count can be increased or decreased as required by the inference load, up to the maximum number of nodes and never fewer than this number of nodes. This value must be greater than or equal to 1.
  * MAX_REPLICA_COUNT: The maximum number of nodes for this deployment. The node count can be increased or decreased as required by the inference load, up to this number of nodes and never fewer than the minimum number of nodes. 
  * REQUIRED_REPLICA_COUNT: Optional. The required number of nodes for this deployment to be marked as successful. Must be greater than or equal to 1 and fewer than or equal to the minimum number of nodes. If not specified, the default value is the minimum number of nodes. 
  * TRAFFIC_SPLIT_THIS_MODEL: The percentage of the prediction traffic to this endpoint to be routed to the model being deployed with this operation. Defaults to 100. All traffic percentages must add up to 100. [Learn more about traffic splits](https://docs.cloud.google.com/vertex-ai/docs/general/deployment#models-endpoint). 
  * DEPLOYED_MODEL_ID_N: Optional. If other models are deployed to this endpoint, you must update their traffic split percentages so that all percentages add up to 100. 
  * TRAFFIC_SPLIT_MODEL_N: The traffic split percentage value for the deployed model id key. 
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:deployModel

Request JSON body: 
    
    
    {
      "deployedModel": {
        "model": "projects/PROJECT/locations/us-central1/models/MODEL_ID",
        "displayName": "DEPLOYED_MODEL_NAME",
        "dedicatedResources": {
           "machineSpec": {
             "machineType": "MACHINE_TYPE",
             "acceleratorType": "ACCELERATOR_TYPE",
             "acceleratorCount": "ACCELERATOR_COUNT"
           },
           "minReplicaCount": MIN_REPLICA_COUNT,
           "maxReplicaCount": MAX_REPLICA_COUNT,
           "requiredReplicaCount": REQUIRED_REPLICA_COUNT
         },
      },
      "trafficSplit": {
        "0": TRAFFIC_SPLIT_THIS_MODEL,
        "DEPLOYED_MODEL_ID_1": TRAFFIC_SPLIT_MODEL_1,
        "DEPLOYED_MODEL_ID_2": TRAFFIC_SPLIT_MODEL_2
      },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:deployModel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:deployModel" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/endpoints/ENDPOINT_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.DeployModelOperationMetadata",
        "genericMetadata": {
          "createTime": "2020-10-19T17:53:16.502088Z",
          "updateTime": "2020-10-19T17:53:16.502088Z"
        }
      }
    }
    

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

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    def deploy_model_with_dedicated_resources_sample(
        project,
        location,
        model_name: str,
        machine_type: str,
        endpoint: Optional[aiplatform.Endpoint] = None,
        deployed_model_display_name: Optional[str] = None,
        traffic_percentage: Optional[int] = 0,
        traffic_split: Optional[Dict[str, int]] = None,
        min_replica_count: int = 1,
        max_replica_count: int = 1,
        accelerator_type: Optional[str] = None,
        accelerator_count: Optional[int] = None,
        explanation_metadata: Optional[explain.ExplanationMetadata] = None,
        explanation_parameters: Optional[explain.ExplanationParameters] = None,
        metadata: Optional[Sequence[Tuple[str, str]]] = (),
        sync: bool = True,
    ):
        """
        model_name: A fully-qualified model resource name or model ID.
              Example: "projects/123/locations/us-central1/models/456" or
              "456" when project and location are initialized or passed.
        """
    
        aiplatform.init(project=project, location=location)
    
        model = aiplatform.Model(model_name=model_name)
    
        # The explanation_metadata and explanation_parameters should only be
        # provided for a custom trained model and not an AutoML model.
        model.deploy(
            endpoint=endpoint,
            deployed_model_display_name=deployed_model_display_name,
            traffic_percentage=traffic_percentage,
            traffic_split=traffic_split,
            machine_type=machine_type,
            min_replica_count=min_replica_count,
            max_replica_count=max_replica_count,
            accelerator_type=accelerator_type,
            accelerator_count=accelerator_count,
            explanation_metadata=explanation_metadata,
            explanation_parameters=explanation_parameters,
            metadata=metadata,
            sync=sync,
        )
    
        model.wait()
    
        print(model.display_name)
        print(model.resource_name)
        return model
    
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const automl = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)');
    const client = new automl.v1beta1.[AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
    /**
     * Demonstrates using the AutoML client to create a model.
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = '[PROJECT_ID]' e.g., "my-gcloud-project";
    // const computeRegion = '[REGION_NAME]' e.g., "us-central1";
    // const datasetId = '[DATASET_ID]' e.g., "TBL2246891593778855936";
    // const tableId = '[TABLE_ID]' e.g., "1991013247762825216";
    // const columnId = '[COLUMN_ID]' e.g., "773141392279994368";
    // const modelName = '[MODEL_NAME]' e.g., "testModel";
    // const trainBudget = '[TRAIN_BUDGET]' e.g., "1000",
    // `Train budget in milli node hours`;
    
    // A resource that represents Google Cloud Platform location.
    const projectLocation = client.locationPath(projectId, computeRegion);
    
    // Get the full path of the column.
    const columnSpecId = client.columnSpecPath(
      projectId,
      computeRegion,
      datasetId,
      tableId,
      columnId
    );
    
    // Set target column to train the model.
    const targetColumnSpec = {name: columnSpecId};
    
    // Set tables model metadata.
    const tablesModelMetadata = {
      targetColumnSpec: targetColumnSpec,
      trainBudgetMilliNodeHours: trainBudget,
    };
    
    // Set datasetId, model name and model metadata for the dataset.
    const myModel = {
      datasetId: datasetId,
      displayName: modelName,
      tablesModelMetadata: tablesModelMetadata,
    };
    
    // Create a model with the model metadata in the region.
    client
      .createModel({parent: projectLocation, model: myModel})
      .then(responses => {
        const initialApiResponse = responses[1];
        console.log(`Training operation name: ${initialApiResponse.name}`);
        console.log('Training started...');
      })
      .catch(err => {
        console.error(err);
      });

Learn how to [change the default settings for inference logging](https://docs.cloud.google.com/vertex-ai/docs/predictions/online-prediction-logging#enabling-and-disabling). 

### Get operation status

Some requests start long-running operations that require time to complete. These requests return an operation name, which you can use to view the operation's status or cancel the operation. Vertex AI provides helper methods to make calls against long-running operations. For more information, see [Working with long-running operations](https://docs.cloud.google.com/vertex-ai/docs/general/long-running-operations). 

## Get an online inference using your deployed model

To make an online inference, submit one or more test items to a model for analysis, and the model returns results that are based on your model's objective. Use the Google Cloud console or the Vertex AI API to request an online inference.

###  Google Cloud console 

  1. In the Google Cloud console, in the Vertex AI section, go to the **Models** page.

[Go to the Models page](https://console.cloud.google.com/vertex-ai/models)

  2. From the list of models, click the name of the model to request inferences from.

  3. Select the **Deploy & test** tab.

  4. Under the **Test your model** section, add test items to request an inference. The baseline inference data is filled in for you, or you can enter your own inference data and click **Predict**.

After the inference is complete, Vertex AI returns the results in the console.




###  API: Classification 

### gcloud

  1. Create a file named `request.json` with the following contents: 
         
         {
           "instances": [
             {
               PREDICTION_DATA_ROW
             }
           ]
         }
             

Replace the following: 

     * PREDICTION_DATA_ROW: A JSON object with keys as the feature names and values as the corresponding feature values. For example, for a dataset with a number, an array of strings, and a category, the row of data might look like the following example request:
           
           "length":3.6,
           "material":"cotton",
           "tag_array": ["abc","def"]
           

A value must be provided for every feature included in training. The format of the data used for prediction must match the format used for training. Refer to [Data format for predictions](https://docs.cloud.google.com/vertex-ai/docs/datasets/data-types-tabular#format-for-prediction) for details. 

  2. Run the following command:
         
         gcloud ai endpoints predict ENDPOINT_ID \
           --region=LOCATION_ID \
           --json-request=request.json

Replace the following:

     * ENDPOINT_ID: The ID for the endpoint. 
     * LOCATION_ID: The region where you are using Vertex AI. 



### REST

You use the [endpoints.predict](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/predict) method to request an online inference. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where Endpoint is located. For example, `us-central1`. 
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * ENDPOINT_ID: The ID for the endpoint.
  * PREDICTION_DATA_ROW: A JSON object with keys as the feature names and values as the corresponding feature values. For example, for a dataset with a number, an array of strings, and a category, the row of data might look like the following example request:
        
        "length":3.6,
        "material":"cotton",
        "tag_array": ["abc","def"]
        

A value must be provided for every feature included in training. The format of the data used for prediction must match the format used for training. Refer to [Data format for predictions](https://docs.cloud.google.com/vertex-ai/docs/datasets/data-types-tabular#format-for-prediction) for details. 

  * DEPLOYED_MODEL_ID: Output by the `predict` method. The ID of the model used to generate the inference. 



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          PREDICTION_DATA_ROW
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:predict"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:predict" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
       {
         "predictions": [
          {
             "scores": [
               0.96771615743637085,
               0.032283786684274673
             ],
             "classes": [
               "0",
               "1"
             ]
          }
         ]
         "deployedModelId": "2429510197"
       }
       

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.util.[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html);
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html);
    import com.google.cloud.aiplatform.v1.schema.predict.prediction.[TabularClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularClassificationPredictionResult.html);
    import com.google.protobuf.[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.List;
    
    public class PredictTabularClassificationSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String instance = "[{ “feature_column_a”: “value”, “feature_column_b”: “value”}]";
        String endpointId = "YOUR_ENDPOINT_ID";
        predictTabularClassification(instance, project, endpointId);
      }
    
      static void predictTabularClassification(String instance, String project, String endpointId)
          throws IOException {
        PredictionServic[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html)ceSettings =
            PredictionServic[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html)          .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (PredictionServic[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html)ceClient =
            PredictionServic[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html)onServiceSettings)) {
          String location = "us-central1";
          EndpointName end[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html)EndpointName.of([EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html)ation, endpointId);
    
          ListValue.Builde[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)ue = ListValue.newBui[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)     JsonFormat.parse[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html)instance, listValue);
          List<Value> instan[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)listValue.getValuesList();
    
          Value parameters[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)lue.newBuilder[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)tListValue(listValue).build();
          PredictResponse [PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html) =
              predictionServiceClient.predict(endpointName, instanceList, parameters);
          System.out.println("Predict Tabular Classification Response");
          System.out.format("\tDeployed Model Id: %s\n", predictResponse.predictResponse.[getDeployedModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getDeployedModelId__)().out.println("Predictions");
          for (Value prediction[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)edictResponse.predictResponse.[getPredictionsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getPredictionsList__)()larClassific[TabularClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularClassificationPredictionResult.html)uilder =
                TabularClassific[TabularClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularClassificationPredictionResult.html)       TabularClassific[TabularClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularClassificationPredictionResult.html)      (TabularClassific[TabularClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularClassificationPredictionResult.html)  ValueConverter.f[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html)tBuilder, prediction);
    
            for (int i = 0; i < result.getClasseresult.[getClassesCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularClassificationPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularClassificationPredictionResult_getClassesCount__)()   System.out.printf("\tClass: %s", result.getClasseresult.[getClasses](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularClassificationPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularClassificationPredictionResult_getClasses_int_)(i)tem.out.printf("\tScore: %f", result.getScoresresult.[getScores](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularClassificationPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularClassificationPredictionResult_getScores_int_)(i)   }
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
    
    // const endpointId = 'YOUR_ENDPOINT_ID';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    const aiplatform = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    const {prediction} =
      aiplatform.protos.google.cloud.aiplatform.v1.schema.predict;
    
    // Imports the Google Cloud Prediction service client
    const {PredictionServiceClient} = aiplatform.v1;
    
    // Import the helper module for converting arbitrary protobuf.Value objects.
    const {helpers} = aiplatform;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const predictionServiceClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function predictTablesClassification() {
      // Configure the endpoint resource
      const endpoint = `projects/${project}/locations/${location}/endpoints/${endpointId}`;
      const parameters = [helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue({});
    
      const instance = [helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue({
        petal_length: '1.4',
        petal_width: '1.3',
        sepal_length: '5.1',
        sepal_width: '2.8',
      });
    
      const instances = [instance];
      const request = {
        endpoint,
        instances,
        parameters,
      };
    
      // Predict request
      const [response] = await predictionServiceClient.predict(request);
    
      console.log('Predict tabular classification response');
      console.log(`\tDeployed model id : ${response.deployedModelId}\n`);
      const predictions = response.predictions;
      console.log('Predictions :');
      for (const predictionResultVal of predictions) {
        const predictionResultObj =
          prediction.TabularClassificationPredictionResult.fromValue(
            predictionResultVal
          );
        for (const [i, class_] of predictionResultObj.classes.entries()) {
          console.log(`\tClass: ${class_}`);
          console.log(`\tScore: ${predictionResultObj.scores[i]}\n\n`);
        }
      }
    }
    predictTablesClassification();

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    def predict_tabular_classification_sample(
        project: str,
        location: str,
        endpoint_name: str,
        instances: List[Dict],
    ):
        """
        Args
            project: Your project ID or project number.
            location: Region where Endpoint is located. For example, 'us-central1'.
            endpoint_name: A fully qualified endpoint name or endpoint ID. Example: "projects/123/locations/us-central1/endpoints/456" or
                   "456" when project and location are initialized or passed.
            instances: A list of one or more instances (examples) to return a prediction for.
        """
        aiplatform.init(project=project, location=location)
    
        endpoint = aiplatform.Endpoint(endpoint_name)
    
        response = endpoint.predict(instances=instances)
    
        for prediction_ in response.predictions:
            print(prediction_)
    
    

###  API: Regression 

### gcloud

  1. Create a file named `request.json` with the following contents: 
         
         {
           "instances": [
             {
               PREDICTION_DATA_ROW
             }
           ]
         }
             

Replace the following: 

     * PREDICTION_DATA_ROW: A JSON object with keys as the feature names and values as the corresponding feature values. For example, for a dataset with a number, an array of numbers, and a category, the row of data might look like the following example request:
           
           "age":3.6,
           "sq_ft":5392,
           "code": "90331"
           

A value must be provided for every feature included in training. The format of the data used for prediction must match the format used for training. Refer to [Data format for predictions](https://docs.cloud.google.com/vertex-ai/docs/datasets/data-types-tabular#format-for-prediction) for details. 

  2. Run the following command:
         
         gcloud ai endpoints predict ENDPOINT_ID \
           --region=LOCATION_ID \
           --json-request=request.json

Replace the following:

     * ENDPOINT_ID: The ID for the endpoint. 
     * LOCATION_ID: The region where you are using Vertex AI. 



### REST

You use the [endpoints.predict](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/predict) method to request an online inference. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where Endpoint is located. For example, `us-central1`. 
  * PROJECT_ID: .
  * ENDPOINT_ID: The ID for the endpoint.
  * PREDICTION_DATA_ROW: A JSON object with keys as the feature names and values as the corresponding feature values. For example, for a dataset with a number, an array of numbers, and a category, the row of data might look like the following example request:
        
        "age":3.6,
        "sq_ft":5392,
        "code": "90331"
        

A value must be provided for every feature included in training. The format of the data used for prediction must match the format used for training. Refer to [Data format for predictions](https://docs.cloud.google.com/vertex-ai/docs/datasets/data-types-tabular#format-for-prediction) for details. 

  * DEPLOYED_MODEL_ID: Output by the `predict` method. The ID of the model used to generate the inference. 



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          PREDICTION_DATA_ROW
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:predict"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/endpoints/ENDPOINT_ID:predict" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "predictions": [
        [
          {
            "value": 65.14233
          }
        ]
      ],
      "deployedModelId": "DEPLOYED_MODEL_ID"
    }
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.util.[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html);
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html);
    import com.google.cloud.aiplatform.v1.schema.predict.prediction.[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html);
    import com.google.protobuf.[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.List;
    
    public class PredictTabularRegressionSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String instance = "[{ “feature_column_a”: “value”, “feature_column_b”: “value”}]";
        String endpointId = "YOUR_ENDPOINT_ID";
        predictTabularRegression(instance, project, endpointId);
      }
    
      static void predictTabularRegression(String instance, String project, String endpointId)
          throws IOException {
        PredictionServic[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html)ceSettings =
            PredictionServic[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html)          .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (PredictionServic[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html)ceClient =
            PredictionServic[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html)onServiceSettings)) {
          String location = "us-central1";
          EndpointName end[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html)EndpointName.of([EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html)ation, endpointId);
    
          ListValue.Builde[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)ue = ListValue.newBui[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)     JsonFormat.parse[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html)instance, listValue);
          List<Value> instan[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)listValue.getValuesList();
    
          Value parameters[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)lue.newBuilder[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)tListValue(listValue).build();
          PredictResponse [PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html) =
              predictionServiceClient.predict(endpointName, instanceList, parameters);
          System.out.println("Predict Tabular Regression Response");
          System.out.format("\tDisplay Model Id: %s\n", predictResponse.predictResponse.[getDeployedModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getDeployedModelId__)().out.println("Predictions");
          for (Value prediction[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)edictResponse.predictResponse.[getPredictionsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getPredictionsList__)()larRegressio[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html)uilder =
                TabularRegressio[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html)        TabularRegressio[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html)      (TabularRegressio[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html).f[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html)tBuilder, prediction);
    
            System.out.printf("\tUpper bound: %f\n", result.getUpperBresult.[getUpperBound](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularRegressionPredictionResult_getUpperBound__)()m.out.printf("\tLower bound: %f\n", result.getLowerBresult.[getLowerBound](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularRegressionPredictionResult_getLowerBound__)()m.out.printf("\tValue: %f\n", result.getValue(result.[getValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularRegressionPredictionResult_getValue__)()
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const endpointId = 'YOUR_ENDPOINT_ID';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    const aiplatform = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    const {prediction} =
      aiplatform.protos.google.cloud.aiplatform.v1.schema.predict;
    
    // Imports the Google Cloud Prediction service client
    const {PredictionServiceClient} = aiplatform.v1;
    
    // Import the helper module for converting arbitrary protobuf.Value objects.
    const {helpers} = aiplatform;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const predictionServiceClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function predictTablesRegression() {
      // Configure the endpoint resource
      const endpoint = `projects/${project}/locations/${location}/endpoints/${endpointId}`;
      const parameters = [helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue({});
    
      // TODO (erschmid): Make this less painful
      const instance = [helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue({
        BOOLEAN_2unique_NULLABLE: false,
        DATETIME_1unique_NULLABLE: '2019-01-01 00:00:00',
        DATE_1unique_NULLABLE: '2019-01-01',
        FLOAT_5000unique_NULLABLE: 1611,
        FLOAT_5000unique_REPEATED: [2320, 1192],
        INTEGER_5000unique_NULLABLE: '8',
        NUMERIC_5000unique_NULLABLE: 16,
        STRING_5000unique_NULLABLE: 'str-2',
        STRUCT_NULLABLE: {
          BOOLEAN_2unique_NULLABLE: false,
          DATE_1unique_NULLABLE: '2019-01-01',
          DATETIME_1unique_NULLABLE: '2019-01-01 00:00:00',
          FLOAT_5000unique_NULLABLE: 1308,
          FLOAT_5000unique_REPEATED: [2323, 1178],
          FLOAT_5000unique_REQUIRED: 3089,
          INTEGER_5000unique_NULLABLE: '1777',
          NUMERIC_5000unique_NULLABLE: 3323,
          TIME_1unique_NULLABLE: '23:59:59.999999',
          STRING_5000unique_NULLABLE: 'str-49',
          TIMESTAMP_1unique_NULLABLE: '1546387199999999',
        },
        TIMESTAMP_1unique_NULLABLE: '1546387199999999',
        TIME_1unique_NULLABLE: '23:59:59.999999',
      });
    
      const instances = [instance];
      const request = {
        endpoint,
        instances,
        parameters,
      };
    
      // Predict request
      const [response] = await predictionServiceClient.predict(request);
    
      console.log('Predict tabular regression response');
      console.log(`\tDeployed model id : ${response.deployedModelId}`);
      const predictions = response.predictions;
      console.log('\tPredictions :');
      for (const predictionResultVal of predictions) {
        const predictionResultObj =
          prediction.TabularRegressionPredictionResult.fromValue(
            predictionResultVal
          );
        console.log(`\tUpper bound: ${predictionResultObj.upper_bound}`);
        console.log(`\tLower bound: ${predictionResultObj.lower_bound}`);
        console.log(`\tLower bound: ${predictionResultObj.value}`);
      }
    }
    predictTablesRegression();

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    def predict_tabular_regression_sample(
        project: str,
        location: str,
        endpoint_name: str,
        instances: List[Dict],
    ):
        aiplatform.init(project=project, location=location)
    
        endpoint = aiplatform.Endpoint(endpoint_name)
    
        response = endpoint.predict(instances=instances)
    
        for prediction_ in response.predictions:
            print(prediction_)
    
    

## Interpret prediction results

###  Classification 

Classification models return a confidence score. 

The confidence score communicates how strongly your model associates each class or label with a test item. The higher the number, the higher the model's confidence that the label should be applied to that item. You decide how high the confidence score must be for you to accept the model's results.

###  Regression 

Regression models return an inference value. 

If your model uses probabilistic inference, the `value` field contains the minimizer of the optimization objective. For example, if your optimization objective is `minimize-rmse`, the `value` field contains the mean value. If it is `minimize-mae`, the `value` field contains the median value.

If your model uses probabilistic inference with quantiles, Vertex AI provides quantile values and inferences in addition to the minimizer of the optimization objective. Quantile values are set during model training. Quantile inferences are the inference values associated with the quantile values.

TabNet provides inherent model interpretability by giving users insight into which features it used to help make its decision. The algorithm utilizes [attention](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf), which learns to selectively enhance the influence of some features while diminishing the influence of others through a weighted average. For a particular decision, TabNet decides in a stepwise fashion how much importance to place on each feature. It then combines each of the steps to create a final prediction. The attention is multiplicative, where larger values indicate that the feature played a larger role in the prediction and a value of zero means that the feature played no role in that decision. Because TabNet uses multiple decision steps, the attention placed on the features across all of the steps are linearly combined after appropriate scaling. This linear combination across all of TabNet's decision steps is the total feature importance that TabNet provides you. 

## Example output for inferences

The return payload for an online inference with feature importance from a regression model looks similar to the following example.
    
    
    {
       "predictions":[
          {
             "value":0.3723912537097931,
             "feature_importance":{
                "MSSubClass":0.12,
                "MSZoning":0.33,
                "LotFrontage":0.27,
                "LotArea":0.06,
                ...
             }
          }
       ]
    }
    

## What's next

  * Learn how to [export your model](https://docs.cloud.google.com/vertex-ai/docs/export/export-model-tabular).
  * Learn about [pricing for online inferences](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


