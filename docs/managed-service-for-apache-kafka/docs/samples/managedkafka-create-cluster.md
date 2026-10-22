---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples/managedkafka-create-cluster/
title: Create a Kafka cluster \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:53.073089+00:00
---

# Create a Kafka cluster  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples/managedkafka-create-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/samples)



#  Create a Kafka cluster Stay organized with collections  Save and categorize content based on your preferences. 

Create a Kafka cluster

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a Google Cloud Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster)
  * [Managed Service for Apache Kafka client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Managed Service for Apache Kafka quickstart using client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [Managed Service for Apache Kafka Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1). 

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func createCluster(w io.Writer, projectID, region, clusterID, subnet string, cpu, memoryBytes int64, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	// subnet := "projects/my-project-id/regions/us-central1/subnetworks/default"
    	// cpu := 3
    	// memoryBytes := 3221225472
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	locationPath := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    	clusterPath := fmt.Sprintf("%s/clusters/%s", locationPath, clusterID)
    
    	// Memory must be between 1 GiB and 8 GiB per CPU.
    	capacityConfig := &managedkafkapb.CapacityConfig{
    		VcpuCount:   cpu,
    		MemoryBytes: memoryBytes,
    	}
    	var networkConfig []*managedkafkapb.NetworkConfig
    	networkConfig = append(networkConfig, &managedkafkapb.NetworkConfig{
    		Subnet: subnet,
    	})
    	platformConfig := &managedkafkapb.Cluster_GcpConfig{
    		GcpConfig: &managedkafkapb.GcpConfig{
    			AccessConfig: &managedkafkapb.AccessConfig{
    				NetworkConfigs: networkConfig,
    			},
    		},
    	}
    	rebalanceConfig := &managedkafkapb.RebalanceConfig{
    		Mode: managedkafkapb.[RebalanceConfig_AUTO_REBALANCE_ON_SCALE_UP](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1/managedkafkapb.html#cloud_google_com_go_managedkafka_apiv1_managedkafkapb_RebalanceConfig_MODE_UNSPECIFIED_RebalanceConfig_NO_REBALANCE_RebalanceConfig_AUTO_REBALANCE_ON_SCALE_UP),
    	}
    	cluster := &managedkafkapb.Cluster{
    		Name:            clusterPath,
    		CapacityConfig:  capacityConfig,
    		PlatformConfig:  platformConfig,
    		RebalanceConfig: rebalanceConfig,
    	}
    
    	req := &managedkafkapb.CreateClusterRequest{
    		Parent:    locationPath,
    		ClusterId: clusterID,
    		Cluster:   cluster,
    	}
    	op, err := client.CreateCluster(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateCluster got err: %w", err)
    	}
    	// The duration of this operation can vary considerably, typically taking 10-40 minutes.
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("op.Wait got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created cluster: %s\n", resp.Name)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Kafka quickstart using client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [Managed Service for Apache Kafka Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview). 

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.api.gax.longrunning.[OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html);
    import com.google.api.gax.longrunning.[OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.api.gax.retrying.[RetryingFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryingFuture.html);
    import com.google.api.gax.retrying.[TimedRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedRetryAlgorithm.html);
    import com.google.cloud.managedkafka.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.AccessConfig.html);
    import com.google.cloud.managedkafka.v1.[CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html);
    import com.google.cloud.managedkafka.v1.[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html);
    import com.google.cloud.managedkafka.v1.[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateClusterRequest.html);
    import com.google.cloud.managedkafka.v1.[GcpConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.GcpConfig.html);
    import com.google.cloud.managedkafka.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaSettings.html);
    import com.google.cloud.managedkafka.v1.[NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.NetworkConfig.html);
    import com.google.cloud.managedkafka.v1.[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.OperationMetadata.html);
    import com.google.cloud.managedkafka.v1.[RebalanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RebalanceConfig.html);
    import java.time.Duration;
    import java.util.concurrent.ExecutionException;
    
    public class CreateCluster {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        String subnet = "my-subnet"; // e.g. projects/my-project/regions/my-region/subnetworks/my-subnet
        int cpu = 3;
        long memoryBytes = 3221225472L; // 3 GiB
        createCluster(projectId, region, clusterId, subnet, cpu, memoryBytes);
      }
    
      public static void createCluster(
          String projectId, String region, String clusterId, String subnet, int cpu, long memoryBytes)
          throws Exception {
        [CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html) capacityConfig =
            [CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html).newBuilder().[setVcpuCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.Builder.html#com_google_cloud_managedkafka_v1_CapacityConfig_Builder_setVcpuCount_long_)(cpu).[setMemoryBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.Builder.html#com_google_cloud_managedkafka_v1_CapacityConfig_Builder_setMemoryBytes_long_)(memoryBytes).build();
        [NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.NetworkConfig.html) networkConfig = [NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.NetworkConfig.html).newBuilder().[setSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.NetworkConfig.Builder.html#com_google_cloud_managedkafka_v1_NetworkConfig_Builder_setSubnet_java_lang_String_)(subnet).build();
        [GcpConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.GcpConfig.html) gcpConfig =
            [GcpConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.GcpConfig.html).newBuilder()
                .setAccessConfig([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.AccessConfig.html).newBuilder().addNetworkConfigs(networkConfig).build())
                .build();
        [RebalanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RebalanceConfig.html) rebalanceConfig =
            [RebalanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RebalanceConfig.html).newBuilder()
                .[setMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RebalanceConfig.Builder.html#com_google_cloud_managedkafka_v1_RebalanceConfig_Builder_setMode_com_google_cloud_managedkafka_v1_RebalanceConfig_Mode_)([RebalanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RebalanceConfig.html).Mode.AUTO_REBALANCE_ON_SCALE_UP)
                .build();
        [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html) cluster =
            [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html).newBuilder()
                .setCapacityConfig(capacityConfig)
                .setGcpConfig(gcpConfig)
                .[setRebalanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.Builder.html#com_google_cloud_managedkafka_v1_Cluster_Builder_setRebalanceConfig_com_google_cloud_managedkafka_v1_RebalanceConfig_)(rebalanceConfig)
                .build();
    
        // Create the settings to configure the timeout for polling operations
        [ManagedKafkaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaSettings.html).Builder settingsBuilder = [ManagedKafkaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaSettings.html).newBuilder();
        [TimedRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedRetryAlgorithm.html) timedRetryAlgorithm = [OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html).create(
            [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                .[setTotalTimeoutDuration](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeoutDuration_java_time_Duration_)(Duration.ofHours(1L))
                .build());
        settingsBuilder.createClusterOperationSettings()
            .setPollingAlgorithm(timedRetryAlgorithm);
    
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create(
            settingsBuilder.build())) {
    
          [CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateClusterRequest.html) request =
              [CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateClusterRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html).of(projectId, region).toString())
                  .[setClusterId](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateClusterRequest.Builder.html#com_google_cloud_managedkafka_v1_CreateClusterRequest_Builder_setClusterId_java_lang_String_)(clusterId)
                  .setCluster(cluster)
                  .build();
    
          // The duration of this operation can vary considerably, typically taking between 10-40
          // minutes.
          OperationFuture<Cluster, OperationMetadata> future =
              managedKafkaClient.[createClusterOperationCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html#com_google_cloud_managedkafka_v1_ManagedKafkaClient_createClusterOperationCallable__)().futureCall(request);
    
          // Get the initial LRO and print details.
          [OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html) operation = future.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.printf("Cluster creation started. Operation name: %s\nDone: %s\nMetadata: %s\n",
              operation.[getName](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_getName__)(),
              operation.[isDone](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_isDone__)(),
              future.getMetadata().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().toString());
    
          while (!future.isDone()) {
            // The pollingFuture gives us the most recent status of the operation
            RetryingFuture<OperationSnapshot> pollingFuture = future.getPollingFuture();
            [OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html) currentOp = pollingFuture.[getAttemptResult](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryingFuture.html#com_google_api_gax_retrying_RetryingFuture_getAttemptResult__)().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
            System.out.printf("Polling Operation:\nName: %s\n Done: %s\n",
                currentOp.[getName](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_getName__)(),
                currentOp.[isDone](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_isDone__)());
          }
    
          // NOTE: future.get() blocks completion until the operation is complete (isDone =  True)
          [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.printf("Created cluster: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html#com_google_cloud_managedkafka_v1_Cluster_getName__)());
        } catch (ExecutionException e) {
          System.err.printf("managedKafkaClient.createCluster got err: %s", e.getMessage());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Kafka quickstart using client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [Managed Service for Apache Kafka Python API reference documentation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest). 

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # cluster_id = "my-cluster"
    # subnet = "projects/my-project-id/regions/us-central1/subnetworks/default"
    # cpu = 3
    # memory_bytes = 3221225472
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    cluster = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Cluster.html)()
    cluster.name = client.[cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_cluster_path)(project_id, region, cluster_id)
    cluster.capacity_config.vcpu_count = cpu
    cluster.capacity_config.memory_bytes = memory_bytes
    cluster.gcp_config.access_config.network_configs = [
        [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[NetworkConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.NetworkConfig.html)(subnet=subnet)
    ]
    cluster.rebalance_config.mode = (
        [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[RebalanceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RebalanceConfig.html).[Mode](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RebalanceConfig.Mode.html).AUTO_REBALANCE_ON_SCALE_UP
    )
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[CreateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateClusterRequest.html)(
        parent=client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_common_location_path)(project_id, region),
        cluster_id=cluster_id,
        cluster=cluster,
    )
    
    try:
        operation = client.[create_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_create_cluster)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        # The duration of this operation can vary considerably, typically taking 10-40 minutes.
        # We can set a timeout of 3000s (50 minutes).
        response = operation.result(timeout=3000)
        print("Created cluster:", response)
    except GoogleAPICallError as e:
        print(f"The operation failed with error: {e.message}")
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_managed_kafka_cluster" "default" {
      project    = data.google_project.default.project_id # Replace this with your project ID in quotes
      cluster_id = "my-cluster-id"
      location   = "us-central1"
      capacity_config {
        vcpu_count   = 3
        memory_bytes = 3221225472
      }
      gcp_config {
        access_config {
          network_configs {
            subnet = google_compute_subnetwork.default.id
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=apachekafkaforbigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
