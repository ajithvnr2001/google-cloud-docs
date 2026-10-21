---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster/
title: View a Google Cloud Managed Service for Apache Kafka cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:21.485834+00:00
---

# View a Google Cloud Managed Service for Apache Kafka cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  View a Google Cloud Managed Service for Apache Kafka cluster Stay organized with collections  Save and categorize content based on your preferences. 

To view a cluster, you can use the Google Cloud console, the Google Cloud CLI, the client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to view a cluster.

## Required roles and permissions to view a cluster

To get the permissions that you need to view a cluster, ask your administrator to grant you the [Managed Kafka Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view a cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view a cluster:

  * List clusters: `managedkafka.clusters.list`
  * Get cluster details: `managedkafka.clusters.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View a cluster

To view a cluster, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

The clusters you created in a project are listed.

  2. To view a specific cluster, click a cluster name.

  3. The cluster details page opens. This page has the following tabs:

     * **Resources** : Displays the list of topics and consumer groups associated with the cluster.
     * **Access control** : Displays the [ACL entries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls) for the cluster.
     * **Configurations** : Displays the configuration of the cluster, including the list of subnets associated with the cluster.
     * **Monitoring** : Displays the monitoring alerts associated with the cluster.
     * **Logs** : Displays the logs related to clusters from Logs Explorer.
     * **Sources** : Provides shortcuts for creating [Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview) source connectors or generating [synthetic test data](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-synthetic-data).
     * **Sinks** : Provides shortcuts for creating Kafka Connect sink connectors.



###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Before using any of the command data below, make the following replacements: 

     * `PROJECT_ID`: the project ID. 
     * `LOCATION`: the location of the cluster. 
     * `CLUSTER_ID`: the ID of the cluster. 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters describe CLUSTER_ID \
        --location=LOCATION \
        --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters describe CLUSTER_ID `
        --location=LOCATION `
        --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters describe CLUSTER_ID ^
        --location=LOCATION ^
        --project=PROJECT_ID

You should receive a response similar to the following:
    
    bootstrapAddress: bootstrap.CLUSTER_ID.LOCATION.managedkafka.PROJECT_ID.cloud.goog:9092
    bootstrapAddressMTLS: bootstrap.CLUSTER_ID.LOCATION.managedkafka.PROJECT_ID.cloud.goog:9192
    brokerCapacityConfig: {}
    capacityConfig:
      memoryBytes: 'MEMORY'
      vcpuCount: 'CPU_COUNT'
    createTime: 'CREATE_TIME'
    gcpConfig:
      accessConfig:
        networkConfigs:
        - subnet: projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID
        publicClusterConfig:
          allowedSourceIpRanges:
          - 203.0.113.5/32
    labels:
      goog-terraform-provisioned: 'true'
    name: projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID
    publicClusterDetails:
      discoveryDnsRecords:
      - discovery-1.CLUSTER_ID.LOCATION.managedkafka.PROJECT_ID.cloud.goog
      externalIpAddresses:
      - 203.0.113.1
      - 203.0.113.2
      - 203.0.113.3
      - 203.0.113.4
    rebalanceConfig:
      mode: AUTO_REBALANCE_ON_SCALE_UP
    satisfiesPzi: false
    satisfiesPzs: false
    state: ACTIVE
    tlsConfig:
      trustConfig: {}
    updateOptions: {}
    updateTime: 'UPDATE_TIME'
    




###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster. 
  * `CLUSTER_ID`: the ID of the cluster. 
  * `CLUSTER_VIEW`: the amount of metadata to return. Specify one of the following values:

    * `CLUSTER_VIEW_BASIC`: Return the basic metadata for the cluster.
    * `CLUSTER_VIEW_FULL`: Return all of the metadata for the cluster, including information about the cluster's brokers and the Kafka version number that the cluster is running.

If not specified, the method defaults to `CLUSTER_VIEW_BASIC`.




HTTP method and URL: 
    
    
    GET https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID",
      "createTime": "CREATE_TIME",
      "updateTime": "UPDATE_TIME",
      "capacityConfig": {
        "vcpuCount": "CPU_COUNT",
        "memoryBytes": "MEMORY"
      },
      "rebalanceConfig": {},
      "gcpConfig": {
        "accessConfig": {
          "networkConfigs": [
            {
              "subnet": "projects/PROJECT_ID/locations/LOCATION/subnetworks/SUBNET_ID"
            }
          ],
          "publicClusterConfig": {
            "allowedSourceIpRanges": [
              "203.0.113.5/32"
            ]
          }
        }
      },
      "state": "ACTIVE",
      "satisfiesPzi": false,
      "satisfiesPzs": false,
      "tlsConfig": {
        "trustConfig": {}
      },
      "updateOptions": {},
      "publicClusterDetails": {
        "discoveryDnsRecords": [
          "discovery-1.CLUSTER_ID.LOCATION.managedkafka.PROJECT_ID.cloud.goog"
        ],
        "externalIpAddresses": [
          "203.0.113.1",
          "203.0.113.2",
          "203.0.113.3",
          "203.0.113.4"
        ]
      }
    }
    

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
    
    func getCluster(w io.Writer, projectID, region, clusterID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-cluster"
    	ctx := context.Background()
    	client, err := managedkafka.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1.html#cloud_google_com_go_managedkafka_apiv1_Client_NewClient)(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewClient got err: %w", err)
    	}
    	defer client.Close()
    
    	clusterPath := fmt.Sprintf("projects/%s/locations/%s/clusters/%s", projectID, region, clusterID)
    	req := &managedkafkapb.GetClusterRequest{
    		Name: clusterPath,
    	}
    	cluster, err := client.GetCluster(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetCluster got err: %w", err)
    	}
    	fmt.Fprintf(w, "Got cluster: %#v\n", cluster)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html);
    import com.google.cloud.managedkafka.v1.[ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html);
    import java.io.IOException;
    
    public class GetCluster {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-cluster";
        getCluster(projectId, region, clusterId);
      }
    
      public static void getCluster(String projectId, String region, String clusterId)
          throws Exception {
        try ([ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html) managedKafkaClient = [ManagedKafkaClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaClient.html).create()) {
          // This operation is being handled synchronously.
          [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Cluster.html) cluster = managedKafkaClient.getCluster([ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ClusterName.html).of(projectId, region, clusterId));
          System.out.println(cluster.getAllFields());
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaClient.getCluster got err: %s", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # cluster_id = "my-cluster"
    
    client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    cluster_path = client.[cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_cluster_path)(project_id, region, cluster_id)
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[GetClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetClusterRequest.html)(
        name=cluster_path,
    )
    
    try:
        cluster = client.[get_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_get_cluster)(request=request)
        print("Got cluster:", cluster)
    except NotFound as e:
        print(f"Failed to get cluster {cluster_id} with error: {e.message}")
    

## View cluster properties and resources

The following sections describe how to get details about various properties and resources associated with a Google Cloud Managed Service for Apache Kafka cluster.

### Bootstrap address

Kafka clients use the cluster's _bootstrap address_ to establish a connection with the cluster. The bootstrap address is fixed for the lifetime of a cluster, but the format of the bootstrap URL might differ between clusters.

If your cluster has public access enabled, the bootstrap address automatically resolves to either public or private IP addresses depending on where the client is connecting from (using split-horizon DNS). Both internal and external clients should use this same bootstrap address to connect to the cluster. Don't configure Kafka clients to connect to discovery DNS records, which are reserved only for configuring external egress firewalls.

To get the bootstrap address, perform the following steps:

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. Select the **Configurations** tab.

  4. If you're using SASL to authenticate, the bootstrap URL is listed under **Bootstrap URL**.

If you're using [mutual TLS](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls) (mTLS) to authenticate, the bootstrap URL is listed under **mTLS Bootstrap URL**.

Click content_copy **Copy** to copy the value.




###  gcloud 

To get the bootstrap URL, use the [`managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command.

If you're using SASL to authenticate, run the following command:
    
    
    gcloud managed-kafka clusters describe CLUSTER_ID \
        --location=LOCATION \
        --format="value(bootstrapAddress)"
    

If you're using [mutual TLS](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls) (mTLS) to authenticate, run the following command:
    
    
    gcloud managed-kafka clusters describe CLUSTER_ID \
        --location=LOCATION \
        --format="value(bootstrapAddressMTLS)"
    

Replace the following:

  * CLUSTER_ID: The ID or name of the cluster.
  * LOCATION: The location of the cluster.



If you have a bootstrap address and want to find the corresponding cluster, you can filter the cluster list in the Google Cloud console or run [`gcloud managed-kafka clusters list`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/list) with `--filter="bootstrapAddress:BOOTSTRAP_ADDRESS"`. For more information, see [List your clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-clusters#list).

For more information about SASL and mTLS authentication, see [Authentication types for Kafka brokers](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authn-types-kafka).

### Brokers

To view the brokers in your cluster, see [View brokers in a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/view-brokers).

### Consumer groups

A [consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/consumer-groups) is a set of consumers that cooperate to consume data from various topics. To view the consumer groups for a cluster, see the following pages:

  * [List your consumer groups](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-consumer-groups)
  * [View a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-consumer-group)



### Subnetworks

To view the subnetworks that are connected to your cluster, perform the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. In the cluster details page, click the **Configurations** tab. Connected subnetworks are listed under **Subnetworks**.




###  gcloud 

  1. Run the [`gcloud managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command:
         
         gcloud managed-kafka clusters describe CLUSTER_ID \
             --location=LOCATION \
             --format="yaml(gcpConfig.accessConfig.networkConfigs)"
         

Replace the following:

     * CLUSTER_ID: The ID or name of the cluster.
     * LOCATION: The location of the cluster.



For more information, see [Configure networking for Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).

### Allowed source IP ranges

To view the allowed source IP ranges for a public cluster, perform the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. Click the **Configurations** tab. The allowed source IP ranges are listed in the **Allowed source IP ranges** table under the **IP range** column.




###  gcloud 

  1. To view the allowed source IP ranges using `gcloud`, check the `gcpConfig.accessConfig.publicClusterConfig.allowedSourceIpRanges` field in the response of the [`gcloud managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command:
         
         gcloud managed-kafka clusters describe CLUSTER_ID \
             --location=LOCATION \
             --format="yaml(gcpConfig.accessConfig.publicClusterConfig.allowedSourceIpRanges)"
         

Replace the following:

     * CLUSTER_ID: The ID or name of the cluster.
     * LOCATION: The location of the cluster.



###  REST 

To view the allowed source IP ranges using the REST API, check the `gcpConfig.accessConfig.publicClusterConfig.allowedSourceIpRanges` field in the response of a `GET` request:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster. 
  * `CLUSTER_ID`: the ID of the cluster. 
  * `CLUSTER_VIEW`: the amount of metadata to return. Specify one of the following values:

    * `CLUSTER_VIEW_BASIC`: Return the basic metadata for the cluster.
    * `CLUSTER_VIEW_FULL`: Return all of the metadata for the cluster, including information about the cluster's brokers and the Kafka version number that the cluster is running.

If not specified, the method defaults to `CLUSTER_VIEW_BASIC`.




HTTP method and URL: 
    
    
    GET https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID",
      "createTime": "CREATE_TIME",
      "updateTime": "UPDATE_TIME",
      "capacityConfig": {
        "vcpuCount": "CPU_COUNT",
        "memoryBytes": "MEMORY"
      },
      "rebalanceConfig": {},
      "gcpConfig": {
        "accessConfig": {
          "networkConfigs": [
            {
              "subnet": "projects/PROJECT_ID/locations/LOCATION/subnetworks/SUBNET_ID"
            }
          ],
          "publicClusterConfig": {
            "allowedSourceIpRanges": [
              "203.0.113.5/32"
            ]
          }
        }
      },
      "state": "ACTIVE",
      "satisfiesPzi": false,
      "satisfiesPzs": false,
      "tlsConfig": {
        "trustConfig": {}
      },
      "updateOptions": {},
      "publicClusterDetails": {
        "discoveryDnsRecords": [
          "discovery-1.CLUSTER_ID.LOCATION.managedkafka.PROJECT_ID.cloud.goog"
        ],
        "externalIpAddresses": [
          "203.0.113.1",
          "203.0.113.2",
          "203.0.113.3",
          "203.0.113.4"
        ]
      }
    }
    

For more information about allowed source IP ranges, see [Public clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#public-connectivity).

### Public cluster details

To view the public cluster details, including the external IP addresses and discovery DNS records, perform the following steps:

**Note:** Discovery DNS records are intended only for configuring external egress firewalls. Don't configure your Kafka clients to connect to discovery DNS records; instead, configure all clients to connect to the bootstrap address.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. Click the **Configurations** tab. The external IP addresses and discovery DNS records are listed in the **External IP Addresses** and **DNS Discovery Records** fields.




###  gcloud 

  1. Run the [`gcloud managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command:
         
         gcloud managed-kafka clusters describe CLUSTER_ID \
             --location=LOCATION \
             --format="yaml(publicClusterDetails)"
         

Replace the following:

     * CLUSTER_ID: The ID or name of the cluster.
     * LOCATION: The location of the cluster.



###  REST 

To view the public cluster details using the REST API, check the `publicClusterDetails` field in the response of a `GET` request:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster. 
  * `CLUSTER_ID`: the ID of the cluster. 
  * `CLUSTER_VIEW`: the amount of metadata to return. Specify one of the following values:

    * `CLUSTER_VIEW_BASIC`: Return the basic metadata for the cluster.
    * `CLUSTER_VIEW_FULL`: Return all of the metadata for the cluster, including information about the cluster's brokers and the Kafka version number that the cluster is running.

If not specified, the method defaults to `CLUSTER_VIEW_BASIC`.




HTTP method and URL: 
    
    
    GET https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID?view=CLUSTER_VIEW" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID",
      "createTime": "CREATE_TIME",
      "updateTime": "UPDATE_TIME",
      "capacityConfig": {
        "vcpuCount": "CPU_COUNT",
        "memoryBytes": "MEMORY"
      },
      "rebalanceConfig": {},
      "gcpConfig": {
        "accessConfig": {
          "networkConfigs": [
            {
              "subnet": "projects/PROJECT_ID/locations/LOCATION/subnetworks/SUBNET_ID"
            }
          ],
          "publicClusterConfig": {
            "allowedSourceIpRanges": [
              "203.0.113.5/32"
            ]
          }
        }
      },
      "state": "ACTIVE",
      "satisfiesPzi": false,
      "satisfiesPzs": false,
      "tlsConfig": {
        "trustConfig": {}
      },
      "updateOptions": {},
      "publicClusterDetails": {
        "discoveryDnsRecords": [
          "discovery-1.CLUSTER_ID.LOCATION.managedkafka.PROJECT_ID.cloud.goog"
        ],
        "externalIpAddresses": [
          "203.0.113.1",
          "203.0.113.2",
          "203.0.113.3",
          "203.0.113.4"
        ]
      }
    }
    

### Topics

To view the topics in a cluster, see the following pages:

  * [List your topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-topics)
  * [View a topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-topic)



## What's next?

  * [Monitor your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster).

  * [Create a topic within your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic).

  * [Edit a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster).

  * [Delete your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-cluster).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
