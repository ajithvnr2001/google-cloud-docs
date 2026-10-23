---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster/
title: Create a Connect cluster \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:34.110577+00:00
---

# Create a Connect cluster  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Connect cluster Stay organized with collections  Save and categorize content based on your preferences. 

A Connect cluster provides an environment for connectors that helps to move data from existing Kafka deployments into a Google Cloud Managed Service for Apache Kafka cluster or move data from Managed Service for Apache Kafka cluster to another Google Cloud service or another Kafka cluster. The secondary Kafka cluster can be another Google Cloud Managed Service for Apache Kafka cluster, a self-managed, or a on-premises one.

## Before you begin

Ensure that you have already created a [Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster). You need the name of the Managed Service for Apache Kafka cluster to which the Connect cluster is going to be attached.

Each Connect cluster is associated with a Managed Service for Apache Kafka cluster. This cluster stores the state of the connectors running on the Connect cluster.

### Required roles and permissions to create a Connect cluster

To get the permissions that you need to create a Connect cluster, ask your administrator to grant you the [Managed Kafka Connect Cluster Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a Connect cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a Connect cluster:

  * Grant the create a Connect cluster permission on the specified location: `managedkafka.connectClusters.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required ACL principals

**Note:** This section only applies to configurations where the Managed Service for Apache Kafka cluster that is going to be associated with the Connect Cluster has Kafka ACLs.

By default Managed Service for Apache Kafka clusters let Connect Cluster access to resources if no ACLs are configured. This is done by setting `allow.everyone.if.no.acl.found` to `true`, which is the default setting.

However, if the Managed Service for Apache Kafka cluster has ACLs configured, the Connect Cluster doesn't automatically have the read and write permissions to the resources. You have to grant them manually.

The Connect cluster service account that is used as the principal in ACLs follows this format: `User:service-{consumer project number}@gcp-sa-managedkafka.iam.gserviceaccount.com`.

If you have configured ACLs on your Kafka cluster, grant the Connect cluster read and write permissions to topics and read permissions to consumer groups using the following commands:
    
    
    /bin/kafka-acls.sh \
        --bootstrap-server BOOTSTRAP_ADDR \
        --command-config PATH_TO_CLIENT_PROPERTIES \
        --add \
        --allow-principal User:service-{consumer project number}@gcp-sa-managedkafka.iam.gserviceaccount.com \
        --operation READ --operation WRITE --topic *
    
    
    
    /bin/kafka-acls.sh \
        --bootstrap-server BOOTSTRAP_ADDR \
        --command-config PATH_TO_CLIENT_PROPERTIES \
        --add \
        --allow-principal User:service-{consumer project number}@gcp-sa-managedkafka.iam.gserviceaccount.com \
        --operation READ --group *
    

For more information about these commands, see [Configure Apache Kafka ACLs for granular access control](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls#configure-acls).

### Create a Connect cluster in a different project

Managed Service for Apache Kafka uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to access Google Cloud resources. The service agent is associated with the project where you create the cluster.

If you create a Connect cluster in a different project from the Managed Service for Apache Kafka cluster, then the Connect cluster and the Kafka cluster use the service agents associated with their respective projects. In that case, the service agent for the Connect cluster needs permission to access Google Cloud resources in the Kafka cluster's project.

To give the necessary permissions, grant the [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) role to the Connect cluster's service agent on the Kafka cluster's project. For example, if you create a Kafka cluster in the project `kafka-project` and a Connect cluster in the project `connect-project`, grant the Managed Kafka Service Agent role on `kafka-project` to the service agent associated with `connect-project`.

The service agent's email address has the following format: `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`, where PROJECT_NUMBER is the project number. For more information about how to grant the role, see [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents#grant-role).

## Properties of a Connect cluster

This section describes the properties of a Connect cluster.

### Connect cluster name

The name of the Connect cluster that you are creating. For guidelines on how to name a Connect cluster, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a cluster is immutable.

### Primary Kafka cluster

The Managed Service for Apache Kafka cluster associated with your Connect cluster. This associated cluster (primary cluster) stores the state of the connectors running on the Connect cluster. Generally, the primary Managed Service for Apache Kafka cluster also serves as the destination for all source connectors and the input for all sink connectors running on the Connect cluster.

A single Managed Service for Apache Kafka cluster can have multiple Connect clusters. If you choose a Managed Service for Apache Kafka cluster in a different project, ensure appropriate permissions are configured.

You cannot update to a different Kafka cluster after you create the Connect cluster.

#### Region colocation benefits for latency and network costs

Co-locating your Managed Service for Apache Kafka and Connect clusters in the same region reduces latency and network costs. For example, assume your Managed Service for Apache Kafka cluster is in `region-a` and you're using a sink connector to write data from this Managed Service for Apache Kafka cluster (source) to a BigQuery table (sink) that is also in `region-a`. If you deploy your Connect cluster in `region-a`, this deployment choice minimizes latency for the BigQuery write operation and eliminates inter-region network transfer costs between the Managed Service for Apache Kafka cluster and the Connect cluster.

#### Multi-system latency and cost considerations

Kafka Connect uses connectors to move data between systems. One side of the connector always interacts with a Managed Service for Apache Kafka cluster. A single Kafka Connect cluster can run multiple connectors, each acting as either a _source_ (pulling data from a system) or a _sink_ (pushing data to a system).

While a Connect cluster in the same region as the Managed Service for Apache Kafka cluster benefits from lower communication latency between them, each connector also interacts with another system, such as a BigQuery table or another Kafka cluster. Even if the Connect cluster and the Managed Service for Apache Kafka cluster are co-located, that other system could be in a different region. This leads to higher latency and cost. The overall pipeline latency depends on the locations of all three systems: the Managed Service for Apache Kafka cluster, the Connect cluster, and the source or sink system.

For example, if your Managed Service for Apache Kafka cluster is in `region-a`, your Connect cluster in `region-b`, and you're using a Cloud Storage connector for a bucket in `region-c`, you'll be charged for two network hops (`region-a` to `region-b` and then `region-b` to `region-c`, or the reverse depending on the connector direction).

Carefully consider all involved regions when planning your Connect cluster placement to optimize for both latency and cost.

### Capacity configuration

Capacity configuration requires you to configure the number of vCPUs and the amount of memory for each vCPU for your Connect cluster. You can update the capacity of a Connect cluster after you create it. The following are the properties for capacity configuration:

  * vCPUs: The number of vCPUs assigned to a Connect cluster. The minimum value is 3 vCPUs.

  * Memory: The amount of memory that is assigned for each vCPU. You must provision between 1 GiB and 8 GiB per vCPU. The amount of memory can be increased or decreased within these limits after the cluster is created.

For example, if you create a cluster with 6 vCPUs, the minimum memory you can allocate to the cluster is 6 GiB (1 GiB per vCPU), and the maximum is 48 GiB (8 GiB per vCPU).




The vCPU and memory allocated to each worker in a Connect cluster have a significant impact on the cluster's performance, capacity, and cost. Here's a breakdown of how vCPU and memory affect a Connect cluster.

#### vCPU count

  * Kafka Connect divides the work of a connector into tasks. Each task can process data in parallel. More vCPUs mean more tasks can run simultaneously, leading to higher throughput.

  * More vCPUs increases the costs for your Connect cluster.




#### Memory

  * Kafka Connect uses memory for buffering data as it flows between connectors and Managed Service for Apache Kafka. Larger memory allows for larger buffers. Large memory can improve throughput, especially for high-volume data streams. Connectors dealing with very large messages or records require sufficient memory to process them without running into `OutOfMemoryError` exceptions.

  * More memory increases the cost of your Connect cluster.

  * If you are using heavy transformation logic, you require more memory allocation.




Your goal is to pick the right capacity configuration for your Connect cluster. To do this, you must understand the throughput your Connect cluster can handle.

### Worker (primary) subnet

The **worker subnet** , also known as the **primary subnet** , connects your VPC network to the Connect cluster. This subnet lets the cluster workers reach the endpoints of sources and sinks in the consumer network, such as Managed Service for Apache Kafka clusters or self-hosted Kafka clusters.

Here are some requirements for configuring the worker subnet:

  * The worker subnet is required.

  * The subnet must be located in the same region as the Connect cluster.

  * The subnet must be in the same parent VPC as one of the primary Kafka cluster's list of [connected subnets](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#network-config).

  * The subnet CIDR range must have a minimum size of /22 (1024 addresses).




The cluster workers are assigned IP addresses in the worker subnet, using a [Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/private-service-connect#interfaces). Workers can reach any network destination that is accessible from the subnet's VPC network, with the following requirements:

  * The endpoint must not be in the `172.16.0.0/14` CIDR range. This range is reserved for Managed Service for Apache Kafka Connect internal use.
  * Firewall rules must permit the traffic. See [Configure security for network attachments](https://docs.cloud.google.com/vpc/docs/configure-security-network-attachments).
  * For internet traffic, you must configure a [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview). For example, a Cloud NAT is required for a [MirrorMaker connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector) to replicate data from a Kafka cluster that is accessible over the internet.
  * To access Private Service Connect endpoints that are in a different VPC from the worker subnet VPC, you must ensure you are using a supported consumer configuration (for example, NCC). For more information, see [About accessing published services through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints).



### Resolvable DNS domains

**Resolvable DNS domains** , also known as DNS domain names, allow DNS addresses in the consumer VPC network to be made available to the tenant VPC. This enables the Connect cluster to resolve DNS names to IP addresses, facilitating communication with other services, including other Kafka clusters for MirrorMaker connectors.

For resolvable DNS domains, you can select a Managed Service for Apache Kafka cluster. You don't need to configure the DNS domain name for the primary Managed Service for Apache Kafka cluster, as its bootstrap address is automatically included in the list of resolvable DNS domains.

However, you can also specify a DNS domain manually, which is necessary if you select an external Kafka cluster. The primary Managed Service for Apache Kafka cluster's DNS domain is automatically included. Other Kafka clusters still require configuring DNS domains.

### Secret Manager resources

Some connectors require sensitive data, such as passwords, as part of their configuration. To manage this type of data securely, you can store the data in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) and give the Connect cluster access to the secret.

To use Secret Manager secrets with Kafka Connect, do the following:

  1. Grant the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) role to the Managed Kafka Service Account. This role allows your Connect cluster to access secrets.

  2. Create a secret that contains the sensitive data. For more information, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

  3. When you create or update your Connect cluster, specify the secrets that the cluster has access to. You can specify up to 32 secrets per Connect cluster.




Secrets are mounted as files in the cluster workers. Connectors have read-only access to these files. When you create a connector, the connector's configuration properties can reference the secrets.

  * To reference the path to a secret file, use the following format:
        
        /var/secrets/PROJECT_NAME-SECRET_NAME-SECRET_VERSION
        

Example: `ssl.truststore.location=/var/secrets/project1-truststore-1`

  * To use the _value_ of a secret as a configuration value (for example, a password), use the following format:
        
        ${directory:/var/secrets:PROJECT_NAME-SECRET_NAME-SECRET_VERSION}
        

Example: `password=${directory:/var/secrets:project1-database_password-3}`




Replace the following:

  * PROJECT_NAME: The name of the Google Cloud project.
  * SECRET_NAME: The name of the secret.
  * SECRET_VERSION: The secret version.



### Labels

Labels are key-value pairs that help you with organization and identification. They help you organize Connect clusters. You can attach a label to each Connect cluster, then filter the resources based on their labels. Examples of labels are `environment:prod`, `application:web-app`.

## Create a Connect cluster

Before you create a cluster, review the documentation for Connect cluster properties.

Creating a Connect cluster takes 20 to 30 minutes.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click add_box**Create**.

  3. In the **Connect cluster name** field, enter a name for the Connect cluster. For more information, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

  4. In the **Primary Kafka cluster** list, select a Managed Service for Apache Kafka cluster. For more information, see Primary Kafka cluster.

  5. In the **Region** list, select a location for the Connect cluster. For more information about how to select a location, see Primary Kafka cluster.

  6. In the **Capacity configuration** section, enter values for the following fields or keep the default values.

     * In the **vCPUs** field, enter the number of virtual CPUs for the cluster.

     * In the **Memory** field, enter the amount of memory per CPU, in GiB. The value cannot exceed 8 GiB per CPU.

For more information, see Capacity configuration.

  7. In the **Network configuration** section, select a VPC network from the **Network** list or leave the default value. This list is populated when you select the primary Kafka cluster.

  8. In the **Worker subnet** section, select a subnet from the **Subnet** list or leave the default value. For more information, see Worker subnet. The **Subnet URI path** field is automatically populated when you select the subnet.

  9. Optional: Add a resolvable DNS domain. The DNS domain of the primary Kafka cluster is automatically added as a resolvable DNS domain. To specify additional DNS domains, do the following:

     1. Expand the **Resolvable DNS domains** section.

     2. Click **Add DNS domain**.

     3. To add the DNS domain of an existing Managed Service for Apache Kafka cluster, select the cluster from the **Kafka cluster** list. Otherwise, enter the DNS domain in the **DNS domain** field.

     4. Click **Done**.

  10. Optional: To add Secret Manager resources, do the following:

     1. Expand the **Secret manager resources** section.

     2. Click **Add secret resource**.

     3. In the **Secret** list, select a secret.

     4. In the **Secret version** list, select a version of the secret.

     5. Click **Done**.

  11. Optional: Add [labels](https://docs.cloud.google.com/resource-manager/docs/labels-overview) to organize your project. To add a label, do the following:

     1. Expand the **Labels** section.

     2. Click **Add label**.

     3. In the **Key** field, enter the label's key.

     4. In the **Value** field, enter the label's value.

  12. Click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka connect-clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/create) command:
         
         gcloud managed-kafka connect-clusters create CONNECT_CLUSTER_ID \
             --location=LOCATION \
             --cpu=CPU \
             --memory=MEMORY \
             --primary-subnet=WORKER_SUBNET \
             --kafka-cluster=KAFKA_CLUSTER \
             [--project=PROJECT_ID] \
             [--secret=SECRET] \
             [--dns-name=DNS_DOMAIN_NAME] \
             [--config-file=CONFIG_FILE] \
             [--labels=LABELS]
             [--async]
         

Replace the following:

     * CONNECT_CLUSTER_ID: The ID or name of the Connect cluster. For guidelines on how to name a Connect cluster, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a Connect cluster is immutable.

     * LOCATION: The location where you create the Connect cluster. This must be a supported Google Cloudregion. You cannot change a Connect cluster's location after creation. For a list of available locations, see [Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations). For more information about location recommendations, see Primary Kafka cluster.

     * CPU: The number of vCPUs for the Connect cluster. The minimum value is 3 vCPUs. See vCPU count.

     * MEMORY: The amount of memory for the Connect cluster. Use "MB", "MiB", "GB", "GiB", "TB", or "TiB" units. For example, "3GiB". You must provision between 1 GiB and 8 GiB per vCPU. See Memory.

     * WORKER_SUBNET: The worker subnet for the Connect cluster.

The format of the subnet is `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_ID`.

The worker subnet must be in the same region as the Connect cluster.

     * PROJECT_ID: (Optional) The ID of the Google Cloud project. If not provided, the current project is used.

     * KAFKA_CLUSTER: The ID or fully qualified name of the primary Managed Service for Apache Kafka cluster associated with the Connect cluster. See Kafka cluster. The format of the Kafka cluster is `projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID`.

You cannot update to a different Kafka cluster after you create the Connect cluster.

     * SECRET: (Optional) Secrets to load into workers. Exact Secret versions from Secret Manager must be provided, aliases are not supported. Up to 32 secrets may be loaded into one cluster. Format: `projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION_ID`

     * DNS_DOMAIN_NAME: (Optional) DNS domain names from the subnet to be made visible to the Connect Cluster. The Connect cluster can access resources using domain names instead of relying on IP addresses. See DNS peering.

     * LABELS: (Optional) Labels to associate with the cluster. For more information about the format for labels, see Labels. List of label KEY=VALUE pairs to add. Keys must start with a lowercase character and contain only hyphens (-), underscores (_), lowercase characters, and numbers. Values must contain only hyphens (-), underscores (_), lowercase characters, and numbers.

     * CONFIG_FILE: (Optional) The path to the JSON or YAML file containing the configuration that is overridden from the cluster or connector defaults. This file also supports inline JSON or YAML.

     * `--async`: (Optional) Return immediately, without waiting for the operation in progress to complete. With the `--async` flag, you can continue with other tasks while the cluster creation happens in the background. If you don't use the flag, the system waits for the operation to complete before returning a response. You have to wait until the cluster is fully updated before you can continue with other tasks.

You get a response similar to the following:
    
    Create request issued for: [sample-connectcluster]
    Check operation [projects/test-project/locations/us-east1/operations/operation-1753590328249-63ae19098cc06-64300a0a-06512d02] for status.
    

Store the `OPERATION_ID` to track progress. For example, the value here is `operation-1753590328249-63ae19098cc06-64300a0a-06512d02`.




###  Terraform 

You can use a Terraform resource to create a [Connect cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_connect_cluster).
    
    
    resource "google_managed_kafka_connect_cluster" "default" {
      provider           = google-beta
      project            = data.google_project.default.project_id
      connect_cluster_id = "my-connect-cluster-id"
      location           = "us-central1"
      kafka_cluster      = google_managed_kafka_cluster.default.id
      capacity_config {
        vcpu_count   = 12
        memory_bytes = 12884901888 # 12 GiB
      }
      gcp_config {
        access_config {
          network_configs {
            primary_subnet = google_compute_subnetwork.default.id
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
    
    func createConnectCluster(w io.Writer, projectID, region, clusterID, kafkaCluster string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// clusterID := "my-connect-cluster"
    	// kafkaCluster := "projects/my-project-id/locations/us-central1/clusters/my-kafka-cluster"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	locationPath := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    	clusterPath := fmt.Sprintf("%s/connectClusters/%s", locationPath, clusterID)
    
    	// Capacity configuration with 12 vCPU and 12 GiB RAM
    	capacityConfig := &managedkafkapb.CapacityConfig{
    		VcpuCount:   12,
    		MemoryBytes: 12884901888, // 12 GiB in bytes
    	}
    
    	// Optionally, you can also specify accessible subnets and resolvable DNS
    	// domains as part of your network configuration. For example:
    	// networkConfigs := []*managedkafkapb.ConnectNetworkConfig{
    	// 	{
    	// 		PrimarySubnet:      primarySubnet,
    	// 		AdditionalSubnets:  []string{"subnet-1", "subnet-2"},
    	// 		DnsDomainNames:     []string{"domain-1", "domain-2"},
    	// 	},
    	// }
    
    	connectCluster := &managedkafkapb.ConnectCluster{
    		Name:           clusterPath,
    		KafkaCluster:   kafkaCluster,
    		CapacityConfig: capacityConfig,
    	}
    
    	req := &managedkafkapb.CreateConnectClusterRequest{
    		Parent:           locationPath,
    		ConnectClusterId: clusterID,
    		ConnectCluster:   connectCluster,
    	}
    	op, err := client.CreateConnectCluster(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateConnectCluster got err: %w", err)
    	}
    	// The duration of this operation can vary considerably, typically taking 5-15 minutes.
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("op.Wait got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created connect cluster: %s\n", resp.Name)
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
    import com.google.cloud.managedkafka.v1.[CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html);
    import com.google.cloud.managedkafka.v1.[ConnectAccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectAccessConfig.html);
    import com.google.cloud.managedkafka.v1.[ConnectCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html);
    import com.google.cloud.managedkafka.v1.[ConnectGcpConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectGcpConfig.html);
    import com.google.cloud.managedkafka.v1.[ConnectNetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectNetworkConfig.html);
    import com.google.cloud.managedkafka.v1.[CreateConnectClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectClusterRequest.html);
    import com.google.cloud.managedkafka.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectSettings.html);
    import com.google.cloud.managedkafka.v1.[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.OperationMetadata.html);
    import java.time.Duration;
    import java.util.concurrent.ExecutionException;
    
    public class CreateConnectCluster {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String clusterId = "my-connect-cluster";
        String subnet = "my-subnet"; // e.g. projects/my-project/regions/my-region/subnetworks/my-subnet
        String kafkaCluster = "my-kafka-cluster"; // The Kafka cluster to connect to
        int cpu = 12;
        long memoryBytes = 12884901888L; // 12 GiB
        createConnectCluster(projectId, region, clusterId, subnet, kafkaCluster, cpu, memoryBytes);
      }
    
      public static void createConnectCluster(
          String projectId,
          String region,
          String clusterId,
          String subnet,
          String kafkaCluster,
          int cpu,
          long memoryBytes)
          throws Exception {
        [CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html) capacityConfig = [CapacityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.html).newBuilder().[setVcpuCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.Builder.html#com_google_cloud_managedkafka_v1_CapacityConfig_Builder_setVcpuCount_long_)(cpu)
            .[setMemoryBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CapacityConfig.Builder.html#com_google_cloud_managedkafka_v1_CapacityConfig_Builder_setMemoryBytes_long_)(memoryBytes).build();
        [ConnectNetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectNetworkConfig.html) networkConfig = [ConnectNetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectNetworkConfig.html).newBuilder()
            .[setPrimarySubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectNetworkConfig.Builder.html#com_google_cloud_managedkafka_v1_ConnectNetworkConfig_Builder_setPrimarySubnet_java_lang_String_)(subnet)
            .build();
        // Optionally, you can also specify additional accessible subnets and resolvable
        // DNS domains as part of your network configuration. For example:
        // .addAllAdditionalSubnets(List.of("subnet-1", "subnet-2"))
        // .addAllDnsDomainNames(List.of("dns-1", "dns-2"))
        [ConnectGcpConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectGcpConfig.html) gcpConfig = [ConnectGcpConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectGcpConfig.html).newBuilder()
            .setAccessConfig([ConnectAccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectAccessConfig.html).newBuilder().addNetworkConfigs(networkConfig).build())
            .build();
        [ConnectCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html) connectCluster = [ConnectCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html).newBuilder()
            .setCapacityConfig(capacityConfig)
            .setGcpConfig(gcpConfig)
            .[setKafkaCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.Builder.html#com_google_cloud_managedkafka_v1_ConnectCluster_Builder_setKafkaCluster_java_lang_String_)(kafkaCluster)
            .build();
    
        // Create the settings to configure the timeout for polling operations
        [ManagedKafkaConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectSettings.html).Builder settingsBuilder = [ManagedKafkaConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectSettings.html).newBuilder();
        [TimedRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedRetryAlgorithm.html) timedRetryAlgorithm = [OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html).create(
            [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                .[setTotalTimeoutDuration](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeoutDuration_java_time_Duration_)(Duration.ofHours(1L))
                .build());
        settingsBuilder.createConnectClusterOperationSettings()
            .setPollingAlgorithm(timedRetryAlgorithm);
    
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html)
            .create(settingsBuilder.build())) {
          [CreateConnectClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectClusterRequest.html) request = [CreateConnectClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectClusterRequest.html).newBuilder()
              .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.LocationName.html).of(projectId, region).toString())
              .[setConnectClusterId](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectClusterRequest.Builder.html#com_google_cloud_managedkafka_v1_CreateConnectClusterRequest_Builder_setConnectClusterId_java_lang_String_)(clusterId)
              .setConnectCluster(connectCluster)
              .build();
    
          // The duration of this operation can vary considerably, typically taking
          // between 10-30 minutes.
          OperationFuture<ConnectCluster, OperationMetadata> future = managedKafkaConnectClient
              .[createConnectClusterOperationCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html#com_google_cloud_managedkafka_v1_ManagedKafkaConnectClient_createConnectClusterOperationCallable__)().futureCall(request);
    
          // Get the initial LRO and print details.
          [OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html) operation = future.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.printf(
              "Connect cluster creation started. Operation name: %s\nDone: %s\nMetadata: %s\n",
              operation.[getName](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_getName__)(), operation.[isDone](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_isDone__)(), future.getMetadata().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().toString());
    
          while (!future.isDone()) {
            // The pollingFuture gives us the most recent status of the operation
            RetryingFuture<OperationSnapshot> pollingFuture = future.getPollingFuture();
            [OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html) currentOp = pollingFuture.[getAttemptResult](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryingFuture.html#com_google_api_gax_retrying_RetryingFuture_getAttemptResult__)().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
            System.out.printf("Polling Operation:\nName: %s\n Done: %s\n",
                currentOp.[getName](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_getName__)(),
                currentOp.[isDone](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot.html#com_google_api_gax_longrunning_OperationSnapshot_isDone__)());
          }
    
          // NOTE: future.get() blocks completion until the operation is complete (isDone
          // = True)
          [ConnectCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.printf("Created connect cluster: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectCluster.html#com_google_cloud_managedkafka_v1_ConnectCluster_getName__)());
        } catch (ExecutionException e) {
          System.err.printf("managedKafkaConnectClient.createConnectCluster got err: %s\n", 
              e.getMessage());
          throw e;
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html)
    from google.cloud.managedkafka_v1.types import [ConnectCluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectCluster.html), [CreateConnectClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateConnectClusterRequest.html), [ConnectNetworkConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectNetworkConfig.html)
    
    # TODO(developer): Update with your values.
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    # kafka_cluster_id = "my-kafka-cluster"
    # primary_subnet = "projects/my-project-id/regions/us-central1/subnetworks/default"
    # cpu = 12
    # memory_bytes = 12884901888  # 12 GiB
    
    connect_client = ManagedKafkaConnectClient()
    kafka_client = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html)()
    
    parent = connect_client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_common_location_path)(project_id, region)
    kafka_cluster_path = kafka_client.[cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient.html#google_cloud_managedkafka_v1_services_managed_kafka_ManagedKafkaClient_cluster_path)(project_id, region, kafka_cluster_id)
    
    connect_cluster = ConnectCluster()
    connect_cluster.name = connect_client.[connect_cluster_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connect_cluster_path)(project_id, region, connect_cluster_id)
    connect_cluster.kafka_cluster = kafka_cluster_path
    connect_cluster.capacity_config.vcpu_count = cpu
    connect_cluster.capacity_config.memory_bytes = memory_bytes
    connect_cluster.gcp_config.access_config.network_configs = [ConnectNetworkConfig(primary_subnet=primary_subnet)]
    # Optionally, you can also specify accessible subnets and resolvable DNS domains as part of your network configuration.
    # For example:
    # connect_cluster.gcp_config.access_config.network_configs = [
    #     ConnectNetworkConfig(
    #         primary_subnet=primary_subnet,
    #         additional_subnets=additional_subnets,
    #         dns_domain_names=dns_domain_names,
    #     )
    # ]
    
    request = CreateConnectClusterRequest(
        parent=parent,
        connect_cluster_id=connect_cluster_id,
        connect_cluster=connect_cluster,
    )
    
    try:
        operation = connect_client.[create_connect_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_create_connect_cluster)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        # Creating a Connect cluster can take 10-40 minutes.
        response = operation.result(timeout=3000)
        print("Created Connect cluster:", response)
    except GoogleAPICallError as e:
        print(f"The operation failed with error: {e}")
    

## Monitor the cluster creation operation

You can run the following command only if you ran the gcloud CLI for creating the Connect cluster.

  * Creating a Connect cluster usually takes 20-30 minutes. To track progress of the cluster creation, the `gcloud managed-kafka connect-clusters create` command uses a long-running operation (LRO), which you can monitor using the following command:
        
        gcloud managed-kafka operations describe OPERATION_ID \
            --location=LOCATION
        

Replace the following:

    * `OPERATION_ID` with the value of the operation ID from the previous section.
    * `LOCATION` with the value of the location from the previous section.



## What's next?

  * [View details about a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connect-cluster)

  * [Update a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connect-cluster)

  * [An overview of connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
