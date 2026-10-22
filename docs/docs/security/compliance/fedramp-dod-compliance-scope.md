---
url: https://docs.cloud.google.com/docs/security/compliance/fedramp-dod-compliance-scope/
title: FedRAMP and DoD compliance scope for Google Cloud and Google Workspace \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:49.799363+00:00
---

# FedRAMP and DoD compliance scope for Google Cloud and Google Workspace  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/fedramp-dod-compliance-scope/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  FedRAMP and DoD compliance scope for Google Cloud and Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-21 UTC

[Google Cloud](https://cloud.google.com/why-google-cloud) and [ Google Workspace](https://workspace.google.com/) services meet demanding US government compliance requirements that are verified through formal third-party authorizations, including the following:

  * [Federal Risk and Authorization Management Program (FedRAMP)](https://www.fedramp.gov/) High provisional authorization to operate (P-ATO).
  * Department of Defense (DoD) Cloud Computing [Security Requirements Guide (SRG)](https://www.cyber.mil/dccs/dccs-documents/) Impact Level 2 (IL2) and Impact Level 4 (IL4) provisional authorizations (PA) issued by the Defense Information Systems Agency (DISA).
  * Moreover, Google Cloud also maintains a DoD IL5 PA issued by DISA.



For more information, see the Google [FedRAMP](https://cloud.google.com/security/compliance/fedramp) and [DoD](https://cloud.google.com/security/compliance/disa) compliance offerings pages.

This document provides a detailed list of Google Cloud and Google Workspace services in scope for FedRAMP High, DoD IL2, DoD IL4, and DoD IL5 provisional authorizations. You can use all Google Cloud and Google Workspace services that are FedRAMP High authorized for FedRAMP Moderate deployments.

This document also tracks the Google Cloud regions that are suitable for FedRAMP Moderate, FedRAMP High, DoD IL2, DoD IL4, and DoD IL5 deployments.

## Terminology

This document uses the following terminology:

  * **FedRAMP High** : FedRAMP High P-ATO
  * **FedRAMP Moderate** : FedRAMP Moderate deployment for a cloud region based on inheritance from a FedRAMP High P-ATO
  * **DoD IL2** : DoD SRG Impact Level 2 PA
  * **DoD IL4** : DoD SRG Impact Level 4 PA
  * **DoD IL5** : DoD SRG Impact Level 5 PA
  * **GSA review** : Service was submitted for FedRAMP authorization and is waiting for GSA approval
  * **DISA review** : Service was submitted for DoD authorization and is waiting for DISA approval
  * : Service or cloud region is authorized



## Google Cloud services by audit scope

_Last updated: October 2026_

Google's authorization strategy focuses on the top-level cloud services.

A component service or feature of an authorized top-level cloud service might not be authorized yet, in which case it's explicitly excluded from the authorization scope. Conversely, a commonly used feature of an authorized cloud service might be explicitly called out as authorized for emphasis and to proactively address questions about the authorization status for commonly used Google Cloud services. You can use all Google Cloud services that are FedRAMP High authorized for FedRAMP Moderate deployments.

This document also tracks changes to authorization status resulting from service rebranding, restructuring, and deprecation. Typically, authorization status is no longer tracked for deprecated services that are shut down and unavailable for provisioning.

**Note:** [Only Google models that support US multi-regional endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency#ml-processing-google-models), including most Generally Available Gemini models, offer data residency (DRZ) commitments and can support FedRAMP High and DoD IL4 and IL5 requirements without requiring you to configure additional settings. For more information, see [Google model support](https://docs.cloud.google.com/docs/security/compliance/deploy-gemini-gov#model_support).

  
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
---|---|---|---|---  
[Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) |  |  |  |   
[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) |  |  |  |   
[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) |  |  | DISA review | DISA review  
[Agent Assist](https://cloud.google.com/agent-assist) |  |  |  |   
[Agent Search on Gemini Enterprise Agent Platform](https://cloud.google.com/enterprise-search) (formerly Vertex AI Search) |  |  |  |   
[AlloyDB](https://cloud.google.com/products/alloydb) |  |  |  |   
[API keys](https://docs.cloud.google.com/api-keys/docs/overview) | GSA review |  |  |   
[Apigee](https://cloud.google.com/apigee) |  |  | DISA review | DISA review  
[App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard) (excluding bundled services) |  |  |  |   
[App Hub](https://cloud.google.com/products/app-hub) |  |  | DISA review | DISA review  
[Application Integration](https://docs.cloud.google.com/application-integration/docs/overview) |  |  |  |   
[Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) |  |  | DISA review | DISA review  
[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) (replaced [Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr)) |  |  |  |   
[ Assured Open Source Software (Assured OSS)](https://cloud.google.com/security/products/assured-open-source-software) |  |  |  |   
[ Audit Manager](https://cloud.google.com/products/audit-manager) |  |  | DISA review | DISA review  
[Backup and DR Service](https://cloud.google.com/backup-disaster-recovery) |  |  | DISA review | DISA review  
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Batch](https://cloud.google.com/batch) |  |  |  |   
[BigQuery](https://cloud.google.com/bigquery) (excluding [BigLake](https://docs.cloud.google.com/bigquery/docs/biglake-intro) and [BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction)) |  |  |  |   
[BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) |  |  | DISA review | DISA review  
[Bigtable](https://cloud.google.com/bigtable) |  |  | DISA review | DISA review  
[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) |  |  | DISA review | DISA review  
[Certificate Authority Service](https://cloud.google.com/security/products/certificate-authority-service) |  |  |  |   
[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) |  |  | DISA review | DISA review  
[Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs) |  |  | DISA review | DISA review  
[Cloud Billing](https://docs.cloud.google.com/billing/docs/concepts) |  |  |  |   
[Cloud Build](https://docs.cloud.google.com/build/docs/overview) |  |  |  |   
[Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) |  |  |  |   
[Cloud Data Fusion](https://cloud.google.com/data-fusion) |  |  |  |   
[Cloud Deploy](https://cloud.google.com/deploy) |  |  | DISA review | DISA review  
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs) (replaced by [Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/overview)) |  |  |  |   
[Cloud DNS](https://cloud.google.com/dns) |  |  |  |   
[Cloud Domains](https://docs.cloud.google.com/domains/docs/overview) |  |  |  |   
[Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs) |  |  |  |   
[Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) |  |  |  |   
[Cloud Functions for Firebase](https://firebase.google.com/docs/functions) |  |  |  |   
[Cloud Healthcare API](https://cloud.google.com/healthcare-api) |  |  |  |   
[Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) |  |  |  |   
[Cloud Identity](https://cloud.google.com/identity) |  |  |  |   
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) |  |  |  |   
[Cloud Intrusion Detection System (Cloud IDS)](https://cloud.google.com/security/products/intrusion-detection-system) |  |  |  |   
[Cloud Key Management Service (Cloud KMS)](https://cloud.google.com/security/products/security-key-management) |  |  |  |   
[Cloud Life Sciences](https://cloud.google.com/life-sciences-solutions) (formerly Google Genomics) |  |  |  |   
[Cloud Load Balancing: Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) |  |  |  |   
[External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) (regional) |  |  |  |   
[Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) (regional) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Cloud Load Balancing: Passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) |  |  |  |   
[Regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service) |  |  |  |   
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) |  |  |  |   
[Cloud Load Balancing: Proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer) |  |  |  |   
[External proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp) (regional) |  |  |  |   
[Internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) (regional) |  |  |  |   
[Cloud Logging](https://cloud.google.com/logging) |  |  |  |   
[Cloud Monitoring](https://cloud.google.com/monitoring) |  |  |  |   
[Cloud NAT](https://cloud.google.com/nat) |  |  |  |   
[Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs) |  |  |  |   
[ Cloud Next Generation Firewall (Cloud NGFW)](https://cloud.google.com/security/products/firewall) |  |  |  |   
[Cloud Next Generation Firewall Essentials](https://docs.cloud.google.com/firewall/docs/about-firewalls#ngfw-tiers) |  |  |  |   
[Cloud Next Generation Firewall Standard](https://docs.cloud.google.com/firewall/docs/about-firewalls#ngfw-tiers) |  |  |  |   
[Cloud Next Generation Firewall Enterprise](https://docs.cloud.google.com/firewall/docs/about-firewalls#ngfw-tiers) |  |  |  |   
[Cloud Profiler](https://docs.cloud.google.com/profiler/docs/about-profiler) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Cloud Quotas](https://docs.cloud.google.com/docs/quotas/overview) |  |  |  |   
[Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) |  |  |  |   
[Cloud Run](https://cloud.google.com/run) |  |  |  |   
[Cloud Run functions](https://docs.cloud.google.com/run/docs/functions/overview) (formerly Cloud Functions) |  |  |  |   
[Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview) (formerly Cloud Run for Anthos) |  |  |  |   
[Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) (replaced [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access)) |  |  |  |   
[Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) |  |  |  |   
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) (formerly Anthos Service Mesh) |  |  |  |   
[Traffic Director API](https://cloud.google.com/blog/topics/developers-practitioners/traffic-director-explained) |  |  |  |   
[Cloud Shell](https://cloud.google.com/shell/docs) |  |  |  |   
[Cloud SQL](https://cloud.google.com/sql) |  |  |  |   
[Cloud SQL for MySQL](https://cloud.google.com/sql/mysql) |  |  |  |   
[Cloud SQL for PostgreSQL](https://cloud.google.com/sql/postgresql) |  |  |  |   
[Cloud SQL for SQL Server](https://cloud.google.com/sql/sqlserver) |  |  |  |   
[Cloud Storage](https://cloud.google.com/storage) |  |  |  |   
[Cloud Storage for Firebase](https://firebase.google.com/docs/storage) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Cloud Tasks](https://docs.cloud.google.com/tasks/docs/dual-overview) |  |  |  |   
[Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) |  |  |  |   
[Cloud Translation API](https://cloud.google.com/translate) |  |  |  |   
[Cloud Vision API](https://docs.cloud.google.com/vision/docs) |  |  |  |   
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  |  |  |   
[Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) |  |  |  |   
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview) |  |  |  |   
[Compute Engine: OS Login](https://docs.cloud.google.com/compute/docs/oslogin) |  |  | DISA review | DISA review  
[Compute Engine: VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) |  |  | DISA review | DISA review  
[ Customer Experience Insights](https://cloud.google.com/solutions/ccai-insights) (formerly CCAI Insights) |  |  |  |   
[Database Center](https://docs.cloud.google.com/database-center/docs/overview) |  |  | DISA review | DISA review  
[Database Migration Service](https://cloud.google.com/database-migration) |  |  |  |   
[Dataflow](https://cloud.google.com/products/dataflow) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Dataform](https://cloud.google.com/dataform) |  |  | DISA review | DISA review  
[Datastream](https://docs.cloud.google.com/datastream/docs/overview) |  |  |  |   
[Data Studio](https://docs.cloud.google.com/data-studio) (formerly Google Data Studio) |  |  |  |   
[Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro) |  |  |  |   
[Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs) |  |  |  |   
[Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs) |  |  |  |   
[Document AI](https://cloud.google.com/document-ai) |  |  |  |   
[Error Reporting](https://docs.cloud.google.com/error-reporting/docs) |  |  |  |   
[Eventarc](https://docs.cloud.google.com/eventarc/docs) (excluding [Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/overview)) |  |  |  |   
[Eventarc Standard](https://docs.cloud.google.com/eventarc/standard/docs/overview) |  |  |  |   
[Filestore](https://cloud.google.com/filestore) |  |  |  |   
[Filestore Basic HDD tier](https://docs.cloud.google.com/filestore/docs/service-tiers) |  |  |  |   
[Filestore Basic SSD tier](https://docs.cloud.google.com/filestore/docs/service-tiers) |  |  |  |   
[Firebase Authentication](https://firebase.google.com/docs/auth) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Firebase Security Rules](https://firebase.google.com/docs/rules) |  |  | DISA review | DISA review  
[Firestore](https://firebase.google.com/docs/firestore) (replaced [Datastore](https://docs.cloud.google.com/datastore/docs); excluding Firestore with MongoDB compatibility) |  |  | DISA review | DISA review  
[Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs) (formerly Google Agentspace; for a full list of exclusions, see [Deployment guidance for Gemini for Government](https://docs.cloud.google.com/docs/security/compliance/deploy-gemini-gov)) |  |  |  |   
[Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview) (excludes Audio Overview, Infographic, Slide Deck, and Video Overview) |  |  | DISA review |   
[Gemini Enterprise Agent Platform Inference: Batch and Online](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/overview) (formerly Vertex AI Inference, also known as Vertex Online and Batch Prediction) |  |  |  |   
[Gemini Enterprise Agent Platform Managed Training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview) (formerly Vertex AI Training) |  |  |  |   
[Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) (formerly Vertex AI Pipelines) |  |  |  |   
[Gemini Enterprise Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction) (formerly Vertex AI Workbench) |  |  |  |   
[Generative AI on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook) (formerly Generative AI on Vertex AI) |  |  |  |   
[Gemini Enterprise Agent Platform Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models) (formerly Vertex AI Tuning) |  |  | DISA review | DISA review  
[Google Admin console](https://support.google.com/a/topic/2413312) |  |  |  |   
[Google Admin console: Admin SDK](https://developers.google.com/workspace/admin/reference-overview) |  |  |  |   
[Google Admin console: Directory Sync](https://knowledge.workspace.google.com/business-continuity/directory-sync/get-started-with-directory-sync) |  |  |  |   
[Google Cloud app](https://cloud.google.com/app) |  |  |  |   
[Google Cloud Armor](https://cloud.google.com/security/products/armor) |  |  |  |   
[Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview) (excluding [Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview) and [Kafka Schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview)) |  |  | DISA review | DISA review  
[Google Cloud Marketplace](https://cloud.google.com/marketplace) |  |  |  |   
[Google Cloud Migration Center](https://docs.cloud.google.com/migration-center/docs/migration-center-overview) |  |  |  |   
[Google Cloud SDK](https://cloud.google.com/sdk) |  |  |  |   
[Google Earth Engine](https://cloud.google.com/earth-engine) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine) |  |  |  |   
[Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) |  |  | DISA review | DISA review  
[GKE Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) |  |  |  |   
[GKE Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent) |  |  |  |   
[GKE connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway) |  |  |  |   
[GKE Hub](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest) |  |  |  |   
[GKE Identity Service](https://cloud.google.com/kubernetes-engine/enterprise/identity) (formerly Anthos Identity Service) |  |  |  |   
[GKE Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) |  |  |  |   
[Google Security Operations SIEM (Google SecOps SIEM)](https://docs.cloud.google.com/chronicle/docs/overview) |  |  |  |   
[ Google Security Operations SOAR (Google SecOps SOAR)](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-overview) |  |  |  |   
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) |  |  |  |   
[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) |  |  |  |   
[Identity Platform](https://cloud.google.com/security/products/identity-platform) |  |  |  |   
[Identity-Aware Proxy (IAP)](https://cloud.google.com/security/products/iap) |  |  |  |   
[IAP for TCP](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) |  |  |  |   
[Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/overview) |  |  | DISA review | DISA review  
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview) |  |  | DISA review | DISA review  
[Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) |  |  | DISA review | DISA review  
[Knowledge Catalog](https://cloud.google.com/dataplex) (formerly Dataplex Universal Catalog; replaced [Data Catalog](https://docs.cloud.google.com/data-catalog/docs/concepts/overview)) |  |  |  |   
[Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) |  |  | DISA review | DISA review  
[Managed Service for Apache Airflow](https://cloud.google.com/composer) (formerly Cloud Composer) |  |  |  |   
[Managed Service for Apache Spark](https://cloud.google.com/dataproc) |  |  |  |   
[Memorystore](https://cloud.google.com/memorystore) |  |  | DISA review | DISA review  
[Memorystore for Memcached](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview) |  |  |  |   
[Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview) |  |  |  |   
[Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster) |  |  | DISA review | DISA review  
[Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview) |  |  | DISA review | DISA review  
[Metadata on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/introduction) (formerly Vertex ML Metadata) |  |  |  |   
[Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0) |  |  |  |   
[Model Armor](https://cloud.google.com/security/products/model-armor) |  |  | DISA review | DISA review  
[Model Monitoring on Gemini Enterprise Agent Platform (v1)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) (formerly Vertex AI Model Monitoring) |  |  |  |   
[Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction) (formerly Vertex AI Model Registry) |  |  |  |   
[Neural Architecture Search on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/neural-architecture-search/overview) (formerly Vertex AI Neural Architecture Search) |  |  |  |   
[Network Connectivity Center](https://cloud.google.com/network-connectivity-center) |  |  |  |   
[Network Intelligence Center](https://cloud.google.com/network-intelligence-center) |  |  |  |   
[ Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview) |  |  |  |   
[ Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview) |  |  |  |   
[Network Service Tiers](https://cloud.google.com/network-tiers/docs) |  |  |  |   
[Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview) |  |  | DISA review | DISA review  
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview) |  |  |  |   
[Persistent Disk](https://cloud.google.com/persistent-disk) |  |  |  |   
[Pub/Sub](https://cloud.google.com/pubsub) |  |  |  |   
[reCAPTCHA Enterprise](https://docs.cloud.google.com/recaptcha/docs) |  |  |  |   
[Resource Manager](https://docs.cloud.google.com/resource-manager/docs) |  |  | DISA review | DISA review  
[Recommender](https://docs.cloud.google.com/recommender/docs) |  |  |  |   
[Secret Manager](https://cloud.google.com/security/products/secret-manager) (excluding [Global secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/global-regionalized-service-comparison)) |  |  |  |   
[Secret Manager: Regional secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/data-residency) |  |  |  |   
[Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview) (replaced [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs)) |  |  | DISA review | DISA review  
[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) |  |  |  |   
[Security Command Center](https://cloud.google.com/security/products/security-command-center) (excluding [Enterprise)](https://docs.cloud.google.com/security-command-center/docs/service-tiers) |  |  | DISA review | DISA review  
[Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (excluding [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview)) |  |  |  |   
[Security Graph](https://docs.cloud.google.com/security-command-center/docs/predefined-security-graph-rules) |  |  |  |   
[ Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection) (formerly Cloud DLP) |  |  |  |   
[Cloud Data Loss Prevention API](https://cloud.google.com/security/products/dlp) |  |  |  |   
[Service Directory](https://docs.cloud.google.com/service-directory/docs) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Spanner](https://cloud.google.com/spanner) |  |  |  |   
[Speech-to-Text](https://cloud.google.com/speech-to-text) |  |  |  |   
[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) |  |  | DISA review | DISA review  
[Tabular Workflows on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/tabular-workflows/overview) (formerly Vertex AI Tabular Workflows) |  |  |  |   
[Talent Solution](https://cloud.google.com/solutions/talent-solution) |  |  |  |   
[Text-to-Speech](https://cloud.google.com/text-to-speech) |  |  |  |   
[Vector Search on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview) (formerly Vertex AI Vector Search) |  |  | DISA review | DISA review  
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Video Intelligence API](https://docs.cloud.google.com/video-intelligence/docs) |  |  |  |   
[Virtual Private Cloud (VPC)](https://cloud.google.com/vpc) |  |  |  |   
[Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) |  |  |  |   
[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) |  |  |  |   
[Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) |  |  |  |   
[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) |  |  |  |   
[VPC Service Controls](https://cloud.google.com/security/vpc-service-controls) |  |  |  |   
[Web Risk API](https://cloud.google.com/security/products/web-risk) |  |  |  |   
[Workflows](https://cloud.google.com/workflows) |  |  |  |   
[Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview) |  |  |  |   
  
## Google Workspace services by audit scope

_Last updated: January 2026_

To comply with FedRAMP High and DoD IL4 requirements, you must use one of the following Google Workspace editions:

  * [Google Workspace Enterprise Plus](https://workspace.google.com/pricing.html)
  * [Frontline Plus](https://knowledge.workspace.google.com/admin/getting-started/editions/frontline-editions#frontline_plus)
  * [Business Continuity](https://knowledge.workspace.google.com/business-continuity/overview)
  * [Business Continuity Plus](https://knowledge.workspace.google.com/business-continuity/overview)



Note that not all services that are available within these editions are FedRAMP or IL authorized. To configure your domains to support your FedRAMP High or IL4 compliance requirements, follow the [Google Workspace FedRAMP configuration guide](https://knowledge.workspace.google.com/admin/compliance/google-workspace-fedramp-configuration-guide) or [Google Workspace IL4 configuration guide](https://knowledge.workspace.google.com/admin/compliance/google-workspace-il4-configuration-guide).

  
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
---|---|---|---|---  
[AppSheet](https://about.appsheet.com/home/) (excluding [Tables](https://support.google.com/appsheet/answer/10105821)) |  |  |  |   
[Contacts](https://support.google.com/a/users/answer/9310345) |  |  |  |   
[Drawings](https://support.google.com/docs/answer/179740) |  |  | DISA review |   
[Gemini app](https://support.google.com/a/answer/14571493#what) |  |  |  |   
[Gmail](https://workspace.google.com/products/gmail/) |  |  |  | DISA review  
[ Google Admin console: Admin SDK](https://developers.google.com/workspace/admin/reference-overview) (including Admin Settings API, Apps Email Audit API, Calendar Resource API, Directory API (which replaced Provisioning API), Domain Shared Contacts API, Email Settings API, Enterprise License Manager API, Groups Migration API, Groups Settings API, Reports API, and Reseller API) |  |  |  |   
[ Google Admin console: Android and Chrome device management](https://support.google.com/chrome/a/answer/9490493) |  |  |  |   
[Google Calendar](https://workspace.google.com/products/calendar/) |  |  |  | DISA review  
[Google Chat](https://workspace.google.com/products/chat/) |  |  |  |   
[ Google Chrome sync](https://support.google.com/chrome/a/answer/6309115) (Google Workspace for Education domains only) |  |  |  |   
[Google Classroom](https://edu.google.com/intl/ALL_us/workspace-for-education/products/classroom/) |  |  |  |   
[Google Cloud Search](https://knowledge.workspace.google.com/cloud-search/what-is-google-cloud-search) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Google Docs](https://workspace.google.com/products/docs/) |  |  |  | DISA review  
[Google Drive](https://workspace.google.com/products/drive/) |  |  |  | DISA review  
[Google Forms](https://workspace.google.com/products/forms/) |  |  |  |   
[Google Keep](https://workspace.google.com/products/keep/) |  |  |  |   
[Google Meet](https://workspace.google.com/products/meet/) |  |  |  | DISA review  
[Google Meet: Live stream](https://support.google.com/meet/answer/9308630) |  |  |  |   
[Google Sheets](https://workspace.google.com/products/sheets/) |  |  |  | DISA review  
[Google Sites Classic](https://developers.google.com/workspace/sites) (replaced by Google Sites New) |  |  |  |   
[Google Sites New](https://workspace.google.com/products/sites/) |  |  | DISA review |   
[Google Slides](https://workspace.google.com/products/slides/) |  |  |  | DISA review  
[Google Tasks](https://workspace.google.com/products/tasks/) |  |  |  |   
[Google Vault](https://workspace.google.com/products/vault/) |  |  |  |   
[Google Vids](https://workspace.google.com/products/vids/) |  |  |  |   
[Google Voice](https://workspace.google.com/products/voice/) |  |  |  |   
Service | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
[Google Workspace Security Center](https://support.google.com/a/answer/7492003) (for Google Workspace Enterprise and Google Workspace Enterprise for Education domains only) |  |  |  |   
[Google Workspace with Gemini](https://support.google.com/a/answer/13623623) |  |  |  |   
[Gemini in Chat](https://support.google.com/chat/answer/15395284) |  |  |  |   
[Gemini in Docs](https://workspace.google.com/products/docs/ai/) |  |  |  |   
[Gemini in Drive](https://support.google.com/drive/answer/14217860) |  |  |  |   
[Gemini in Gmail](https://workspace.google.com/products/gmail/ai/) |  |  |  |   
[Gemini in Meet ](https://support.google.com/meet/answer/14441737) |  |  |  |   
Generative images in Meet backgrounds |  |  |  |   
Live translated captions |  |  |  |   
Studio look |  |  |  |   
[Gemini in Sheets](https://workspace.google.com/resources/spreadsheet-ai/) |  |  |  |   
[Gemini in Slides](https://workspace.google.com/resources/presentation-ai/) |  |  |  |   
[Secure LDAP](https://support.google.com/a/answer/9048516) |  |  |  |   
  
## Authorized Google Cloud regions

_Last updated: January 2026_

Google Cloud regions hold FedRAMP and Department of Defense (DoD) provisional authorizations (PAs). The suitability of these regions depends on the following security impact levels (IL):

  * For an IL2 PA, DoD grants full reciprocity with a FedRAMP Moderate or High P-ATO.
  * Only US-based cloud regions are appropriate for FedRAMP High, DoD IL2, DoD IL4, and DoD IL5 deployments.
  * You can use any US-based cloud region that's approved for FedRAMP High for FedRAMP Moderate deployments.
  * Non-US cloud regions are only suitable for FedRAMP Moderate deployments, which can rely on the FedRAMP High P-ATO.



  
Geographic area | Location | Cloud region | FedRAMP Moderate | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
---|---|---|---|---|---|---|---  
North America | Arcola, VA, USA | `us-east4` |  |  |  |  |   
| Ashburn (1), VA, USA | `us-east4` |  |  |  |  |   
| Ashburn (2), VA, USA | `us-east4` |  |  |  |  |   
| Ashburn (3), VA, USA | `us-east4` |  |  |  |  |   
| Atlanta (1), GA, USA | Not applicable (N/A) |  |  |  |  |   
| Atlanta (2), GA, USA | N/A |  |  |  |  |   
| Clarksville, TN, USA | `us-east6` |  |  |  |  |   
| Columbus, OH, USA | `us-east5` |  |  |  |  |   
| Council Bluffs (1), IA, USA | `us-central1` |  |  |  |  |   
| Council Bluffs (2), IA, USA | `us-central1` |  |  |  |  |   
| Henderson, NV, USA | `us-west4` |  |  |  |  |   
| Las Vegas, NV, USA | `us-west4` |  |  |  |  |   
Geographic area | Location | Cloud region | FedRAMP Moderate | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
| Lancaster, OH, USA | `us-east5` |  |  |  |  |   
| Leesburg, VA, USA | N/A |  |  |  |  |   
| Lenoir, NC, USA | N/A |  |  |  |  |   
| Los Angeles (1), CA, USA | `us-west2` |  |  |  |  |   
| Los Angeles (2), CA, USA | `us-west2` |  |  |  |  |   
| Los Angeles (3), CA, USA | `us-west2` |  |  |  |  |   
| Midlothian (Dallas), TX, USA | `us-south1` |  |  |  |  |   
| Moncks Corner, SC, USA | `us-east1` |  |  |  |  |   
| Montreal, Québec, Canada | `northamerica-northeast1` |  |  |  |  |   
| New Albany, OH, USA | `us-east5` |  |  |  |  |   
| Papillion, NE, USA | `us-central1` |  |  |  |  |   
| Phoenix, AZ, USA | `us-west8` |  |  |  |  |   
Geographic area | Location | Cloud region | FedRAMP Moderate | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
| Pryor Creek, OK, USA | `us-central2` |  |  |  |  |   
| Reno, NV, USA | N/A |  |  |  |  |   
| Salt Lake City (1), UT, USA | `us-west3` |  |  |  |  |   
| Salt Lake City (2), UT, USA | `us-west3` |  |  |  |  |   
| Salt Lake City (3), UT, USA | `us-west3` |  |  |  |  |   
| The Dalles (1), OR, USA | `us-west1` |  |  |  |  |   
| The Dalles (2), OR, USA | `us-west1` |  |  |  |  |   
| Toronto, Ontario, Canada | `northamerica-northeast2` |  |  |  |  |   
| Widows Creek, AL, USA | N/A |  |  |  |  |   
South America | Osasco, São Paulo, Brazil | `southamerica-east1` |  |  |  |  |   
| Vinhedo, São Paulo, Brazil | `southamerica-east1` |  |  |  |  |   
| Quilicura, Santiago, Chile | `southamerica-west1` |  |  |  |  |   
Geographic area | Location | Cloud region | FedRAMP Moderate | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
Europe | Eemshaven, Netherlands | `europe-west4` |  |  |  |  |   
| Frankfurt (1), Hesse, Germany | `europe-west3` |  |  |  |  |   
| Frankfurt (2), Hesse, Germany | `europe-west3` |  |  |  |  |   
| Frankfurt (3), Hesse, Germany | `europe-west3` |  |  |  |  |   
| Frankfurt (4), Hesse, Germany | `europe-west3` |  |  |  |  |   
| Frankfurt (5), Hesse, Germany | `europe-west3` |  |  |  |  |   
| Frankfurt (6), Hesse, Germany | `europe-west3` |  |  |  |  |   
| Frankfurt (7), Hesse, Germany | `europe-west3` |  |  |  |  |   
| Fredericia, Denmark | N/A |  |  |  |  |   
| Ghlin, Hainaut, Belgium | `europe-west1` |  |  |  |  |   
| Hamina, Finland | `europe-north1` |  |  |  |  |   
| London (1), United Kingdom | `europe-west2` |  |  |  |  |   
Geographic area | Location | Cloud region | FedRAMP Moderate | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
| London (2), United Kingdom | `europe-west2` |  |  |  |  |   
| London (3), United Kingdom | `europe-west2` |  |  |  |  |   
| London (4), United Kingdom | `europe-west2` |  |  |  |  |   
| London (5), United Kingdom | `europe-west2` |  |  |  |  |   
| London (6), United Kingdom | `europe-west2` |  |  |  |  |   
| Madrid (1), Spain | `europe-southwest1` |  |  |  |  |   
| Madrid (2), Spain | `europe-southwest1` |  |  |  |  |   
| Middenmeer, Netherlands | `europe-west11` |  |  |  |  |   
| Milan (1), Italy | `europe-west8` |  |  |  |  |   
| Milan (2), Italy | `europe-west8` |  |  |  |  |   
| Paris (1), France | `europe-west9` |  |  |  |  |   
| Paris (2), France | `europe-west9` |  |  |  |  |   
Geographic area | Location | Cloud region | FedRAMP Moderate | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
| Paris (3), France | `europe-west9` |  |  |  |  |   
| Warsaw (1), Poland | `europe-central2` |  |  |  |  |   
| Warsaw (2), Poland | `europe-central2` |  |  |  |  |   
| Zurich, Switzerland | `europe-west6` |  |  |  |  |   
Middle East | Doha (1), Qatar | `me-central1` |  |  |  |  |   
| Tel Aviv (1), Israel | `me-west1` |  |  |  |  |   
| Tel Aviv (2), Israel | `me-west1` |  |  |  |  |   
Asia Pacific | Changhua, Taiwan | `asia-east1` |  |  |  |  |   
| Delhi (1), India | `asia-south2` |  |  |  |  |   
| Jakarta (1), Indonesia | `asia-southeast2` |  |  |  |  |   
| Jakarta (2), Indonesia | `asia-southeast2` |  |  |  |  |   
| Kōtō-ku (1), Tokyo, Japan | `asia-northeast1` |  |  |  |  |   
Geographic area | Location | Cloud region | FedRAMP Moderate | FedRAMP High | DoD IL2 | DoD IL4 | DoD IL5  
| Kōtō-ku (2), Tokyo, Japan | `asia-northeast1` |  |  |  |  |   
| Kōtō-ku (3), Tokyo, Japan | `asia-northeast1` |  |  |  |  |   
| Lok Yang Way, Singapore | `asia-southeast1` |  |  |  |  |   
| Melbourne, Victoria, Australia | `australia-southeast2` |  |  |  |  |   
| Mumbai (1), India | `asia-south1` |  |  |  |  |   
| Mumbai (2), India | `asia-south1` |  |  |  |  |   
| Mumbai (3), India | `asia-south1` |  |  |  |  |   
| Osaka, Japan | `asia-northeast2` |  |  |  |  |   
| Seoul, South Korea | `asia-northeast3` |  |  |  |  |   
| Sydney (1), NSW, Australia | `australia-southeast1` |  |  |  |  |   
| Sydney (2), NSW, Australia | `australia-southeast1` |  |  |  |  |   
| Sydney (3), NSW, Australia | `australia-southeast1` |  |  |  |  |   
| Sydney (4), NSW, Australia | `australia-southeast1` |  |  |  |  |   
| Wenya, Singapore | `asia-southeast1` |  |  |  |  |   
  
## What's next

  * [Deployment guidance for Gemini for Government](https://docs.cloud.google.com/docs/security/compliance/deploy-gemini-gov)
  * [FedRAMP implementation guidance on Google Cloud](https://docs.cloud.google.com/docs/security/compliance/fedramp-implementation-guide)
  * [FedRAMP compliance offering](https://cloud.google.com/security/compliance/fedramp)
  * [DoD compliance offering](https://cloud.google.com/security/compliance/disa)
  * [Meet regulatory, compliance, and privacy needs](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs)
  * [Google Cloud trust center](https://cloud.google.com/trust-center)
  * [Google Cloud compliance resource center](https://cloud.google.com/compliance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
