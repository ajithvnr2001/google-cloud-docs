---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster/
title: Update a Google Cloud Managed Service for Apache Kafka cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:32.149920+00:00
---

# Update a Google Cloud Managed Service for Apache Kafka cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Update a Google Cloud Managed Service for Apache Kafka cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can edit a Google Cloud Managed Service for Apache Kafka cluster to update properties such as the cluster size, including vCPU count and memory, the list of connected subnets, the allowed source IP ranges for public clusters, the automatic rebalancing configuration, and the mTLS configuration.

To edit a cluster, you can use the Google Cloud console, the Google Cloud CLI, the client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to update a cluster.

Updating certain properties, such as vCPU count and memory, might require the service to restart the cluster. The service restarts the cluster one broker at a time. During this process, requests to individual brokers might fail, but these failures are transient. Commonly used client libraries automatically handle these errors.

## Required roles and permissions

To get the permissions that you need to update a cluster, ask your administrator to grant you the [Managed Kafka Cluster Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to update a cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to update a cluster:

  * Edit a cluster: `managedkafka.clusters.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Resize a cluster

If you update a cluster's vCPU count or memory, the following rules apply:

  * The cluster's overall vCPU-to-memory ratio must always remain between 1:1 and 1:8.

  * There must be at least 1 vCPU and 1 GiB of memory for each existing broker. The number of brokers never decreases.

  * If the cluster has a [custom disk configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size#custom-disk-configuration), the update must meet the [disk configuration requirements](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size#disk-configuration-requirements) for local storage.

  * If you upscale, the average vCPU and memory per broker can't decrease by more than 10% compared to the averages before the update. For example, if you try to upscale a cluster from 45 vCPUs (3 brokers) to 48 vCPUs (4 brokers), the average vCPU per broker decreases from 15 to 12, which is a 20% reduction, exceeding the 10% limit.

If you need to decrease the vCPU count by more than 10%, we recommend reducing it in several stages. After each update, monitor resource utilization, and rebalance partitions if needed.

However, if you are confident that your brokers will have enough capacity after the update, you can disable this check by running the [`gcloud managed-kafka clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update) command with the `allow_broker_downscale_on_cluster_upscale=true` flag. This flag signals that you accept the potential performance risk.




