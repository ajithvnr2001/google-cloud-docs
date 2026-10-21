---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka/
title: Google Cloud Managed Service for Apache Kafka roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:13.109939+00:00
---

# Google Cloud Managed Service for Apache Kafka roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud Managed Service for Apache Kafka roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud Managed Service for Apache Kafka. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud Managed Service for Apache Kafka roles

Role | Permissions  
---|---  
  
#### Managed Kafka Admin 

(`roles/managedkafka.admin`) Full access to Managed Kafka resources.  |  `cloudasset.assets.searchAllResources` `managedkafka.*`

  * `managedkafka.acls.create`
  * `managedkafka.acls.delete`
  * `managedkafka.acls.get`
  * `managedkafka.acls.list`
  * `managedkafka.acls.update`
  * `managedkafka.acls.updateEntries`
  * `managedkafka.clusters.attachConnectCluster`
  * `managedkafka.clusters.connect`
  * `managedkafka.clusters.create`
  * `managedkafka.clusters.delete`
  * `managedkafka.clusters.get`
  * `managedkafka.clusters.list`
  * `managedkafka.clusters.update`
  * `managedkafka.config.delete`
  * `managedkafka.config.get`
  * `managedkafka.config.update`
  * `managedkafka.connectClusters.create`
  * `managedkafka.connectClusters.delete`
  * `managedkafka.connectClusters.get`
  * `managedkafka.connectClusters.list`
  * `managedkafka.connectClusters.update`
  * `managedkafka.connectors.create`
  * `managedkafka.connectors.delete`
  * `managedkafka.connectors.get`
  * `managedkafka.connectors.list`
  * `managedkafka.connectors.pause`
  * `managedkafka.connectors.restart`
  * `managedkafka.connectors.resume`
  * `managedkafka.connectors.stop`
  * `managedkafka.connectors.update`
  * `managedkafka.consumerGroups.delete`
  * `managedkafka.consumerGroups.get`
  * `managedkafka.consumerGroups.list`
  * `managedkafka.consumerGroups.update`
  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`
  * `managedkafka.locations.get`
  * `managedkafka.locations.list`
  * `managedkafka.mode.delete`
  * `managedkafka.mode.get`
  * `managedkafka.mode.update`
  * `managedkafka.operations.cancel`
  * `managedkafka.operations.delete`
  * `managedkafka.operations.get`
  * `managedkafka.operations.list`
  * `managedkafka.schemaRegistries.create`
  * `managedkafka.schemaRegistries.delete`
  * `managedkafka.schemaRegistries.get`
  * `managedkafka.schemaRegistries.list`
  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`
  * `managedkafka.subjects.delete`
  * `managedkafka.subjects.list`
  * `managedkafka.subjects.lookup`
  * `managedkafka.topics.create`
  * `managedkafka.topics.delete`
  * `managedkafka.topics.get`
  * `managedkafka.topics.list`
  * `managedkafka.topics.update`
  * `managedkafka.versions.checkCompatibility`
  * `managedkafka.versions.create`
  * `managedkafka.versions.delete`
  * `managedkafka.versions.get`
  * `managedkafka.versions.list`
  * `managedkafka.versions.referencedby`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Managed Kafka Viewer 

(`roles/managedkafka.viewer`) Readonly access to Managed Kafka resources.  |  `cloudasset.assets.searchAllResources` `managedkafka.acls.get` `managedkafka.acls.list` `managedkafka.clusters.get` `managedkafka.clusters.list` `managedkafka.config.get` `managedkafka.connectClusters.get` `managedkafka.connectClusters.list` `managedkafka.connectors.get` `managedkafka.connectors.list` `managedkafka.consumerGroups.get` `managedkafka.consumerGroups.list` `managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.locations.*`

  * `managedkafka.locations.get`
  * `managedkafka.locations.list`

