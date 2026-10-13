---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/summary_class/
title: Package Classes (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:53.031283+00:00
---

# Package Classes (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.12 

Summary of entries of Classes for google-cloud-managedkafka.

## Classes 

### [ManagedKafkaAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaAsyncClient)

The service that a client application uses to manage Apache Kafka clusters, topics and consumer groups.

### [ManagedKafkaClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.ManagedKafkaClient)

The service that a client application uses to manage Apache Kafka clusters, topics and consumer groups.

### [ListAclsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers.ListAclsAsyncPager)

A pager for iterating through `list_acls` requests.

This class thinly wraps an initial [ListAclsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListAclsResponse) object, and provides an `__aiter__` method to iterate through its `acls` field.

If there are more pages, the `__aiter__` method will make additional `ListAcls` requests and continue to iterate through the `acls` field on the corresponding responses.

All the usual [ListAclsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListAclsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAclsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers.ListAclsPager)

A pager for iterating through `list_acls` requests.

This class thinly wraps an initial [ListAclsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListAclsResponse) object, and provides an `__iter__` method to iterate through its `acls` field.

If there are more pages, the `__iter__` method will make additional `ListAcls` requests and continue to iterate through the `acls` field on the corresponding responses.

All the usual [ListAclsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListAclsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers.ListClustersAsyncPager)

A pager for iterating through `list_clusters` requests.

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListClustersResponse) object, and provides an `__aiter__` method to iterate through its `clusters` field.

If there are more pages, the `__aiter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers.ListClustersPager)

A pager for iterating through `list_clusters` requests.

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListClustersResponse) object, and provides an `__iter__` method to iterate through its `clusters` field.

If there are more pages, the `__iter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConsumerGroupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers.ListConsumerGroupsAsyncPager)

A pager for iterating through `list_consumer_groups` requests.

This class thinly wraps an initial [ListConsumerGroupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConsumerGroupsResponse) object, and provides an `__aiter__` method to iterate through its `consumer_groups` field.

If there are more pages, the `__aiter__` method will make additional `ListConsumerGroups` requests and continue to iterate through the `consumer_groups` field on the corresponding responses.

All the usual [ListConsumerGroupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConsumerGroupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConsumerGroupsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers.ListConsumerGroupsPager)

A pager for iterating through `list_consumer_groups` requests.

This class thinly wraps an initial [ListConsumerGroupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConsumerGroupsResponse) object, and provides an `__iter__` method to iterate through its `consumer_groups` field.

If there are more pages, the `__iter__` method will make additional `ListConsumerGroups` requests and continue to iterate through the `consumer_groups` field on the corresponding responses.

All the usual [ListConsumerGroupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConsumerGroupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTopicsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers.ListTopicsAsyncPager)

A pager for iterating through `list_topics` requests.

This class thinly wraps an initial [ListTopicsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListTopicsResponse) object, and provides an `__aiter__` method to iterate through its `topics` field.

If there are more pages, the `__aiter__` method will make additional `ListTopics` requests and continue to iterate through the `topics` field on the corresponding responses.

All the usual [ListTopicsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListTopicsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTopicsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers.ListTopicsPager)

A pager for iterating through `list_topics` requests.

This class thinly wraps an initial [ListTopicsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListTopicsResponse) object, and provides an `__iter__` method to iterate through its `topics` field.

If there are more pages, the `__iter__` method will make additional `ListTopics` requests and continue to iterate through the `topics` field on the corresponding responses.

All the usual [ListTopicsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListTopicsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ManagedKafkaConnectAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectAsyncClient)

The service that a client application uses to manage Apache Kafka Connect clusters and connectors.

### [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient)

The service that a client application uses to manage Apache Kafka Connect clusters and connectors.

### [ListConnectClustersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.pagers.ListConnectClustersAsyncPager)

A pager for iterating through `list_connect_clusters` requests.

This class thinly wraps an initial [ListConnectClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectClustersResponse) object, and provides an `__aiter__` method to iterate through its `connect_clusters` field.

If there are more pages, the `__aiter__` method will make additional `ListConnectClusters` requests and continue to iterate through the `connect_clusters` field on the corresponding responses.

All the usual [ListConnectClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConnectClustersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.pagers.ListConnectClustersPager)