For more information, see [Update the cluster size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size#update-size).

## Public cluster configuration

You can enable or disable public access for an existing cluster, as well as add or remove allowed source IP ranges. For more information about the requirements and rules for allowed source IP ranges, see [Public clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#public-cluster).

**Caution:** To protect your cluster, allow access from only trusted external IP ranges. Don't expose your cluster to untrusted ranges. 

Managed Service for Apache Kafka uses [Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall/docs/about-firewalls) to restrict access to public clusters. Removing allowed source IP ranges or disabling public access applies only to new connections. For more information, see [effects on existing traffic](https://docs.cloud.google.com/firewall/docs/firewalls#effects_on_existing_traffic).

## Edit a cluster

To edit a cluster, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.



[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  1. From the list of clusters, click the cluster whose properties you want to edit.



The console displays the cluster details page.

  1. On the cluster details page, click **Edit**.

  2. Edit the properties as required. You can edit the following properties of a cluster from the console:

     * Memory
     * vCPUs
     * Subnet
     * Rebalancing configuration
     * mTLS configuration
     * Labels
  3. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Before using any of the command data below, make the following replacements: 

     * `PROJECT_ID`: the project ID. 
     * `LOCATION`: the location of the cluster. 
     * `CLUSTER_ID`: the ID of the cluster. 
     * `CPU_COUNT`: the number of vCPUs for the cluster. 
     * `MEMORY`: the amount of memory for the cluster. Example: `10GiB`. 
     * `SUBNET_ID`: the subnet ID of the subnet to connect to. Example: `default`. 
     * `LABELS`: the labels to associate with the cluster. 
     * `ALLOWED_SOURCE_IP_RANGES`: the allowed source IPv4 CIDR ranges for public cluster internet access. 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters update CLUSTER_ID \
        --location=LOCATION \
        --cpu=CPU_COUNT \
        --memory=MEMORY \
        --subnets=projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID \
        --auto-rebalance \
        --labels=LABELS \
        --public-cluster \
        --allowed-source-ip-ranges=ALLOWED_SOURCE_IP_RANGES

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters update CLUSTER_ID `
        --location=LOCATION `
        --cpu=CPU_COUNT `
        --memory=MEMORY `
        --subnets=projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID `
        --auto-rebalance `
        --labels=LABELS `
        --public-cluster `
        --allowed-source-ip-ranges=ALLOWED_SOURCE_IP_RANGES

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters update CLUSTER_ID ^
        --location=LOCATION ^
        --cpu=CPU_COUNT ^
        --memory=MEMORY ^
        --subnets=projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID ^
        --auto-rebalance ^
        --labels=LABELS ^
        --public-cluster ^
        --allowed-source-ip-ranges=ALLOWED_SOURCE_IP_RANGES

You should receive a response similar to the following:
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.managedkafka.v1.OperationMetadata
      apiVersion: v1
      createTime: 'CREATE_TIME'
      requestedCancellation: false
      target: projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID
      verb: update
    name: projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

     * To disable public access, use the `--no-public-cluster` flag.
     * If you use the `--async` flag with your command, the system sends the update request and immediately returns a response, without waiting for the operation to complete. With the `--async` flag, you can continue with other tasks while the cluster update happens in the background. If you don't use the `--async` flag, the system waits for the operation to complete before returning a response. You must wait until the cluster is fully updated before you can continue with other tasks.



###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster. 
  * `CLUSTER_ID`: the ID of the cluster. 
  * `UPDATE_MASK`: which fields to update, as a comma-separated list of fully qualified names. Example: `capacityConfig.vcpuCount,capacityConfig.memoryBytes`
  * `CPU_COUNT`: the number of vCPUs for the cluster. 
  * `MEMORY`: the amount of memory for the cluster, in bytes. Example: `3221225472`. 
  * `SUBNET_ID`: subnet ID of the subnet to connect to. Example: `default`. 



HTTP method and URL: 
    
    
    PATCH https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?updateMask=UPDATE_MASK

Request JSON body: 
    
    
    {
      "capacityConfig": {
        "vcpuCount": CPU_COUNT,
        "memoryBytes": MEMORY
      },
      "gcpConfig": {
        "accessConfig": {
          "networkConfigs": [
            {
              "subnet": "projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID"
            }
          ]
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?updateMask=UPDATE_MASK"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?updateMask=UPDATE_MASK" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.managedkafka.v1.OperationMetadata",
        "createTime": "CREATE_TIME",
        "target": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

In the request body, include only the fields that you are updating, as specified in the UPDATE_MASK query parameter.

  * To add a subnet, append a new entry to `networkConfigs` in the following format: `projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID`. Example: `projects/sample-project/regions/us-central1/subnetworks/default`.
  * To enable public access or update the allowed source IP ranges, include `gcpConfig.accessConfig.publicClusterConfig` in the UPDATE_MASK query parameter and specify the `allowedSourceIpRanges` array in the request body. Example request body:
        
        {
          "gcpConfig": {
            "accessConfig": {
              "publicClusterConfig": {
                "allowedSourceIpRanges": [
                  "203.0.113.0/24"
                ]
              }
            }
          }
        }
        

  * To disable public access, include `gcpConfig.accessConfig.publicClusterConfig` in the UPDATE_MASK query parameter and pass an empty JSON object `{}` in the request body (or omit `publicClusterConfig`). Example request body:
        
        {}
        




### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func updateCluster(w io.Writer, projectID, region, clusterID string, memory int64, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	// memoryBytes := 4221225472
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/clusters/%s", projectID, region, clusterID)
    	capacityConfig := &managedkafkapb.CapacityConfig{
    		MemoryBytes: memory,
    	}
    	cluster := &managedkafkapb.Cluster{
    		Name:           clusterPath,
    		CapacityConfig: capacityConfig,
    	}
    	paths := []string{"capacity_config.memory_bytes"}
    	updateMask := &fieldmaskpb.FieldMask{
    		Paths: paths,
    	}
    
    	req := &managedkafkapb.UpdateClusterRequest{
    		UpdateMask: updateMask,
    		Cluster:    cluster,
    	}
    	op, err := client.UpdateCluster(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.UpdateCluster got err: %w", err)
    	}
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("op.Wait got err: %w", err)
    	}
    	fmt.Fprintf(w, "Updated cluster: %#v\n", resp)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.api.gax.longrunning.[OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html);
    import com.google.api.gax.longrunning.[OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.api.gax.retrying.[TimedRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedRetryAlgorithm.html);
    import com.google.cloud.managedkafka.v1.[CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html);
    import com.google.cloud.managedkafka.v1.[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html);
    import com.google.cloud.managedkafka.v1.[ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaSettings.html);
    import com.google.cloud.managedkafka.v1.[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.OperationMetadata.html);
    import com.google.cloud.managedkafka.v1.[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateClusterRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.time.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.util.concurrent.ExecutionException;
    
    public class UpdateCluster {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        long memoryBytes = 25769803776L; // 24 GiB
        updateCluster(projectId, region, clusterId, memoryBytes);
      }
    
      public static void updateCluster(
          String projectId, String region, String clusterId, long memoryBytes) throws Exception {
        [CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html) capacityConfig = [CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html).newBuilder().[setMemoryBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.Builder.html#com_google_cloud_managedkafka_v1_CapacityConfig_Builder_setMemoryBytes_long_)(memoryBytes).build();
        [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html) cluster =
            [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html).newBuilder()
                .setName([ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html).of(projectId, region, clusterId).toString())
                .setCapacityConfig(capacityConfig)
                .build();
        [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("capacity_config.memory_bytes").build();
    
        // Create the settings to configure the timeout for polling operations
        [ManagedKafkaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaSettings.html).Builder settingsBuilder = [ManagedKafkaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaSettings.html).newBuilder();
        [TimedRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedRetryAlgorithm.html) timedRetryAlgorithm = [OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html).create(
            [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                .[setTotalTimeoutDuration](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeoutDuration_java_time_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofHours(1L))
                .build());
        settingsBuilder.updateClusterOperationSettings()
            .setPollingAlgorithm(timedRetryAlgorithm);
    
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create(
            settingsBuilder.build())) {
          [UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateClusterRequest.html) request =
              [UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.UpdateClusterRequest.html).newBuilder().setUpdateMask(updateMask).setCluster(cluster).build();
          OperationFuture<Cluster, OperationMetadata> future =
              managedKafkaClient.[updateClusterOperationCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html#com_google_cloud_managedkafka_v1_ManagedKafkaClient_updateClusterOperationCallable__)().futureCall(request);
    
          // Get the initial LRO and print details. CreateCluster contains sample code for polling logs.
          [OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html) operation = future.getInitialFuture().get();
          System.out.printf("Cluster update started. Operation name: %s\nDone: %s\nMetadata: %s\n",
              operation.[getName](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_getName__)(),
              operation.[isDone](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_isDone__)(),
              future.getMetadata().get().toString());
    
          [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html) response = future.get();
          System.out.printf("Updated cluster: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html#com_google_cloud_managedkafka_v1_Cluster_getName__)());
        } catch (ExecutionException e) {
          System.err.printf("managedKafkaClient.updateCluster got err: %s", e.getMessage());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    from google.protobuf import field_mask_pb2
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # cluster_id = "my-cluster"
    # memory_bytes = 4295000000
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    cluster = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Cluster.html)()
    cluster.name = client.[cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_cluster_path)(project_id, region, cluster_id)
    cluster.capacity_config.memory_bytes = memory_bytes
    update_mask = field_mask_pb2.FieldMask()
    update_mask.paths.append("capacity_config.memory_bytes")
    
    # For a list of editable fields, one can check https://cloud.google.com/managed-kafka/docs/create-cluster#properties.
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[UpdateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateClusterRequest.html)(
        update_mask=update_mask,
        cluster=cluster,
    )
    
    try:
        operation = client.[update_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_update_cluster)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        response = operation.result()
        print("Updated cluster:", response)
    except GoogleAPICallError as e:
        print(f"The operation failed with error: {e.message}")
    

## Limitations

After you create a Managed Service for Apache Kafka cluster, you can't update the following properties:

  * The cluster name
  * The cluster location
  * The encryption type



Although you can't change the encryption type, you can [rotate encryption keys](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption#rotate-keys).

## What's next?

  * [Monitor your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster).

  * [Plan the size of your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size).

  * [Create a topic within your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic).

  * [View your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster).

  * [Delete your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-cluster).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