`managedkafka.mode.get` `managedkafka.operations.get` `managedkafka.operations.list` `managedkafka.schemaRegistries.get` `managedkafka.schemaRegistries.list` `managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.list` `managedkafka.subjects.lookup` `managedkafka.topics.get` `managedkafka.topics.list` `managedkafka.versions.checkCompatibility` `managedkafka.versions.get` `managedkafka.versions.list` `managedkafka.versions.referencedby` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Managed Kafka ACL Editor 

(`roles/managedkafka.aclEditor`) Read and write access to Managed Kafka ACL resources.  |  `managedkafka.acls.*`

  * `managedkafka.acls.create`
  * `managedkafka.acls.delete`
  * `managedkafka.acls.get`
  * `managedkafka.acls.list`
  * `managedkafka.acls.update`
  * `managedkafka.acls.updateEntries`

  
  
#### Managed Kafka ACL Viewer 

(`roles/managedkafka.aclViewer`) Readonly access to Managed Kafka ACL resources.  |  `managedkafka.acls.get` `managedkafka.acls.list`  
  
#### Managed Kafka Client 

(`roles/managedkafka.client`) Provides access to connect to the Kafka servers in a cluster, i.e. provides Kafka data plane access. Intended for, e.g., producers and consumers.  |  `cloudasset.assets.searchAllResources` `managedkafka.acls.get` `managedkafka.acls.list` `managedkafka.clusters.attachConnectCluster` `managedkafka.clusters.connect` `managedkafka.clusters.get` `managedkafka.clusters.list` `managedkafka.config.get` `managedkafka.connectClusters.get` `managedkafka.connectClusters.list` `managedkafka.connectors.get` `managedkafka.connectors.list` `managedkafka.consumerGroups.*`

  * `managedkafka.consumerGroups.delete`
  * `managedkafka.consumerGroups.get`
  * `managedkafka.consumerGroups.list`
  * `managedkafka.consumerGroups.update`

`managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.locations.*`

  * `managedkafka.locations.get`
  * `managedkafka.locations.list`

`managedkafka.mode.get` `managedkafka.operations.get` `managedkafka.operations.list` `managedkafka.schemaRegistries.get` `managedkafka.schemaRegistries.list` `managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.list` `managedkafka.subjects.lookup` `managedkafka.topics.*`

  * `managedkafka.topics.create`
  * `managedkafka.topics.delete`
  * `managedkafka.topics.get`
  * `managedkafka.topics.list`
  * `managedkafka.topics.update`

`managedkafka.versions.checkCompatibility` `managedkafka.versions.get` `managedkafka.versions.list` `managedkafka.versions.referencedby` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Managed Kafka Cluster Editor 

(`roles/managedkafka.clusterEditor`) Provides read and write access to Kafka clusters. Intended for, e.g., IT Departments that provision Kafka clusters, but need not be able to read or modify topics or consumer groups.  |  `cloudasset.assets.searchAllResources` `managedkafka.acls.get` `managedkafka.acls.list` `managedkafka.clusters.create` `managedkafka.clusters.delete` `managedkafka.clusters.get` `managedkafka.clusters.list` `managedkafka.clusters.update` `managedkafka.config.get` `managedkafka.connectClusters.get` `managedkafka.connectClusters.list` `managedkafka.connectors.get` `managedkafka.connectors.list` `managedkafka.consumerGroups.get` `managedkafka.consumerGroups.list` `managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.locations.*`

  * `managedkafka.locations.get`
  * `managedkafka.locations.list`

`managedkafka.mode.get` `managedkafka.operations.get` `managedkafka.operations.list` `managedkafka.schemaRegistries.get` `managedkafka.schemaRegistries.list` `managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.list` `managedkafka.subjects.lookup` `managedkafka.topics.get` `managedkafka.topics.list` `managedkafka.versions.checkCompatibility` `managedkafka.versions.get` `managedkafka.versions.list` `managedkafka.versions.referencedby` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Managed Kafka Connect Cluster Editor Beta

