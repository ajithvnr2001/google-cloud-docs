---
url: https://docs.cloud.google.com/iam/docs/conditions-resource-attributes/
title: Resource attributes for IAM Conditions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:00.051351+00:00
---

# Resource attributes for IAM Conditions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/conditions-resource-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Resource attributes for IAM Conditions Stay organized with collections  Save and categorize content based on your preferences. 

This topic contains a list of values that can be used for [resource attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource) in a condition, including string values for resource service, resource type, and the format for resource name strings.

You can use resource attributes to change the scope of the grant provided by a role binding. When a role contains permissions that apply to different kinds of resources, a condition can grant a subset of the role's permissions based on the resource service, resource type, and resource name.

Resource attributes are available for the Google Cloud services and resource types that are listed on this page. Other services and resource types do not recognize resource attributes.

For more information about Identity and Access Management (IAM) Conditions, see the following:

  * [Conditions overview](https://docs.cloud.google.com/iam/docs/conditions-overview)
  * [Managing conditional role bindings](https://docs.cloud.google.com/iam/docs/managing-conditional-policies)



## Resource service values

The following table lists the values that the resource service attribute can contain.

Resource service value  |  REST reference  | `agentregistry.googleapis.com` | [API reference](https://docs.cloud.google.com/agent-registry/reference/rest)  
---|---  
`apigee.googleapis.com` | [API reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)  
`apihub.googleapis.com` | [API reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest)  
`backupdr.googleapis.com` | [API reference](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest)  
`bigquery.googleapis.com` | [API reference](https://docs.cloud.google.com/bigquery/docs/reference/rest)  
`bigqueryreservation.googleapis.com` | [API reference](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest)  
`bigtableadmin.googleapis.com` | [API reference](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest)  
`binaryauthorization.googleapis.com` | [API reference](https://docs.cloud.google.com/binary-authorization/docs/reference/rest)  
`ces.googleapis.com` | [API reference](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/rest)  
`clouddeploy.googleapis.com` | [API reference](https://docs.cloud.google.com/deploy/docs/api/reference/rest)  
`cloudkms.googleapis.com` | [API reference](https://docs.cloud.google.com/kms/docs/reference/rest)  
`cloudresourcemanager.googleapis.com` | [API reference](https://docs.cloud.google.com/resource-manager/reference/rest)  
`compute.googleapis.com` | [API reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1)  
`container.googleapis.com` | [API reference](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest)  
`connectors.googleapis.com` | [API reference](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)  
`dataform.googleapis.com` | [API reference](https://docs.cloud.google.com/dataform/reference/rest)  
`dns.googleapis.com` | [API reference](https://docs.cloud.google.com/dns/docs/reference/rest/v1)  
`firestore.googleapis.com` | [API reference](https://docs.cloud.google.com/firestore/docs/reference/rest)  
`iap.googleapis.com` | [API reference](https://docs.cloud.google.com/iap/docs/reference/rest)  
`integrations.googleapis.com` | [API reference](https://docs.cloud.google.com/application-integration/docs/reference/rest)  
`logging.googleapis.com` | [API reference](https://docs.cloud.google.com/logging/docs/reference/rest)  
`managedkafka.googleapis.com` | [API reference](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest)  
`networksecurity.googleapis.com` | [API reference](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest)  
`parametermanager.googleapis.com` | [API reference](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest)  
`pubsublite.googleapis.com` | [API reference](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest)  
`secretmanager.googleapis.com` | [API reference](https://docs.cloud.google.com/secret-manager/docs/reference/rest)  
`spanner.googleapis.com` | [API reference](https://docs.cloud.google.com/spanner/docs/reference/rest)  
`sqladmin.googleapis.com` | [API reference](https://docs.cloud.google.com/sql/docs/mysql/admin-api)  
`storage.googleapis.com` | [API reference](https://docs.cloud.google.com/storage/docs/json_api)  
  
## Resource type values

The following table lists the values that the resource type attribute can contain.

Resource type value  |  Reference  | `agentregistry.googleapis.com/Skill` | [Read more](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills)  
---|---  
`agentregistry.googleapis.com/SkillRevision` | [Read more](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions)  
`apigee.googleapis.com/ApiProduct` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts)  
`apigee.googleapis.com/ApiProductAttribute` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes)  
`apigee.googleapis.com/Cache` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.caches)  
`apigee.googleapis.com/Developer` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers)  
`apigee.googleapis.com/DeveloperApp` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps)  
`apigee.googleapis.com/DeveloperAppAttribute` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.attributes)  
`apigee.googleapis.com/DeveloperAttribute` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/attributes)  
`apigee.googleapis.com/Export` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports)  
`apigee.googleapis.com/FlowHook` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks)  
`apigee.googleapis.com/KeyStore` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores)  
`apigee.googleapis.com/KeyStoreAlias` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases)  
`apigee.googleapis.com/KeyValueEntry` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries)  
`apigee.googleapis.com/KeyValueMap` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps)  
`apigee.googleapis.com/Proxy` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ApiProxy)  
`apigee.googleapis.com/ProxyRevision` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ApiProxyRevision)  
`apigee.googleapis.com/Query` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.queries)  
`apigee.googleapis.com/RatePlan` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans)  
`apigee.googleapis.com/Reference` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references)  
`apigee.googleapis.com/SharedFlow` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SharedFlow)  
`apigee.googleapis.com/SharedFlowRevision` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SharedFlowRevision)  
`apigee.googleapis.com/TargetServer` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers)  
`apigee.googleapis.com/TraceSession` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions)  
`apihub.googleapis.com/Api` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis)  
`apihub.googleapis.com/Deployment` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments)  
`apihub.googleapis.com/Version` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions)  
`apihub.googleapis.com/Spec` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs)  
`apihub.googleapis.com/ApiOperation` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations)  
`apihub.googleapis.com/Definition` | [Read more](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.definitions)  
`backupdr.googleapis.com/BackupVaults` | [Read more](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault)  
`bigquery.googleapis.com/Dataset` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets)  
`bigquery.googleapis.com/Model` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/models)  
`bigquery.googleapis.com/Routine` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines)  
`bigquery.googleapis.com/Table` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables)  
`bigqueryreservation.googleapis.com/Assignment` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations.assignments)  
`bigqueryreservation.googleapis.com/BiReservation` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/BiReservation)  
`bigqueryreservation.googleapis.com/CapacityCommitment` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.capacityCommitments)  
`bigqueryreservation.googleapis.com/Location` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations)  
`bigqueryreservation.googleapis.com/Reservation` | [Read more](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations)  
`bigtableadmin.googleapis.com/AppProfile` | [Read more](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.appProfiles)  
`bigtableadmin.googleapis.com/Backup` | [Read more](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups)  
`bigtableadmin.googleapis.com/Cluster` | [Read more](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters)  
`bigtableadmin.googleapis.com/Instance` | [Read more](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances)  
`bigtableadmin.googleapis.com/Table` | [Read more](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables)  
`binaryauthorization.googleapis.com/Attestor` | [Read more](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.attestors)  
`binaryauthorization.googleapis.com/ContinuousValidationConfig` | [Read more](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1alpha2/projects.continuousValidationConfig)  
`binaryauthorization.googleapis.com/Policy` | [Read more](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.policy)  
`ces.googleapis.com/App` | [Read more](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/rest/v1/projects.locations.apps)  
`ces.googleapis.com/Operation` | [Read more](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/rest/v1/projects.locations.operations)  
`cloud.googleapis.com/Location`1 | [Read more](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations)  
`cloudkms.googleapis.com/CryptoKey` | [Read more](https://docs.cloud.google.com/kms/docs/object-hierarchy#key)  
`cloudkms.googleapis.com/CryptoKeyVersion` | [Read more](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_version)  
`cloudkms.googleapis.com/KeyRing` | [Read more](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_ring)  
`cloudresourcemanager.googleapis.com/Project`2 | [Read more](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects)  
`compute.googleapis.com/BackendService` | [Read more](https://docs.cloud.google.com/load-balancing/docs/backend-service)  
`compute.googleapis.com/Disk` | [Read more](https://docs.cloud.google.com/compute/docs/disks#pdspecs)  
`compute.googleapis.com/Firewall` | [Read more](https://docs.cloud.google.com/vpc/docs/firewalls)  
`compute.googleapis.com/ForwardingRule` | [Read more](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
`compute.googleapis.com/GlobalForwardingRule` | [Read more](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
`compute.googleapis.com/Image` | [Read more](https://docs.cloud.google.com/compute/docs/images)  
`compute.googleapis.com/Instance` | [Read more](https://docs.cloud.google.com/compute/docs/instances)  
`compute.googleapis.com/InstanceTemplate` | [Read more](https://docs.cloud.google.com/compute/docs/instance-templates)  
`compute.googleapis.com/Snapshot` | [Read more](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)  
`compute.googleapis.com/TargetHttpProxy` | [Read more](https://docs.cloud.google.com/load-balancing/docs/target-proxies)  
`compute.googleapis.com/TargetHttpsProxy` | [Read more](https://docs.cloud.google.com/load-balancing/docs/target-proxies)  
`compute.googleapis.com/TargetSslProxy` | [Read more](https://docs.cloud.google.com/load-balancing/docs/target-proxies)  
`compute.googleapis.com/TargetTcpProxy` | [Read more](https://docs.cloud.google.com/load-balancing/docs/target-proxies)  
`connectors.googleapis.com/Connection` | [Read more](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections)  
`connectors.googleapis.com/ConnectionSchemaMetadata` | [Read more](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.connectionSchemaMetadata)  
`connectors.googleapis.com/EndpointAttachment` | [Read more](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.endpointAttachments)  
`connectors.googleapis.com/EventSubscription` | [Read more](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.eventSubscriptions)  
`connectors.googleapis.com/ManagedZone` | [Read more](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.global.managedZones)  
`container.googleapis.com/Cluster` | [Read more](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters)  
`dataform.googleapis.com/CompilationResult` | [Read more](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults)  
`dataform.googleapis.com/Location` | [Read more](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations)  
`dataform.googleapis.com/ReleaseConfig` | [Read more](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs)  
`dataform.googleapis.com/Repository` | [Read more](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories)  
`dataform.googleapis.com/WorkflowConfig` | [Read more](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs)  
`dataform.googleapis.com/WorkflowInvocation` | [Read more](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations)  
`dataform.googleapis.com/Workspace` | [Read more](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces)  
`dns.googleapis.com/ResourceRecordSet` | [Read more](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets)  
`firestore.googleapis.com/Database` | [Read more](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases)  
`iap.googleapis.com/Tunnel` | [Read more](https://docs.cloud.google.com/iap/docs/managing-access#resources_and_permissions)  
`iap.googleapis.com/TunnelInstance` | [Read more](https://docs.cloud.google.com/iap/docs/managing-access#resources_and_permissions)  
`iap.googleapis.com/TunnelZone` | [Read more](https://docs.cloud.google.com/iap/docs/managing-access#resources_and_permissions)  
`iap.googleapis.com/Web` | [Read more](https://docs.cloud.google.com/iap/docs/managing-access#resources_and_permissions)  
`iap.googleapis.com/WebService` | [Read more](https://docs.cloud.google.com/iap/docs/managing-access#resources_and_permissions)  
`iap.googleapis.com/WebServiceVersion` | [Read more](https://docs.cloud.google.com/iap/docs/managing-access#resources_and_permissions)  
`iap.googleapis.com/WebType` | [Read more](https://docs.cloud.google.com/iap/docs/managing-access#resources_and_permissions)  
`integrations.googleapis.com/AuthConfig` | [Read more](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.authConfigs)  
`integrations.googleapis.com/Execution` | [Read more](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions)  
`integrations.googleapis.com/Integration` | [Read more](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations)  
`integrations.googleapis.com/IntegrationVersion` | [Read more](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions)  
`integrations.googleapis.com/Location` | n/a  
`integrations.googleapis.com/Suspension` | [Read more](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions.suspensions)  
`logging.googleapis.com/LogBucket` | [Read more](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets)  
`logging.googleapis.com/LogView` | [Read more](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views)  
`managedkafka.googleapis.com/Cluster` | [Read more](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters)  
`managedkafka.googleapis.com/ConsumerGroup` | [Read more](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.consumerGroups)  
`managedkafka.googleapis.com/Operation` | [Read more](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.operations)  
`managedkafka.googleapis.com/Topic` | [Read more](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.topics)  
`networksecurity.googleapis.com/AddressGroup` | [Read more](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.addressGroups)  
`networksecurity.googleapis.com/FirewallEndpoint` | [Read more](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.firewallEndpoints)  
`networksecurity.googleapis.com/FirewallEndpointAssociation` | [Read more](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.firewallEndpointAssociations)  
`networksecurity.googleapis.com/InterceptDeployment` | [Read more](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments)  
`networksecurity.googleapis.com/InterceptDeploymentGroup` | [Read more](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups)  
`networksecurity.googleapis.com/InterceptEndpointGroup` | [Read more](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups)  
`networksecurity.googleapis.com/InterceptEndpointGroupAssociation` | [Read more](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations)  
`networksecurity.googleapis.com/MirroringDeployment` | [Read more](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments)  
`networksecurity.googleapis.com/MirroringDeploymentGroup` | [Read more](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups)  
`networksecurity.googleapis.com/MirroringEndpointGroup` | [Read more](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups)  
`networksecurity.googleapis.com/MirroringEndpointGroupAssociation` | [Read more](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations)  
`networksecurity.googleapis.com/SecurityProfile` | [Read more](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfiles)  
`networksecurity.googleapis.com/SecurityProfileGroup` | [Read more](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfileGroups)  
`parametermanager.googleapis.com/Parameter` | [Read more](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters)  
`parametermanager.googleapis.com/ParameterVersion` | [Read more](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions)  
`pubsublite.googleapis.com/Location` | [Read more](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest)  
`pubsublite.googleapis.com/Subscription` | [Read more](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions)  
`pubsublite.googleapis.com/Topic` | [Read more](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics)  
`secretmanager.googleapis.com/Secret` | [Read more](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets)  
`secretmanager.googleapis.com/SecretVersion` | [Read more](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions)  
`spanner.googleapis.com/Backup` | [Read more](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups)  
`spanner.googleapis.com/Database` | [Read more](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases)  
`spanner.googleapis.com/Instance` | [Read more](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances)  
`sqladmin.googleapis.com/BackupRun` | [Read more](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns)  
`sqladmin.googleapis.com/Instance` | [Read more](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances)  
`storage.googleapis.com/Bucket` | [Read more](https://docs.cloud.google.com/storage/docs/buckets)  
`storage.googleapis.com/Folder` | [Read more](https://docs.cloud.google.com/storage/docs/folders-overview)  
`storage.googleapis.com/ManagedFolder` | [Read more](https://docs.cloud.google.com/storage/docs/managed-folders)  
`storage.googleapis.com/Object` | [Read more](https://docs.cloud.google.com/storage/docs/objects)  
  
1 Cloud Key Management Service uses this resource type as the parent of [key ring](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_ring) resources.

2 Apigee uses this resource type as the parent of any resource that belongs to an Apigee organization. 

## Resource name format

The following table lists the format of each type of resource name attribute.

**Note:** Ensure that you use the correct identifier for your project. Project IDs are alphanumeric, and project numbers are numeric. You can't substitute the project ID for the project number, or the project number for the project ID. For more information, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin). Resource reference  |  Resource name format template  | Agent Registry [skills](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills) | `projects/project-id/locations/location/skills/skill-id`  
---|---  
Agent Registry [skill-revisions](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions) | `projects/project-id/locations/location/skills/skill-id/revisions/skill-revision-id`  
Apigee [API product attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes) | `organizations/organization-name/apiproducts/product-id/attributes/attribute-id`  
Apigee [API products](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts) | `organizations/organization-name/apiproducts/product-id`  
Apigee [API proxies](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ApiProxy) | `organizations/organization-name/apis/proxy-id`  
Apigee [API proxy key-value map entries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries) | `organizations/organization-name/api/proxy-id/keyvaluemaps/keyvaluemap-id/entries/entry-id`  
Apigee [API proxy key-value maps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps) | `organizations/organization-name/apis/proxy-id/keyvaluemaps/key-value-map-id`  
Apigee [API proxy revisions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ApiProxyRevision) | `organizations/organization-name/apis/proxy-id/revisions/revision-id`  
Apigee [caches](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.caches) | `organizations/organization-name/environments/environment-id/caches/cache-id`  
Apigee [developer app attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.attributes) | `organizations/organization-name/developers/developer-id/apps/app-id/attributes/attribute-id`  
Apigee [developer apps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps) | `organizations/organization-name/developers/developer-id/apps/app-id`  
Apigee [developer attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/attributes) | `organizations/organization-name/developers/developer-id/attributes/attribute-id`  
Apigee [developers](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers) | `organizations/organization-name/developers/developer-id`  
Apigee [environment key-value map entries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries) | `organizations/organization-name/environments/environment-id/keyvaluemaps/keyvaluemap-id/entries/entry-id`  
Apigee [environment key-value maps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps) | `organizations/organization-name/environments/environment/keyvaluemaps/key-value-map-id`  
Apigee [exports](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports) | `organizations/organization-name/environments/environment-id/analytics/exports/export-id`  
Apigee [flow hooks](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks) | `organizations/organization-name/environments/environment-id/flowhooks/flowhook-id`  
Apigee [keystore aliases](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases) | `organizations/organization-name/environments/environment-id/keystores/keystore-id/aliases/alias-id`  
Apigee [keystores](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores) | `organizations/organization-name/environments/environment-id/keystores/keystore-id`  
Apigee [queries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.queries) | `organizations/organization-name/environments/environment-id/queries/query-id`  
Apigee [rate plans](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans) | `organizations/organization-name/apiproducts/product-id/rateplans/rate-plan-id`  
Apigee [references](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references) | `organizations/organization-name/environments/environment-id/references/reference-id`  
Apigee [shared flow revisions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SharedFlowRevision) | `organizations/organization-name/sharedflows/shared-flow-id/revisions/revision-id`  
Apigee [shared flows](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SharedFlow) | `organizations/organization-name/sharedflows/shared-flow-id`  
Apigee [target servers](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers) | `organizations/organization-name/environments/environment-id/targetservers/targetserver-id`  
Apigee [trace (debug) sessions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions) | `organizations/organization-name/environments/environment-id/apis/proxy-id/revisions/revision-id/debugsessions/session-id`  
Apigee API Hub [apis](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis) | `projects/project-id/locations/location-id/apis/api-id`  
Apigee API Hub [deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments) | `projects/project-id/locations/location-id/deployments/deployment-id`  
Apigee API Hub [versions](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions) | `projects/project-id/locations/location-id/apis/api-id/versions/version-id`  
Apigee API Hub [specs](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs) | `projects/project-id/locations/location-id/apis/api-id/versions/version-id/specs/spec-id`  
Apigee API Hub [operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations) | `projects/project-id/locations/location-id/apis/api-id/versions/version-id/operations/operation-id`  
Apigee API Hub [definitions](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.definitions) | `projects/project-id/locations/location-id/apis/api-id/versions/version-id/definitions/definition-id`  
Backup and DR Service [backupVaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) science | `projects/project-id/locations/location-id/backupVaults/backup-vault-id`  
BigQuery [datasets](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets) | `projects/project-id/datasets/dataset-id`  
BigQuery [models](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/models) | `projects/project-id/datasets/dataset-id/models/model-id`  
BigQuery [routines](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines) | `projects/project-id/datasets/dataset-id/routines/routine-id`  
BigQuery [tables](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables) | `projects/project-id/datasets/dataset-id/tables/table-id`  
BigQuery Reservation API [assignments](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations.assignments) | `projects/project-id/locations/location-id/reservations/reservation-id/assignments/assignment-id`  
BigQuery Reservation API [BI reservations](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/BiReservation) | `projects/project-id/locations/location-id/biReservation`  
BigQuery Reservation API [capacity commitments](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.capacityCommitments) | `projects/project-id/locations/location-id/capacityCommitments/capacity-commitment-id`  
BigQuery Reservation API [locations](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations) | `projects/project-id/locations/location-id`  
BigQuery Reservation API [reservations](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations) | `projects/project-id/locations/location-id/reservations/reservation-id`  
Binary Authorization [attestors](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.attestors) | `projects/project-number/attestors/attestor-id`  
Binary Authorization [continuous validation configs](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1alpha2/projects.continuousValidationConfig) | `projects/project-number/continuousValidationConfig`  
Binary Authorization [policies](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.policy) | `projects/project-number/policy`  
Customer Experience Agent Studio [apps](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/rest/v1/projects.locations.apps) | `projects/project-id/locations/location-id/apps/app-id`  
Customer Experience Agent Studio [operations](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/rest/v1/projects.locations.operations) | `projects/project-id/locations/location-id/operations/operation-id`  
Bigtable [appProfiles](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.appProfiles) | `projects/project-id/instances/instance-id/appProfiles/appProfile-id`  
Bigtable [backups](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups) | `projects/project-id/instances/instance-id/clusters/cluster-id/backups/backup-id`  
Bigtable [clusters](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters) | `projects/project-id/instances/instance-id/clusters/cluster-id`  
Bigtable [instances](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances) | `projects/project-id/instances/instance-id`  
Bigtable [tables](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables) | `projects/project-id/instances/instance-id/tables/table-id`  
Cloud Deploy [automation runs](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns) | `projects/project-id/locations/location-id/deliveryPipelines/delivery-pipeline-id/automationRuns/automation-run-id`  
Cloud Deploy [automations](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations) | `projects/project-id/locations/location-id/deliveryPipelines/delivery-pipeline-id/automations/automation-id`  
Cloud Deploy [custom target types](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes) | `projects/project-id/locations/location-id/customTargetTypes/custom-target-type-id`  
Cloud Deploy [delivery pipelines](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines) | `projects/project-id/locations/location-id/deliveryPipelines/delivery-pipeline-id`  
Cloud Deploy [job runs](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns) | `projects/project-id/locations/location-id/deliveryPipelines/delivery-pipeline-id/releases/release-id/rollouts/rollout-id/jobRuns/job-run-id`  
Cloud Deploy [releases](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases) | `projects/project-id/locations/location-id/deliveryPipelines/delivery-pipeline-id/releases/release-id`  
Cloud Deploy [rollouts](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts) | `projects/project-id/locations/location-id/deliveryPipelines/delivery-pipeline-id/releases/release-id/rollouts/rollout-id`  
Cloud Deploy [targets](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets) | `projects/project-id/locations/location-id/targets/target-id`  
Firestore [databases](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases) | `projects/project-id/databases/database-id`  
Cloud NGFW [address groups](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.addressGroups) |  `projects/project-number/locations/location/addressGroups/address-group-name`  
`organizations/organization-id/locations/location/addressGroups/address-group-name`  
Cloud NGFW [firewall endpoints](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.firewallEndpoints) |  `projects/project-number/locations/location/firewallEndpoints/firewall-endpoint-id`  
`organizations/organization-id/locations/location/firewallEndpoints/firewall-endpoint-id`  
Cloud NGFW [firewall endpoint associations](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.firewallEndpointAssociations) |  `projects/project-number/locations/location/firewallEndpointAssociations/firewall-endpoint-association-id`  
Cloud NGFW [security profile groups](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.securityProfileGroups)1 |  `projects/project-number/locations/location/securityProfileGroups/security-profile-group-id`  
Cloud NGFW [security profiles](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.securityProfiles)1 |  `projects/project-number/locations/location/securityProfiles/security-profile-id`  
Network Security Integration [intercept deployment groups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups) |  `projects/project-number/locations/location/interceptDeploymentGroups/intercept-deployment-group-id`  
Network Security Integration [intercept deployments](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments) |  `projects/project-number/locations/location/interceptDeployments/intercept-deployment-id`  
Network Security Integration [intercept endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations) |  `projects/project-number/locations/location/interceptEndpointGroupAssociations/intercept-endpoint-group-association-id`  
Network Security Integration [intercept endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups) |  `projects/project-number/locations/location/interceptEndpoints/intercept-endpoint-group-id`  
Network Security Integration [mirroring deployment groups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups) |  `projects/project-number/locations/location/mirroringDeploymentGroups/mirroring-deployment-group-id`  
Network Security Integration [mirroring deployments](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments) |  `projects/project-number/locations/location/mirroringDeployments/mirroring-deployment-id`  
Network Security Integration [mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations) |  `projects/project-number/locations/location/mirroringEndpointGroupAssociations/mirroring-endpoint-group-association-id`  
Network Security Integration [mirroring endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups) |  `projects/project-number/locations/location/mirroringEndpoints/mirroring-endpoint-group-id`  
Cloud Key Management Service [crypto keys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) | `projects/project-id/locations/location-id/keyRings/keyring-id/cryptoKeys/cryptokey-id`  
Cloud Key Management Service [crypto key versions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions) | `projects/project-id/locations/location-id/keyRings/keyring-id/cryptoKeys/cryptokey-id/cryptoKeyVersions/cryptokeyversion-id`  
Cloud Key Management Service [key rings](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings) | `projects/project-id/locations/location-id/keyRings/keyring-id`  
Cloud Logging [log buckets](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets) | `projects/project-id/locations/location-id/buckets/bucket-id`  
Cloud Logging [log views](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views) | `projects/project-id/locations/location-id/buckets/bucket-id/views/view-id`  
Spanner [backups](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups) | `projects/project-id/instances/instance-id/backups/backup-id`  
Spanner [databases](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases) | `projects/project-id/instances/instance-id/databases/database-id`  
Spanner [instances](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances) | `projects/project-id/instances/instance-id`  
Cloud SQL [backup runs](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns) | `projects/project-id/instances/instance-id/backupRuns/backup-id`  
Cloud SQL [instances](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances) | `projects/project-id/instances/instance-id`  
Cloud Storage [buckets](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets)2 | `projects/_/buckets/bucket-name`  
Cloud Storage [folders](https://docs.cloud.google.com/storage/docs/json_api/v1/folders) in buckets with hierarchical namespace enabled2, 3 | `projects/_/buckets/bucket-name/folders/folder-name`  
Cloud Storage [managed folders](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder)2, 4 | `projects/_/buckets/bucket-name/managedFolders/managed-folder-name`  
Cloud Storage [objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects)2, 5 | `projects/_/buckets/bucket-name/objects/object-name`  
Compute Engine [global backend services](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) | `projects/project-id/global/backendServices/backend-service-id`  
Compute Engine [regional backend services](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) | `projects/project-id/regions/region-id/backendServices/backend-service-id`  
Compute Engine [firewalls](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls) | `projects/project-id/global/firewalls/firewall-id`  
Compute Engine [global forwarding rules](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules) | `projects/project-id/global/forwardingRules/forwarding-rule-id`  
Compute Engine [regional forwarding rules](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) | `projects/project-id/regions/region-id/forwardingRules/forwarding-rule-id`  
Compute Engine [images](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images) | `projects/project-id/global/images/image-id`  
Compute Engine [instance templates](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates) | `projects/project-id/global/instanceTemplates/instance-template-id`  
Compute Engine [instances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) | `projects/project-id/zones/zone-id/instances/instance-id`  
Compute Engine [regional persistent disks](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks) | `projects/project-id/regions/region-id/disks/disk-id`  
Compute Engine [zonal persistent disks](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks) | `projects/project-id/zones/zone-id/disks/disk-id`  
Compute Engine [snapshots](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots) | `projects/project-id/global/snapshots/snapshot-id`  
Compute Engine [global target HTTP proxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies) | `projects/project-id/global/targetHttpProxies/target-http-proxy-id`  
Compute Engine [regional target HTTP proxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpProxies) | `projects/project-id/regions/region-id/targetHttpProxies/target-http-proxy-id`  
Compute Engine [global target HTTPS proxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies) | `projects/project-id/global/targetHttpsProxies/target-https-proxy-id`  
Compute Engine [regional target HTTPS proxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies) | `projects/project-id/regions/region-id/targetHttpsProxies/target-https-proxy-id`  
Compute Engine [target SSL proxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies) | `projects/project-id/global/targetSslProxies/target-ssl-proxy-id`  
Compute Engine [target TCP proxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetTcpProxies) | `projects/project-id/global/targetTcpProxies/target-tcp-proxy-id`  
Google Kubernetes Engine [zonal clusters](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters) | `projects/project-id/zones/zone/clusters/cluster-id`  
Google Kubernetes Engine [regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters) | `projects/project-id/locations/location/clusters/cluster-id`  
Dataform [compilation results](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults) | `projects/project-id/locations/location/repositories/repository/compilationResults/compilation-result`  
Dataform [locations](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations) | `projects/project-id/locations/location`  
Dataform [release configs](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs) | `projects/project-id/locations/location/repositories/repository/releaseConfigs/release-config`  
Dataform [repositories](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories) | `projects/project-id/locations/location/repositories/repository`  
Dataform [workflow configs](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs) | `projects/project-id/locations/location/repositories/repository/workflowConfigs/workflow-config`  
Dataform [workflow invocations](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations) | `projects/project-id/locations/location/repositories/repository/workflowInvocations/workflow-invocation`  
Dataform [workspaces](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces) | `projects/project-id/locations/location/repositories/repository/workspaces/workspace`  
Cloud DNS [resource record sets](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets) | `projects/project-id/managedZones/zone-id/rrsets/rrset-name/rrset-type`  
Integration Connectors [connections](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections) | `projects/project-id/locations/location/connections/connection-name`  
Integration Connectors [connection schema metadata](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.connectionSchemaMetadata) | `projects/project-id/locations/location/connections/connection-name/connectionSchemaMetadata`  
Integration Connectors [endpoint attachments](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.endpointAttachments) | `projects/project-id/locations/location/endpointAttachments/endpoint-attachment-name`  
Integration Connectors [event subscriptions](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.eventSubscriptions) | `projects/project-id/locations/location/eventSubscriptions/event-subscription-name`  
Integration Connectors [managed zones](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.global.managedZones) | `projects/project-id/locations/global/managedZones/managed-zone-name`  
Google Cloud Managed Service for Apache Kafka [clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters) | `projects/project-number/locations/location/clusters/cluster-name`  
Google Cloud Managed Service for Apache Kafka [consumer groups](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.consumerGroups) | `projects/project-number/locations/location/clusters/cluster-name/consumerGroups/consumer-group`  
Google Cloud Managed Service for Apache Kafka [operations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.operations) | `projects/project-number/locations/location/operations/operation`  
Google Cloud Managed Service for Apache Kafka [topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.topics) | `projects/project-number/locations/location/clusters/cluster-name/topics/topic-name`  
Parameter Manager [parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters) | `projects/project-number/locations/location/parameters/parameter-id`  
Parameter Manager [parameter versions](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions) | `projects/project-number/locations/location/parameters/parameter-id/versions/version-id`  
Pub/Sub Lite [locations](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest) | `projects/project-number/locations/location`  
Pub/Sub Lite [subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions) | `projects/project-number/locations/location/subscriptions/subscription-id`  
Pub/Sub Lite [topics](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics) | `projects/project-number/locations/location/topics/topic-id`  
Resource Manager [organizations](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations)6 | `organizations/organization-name`  
Secret Manager [secrets](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets) | `projects/project-number/secrets/secret-id`  
Secret Manager [secret versions](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions)7 | `projects/project-number/secrets/secret-id/versions/secret-version`  
  
1 IAM Conditions only supports project-level Cloud NGFW resources. Organization-level Cloud NGFW resources are not supported.

2 For Cloud Storage, resource names contain an underscore (`_`) rather than a project ID. You _cannot_ replace the underscore with a project ID, project name, or project number.

3 Use the entire [folder name](https://docs.cloud.google.com/storage/docs/folders-overview#folder-metadata), including forward slashes.

4 Use the entire [managed folder name](https://docs.cloud.google.com/storage/docs/managed-folders#managed_folder_names), including forward slashes.

5 Use the entire [object name](https://docs.cloud.google.com/storage/docs/objects#naming), including forward slashes.

6 Apigee uses this format when you list any type of resource that belongs to an Apigee organization. 7 If a condition evaluates the resource name for a secret version, the secret version in the request must exactly match the secret version in the condition for the condition to be satisfied. For example, if the version in the condition is `latest`, only a request with the version `latest` satisfies the condition; a request with the version `3` does not satisfy the condition, even if `3` is the latest version. 

## Resource tags

You can attach [tags](https://docs.cloud.google.com/iam/docs/tags-access-control) to organizations, projects, and folders. Any Google Cloud resource can inherit tags from these higher-level resources.

You can use a few different types of identifiers to refer to tag keys and values:

  * A _permanent ID_ , which is globally unique and can never be reused. For example, a tag key could have the permanent ID `tagKeys/123456789012`, and a tag value could have the permanent ID `tagValues/567890123456`. 
  * A _short name_. The short name for each key must be unique within the project or organization under which the key is defined, and the short name for each value must be unique for its associated key. For example, a tag key could have the short name `env`, and a tag value could have the short name `prod`. 
  * A _namespaced name_ , which adds your organization's numeric ID or project's ID to the short name of a tag key. For example, a tag key created for an organization could have the namespaced name `123456789012/env`. To learn how to get your organization ID, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). A tag key created for a project could have the namespaced name `myproject/env`. To learn how to get your project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 



The specific identifiers depend on the tag keys and values that you have created for your organization. To learn how to list the tag keys and values that are available to you, see [Listing tag keys](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#listing_keys) and [Listing tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#listing_values).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
