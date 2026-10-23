---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connect-cluster/
title: View a Connect cluster \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:18.420205+00:00
---

# View a Connect cluster  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connect-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  View a Connect cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can view the details of a Connect cluster to learn more about its configuration details, including the name of the primary Google Cloud Managed Service for Apache Kafka cluster, the Connect cluster's state, resource allocation, network settings, and the connectors hosted by the Connect cluster.

To view your Connect clusters, you can use the Google Cloud console, the gcloud CLI, the client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to list Connect clusters.

## Required roles and permissions to view a Connect cluster

To get the permissions that you need to list your Connect clusters, ask your administrator to grant you the Managed Kafka Viewer(`roles/managedkafka.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list your Connect clusters. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list your Connect clusters:

  * Grant the list clusters permission on the specified location: `managedkafka.connectClusters.list`
  * Grant the get cluster details permission on the specified location: `managedkafka.connectClusters.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View a Connect cluster details

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster that you want to view.

  3. The Connect cluster page is displayed with four tabs:

     * **Resources** : Provides a focused view of the connectors running on your cluster, including their operational status and type.
     * **Configurations** : Displays the Connect cluster's essential properties and settings, such as the primary Kafka cluster, state, resource allocation, and network settings.
     * **Logs** : Provides a real-time stream of log entries from your Connect cluster for monitoring and troubleshooting.
     * **Monitoring** : Provides metrics to help you monitor the performance and resource utilization of your Connect cluster.



###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connect-clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/describe) command to view details of a Connect cluster:
         
         gcloud managed-kafka connect-clusters describe CONNECT_CLUSTER \
             --location=LOCATION
         

  3. Replace the following:

     * CONNECT_CLUSTER: The ID of the Connect cluster you want to view.
     * LOCATION: The location of the Connect cluster.



Example output:
    
    
    capacityConfig:
    memoryBytes: '3221225472'
    vcpuCount: '3'
    createTime: '2025-03-05T15:19:17.998009888Z'
    gcpConfig:
    accessConfig:
    networkConfigs:
    -   primarySubnet: projects/sample-project/regions/us-central1/subnetworks/default
    kafkaCluster: projects/sample-project/locations/us-central1/clusters/kafka-test
    name: projects/sample-project/locations/us-central1/connectClusters/my-connect-cluster
    state: ACTIVE
    updateTime: '2025-03-05T15:24:40.861655595Z'
    

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
    
    func getConnectCluster(w io.Writer, projectID, region, clusterID string, opts ...option.ClientOption) error {
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
    	req := &managedkafkapb.GetConnectClusterRequest{
    		Name: clusterPath,
    	}
    	cluster, err := client.GetConnectCluster(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetConnectCluster got err: %w", err)
    	}
    	fmt.Fprintf(w, "Got connect cluster: %#v\n", cluster)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html);
    import com.google.cloud.managedkafka.v1.[ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import java.io.IOException;
    
    public class GetConnectCluster {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-connect-cluster";
        getConnectCluster(projectId, region, clusterId);
      }
    
      public static void getConnectCluster(String projectId, String region, String clusterId)
          throws Exception {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          // This operation is being handled synchronously.
          [ConnectCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html) connectCluster = managedKafkaConnectClient
              .getConnectCluster([ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html).of(projectId, region, clusterId));
          System.out.println(connectCluster.getAllFields());
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.getConnectCluster got err: %s\n", 
              e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html)
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    
    client = ManagedKafkaConnectClient()
    
    cluster_path = client.[connect_cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connect_cluster_path)(project_id, region, connect_cluster_id)
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[GetConnectClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetConnectClusterRequest.html)(
        name=cluster_path,
    )
    
    try:
        cluster = client.[get_connect_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_get_connect_cluster)(request=request)
        print("Got Connect cluster:", cluster)
    except NotFound as e:
        print(f"Failed to get Connect cluster {connect_cluster_id} with error: {e}")
    

## Connect cluster details overview

The Connect cluster page is displayed with four tabs called **Resources** , **Configurations** , **Monitoring** , and **Logs**.

### Resources

The **Resources** tab on the Connect cluster page summarizes the types of connectors deployed and their operational status. The following information is displayed:

  * **Connectors table** : A table listing all connectors on the Connect cluster.

    * **Name** : The assigned name of each connector.

    * **State** : The current operational state of the connector.

    * **Connector type** : Indicates the type of connector, such as MirrorMaker 2.0 Source, BigQuery Sink, Cloud Storage Sink, or Pub/Sub Sink.

  * **Filter** : A search bar that you can use to filter connectors by their properties.




To monitor connector health, use the **Resources** tab.

### Configurations

The **Configurations** tab displays information about the cluster's state, resource allocation, network settings, and DNS configuration.

  * **Primary Kafka cluster** : Displays the name of the Managed Service for Apache Kafka cluster associated with this Connect cluster. The Connect cluster stores its configurations and offsets in the Managed Service for Apache Kafka cluster.

  * **State** : Shows the current state of the Connect cluster. Possible states include `Active`, `Creating`, `Deleting`, and `State_unspecified`.

  * **Region** : Indicates the Connect cluster's region.

  * **vCPUs** : Shows the number of virtual CPUs allocated to the Connect cluster. A higher vCPU count increases cluster processing capacity.

  * **Memory** : Shows the Connect cluster's total provisioned memory.

  * **Labels** : Shows the labels attached to the Connect cluster.

  * **Secret resources** : Lists the secrets associated with the Connect cluster.

  * **Subnetworks** : Lists the subnetworks associated with the Connect cluster. The table includes columns for Name, Region, and Project.

  * **DNS names** : Displays any custom DNS names configured for the Connect cluster. If no custom DNS names are configured, the table is empty.




### Monitoring

The **Monitoring** tab provides metrics that help you understand the performance and resource utilization of your connectors. Metrics include:

  * **Worker CPU usage:** Total CPU usage, in vCPU seconds, for each worker. This metric helps identify resource constraints.

  * **Worker memory usage:** Current memory usage, in bytes, for each worker. This metric helps prevent out-of-memory errors.

  * **Connector incoming byte rate:** Average incoming byte rate per second, from client connections, for each connector. This metric helps assess data ingestion rates.

  * **Connector outgoing byte rate:** Average outgoing byte rate per second, to servers, from client connections, for each connector. This metric helps monitor data delivery rates.




### Logs

The **Logs** tab provides a real-time stream of log entries from your Connect cluster. Use this tab to monitor connector health, activity, and troubleshoot issues. These features help you effectively monitor and debug your Connect cluster:

  * **Filter by Severity:** Filter log entries by severity level to quickly pinpoint critical issues.

  * **Search:** Search log entries for specific keywords or phrases to find events related to a particular connector or task.

  * **Timestamps:** Timestamps on each log entry help track event sequences and identify when actions occurred.

  * **Summary:** Log entries provide details about various events, such as connector startup and shutdown, task execution, and data processing.




## What's next?

  * [List all Connect clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/list-connect-cluster)

  * [Update a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connect-cluster)

  * [Delete a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/delete-connect-cluster)

  * [An overview of connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