(`roles/managedkafka.connectClusterEditor`) Provides read and write access to Kafka Connect clusters. Intended for, e.g., IT Departments that provision Kafka Connect clusters, but need not be able to read or modify connectors.  |  `managedkafka.connectClusters.*`

  * `managedkafka.connectClusters.create`
  * `managedkafka.connectClusters.delete`
  * `managedkafka.connectClusters.get`
  * `managedkafka.connectClusters.list`
  * `managedkafka.connectClusters.update`

`managedkafka.connectors.get` `managedkafka.connectors.list`  
  
#### Managed Kafka Connector Editor Beta

(`roles/managedkafka.connectorEditor`) Provides read and write access to connectors. Intended for, e.g., developers who configure and operate connectors.  |  `cloudasset.assets.searchAllResources` `managedkafka.acls.get` `managedkafka.acls.list` `managedkafka.clusters.get` `managedkafka.clusters.list` `managedkafka.config.get` `managedkafka.connectClusters.get` `managedkafka.connectClusters.list` `managedkafka.connectors.*`

  * `managedkafka.connectors.create`
  * `managedkafka.connectors.delete`
  * `managedkafka.connectors.get`
  * `managedkafka.connectors.list`
  * `managedkafka.connectors.pause`
  * `managedkafka.connectors.restart`
  * `managedkafka.connectors.resume`
  * `managedkafka.connectors.stop`
  * `managedkafka.connectors.update`

`managedkafka.consumerGroups.get` `managedkafka.consumerGroups.list` `managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.locations.*`

  * `managedkafka.locations.get`
  * `managedkafka.locations.list`

`managedkafka.mode.get` `managedkafka.operations.get` `managedkafka.operations.list` `managedkafka.schemaRegistries.get` `managedkafka.schemaRegistries.list` `managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.list` `managedkafka.subjects.lookup` `managedkafka.topics.get` `managedkafka.topics.list` `managedkafka.versions.checkCompatibility` `managedkafka.versions.get` `managedkafka.versions.list` `managedkafka.versions.referencedby` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Managed Kafka Consumer Group Editor 

(`roles/managedkafka.consumerGroupEditor`) Provides read and write access to consumer group metadata. Intended for, e.g., developers who configure consumer groups.  |  `cloudasset.assets.searchAllResources` `managedkafka.acls.get` `managedkafka.acls.list` `managedkafka.clusters.get` `managedkafka.clusters.list` `managedkafka.config.get` `managedkafka.connectClusters.get` `managedkafka.connectClusters.list` `managedkafka.connectors.get` `managedkafka.connectors.list` `managedkafka.consumerGroups.*`

  * `managedkafka.consumerGroups.delete`
  * `managedkafka.consumerGroups.get`
  * `managedkafka.consumerGroups.list`
  * `managedkafka.consumerGroups.update`

`managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.locations.*`

  * `managedkafka.locations.get`
  * `managedkafka.locations.list`

`managedkafka.mode.get` `managedkafka.operations.get` `managedkafka.operations.list` `managedkafka.schemaRegistries.get` `managedkafka.schemaRegistries.list` `managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.list` `managedkafka.subjects.lookup` `managedkafka.topics.get` `managedkafka.topics.list` `managedkafka.versions.checkCompatibility` `managedkafka.versions.get` `managedkafka.versions.list` `managedkafka.versions.referencedby` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Schema Registry Admin Beta

(`roles/managedkafka.schemaRegistryAdmin`) Full access to schemas, schema versions and configs  |  `managedkafka.config.*`

  * `managedkafka.config.delete`
  * `managedkafka.config.get`
  * `managedkafka.config.update`

`managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.mode.*`

  * `managedkafka.mode.delete`
  * `managedkafka.mode.get`
  * `managedkafka.mode.update`

`managedkafka.schemaRegistries.*`

  * `managedkafka.schemaRegistries.create`
  * `managedkafka.schemaRegistries.delete`
  * `managedkafka.schemaRegistries.get`
  * `managedkafka.schemaRegistries.list`

`managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.*`

  * `managedkafka.subjects.delete`
  * `managedkafka.subjects.list`
  * `managedkafka.subjects.lookup`

