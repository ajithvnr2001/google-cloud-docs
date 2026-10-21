---
url: https://docs.cloud.google.com/security-command-center/docs/supported-asset-types/
title: Supported asset types in Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:47.738894+00:00
---

# Supported asset types in Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/supported-asset-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Resources ](https://docs.cloud.google.com/security-command-center/docs/resources)



Send feedback 

#  Supported asset types in Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page lists the Google Cloud assets supported by the Security Command Center Assets API. The Security Command Center Assets API supports a subset of assets from [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types), Google's centralized inventory of cloud-managed assets.

Resource types in Security Command Center use a different naming convention than Cloud Asset Inventory. The following table lists supported asset types and includes the resource type format for Security Command Center. Resource types are useful when [listing assets](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-assets) in the Security Command Center API.

Table 1. Supported asset types Service | Cloud Asset Inventory format | Security Command Center format  
---|---|---  
**App Engine** |  [ `appengine.googleapis.com/Application`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps) | `google.appengine.Application`  
[ `appengine.googleapis.com/Service`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services) | `google.appengine.Service`  
[ `appengine.googleapis.com/Version`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions) | `google.appengine.Version`  
**Artifact Registry** | [ `artifactregistry.googleapis.com/Repository`](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories) | `google.artifactregistry.Repository`  
**BigQuery** | [ `bigquery.googleapis.com/Dataset`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets) | `google.cloud.bigquery.Dataset`  
**Managed Service for Apache Airflow** | [ `composer.googleapis.com/Environment`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments) | `google.composer.Environment`  
**Cloud DNS** | [ `dns.googleapis.com/ManagedZone`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones) | `google.cloud.dns.ManagedZone`  
[ `dns.googleapis.com/Policy`](https://docs.cloud.google.com/dns/docs/reference/v1/policies) | `google.cloud.dns.Policy`  
**Cloud Run functions** | [ `cloudfunctions.googleapis.com/CloudFunction`](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions) | `google.cloud.functions.CloudFunction`  
**Cloud Key Management Service** | [ `cloudkms.googleapis.com/CryptoKey`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) | `google.cloud.kms.CryptoKey`  
[ `cloudkms.googleapis.com/CryptoKeyVersion`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions) | `google.cloud.kms.CryptoKeyVersion`  
[ `cloudkms.googleapis.com/ImportJob`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs) | `google.cloud.kms.ImportJob`  
[ `cloudkms.googleapis.com/KeyRing`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings) | `google.cloud.kms.KeyRing`  
**Cloud Logging** | [ `logging.googleapis.com/LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets) | `google.logging.LogBucket`  
[ `logging.googleapis.com/LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics) | `google.logging.LogMetric`  
[ `logging.googleapis.com/LogSink`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks) | `google.logging.LogSink`  
**Spanner** | [ `spanner.googleapis.com/Database`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases) | `google.spanner.Database`  
[ `spanner.googleapis.com/Instance`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances) | `google.spanner.Instance`  
**Cloud SQL** | [ `sqladmin.googleapis.com/Instance`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances) | `google.cloud.sql.Instance`  
**Cloud Storage** | [ `storage.googleapis.com/Bucket`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets) | `google.cloud.storage.Bucket`  
**Compute Engine** | [ `compute.googleapis.com/Address`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) | `google.compute.Address`  
[ `compute.googleapis.com/Autoscaler`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers) | `google.compute.Autoscaler`  
[ `compute.googleapis.com/BackendBucket`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets) | `google.compute.BackendBucket`  
[ `compute.googleapis.com/BackendService`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) | `google.compute.BackendService`  
[ `compute.googleapis.com/Commitment`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments) | `google.compute.Commitment`  
[ `compute.googleapis.com/Disk`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks) | `google.compute.Disk`  
[ `compute.googleapis.com/Firewall`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls) | `google.compute.Firewall`  
[ `compute.googleapis.com/ForwardingRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) | `google.compute.ForwardingRule`  
[ `compute.googleapis.com/GlobalAddress`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses) | `google.compute.GlobalAddress`  
[ `compute.googleapis.com/GlobalForwardingRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules) | `google.compute.GlobalForwardingRule`  
[ `compute.googleapis.com/HealthCheck`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks) | `google.compute.HealthCheck`  
[ `compute.googleapis.com/HttpHealthCheck`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks) | `google.compute.HttpHealthCheck`  
[ `compute.googleapis.com/HttpsHealthCheck`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks) | `google.compute.HttpsHealthCheck`  
[ `compute.googleapis.com/Image`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images) | `google.compute.Image`  
[ `compute.googleapis.com/Instance`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) | `google.compute.Instance`  
[ `compute.googleapis.com/InstanceGroup`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups) | `google.compute.InstanceGroup`  
[ `compute.googleapis.com/InstanceGroupManagers`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers) | `google.compute.InstanceGroupManager`  
[ `compute.googleapis.com/InstanceTemplate`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates) | `google.compute.InstanceTemplate`  
[ `compute.googleapis.com/InterconnectAttachment`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments) | `google.compute.InterconnectAttachment`  
[ `compute.googleapis.com/License`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/licenses) | `google.compute.License`  
[ `compute.googleapis.com/Network`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) | `google.compute.Network`  
[ `compute.googleapis.com/NetworkEndpointGroup`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups) | `google.compute.NetworkEndpointGroup`  
[ `compute.googleapis.com/NodeGroup`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups) | `google.compute.NodeGroup`  
[ `compute.googleapis.com/NodeTemplate`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates) | `google.compute.NodeTemplate`  
[ `compute.googleapis.com/PacketMirroring`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings) | `google.compute.PacketMirroring`  
[ `compute.googleapis.com/Project`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects) | `google.compute.Project`  
[ `compute.googleapis.com/RegionBackendService`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices) | `google.compute.RegionBackendService`  
[ `compute.googleapis.com/RegionDisk`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks) | `google.compute.RegionDisk`  
[ `compute.googleapis.com/Reservation`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations) | `google.compute.Reservation`  
[ `compute.googleapis.com/ResourcePolicy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies) | `google.compute.ResourcePolicy`  
[ `compute.googleapis.com/Route`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes) | `google.compute.Route`  
[ `compute.googleapis.com/Router`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers) | `google.compute.Router`  
[ `compute.googleapis.com/SecurityPolicy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies) | `google.compute.SecurityPolicy`  
[ `compute.googleapis.com/Snapshot`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots) | `google.compute.Snapshot`  
[ `compute.googleapis.com/SslCertificate`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates) | `google.compute.SslCertificate`  
[ `compute.googleapis.com/SslPolicy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslPolicies) | `google.compute.SslPolicy`  
[ `compute.googleapis.com/Subnetwork`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks) | `google.compute.Subnetwork`  
[ `compute.googleapis.com/TargetHttpProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies) | `google.compute.TargetHttpProxy`  
[ `compute.googleapis.com/TargetHttpsProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies) | `google.compute.TargetHttpsProxy`  
[ `compute.googleapis.com/TargetInstance`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetInstances) | `google.compute.TargetInstance`  
[ `compute.googleapis.com/TargetPool`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetPools) | `google.compute.TargetPool`  
[ `compute.googleapis.com/TargetSslProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies) | `google.compute.TargetSslProxy`  
[ `compute.googleapis.com/TargetTcpProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetTcpProxies) | `google.compute.TargetTcpProxy`  
[ `compute.googleapis.com/TargetVpnGateway`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways) | `google.compute.TargetVpnGateway`  
[ `compute.googleapis.com/UrlMap`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps) | `google.compute.UrlMap`  
[ `compute.googleapis.com/VpnGateway`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways) | `google.compute.VpnGateway`  
[ `compute.googleapis.com/VpnGateway`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways) | `google.compute.VpnGateway`  
[ `compute.googleapis.com/VpnTunnel`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels) | `google.compute.VpnTunnel`  
**Container Registry** Note: Container Registry implements the [ Docker HTTP API V2](https://docs.docker.com/registry/spec/api/) and does not provide a public API. | `containerregistry.googleapis.com/Image` | `google.containerregistry.Image`  
**Dataflow** | [ `dataflow.googleapis.com/Job`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs) | `google.dataflow.Job`  
**Managed Service for Apache Spark** | [ `dataproc.googleapis.com/Cluster`](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters) | `google.cloud.dataproc.Cluster`  
**Google Kubernetes Engine** | [ `container.googleapis.com/Cluster`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters) | `google.container.Cluster`  
[ `rbac.authorization.k8s.io/ClusterRole`](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/) | `google.container.ClusterRole`  
[ `rbac.authorization.k8s.io/ClusterRoleBinding`](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-binding-v1/) | `google.container.ClusterRoleBinding`  
[ `k8s.io/Namespace`](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/) | `google.container.Namespace`  
[ `k8s.io/Node`](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/) | `google.container.Node`  
[ `k8s.io/Pod`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/) | `google.container.Pod`  
[ `rbac.authorization.k8s.io/Role`](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-v1/) | `google.container.Role`  
[ `rbac.authorization.k8s.io/RoleBinding`](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-binding-v1/) | `google.container.RoleBinding`  
[ `k8s.io/Service`](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/) | `google.container.Service`  
**Identity and Access Management** | [ `iam.googleapis.com/Role`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles) | `google.iam.Role`  
[ `iam.googleapis.com/ServiceAccount`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts) | `google.iam.ServiceAccount`  
[ `iam.googleapis.com/ServiceAccountKey`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys) | `google.iam.ServiceAccountKey`  
**Pub/Sub** | [ `pubsub.googleapis.com/Snapshot`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/Snapshot) | `google.pubsub.Snapshot`  
[ `pubsub.googleapis.com/Subscription`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions) | `google.pubsub.Subscription`  
[ `pubsub.googleapis.com/Topic`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics) | `google.pubsub.Topic`  
**Resource Manager** | [ `cloudresourcemanager.googleapis.com/Organization`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations) | `google.cloud.resourcemanager.Organization`  
[ `cloudresourcemanager.googleapis.com/Folder`](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders) | `google.cloud.resourcemanager.Folder`  
[ `cloudresourcemanager.googleapis.com/Project`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects) | `google.cloud.resourcemanager.Project`  
**Serverless VPC Access** | [ `vpcaccess.googleapis.com/Connector`](https://vpcaccess.googleapis.com/$discovery/rest?version=v1) | `google.vpcaccess.Connector`  
**Service Usage** | [ `serviceusage.googleapis.com/Service`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services) | `google.serviceusage.Service`  
**Gemini Enterprise Agent Platform** | [ `aiplatform.googleapis.com/BatchPredictionJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs) | `google.aiplatform.BatchPredictionJob`  
[ `aiplatform.googleapis.com/CustomJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.customJobs) | `google.aiplatform.CustomJob`  
[ `aiplatform.googleapis.com/Dataset`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.datasets) | `google.aiplatform.Dataset`  
[ `aiplatform.googleapis.com/Endpoint`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints) | `google.aiplatform.Endpoint`  
[ `aiplatform.googleapis.com/HyperparameterTuningJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.hyperparameterTuningJobs) | `google.aiplatform.HyperparameterTuningJob`  
[ `aiplatform.googleapis.com/Model`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models) | `google.aiplatform.Model`  
[ `aiplatform.googleapis.com/SpecialistPool`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.specialistPools) | `google.aiplatform.SpecialistPool`  
[ `aiplatform.googleapis.com/TrainingPipeline`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.trainingPipelines) | `google.aiplatform.TrainingPipeline`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
