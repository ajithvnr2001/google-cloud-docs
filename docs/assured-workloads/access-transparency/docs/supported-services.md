---
url: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services/
title: Supported services \u00a0|\u00a0 Access Transparency \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:05.992050+00:00
---

# Supported services  |  Access Transparency  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services/

The names for some Assured Workload control packages are changing. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Transparency ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported services

This page lists all the Google Cloud services that write Access Transparency logs.

_GA_ indicates that a log type is generally available for a service. _Preview_ indicates that a log type is available, but might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

If you want to enable Access Transparency logs, see [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable#enabling).

## Supported Google Cloud services

Access Transparency supports the following Google Cloud services:

Supported service | Launch stage | Notes  
---|---|---  
[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs) |  GA  |  None   
[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs) |  GA  |  None   
[Agent Assist](https://docs.cloud.google.com/agent-assist/docs) |  GA  |  None   
[Agent Identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview) |  GA  |  None   
[Agent Platform Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore) |  GA  |  None   
[Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/agent-builder/agent-engine/overview) |  GA  |  None   
[Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs) |  GA  |  Access to your data in Gemini Enterprise Agent Platform by Google personnel isn't always logged. See [Limitations of Access Transparency in Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-transparency#limitations) for more information.   
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb) |  GA  |  None   
[Anti Money Laundering AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs) |  GA  |  None   
[Apigee](https://docs.cloud.google.com/apigee) |  GA  |  The following Apigee features are not supported by Access Transparency:  


  * Apigee portal
  * Features in the Preview launch stage

Additionally, Apigee Hybrid customers must [upgrade to the latest version](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#release-history) to get full Access Transparency support.   
[API keys](https://docs.cloud.google.com/api-keys/docs/overview) |  Preview  |  None   
[App Engine](https://docs.cloud.google.com/appengine) |  GA  |  Cloud Storage and Cloud SQL are the only [compatible storage backends](https://docs.cloud.google.com/appengine/docs/standard/java/storage) for App Engine supported by Access Transparency.   
[App Hub](https://docs.cloud.google.com/app-hub/docs) |  GA  |  None   
[App Topology](https://docs.cloud.google.com/app-topology) |  GA  |  Access Transparency supports One Graph.   
[Application Design Center](https://docs.cloud.google.com/application-design-center/docs) |  GA  |  None   
[Application Integration](https://docs.cloud.google.com/application-integration/docs) |  GA  |  None   
[Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) |  GA  |  None   
[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) |  GA  |  None   
[Automotive AI Agent](https://docs.cloud.google.com/solutions/vertical-ai-agents?e=48754805#automotive-agent) |  GA  |  None   
[Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke) |  GA  |  None   
[Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) |  GA  |  Workloads that depend on a management console and backup/recovery appliances are not supported by Access Transparency.   
[BigQuery](https://docs.cloud.google.com/bigquery) |  GA  |  Some information about your queries, tables, and datasets might not generate an Access Transparency log entry if viewed by Cloud Customer Care. Viewing query text, table names, dataset names, and dataset access control lists might not generate Access Transparency log entries; this access pathway gives read-only access. Viewing query results and table or dataset data generates Access Transparency log entries.  
  
Data in queries residing in [non-Google regions for BigQuery Omni](https://docs.cloud.google.com/bigquery-omni/docs/locations) does not generate an Access Transparency log entry.  
  
Gemini in BigQuery is not supported in Assured Workloads. Access Transparency supports [ BigQuery data preparation](https://docs.cloud.google.com/bigquery/docs/data-prep-introduction). Access Transparency supports [Lakehouse tables](https://docs.cloud.google.com/lakehouse/docs/introduction).  
[Bigtable](https://docs.cloud.google.com/bigtable) |  GA  |  None   
[BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) |  GA  |  None   
[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) |  GA  |  None   
[Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service) |  GA  |  None   
[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) |  GA  |  None   
[Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview) |  GA  |  Access Transparency supports [Chrome Enterprise Premium secure gateway](https://docs.cloud.google.com/chrome-enterprise-premium/docs/security-gateway-private-web-apps#create-gateway).   
[Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) |  GA  |  None   
[Cloud Billing](https://docs.cloud.google.com/billing/docs) |  Preview  |  None   
[Cloud Build](https://docs.cloud.google.com/build) |  GA  |  None   
[Managed Service for Apache Airflow](https://docs.cloud.google.com/composer) |  GA  |  None   
[Cloud Data Fusion](https://docs.cloud.google.com/data-fusion) |  GA  |  None   
[Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) |  GA  |  None   
[Cloud DNS](https://docs.cloud.google.com/dns) |  GA  |  None   
[Cloud Domains](https://docs.cloud.google.com/domains/docs/overview) |  GA  |  None   
[Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) |  GA  |  None   
[Fault Injection Testing](https://docs.cloud.google.com/fault-injection-testing/overview) |  GA  |  None   
[Cloud Run functions](https://docs.cloud.google.com/functions) |  GA  |  None   
[Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api) |  GA  |  Features within Cloud Healthcare API that are not yet generally available might not generate Access Transparency logs. For more information, see the [Cloud Healthcare API documentation](https://docs.cloud.google.com/healthcare-api/docs).   
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) |  GA  |  None   
[Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) |  GA  |  None   
[Cloud Logging](https://docs.cloud.google.com/logging) |  GA  |  None   
[Cloud NAT](https://docs.cloud.google.com/nat) |  GA  |  None   
[Cloud OS Login API](https://docs.cloud.google.com/compute/docs/oslogin) |  GA  |  None   
[Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router) |  GA  |  None   
[Cloud Run](https://docs.cloud.google.com/run/docs) |  GA  |  None   
[Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) |  GA  |  None   
[Cloud SQL](https://docs.cloud.google.com/sql) |  GA  |  None   
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh) |  GA  |  None   
[Cloud Storage](https://docs.cloud.google.com/storage) |  GA  |  None   
[Cloud Tasks](https://docs.cloud.google.com/tasks) |  GA  |  None   
[Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) |  GA  |  None   
[Cloud Trace](https://docs.cloud.google.com/trace/docs) |  GA  |  None   
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) |  GA  |  None   
[Cloud Vision API](https://docs.cloud.google.com/vision) |  GA  |  None   
[Cloud Workstations](https://docs.cloud.google.com/workstations/docs) |  GA  |  None   
[Colab Enterprise](https://docs.cloud.google.com/colab/docs/introduction) |  GA  |  None   
[Compute Engine](https://docs.cloud.google.com/compute-engine) |  GA  |  None   
[Container Registry](https://docs.cloud.google.com/container-registry/docs) |  Preview  |  None   
[Customer Experience Agent Studio](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps) |  GA  |  None   
[Customer Experience Insights](https://docs.cloud.google.com/contact-center/insights/docs) |  GA  |  None   
[Database Center](https://docs.cloud.google.com/database-center) |  GA  |  None   
[Database Migration Service](https://docs.cloud.google.com/database-migration/docs) |  GA  |  None   
[Dataflow](https://docs.cloud.google.com/dataflow/docs) |  GA  |  None   
[Dataform](https://docs.cloud.google.com/dataform) |  GA  |  None   
[Knowledge Catalog](https://docs.cloud.google.com/dataplex) |  GA  |  None   
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs) |  GA  |  None   
[Datastream](https://docs.cloud.google.com/datastream/docs) |  GA  |  None   
[Developer Connect](https://docs.cloud.google.com/developer-connect/docs) |  GA  |  None   
[Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs) |  GA  |  None   
[Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs) |  GA  |  None   
[DNS Armor](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/dns/docs/threat-detection) |  GA  |  None   
[Document AI](https://docs.cloud.google.com/document-ai/docs) |  GA  |  None   
[Eventarc](https://docs.cloud.google.com/eventarc/docs) |  GA  |  None   
[External passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) |  GA  |  None   
[Filestore](https://docs.cloud.google.com/filestore) |  GA  |  None   
[Firebase App Hosting](https://firebase.google.com/docs/app-hosting) |  Preview  |  None   
[Firebase Data Connect](https://firebase.google.com/docs/data-connect) |  GA  |  None   
[Firebase Security Rules](https://firebase.google.com/docs/rules) |  GA  |  None   
[Firestore](https://firebase.google.com/docs/firestore) |  GA  |  None   
[Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview) |  GA  |  None   
[Gemini Data Analytics](https://docs.cloud.google.com/gemini/data-agents) |  GA  |  None   
[Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-transparency) |  GA  |  Access to your data in Gemini Enterprise Agent Platform by Google personnel isn't always logged. See [Limitations of Access Transparency in Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-transparency#limitations) for more information.   
[Gemini Enterprise Agent Platform Workbench instances](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/introduction) |  GA  |  None   
[Gemini Enterprise Agent Platform Workbench managed notebooks](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/managed/introduction) |  GA  |  None   
[Gemini Enterprise Agent Platform Workbench user-managed notebooks](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/user-managed/introduction) |  GA  |  None   
[Gemini Enterprise for Customer Experience](https://docs.cloud.google.com/customer-engagement-ai) |  GA  |  None   
[GKE Connect](https://docs.cloud.google.com/kubernetes-engine/docs) |  GA  |  None   
[GKE Hub](https://docs.cloud.google.com/anthos/fleet-management/docs) |  GA  |  None   
[GKE Identity Service](https://docs.cloud.google.com/anthos/identity) |  GA  |  None   
[Google Cloud Armor](https://docs.cloud.google.com/armor) |  GA  |  Access Transparency logs are generated for regional Google Cloud Armor security policies. Global Google Cloud Armor security policies won't generate logs.   
[Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) |  GA  |  None   
[Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview) |  GA  |  None   
[Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs) |  GA  |  None   
[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) |  GA  |  None   
[Google Distributed Cloud](https://docs.cloud.google.com/anthos/gke/docs/on-prem) |  GA  |  None   
[Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs) |  GA  |  Access Transparency supports [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming).   
[Google Security Operations SIEM](https://docs.cloud.google.com/chronicle-siem) |  GA  |  None   
[Google Security Operations SOAR](https://docs.cloud.google.com/chronicle/docs/soar) |  GA  |  None   
[Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) |  GA  |  None   
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) |  GA  |  Access Transparency supports System for Cross-domain Identity Management (SCIM) through Workforce Identity Federation.   
[Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs) |  GA  |  None   
[Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) |  GA  |  None   
[Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs) |  GA  |  None   
[Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs) |  GA  |  None   
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) |  GA  |  None   
[Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console) |  GA  |  None   
[Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) |  GA  |  None   
[Data Studio](https://docs.cloud.google.com/looker/docs/studio) |  GA  |  None   
[Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis) |  GA  |  None   
[Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster) |  GA  |  None   
[Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey) |  GA  |  None   
[Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) |  GA  |  None   
[Cloud Monitoring](https://docs.cloud.google.com/monitoring) |  GA  |  None   
[NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview) |  GA  |  None   
[Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) |  GA  |  None   
[Org Lifecycle API](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations#LifecycleState) |  GA  |  None   
[Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) |  GA  |  None   
[Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview) |  GA  |  None   
[Persistent Disk](https://docs.cloud.google.com/compute/docs/disks) |  GA  |  None   
[Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview) |  GA  |  None   
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs) |  GA  |  None   
[regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#regional-td) |  GA  |  None   
[regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp#regional-external-proxy-network-load-balancer) |  GA  |  None   
[regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) |  GA  |  None   
[regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp#regional-internal-proxy-network-load-balancer) |  GA  |  None   
[Resource Manager](https://docs.cloud.google.com/resource-manager/docs) |  GA  |  None   
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs) |  GA  |  None   
[Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs) |  GA  |  None   
[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) |  GA  |  None   
[Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) |  GA  |  Access Transparency supports the Security Command Center Premium tier.   
[Sensitive Data Protection](https://docs.cloud.google.com/dlp/docs) |  GA  |  None   
[Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) |  GA  |  None   
[Service Management](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest) |  GA  |  None   
[Service Usage](https://docs.cloud.google.com/service-usage/docs/reference/rest) |  Preview  |  None   
[Spanner](https://docs.cloud.google.com/spanner) |  GA  |  None   
[Speaker ID](https://docs.cloud.google.com/speaker-id) |  GA  |  None   
[Speech-to-Text](https://docs.cloud.google.com/speech-to-text) |  GA  |  None   
[Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview) |  GA  |  None   
[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer-service) |  GA  |  None   
[Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs) |  GA  |   
[Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs) |  GA  |  None   
[Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview) |  GA  |  (except for Vector Search 2.0) Access to your data in Gemini Enterprise Agent Platform by Google personnel isn't always logged. See [Limitations of Access Transparency in Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-transparency#limitations) for more information.   
[Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs) |  GA  |  None   
[VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) |  GA  |  None   
[Web Risk](https://docs.cloud.google.com/web-risk/docs/overview) |  GA  |  None   
[Workflows](https://docs.cloud.google.com/workflows/docs/overview) |  GA  |  None   
[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) |  GA  |  None   
[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) |  GA  |  None   
  
## Support for Google Workspace

Several Google Workspace services such as Gmail, Google Docs, Google Calendar, and Google Drive record the actions that Google personnel take when accessing Customer Data.

Access Transparency logs help ensure that Google personnel access Customer Data with a valid business justification. Access Transparency logs can also help security information and event management (SIEM) tools identify data exfiltration and exposure to external malicious actors targeting your Google Workspace resources. You can use the Google Cloud console to access the Access Transparency logs that Google Workspace services generate.

For more information about Access Transparency logs for Google Workspace, including the list of Google Workspace services that support Access Transparency, see [Access Transparency: View logs on Google access to user content](https://support.google.com/a/answer/9230474).

For information about viewing and understanding the Access Transparency logs that Google Workspace services generate, see [Viewing Access Transparency logs for Google Workspace](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/understanding-workspace-logs).

For information about the audit logs that Google Workspace services generate, see [Cloud Audit Logs for Google Workspace](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
