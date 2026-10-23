---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/delete-connect-cluster/
title: Delete a Connect cluster \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:27.049489+00:00
---

# Delete a Connect cluster  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/delete-connect-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Delete a Connect cluster Stay organized with collections  Save and categorize content based on your preferences. 

Deleting a Connect cluster erases all associated data, including connector configurations stored in its primary Kafka cluster. This action is irreversible.

To delete a Connect cluster, you can use the Google Cloud console, the gcloud CLI, the client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to delete a Connect cluster.

## Required roles and permissions to delete a Connect cluster

To get the permissions that you need to delete a Connect cluster, ask your administrator to grant you the [Managed Kafka Connect Cluster Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete a Connect cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete a Connect cluster:

  * Grant the delete a Connect cluster permission on the Connect cluster: `managedkafka.connectClusters.delete`
  * Grant the list Connect clusters permission on the specified location. This permission is only required for deleting a Connect cluster using the Google Cloud console: `managedkafka.connectClusters.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete a Connect cluster

  * **Understand data loss implications:** Deleting a Connect cluster erases all data stored _within the Connect cluster itself_. This includes the following:

    * Connectors and their configurations

    * Any other data directly managed by the Connect cluster

Deleting a Connect cluster does _not_ delete data in your source or target Kafka clusters. If you're using a source connector to move data to a Kafka topic, deleting the Connect cluster does not delete the data that is already published to that Kafka topic. Similarly, deleting a Connect cluster does not delete the Kafka clusters that the Connect cluster is associated with.

  * **Plan for service disruption:** Any applications or services depending on data read or written by the Connect cluster might experience disruptions. Plan for this service disruption before deleting the cluster.

  * **Review billing implications:** You stop incurring charges for the cluster after you delete it. You might still be billed for resources used until deletion.

  * **Expect asynchronous operation:** Cluster deletion is asynchronous by default. The command returns immediately, and you can track the deletion progress separately.




###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Select the Connect cluster that you want to delete. You can select more than one.

  3. Click **Delete**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connect-clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/delete) command to delete Connect clusters:
         
         gcloud managed-kafka connect-clusters delete CONNECT_CLUSTER \
             --location=LOCATION [--async]
         

Replace the following:

     * CONNECT_CLUSTER: The ID of the Connect cluster you want to delete.
     * LOCATION: The location of the Connect cluster.

The following flag is optional:

     * `--async`: Return immediately, without waiting for the operation in progress to complete.



### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func deleteConnectCluster(w io.Writer, projectID, region, clusterID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-connect-cluster"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s", projectID, region, clusterID)
    	req := &managedkafkapb.DeleteConnectClusterRequest{
    		Name: clusterPath,
    	}
    	op, err := client.DeleteConnectCluster(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.DeleteConnectCluster got err: %w", err)
    	}
    	err = op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("op.Wait got err: %w", err)
    	}
    	fmt.Fprint(w, "Deleted connect cluster\n")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.api.gax.longrunning.[OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html);
    import com.google.api.gax.longrunning.[OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html);
    import com.google.api.gax.[retrying](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Callables.html#com_google_api_gax_rpc_Callables__RequestT_ResponseT_retrying_com_google_api_gax_rpc_ServerStreamingCallable_RequestT_ResponseT__com_google_api_gax_rpc_ServerStreamingCallSettings_RequestT_ResponseT__com_google_api_gax_rpc_ClientContext_).[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.api.gax.[retrying](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Callables.html#com_google_api_gax_rpc_Callables__RequestT_ResponseT_retrying_com_google_api_gax_rpc_ServerStreamingCallable_RequestT_ResponseT__com_google_api_gax_rpc_ServerStreamingCallSettings_RequestT_ResponseT__com_google_api_gax_rpc_ClientContext_).[TimedRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedRetryAlgorithm.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html);
    import com.google.cloud.managedkafka.v1.[DeleteConnectClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.DeleteConnectClusterRequest.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectSettings.html);
    import com.google.cloud.managedkafka.v1.[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.OperationMetadata.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.io.IOException;
    import java.time.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    
    public class DeleteConnectCluster {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-connect-cluster";
        deleteConnectCluster(projectId, region, clusterId);
      }
    
      public static void deleteConnectCluster(String projectId, String region, String clusterId)
          throws Exception {
    
        // Create the settings to configure the timeout for polling operations
        [ManagedKafkaConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectSettings.html).Builder settingsBuilder = [ManagedKafkaConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectSettings.html).newBuilder();
        [TimedRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedRetryAlgorithm.html) timedRetryAlgorithm = [OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html).create(
            [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                .[setTotalTimeoutDuration](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeoutDuration_java_time_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofHours(1L))
                .build());
        settingsBuilder.deleteConnectClusterOperationSettings()
            .[setPollingAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.Builder.html#com_google_api_gax_rpc_OperationCallSettings_Builder_setPollingAlgorithm_com_google_api_gax_retrying_TimedRetryAlgorithm_)(timedRetryAlgorithm);
    
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create(
            settingsBuilder.build())) {
          [DeleteConnectClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.DeleteConnectClusterRequest.html) request = [DeleteConnectClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.DeleteConnectClusterRequest.html).newBuilder()
              .setName([ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html).of(projectId, region, clusterId).toString())
              .build();
          OperationFuture<Empty, OperationMetadata> future = managedKafkaConnectClient
              .[deleteConnectClusterOperationCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html#com_google_cloud_managedkafka_v1_ManagedKafkaConnectClient_deleteConnectClusterOperationCallable__)().futureCall(request);
    
          // Get the initial LRO and print details. CreateConnectCluster contains sample
          // code for polling logs.
          [OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html) operation = future.getInitialFuture().get();
          System.out.printf(
              "Connect cluster deletion started. Operation name: %s\nDone: %s\nMetadata: %s\n",
              operation.[getName](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_getName__)(),
              operation.[isDone](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_isDone__)(),
              future.getMetadata().get().toString());
    
          future.get();
          System.out.println("Deleted connect cluster");
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.deleteConnectCluster got err: %s\n", 
              e.getMessage());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html),
    )
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    
    connect_client = ManagedKafkaConnectClient()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[DeleteConnectClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.DeleteConnectClusterRequest.html)(
        name=connect_client.[connect_cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connect_cluster_path)(project_id, region, connect_cluster_id),
    )
    
    try:
        operation = connect_client.[delete_connect_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_delete_connect_cluster)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        operation.result()
        print("Deleted Connect cluster")
    except GoogleAPICallError as e:
        print(f"The operation failed with error: {e}")
    

## What's next?

  * [List all Connect clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connect-cluster)

  * [View details about a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connect-cluster)

  * [Update a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connect-cluster)

  * [An overview of connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
