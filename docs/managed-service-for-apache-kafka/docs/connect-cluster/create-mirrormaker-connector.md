---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector/
title: Create a MirrorMaker 2.0 Source connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:17.316959+00:00
---

# Create a MirrorMaker 2.0 Source connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a MirrorMaker 2.0 Source connector Stay organized with collections  Save and categorize content based on your preferences. 

The MirrorMaker 2.0 Source connector replicates topics and data from one Kafka cluster (the source) to another Kafka cluster (the target).

Use this connector for the following scenarios:

  * **Data migration**. Move your Kafka workload to a new Managed Service for Apache Kafka cluster.

  * **Disaster recovery**. Create a backup cluster to ensure business continuity in case of failures.

  * **Data aggregation**. Consolidate data from multiple Kafka clusters into a central Managed Service for Apache Kafka cluster to perform analytics.




For basic data replication between Kafka clusters, you can use the MirrorMaker 2.0 Source connector by itself. To ensure more robust disaster recovery, use the following connectors in conjunction with the MirrorMaker 2.0 Source connector:

  * Use the [MirrorMaker 2.0 Checkpoint](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-checkpoint-connector) connector to replicate consumer offsets, so that consumers can fail over to the target cluster without losing data.

  * Use the [MirrorMaker 2.0 Heartbeat](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-heartbeat-connector) connector to generates periodic heartbeat messages, and use these to monitor connectivity and replication lag.




## Understand cluster roles in MirrorMaker 2.0

A MirrorMaker 2.0 connector reads from a _source_ Kafka cluster and writes to a _target_ Kafka cluster. In Managed Service for Apache Kafka, the Connect cluster's [primary cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#kafka-cluster) must be the target cluster. This configuration minimizes latency for write operations. The source cluster can be another Managed Service for Apache Kafka cluster or an external or self-managed Kafka cluster.

If you want to replicate data from a Managed Service for Apache Kafka cluster to an external or self-managed cluster, we recommend running Kafka Connect in the same location or region as the other cluster, and use MirrorMaker 2.0 to ingest the data from Managed Service for Apache Kafka.

