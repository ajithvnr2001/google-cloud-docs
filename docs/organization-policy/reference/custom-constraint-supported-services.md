---
url: https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services/
title: Services that support custom constraints \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:46.770904+00:00
---

# Services that support custom constraints  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  Services that support custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

Custom organization policies allow administrators to define their own restrictions on Google Cloud services. For more information about custom constraints, see the [Custom constraints overview](https://docs.cloud.google.com/organization-policy/overview#custom-constraints).

Each service defines the set of custom constraint fields that can be used to enforce organization policies on their service resources. See the list of supported service resources to learn which Google Cloud services support custom constraints. To learn how to create custom constraints, see [Create custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints).

For a list of sample custom constraints, see the [custom organization policy library](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/custom-organization-policy-library) on GitHub.

## Supported service resources

Resources associated with the following services can be subjected to custom constraints. Not all resource attributes are available for these resources. See the service-specific documentation to find the resources and attributes that are available for use.

Any launch statusPreviewGAGoogle Cloud service | Resource type | Launch status  
---|---|---  
Access Context Manager  |  ` [ accesscontextmanager.googleapis.com/AccessLevel ](https://docs.cloud.google.com/access-context-manager/docs/custom-constraints) ` |  GA   
` [ accesscontextmanager.googleapis.com/AccessPolicy ](https://docs.cloud.google.com/access-context-manager/docs/custom-constraints) ` |  GA   
` [ accesscontextmanager.googleapis.com/AuthorizedOrgsDesc ](https://docs.cloud.google.com/access-context-manager/docs/custom-constraints) ` |  GA   
` [ accesscontextmanager.googleapis.com/ServicePerimeter ](https://docs.cloud.google.com/access-context-manager/docs/custom-constraints) ` |  GA   
Agent Identity API  |  ` [ agentidentity.googleapis.com/AuthProvider ](https://docs.cloud.google.com/iam/docs/agent-identity-custom-constraints) ` |  Preview   
AI Platform Training  |  ` [ aiplatform.googleapis.com/CustomJob ](https://docs.cloud.google.com/vertex-ai/docs/training/custom-constraints) ` |  GA   
` [ aiplatform.googleapis.com/HyperparameterTuningJob ](https://docs.cloud.google.com/vertex-ai/docs/training/custom-constraints) ` |  GA   
` [ aiplatform.googleapis.com/NasJob ](https://docs.cloud.google.com/vertex-ai/docs/training/custom-constraints) ` |  GA   
AlloyDB for PostgreSQL  |  ` [ alloydb.googleapis.com/Backup ](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints) ` |  Preview   
` [ alloydb.googleapis.com/Cluster ](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints) ` |  Preview   
` [ alloydb.googleapis.com/Instance ](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints) ` |  Preview   
API keys  |  ` [ apikeys.googleapis.com/Key ](https://docs.cloud.google.com/api-keys/docs/custom-constraints) ` |  GA   
Application Integration  |  ` [ integrations.googleapis.com/AuthConfig ](https://docs.cloud.google.com/application-integration/docs/custom-constraints) ` |  Preview   
` [ integrations.googleapis.com/IntegrationVersion ](https://docs.cloud.google.com/application-integration/docs/custom-constraints) ` |  Preview   
` [ integrations.googleapis.com/SfdcChannel ](https://docs.cloud.google.com/application-integration/docs/custom-constraints) ` |  Preview   
` [ integrations.googleapis.com/SfdcInstance ](https://docs.cloud.google.com/application-integration/docs/custom-constraints) ` |  Preview   
Artifact Analysis  |  ` [ containeranalysis.googleapis.com/Note ](https://docs.cloud.google.com/artifact-analysis/docs/custom-constraints) ` |  GA   
` [ containeranalysis.googleapis.com/Occurrence ](https://docs.cloud.google.com/artifact-analysis/docs/custom-constraints) ` |  GA   
Artifact Registry  |  ` [ artifactregistry.googleapis.com/Repository ](https://docs.cloud.google.com/artifact-registry/docs/custom-constraints) ` |  GA   
Backup and DR Service  |  ` [ backupdr.googleapis.com/Backup ](https://docs.cloud.google.com/backup-disaster-recovery/docs/customconstraints) ` |  GA   
` [ backupdr.googleapis.com/BackupPlan ](https://docs.cloud.google.com/backup-disaster-recovery/docs/customconstraints) ` |  GA   
` [ backupdr.googleapis.com/BackupPlanAssociation ](https://docs.cloud.google.com/backup-disaster-recovery/docs/customconstraints) ` |  GA   
` [ backupdr.googleapis.com/BackupVault ](https://docs.cloud.google.com/backup-disaster-recovery/docs/customconstraints) ` |  GA   
Backup for GKE  |  ` [ gkebackup.googleapis.com/Backup ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/create-custom-constraints) ` |  GA   
` [ gkebackup.googleapis.com/BackupPlan ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/create-custom-constraints) ` |  GA   
` [ gkebackup.googleapis.com/Restore ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/create-custom-constraints) ` |  GA   
` [ gkebackup.googleapis.com/RestorePlan ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/create-custom-constraints) ` |  GA   
BigQuery  |  ` [ bigquery.googleapis.com/Dataset ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  GA   
` [ bigquery.googleapis.com/Routine ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  Preview   
` [ bigquery.googleapis.com/RowAccessPolicy ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  Preview   
` [ bigquery.googleapis.com/Table ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  Preview   
BigQuery Data Policy  |  ` [ bigquerydatapolicy.googleapis.com/DataPolicy ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  Preview   
BigQuery Data Transfer Service  |  ` [ bigquerydatatransfer.googleapis.com/TransferConfig ](https://docs.cloud.google.com/bigquery/docs/transfer-custom-constraints) ` |  GA   
BigQuery Migration Service  |  ` [ bigquerymigration.googleapis.com/MigrationWorkflow ](https://docs.cloud.google.com/bigquery/docs/migration-custom-org-policies) ` |  Preview   
BigQuery Reservation API  |  ` [ bigqueryreservation.googleapis.com/BiReservation ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  Preview   
` [ bigqueryreservation.googleapis.com/CapacityCommitment ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  Preview   
` [ bigqueryreservation.googleapis.com/Reservation ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  Preview   
` [ bigqueryreservation.googleapis.com/ReservationAssignment ](https://docs.cloud.google.com/bigquery/docs/custom-constraints) ` |  Preview   
BigQuery sharing  |  ` [ analyticshub.googleapis.com/DataExchange ](https://docs.cloud.google.com/bigquery/docs/analytics-hub-custom-constraints) ` |  GA   
` [ analyticshub.googleapis.com/Listing ](https://docs.cloud.google.com/bigquery/docs/analytics-hub-custom-constraints) ` |  GA   
Binary Authorization  |  ` [ binaryauthorization.googleapis.com/Attestor ](https://docs.cloud.google.com/binary-authorization/docs/binary-authorization-custom-constraints) ` |  GA   
` [ binaryauthorization.googleapis.com/Policy ](https://docs.cloud.google.com/binary-authorization/docs/binary-authorization-custom-constraints) ` |  GA   
Certificate Authority Service  |  ` [ privateca.googleapis.com/CaPool ](https://docs.cloud.google.com/certificate-authority-service/docs/custom-constraints) ` |  GA   
` [ privateca.googleapis.com/CertificateAuthority ](https://docs.cloud.google.com/certificate-authority-service/docs/custom-constraints) ` |  GA   
` [ privateca.googleapis.com/CertificateTemplate ](https://docs.cloud.google.com/certificate-authority-service/docs/custom-constraints) ` |  GA   
Certificate Manager  |  ` [ certificatemanager.googleapis.com/Certificate ](https://docs.cloud.google.com/certificate-manager/docs/custom-constraints) ` |  GA   
` [ certificatemanager.googleapis.com/CertificateIssuanceConfig ](https://docs.cloud.google.com/certificate-manager/docs/custom-constraints) ` |  GA   
` [ certificatemanager.googleapis.com/CertificateMap ](https://docs.cloud.google.com/certificate-manager/docs/custom-constraints) ` |  GA   
` [ certificatemanager.googleapis.com/CertificateMapEntry ](https://docs.cloud.google.com/certificate-manager/docs/custom-constraints) ` |  GA   
` [ certificatemanager.googleapis.com/DnsAuthorization ](https://docs.cloud.google.com/certificate-manager/docs/custom-constraints) ` |  GA   
` [ certificatemanager.googleapis.com/TrustConfig ](https://docs.cloud.google.com/certificate-manager/docs/custom-constraints) ` |  GA   
Cloud Bigtable Admin API  |  ` [ bigtableadmin.googleapis.com/AppProfile ](https://docs.cloud.google.com/bigtable/docs/custom-constraints) ` |  GA   
` [ bigtableadmin.googleapis.com/Backup ](https://docs.cloud.google.com/bigtable/docs/custom-constraints) ` |  GA   
` [ bigtableadmin.googleapis.com/Cluster ](https://docs.cloud.google.com/bigtable/docs/custom-constraints) ` |  GA   
` [ bigtableadmin.googleapis.com/Instance ](https://docs.cloud.google.com/bigtable/docs/custom-constraints) ` |  GA   
` [ bigtableadmin.googleapis.com/LogicalView ](https://docs.cloud.google.com/bigtable/docs/custom-constraints) ` |  GA   
` [ bigtableadmin.googleapis.com/MaterializedView ](https://docs.cloud.google.com/bigtable/docs/custom-constraints) ` |  GA   
` [ bigtableadmin.googleapis.com/SchemaBundle ](https://docs.cloud.google.com/bigtable/docs/custom-constraints) ` |  GA   
` [ bigtableadmin.googleapis.com/Table ](https://docs.cloud.google.com/bigtable/docs/custom-constraints) ` |  GA   
Cloud Build  |  ` [ cloudbuild.googleapis.com/BitbucketServerConfig ](https://docs.cloud.google.com/build/docs/custom-constraints) ` |  GA   
` [ cloudbuild.googleapis.com/Build ](https://docs.cloud.google.com/build/docs/custom-constraints) ` |  GA   
` [ cloudbuild.googleapis.com/BuildTrigger ](https://docs.cloud.google.com/build/docs/custom-constraints) ` |  GA   
` [ cloudbuild.googleapis.com/Connection ](https://docs.cloud.google.com/build/docs/custom-constraints) ` |  GA   
` [ cloudbuild.googleapis.com/GithubEnterpriseConfig ](https://docs.cloud.google.com/build/docs/custom-constraints) ` |  GA   
` [ cloudbuild.googleapis.com/Repository ](https://docs.cloud.google.com/build/docs/custom-constraints) ` |  GA   
` [ cloudbuild.googleapis.com/WorkerPool ](https://docs.cloud.google.com/build/docs/custom-constraints) ` |  GA   
Cloud Data Fusion  |  ` [ datafusion.googleapis.com/DnsPeering ](https://docs.cloud.google.com/data-fusion/docs/how-to/create-custom-constraints) ` |  GA   
` [ datafusion.googleapis.com/Instance ](https://docs.cloud.google.com/data-fusion/docs/how-to/create-custom-constraints) ` |  GA   
Cloud Deploy  |  ` [ clouddeploy.googleapis.com/Automation ](https://docs.cloud.google.com/deploy/docs/custom-org-policy) ` |  GA   
` [ clouddeploy.googleapis.com/CustomTargetType ](https://docs.cloud.google.com/deploy/docs/custom-org-policy) ` |  GA   
` [ clouddeploy.googleapis.com/DeliveryPipeline ](https://docs.cloud.google.com/deploy/docs/custom-org-policy) ` |  GA   
` [ clouddeploy.googleapis.com/DeployPolicy ](https://docs.cloud.google.com/deploy/docs/custom-org-policy) ` |  GA   
` [ clouddeploy.googleapis.com/Release ](https://docs.cloud.google.com/deploy/docs/custom-org-policy) ` |  GA   
` [ clouddeploy.googleapis.com/Rollout ](https://docs.cloud.google.com/deploy/docs/custom-org-policy) ` |  GA   
` [ clouddeploy.googleapis.com/Target ](https://docs.cloud.google.com/deploy/docs/custom-org-policy) ` |  GA   
Cloud DNS  |  ` [ dns.googleapis.com/ManagedZone ](https://docs.cloud.google.com/dns/docs/create-custom-constraints) ` |  GA   
` [ dns.googleapis.com/Policy ](https://docs.cloud.google.com/dns/docs/create-custom-constraints) ` |  GA   
` [ dns.googleapis.com/ResourceRecordSet ](https://docs.cloud.google.com/dns/docs/create-custom-constraints) ` |  GA   
` [ dns.googleapis.com/ResponsePolicy ](https://docs.cloud.google.com/dns/docs/create-custom-constraints) ` |  GA   
` [ dns.googleapis.com/ResponsePolicyRule ](https://docs.cloud.google.com/dns/docs/create-custom-constraints) ` |  GA   
Cloud Domains  |  ` [ domains.googleapis.com/Registration ](https://docs.cloud.google.com/domains/docs/custom-constraints) ` |  GA   
Cloud Healthcare API  |  ` [ healthcare.googleapis.com/ConsentStore ](https://docs.cloud.google.com/healthcare-api/docs/custom-org-policy) ` |  GA   
` [ healthcare.googleapis.com/Dataset ](https://docs.cloud.google.com/healthcare-api/docs/custom-org-policy) ` |  GA   
` [ healthcare.googleapis.com/DicomStore ](https://docs.cloud.google.com/healthcare-api/docs/custom-org-policy) ` |  GA   
` [ healthcare.googleapis.com/FhirStore ](https://docs.cloud.google.com/healthcare-api/docs/custom-org-policy) ` |  GA   
` [ healthcare.googleapis.com/Hl7V2Store ](https://docs.cloud.google.com/healthcare-api/docs/custom-org-policy) ` |  GA   
Cloud Interconnect  |  ` [ compute.googleapis.com/Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/custom-constraints) ` |  GA   
` [ compute.googleapis.com/InterconnectAttachment ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/custom-constraints) ` |  GA   
Cloud Key Management Service  |  ` [ cloudkms.googleapis.com/AutokeyConfig ](https://docs.cloud.google.com/kms/docs/custom-org-policies) ` |  GA   
` [ cloudkms.googleapis.com/CryptoKey ](https://docs.cloud.google.com/kms/docs/custom-org-policies) ` |  GA   
` [ cloudkms.googleapis.com/CryptoKeyVersion ](https://docs.cloud.google.com/kms/docs/custom-org-policies) ` |  GA   
` [ cloudkms.googleapis.com/EkmConfig ](https://docs.cloud.google.com/kms/docs/custom-org-policies) ` |  GA   
` [ cloudkms.googleapis.com/EkmConnection ](https://docs.cloud.google.com/kms/docs/custom-org-policies) ` |  GA   
` [ cloudkms.googleapis.com/ImportJob ](https://docs.cloud.google.com/kms/docs/custom-org-policies) ` |  GA   
` [ cloudkms.googleapis.com/KeyHandle ](https://docs.cloud.google.com/kms/docs/custom-org-policies) ` |  GA   
Cloud Load Balancing  |  ` [ compute.googleapis.com/BackendBucket ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/BackendService ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/ForwardingRule ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/HealthCheck ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/InstanceGroup ](https://docs.cloud.google.com/compute/docs/access/custom-constraints) ` |  GA   
` [ compute.googleapis.com/NetworkEndpointGroup ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/SslPolicy ](https://docs.cloud.google.com/compute/docs/access/custom-constraints) ` |  GA   
` [ compute.googleapis.com/TargetGrpcProxy ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/TargetHttpProxy ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/TargetHttpsProxy ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/TargetInstance ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/TargetPool ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/TargetSslProxy ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/TargetTcpProxy ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/UrlMap ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/ServiceLbPolicy ](https://docs.cloud.google.com/load-balancing/docs/custom-constraints) ` |  GA   
Cloud Logging  |  ` [ logging.googleapis.com/Link ](https://docs.cloud.google.com/logging/docs/custom-constraints) ` |  GA   
` [ logging.googleapis.com/LogBucket ](https://docs.cloud.google.com/logging/docs/custom-constraints) ` |  GA   
` [ logging.googleapis.com/LogMetric ](https://docs.cloud.google.com/logging/docs/custom-constraints) ` |  GA   
` [ logging.googleapis.com/LogSink ](https://docs.cloud.google.com/logging/docs/custom-constraints) ` |  GA   
` [ logging.googleapis.com/LogView ](https://docs.cloud.google.com/logging/docs/custom-constraints) ` |  GA   
` [ logging.googleapis.com/SavedQuery ](https://docs.cloud.google.com/logging/docs/custom-constraints) ` |  GA   
Cloud Monitoring  |  ` [ monitoring.googleapis.com/AlertPolicy ](https://docs.cloud.google.com/monitoring/docs/custom-constraints) ` |  GA   
` [ monitoring.googleapis.com/NotificationChannel ](https://docs.cloud.google.com/monitoring/docs/custom-constraints) ` |  GA   
` [ monitoring.googleapis.com/Snooze ](https://docs.cloud.google.com/monitoring/docs/custom-constraints) ` |  GA   
Cloud Next Generation Firewall  |  ` [ compute.googleapis.com/Firewall ](https://docs.cloud.google.com/firewall/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/FirewallPolicy ](https://docs.cloud.google.com/firewall/docs/custom-constraints-fw-policy) ` |  GA   
Cloud Quotas  |  ` [ cloudquotas.googleapis.com/QuotaPreference ](https://docs.cloud.google.com/docs/quotas/custom-constraints) ` |  Preview   
Cloud Router, Cloud NAT  |  ` [ compute.googleapis.com/Router ](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/custom-constraints) ` |  GA   
Cloud Run  |  ` [ run.googleapis.com/Job ](https://docs.cloud.google.com/run/docs/securing/custom-constraints) ` |  GA   
` [ run.googleapis.com/Service ](https://docs.cloud.google.com/run/docs/securing/custom-constraints) ` |  GA   
Cloud Run functions  |  ` [ cloudfunctions.googleapis.com/Function ](https://docs.cloud.google.com/functions/docs/securing/custom-constraints) ` |  GA   
Cloud Service Mesh  |  ` [ networksecurity.googleapis.com/AuthorizationPolicy ](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/custom-constraints) ` |  GA   
` [ networksecurity.googleapis.com/ClientTlsPolicy ](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/custom-constraints) ` |  GA   
` [ networksecurity.googleapis.com/ServerTlsPolicy ](https://docs.cloud.google.com/service-mesh/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/EndpointPolicy ](https://docs.cloud.google.com/service-mesh/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/Gateway ](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/GrpcRoute ](https://docs.cloud.google.com/service-mesh/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/HttpRoute ](https://docs.cloud.google.com/service-mesh/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/Mesh ](https://docs.cloud.google.com/service-mesh/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/ServiceBinding ](https://docs.cloud.google.com/service-mesh/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/TcpRoute ](https://docs.cloud.google.com/service-mesh/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/TlsRoute ](https://docs.cloud.google.com/service-mesh/docs/custom-constraints) ` |  GA   
Cloud SQL  |  ` [ sqladmin.googleapis.com/BackupRun ](https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy) ` |  GA   
` [ sqladmin.googleapis.com/Instance ](https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy) ` |  GA   
Cloud Storage  |  ` [ storage.googleapis.com/Bucket ](https://docs.cloud.google.com/storage/docs/custom-constraints) ` |  GA   
Cloud VPN  |  ` [ compute.googleapis.com/ExternalVpnGateway ](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/custom-constraints) ` |  GA   
` [ compute.googleapis.com/TargetVpnGateway ](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/custom-constraints) ` |  GA   
` [ compute.googleapis.com/VpnGateway ](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/custom-constraints) ` |  GA   
` [ compute.googleapis.com/VpnTunnel ](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/custom-constraints) ` |  GA   
Cloud Workstations  |  ` [ workstations.googleapis.com/Workstation ](https://docs.cloud.google.com/workstations/docs/custom-constraints) ` |  GA   
` [ workstations.googleapis.com/WorkstationCluster ](https://docs.cloud.google.com/workstations/docs/custom-constraints) ` |  GA   
` [ workstations.googleapis.com/WorkstationConfig ](https://docs.cloud.google.com/workstations/docs/custom-constraints) ` |  GA   
Colab Enterprise  |  ` [ aiplatform.googleapis.com/NotebookExecutionJob ](https://docs.cloud.google.com/colab/docs/custom-constraints) ` |  Preview   
` [ aiplatform.googleapis.com/NotebookRuntime ](https://docs.cloud.google.com/colab/docs/custom-constraints) ` |  GA   
` [ aiplatform.googleapis.com/NotebookRuntimeTemplate ](https://docs.cloud.google.com/colab/docs/custom-constraints) ` |  GA   
Compute Engine  |  ` [ compute.googleapis.com/Disk ](https://docs.cloud.google.com/compute/docs/access/custom-constraints) ` |  GA   
` [ compute.googleapis.com/Image ](https://docs.cloud.google.com/compute/docs/access/custom-constraints) ` |  GA   
` [ compute.googleapis.com/Instance ](https://docs.cloud.google.com/compute/docs/access/custom-constraints) ` |  GA   
` [ compute.googleapis.com/PreviewFeature ](https://docs.cloud.google.com/compute/docs/access/custom-constraints) ` |  GA   
Data Lineage API  |  ` [ datalineage.googleapis.com/Process ](https://docs.cloud.google.com/dataplex/docs/lineage-custom-constraints) ` |  GA   
Database Migration Service  |  ` [ datamigration.googleapis.com/ConnectionProfile ](https://docs.cloud.google.com/database-migration/docs/custom-constraints) ` |  GA   
` [ datamigration.googleapis.com/ConversionWorkspace ](https://docs.cloud.google.com/database-migration/docs/custom-constraints) ` |  GA   
` [ datamigration.googleapis.com/MigrationJob ](https://docs.cloud.google.com/database-migration/docs/custom-constraints) ` |  GA   
` [ datamigration.googleapis.com/PrivateConnection ](https://docs.cloud.google.com/database-migration/docs/custom-constraints) ` |  GA   
Dataflow  |  ` [ dataflow.googleapis.com/Job ](https://docs.cloud.google.com/dataflow/docs/custom-constraints) ` |  GA   
Dataform  |  ` [ dataform.googleapis.com/CompilationResult ](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) ` |  GA   
` [ dataform.googleapis.com/Folder ](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) ` |  GA   
` [ dataform.googleapis.com/ReleaseConfig ](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) ` |  GA   
` [ dataform.googleapis.com/Repository ](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) ` |  GA   
` [ dataform.googleapis.com/TeamFolder ](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) ` |  GA   
` [ dataform.googleapis.com/WorkflowConfig ](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) ` |  GA   
` [ dataform.googleapis.com/WorkflowInvocation ](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) ` |  GA   
` [ dataform.googleapis.com/Workspace ](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) ` |  GA   
Dataproc Metastore  |  ` [ metastore.googleapis.com/Backup ](https://docs.cloud.google.com/dataproc-metastore/docs/org-policy-custom-constraints) ` |  GA   
` [ metastore.googleapis.com/MetadataImport ](https://docs.cloud.google.com/dataproc-metastore/docs/org-policy-custom-constraints) ` |  GA   
` [ metastore.googleapis.com/Service ](https://docs.cloud.google.com/dataproc-metastore/docs/org-policy-custom-constraints) ` |  GA   
Datastream  |  ` [ datastream.googleapis.com/ConnectionProfile ](https://docs.cloud.google.com/datastream/docs/custom-constraints) ` |  GA   
` [ datastream.googleapis.com/PrivateConnection ](https://docs.cloud.google.com/datastream/docs/custom-constraints) ` |  GA   
` [ datastream.googleapis.com/Stream ](https://docs.cloud.google.com/datastream/docs/custom-constraints) ` |  GA   
Developer Connect  |  ` [ developerconnect.googleapis.com/AccountConnector ](https://docs.cloud.google.com/developer-connect/docs/custom-constraints) ` |  GA   
` [ developerconnect.googleapis.com/Connection ](https://docs.cloud.google.com/developer-connect/docs/custom-constraints) ` |  GA   
` [ developerconnect.googleapis.com/GitRepositoryLink ](https://docs.cloud.google.com/developer-connect/docs/custom-constraints) ` |  GA   
Document AI  |  ` [ documentai.googleapis.com/Processor ](https://docs.cloud.google.com/document-ai/docs/custom-org-policies) ` |  GA   
` [ documentai.googleapis.com/ProcessorVersion ](https://docs.cloud.google.com/document-ai/docs/custom-org-policies) ` |  GA   
Essential Contacts  |  ` [ essentialcontacts.googleapis.com/Contact ](https://docs.cloud.google.com/resource-manager/docs/essentialcontacts-custom-org-policies) ` |  GA   
Eventarc  |  ` [ eventarc.googleapis.com/Channel ](https://docs.cloud.google.com/eventarc/standard/docs/custom-constraints) ` |  GA   
` [ eventarc.googleapis.com/ChannelConnection ](https://docs.cloud.google.com/eventarc/standard/docs/custom-constraints) ` |  GA   
` [ eventarc.googleapis.com/Enrollment ](https://docs.cloud.google.com/eventarc/advanced/docs/custom-constraints) ` |  GA   
` [ eventarc.googleapis.com/GoogleApiSource ](https://docs.cloud.google.com/eventarc/advanced/docs/custom-constraints) ` |  GA   
` [ eventarc.googleapis.com/GoogleChannelConfig ](https://docs.cloud.google.com/eventarc/standard/docs/custom-constraints) ` |  GA   
` [ eventarc.googleapis.com/MessageBus ](https://docs.cloud.google.com/eventarc/advanced/docs/custom-constraints) ` |  GA   
` [ eventarc.googleapis.com/Pipeline ](https://docs.cloud.google.com/eventarc/advanced/docs/custom-constraints) ` |  GA   
` [ eventarc.googleapis.com/Trigger ](https://docs.cloud.google.com/eventarc/standard/docs/custom-constraints) ` |  GA   
Filestore  |  ` [ file.googleapis.com/Backup ](https://docs.cloud.google.com/filestore/docs/create-custom-constraints) ` |  GA   
` [ file.googleapis.com/Instance ](https://docs.cloud.google.com/filestore/docs/create-custom-constraints) ` |  GA   
` [ file.googleapis.com/Snapshot ](https://docs.cloud.google.com/filestore/docs/create-custom-constraints) ` |  GA   
Firestore  |  ` [ firestore.googleapis.com/Database ](https://docs.cloud.google.com/firestore/docs/custom-constraints) ` |  GA   
GKE  |  ` [ container.googleapis.com/Cluster ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies) ` |  GA   
` [ container.googleapis.com/NodePool ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies) ` |  GA   
GKE attached clusters  |  ` [ gkemulticloud.googleapis.com/AttachedCluster ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/setup-custom-constraints) ` |  GA   
GKE Fleet  |  ` gkehub.googleapis.com/Feature ` |  GA   
` gkehub.googleapis.com/Fleet ` |  GA   
` gkehub.googleapis.com/Membership ` |  GA   
` gkehub.googleapis.com/MembershipBinding ` |  GA   
` gkehub.googleapis.com/Namespace ` |  GA   
` gkehub.googleapis.com/RBACRoleBinding ` |  GA   
` gkehub.googleapis.com/Scope ` |  GA   
GKE on AWS  |  ` [ gkemulticloud.googleapis.com/AwsCluster ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/setup-custom-constraints) ` |  GA   
` [ gkemulticloud.googleapis.com/AwsNodePool ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/setup-custom-constraints) ` |  GA   
GKE on Azure  |  ` [ gkemulticloud.googleapis.com/AzureClient ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/setup-custom-constraints) ` |  GA   
` [ gkemulticloud.googleapis.com/AzureCluster ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/setup-custom-constraints) ` |  GA   
` [ gkemulticloud.googleapis.com/AzureNodePool ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/setup-custom-constraints) ` |  GA   
GKE On-Prem API  |  ` [ gkeonprem.googleapis.com/BareMetalAdminCluster ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/custom-constraints) ` |  GA   
` [ gkeonprem.googleapis.com/BareMetalCluster ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/custom-constraints) ` |  GA   
` [ gkeonprem.googleapis.com/BareMetalNodePool ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/custom-constraints) ` |  GA   
` [ gkeonprem.googleapis.com/VmwareAdminCluster ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/custom-constraints) ` |  GA   
` [ gkeonprem.googleapis.com/VmwareCluster ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/custom-constraints) ` |  GA   
` [ gkeonprem.googleapis.com/VmwareNodePool ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/custom-constraints) ` |  GA   
Google Cloud Armor  |  ` [ compute.googleapis.com/NetworkEdgeSecurityService ](https://docs.cloud.google.com/armor/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/SecurityPolicy ](https://docs.cloud.google.com/armor/docs/custom-constraints) ` |  GA   
Google Cloud Contact Center as a Service  |  ` [ contactcenteraiplatform.googleapis.com/ContactCenter ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaip-custom-constraints) ` |  Preview   
Google Cloud Managed Service for Apache Kafka  |  ` [ managedkafka.googleapis.com/Cluster ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/custom-constraints) ` |  GA   
Google Cloud NetApp Volumes  |  ` [ netapp.googleapis.com/ActiveDirectory ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/Backup ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/BackupPolicy ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/BackupVault ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/HostGroup ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/KmsConfig ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/QuotaRule ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/Replication ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/Snapshot ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/StoragePool ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
` [ netapp.googleapis.com/Volume ](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints) ` |  GA   
Google Cloud VMware Engine  |  ` [ vmwareengine.googleapis.com/Cluster ](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints) ` |  GA   
` [ vmwareengine.googleapis.com/ExternalAccessRule ](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints) ` |  GA   
` [ vmwareengine.googleapis.com/ExternalAddress ](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints) ` |  GA   
` [ vmwareengine.googleapis.com/NetworkPeering ](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints) ` |  GA   
` [ vmwareengine.googleapis.com/NetworkPolicy ](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints) ` |  GA   
` [ vmwareengine.googleapis.com/PrivateCloud ](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints) ` |  GA   
` [ vmwareengine.googleapis.com/PrivateConnection ](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints) ` |  GA   
` [ vmwareengine.googleapis.com/VmwareEngineNetwork ](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints) ` |  GA   
Identity and Access Management  |  ` [ iam.googleapis.com/AllowPolicy ](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints) ` |  GA   
` [ iam.googleapis.com/ServiceAccount ](https://docs.cloud.google.com/iam/docs/service-accounts-custom-constraints) ` |  GA   
` [ iam.googleapis.com/ServiceAccountKey ](https://docs.cloud.google.com/iam/docs/service-accounts-custom-constraints) ` |  GA   
` [ iam.googleapis.com/WorkloadIdentityPool ](https://docs.cloud.google.com/iam/docs/workload-identity-federation-custom-constraints) ` |  GA   
` [ iam.googleapis.com/WorkloadIdentityPoolManagedIdentity ](https://docs.cloud.google.com/iam/docs/managed-workload-identity-custom-constraints) ` |  Preview   
` [ iam.googleapis.com/WorkloadIdentityPoolNamespace ](https://docs.cloud.google.com/iam/docs/managed-workload-identity-custom-constraints) ` |  Preview   
` [ iam.googleapis.com/WorkloadIdentityPoolProvider ](https://docs.cloud.google.com/iam/docs/workload-identity-federation-custom-constraints) ` |  GA   
` [ iam.googleapis.com/WorkloadIdentityPoolProviderKey ](https://docs.cloud.google.com/iam/docs/workload-identity-federation-custom-constraints) ` |  GA   
Identity Platform  |  ` [ identitytoolkit.googleapis.com/Config ](https://docs.cloud.google.com/identity-platform/docs/admin/org-policy-custom-constraints) ` |  GA   
` [ identitytoolkit.googleapis.com/DefaultSupportedIdpConfig ](https://docs.cloud.google.com/identity-platform/docs/admin/org-policy-custom-constraints) ` |  GA   
` [ identitytoolkit.googleapis.com/InboundSamlConfig ](https://docs.cloud.google.com/identity-platform/docs/admin/org-policy-custom-constraints) ` |  GA   
` [ identitytoolkit.googleapis.com/OauthIdpConfig ](https://docs.cloud.google.com/identity-platform/docs/admin/org-policy-custom-constraints) ` |  GA   
` [ identitytoolkit.googleapis.com/Tenant ](https://docs.cloud.google.com/identity-platform/docs/admin/org-policy-custom-constraints) ` |  GA   
Identity-Aware Proxy  |  ` [ iap.googleapis.com/TunnelDestGroup ](https://docs.cloud.google.com/iap/docs/custom-org-policies) ` |  GA   
Infrastructure Manager  |  ` [ config.googleapis.com/Deployment ](https://docs.cloud.google.com/infrastructure-manager/docs/custom-constraints) ` |  GA   
` [ config.googleapis.com/Preview ](https://docs.cloud.google.com/infrastructure-manager/docs/custom-constraints) ` |  GA   
Integration Connectors  |  ` [ connectors.googleapis.com/Connection ](https://docs.cloud.google.com/integration-connectors/docs/custom-constraints) ` |  GA   
` [ connectors.googleapis.com/EndpointAttachment ](https://docs.cloud.google.com/integration-connectors/docs/custom-constraints) ` |  GA   
` [ connectors.googleapis.com/EventSubscription ](https://docs.cloud.google.com/integration-connectors/docs/custom-constraints) ` |  GA   
` [ connectors.googleapis.com/ManagedZone ](https://docs.cloud.google.com/connectors/docs/custom-constraints) ` |  GA   
` [ connectors.googleapis.com/RegionalSettings ](https://docs.cloud.google.com/connectors/docs/custom-constraints) ` |  GA   
Knowledge Catalog  |  ` [ dataplex.googleapis.com/AspectType ](https://docs.cloud.google.com/dataplex/docs/dataplex-custom-constraints) ` |  GA   
` [ dataplex.googleapis.com/DataScan ](https://docs.cloud.google.com/dataplex/docs/dataplex-custom-constraints) ` |  GA   
` [ dataplex.googleapis.com/EntryGroup ](https://docs.cloud.google.com/dataplex/docs/dataplex-custom-constraints) ` |  GA   
` [ dataplex.googleapis.com/EntryType ](https://docs.cloud.google.com/dataplex/docs/dataplex-custom-constraints) ` |  GA   
` [ dataplex.googleapis.com/MetadataJob ](https://docs.cloud.google.com/dataplex/docs/dataplex-custom-constraints) ` |  GA   
Live Stream API  |  ` [ livestream.googleapis.com/Asset ](https://docs.cloud.google.com/livestream/docs/custom-constraints) ` |  GA   
` [ livestream.googleapis.com/Channel ](https://docs.cloud.google.com/livestream/docs/custom-constraints) ` |  GA   
` [ livestream.googleapis.com/Input ](https://docs.cloud.google.com/livestream/docs/custom-constraints) ` |  GA   
Managed Service for Apache Airflow  |  ` [ composer.googleapis.com/Environment ](https://docs.cloud.google.com/composer/docs/latest/create-custom-constraints) ` |  GA   
Managed Service for Apache Kafka  |  ` [ managedkafka.googleapis.com/ConnectCluster ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/custom-constraints) ` |  GA   
Managed Service for Apache Spark  |  ` [ dataproc.googleapis.com/Batch ](https://docs.cloud.google.com/dataproc-serverless/docs/guides/dataproc-serverless-custom-constraints) ` |  GA   
` [ dataproc.googleapis.com/Cluster ](https://docs.cloud.google.com/dataproc/docs/concepts/dataproc-custom-constraints) ` |  GA   
` [ dataproc.googleapis.com/Session ](https://docs.cloud.google.com/dataproc-serverless/docs/guides/dataproc-serverless-custom-constraints) ` |  GA   
` [ dataproc.googleapis.com/SessionTemplate ](https://docs.cloud.google.com/dataproc-serverless/docs/guides/dataproc-serverless-custom-constraints) ` |  Preview   
Memorystore  |  ` [ redis.googleapis.com/Instance ](https://docs.cloud.google.com/memorystore/docs/redis/custom-constraints) ` |  GA   
Memorystore for Redis Cluster  |  ` [ redis.googleapis.com/Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster/custom-constraints) ` |  GA   
Network Connectivity  |  ` [ networkconnectivity.googleapis.com/Group ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/org-policy-constraints) ` |  GA   
` [ networkconnectivity.googleapis.com/Hub ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/org-policy-constraints) ` |  GA   
` [ networkconnectivity.googleapis.com/InternalRange ](https://docs.cloud.google.com/vpc/docs/custom-constraints) ` |  GA   
` [ networkconnectivity.googleapis.com/RegionalEndpoint ](https://docs.cloud.google.com/vpc/docs/custom-constraints) ` |  GA   
` [ networkconnectivity.googleapis.com/Spoke ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/org-policy-constraints) ` |  GA   
Private Service Connect  |  ` [ compute.googleapis.com/NetworkAttachment ](https://docs.cloud.google.com/compute/docs/access/custom-constraints) ` |  GA   
` [ compute.googleapis.com/ServiceAttachment ](https://docs.cloud.google.com/compute/docs/access/custom-constraints) ` |  GA   
Privileged Access Manager  |  ` [ privilegedaccessmanager.googleapis.com/Entitlement ](https://docs.cloud.google.com/iam/docs/pam-custom-constraints) ` |  Preview   
` [ privilegedaccessmanager.googleapis.com/Grant ](https://docs.cloud.google.com/iam/docs/pam-custom-constraints) ` |  Preview   
Pub/Sub  |  ` [ pubsub.googleapis.com/Schema ](https://docs.cloud.google.com/pubsub/docs/custom-constraints) ` |  GA   
` [ pubsub.googleapis.com/Snapshot ](https://docs.cloud.google.com/pubsub/docs/custom-constraints) ` |  GA   
` [ pubsub.googleapis.com/Subscription ](https://docs.cloud.google.com/pubsub/docs/custom-constraints) ` |  GA   
` [ pubsub.googleapis.com/Topic ](https://docs.cloud.google.com/pubsub/docs/custom-constraints) ` |  GA   
reCAPTCHA  |  ` [ recaptchaenterprise.googleapis.com/FirewallPolicy ](https://docs.cloud.google.com/recaptcha/docs/custom-constraints) ` |  GA   
` [ recaptchaenterprise.googleapis.com/Key ](https://docs.cloud.google.com/recaptcha/docs/custom-constraints) ` |  GA   
Resource Manager  |  ` [ cloudresourcemanager.googleapis.com/Folder ](https://docs.cloud.google.com/resource-manager/docs/custom-constraints) ` |  Preview   
` [ cloudresourcemanager.googleapis.com/Project ](https://docs.cloud.google.com/resource-manager/docs/custom-constraints) ` |  Preview   
Secret Manager  |  ` [ secretmanager.googleapis.com/Secret ](https://docs.cloud.google.com/secret-manager/docs/secret-manager-custom-constraints) ` |  GA   
Secure Source Manager  |  ` [ securesourcemanager.googleapis.com/Instance ](https://docs.cloud.google.com/secure-source-manager/docs/custom-constraints) ` |  GA   
Security Command Center  |  ` [ securitycenter.googleapis.com/BigQueryExport ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycenter.googleapis.com/ContainerThreatDetectionSettings ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycenter.googleapis.com/EventThreatDetectionSettings ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycenter.googleapis.com/MuteConfig ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycenter.googleapis.com/NotificationConfig ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycenter.googleapis.com/ResourceValueConfig ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycenter.googleapis.com/SecurityHealthAnalyticsSettings ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycenter.googleapis.com/VirtualMachineThreatDetectionSettings ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycenter.googleapis.com/WebSecurityScannerSettings ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycentermanagement.googleapis.com/EventThreatDetectionCustomModule ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycentermanagement.googleapis.com/SecurityCenterService ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
` [ securitycentermanagement.googleapis.com/SecurityHealthAnalyticsCustomModule ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
security posture  |  ` [ securityposture.googleapis.com/Posture ](https://docs.cloud.google.com/security-command-center/docs/security-posture-custom-constraints) ` |  GA   
` [ securityposture.googleapis.com/PostureDeployment ](https://docs.cloud.google.com/security-command-center/docs/security-posture-custom-constraints) ` |  GA   
Serverless VPC Access  |  ` [ vpcaccess.googleapis.com/Connector ](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#custom-constraints) ` |  GA   
Service Extensions  |  ` [ networkservices.googleapis.com/LbRouteExtension ](https://docs.cloud.google.com/service-extensions/docs/custom-constraints) ` |  GA   
` [ networkservices.googleapis.com/LbTrafficExtension ](https://docs.cloud.google.com/service-extensions/docs/custom-constraints) ` |  GA   
Service Management  |  ` [ servicemanagement.googleapis.com/Service ](https://docs.cloud.google.com/service-infrastructure/docs/service-management/custom-constraints) ` |  Preview   
Service Networking  |  ` [ servicenetworking.googleapis.com/Connection ](https://docs.cloud.google.com/vpc/docs/custom-constraints) ` |  GA   
Spanner  |  ` [ spanner.googleapis.com/Backup ](https://docs.cloud.google.com/spanner/docs/spanner-custom-constraints) ` |  GA   
` [ spanner.googleapis.com/Database ](https://docs.cloud.google.com/spanner/docs/spanner-custom-constraints) ` |  GA   
` [ spanner.googleapis.com/Instance ](https://docs.cloud.google.com/spanner/docs/spanner-custom-constraints) ` |  GA   
` [ spanner.googleapis.com/InstanceConfig ](https://docs.cloud.google.com/spanner/docs/spanner-custom-constraints) ` |  GA   
Storage Transfer Service  |  ` [ storagetransfer.googleapis.com/TransferJob ](https://docs.cloud.google.com/storage-transfer/docs/custom-constraints) ` |  GA   
Vector Search  |  ` [ aiplatform.googleapis.com/Index ](https://docs.cloud.google.com/vertex-ai/docs/vector-search/custom-constraints) ` |  GA   
` [ aiplatform.googleapis.com/IndexEndpoint ](https://docs.cloud.google.com/vertex-ai/docs/vector-search/custom-constraints) ` |  GA   
Vertex AI  |  ` [ aiplatform.googleapis.com/DeploymentResourcePool ](https://docs.cloud.google.com/vertex-ai/docs/predictions/custom-constraints) ` |  Preview   
` [ aiplatform.googleapis.com/Endpoint ](https://docs.cloud.google.com/vertex-ai/docs/predictions/custom-constraints) ` |  Preview   
Vertex AI Pipelines  |  ` [ aiplatform.googleapis.com/PipelineJob ](https://docs.cloud.google.com/vertex-ai/docs/pipelines/use-custom-constraints) ` |  Preview   
Vertex ML Metadata  |  ` [ aiplatform.googleapis.com/MetadataStore ](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/use-custom-constraints) ` |  GA   
Video Stitcher API  |  ` [ videostitcher.googleapis.com/CdnKey ](https://docs.cloud.google.com/video-stitcher/docs/how-to/create-custom-constraints) ` |  GA   
` [ videostitcher.googleapis.com/LiveConfig ](https://docs.cloud.google.com/video-stitcher/docs/how-to/create-custom-constraints) ` |  GA   
` [ videostitcher.googleapis.com/Slate ](https://docs.cloud.google.com/video-stitcher/docs/how-to/create-custom-constraints) ` |  GA   
` [ videostitcher.googleapis.com/VodConfig ](https://docs.cloud.google.com/video-stitcher/docs/how-to/create-custom-constraints) ` |  GA   
Virtual Private Cloud  |  ` [ compute.googleapis.com/Address ](https://docs.cloud.google.com/vpc/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/Network ](https://docs.cloud.google.com/vpc/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/PacketMirroring ](https://docs.cloud.google.com/vpc/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/Route ](https://docs.cloud.google.com/vpc/docs/custom-constraints) ` |  GA   
` [ compute.googleapis.com/Subnetwork ](https://docs.cloud.google.com/vpc/docs/custom-constraints) ` |  GA   
Web Security Scanner  |  ` [ websecurityscanner.googleapis.com/ScanConfig ](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints) ` |  GA   
Workflows  |  ` [ workflows.googleapis.com/Workflow ](https://docs.cloud.google.com/workflows/docs/custom-constraints) ` |  GA   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