A pager for iterating through `list_connect_clusters` requests.

This class thinly wraps an initial [ListConnectClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectClustersResponse) object, and provides an `__iter__` method to iterate through its `connect_clusters` field.

If there are more pages, the `__iter__` method will make additional `ListConnectClusters` requests and continue to iterate through the `connect_clusters` field on the corresponding responses.

All the usual [ListConnectClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConnectorsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.pagers.ListConnectorsAsyncPager)

A pager for iterating through `list_connectors` requests.

This class thinly wraps an initial [ListConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectorsResponse) object, and provides an `__aiter__` method to iterate through its `connectors` field.

If there are more pages, the `__aiter__` method will make additional `ListConnectors` requests and continue to iterate through the `connectors` field on the corresponding responses.

All the usual [ListConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConnectorsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.pagers.ListConnectorsPager)

A pager for iterating through `list_connectors` requests.

This class thinly wraps an initial [ListConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectorsResponse) object, and provides an `__iter__` method to iterate through its `connectors` field.

If there are more pages, the `__iter__` method will make additional `ListConnectors` requests and continue to iterate through the `connectors` field on the corresponding responses.

All the usual [ListConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AccessConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.AccessConfig)

The configuration of access to the Kafka cluster.

### [Acl](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Acl)

Represents the set of ACLs for a given Kafka Resource Pattern, which consists of resource_type, resource_name and pattern_type.

### [AclEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.AclEntry)

Represents the access granted for a given Resource Pattern in an ACL.

### [AddAclEntryRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.AddAclEntryRequest)

Request for AddAclEntry.

### [AddAclEntryResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.AddAclEntryResponse)

Response for AddAclEntry.

### [CapacityConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CapacityConfig)

A capacity configuration of a Kafka cluster.

### [Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Cluster)

An Apache Kafka cluster deployed in a location.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Cluster.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Cluster.State)

The state of the cluster.

### [ConnectAccessConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectAccessConfig)

The configuration of access to the Kafka Connect cluster.

### [ConnectCluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectCluster)

An Apache Kafka Connect cluster deployed in a location.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConfigEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectCluster.ConfigEntry)

The abstract base class for a message.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectCluster.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectCluster.State)

The state of the cluster.

### [ConnectGcpConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectGcpConfig)

Configuration properties for a Kafka Connect cluster deployed to Google Cloud Platform.

### [ConnectNetworkConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectNetworkConfig)

The configuration of a Virtual Private Cloud (VPC) network that can access the Kafka Connect cluster.

### [Connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Connector)

A Kafka Connect connector in a given ConnectCluster.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConfigsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Connector.ConfigsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Connector.State)

The state of the connector.

### [ConsumerGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConsumerGroup)

A Kafka consumer group in a given cluster.

### [TopicsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConsumerGroup.TopicsEntry)

The abstract base class for a message.

### [ConsumerPartitionMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConsumerPartitionMetadata)

Metadata for a consumer group corresponding to a specific partition.

### [ConsumerTopicMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConsumerTopicMetadata)

Metadata for a consumer group corresponding to a specific topic.

### [PartitionsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConsumerTopicMetadata.PartitionsEntry)

The abstract base class for a message.

### [CreateAclRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateAclRequest)

Request for CreateAcl.

### [CreateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateClusterRequest)

Request for CreateCluster.

### [CreateConnectClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateConnectClusterRequest)

Request for CreateConnectCluster.

### [CreateConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateConnectorRequest)

Request for CreateConnector.

### [CreateTopicRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateTopicRequest)

Request for CreateTopic.

### [DeleteAclRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.DeleteAclRequest)

Request for DeleteAcl.

### [DeleteClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.DeleteClusterRequest)

Request for DeleteCluster.

### [DeleteConnectClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.DeleteConnectClusterRequest)

Request for DeleteConnectCluster.

### [DeleteConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.DeleteConnectorRequest)

Request for DeleteConnector.

### [DeleteConsumerGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.DeleteConsumerGroupRequest)

Request for DeleteConsumerGroup.

### [DeleteTopicRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.DeleteTopicRequest)

Request for DeleteTopic.

### [GcpConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GcpConfig)

Configuration properties for a Kafka cluster deployed to Google Cloud Platform.

