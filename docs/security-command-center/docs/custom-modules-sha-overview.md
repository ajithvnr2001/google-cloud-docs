---
url: https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview/
title: Overview of custom modules for Security Health Analytics \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:58.184750+00:00
---

# Overview of custom modules for Security Health Analytics  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of custom modules for Security Health Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides an overview of Security Health Analytics _custom modules_. For information about _predefined modules_ , see [Security Health Analytics predefined detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-detectors-built-in).

With custom modules, you can extend Security Health Analytics's detection capabilities by creating custom detectors that scan the Google Cloud resources and policies that you specify using rules that you define to check for vulnerabilities, misconfigurations, or compliance violations.

The configuration or definition of a custom module, whether you create it in the Google Cloud console or code it yourself, determines the resources that the detector checks, the properties the detector evaluates, and the information that the detector returns when a vulnerability or misconfiguration is detected.

You can create custom modules for any resource or asset that Security Command Center supports.

If you code custom module definitions yourself, you use YAML and Common Expression Language (CEL) expressions. If you use the Google Cloud console to create your custom modules, most of the coding is done for you, although you do need to code the CEL expressions.

For an example of custom module definition in a YAML file, see [Example custom module definition](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code#example_custom_module_definition).

Custom modules run alongside Security Health Analytics's predefined detectors in real-time, batch, or mixed-mode. For more information about these modes, see [Security Health Analytics scan types](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-scan-types).

During a scan, each custom detector is applied to all matching assets in each organization, folder, or project for which it is enabled.

Findings from custom detectors are written to Security Command Center.

For more information, see the following:

  * [Creating custom modules](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create#create_module)
  * [Security Health Analytics scan types](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-scan-types)
  * Supported resource types
  * [YAML](https://yaml.org/spec/)
  * [Introduction to CEL](https://github.com/google/cel-spec/blob/master/doc/intro.md)



## Comparing predefined detectors and custom modules

Custom modules offer broader detection capabilities than predefined Security Health Analytics detectors. However, custom modules lack support for some Security Command Center features that the predefined detectors provide.

### Feature support

Security Health Analytics custom modules are not supported by attack path simulations. Findings that are produced by custom modules don't include [attack exposure scores or attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

### Comparing detection logic

As an example of some of the things that you can do with a custom module, compare what the predefined detector `PUBLIC_SQL_INSTANCE` checks for with what you can do with a custom module.

The predefined detector `PUBLIC_SQL_INSTANCE` checks whether the `authorizedNetworks` property of Cloud SQL instances is set to `0.0.0.0/0`. If it is, the detector generates a finding that states that the Cloud SQL instance is open to the public, because it accepts connections from all IP addresses.

With a custom module, you can implement more complex detection logic to check Cloud SQL instances for things like:

  * IP addresses with specific prefixes, by using wildcards.
  * The value of the `state` property, which you can use to ignore instances if the value is set to `MAINTENANCE` or trigger findings if the value is something else.
  * The value of the `region` property, which you can use to trigger findings only for instances with public IP addresses in specific regions.



## Required IAM roles and permissions

IAM roles determine the actions that you can perform with Security Health Analytics custom modules.

The following table contains a list of Security Health Analytics custom module permissions that are required as well as the predefined IAM roles that include them.

You can use the Google Cloud console or Security Command Center API to apply these roles at the organization, folder, or project level.

Permissions required | Roles  
---|---  
`securitycentermanagement.securityHealthAnalyticsCustomModules.create  
securitycentermanagement.securityHealthAnalyticsCustomModules.update  
securitycentermanagement.securityHealthAnalyticsCustomModules.delete  
securitycentermanagement.securityHealthAnalyticsCustomModules.list  
securitycentermanagement.securityHealthAnalyticsCustomModules.get  
securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list  
securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get  
securitycentermanagement.securityHealthAnalyticsCustomModules.simulate  
securitycentermanagement.securityHealthAnalyticsCustomModules.test ` | `roles/securitycentermanagement.shaCustomModulesEditor  
roles/securitycenter.settingsEditor  
roles/securitycenter.admin`  
`securitycentermanagement.securityHealthAnalyticsCustomModules.list  
securitycentermanagement.securityHealthAnalyticsCustomModules.get  
securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list  
securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get  
securitycentermanagement.securityHealthAnalyticsCustomModules.simulate  
securitycentermanagement.securityHealthAnalyticsCustomModules.test ` | `roles/securitycentermanagement.shaCustomModulesViewer   
roles/securitycenter.settingsViewer  
roles/securitycenter.adminViewer  
roles/securitycenter.admin`  
  
For more information about IAM permissions and roles and how to grant them, see [Grant an IAM role by using the Google Cloud console](https://docs.cloud.google.com/iam/docs/grant-role-console).

## Custom module quotas

Security Health Analytics custom modules are subject to quota limits.

The default quota limit for the creation of custom modules is 100, but you can request a quota increase, if necessary.

API calls to custom module methods are also subject to quota limits. The following table shows the default quota limits for custom module API calls.

API Call Type | Limit  
---|---  
**CustomModules Read Requests** (Get, List) | 1,000 API calls per minute, per organization  
**CustomModules Write Requests** (Create, Update, Delete) | 60 API calls per minute, per organization  
**CustomModules Test Requests** | 12 API calls per minute, per organization  
  
For quota increases, submit a request in the Google Cloud console on the [**Quotas**](https://console.cloud.google.com/iam-admin/quotas) page.

For more information about Security Command Center quotas, see [Quotas and limits](https://docs.cloud.google.com/security-command-center/quotas).

## Supported resource types

This section summarizes the Google Cloud resource types supported with custom modules.

Service name | Resource name  
---|---  
Access Context Manager | [ `accesscontextmanager.googleapis.com/AccessLevel`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)   
[ `accesscontextmanager.googleapis.com/AccessPolicy`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies)   
[ `accesscontextmanager.googleapis.com/ServicePerimeter`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)  
Gemini Enterprise Agent Platform | [ `aiplatform.googleapis.com/BatchPredictionJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs)   
[ `aiplatform.googleapis.com/CustomJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.customJobs)   
[ `aiplatform.googleapis.com/Dataset`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.datasets)   
[ `aiplatform.googleapis.com/Endpoint`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints)   
[ `aiplatform.googleapis.com/Featurestore`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores)   
[ `aiplatform.googleapis.com/HyperparameterTuningJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.hyperparameterTuningJobs)   
[ `aiplatform.googleapis.com/Index`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.indexes)   
[ `aiplatform.googleapis.com/MetadataStore`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores)   
[ `aiplatform.googleapis.com/Model`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models)   
[ `aiplatform.googleapis.com/NotebookRuntimeTemplate`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookRuntimeTemplates)   
[ `aiplatform.googleapis.com/SpecialistPool`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.specialistPools)   
[ `aiplatform.googleapis.com/Tensorboard`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.tensorboards)   
[ `aiplatform.googleapis.com/TrainingPipeline`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.trainingPipelines)  
AlloyDB | [ `alloydb.googleapis.com/Backup`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.backups)   
[ `alloydb.googleapis.com/Cluster`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters)   
[ `alloydb.googleapis.com/Instance`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances)  
API keys | [ `apikeys.googleapis.com/Key`](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/keys)  
Artifact Registry Repository | [ `artifactregistry.googleapis.com/Repository`](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories)  
BigQuery | [ `bigquery.googleapis.com/Dataset`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets)   
[ `bigquery.googleapis.com/Model`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/models)   
[ `bigquery.googleapis.com/Table`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables)   
[ `bigquerydatatransfer.googleapis.com/TransferConfig`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs)  
Cloud Billing Project Billing Info | [ `cloudbilling.googleapis.com/ProjectBillingInfo`](https://docs.cloud.google.com/billing/docs/reference/rest/v1/ProjectBillingInfo)  
Cloud Run functions | [ `cloudfunctions.googleapis.com/CloudFunction`](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions)  
Cloud KMS |  [ `cloudkms.googleapis.com/CryptoKey`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys)   
[ `cloudkms.googleapis.com/CryptoKeyVersion`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions)   
[ `cloudkms.googleapis.com/ImportJob`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs)   
[ `cloudkms.googleapis.com/KeyRing`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings)  
Resource Manager | [ `cloudresourcemanager.googleapis.com/Folder`](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders)   
[ `cloudresourcemanager.googleapis.com/Organization`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations)   
[ `cloudresourcemanager.googleapis.com/Project`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects)   
[ `cloudresourcemanager.googleapis.com/TagBinding`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings)  
Managed Service for Apache Airflow Environment | [ `composer.googleapis.com/Environment`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments)  
Compute Engine | [ `compute.googleapis.com/Address`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses)   
[ `compute.googleapis.com/Autoscaler`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers)   
[ `compute.googleapis.com/BackendBucket`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets)   
[ `compute.googleapis.com/BackendService`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices)   
[ `compute.googleapis.com/Commitment`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments)   
[ `compute.googleapis.com/Disk`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks)   
[ `compute.googleapis.com/Firewall`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls)   
[ `compute.googleapis.com/FirewallPolicy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies)   
[ `compute.googleapis.com/ForwardingRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules)   
[ `compute.googleapis.com/GlobalForwardingRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules)   
[ `compute.googleapis.com/HealthCheck`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks)   
[ `compute.googleapis.com/Image`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images)   
[ `compute.googleapis.com/Instance`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances)   
[ `compute.googleapis.com/InstanceGroup`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups)   
[ `compute.googleapis.com/InstanceGroupManagers`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers)   
[ `compute.googleapis.com/InstanceTemplate`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates)   
[ `compute.googleapis.com/InterconnectAttachment`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments)   
[ `compute.googleapis.com/MachineImage`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/machineImages)   
[ `compute.googleapis.com/Network`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks)   
[ `compute.googleapis.com/NetworkEndpointGroup`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups)   
[ `compute.googleapis.com/NodeGroup`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups)   
[ `compute.googleapis.com/NodeTemplate`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates)   
[ `compute.googleapis.com/PacketMirroring`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings)   
[ `compute.googleapis.com/Project`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects)   
[ `compute.googleapis.com/RegionBackendService`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices)   
[ `compute.googleapis.com/RegionDisk`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks)   
[ `compute.googleapis.com/Reservation`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations)   
[ `compute.googleapis.com/ResourcePolicy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies)   
[ `compute.googleapis.com/Route`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes)   
[ `compute.googleapis.com/Router`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers)   
[ `compute.googleapis.com/SecurityPolicy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies)   
[ `compute.googleapis.com/Snapshot`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots)   
[ `compute.googleapis.com/SslCertificate`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)   
[ `compute.googleapis.com/SslPolicy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslPolicies)   
[ `compute.googleapis.com/Subnetwork`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks)   
[ `compute.googleapis.com/TargetHttpProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies)   
[ `compute.googleapis.com/TargetHttpsProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies)   
[ `compute.googleapis.com/TargetInstance`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetInstances)   
[ `compute.googleapis.com/TargetPool`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetPools)   
[ `compute.googleapis.com/TargetSslProxy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies)   
[ `compute.googleapis.com/TargetVpnGateway`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways)   
[ `compute.googleapis.com/UrlMap`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps)   
[ `compute.googleapis.com/VpnGateway`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways)   
[ `compute.googleapis.com/VpnTunnel`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels)  
Google Kubernetes Engine | [ `container.googleapis.com/Cluster`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters)   
[ `container.googleapis.com/NodePool`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools)  
Dataflow | [ `dataflow.googleapis.com/Job`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs)  
Cloud Data Fusion | [ `datafusion.googleapis.com/Instance`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances)  
Managed Service for Apache Spark | [ `dataproc.googleapis.com/AutoscalingPolicy`](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.autoscalingPolicies)   
[ `dataproc.googleapis.com/Batch`](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.batches)   
[ `dataproc.googleapis.com/Cluster`](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters)   
[ `dataproc.googleapis.com/Job`](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs)  
Datastream | [ `datastream.googleapis.com/ConnectionProfile`](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles)   
[ `datastream.googleapis.com/PrivateConnection`](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections)   
[ `datastream.googleapis.com/Stream`](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams)  
Dialogflow CX | [ `dialogflow.googleapis.com/Agent`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents)  
Sensitive Data Protection | [ `dlp.googleapis.com/DeidentifyTemplate`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.deidentifyTemplates)   
[ `dlp.googleapis.com/DlpJob`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs)   
[ `dlp.googleapis.com/InspectTemplate`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.inspectTemplates)   
[ `dlp.googleapis.com/JobTrigger`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.jobTriggers)   
[ `dlp.googleapis.com/StoredInfoType`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.storedInfoTypes)  
Cloud DNS | [ `dns.googleapis.com/ManagedZone`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones)   
[ `dns.googleapis.com/Policy`](https://docs.cloud.google.com/dns/docs/reference/v1/policies)  
Filestore | [ `file.googleapis.com/Instance`](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances)  
GKE Fleet (also known as fleets) |  [ `gkehub.googleapis.com/Feature`](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.features)   
[ `gkehub.googleapis.com/Membership`](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.memberships)  
IAM |  [ `iam.googleapis.com/Role`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles)   
[ `iam.googleapis.com/ServiceAccountKey`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys)  
`Kubernetes` |  [ `k8s.io/Namespace`](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)   
[ `k8s.io/Node`](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/)   
[ `k8s.io/Pod`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/)   
[ `k8s.io/Service`](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)   
[ `apps.k8s.io/DaemonSet`](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)   
[ `apps.k8s.io/Deployment`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/)   
[ `apps.k8s.io/ReplicaSet`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)   
[ `apps.k8s.io/StatefulSet`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)   
[ `batch.k8s.io/CronJob`](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)   
[ `networking.k8s.io/Ingress`](https://kubernetes.io/docs/concepts/services-networking/ingress/)   
[ `networking.k8s.io/NetworkPolicy`](https://kubernetes.io/docs/concepts/services-networking/network-policies/)   
[ `rbac.authorization.k8s.io/ClusterRole`](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/)   
[ `rbac.authorization.k8s.io/ClusterRoleBinding`](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-binding-v1/)   
[ `rbac.authorization.k8s.io/Role`](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-v1/)   
[ `rbac.authorization.k8s.io/RoleBinding`](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-binding-v1/)  
Cloud Logging | [ `logging.googleapis.com/LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets)   
[ `logging.googleapis.com/LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics)   
[ `logging.googleapis.com/LogSink`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks)  
Cloud Monitoring | [ `monitoring.googleapis.com/AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)   
[ `monitoring.googleapis.com/NotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels)  
NetApp Volumes | [ `netapp.googleapis.com/Snapshot`](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.snapshots)   
[ `netapp.googleapis.com/Volume`](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes)  
Gemini Enterprise Agent Platform Workbench | [ `notebooks.googleapis.com/Instance`](https://docs.cloud.google.com/vertex-ai/docs/workbench/reference/rest/v2/projects.locations.instances)  
Organization Policy Service v2 | [ `orgpolicy.googleapis.com/CustomConstraint`](https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest/v2/organizations.customConstraints)   
[ `orgpolicy.googleapis.com/Policy`](https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest/v2/organizations.policies)  
Certificate Authority Service | [ `privateca.googleapis.com/Certificate`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates)   
[ `privateca.googleapis.com/CertificateRevocationList`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificateAuthorities.certificateRevocationLists)  
Pub/Sub | [ `pubsub.googleapis.com/Snapshot`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.snapshots)   
[ `pubsub.googleapis.com/Subscription`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)   
[ `pubsub.googleapis.com/Topic`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)  
Memorystore for Redis | [ `redis.googleapis.com/Cluster`](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters)   
[ `redis.googleapis.com/Instance`](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances)  
Cloud Run | [ `run.googleapis.com/DomainMapping`](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.domainmappings)   
[ `run.googleapis.com/Execution`](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.executions)   
[ `run.googleapis.com/Job`](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs)   
[ `run.googleapis.com/Revision`](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions)   
[ `run.googleapis.com/Service`](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.services)  
Secret Manager | [ `secretmanager.googleapis.com/Secret`](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets)   
[ `secretmanager.googleapis.com/SecretVersion`](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions)  
Service Usage | [ `serviceusage.googleapis.com/Service`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services)  
Spanner | [ `spanner.googleapis.com/Backup`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups)   
[ `spanner.googleapis.com/Database`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases)   
[ `spanner.googleapis.com/Instance`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances)  
Cloud SQL for MySQL | [ `sqladmin.googleapis.com/BackupRun`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns)   
[ `sqladmin.googleapis.com/Instance`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances)  
Cloud Storage | [ `storage.googleapis.com/Bucket`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets)  
Google Cloud VMware Engine | [ `vmwareengine.googleapis.com/Cluster`](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.clusters)   
[ `vmwareengine.googleapis.com/ExternalAccessRule`](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules)   
[ `vmwareengine.googleapis.com/ExternalAddress`](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses)   
[ `vmwareengine.googleapis.com/NetworkPeering`](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.global.networkPeerings)   
[ `vmwareengine.googleapis.com/NetworkPolicy`](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPolicies)   
[ `vmwareengine.googleapis.com/PrivateCloud`](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds)   
[ `vmwareengine.googleapis.com/PrivateConnection`](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateConnections)   
[ `vmwareengine.googleapis.com/VmwareEngineNetwork`](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.vmwareEngineNetworks)  
VPC Connector | [ `vpcaccess.googleapis.com/Connector`](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1/projects.locations.connectors)  
Cloud Workstations | [ `workstations.googleapis.com/Workstation`](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs.workstations)   
[ `workstations.googleapis.com/WorkstationConfig`](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs)  
  
## What's next

  * To work with custom modules, see [Using custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create).
  * To code custom module definitions yourself, see [Code custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code).
  * To test your custom modules, see [Test custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