You must correctly configure all properties for the connector. These also include producer authentication properties which are directed at the secondary cluster. For details on potential issues, see [Improve MirrorMaker 2.0 client configuration](https://cwiki.apache.org/confluence/display/KAFKA/KIP-781%3A+Improve+MirrorMaker2%27s+client+configuration).

## Required roles and permissions

To get the permissions that you need to create a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a connector:

  * Create a connector: `managedkafka.connectors.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure networking

This section describes the networking requirements for MirrorMaker 2.0 to connect to the secondary Kafka cluster. Here are the general requirements:

  * **Connectivity**. The Connect cluster workers must be able to connect to the secondary Kafka cluster.

  * **DNS resolution**. You must add the secondary cluster's DNS domain to the Connect cluster's [resolvable DNS domains](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#dns-peering). In addition, the DNS domain must be resolvable from the Connect cluster's subnet, for example by creating a Cloud DNS zone.

  * **Firewall rules**. Firewall rules must allow the Connect cluster workers to reach both the source and target Kafka clusters.




Many of the details depend on how and where the secondary Kafka cluster is hosted, whether it is a Managed Service for Apache Kafka cluster, a self-managed cluster in Google Cloud, or an external cluster.

  * Managed Service for Apache Kafka cluster

    * If the secondary cluster is in a different VPC network, add a subnet from the Connect cluster's VPC network to the secondary cluster's connected subnets. For more information, see [Network configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#network-config).
  * Self-managed Kafka cluster in Google Cloud

    * If the secondary cluster is in a different VPC network, connectivity options include [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [Network Connectivity Center (NCC)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview), and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

    * If the secondary cluster is in a different VPC network, create a [Cloud DNS peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones) that peers to the secondary cluster's VPC network and is visible in the Connect cluster's subnet.

  * External Kafka cluster

    * Options to connect to an external cluster include:

      * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview): A cost-effective solution suitable for lower bandwidth. It creates an encrypted tunnel over the public internet.

      * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview): Provides a dedicated, high-bandwidth connection between your on-premises network and Google Cloud. You can choose between Dedicated Interconnect for direct physical connection or Partner Interconnect to connect through a service provider.

    * Configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to allow the Connect workers to access the internet.

    * Create a [Cloud DNS forwarding zone](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones) in the Connect cluster's VPC network to resolve DNS queries for your external cluster's bootstrap address and broker endpoints.




## Configure authentication

If the source or target Kafka cluster is a Managed Service for Apache Kafka cluster, the connector is automatically configured to use [OAuthBearer](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka#oauthbearer) authentication. You don't need to set any additional configurations.

For a self-managed or external Kafka cluster, you must configure authentication and TLS encryption. The configurations depend on the authentication mechanism that the Kafka cluster supports. For more information, see [MirrorMaker Common Configs](https://kafka.apache.org/37/configuration/mirrormaker-configs/#mirrormaker-common-configs) in the Apache Kafka documentation.

If the cluster supports OAuthBearer authentication, use the following settings:
    
    
    source.cluster.security.protocol=SASL_SSL
    source.cluster.sasl.mechanism=OAUTHBEARER
    source.cluster.sasl.login.callback.handler.class=com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
    source.cluster.sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
    

Store required credentials in Secret Manager, as described in the next section.

### Use Secret Manager for credentials

When connecting to self-managed or external Kafka clusters, use Secret Manager to store sensitive configuration values needed for authentication. This information might include passwords, key store files, and trust store files, depending on how authentication is configured in the cluster.

For more information about how to associate Secret Manager secrets with a Connect cluster, see [Secret Manager resources](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#secrets).

In the connector configuration, reference secrets as follows:

  * For file paths, use the format `/var/secrets/PROJECT_NAME-SECRET_NAME-SECRET_VERSION`. Example: `ssl.truststore.location=/var/secrets/project1-truststore-1`.

  * For passwords, use the format `${directory:/var/secrets:PROJECT_NAME-SECRET_NAME-SECRET_VERSION}`. Example: `password=${directory:/var/secrets:project1-database_password-3}`.




Replace the following:

  * PROJECT_NAME: The name of the Google Cloud project.
  * SECRET_NAME: The name of the secret.
  * SECRET_VERSION: The secret version.



## How a MirrorMaker Source connector works

A MirrorMaker Source connector pulls data from one or more Kafka topics in a source cluster and replicates that data, along with ACLs, to topics in a target cluster.

Here's a detailed breakdown of how the MirrorMaker Source connector replicates data:

  * The connector consumes messages from specified Kafka topics within the source cluster. Specify the topics to replicate using the `topics` configuration property, which accepts comma-separated topic names or a single Java-style regular expression. For example, `topic-a,topic-b` or `my-prefix-.*`.

  * The connector can also skip replicating specific topics that you specify by using the `topics.exclude` property; exclusions override inclusions.

  * The connector writes the consumed messages to the target cluster.

  * The connector requires the source and target cluster connection details such as `source.cluster.bootstrap.servers` and `target.cluster.bootstrap.servers`.

  * The connector also requires aliases for the source and target clusters as specified by `source.cluster.alias` and `target.cluster.alias`. By default, replicated topics are automatically renamed using the source alias. For example, a topic named `orders` from a source with alias `primary` becomes `primary.orders` in the target.

  * ACLs associated with the replicated topics are also synced from the source to the target cluster. This can be disabled using the `sync.topic.acls.enabled` property.

  * Authentication details for connecting to both the source and target clusters must be provided in the configuration if required by the clusters. You must configure properties like `security.protocol`, `sasl.mechanism`, and `sasl.jaas.config`, prefixed with `source.cluster.` for the source and `target.cluster.` for the target.

  * The connector relies on internal topics. You might need to configure properties related to these, such as `offset-syncs.topic.replication.factor`.

  * The connector uses Kafka record converters `key.converter`, `value.converter`, and `header.converter`. For direct replication, these often default to `org.apache.kafka.connect.converters.ByteArrayConverter`, which performs no conversion (pass-through).

  * The `tasks.max` property controls the level of parallelism for the connector. Increasing `tasks.max` can potentially improve throughput, but the effective parallelism is often limited by the number of partitions in the source Kafka topics being replicated.




## Properties of a MirrorMaker 2.0 connector

When you create or update a MirrorMaker 2.0 connector, specify these properties:

### Connector name

The name or ID of the connector. For guidelines about how to name the resource, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name is immutable.

### Connector type

The connector type must be one of the following:

  * [MirrorMaker 2.0 Source](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#mirrormaker-2-0-source)

  * [MirrorMaker 2.0 Checkpoint](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#mirrormaker-2-0-checkpoint)

  * [MirrorMaker 2.0 Heartbeat](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#mirrormaker-2-0-heartbeat)




### Source cluster

The source Kafka cluster that the MirrorMaker 2.0 connector reads from.

  * **Managed Service for Apache Kafka cluster:** Select a cluster from the drop-down menu.

  * **Self-managed or external Kafka cluster:** Enter the bootstrap address in the format `hostname:port_number`. For example: `kafka-test:9092`.




### Topic names or regular expressions

The topics to replicate. Specify individual names (`topic1`, `topic2`) or use a regular expression (`topic.*`). This property is required for the MirrorMaker 2.0 Source connector. The default value is `.*`

### Consumer group names or regular expressions

The consumer groups to replicate. Specify individual names (group1, group2) or use a regular expression (`group.*`). This property is required for the MirrorMaker 2.0 Checkpoint connector. The default value is `.*`

### Configuration

This section lets you specify additional, connector-specific configuration properties for the MirrorMaker 2.0 connector.

Since data in Kafka topics can be in various formats like Avro, JSON, or raw bytes, a key part of the configuration involves specifying converters. Converters translate data from the format used in your Kafka topics into the standardized, internal format of Kafka Connect.

For more general information about the role of converters in Kafka Connect, supported converter types, and common configuration options, see [Converters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#converters).

Some common configurations for all MirrorMaker 2.0 connectors include:

  * **`source.cluster.alias`** : Alias for the source cluster.

  * **`target.cluster.alias`** : Alias for the target cluster.




Configurations used to exclude specific resources when replicating data:

  * **`topics.exclude`** : Excluded topics. Supports comma-separated topic names and regexes. Excludes take precedence over includes. Used for MirrorMaker 2.0 Source connector. The default value is `mm2.*.internal,.*.replica,__.*`

  * **`groups.exclude`** : Exclude groups. Supports comma-separated group IDs and regexes. Excludes take precedence over includes. Used for MirrorMaker 2.0 Checkpoint connector. The default value is `console-consumer-.*,connect-.*,__.*`




The available configuration properties depend on the specific connector. Check the [version of the MirrorMaker 2.0 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview#upgrades) supported to see which config examples are supported. See the following documents:

  * [MirrorMaker 2.0 configuration properties common to all MirrorMaker 2.0 connectors](https://kafka.apache.org/37/configuration/mirrormaker-configs/#mirrormaker-common-configs)

  * [MirrorMaker 2.0 Source-specific configuration properties](https://kafka.apache.org/37/configuration/mirrormaker-configs/#mirrormaker-source-configs)

  * [MirrorMaker 2.0 Checkpoint-specific configuration properties](https://kafka.apache.org/37/configuration/mirrormaker-configs/#mirrormaker-checkpoint-configs)

  * [MirrorMaker 2.0 Heartbeat-specific configuration properties](https://kafka.apache.org/37/configuration/mirrormaker-configs/#mirrormaker-heartbeat-configs)




### Kafka record conversion

Kafka Connect uses `org.apache.kafka.connect.converters.ByteArrayConverter` as the default converter for key and value, which provides a pass-through option that does no conversion.

You can configure `header.converter`, `key.converter`, and `value.converter` to use other converters.

### Task count

The `tasks.max` value configures the maximum tasks Kafka Connect uses to run MirrorMaker connectors. It controls the level of parallelism for a connector. Increasing the task count may increase throughput, but is limited by factors like the number of Kafka topic partitions.

## Create a MirrorMaker 2.0 Source connector

Before you create a connector, review the documentation for connector properties.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster where you want to create the connector.

The **Connect cluster details** page displays.

  3. Click **Create Connector**.

The **Create Kafka Connector** page displays.

  4. For the **Connector name** , enter a string.

For more information about how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

  5. For **Connector plugin** , select "MirrorMaker 2.0 Source".

  6. For **Source cluster** , choose one of the following options:

     * **Managed Service for Apache Kafka Cluster** : Select from the menu.
     * **Self-managed or External Kafka Cluster** : Enter the bootstrap address in the format `hostname:port_number`.
  7. Enter the **Comma-separated topic names or topic regex**.

  8. Review and adjust the **Configurations** , including the required security settings.

For more information about configuration and authentication, see [Configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector#configuration).

  9. Select the **Task restart policy**. For more information, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).

  10. Click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka connectors create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create) command:
         
         gcloud managed-kafka connectors create CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID \
             --config-file=CONFIG_FILE
         

Replace the following:

     * CONNECTOR_ID: The ID or name of the connector. For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a connector is immutable.

     * LOCATION: The location where you create the connector. This must be the same location where you created the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster).

     * CONNECT_CLUSTER_ID: The ID of the Connect cluster where the connector is created.

     * CONFIG_FILE: The path to the YAML configuration file for the connector.

Here is an example of a configuration file for the MirrorMaker 2.0 Source connector:
    
    connector.class: "org.apache.kafka.connect.mirror.MirrorSourceConnector"
    name: "MM2_CONNECTOR_ID"
    source.cluster.alias: "source"
    target.cluster.alias: "target"
    topics: "GMK_TOPIC_NAME"
    source.cluster.bootstrap.servers: "GMK_SOURCE_CLUSTER_DNS"
    target.cluster.bootstrap.servers: "GMK_TARGET_CLUSTER_DNS"
    offset-syncs.topic.replication.factor: "1"
    source.cluster.security.protocol: "SASL_SSL"
    source.cluster.sasl.mechanism: "OAUTHBEARER"
    source.cluster.sasl.login.callback.handler.class: com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
    source.cluster.sasl.jaas.config: org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
    target.cluster.security.protocol: "SASL_SSL"
    target.cluster.sasl.mechanism: "OAUTHBEARER"
    target.cluster.sasl.login.callback.handler.class: "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler"
    target.cluster.sasl.jaas.config: "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
    




###  Terraform 

You can use a Terraform resource to create a [connector](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/managed_kafka_connector).
    
    
    # A single MirrorMaker 2 Source Connector to replicate from one source to one target.
    resource "google_managed_kafka_connector" "default" {
      project         = data.google_project.default.project_id
      connector_id    = "mm2-source-to-target-connector-id"
      connect_cluster = google_managed_kafka_connect_cluster.default.connect_cluster_id
      location        = "us-central1"
    
      configs = {
        "connector.class"      = "org.apache.kafka.connect.mirror.MirrorSourceConnector"
        "name"                 = "mm2-source-to-target-connector-id"
        "tasks.max"            = "3"
        "source.cluster.alias" = "source"
        "target.cluster.alias" = "target"
        "topics"               = ".*" # Replicate all topics from the source
        # The value for bootstrap.servers is a comma-separated list of hostname:port pairs
        # for one or more Kafka brokers in the source/target cluster.
        "source.cluster.bootstrap.servers" = "source_cluster_dns"
        "target.cluster.bootstrap.servers" = "target_cluster_dns"
        # You can define an exclusion policy for topics as follows:
        # To exclude internal MirrorMaker 2 topics, internal topics and replicated topics,.
        "topics.exclude" = "mm2.*\\.internal,.*\\.replica,__.*"
      }
    
      provider = google-beta
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    )
    
    // createMirrorMaker2SourceConnector creates a MirrorMaker 2.0 Source connector.
    func createMirrorMaker2SourceConnector(w io.Writer, projectID, region, connectClusterID, connectorID, sourceBootstrapServers, targetBootstrapServers, tasksMax, sourceClusterAlias, targetClusterAlias, topics, topicsExclude string, opts ...option.ClientOption) error {
    	// TODO(developer): Update with your config values. Here is a sample configuration:
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "mm2-source-to-target-connector-id"
    	// sourceBootstrapServers := "source_cluster_dns"
    	// targetBootstrapServers := "target_cluster_dns"
    	// tasksMax := "3"
    	// sourceClusterAlias := "source"
    	// targetClusterAlias := "target"
    	// topics := ".*"
    	// topicsExclude := "mm2.*.internal,.*.replica,__.*"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s", projectID, region, connectClusterID)
    
    	config := map[string]string{
    		"connector.class":      "org.apache.kafka.connect.mirror.MirrorSourceConnector",
    		"name":                 connectorID,
    		"tasks.max":            tasksMax,
    		"source.cluster.alias": sourceClusterAlias,
    		"target.cluster.alias": targetClusterAlias, // This is usually the primary cluster.
    		// Replicate all topics from the source
    		"topics": topics,
    		// The value for bootstrap.servers is a hostname:port pair for the Kafka broker in
    		// the source/target cluster.
    		// For example: "kafka-broker:9092"
    		"source.cluster.bootstrap.servers": sourceBootstrapServers,
    		"target.cluster.bootstrap.servers": targetBootstrapServers,
    		// You can define an exclusion policy for topics as follows:
    		// To exclude internal MirrorMaker 2 topics, internal topics and replicated topics.
    		// topicsExclude := "mm2.*.internal,.*.replica,__.*"
    		"topics.exclude": topicsExclude,
    	}
    
    	connector := &managedkafkapb.Connector{
    		Name:    fmt.Sprintf("%s/connectors/%s", parent, connectorID),
    		Configs: config,
    	}
    
    	req := &managedkafkapb.CreateConnectorRequest{
    		Parent:      parent,
    		ConnectorId: connectorID,
    		Connector:   connector,
    	}
    
    	resp, err := client.CreateConnector(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateConnector got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created MirrorMaker 2.0 Source connector: %s\n", resp.Name)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html);
    import com.google.cloud.managedkafka.v1.[Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html);
    import com.google.cloud.managedkafka.v1.[ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html);
    import com.google.cloud.managedkafka.v1.[CreateConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class CreateMirrorMaker2SourceConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String maxTasks = "3";
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-mirrormaker2-connector";
        String sourceClusterBootstrapServers = "my-source-cluster:9092";
        String targetClusterBootstrapServers = "my-target-cluster:9092";
        String sourceClusterAlias = "source";
        String targetClusterAlias = "target"; // This is usually the primary cluster.
        String connectorClass = "org.apache.kafka.connect.mirror.MirrorSourceConnector";
        String topics = ".*";
        // You can define an exclusion policy for topics as follows:
        // To exclude internal MirrorMaker 2 topics, internal topics and replicated topics.
        String topicsExclude = "mm2.*.internal,.*.replica,__.*";
        createMirrorMaker2SourceConnector(
            projectId,
            region,
            maxTasks,
            connectClusterId,
            connectorId,
            sourceClusterBootstrapServers,
            targetClusterBootstrapServers,
            sourceClusterAlias,
            targetClusterAlias,
            connectorClass,
            topics,
            topicsExclude);
      }
    
      public static void createMirrorMaker2SourceConnector(
          String projectId,
          String region,
          String maxTasks,
          String connectClusterId,
          String connectorId,
          String sourceClusterBootstrapServers,
          String targetClusterBootstrapServers,
          String sourceClusterAlias,
          String targetClusterAlias,
          String connectorClass,
          String topics,
          String topicsExclude)
          throws Exception {
    
        // Build the connector configuration
        Map<String, String> configMap = new HashMap<>();
        configMap.put("tasks.max", maxTasks);
        configMap.put("connector.class", connectorClass);
        configMap.put("name", connectorId);
        configMap.put("source.cluster.alias", sourceClusterAlias);
        configMap.put("target.cluster.alias", targetClusterAlias);
        configMap.put("topics", topics);
        configMap.put("topics.exclude", topicsExclude);
        configMap.put("source.cluster.bootstrap.servers", sourceClusterBootstrapServers);
        configMap.put("target.cluster.bootstrap.servers", targetClusterBootstrapServers);
    
        [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) connector = [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html).newBuilder()
            .setName(
                [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, connectClusterId, connectorId).toString())
            .putAllConfigs(configMap)
            .build();
    
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [CreateConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.html) request = [CreateConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.html).newBuilder()
              .setParent([ConnectClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectClusterName.html).of(projectId, region, connectClusterId).toString())
              .[setConnectorId](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.CreateConnectorRequest.Builder.html#com_google_cloud_managedkafka_v1_CreateConnectorRequest_Builder_setConnectorId_java_lang_String_)(connectorId)
              .setConnector(connector)
              .build();
    
          // This operation is being handled synchronously.
          [Connector](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html) response = managedKafkaConnectClient.createConnector(request);
          System.out.printf("Created MirrorMaker2 Source connector: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.Connector.html#com_google_cloud_managedkafka_v1_Connector_getName__)());
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.createConnector got err: %s\n", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        ManagedKafkaConnectClient,
    )
    from google.cloud.managedkafka_v1.types import Connector, CreateConnectorRequest
    
    connect_client = ManagedKafkaConnectClient()
    parent = connect_client.connect_cluster_path(project_id, region, connect_cluster_id)
    
    configs = {
        "connector.class": "org.apache.kafka.connect.mirror.MirrorSourceConnector",
        "name": connector_id,
        "tasks.max": tasks_max,
        "source.cluster.alias": source_cluster_alias,
        "target.cluster.alias": target_cluster_alias,  # This is usually the primary cluster.
        # Replicate all topics from the source
        "topics": topics,
        # The value for bootstrap.servers is a hostname:port pair for the Kafka broker in
        # the source/target cluster.
        # For example: "kafka-broker:9092"
        "source.cluster.bootstrap.servers": source_bootstrap_servers,
        "target.cluster.bootstrap.servers": target_bootstrap_servers,
        # You can define an exclusion policy for topics as follows:
        # To exclude internal MirrorMaker 2 topics, internal topics and replicated topics.
        "topics.exclude": topics_exclude,
    }
    
    connector = Connector()
    # The name of the connector.
    connector.name = connector_id
    connector.configs = configs
    
    request = CreateConnectorRequest(
        parent=parent,
        connector_id=connector_id,
        connector=connector,
    )
    
    try:
        operation = connect_client.create_connector(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        response = operation.result()
        print("Created Connector:", response)
    except GoogleAPICallError as e:
        print(f"The operation failed with error: {e}")

## What's next?

  * [Replicate Kafka topics with MirrorMaker 2.0](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/replicate-kafka-topics)

  * [Troubleshoot a MirrorMaker 2.0 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-mirrormaker-connector)

  * [Pause, resume, stop, and restart a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/pause-resume-stop-restart-connector)

  * [View the details of a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connector)

  * [Update a connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connector)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