### [GetAclRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetAclRequest)

Request for GetAcl.

### [GetClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetClusterRequest)

Request for GetCluster.

### [GetConnectClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetConnectClusterRequest)

Request for GetConnectCluster.

### [GetConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetConnectorRequest)

Request for GetConnector.

### [GetConsumerGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetConsumerGroupRequest)

Request for GetConsumerGroup.

### [GetTopicRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.GetTopicRequest)

Request for GetTopic.

### [ListAclsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListAclsRequest)

Request for ListAcls.

### [ListAclsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListAclsResponse)

Response for ListAcls.

### [ListClustersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListClustersRequest)

Request for ListClusters.

### [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListClustersResponse)

Response for ListClusters.

### [ListConnectClustersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectClustersRequest)

Request for ListConnectClusters.

### [ListConnectClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectClustersResponse)

Response for ListConnectClusters.

### [ListConnectorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectorsRequest)

Request for ListConnectors.

### [ListConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConnectorsResponse)

Response for ListConnectors.

### [ListConsumerGroupsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConsumerGroupsRequest)

Request for ListConsumerGroups.

### [ListConsumerGroupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListConsumerGroupsResponse)

Response for ListConsumerGroups.

### [ListTopicsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListTopicsRequest)

Request for ListTopics.

### [ListTopicsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ListTopicsResponse)

Response for ListTopics.

### [NetworkConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.NetworkConfig)

The configuration of a Virtual Private Cloud (VPC) network that can access the Kafka cluster.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [PauseConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.PauseConnectorRequest)

Request for PauseConnector.

### [PauseConnectorResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.PauseConnectorResponse)

Response for PauseConnector.

### [RebalanceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RebalanceConfig)

Defines rebalancing behavior of a Kafka cluster.

### [Mode](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RebalanceConfig.Mode)

The partition rebalance mode for the cluster.

### [RemoveAclEntryRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RemoveAclEntryRequest)

Request for RemoveAclEntry.

### [RemoveAclEntryResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RemoveAclEntryResponse)

Response for RemoveAclEntry.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestartConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RestartConnectorRequest)

Request for RestartConnector.

### [RestartConnectorResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RestartConnectorResponse)

Response for RestartConnector.

### [ResumeConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ResumeConnectorRequest)

Request for ResumeConnector.

### [ResumeConnectorResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ResumeConnectorResponse)

Response for ResumeConnector.

### [StopConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.StopConnectorRequest)

Request for StopConnector.

### [StopConnectorResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.StopConnectorResponse)

Response for StopConnector.

### [TaskRetryPolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.TaskRetryPolicy)

Task Retry Policy is implemented on a best-effort basis. Retry delay will be exponential based on provided minimum and maximum backoffs. <https://en.wikipedia.org/wiki/Exponential_backoff>. Note that the delay between consecutive task restarts may not always precisely match the configured settings. This can happen when the ConnectCluster is in rebalancing state or if the ConnectCluster is unresponsive etc. The default values for minimum and maximum backoffs are 60 seconds and 30 minutes respectively.

### [TlsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.TlsConfig)

The TLS configuration for the Kafka cluster.

### [Topic](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Topic)

A Kafka topic in a given cluster.

### [ConfigsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.Topic.ConfigsEntry)

The abstract base class for a message.

### [TrustConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.TrustConfig)

Sources of CA certificates to install in the broker's truststore.

### [CertificateAuthorityServiceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.TrustConfig.CertificateAuthorityServiceConfig)

A configuration for the Google Certificate Authority Service.

### [UpdateAclRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateAclRequest)

Request for UpdateAcl.

### [UpdateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateClusterRequest)

Request for UpdateCluster.

### [UpdateConnectClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateConnectClusterRequest)

Request for UpdateConnectCluster.

### [UpdateConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateConnectorRequest)

Request for UpdateConnector.

### [UpdateConsumerGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateConsumerGroupRequest)

Request for UpdateConsumerGroup.

### [UpdateTopicRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.UpdateTopicRequest)

Request for UpdateTopic.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka.pagers)

API documentation for `managedkafka_v1.services.managed_kafka.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.pagers)

API documentation for `managedkafka_v1.services.managed_kafka_connect.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
