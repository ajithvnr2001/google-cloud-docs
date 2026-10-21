---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster/
title: Create a Google Cloud Managed Service for Apache Kafka cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:09.215527+00:00
---

# Create a Google Cloud Managed Service for Apache Kafka cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Google Cloud Managed Service for Apache Kafka cluster Stay organized with collections  Save and categorize content based on your preferences. 

A Managed Service for Apache Kafka cluster provides an environment for storing and processing streams of messages organized into topics.

To create a cluster, you can use the Google Cloud console, the Google Cloud CLI, the client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to create a cluster.

## Before you begin

Verify that you are familiar with the following:

  * [How Managed Service for Apache Kafka works](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview).

  * [The networking concepts related to Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).




## Required roles and permissions to create a cluster

To get the permissions that you need to create a cluster, ask your administrator to grant you the [Managed Kafka Cluster Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a cluster:

  * Create a cluster: `managedkafka.clusters.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Properties of a Managed Service for Apache Kafka cluster

When you create or update a Managed Service for Apache Kafka cluster, you must specify the following properties.

### Cluster name

The name or ID of the Managed Service for Apache Kafka cluster that you are creating. For guidelines on how to name a cluster, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a cluster is immutable.

### Location

The location where you are creating the cluster. The location must be one of the supported Google Cloud regions. The location of a cluster can't be changed later. For a list of available locations, see [Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations).

### Capacity configuration

The compute, memory, and storage capacity of the Kafka cluster. When you create a cluster, you must specify the following values:

  * **vCPUs** : The number of vCPUs in the cluster. At 3 least vCPUs per cluster are required.

  * **Memory** : The amount of memory that is assigned to the cluster. You must provision between 1 GiB and 8 GiB per vCPU.

For example, if you create a cluster with 6 vCPUs, the minimum memory you can allocate to the cluster is 6 GiB (1 GiB per vCPU), and the maximum is 48 GiB (8 GiB per vCPU).




The service automatically provisions [brokers](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers), including Persistent Disk volumes for the brokers. Optionally, you can enable **Custom local storage** , which lets you specify the disk capacity for each broker. For more information, see [Configure broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size).

For guidelines about estimating how much capacity your cluster needs, see [Plan the size of your Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size).

### Network configuration

Network configuration is a list of VPC subnets where the cluster is accessible. To produce or consume messages, clients must be able to reach one of these subnets.

The following are some guidelines for your network configuration:

  * A minimum of 1 subnet is required for a cluster. The maximum is 10.

  * Exactly 1 subnet per network is allowed for any given cluster.

  * Each subnet must be in the same region as the cluster. The project and network can be different.

  * IP addresses for the brokers and bootstrap server are automatically allocated in each subnet. In addition, DNS entries for these IP addresses are created in the corresponding VPC networks.

  * If you add a subnet from a different project, you must grant permissions to the Google-managed service account that is associated with the cluster. For more information, see [Connect a cluster across projects](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka#cross-project-vpc).




After you create the cluster, you can [update](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster) the list of subnets. For more information about networking, see [Configure networking for Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).

### Public clusters

You can optionally configure your cluster as a public cluster to allow client applications to connect to your cluster and run Kafka operations (including sending and receiving messages) over the public internet. To enable public access, you must specify one or more allowed source IP ranges.

When you configure allowed source IP ranges, the following rules apply:

  * All allowed source IP ranges must be specified in IPv4 CIDR notation (for example, `203.0.113.0/24` or `198.51.100.5/32`).

  * Each CIDR subnet size must be between `/16` and `/32`.

  * CIDR ranges must not overlap.

  * All allowed source IP ranges must be publicly routable. Private IP ranges, such as `10.0.0.0/8` ([RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)), are rejected.

  * You can specify a maximum of 500 allowed source IP ranges.

  * IPv6 addresses aren't supported.


**Caution:** To protect your cluster, allow access from only trusted external IP ranges. Don't expose your cluster to untrusted ranges. 

Before you enable public access for a cluster, we recommend that you read [Connect clients to a public cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka#connect-clients-to-a-public-cluster) to learn how the public access feature is implemented.

### Labels

Labels are key-value pairs that help you with organization and identification. Labels let you categorize resources based on environment. Examples are `"env:production"` and `"owner:data-engineering"`.

You can filter and search for resources based on their labels. For example, assume you have multiple Managed Service for Apache Kafka clusters for different departments. You can configure and search for clusters with the label `"department:marketing"` to find the relevant one.

### Rebalancing configuration

This setting determines if the service automatically rebalances partition replicas across brokers.

The available modes are:

  * **Auto rebalance on scale up** : When this option is enabled, the service automatically triggers a rebalance of replicas when you scale up the cluster. This mode helps maintain an even load distribution but might temporarily affect performance during the rebalancing operation.

  * **No rebalance** : When this option is enabled, the service doesn't automatically rebalance replicas.




For more information, see [Rebalancing broker partitions](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers#rebalancing).

### Encryption

Managed Service for Apache Kafka can encrypt messages with Google-owned and Google-managed encryption keys (default) or Customer-managed encryption keys (CMEK). Every message is encrypted at rest and in transit. The encryption type for a cluster is immutable.

**Google-owned and Google-managed encryption keys** are used by default. These keys are created, managed, and stored entirely by Google Cloud within its infrastructure.

**CMEKs** are encryption keys that you manage using Cloud Key Management Service. This feature lets you have greater control over the keys that are used to encrypt data at rest within supported Google Cloud services. Using CMEK incurs additional costs related to Cloud Key Management Service. For CMEK usage, your key ring must be in the same location as the resources you use it with. For more information, see [Configure message encryption](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption).

### mTLS configuration

You can optionally configure mTLS as an alternative authentication method that uses client certificates. The configuration includes the following:

  * **CA pools** : A list of 1 to 10 Certificate Authority Service (CAS) pools that the cluster trusts for client authentication.

  * **SSL Principal mapping rules** : An optional but recommended `ssl.principal.mapping.rules` broker property to simplify long certificate principal names for use in Kafka ACLs.




For more information about mTLS, see [Configure mTLS authentication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls).

## Create a cluster

Before you create a cluster, read the documentation of cluster properties.

Creating a cluster usually takes 20-30 minutes.

To create a cluster, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Select **Create**.

The **Create Kafka cluster** page opens.

  3. For the **Cluster name** , enter a string.

For more information about how to name a cluster, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

  4. For **Location** , enter a supported location.

For more information about supported locations, see [Supported Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations).

  5. For **Capacity configuration** , enter values for **Memory** and **vCPUs**.

For more information about how to size a cluster, see [Plan your Kafka cluster size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size).

  6. Optional. To specify the broker disk capacity, do the following:

     1. Click the **Enable custom local storage size** toggle to the on position.

**Important:** After you click **Save** , you can't disable this setting again for this cluster.
     2. In the **Custom local storage** field, enter the disk size per broker, in GiB.

If you leave the **Enable custom local storage size** toggle in the off position, the default disk capacity is provisioned. For more information, see [Configure broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size).

  7. For **Network configuration** , enter the following details:

     1. **Project** : The project where the subnetwork is located. The subnet must be located in the same region as the cluster, but the project might be different.
     2. **Network** : The network to which the subnet is connected.
     3. **Subnetwork** : The name of the subnet.
     4. **Subnet URI path** : This field is automatically populated. Or, you can enter the subnet path here. The name of the subnet must be in the format: `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_ID`.
     5. Click **Done**.
  8. Optional: To add additional subnets, click **Add a connected subnet**.

You can add additional subnets, up to a maximum value of 10.

  9. Optional: Enable public access to your cluster.

     1. In the **Public cluster configuration** section, under **Cluster can be reached** , select **In a private network and using public internet**.

     2. In the **Comma-separated list of allowed source IPv4 ranges in CIDR notation** field, enter the IP ranges of your client applications in IPv4 CIDR notation (for example, `203.0.113.0/24`). IPv6 addresses aren't supported.

  10. Optional: Set a customer-managed encryption key (CMEK).

     1. Under **Encryption** , select **Cloud KMS key**.

     2. For **Key type** , select **Cloud KMS**.

     3. For **Select a customer-managed key** , select or enter the CMEK.

If you don't see this option, ensure that you have enabled the Cloud KMS API for the project.

For more information, see [Configure message encryption](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption).

  11. Click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Before using any of the command data below, make the following replacements: 

     * `PROJECT_ID`: the project ID. 
     * `LOCATION`: the location of the cluster. 
     * `CLUSTER_ID`: the ID of the cluster. 
     * `CPU_COUNT`: the number of vCPUs for the cluster. 
     * `MEMORY`: the amount of memory for the cluster. Example: `3GiB`. 
     * `SUBNET_ID`: the subnet ID of the subnet to connect to. Example: `default`. 
     * `ENCRYPTION_KEY`: the customer-managed encryption key ID to use for the cluster. This is optional. 
     * `LABELS`: the labels to associate with the cluster. 
     * `ALLOWED_SOURCE_IP_RANGES`: the allowed source IP ranges for the public cluster. This is optional. 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters create CLUSTER_ID \
        --location=LOCATION \
        --cpu=CPU_COUNT \
        --memory=MEMORY \
        --subnets=projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID \
        --auto-rebalance \
        --encryption-key=ENCRYPTION_KEY \
        --async \
        --labels=LABELS \
        --public-cluster \
        --allowed-source-ip-ranges=ALLOWED_SOURCE_IP_RANGES

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters create CLUSTER_ID `
        --location=LOCATION `
        --cpu=CPU_COUNT `
        --memory=MEMORY `
        --subnets=projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID `
        --auto-rebalance `
        --encryption-key=ENCRYPTION_KEY `
        --async `
        --labels=LABELS `
        --public-cluster `
        --allowed-source-ip-ranges=ALLOWED_SOURCE_IP_RANGES

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud managed-kafka clusters create CLUSTER_ID ^
        --location=LOCATION ^
        --cpu=CPU_COUNT ^
        --memory=MEMORY ^
        --subnets=projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET_ID ^
        --auto-rebalance ^
        --encryption-key=ENCRYPTION_KEY ^
        --async ^
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
      verb: create
    name: projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

Store the OPERATION_ID to track `progress`.




###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID 
  * `LOCATION`: the location of the cluster. 
  * `CLUSTER_ID`: the ID of the cluster. 
  * `CPU_COUNT`: the number of vCPUs for the cluster. 
  * `MEMORY`: the amount of memory for the cluster, in bytes. Example: `3221225472`. 
  * `SUBNET_ID`: subnet ID of the subnet to connect to. Example: `default`. 



HTTP method and URL: 
    
    
    POST https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters?clusterId=CLUSTER_ID

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
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters?clusterId=CLUSTER_ID"

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
        -Uri "https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters?clusterId=CLUSTER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.managedkafka.v1.OperationMetadata",
        "createTime": "CREATE_TIME",
        "target": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

###  Terraform 

You can use a Terraform resource to create a [cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_cluster).
    
    
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

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

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

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
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

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
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
    

## Monitor the cluster creation operation

You can run the following command only if you used the gcloud CLI to create the cluster.

  * Creating a cluster usually takes 20-30 minutes. To track progress of the cluster creation, the `gcloud managed-kafka clusters create` command uses a long-running operation (LRO), which you can monitor using the following command:
        
        gcloud managed-kafka operations describe OPERATION_ID \
            --location=LOCATION
        

Replace the following:

    * `OPERATION_ID` with the value of the operation ID from the previous section.
    * `LOCATION` with the value of the location from the previous section.



## Troubleshoot

For information about how to troubleshoot errors related to creating a cluster, see [Kafka cluster creation errors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-clusters#create-cluster-errors).

## What's next?

  * [Monitor your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster).

  * [Update your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster).

  * [List all your clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-clusters).

  * [View your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster).

  * [Delete a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-cluster).

  * [Create a topic within your cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic).

  * [Configure networking for Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