`managedkafka.versions.*`

  * `managedkafka.versions.checkCompatibility`
  * `managedkafka.versions.create`
  * `managedkafka.versions.delete`
  * `managedkafka.versions.get`
  * `managedkafka.versions.list`
  * `managedkafka.versions.referencedby`

  
  
#### Schema Registry Editor Beta

(`roles/managedkafka.schemaRegistryEditor`) View and edit schemas and schema versions  |  `managedkafka.config.get` `managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.mode.get` `managedkafka.schemaRegistries.*`

  * `managedkafka.schemaRegistries.create`
  * `managedkafka.schemaRegistries.delete`
  * `managedkafka.schemaRegistries.get`
  * `managedkafka.schemaRegistries.list`

`managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.*`

  * `managedkafka.subjects.delete`
  * `managedkafka.subjects.list`
  * `managedkafka.subjects.lookup`

`managedkafka.versions.*`

  * `managedkafka.versions.checkCompatibility`
  * `managedkafka.versions.create`
  * `managedkafka.versions.delete`
  * `managedkafka.versions.get`
  * `managedkafka.versions.list`
  * `managedkafka.versions.referencedby`

  
  
#### Schema Registry Viewer Beta

(`roles/managedkafka.schemaRegistryViewer`) View schemas and schema versions  |  `managedkafka.config.get` `managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.mode.get` `managedkafka.schemaRegistries.get` `managedkafka.schemaRegistries.list` `managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.list` `managedkafka.subjects.lookup` `managedkafka.versions.checkCompatibility` `managedkafka.versions.get` `managedkafka.versions.list` `managedkafka.versions.referencedby`  
  
#### Managed Kafka Topic Editor 

(`roles/managedkafka.topicEditor`) Provides read and write access to topic metadata. Intended for, e.g., developers who configure topics.  |  `cloudasset.assets.searchAllResources` `managedkafka.acls.get` `managedkafka.acls.list` `managedkafka.clusters.get` `managedkafka.clusters.list` `managedkafka.config.get` `managedkafka.connectClusters.get` `managedkafka.connectClusters.list` `managedkafka.connectors.get` `managedkafka.connectors.list` `managedkafka.consumerGroups.get` `managedkafka.consumerGroups.list` `managedkafka.contexts.*`

  * `managedkafka.contexts.get`
  * `managedkafka.contexts.list`

`managedkafka.locations.*`

  * `managedkafka.locations.get`
  * `managedkafka.locations.list`

`managedkafka.mode.get` `managedkafka.operations.get` `managedkafka.operations.list` `managedkafka.schemaRegistries.get` `managedkafka.schemaRegistries.list` `managedkafka.schemas.*`

  * `managedkafka.schemas.get`
  * `managedkafka.schemas.listSubjects`
  * `managedkafka.schemas.listTypes`
  * `managedkafka.schemas.listVersions`

`managedkafka.subjects.list` `managedkafka.subjects.lookup` `managedkafka.topics.*`

  * `managedkafka.topics.create`
  * `managedkafka.topics.delete`
  * `managedkafka.topics.get`
  * `managedkafka.topics.list`
  * `managedkafka.topics.update`

`managedkafka.versions.checkCompatibility` `managedkafka.versions.get` `managedkafka.versions.list` `managedkafka.versions.referencedby` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Managed Kafka Service Agent 

