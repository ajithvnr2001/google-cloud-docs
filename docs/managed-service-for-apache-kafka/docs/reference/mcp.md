---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/
title: MCP Reference: managedkafka \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:54.722479+00:00
---

# MCP Reference: managedkafka  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/apis)



Send feedback 

#  MCP Reference: managedkafka Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

Google Cloud Managed service for Apache Kafka allows agents to provision and view Kafka resources. Managed Service for Apache Kafka is also known as Managed Kafka.

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The managedkafka MCP server has the following MCP endpoint:

  * https://managedkafka.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

The managedkafka MCP server has the following tools:

MCP Tools  
---  
[create_cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/create_cluster) |  Create a new cluster for Google Cloud Managed service for Apache Kafka.This tool returns a long-running operation (LRO) that you can poll using the `get_operation` tool to track the cluster creation status. Cluster creation can take 30 minutes or longer.**Important Notes:**

  * Do not create the cluster without getting all of the required parameters from the user.

  
[update_cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/update_cluster) |  Update an existing Google Cloud Managed service for Apache Kafka cluster.This tool returns a long-running operation (LRO) that you can poll using the `get_operation` tool to track the cluster update status. Cluster updates can take 20 minutes or longer.**Important Notes:**

  * When calling update_cluster, you must provide the name of the cluster to update, formatted as `projects/{project}/locations/{location}/clusters/{cluster}`.
  * Do not update the cluster without getting all of the required parameters from the user.
  * To clear a field, use the `fields_to_clear` parameter with a list of field masks (e.g. `["labels", "tls_config"]`).

  
[delete_cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_cluster) |  Deletes a Google Cloud Managed Service for Apache Kafka cluster.This tool returns a long-running operation (LRO) that you can poll using the `get_operation` tool to track the cluster deletion status. Cluster deletions can take 10 minutes or longer.  
[get_cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_cluster) |  Get the details of an existing Google Cloud Managed Service for Apache Kafka cluster.   
[list_clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/list_clusters) |  Lists all clusters for Google Cloud Managed service for Apache Kafka in a given project and location.   
[get_operation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_operation) |  Get the status of a long-running operation (LRO).**Usage** Some tools (`create_cluster` and `update_cluster`) return a long-running operation. You can use this tool to get the status of the operation.**Parameters**

  * `name`: The name of the operation to get. It corresponds to the `name` field in the long-running operation. It should be in the format of `projects/{project}/locations/{location}/operations/{operation}`.

**Returns**

  * An `Operation` object that contains the status of the operation.
  * If the operation is not complete, the response will be empty.
  * If the operation is complete, the response will contain either: 
    * A `response` field that contains the result of the operation and indicates that it was successful.
    * A `error` field that indicates any errors that occurred during the operation.

  
[create_topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/create_topic) |  Create a new Google Cloud Managed Service for Apache Kafka topic.   
[update_topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/update_topic) |  Update an existing Google Cloud Managed service for Apache Kafka topic.**Important Notes:**

  * The UpdateTopic request requires the name of the topic to be updated in the format `projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}`.

  
[delete_topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_topic) |  Deletes a Google Cloud Managed Service for Apache Kafka topic.   
[get_topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_topic) |  Get the details of an existing Google Cloud Managed Service for Apache Kafka topic.   
[list_topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/list_topics) |  List all topics for Google Cloud Managed Service for Apache Kafka for a given project, location, and cluster.   
[update_consumer_group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/update_consumer_group) |  Update an existing Google Cloud Managed Service for Apache Kafka consumer group. This tool can only be used to update the offsets for topics consumed by the group.**Important Notes:**

  * To update a consumer group's offsets, the consumer group must be inactive (i.e., there are no active consumers in the group), and topics with new offsets must be provided.
  * Before making an update, the agent should call `get_consumer_group` to retrieve the current consumer group configuration.

  
