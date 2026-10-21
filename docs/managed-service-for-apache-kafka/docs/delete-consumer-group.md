---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-consumer-group/
title: Delete a Google Cloud Managed Service for Apache Kafka consumer group \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:59:32.536457+00:00
---

# Delete a Google Cloud Managed Service for Apache Kafka consumer group  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-consumer-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Delete a Google Cloud Managed Service for Apache Kafka consumer group Stay organized with collections  Save and categorize content based on your preferences. 

Deleting a consumer group removes a consumer group from your Managed Service for Apache Kafka cluster.

To delete a consumer group, you can use the Google Cloud console, the Google Cloud CLI, the client libraries, the Managed Kafka API, or the open source Apache Kafka APIs.

## Required roles and permissions to delete a consumer group

To get the permissions that you need to delete your consumer groups, ask your administrator to grant you the [Managed Kafka Consumer Group Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete your consumer groups. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete your consumer groups:

  * Delete consumer groups: `managedkafka.consumerGroups.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete a consumer group

When you delete a consumer group, the consumer offsets it stores are permanently lost. You are also unable to see the logs and metrics for the consumer groups in the console. However, the metrics and logs associated with the consumer group are retained and accessible using [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). Deleting a consumer group also does not delete the messages it has consumed. The messages are still available in the topics with which they were originally associated.

To delete a consumer group, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Cluster** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. From the list of clusters, click the cluster to which the consumer group that you want to delete belongs. 

The **Cluster details** page opens.

  3. Click the consumer group that you want to delete.
  4. In the **Consumer group details** page, click **Delete**.
  5. Confirm the operation.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [ `gcloud managed-kafka consumer-groups delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/delete) command:
         
         gcloud managed-kafka consumer-groups delete CONSUMER_GROUP_ID \
             --cluster=CLUSTER_ID \
             --location=LOCATION

This command permanently removes a consumer group from your Managed Service for Apache Kafka cluster.

Replace the following:

     * CONSUMER_GROUP_ID: The ID or name of the consumer group.

     * CLUSTER_ID: The ID or name of the cluster.

     * LOCATION: The location of the cluster.




### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func deleteConsumerGroup(w io.Writer, projectID, region, clusterID, consumerGroupID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	// consumerGroupID := "my-consumer-group"
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/clusters/%s", projectID, region, clusterID)
    	consumerGroupPath := fmt.Sprintf("%s/consumerGroups/%s", clusterPath, consumerGroupID)
    	req := &managedkafkapb.DeleteConsumerGroupRequest{
    		Name: consumerGroupPath,
    	}
    	if err := client.DeleteConsumerGroup(ctx, req); err != nil {
    		return fmt.Errorf("client.DeleteConsumerGroup got err: %w", err)
    	}
    	fmt.Fprint(w, "Deleted consumer group\n")
    	return nil
    }
    

### Java
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConsumerGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroupName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import java.io.IOException;
    
    public class DeleteConsumerGroup {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        String consumerGroupId = "my-consumer-group";
        deleteConsumerGroup(projectId, region, clusterId, consumerGroupId);
      }
    
      public static void deleteConsumerGroup(
          String projectId, String region, String clusterId, String consumerGroupId) throws Exception {
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create()) {
          // This operation is being handled synchronously.
          managedKafkaClient.deleteConsumerGroup(
              [ConsumerGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConsumerGroupName.html).of(projectId, region, clusterId, consumerGroupId));
          System.out.println("Deleted consumer group");
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaClient.getConsumerGroup got err: %s", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # cluster_id = "my-cluster"
    # consumer_group_id = "my-consumer-group"
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    consumer_group_path = client.[consumer_group_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_consumer_group_path)(
        project_id, region, cluster_id, consumer_group_id
    )
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[DeleteConsumerGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.DeleteConsumerGroupRequest.html)(
        name=consumer_group_path,
    )
    
    try:
        client.[delete_consumer_group](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_delete_consumer_group)(request=request)
        print("Deleted consumer group")
    except NotFound as e:
        print(f"Failed to delete consumer group {consumer_group_id} with error: {e.message}")
    

## What's next?

  * [View a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-consumer-group).
  * [List all consumer groups of a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-consumer-groups).
  * [Edit a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-consumer-group).



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