(`roles/managedkafka.serviceAgent`) Gives Managed Kafka Service Agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.list` `compute.addresses.use` `compute.addresses.useInternal` `compute.forwardingRules.create` `compute.forwardingRules.delete` `compute.forwardingRules.list` `compute.forwardingRules.pscCreate` `compute.forwardingRules.pscDelete` `compute.networkAttachments.create` `compute.networkAttachments.delete` `compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networks.get` `compute.networks.use` `compute.regionOperations.get` `compute.subnetworks.get` `compute.subnetworks.use` `dns.changes.create` `dns.managedZones.create` `dns.managedZones.delete` `dns.managedZones.list` `dns.networks.bindPrivateDNSZone` `dns.networks.targetWithPeeringZone` `dns.resourceRecordSets.create` `dns.resourceRecordSets.delete` `dns.resourceRecordSets.list` `dns.resourceRecordSets.update` `managedkafka.clusters.connect` `privateca.caPools.get` `servicedirectory.namespaces.create` `servicedirectory.services.create` `servicedirectory.services.delete`  
  
## Google Cloud Managed Service for Apache Kafka permissions

Permission | Included in roles  
---|---  
  
#### `managedkafka.acls.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka ACL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`)   
  
#### `managedkafka.acls.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka ACL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`)   
  
#### `managedkafka.acls.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka ACL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`)  [Managed Kafka ACL Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclViewer) (`roles/managedkafka.aclViewer`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.acls.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka ACL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`)  [Managed Kafka ACL Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclViewer) (`roles/managedkafka.aclViewer`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.acls.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka ACL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`)   
  
#### `managedkafka.acls.updateEntries`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka ACL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`)   
  
#### `managedkafka.clusters.attachConnectCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)   
  
#### `managedkafka.clusters.connect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 

  
  
#### `managedkafka.clusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)   
  
#### `managedkafka.clusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)   
  
#### `managedkafka.clusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Managed Flink Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.serviceAgent) (`roles/managedflink.serviceAgent`) 

  
  
#### `managedkafka.clusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Managed Flink Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.serviceAgent) (`roles/managedflink.serviceAgent`) 

  
  
#### `managedkafka.clusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Managed Flink Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.serviceAgent) (`roles/managedflink.serviceAgent`) 

  
  
#### `managedkafka.config.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)   
  
#### `managedkafka.config.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.config.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)   
  
#### `managedkafka.connectClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connect Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`)   
  
#### `managedkafka.connectClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connect Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`)   
  
#### `managedkafka.connectClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connect Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.connectClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connect Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.connectClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connect Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`)   
  
#### `managedkafka.connectors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)   
  
#### `managedkafka.connectors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)   
  
#### `managedkafka.connectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connect Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.connectors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connect Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectClusterEditor) (`roles/managedkafka.connectClusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.connectors.pause`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)   
  
#### `managedkafka.connectors.restart`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)   
  
#### `managedkafka.connectors.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)   
  
#### `managedkafka.connectors.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)   
  
#### `managedkafka.connectors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)   
  
#### `managedkafka.consumerGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)   
  
#### `managedkafka.consumerGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.consumerGroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.consumerGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)   
  
#### `managedkafka.contexts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.contexts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.mode.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)   
  
#### `managedkafka.mode.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.mode.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)   
  
#### `managedkafka.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)   
  
#### `managedkafka.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)   
  
#### `managedkafka.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.schemaRegistries.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)   
  
#### `managedkafka.schemaRegistries.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)   
  
#### `managedkafka.schemaRegistries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.schemaRegistries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.schemas.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.schemas.listSubjects`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.schemas.listTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.schemas.listVersions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.subjects.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)   
  
#### `managedkafka.subjects.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.subjects.lookup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.topics.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.topics.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.topics.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.topics.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.topics.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.versions.checkCompatibility`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.versions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)   
  
#### `managedkafka.versions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)   
  
#### `managedkafka.versions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.versions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
#### `managedkafka.versions.referencedby`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Kafka Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.admin) (`roles/managedkafka.admin`)  [Managed Kafka Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.viewer) (`roles/managedkafka.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)  [Managed Kafka Cluster Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.clusterEditor) (`roles/managedkafka.clusterEditor`)  [Managed Kafka Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`)  [Managed Kafka Consumer Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.consumerGroupEditor) (`roles/managedkafka.consumerGroupEditor`)  [Schema Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryAdmin) (`roles/managedkafka.schemaRegistryAdmin`)  [Schema Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryEditor) (`roles/managedkafka.schemaRegistryEditor`)  [Schema Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.schemaRegistryViewer) (`roles/managedkafka.schemaRegistryViewer`)  [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) (`roles/managedkafka.topicEditor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
