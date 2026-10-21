---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores/
title: Manage featurestores \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:00:39.465891+00:00
---

# Manage featurestores  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Manage featurestores Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

To learn more, run the "Example Feature Store workflow with sample data" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb)

Learn how to create, list, describe, update, and delete featurestores. A featurestore is a top-level container for entity types, features, and feature values.

## Online and offline storage

Vertex AI Feature Store (Legacy) uses two storage methods classified as _online storage_ and _offline storage_ , which are [priced](https://docs.cloud.google.com/vertex-ai/pricing#featurestore) differently. All featurestores have offline storage and optionally, online storage.

Online storage retains the latest timestamp values of your features to efficiently handle online serving requests. When you run an import job by using the API, you can control the job if the data is written to the online store. Skipping the online store prevents any load on the online serving nodes. For example, when you run backfill jobs, you can disable writes to the online store and write only to the offline store. For more information, see the `disableOnlineServing` flag in the [API reference](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/importFeatureValues).

Vertex AI Feature Store (Legacy) uses offline storage to store data until the data reaches the [retention limit](https://docs.cloud.google.com/vertex-ai/docs/quotas#featurestore) or until you delete the data. You can store unlimited data in the offline store. You can control offline storage costs by managing how much data you keep. You can also override the default online store data retention limit for your featurestore and the offline data retention limit for an entity type. [Learn more about Vertex AI Feature Store (Legacy) quotas and limits](https://docs.cloud.google.com/vertex-ai/docs/quotas#featurestore).

Use the Google Cloud console to view the amount of online and offline storage you are using. [View](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics#featurestore) your featurestore's **Total online storage** and **Total offline storage** monitoring metrics to determine your usage.

## Online serving nodes

Online serving nodes provide the compute resources used to store and serve feature values for low-latency online serving. These nodes are always running even when they aren't serving data. You are [charged](https://docs.cloud.google.com/vertex-ai/pricing#featurestore) for each node hour.

The storage limit for online serving nodes is 5 TB per node. [Learn more about Vertex AI Feature Store (Legacy) quotas and limits](https://docs.cloud.google.com/vertex-ai/docs/quotas#featurestore).

**Note:** The storage limit is measured in binary terabytes (TB), where 1 TB is 240 bytes. This unit of measurement is also known as a [tebibyte (TiB)](https://en.wikipedia.org/wiki/Tebibyte).

The number of online serving nodes that you require is directly proportional to the following two factors:

  * The number of online serving requests (queries per second) that the featurestore receives.
  * The number of import jobs that write to online storage.



Both factors contribute to the CPU utilization and performance of the nodes. From the Google Cloud console, view the [metrics](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics#featurestore) of the following:

  * **Queries per second** : Number of queries per second to your featurestore.
  * **Node count** : Number of your online serving nodes.
  * **CPU utilization** : CPU utilization of your nodes.



If CPU utilization is consistently high, consider increasing the number of online serving nodes for your featurestore.

### Test performance of online serving nodes

You can test the performance of online serving nodes for real-time feature serving. This lets you ensure that the featurestore has sufficient machine resources to perform within predetermined QPS or latency thresholds. You can perform these tests based on various benchmarking parameters, such as QPS, latency, and API. For guidelines and best practices to test the performance of online serving nodes, see [Test the performance of online serving nodes for real-time serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/best-practices#online_serving_benchmarking) in [Best practices for Vertex AI Feature Store (Legacy)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/best-practices).

Additionally, you can use the [Vertex AI Benchmarker open source tool](https://github.com/google/vertex-ai-benchmarker/blob/main/README.md) to load test the performance of your feature store resources. The Vertex AI Benchmarker open source tool consists of a Python command-line tool and a Java worker.

**Caution:** Using the Vertex AI Benchmarker framework with production resources can lead to rate limiting, quota limits, and other production issues. Use this tool in an environment designated for testing.

### Scaling Options

You can switch between the following options to configure your number of online serving nodes:

  * **Autoscaling**

If you choose autoscaling, the featurestore automatically changes the number of nodes based on CPU utilization. Autoscaling reviews traffic patterns to maintain performance and optimize your cost by adding nodes when the traffic increases and removing nodes when the traffic decreases.

Autoscaling performs well for traffic patterns that experience gradual growth and decline. If you use Vertex AI Feature Store (Legacy) extensively for traffic patterns that encounter frequent load fluctuations, use autoscaling to improve cost efficiency.

**Caution:** Autoscaling isn't effective for managing sudden bursts of traffic. For more information, see Additional considerations for autoscaling.   
If you are expecting sudden bursts of traffic, set the `minNodeCount` flag to a threshold that is high enough to handle the bursts. For more information, see [Scaling](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores#scaling) in the [API reference](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores#scaling).
  * **Allocating a fixed node count**

If you allocate a fixed node count, Vertex AI Feature Store (Legacy) maintains a consistent number of nodes regardless of the traffic patterns. The fixed node count keeps costs predictable, and the nodes should perform well when there are enough nodes to handle the traffic. You can manually change the fixed node count to handle changes in traffic patterns.




### Additional considerations for autoscaling

If you choose autoscaling, there are four additional points to consider that include:

  * After adding online serving nodes, the online store needs time to rebalance the data. It can take up to 20 minutes under load before you see a significant improvement in performance. As a result, scaling the number of nodes might not help for short bursts of traffic. This limitation applies for both manual scaling and autoscaling.

  * If you submit online serving requests to the featurestore without online serving nodes, the operation returns an error.




### Turn off online serving in your featurestore

If you don't require online serving and want to prevent incurring changes for online serving nodes, set the number of online serving nodes to zero. To turn off online serving in your featurestore, set the following configuration:

  1. If you're using autoscaling, remove the `scaling` parameter.

  2. Set the fixed number of online serving nodes to `0`.




For more information about how to create a featurestore, see [Create a featurestore](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#create_featurestore). For more information about how to modify the configuration of an existing featurestore, see [Update a featurestore](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#update).

If you set the number of online serving nodes to `0`, the entire online store, including its data, is deleted. If you want to temporarily turn off your online store and then restore it, you must reimport the deleted data.

For example, if you set the online serving node count for your featurestore to `0` and then provision online serving nodes by setting the node count to `1` or higher, Vertex AI Feature Store (Legacy) doesn't migrate the deleted feature data to the online store. To repopulate your online store, you must reimport your data. One way to reimport your data is to export the historical data before you disable online serving nodes, and then import the exported data after you provision the nodes.

When you provision online serving nodes, you must wait for the operation to complete before importing new data. In-progress import jobs resume only after the online serving node provisioning is complete.

If you submit an online serving request to the featurestore without online serving nodes, the request returns an error.

## Create a featurestore

Create a featurestore resource to contain entity types and features. The location of your featurestore must be in the same location as your source data. For example, if your featurestore is in `us-central,` you can import data from files in Cloud Storage buckets that are in `us-central1` or in the US multi-region location, though source data from dual-region buckets isn't supported. Similarly for BigQuery, you can import data from tables that are in `us-central1` or in the US multi-region location. For more information, see [Source data requirements](https://docs.cloud.google.com/vertex-ai/docs/featurestore/source-data).

Vertex AI Feature Store (Legacy) availability can vary by location. For more information, see [Feature availability](https://docs.cloud.google.com/vertex-ai/docs/general/locations#feature-availability).

**Note:** Billing for a featurestore instance starts when it is created and continues as long as it is serving requests or idle. For more information, see the [pricing page](https://docs.cloud.google.com/vertex-ai/pricing#featurestore).

### Web UI

You can create a featurestore using the Google Cloud console if a featurestore isn't already created in the Google Cloud project for the selected region. If a featurestore already exists for the project and region, use another method.

To create a featurestore using the Google Cloud console:

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Click **Create featurestore**
  3. Specify a name for the featurestore.
  4. If you want to turn on online serving for the featurestore, click the **Turn on online serving** toggle and set the scaling options.  
For more information about online serving and scaling options, see Online serving nodes
  5. Click **Create**.



### Terraform

The following sample uses the [`google_vertex_ai_featurestore`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vertex_ai_featurestore) Terraform resource to create a featurestore with a fixed node count. The name of the featurestore is `featurestore_yyyyyyyy`, where `yyyyyyyy` is a randomly generated alphanumeric identifier. 

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    # Featurestore name must be unique for the project
    resource "random_id" "featurestore_name_suffix" {
      byte_length = 8
    }
    
    resource "google_vertex_ai_featurestore" "main" {
      name   = "featurestore_${random_id.featurestore_name_suffix.hex}"
      region = "us-central1"
      labels = {
        environment = "testing"
      }
    
      online_serving_config {
        fixed_node_count = 1
      }
    
      force_destroy = true
    }

### REST

To create a featurestore, send a POST request by using the [featurestores.create](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores/create) method. 

The following sample creates a featurestore with a fixed node count of `1`. The node count specifies the number of online serving nodes, which affects the number of online serving requests that the featurestore can handle. The latency could increase if the number of nodes cannot support the number of incoming requests.

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is created. For example, `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID for the featurestore.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores?featurestoreId=FEATURESTORE_ID

Request JSON body: 
    
    
    {
      "online_serving_config": {
        "fixed_node_count": 1
      },
      "labels": {
        "environment": "testing"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores?featurestoreId=FEATURESTORE_ID"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores?featurestoreId=FEATURESTORE_ID" | Select-Object -Expand Content

You should see output similar to the following. You can use the OPERATION_ID in the response to [get the status](https://docs.cloud.google.com/vertex-ai/docs/general/long-running-operations) of the operation.
    
    
    {
    "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-02-26T00:44:40.722474Z",
          "updateTime": "2021-02-26T00:44:40.722474Z"
        }
      }
    }
    

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from google.cloud import aiplatform
    
    
    def create_featurestore_sample(
        project: str,
        location: str,
        featurestore_id: str,
        online_store_fixed_node_count: int = 1,
        sync: bool = True,
    ):
    
        aiplatform.init(project=project, location=location)
    
        fs = aiplatform.Featurestore.create(
            featurestore_id=featurestore_id,
            online_store_fixed_node_count=online_store_fixed_node_count,
            sync=sync,
        )
    
        fs.wait()
    
        return fs
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[CreateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[CreateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreRequest.html);
    import com.google.cloud.aiplatform.v1.[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html);
    import com.google.cloud.aiplatform.v1.[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html).[OnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.html);
    import com.google.cloud.aiplatform.v1.[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html).[OnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.html).[Scaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.Scaling.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateFeaturestoreSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        int minNodeCount = 1;
        int maxNodeCount = 5;
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 900;
        createFeaturestoreSample(
            project, featurestoreId, minNodeCount, maxNodeCount, location, endpoint, timeout);
      }
    
      static void createFeaturestoreSample(
          String project,
          String featurestoreId,
          int minNodeCount,
          int maxNodeCount,
          String location,
          String endpoint,
          int timeout)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
    
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [OnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.html).Builder builderValue =
              [OnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.html).newBuilder()
                  .[setScaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.Builder.html#com_google_cloud_aiplatform_v1_Featurestore_OnlineServingConfig_Builder_setScaling_com_google_cloud_aiplatform_v1_Featurestore_OnlineServingConfig_Scaling_)(
                      [Scaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.Scaling.html).newBuilder().setMinNodeCount(minNodeCount).setMaxNodeCount(maxNodeCount));
          [Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html) featurestore =
              [Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html).newBuilder().[setOnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.Builder.html#com_google_cloud_aiplatform_v1_Featurestore_Builder_setOnlineServingConfig_com_google_cloud_aiplatform_v1_Featurestore_OnlineServingConfig_)(builderValue).build();
          String parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location).toString();
    
          [CreateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreRequest.html) createFeaturestoreRequest =
              [CreateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreRequest.html).newBuilder()
                  .setParent(parent)
                  .setFeaturestore(featurestore)
                  .[setFeaturestoreId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreRequest.Builder.html#com_google_cloud_aiplatform_v1_CreateFeaturestoreRequest_Builder_setFeaturestoreId_java_lang_String_)(featurestoreId)
                  .build();
    
          OperationFuture<Featurestore, CreateFeaturestoreOperationMetadata> featurestoreFuture =
              featurestoreServiceClient.[createFeaturestoreAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html#com_google_cloud_aiplatform_v1_FeaturestoreServiceClient_createFeaturestoreAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_LocationName_com_google_cloud_aiplatform_v1_Featurestore_)(createFeaturestoreRequest);
          System.out.format(
              "Operation name: %s%n", featurestoreFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html) featurestoreResponse = featurestoreFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(timeout, TimeUnit.SECONDS);
          System.out.println("Create Featurestore Response");
          System.out.format("Name: %s%n", featurestoreResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html#com_google_cloud_aiplatform_v1_Featurestore_getName__)());
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
    
    // const project = 'YOUR_PROJECT_ID';
    // const featurestoreId = 'YOUR_FEATURESTORE_ID';
    // const minNodeCount = <MINIMUM_NO_OF_NODES>;
    // const maxNodeCount = <MAXIMUM_NO_OF_NODES>;
    // const location = 'YOUR_PROJECT_LOCATION';
    // const apiEndpoint = 'YOUR_API_ENDPOINT';
    // const timeout = <TIMEOUT_IN_MILLI_SECONDS>;
    
    // Imports the Google Cloud Featurestore Service Client library
    const {FeaturestoreServiceClient} =
      require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: apiEndpoint,
    };
    
    // Instantiates a client
    const featurestoreServiceClient = new [FeaturestoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(
      clientOptions
    );
    
    async function createFeaturestore() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
    
      const featurestore = {
        onlineServingConfig: {
          scaling: {
            minNodeCount: minNodeCount,
            maxNodeCount: maxNodeCount,
          },
        },
      };
    
      const request = {
        parent: parent,
        featurestore: featurestore,
        featurestoreId: featurestoreId,
      };
    
      // Create Featurestore request
      const [operation] = await featurestoreServiceClient.createFeaturestore(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Create featurestore response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    createFeaturestore();

### Create a featurestore that uses a CMEK

Before you begin, if you don't have an existing CMEK (customer-managed encryption key), [use Cloud Key Management Service to configure a customer-managed encryption key and set up permissions](https://docs.cloud.google.com/vertex-ai/docs/general/cmek#configure-cmek). The following sample creates a featurestore that uses a CMEK key.

If Vertex AI loses permission to the associated CMEK key, any resources and values within featurestores that were encrypted by that key become inaccessible until Vertex AI can use that key again.

After 30 days, if Vertex AI still doesn't have access to the CMEK key, Vertex AI deletes all of the featurestores that were encrypted with that key. When creating new featurestores, you can't reuse those featurestores names.

### Web UI

Use another method. You cannot create a featurestore from the Google Cloud console.

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is created. For example, `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID for the featurestore.
  * CMEK_PROJECT: The project ID or project number that contains your CMEK.
  * KEY_RING: The name of the Cloud Key Management Service key ring that your encryption key is on.
  * KEY_NAME: The name of the encryption key to use.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores?featurestoreId=FEATURESTORE_ID

Request JSON body: 
    
    
    {
      "online_serving_config": {
        "fixed_node_count": 1
      },
      "encryption_spec":{
        "kms_key_name": "projects/CMEK_PROJECT/locations/LOCATION_ID/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores?featurestoreId=FEATURESTORE_ID"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores?featurestoreId=FEATURESTORE_ID" | Select-Object -Expand Content

You should see output similar to the following. You can use the OPERATION_ID in the response to [get the status](https://docs.cloud.google.com/vertex-ai/docs/general/long-running-operations) of the operation.
    
    
    {
    "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-02-26T00:44:40.722474Z",
          "updateTime": "2021-02-26T00:44:40.722474Z"
        }
      }
    }
    

## List featurestores

List all featurestores in a project.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Featurestore** column to see the featurestores in your project for the selected region.



### REST

To list featurestores for a particular region in your project, send a GET request by using the [featurestores.list](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores/list) method.

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "featurestores": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/test",
          "createTime": "2021-02-26T00:44:44.216805Z",
          "updateTime": "2021-02-26T00:44:44.364916Z",
          "etag": "AMEw9yNL0s7qZh8lZVZ5T3BEuhoEgFR7JmjbbCSAkRZjeKDXkkIYnxxA4POe5BWT8cCn",
          "labels": {
            "environment": "testing"
          },
          "onlineServingConfig": {
            "fixedNodeCount": 2
          },
          "state": "STABLE"
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/featurestore_demo",
          "createTime": "2021-02-25T00:39:40.598781Z",
          "updateTime": "2021-02-25T00:39:40.744038Z",
          "etag": "AMEw9yO_e0vm-9W_yeCz4rJm-XnnEMYQ-vQesevxya_sz-FckuysnDwo3cEXHdWWSeda",
          "labels": {
            "environment": "testing"
          },
          "onlineServingConfig": {
            "fixedNodeCount": 3
          },
          "state": "STABLE"
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[ListFeaturestoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturestoresRequest.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import java.io.IOException;
    
    public class ListFeaturestoresSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        listFeaturestoresSample(project, location, endpoint);
      }
    
      static void listFeaturestoresSample(String project, String location, String endpoint)
          throws IOException {
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [ListFeaturestoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturestoresRequest.html) listFeaturestoresRequest =
              [ListFeaturestoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturestoresRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location).toString())
                  .build();
    
          System.out.println("List Featurestores Response");
          for ([Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html) element :
              featurestoreServiceClient.listFeaturestores(listFeaturestoresRequest).iterateAll()) {
            System.out.println(element);
          }
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
    
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    // const apiEndpoint = 'YOUR_API_ENDPOINT';
    // const timeout = <TIMEOUT_IN_MILLI_SECONDS>;
    
    // Imports the Google Cloud Featurestore Service Client library
    const {FeaturestoreServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: apiEndpoint,
    };
    
    // Instantiates a client
    const featurestoreServiceClient = new [FeaturestoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(
      clientOptions
    );
    
    async function listFeaturestores() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
    
      const request = {
        parent: parent,
      };
    
      // List featurestores request
      const [response] = await featurestoreServiceClient.listFeaturestores(
        request,
        {timeout: Number(timeout)}
      );
    
      console.log('List featurestores response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    listFeaturestores();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## View featurestore details

Get details about a featurestore such as its name and online serving configuration. If you use the Google Cloud console, you can also view [Cloud Monitoring metrics](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics#featurestore) for featurestores.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Featurestore** column and find the featurestore that you want to view information for.
  4. Click the name of the featurestore to view its Monitoring metrics.
  5. Click the **Properties** tab to view the featurestore's online serving configuration.



### REST

To get details about a single featurestore, send a GET request by using the [featurestores.get](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores/get) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID",
      "createTime": "2021-02-25T00:39:40.598781Z",
      "updateTime": "2021-02-25T00:39:40.744038Z",
      "etag": "AMEw9yNy_b4IaMIvw1803ZT38cpUtjfwlyLkR709oBCY6pQrm6dHophLcqhrvsNqkQQZ",
      "onlineServingConfig": {
        "fixedNodeCount": 3
      },
      "state": "STABLE"
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[GetFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeaturestoreRequest.html);
    import java.io.IOException;
    
    public class GetFeaturestoreSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        getFeaturestoreSample(project, featurestoreId, location, endpoint);
      }
    
      static void getFeaturestoreSample(
          String project, String featurestoreId, String location, String endpoint) throws IOException {
    
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [GetFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeaturestoreRequest.html) getFeaturestoreRequest =
              [GetFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeaturestoreRequest.html).newBuilder()
                  .setName([FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html).of(project, location, featurestoreId).toString())
                  .build();
    
          [Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html) featurestore = featurestoreServiceClient.getFeaturestore(getFeaturestoreRequest);
          System.out.println("Get Featurestore Response");
          System.out.println(featurestore);
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
    
    // const project = 'YOUR_PROJECT_ID';
    // const featurestoreId = 'YOUR_FEATURESTORE_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    // const apiEndpoint = 'YOUR_API_ENDPOINT';
    // const timeout = <TIMEOUT_IN_MILLI_SECONDS>;
    
    // Imports the Google Cloud Featurestore Service Client library
    const {FeaturestoreServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: apiEndpoint,
    };
    
    // Instantiates a client
    const featurestoreServiceClient = new [FeaturestoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(
      clientOptions
    );
    
    async function getFeaturestore() {
      // Configure the parent resource
      const name = `projects/${project}/locations/${location}/featurestores/${featurestoreId}`;
    
      const request = {
        name: name,
      };
    
      // Get Featurestore request
      const [response] = await featurestoreServiceClient.getFeaturestore(
        request,
        {timeout: Number(timeout)}
      );
    
      console.log('Get featurestore response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    getFeaturestore();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## Update a featurestore

Update a featurestore, for example, to change the number of online serving nodes or update labels on a featurestore.

### Web UI

You can update only the number of online serving nodes. To update labels, use the API.

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Featurestore** column and click the name of the featurestore to update.
  4. Click **Edit configuration** to open the **Edit featurestore configuration** pane.
  5. Edit the featurestore configuration.
  6. Click **Update** to apply your changes.



### REST

To update a featurestore, send a PATCH request by using the [featurestores.patch](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores/patch) method. 

The following sample updates the number of online serving nodes to `2` for the featurestore. All other settings remain the same. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.



HTTP method and URL: 
    
    
    PATCH https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID

Request JSON body: 
    
    
    {
      "online_serving_config": {
        "fixed_node_count": 2
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID" | Select-Object -Expand Content

You should see output similar to the following. You can use the OPERATION_ID in the response to [get the status](https://docs.cloud.google.com/vertex-ai/docs/general/long-running-operations) of the operation.
    
    
    {
    "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.UpdateFeaturestoreOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-03-18T21:12:08.373664Z",
          "updateTime": "2021-03-18T21:12:08.373664Z"
        }
      }
    }
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html);
    import com.google.cloud.aiplatform.v1.[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html).[OnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.html);
    import com.google.cloud.aiplatform.v1.[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html).[OnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.html).[Scaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.Scaling.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[UpdateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[UpdateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateFeaturestoreSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        int minNodeCount = 2;
        int maxNodeCount = 4;
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
        updateFeaturestoreSample(
            project, featurestoreId, minNodeCount, maxNodeCount, location, endpoint, timeout);
      }
    
      static void updateFeaturestoreSample(
          String project,
          String featurestoreId,
          int minNodeCount,
          int maxNodeCount,
          String location,
          String endpoint,
          int timeout)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [OnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.html).Builder builderValue =
              [OnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.html).newBuilder()
                  .[setScaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.Builder.html#com_google_cloud_aiplatform_v1_Featurestore_OnlineServingConfig_Builder_setScaling_com_google_cloud_aiplatform_v1_Featurestore_OnlineServingConfig_Scaling_)(
                      [Scaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.Scaling.html).newBuilder().setMinNodeCount(minNodeCount).setMaxNodeCount(maxNodeCount));
          [Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html) featurestore =
              [Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html).newBuilder()
                  .setName([FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html).of(project, location, featurestoreId).toString())
                  .[setOnlineServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.Builder.html#com_google_cloud_aiplatform_v1_Featurestore_Builder_setOnlineServingConfig_com_google_cloud_aiplatform_v1_Featurestore_OnlineServingConfig_)(builderValue)
                  .build();
    
          [UpdateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreRequest.html) request =
              [UpdateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreRequest.html).newBuilder().setFeaturestore(featurestore).build();
    
          OperationFuture<Featurestore, UpdateFeaturestoreOperationMetadata> updateFeaturestoreFuture =
              featurestoreServiceClient.[updateFeaturestoreAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html#com_google_cloud_aiplatform_v1_FeaturestoreServiceClient_updateFeaturestoreAsync_com_google_cloud_aiplatform_v1_Featurestore_com_google_protobuf_FieldMask_)(request);
          System.out.format(
              "Operation name: %s%n", updateFeaturestoreFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html) featurestoreResponse = updateFeaturestoreFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(timeout, TimeUnit.SECONDS);
          System.out.println("Update Featurestore Response");
          System.out.format("Name: %s%n", featurestoreResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore.html#com_google_cloud_aiplatform_v1_Featurestore_getName__)());
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
    
    // const project = 'YOUR_PROJECT_ID';
    // const featurestoreId = 'YOUR_FEATURESTORE_ID';
    // const minNodeCount = <MINIMUM_NO_OF_NODES>;
    // const maxNodeCount = <MAXIMUM_NO_OF_NODES>;
    // const location = 'YOUR_PROJECT_LOCATION';
    // const apiEndpoint = 'YOUR_API_ENDPOINT';
    // const timeout = <TIMEOUT_IN_MILLI_SECONDS>;
    
    // Imports the Google Cloud Featurestore Service Client library
    const {FeaturestoreServiceClient} =
      require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: apiEndpoint,
    };
    
    // Instantiates a client
    const featurestoreServiceClient = new [FeaturestoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(
      clientOptions
    );
    
    async function updateFeaturestore() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}/featurestores/${featurestoreId}`;
    
      const featurestore = {
        name: parent,
        onlineServingConfig: {
          scaling: {
            minNodeCount: minNodeCount,
            maxNodeCount: maxNodeCount,
          },
        },
      };
    
      const request = {
        featurestore: featurestore,
      };
    
      // Update Featurestore request
      const [operation] = await featurestoreServiceClient.updateFeaturestore(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Update featurestore response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    updateFeaturestore();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## Delete a featurestore

Delete a featurestore. If the featurestore includes existing entity types and features, enable the `force` query parameter to delete the featurestore and all of its contents.

### Web UI

Use another method. You cannot delete a featurestore from the Google Cloud console.

### REST

To delete a featurestore and all of its content, send a DELETE request by using the [featurestores.delete](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores/delete) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.
  * BOOLEAN: Whether to delete the featurestore even if it contains entity types and features. The `force` query parameter is optional and is `false` by default.



HTTP method and URL: 
    
    
    DELETE https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID?force=BOOLEAN

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID?force=BOOLEAN"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID?force=BOOLEAN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATIONS_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.DeleteOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-05-03T17:50:21.813112Z",
          "updateTime": "2021-05-03T17:50:21.813112Z"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from google.cloud import aiplatform
    
    
    def delete_featurestore_sample(
        project: str,
        location: str,
        featurestore_name: str,
        sync: bool = True,
        force: bool = True,
    ):
    
        aiplatform.init(project=project, location=location)
    
        fs = aiplatform.featurestore.Featurestore(featurestore_name=featurestore_name)
        fs.delete(sync=sync, force=force)
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[DeleteFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeaturestoreRequest.html);
    import com.google.cloud.aiplatform.v1.[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteFeaturestoreSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        boolean useForce = true;
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 60;
        deleteFeaturestoreSample(project, featurestoreId, useForce, location, endpoint, timeout);
      }
    
      static void deleteFeaturestoreSample(
          String project,
          String featurestoreId,
          boolean useForce,
          String location,
          String endpoint,
          int timeout)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
    
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [DeleteFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeaturestoreRequest.html) deleteFeaturestoreRequest =
              [DeleteFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeaturestoreRequest.html).newBuilder()
                  .setName([FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html).of(project, location, featurestoreId).toString())
                  .setForce(useForce)
                  .build();
    
          OperationFuture<Empty, DeleteOperationMetadata> operationFuture =
              featurestoreServiceClient.[deleteFeaturestoreAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html#com_google_cloud_aiplatform_v1_FeaturestoreServiceClient_deleteFeaturestoreAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_FeaturestoreName_)(deleteFeaturestoreRequest);
          System.out.format("Operation name: %s%n", operationFuture.getInitialFuture().get().getName());
          System.out.println("Waiting for operation to finish...");
          operationFuture.get(timeout, TimeUnit.SECONDS);
    
          System.out.format("Deleted Featurestore.");
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
    
    // const project = 'YOUR_PROJECT_ID';
    // const featurestoreId = 'YOUR_FEATURESTORE_ID';
    // const force = <BOOLEAN>;
    // const location = 'YOUR_PROJECT_LOCATION';
    // const apiEndpoint = 'YOUR_API_ENDPOINT';
    // const timeout = <TIMEOUT_IN_MILLI_SECONDS>;
    
    // Imports the Google Cloud Featurestore Service Client library
    const {FeaturestoreServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: apiEndpoint,
    };
    
    // Instantiates a client
    const featurestoreServiceClient = new [FeaturestoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(
      clientOptions
    );
    
    async function deleteFeaturestore() {
      // Configure the name resource
      const name = `projects/${project}/locations/${location}/featurestores/${featurestoreId}`;
    
      const request = {
        name: name,
        force: Boolean(force),
      };
    
      // Delete Featurestore request
      const [operation] = await featurestoreServiceClient.deleteFeaturestore(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Delete featurestore response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    deleteFeaturestore();

## What's next

  * Learn how to manage [entity types](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-entity-types) and [features](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-features).
  * [Troubleshoot](https://docs.cloud.google.com/vertex-ai/docs/general/troubleshooting#feature-store) common Vertex AI Feature Store (Legacy) issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