[delete_consumer_group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_consumer_group) |  Deletes a Google Cloud Managed Service for Apache Kafka consumer group.   
[get_consumer_group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_consumer_group) |  Get the details of an existing Google Cloud Managed Service for Apache Kafka consumer group.   
[list_consumer_groups](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/list_consumer_groups) |  List all consumer groups for Google Cloud Managed Service for Apache Kafka for a given project, location, and cluster.   
[get_acl](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_acl) |  Get the details of an existing Google Cloud Managed Service for Apache Kafka ACL.   
[list_acls](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/list_acls) |  List all ACLs for Google Cloud Managed Service for Apache Kafka for a given project, location, and cluster.   
[add_acl_entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/add_acl_entry) |  Adds an ACL entry to an existing Google Cloud Managed Service for Apache Kafka ACL. If the ACL does not exist, it will be created. The following fields must be provided: * `cluster` (required): The cluster in which to add the ACL entry. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`. * `resource_type` (required): The resource type for the ACL. Accepted values: CLUSTER, TOPIC, CONSUMER_GROUP, TRANSACTIONAL_ID. * `resource_name` (required): The resource name for the ACL. Can be the wildcard literal "*". * `pattern_type` (optional): The pattern type for the ACL. Accepted values: LITERAL, PREFIXED. If not specified, defaults to LITERAL. * `principal` (required): The principal. Specified as Google Cloud account, with the Kafka StandardAuthorizer prefix "User:". For example: `"User:test-kafka-client@test-project.iam.gserviceaccount.com"`. Can be the wildcard "User:*" to refer to all users. * `operation` (required): The operation type. Allowed values are (case insensitive): ALL, READ, WRITE, CREATE, DELETE, ALTER, DESCRIBE, CLUSTER_ACTION, DESCRIBE_CONFIGS, ALTER_CONFIGS, and IDEMPOTENT_WRITE. * `permission_type` (optional): The permission type. Accepted values are (case insensitive): ALLOW, DENY. If not specified, defaults to ALLOW.**Important Notes:**

  * Certain resource types only allow certain operations. 
    * For the `cluster` resource type, only CREATE, CLUSTER_ACTION, DESCRIBE_CONFIGS, ALTER_CONFIGS, IDEMPOTENT_WRITE, ALTER, DESCRIBE, and ALL are allowed.
    * For the `topic` resource type, only READ, WRITE, CREATE, DESCRIBE, DELETE, ALTER, DESCRIBE_CONFIGS, ALTER_CONFIGS, and ALL are allowed.
    * For the `consumerGroup` resource type, only READ, DESCRIBE, DELETE, and ALL are allowed.
    * For the `transactionalId` resource type only DESCRIBE, WRITE, and ALL are allowed.

  
[remove_acl_entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/remove_acl_entry) |  Removes an ACL entry from an existing Google Cloud Managed service for Apache Kafka ACL. If the removed entry was the last one in the ACL, the ACL will be deleted. The following fields must be provided: * `cluster` (required): The cluster in which to remove the ACL entry. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`. * `resource_type` (required): The resource type for the ACL. Accepted values: CLUSTER, TOPIC, CONSUMER_GROUP, TRANSACTIONAL_ID. * `resource_name` (required): The resource name for the ACL. Can be the wildcard literal "*". * `pattern_type` (optional): The pattern type for the ACL. Accepted values: LITERAL, PREFIXED. If not specified, defaults to LITERAL. * `principal` (required): The principal. Specified as Google Cloud account, with the Kafka StandardAuthorizer prefix "User:". For example: `"User:test-kafka-client@test-project.iam.gserviceaccount.com"`. Can be the wildcard "User:*" to refer to all users. * `operation` (required): The operation type. Allowed values are (case insensitive): ALL, READ, WRITE, CREATE, DELETE, ALTER, DESCRIBE, CLUSTER_ACTION, DESCRIBE_CONFIGS, ALTER_CONFIGS, and IDEMPOTENT_WRITE. * `permission_type` (optional): The permission type. Accepted values are (case insensitive): ALLOW, DENY. If not specified, defaults to ALLOW.   
[create_connect_cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/create_connect_cluster) |  Create a new Google Cloud Managed Service for Apache Kafka Connect cluster.This tool returns a long-running operation (LRO) that you can poll using the `get_operation` tool to track the Connect cluster creation status. Connect cluster creation can take 20 minutes or longer.**Important Notes:**

  * Do not create the connect cluster without getting all of the required parameters first.

  
