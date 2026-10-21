---
url: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-create-cluster/
title: Create cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:59.089675+00:00
---

# Create cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-create-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-spark/docs/samples)



#  Create cluster Stay organized with collections  Save and categorize content based on your preferences. 

Creates a Dataproc cluster.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster)
  * [Create a cluster](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster)
  * [Dataproc client libraries](https://docs.cloud.google.com/managed-spark/docs/reference/libraries)
  * [Use the Cloud Client Libraries for Python](https://docs.cloud.google.com/managed-spark/docs/tutorials/python-library-example)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataproc/apiv1?tab=doc). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/overview). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Node.js setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataproc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
