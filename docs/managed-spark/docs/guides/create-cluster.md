---
url: https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster/
title: Create a cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:36.821250+00:00
---

# Create a cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark prevents the creation of clusters with image versions prior to 1.3.95, 1.4.77, 1.5.53, and 2.0.27, which were affected by [Apache Log4j security vulnerabilities](https://logging.apache.org/log4j/2.x/security.html). Managed Service for Apache Spark also prevents cluster creation for Managed Service for Apache Spark image versions 0.x, 1.0.x, 1.1.x, and 1.2.x. Managed Service for Apache Spark advises that, when possible, you create Managed Service for Apache Spark clusters with the latest sub-minor image versions.

Image version | log4j version | Customer guidance  
---|---|---  
2.0.29, 1.5.55, and 1.4.79, or later of each | log4j.2.17.1 | Advised  
2.0.28, 1.5.54, and 1.4.78 | log4j.2.17.0 | Advised  
2.0.27, 1.5.53, and 1.4.77 | log4j.2.16.0 | Strongly recommended  
2.0.26, 1.5.52, and 1.4.76, or earlier of each | Older version | Discontinue use  
  
See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for specific image and `log4j` update information.

## Create a cluster

Requirements:

  * **Name:** The cluster name must start with a lowercase letter followed by up to 51 lowercase letters, numbers, and hyphens, and cannot end with a hyphen.

  * **Cluster region:** You must specify a Compute Engine region for the cluster, such as `us-east1` or `europe-west1`, to isolate cluster resources, such as VM instances and cluster metadata stored in Cloud Storage, within the region.

    * See [Cluster region](https://docs.cloud.google.com/managed-spark/docs/concepts/cluster-region) for more information on Compute Engine regions.
    * See [Available regions & zones](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) for information on selecting a region. You can also run the `gcloud compute regions list` command to display a listing of available regions.
  * **Connectivity:** [Compute Engine Virtual Machine instances](https://docs.cloud.google.com/compute/docs/instances) (VMs) in a Managed Service for Apache Spark cluster, consisting of master and worker VMs, require full internal IP networking cross connectivity. The [`default` VPC network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) provides this connectivity (see [Managed Service for Apache Spark Cluster Network Configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network)).

  * **Machine type (recommended):** While specifying a machine type is optional, Google recommends that you explicitly select a machine type for the master and worker VMs in your cluster. If you don't specify a machine type, Managed Service for Apache Spark dynamically selects machine types based on resource availability. This dynamic selection can result in variations in both cost and performance.

    * For more information on choosing a machine type, see [Supported machine types](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types).
    * To mitigate potential resource unavailability issues, we recommend using [Flexible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms), which lets you specify a list of acceptable machine types.

Also see: 

  * [The Managed Service for Apache Spark best practices guide.](https://cloud.google.com/blog/topics/developers-practitioners/best-practices-guide)
  * [Create a cluster with an ARM machine type](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types#create_a_cluster_with_an_arm_machine_type).



### Console

Open the Google Cloud console [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page to display default cluster settings. You can confirm or change the displayed default settings, then click **Additional configuration** to further customize the cluster.

Click **Create cluster** to create the cluster. The cluster name appears in the **Clusters** page, and its status is updated to `Running` after the cluster is provisioned. Click the cluster name to open the cluster details page where you can examine jobs, instances, and configuration settings for your cluster and connect to web interfaces running on the cluster.

### gcloud

To create a Managed Service for Apache Spark cluster on the command line, run the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true).
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --master-machine-type=MASTER_MACHINE_TYPE \
        --worker-machine-type=WORKER_MACHINE_TYPE
    

The command creates a cluster. While master and worker machine types are optional, it is recommended to explicitly specify them using the `--master-machine-type` and `--worker-machine-type` flags (for example, `n4-standard-4`) to ensure consistent cost and performance. If you don't specify machine types, default machine types are selected dynamically based on resource availability. See the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command for information on using command line flags to customize cluster settings.

### Create a cluster with a YAML file

  1. Run the following `gcloud` command to export the configuration of an existing Managed Service for Apache Spark cluster into a `cluster.yaml` file. 
         
         gcloud dataproc clusters export EXISTING_CLUSTER_NAME \
             --region=REGION \
             --destination=cluster.yaml
         

  2. Create a new cluster by importing the YAML file configuration. 
         
         gcloud dataproc clusters import NEW_CLUSTER_NAME \
             --region=REGION \
             --source=cluster.yaml
         




**Note:** During the export operation, cluster-specific fields, such as cluster name, output-only fields, and automatically applied labels are filtered. These fields are disallowed in the imported YAML file used to create a cluster.

**Note:** At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request.

### REST

This section shows how to create a cluster. While specifying machine types is optional, it is recommended to explicitly include `machine_type_uri` in your `master_config` and `worker_config` (for example, `n4-standard-4`) to ensure consistent cost and performance. If you don't specify machine types, default machine types are selected dynamically based on resource availability.

Before using any of the request data, make the following replacements: 

  * CLUSTER_NAME: cluster name
  * PROJECT: Google Cloud project ID
  * REGION: An available Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be created.
  * ZONE: An optional [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) within the selected region where the cluster will be created.
  * MASTER_MACHINE_TYPE: (Recommended) The machine type for the master node (for example, `n4-standard-4`).
  * WORKER_MACHINE_TYPE: (Recommended) The machine type for worker nodes (for example, `n4-standard-4`).



HTTP method and URL: 
    
    
    POST https://dataproc.googleapis.com/v1/projects/PROJECT/regions/REGION/clusters

Request JSON body: 
    
    
    {
      "project_id":"PROJECT",
      "cluster_name":"CLUSTER_NAME",
      "config":{
        "master_config":{
          "num_instances":1,
          "machine_type_uri":"MASTER_MACHINE_TYPE",
          "image_uri":""
        },
        "softwareConfig": {
          "imageVersion": "",
          "properties": {},
          "optionalComponents": []
        },
        "worker_config":{
          "num_instances":2,
          "machine_type_uri":"WORKER_MACHINE_TYPE",
          "image_uri":""
        },
        "gce_cluster_config":{
          "zone_uri":"ZONE"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataproc.googleapis.com/v1/projects/PROJECT/regions/REGION/clusters"

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
        -Uri "https://dataproc.googleapis.com/v1/projects/PROJECT/regions/REGION/clusters" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    "name": "projects/PROJECT/regions/REGION/operations/b5706e31......",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.dataproc.v1.ClusterOperationMetadata",
        "clusterName": "CLUSTER_NAME",
        "clusterUuid": "5fe882b2-...",
        "status": {
          "state": "PENDING",
          "innerState": "PENDING",
          "stateStartTime": "2019-11-21T00:37:56.220Z"
        },
        "operationType": "CREATE",
        "description": "Create cluster with 2 workers",
        "warnings": [
          "For PD-Standard without local SSDs, we strongly recommend provisioning 1TB ...""
        ]
      }
    }
    

**Note:** At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request.

### Go

  1. [Install the client library.](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#installing_the_client_library)
  2. [Set up application default credentials.](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#setting_up_authentication)
  3. Run the code. See [Setting up your development environment](https://docs.cloud.google.com/go/docs/setup).

**Note:** While specifying machine types is optional, it is recommended to explicitly set the master and worker machine types in your cluster configuration (for example, to `n4-standard-4`) to ensure consistent cost and performance. If omitted, default machine types are selected dynamically based on resource availability.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	dataproc "cloud.google.com/go/dataproc/apiv1"
         	"cloud.google.com/go/dataproc/apiv1/dataprocpb"
         	"google.golang.org/api/option"
         )
         
         func createCluster(w io.Writer, projectID, region, clusterName string) error {
         	// projectID := "your-project-id"
         	// region := "us-central1"
         	// clusterName := "your-cluster"
         	ctx := context.Background()
         
         	// Create the cluster client.
         	endpoint := region + "-dataproc.googleapis.com:443"
         	clusterClient, err := dataproc.NewClusterControllerClient(ctx, option.WithEndpoint(endpoint))
         	if err != nil {
         		return fmt.Errorf("dataproc.NewClusterControllerClient: %w", err)
         	}
         	defer clusterClient.Close()
         
         	// Create the cluster config.
         	req := &dataprocpb.CreateClusterRequest{
         		ProjectId: projectID,
         		Region:    region,
         		Cluster: &dataprocpb.Cluster{
         			ProjectId:   projectID,
         			ClusterName: clusterName,
         			Config: &dataprocpb.ClusterConfig{
         				MasterConfig: &dataprocpb.InstanceGroupConfig{
         					NumInstances:   1,
         					MachineTypeUri: "n1-standard-2",
         				},
         				WorkerConfig: &dataprocpb.InstanceGroupConfig{
         					NumInstances:   2,
         					MachineTypeUri: "n1-standard-2",
         				},
         			},
         		},
         	}
         
         	// Create the cluster.
         	op, err := clusterClient.CreateCluster(ctx, req)
         	if err != nil {
         		return fmt.Errorf("CreateCluster: %w", err)
         	}
         
         	resp, err := op.Wait(ctx)
         	if err != nil {
         		return fmt.Errorf("CreateCluster.Wait: %w", err)
         	}
         
         	// Output a success message.
         	fmt.Fprintf(w, "Cluster created successfully: %s", resp.ClusterName)
         	return nil
         }
         




### Java

  1. [Install the client library.](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#installing_the_client_library)
  2. [Set up application default credentials.](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#setting_up_authentication)
  3. Run the code. See [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

**Note:** While specifying machine types is optional, it is recommended to explicitly set the master and worker machine types in your cluster configuration (for example, to `n4-standard-4`) to ensure consistent cost and performance. If omitted, default machine types are selected dynamically based on resource availability.
         
         import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
         import com.google.cloud.dataproc.v1.[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html);
         import com.google.cloud.dataproc.v1.[ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html);
         import com.google.cloud.dataproc.v1.[ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html);
         import com.google.cloud.dataproc.v1.[ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html);
         import com.google.cloud.dataproc.v1.[ClusterOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterOperationMetadata.html);
         import com.google.cloud.dataproc.v1.[InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html);
         import java.io.IOException;
         import java.util.concurrent.ExecutionException;
         
         public class CreateCluster {
         
           public static void createCluster() throws IOException, InterruptedException {
             // TODO(developer): Replace these variables before running the sample.
             String projectId = "your-project-id";
             String region = "your-project-region";
             String clusterName = "your-cluster-name";
             createCluster(projectId, region, clusterName);
           }
         
           public static void createCluster(String projectId, String region, String clusterName)
               throws IOException, InterruptedException {
             String myEndpoint = String.format("%s-dataproc.googleapis.com:443", region);
         
             // Configure the settings for the cluster controller client.
             [ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html) clusterControllerSettings =
                 [ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html).newBuilder().setEndpoint(myEndpoint).build();
         
             // Create a cluster controller client with the configured settings. The client only needs to be
             // created once and can be reused for multiple requests. Using a try-with-resources
             // closes the client, but this can also be done manually with the .close() method.
             try ([ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html) clusterControllerClient =
                 [ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html).create(clusterControllerSettings)) {
               // Configure the settings for our cluster.
               [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) masterConfig =
                   [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html).newBuilder()
                       .[setMachineTypeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setMachineTypeUri_java_lang_String_)("n1-standard-2")
                       .[setNumInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setNumInstances_int_)(1)
                       .build();
               [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) workerConfig =
                   [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html).newBuilder()
                       .[setMachineTypeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setMachineTypeUri_java_lang_String_)("n1-standard-2")
                       .[setNumInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setNumInstances_int_)(2)
                       .build();
               [ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html) clusterConfig =
                   [ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html).newBuilder()
                       .[setMasterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.Builder.html#com_google_cloud_dataproc_v1_ClusterConfig_Builder_setMasterConfig_com_google_cloud_dataproc_v1_InstanceGroupConfig_)(masterConfig)
                       .setWorkerConfig(workerConfig)
                       .build();
               // Create the cluster object with the desired cluster config.
               [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) cluster =
                   [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html).newBuilder().setClusterName(clusterName).setConfig(clusterConfig).build();
         
               // Create the Cloud Dataproc cluster.
               OperationFuture<Cluster, ClusterOperationMetadata> createClusterAsyncRequest =
                   clusterControllerClient.[createClusterAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html#com_google_cloud_dataproc_v1_ClusterControllerClient_createClusterAsync_com_google_cloud_dataproc_v1_CreateClusterRequest_)(projectId, region, cluster);
               [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) response = createClusterAsyncRequest.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
         
               // Print out a success message.
               System.out.printf("Cluster created successfully: %s", response.[getClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html#com_google_cloud_dataproc_v1_Cluster_getClusterName__)());
         
             } catch (ExecutionException e) {
               System.err.println(String.format("Error executing createCluster: %s ", e.getMessage()));
             }
           }
         }




### Node.js

  1. [Install the client library.](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#installing_the_client_library)
  2. [Set up application default credentials.](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#setting_up_authentication)
  3. Run the code. See [Setting up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup).

**Note:** While specifying machine types is optional, it is recommended to explicitly set the master and worker machine types in your cluster configuration (for example, to `n4-standard-4`) to ensure consistent cost and performance. If omitted, default machine types are selected dynamically based on resource availability.
         
         const dataproc = require('[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)');
         
         // TODO(developer): Uncomment and set the following variables
         // projectId = 'YOUR_PROJECT_ID'
         // region = 'YOUR_CLUSTER_REGION'
         // clusterName = 'YOUR_CLUSTER_NAME'
         
         // Create a client with the endpoint set to the desired cluster region
         const client = new dataproc.v1.[ClusterControllerClient](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)({
           apiEndpoint: `${region}-dataproc.googleapis.com`,
           projectId: projectId,
         });
         
         async function createCluster() {
           // Create the cluster config
           const request = {
             projectId: projectId,
             region: region,
             cluster: {
               clusterName: clusterName,
               config: {
                 masterConfig: {
                   numInstances: 1,
                   machineTypeUri: 'n1-standard-2',
                 },
                 workerConfig: {
                   numInstances: 2,
                   machineTypeUri: 'n1-standard-2',
                 },
               },
             },
           };
         
           // Create the cluster
           const [operation] = await client.createCluster(request);
           const [response] = await operation.promise();
         
           // Output a success message
           console.log(`Cluster created successfully: ${response.clusterName}`);




### Python

  1. [Install the client library.](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#installing_the_client_library)
  2. [Set up application default credentials.](https://docs.cloud.google.com/managed-spark/docs/reference/libraries#setting_up_authentication)
  3. Run the code. See [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

**Note:** While specifying machine types is optional, it is recommended to explicitly set the master and worker machine types in your cluster configuration (for example, to `n4-standard-4`) to ensure consistent cost and performance. If omitted, default machine types are selected dynamically based on resource availability.
         
         from google.cloud import dataproc_v1 as dataproc
         
         
         def create_cluster(project_id, region, cluster_name):
             """This sample walks a user through creating a Cloud Dataproc cluster
             using the Python client library.
         
             Args:
                 project_id (string): Project to use for creating resources.
                 region (string): Region where the resources should live.
                 cluster_name (string): Name to use for creating a cluster.
             """
         
             # Create a client with the endpoint set to the desired cluster region.
             cluster_client = dataproc.ClusterControllerClient(
                 client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
             )
         
             # Create the cluster config.
             cluster = {
                 "project_id": project_id,
                 "cluster_name": cluster_name,
                 "config": {
                     "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-2"},
                     "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-2"},
                 },
             }
         
             # Create the cluster.
             operation = cluster_client.create_cluster(
                 request={"project_id": project_id, "region": region, "cluster": cluster}
             )
             result = operation.result()
         
             # Output a success message.
             print(f"Cluster created successfully: {result.cluster_name}")




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