[update_connect_cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/update_connect_cluster) |  Update an existing Google Cloud Managed service for Apache Kafka Connect cluster.This tool returns a long-running operation (LRO) that you can poll using the `get_operation` tool to track the Connect cluster update status. Connect cluster updates can take 20 minutes or longer.**Important Notes:**

  * When calling update_connect_cluster, you must provide the name of the Connect cluster to update, formatted as `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.
  * The `kafka_cluster` field is immutable and cannot be updated after creation.
  * To clear a field, use the `fields_to_clear` parameter with a list of field masks.

  
[delete_connect_cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_connect_cluster) |  Deletes a Google Cloud Managed service for Apache Kafka Connect cluster.This tool returns a long-running operation (LRO) that you can poll using the `get_operation` tool to track the Connect cluster deletion status. Connect cluster deletions can take 10 minutes or longer.  
[get_connect_cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_connect_cluster) |  Get the details of an existing Google Cloud Managed service for Apache Kafka Connect cluster.   
[list_connect_clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/list_connect_clusters) |  List all Connect clusters for Google Cloud Managed Service for Apache Kafka Connect for a given project and location.   
[create_connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/create_connector) |  Create a new Google Cloud Managed service for Apache Kafka Connect connector.The user should first be prompted on which connector type they want to create, and then provide the necessary properties for that connector type in the `configs` field. Only use the example configuration for reference. The following connector types are supported:

  * **`configs` (required):** Key-value pairs for connector properties. The available connector types are: 
    * MirrorMaker 2.0 Source connector 
      * Example Configuration: 
        * `connector.class` (required): "org.apache.kafka.connect.mirror.MirrorSourceConnector"
        * `name`: "MM2_CONNECTOR_ID"
        * `source.cluster.alias` (required): "source"
        * `target.cluster.alias` (required): "target"
        * `topics` (required): "TOPIC_NAME"
        * `source.cluster.bootstrap.servers` (required): "SOURCE_CLUSTER_DNS"
        * `target.cluster.bootstrap.servers` (required): "TARGET_CLUSTER_DNS"
        * `offset-syncs.topic.replication.factor`: "1"
        * `source.cluster.security.protocol`: "SASL_SSL"
        * `source.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `source.cluster.sasl.login.callback.handler.class`: com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
        * `source.cluster.sasl.jaas.config`: org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
        * `target.cluster.security.protocol`: "SASL_SSL"
        * `target.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `target.cluster.sasl.login.callback.handler.class`: "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler"
        * `target.cluster.sasl.jaas.config`: "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"
      * Replace with these: 
        * `MM2_CONNECTOR_ID`: The ID or name of the MirrorMaker 2.0 Source connector.
        * `TOPIC_NAME`: The name of the Kafka topic(s) to mirror.
        * `SOURCE_CLUSTER_DNS`: The DNS endpoint for the source Kafka cluster.
        * `TARGET_CLUSTER_DNS`: The DNS endpoint for the target Kafka cluster.
    * MirrorMaker 2.0 Checkpoint connector 
      * Example Configuration: 
        * `connector.class` (required): "org.apache.kafka.connect.mirror.MirrorCheckpointConnector"
        * `name`: "MM2_CONNECTOR_ID"
        * `source.cluster.alias` (required): "source"
        * `target.cluster.alias` (required): "target"
        * `consumer-groups` (required): "CONSUMER_GROUP_NAME"
        * `source.cluster.bootstrap.servers` (required): "SOURCE_CLUSTER_DNS"
        * `target.cluster.bootstrap.servers` (required): "TARGET_CLUSTER_DNS"
        * `source.cluster.security.protocol`: "SASL_SSL"
        * `source.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `source.cluster.sasl.login.callback.handler.class`: com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
        * `source.cluster.sasl.jaas.config`: org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
        * `target.cluster.security.protocol`: "SASL_SSL"
        * `target.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `target.cluster.sasl.login.callback.handler.class`: "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler"
        * `target.cluster.sasl.jaas.config`: "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"
      * Replace with these: 
        * `MM2_CONNECTOR_ID`: The ID or name of the MirrorMaker 2.0 Source connector.
        * `CONSUMER_GROUP_NAME`: The name of the consumer group to use for the checkpoint connector.
        * `SOURCE_CLUSTER_DNS`: The DNS endpoint for the source Kafka cluster.
        * `TARGET_CLUSTER_DNS`: The DNS endpoint for the target Kafka cluster.
    * MirrorMaker 2.0 Heartbeat connector 
      * Example Configuration: 
        * `connector.class` (required): "org.apache.kafka.connect.mirror.MirrorHeartbeatConnector"
        * `name`: "MM2_CONNECTOR_ID"
        * `source.cluster.alias` (required): "source"
        * `target.cluster.alias` (required): "target"
        * `consumer-groups` (required): "CONSUMER_GROUP_NAME"
        * `source.cluster.bootstrap.servers` (required): "SOURCE_CLUSTER_DNS"
        * `target.cluster.bootstrap.servers` (required): "TARGET_CLUSTER_DNS"
        * `source.cluster.security.protocol`: "SASL_SSL"
        * `source.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `source.cluster.sasl.login.callback.handler.class`: com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
        * `source.cluster.sasl.jaas.config`: org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
        * `target.cluster.security.protocol`: "SASL_SSL"
        * `target.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `target.cluster.sasl.login.callback.handler.class`: "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler"
        * `target.cluster.sasl.jaas.config`: "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"
      * Replace with these: 
        * `MM2_CONNECTOR_ID`: The ID or name of the MirrorMaker 2.0 Heartbeat connector.
        * `CONSUMER_GROUP_NAME`: The name of the consumer group to use for the heartbeat connector.
        * `SOURCE_CLUSTER_DNS`: The DNS endpoint for the source Kafka cluster.
        * `TARGET_CLUSTER_DNS`: The DNS endpoint for the target Kafka cluster.
    * BigQuery Sink connector 
      * Example Configuration: 
        * `name`: "BQ_SINK_CONNECTOR_ID"
        * `project` (required): "GCP_PROJECT_ID"
        * `topics`: "TOPIC_ID"
        * `tasks.max`: "3"
        * `connector.class` (required): "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector"
        * `key.converter`: "org.apache.kafka.connect.storage.StringConverter"
        * `value.converter`: "org.apache.kafka.connect.json.JsonConverter"
        * `value.converter.schemas.enable`: "false"
        * `defaultDataset` (`required`): "BQ_DATASET_ID"
      * Replace with these: 
        * `BQ_SINK_CONNECTOR_ID`: The ID or name of the BigQuery Sink connector. The name of a connector is immutable.
        * `GCP_PROJECT_ID`: The ID of the Google Cloud project where your BigQuery dataset resides.
        * `TOPIC_ID`: The ID of the Managed Service for Apache Kafka topic from which the data flows to the BigQuery Sink connector.
        * `BQ_DATASET_ID`: The ID of the BigQuery dataset that acts as the sink for the pipeline.
    * Cloud Storage Sink connector 
      * Example Configuration: 
        * `name`: "GCS_SINK_CONNECTOR_ID"
        * `connector.class` (required): "io.aiven.kafka.connect.gcs.GcsSinkConnector"
        * `tasks.max`: "1"
        * `topics` (required): "TOPIC_ID"
        * `gcs.bucket.name` (required): "GCS_BUCKET_NAME"
        * `gcs.credentials.default`: "true"
        * `format.output.type`: "json"
        * `value.converter`: "org.apache.kafka.connect.json.JsonConverter"
        * `value.converter.schemas.enable`: "false"
        * `key.converter`: "org.apache.kafka.connect.storage.StringConverter"
      * Replace with these: 
        * `TOPIC_ID`: The ID of the Managed Service for Apache Kafka topic from which the data flows to the Cloud Storage Sink connector.
        * `GCS_BUCKET_NAME`: The name of the Cloud Storage bucket that acts as a sink for the pipeline.
        * `GCS_SINK_CONNECTOR_ID`: The ID or name of the Cloud Storage Sink connector. The name of a connector is immutable.
    * Pub/Sub Source connector 
      * Example Configuration: 
        * `connector.class` (required): "com.google.pubsub.kafka.source.CloudPubSubSourceConnector"
        * `cps.project` (required): "PROJECT_ID"
        * `cps.subscription` (required): "PUBSUB_SUBSCRIPTION_ID"
        * `kafka.topic` (required): "KAFKA_TOPIC_ID"
        * `value.converter`: "org.apache.kafka.connect.converters.ByteArrayConverter"
        * `key.converter`: "org.apache.kafka.connect.storage.StringConverter"
        * `tasks.max`: "3"
      * Replace with these: 
        * `PROJECT_ID`: The ID of the Google Cloud project where the Pub/Sub subscription resides.
        * `PUBSUB_SUBSCRIPTION_ID`: The ID of the Pub/Sub subscription to pull data from.
        * `KAFKA_TOPIC_ID`: The ID of the Kafka topic where data is written.
    * Pub/Sub Sink connector 
      * Example Configuration: 
        * `connector.class`: "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector"
        * `name`: "CPS_SINK_CONNECTOR_ID"
        * `tasks.max`: "1"
        * `topics`: "TOPIC_ID"
        * `value.converter`: "org.apache.kafka.connect.storage.StringConverter"
        * `key.converter`: "org.apache.kafka.connect.storage.StringConverter"
        * `cps.topic`: "CPS_TOPIC_ID"
        * `cps.project`: "GCP_PROJECT_ID"
      * Replace with these: 
        * `CPS_SINK_CONNECTOR_ID`: The ID or name of the Pub/Sub Sink connector. The name of a connector is immutable.
        * `TOPIC_ID`: The ID of the Managed Service for Apache Kafka topic from which data is read by the Pub/Sub Sink connector.
        * `CPS_TOPIC_ID`: The ID of the Pub/Sub topic to which data is published.
        * `GCP_PROJECT_ID`: The ID of the Google Cloud project where your Pub/Sub topic resides.
  * **`task_restart_policy` (optional):** A policy that specifies how to restart failed connector tasks. If not set, failed tasks won't be restarted. 
    * **`minimum_backoff` (optional):** The minimum amount of time to wait before retrying a failed task (e.g., "60s"). Defaults to 60 seconds.
    * **`maximum_backoff` (optional):** The maximum amount of time to wait before retrying a failed task (e.g., "43200s" for 12 hours). Defaults to 12 hours.
    * **`task_retry_disabled` (optional):** If true, task retry is disabled.

**Important Notes:**

  * The configs field should be formatted as a JSON object, for example: `"configs":{"name":"my-connector","tasks.max":"1","gcs.bucket.name",...}`. Do not add unnecessary quotes around the keys or values.

  
[update_connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/update_connector) |  Update an existing Google Cloud Managed Service for Apache Kafka Connect connector.The `configs` field can be updated. The agent can first use the `get_connector` method to get the current connector configuration, to provide a baseline configuration for the user to edit. Use the example configurations provided below for reference.

  * **configs:** Key-value pairs for connector properties. The following connectors support configuration updates: 
    * MirrorMaker 2.0 Source connector 
      * Example Configuration: 
        * `connector.class` (required): "org.apache.kafka.connect.mirror.MirrorSourceConnector"
        * `name`: "MM2_CONNECTOR_ID"
        * `source.cluster.alias` (required): "source"
        * `target.cluster.alias` (required): "target"
        * `topics` (required): "TOPIC_NAME"
        * `source.cluster.bootstrap.servers` (required): "SOURCE_CLUSTER_DNS"
        * `target.cluster.bootstrap.servers` (required): "TARGET_CLUSTER_DNS"
        * `offset-syncs.topic.replication.factor`: "1"
        * `source.cluster.security.protocol`: "SASL_SSL"
        * `source.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `source.cluster.sasl.login.callback.handler.class`: com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
        * `source.cluster.sasl.jaas.config`: org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
        * `target.cluster.security.protocol`: "SASL_SSL"
        * `target.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `target.cluster.sasl.login.callback.handler.class`: "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler"
        * `target.cluster.sasl.jaas.config`: "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"
      * Replace with these: 
        * `MM2_CONNECTOR_ID`: The ID or name of the MirrorMaker 2.0 Source connector.
        * `TOPIC_NAME`: The name of the Kafka topic(s) to mirror.
        * `SOURCE_CLUSTER_DNS`: The DNS endpoint for the source Kafka cluster.
        * `TARGET_CLUSTER_DNS`: The DNS endpoint for the target Kafka cluster.
    * MirrorMaker 2.0 Checkpoint connector 
      * Example Configuration: 
        * `connector.class` (required): "org.apache.kafka.connect.mirror.MirrorCheckpointConnector"
        * `name`: "MM2_CONNECTOR_ID"
        * `source.cluster.alias` (required): "source"
        * `target.cluster.alias` (required): "target"
        * `consumer-groups` (required): "CONSUMER_GROUP_NAME"
        * `source.cluster.bootstrap.servers` (required): "SOURCE_CLUSTER_DNS"
        * `target.cluster.bootstrap.servers` (required): "TARGET_CLUSTER_DNS"
        * `source.cluster.security.protocol`: "SASL_SSL"
        * `source.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `source.cluster.sasl.login.callback.handler.class`: com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
        * `source.cluster.sasl.jaas.config`: org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
        * `target.cluster.security.protocol`: "SASL_SSL"
        * `target.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `target.cluster.sasl.login.callback.handler.class`: "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler"
        * `target.cluster.sasl.jaas.config`: "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"
      * Replace with these: 
        * `MM2_CONNECTOR_ID`: The ID or name of the MirrorMaker 2.0 Source connector.
        * `CONSUMER_GROUP_NAME`: The name of the consumer group to use for the checkpoint connector.
        * `SOURCE_CLUSTER_DNS`: The DNS endpoint for the source Kafka cluster.
        * `TARGET_CLUSTER_DNS`: The DNS endpoint for the target Kafka cluster.
    * MirrorMaker 2.0 Heartbeat connector 
      * Example Configuration: 
        * `connector.class` (required): "org.apache.kafka.connect.mirror.MirrorHeartbeatConnector"
        * `name`: "MM2_CONNECTOR_ID"
        * `source.cluster.alias` (required): "source"
        * `target.cluster.alias` (required): "target"
        * `consumer-groups` (required): "CONSUMER_GROUP_NAME"
        * `source.cluster.bootstrap.servers` (required): "SOURCE_CLUSTER_DNS"
        * `target.cluster.bootstrap.servers` (required): "TARGET_CLUSTER_DNS"
        * `source.cluster.security.protocol`: "SASL_SSL"
        * `source.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `source.cluster.sasl.login.callback.handler.class`: com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
        * `source.cluster.sasl.jaas.config`: org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
        * `target.cluster.security.protocol`: "SASL_SSL"
        * `target.cluster.sasl.mechanism`: "OAUTHBEARER"
        * `target.cluster.sasl.login.callback.handler.class`: "com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler"
        * `target.cluster.sasl.jaas.config`: "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;"
      * Replace with these: 
        * `MM2_CONNECTOR_ID`: The ID or name of the MirrorMaker 2.0 Heartbeat connector.
        * `CONSUMER_GROUP_NAME`: The name of the consumer group to use for the heartbeat connector.
        * `SOURCE_CLUSTER_DNS`: The DNS endpoint for the source Kafka cluster.
        * `TARGET_CLUSTER_DNS`: The DNS endpoint for the target Kafka cluster.
    * BigQuery Sink connector 
      * Example Configuration: 
        * `name`: "BQ_SINK_CONNECTOR_ID"
        * `project` (required): "GCP_PROJECT_ID"
        * `topics`: "TOPIC_ID"
        * `tasks.max`: "3"
        * `connector.class` (required): "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector"
        * `key.converter`: "org.apache.kafka.connect.storage.StringConverter"
        * `value.converter`: "org.apache.kafka.connect.json.JsonConverter"
        * `value.converter.schemas.enable`: "false"
        * `defaultDataset` (`required`): "BQ_DATASET_ID"
      * Replace with these: 
        * `BQ_SINK_CONNECTOR_ID`: The ID or name of the BigQuery Sink connector. The name of a connector is immutable.
        * `GCP_PROJECT_ID`: The ID of the Google Cloud project where your BigQuery dataset resides.
        * `TOPIC_ID`: The ID of the Managed Service for Apache Kafka topic from which the data flows to the BigQuery Sink connector.
        * `BQ_DATASET_ID`: The ID of the BigQuery dataset that acts as the sink for the pipeline.
    * Cloud Storage Sink connector 
      * Example Configuration: 
        * `name`: "GCS_SINK_CONNECTOR_ID"
        * `connector.class` (required): "io.aiven.kafka.connect.gcs.GcsSinkConnector"
        * `tasks.max`: "1"
        * `topics` (required): "TOPIC_ID"
        * `gcs.bucket.name` (required): "GCS_BUCKET_NAME"
        * `gcs.credentials.default`: "true"
        * `format.output.type`: "json"
        * `value.converter`: "org.apache.kafka.connect.json.JsonConverter"
        * `value.converter.schemas.enable`: "false"
        * `key.converter`: "org.apache.kafka.connect.storage.StringConverter"
      * Replace with these: 
        * `TOPIC_ID`: The ID of the Managed Service for Apache Kafka topic from which the data flows to the Cloud Storage Sink connector.
        * `GCS_BUCKET_NAME`: The name of the Cloud Storage bucket that acts as a sink for the pipeline.
        * `GCS_SINK_CONNECTOR_ID`: The ID or name of the Cloud Storage Sink connector. The name of a connector is immutable.
    * Pub/Sub Source connector 
      * Example Configuration: 
        * `connector.class` (required): "com.google.pubsub.kafka.source.CloudPubSubSourceConnector"
        * `cps.project` (required): "PROJECT_ID"
        * `cps.subscription` (required): "PUBSUB_SUBSCRIPTION_ID"
        * `kafka.topic` (required): "KAFKA_TOPIC_ID"
        * `value.converter`: "org.apache.kafka.connect.converters.ByteArrayConverter"
        * `key.converter`: "org.apache.kafka.connect.storage.StringConverter"
        * `tasks.max`: "3"
      * Replace with these: 
        * `PROJECT_ID`: The ID of the Google Cloud project where the Pub/Sub subscription resides.
        * `PUBSUB_SUBSCRIPTION_ID`: The ID of the Pub/Sub subscription to pull data from.
        * `KAFKA_TOPIC_ID`: The ID of the Kafka topic where data is written.
    * Pub/Sub Sink connector 
      * Example Configuration: 
        * `connector.class`: "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector"
        * `name`: "CPS_SINK_CONNECTOR_ID"
        * `tasks.max`: "1"
        * `topics`: "TOPIC_ID"
        * `value.converter`: "org.apache.kafka.connect.storage.StringConverter"
        * `key.converter`: "org.apache.kafka.connect.storage.StringConverter"
        * `cps.topic`: "CPS_TOPIC_ID"
        * `cps.project`: "GCP_PROJECT_ID"
      * Replace with these: 
        * `CPS_SINK_CONNECTOR_ID`: The ID or name of the Pub/Sub Sink connector. The name of a connector is immutable.
        * `TOPIC_ID`: The ID of the Managed Service for Apache Kafka topic from which data is read by the Pub/Sub Sink connector.
        * `CPS_TOPIC_ID`: The ID of the Pub/Sub topic to which data is published.
        * `GCP_PROJECT_ID`: The ID of the Google Cloud project where your Pub/Sub topic resides.
  * **`task_restart_policy` (optional):** A policy that specifies how to restart failed connector tasks. If not set, failed tasks won't be restarted. 
    * **`minimum_backoff` (optional):** The minimum amount of time to wait before retrying a failed task (e.g., "60s"). Defaults to 60 seconds.
    * **`maximum_backoff` (optional):** The maximum amount of time to wait before retrying a failed task (e.g., "43200s" for 12 hours). Defaults to 12 hours.
    * **`task_retry_disabled` (optional):** If true, task retry is disabled.

**Important Notes:**

  * When calling update_connector, you must provide the name of the connector to update, formatted as `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}/connectors/{connector_id}`.

  
[delete_connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/delete_connector) |  Deletes a Google Cloud Managed Service for Apache Kafka Connect connector.   
[get_connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_connector) |  Get the details of an existing Google Cloud Managed Service for Apache Kafka Connect connector.   
[list_connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/list_connectors) |  List all connectors for Google Cloud Managed Service for Apache Kafka Connect for a given project, location, and Connect cluster.   
[pause_connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/pause_connector) |  Pauses a Google Cloud Managed service for Apache Kafka Connect connector and its tasks.   
[resume_connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/resume_connector) |  Resumes a Google Cloud Managed service for Apache Kafka Connect connector and its tasks.   
[restart_connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/restart_connector) |  Restarts a Google Cloud Managed service for Apache Kafka Connect Connector.   
[stop_connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/stop_connector) |  Stops a Google Cloud Managed service for Apache Kafka Connect connector.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          curl --location 'https://managedkafka.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
