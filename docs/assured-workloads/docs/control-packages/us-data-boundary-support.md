---
url: https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support/
title: US Data Boundary and Support \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:52.077271+00:00
---

# US Data Boundary and Support  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# US Data Boundary and Support

This page describes the set of controls that are applied on US Data Boundary and Support workloads in Assured Workloads. It provides detailed information about [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency), supported Google Cloud products and their API endpoints, and any applicable restrictions or limitations on those products. The following additional information applies to US Data Boundary and Support:

  * **Data residency** : The US Data Boundary and Support control package sets data location controls to support [US-only regions](https://docs.cloud.google.com/assured-workloads/docs/locations#americas). See the Google Cloud-wide organization policy constraints section for more information.
  * **Support** : Technical support services for US Data Boundary and Support workloads are available with Enhanced or Premium [Cloud Customer Care](https://docs.cloud.google.com/support) subscriptions. US Data Boundary and Support workloads support cases are routed to US Persons located in the US; see [Getting support](https://docs.cloud.google.com/assured-workloads/docs/getting-support#us-regions-support) for more information.
  * **Pricing** : The US Data Boundary and Support control package is included in Assured Workloads' _Premium tier_ , which incurs a 5% additional charge. See [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing) for more information.



## Supported products and API endpoints

Unless otherwise noted, users can access all supported products through the Google Cloud console. Restrictions or limitations that affect the features of a supported product, including those that are enforced through [organization policy constraint settings](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#how_organization_policy_works), are listed in the following table.

If a product is not listed, that product is unsupported and has not met the control requirements for US Data Boundary and Support. Unsupported products are not recommended for use without due diligence and a thorough understanding of your responsibilities in the [shared responsibility model](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility). Before using an unsupported product, ensure that you are aware of and are willing to accept any associated risks involved, such as negative impacts to data residency or data sovereignty. 

**Note** : Unsupported products may share an API service endpoint with supported products, making them available to all users.**Important** : [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) aren't supported for any US Data Boundary and Support products unless otherwise noted. US Data Boundary and Support doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. It's your responsibility to ensure that Google Cloud MCP servers endpoints aren't used with any US Data Boundary and Support products. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page. 

Supported product | API endpoints | Restrictions or limitations  
---|---|---  
[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) |  `securitycenter.googleapis.com`  
|  None   
[Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) |  `accessapproval.googleapis.com`  
|  None   
[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) |  `accesscontextmanager.googleapis.com`  
|  None   
[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) |  `accessapproval.googleapis.com`  
|  None   
[Agent Assist](https://docs.cloud.google.com/agent-assist/docs) |  `dialogflow.googleapis.com`  
|  None   
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) |  `alloydb.googleapis.com`  
|  None   
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) |  `mesh.googleapis.com`  
`meshca.googleapis.com`  
`meshconfig.googleapis.com`  
|  None   
[Apigee](https://docs.cloud.google.com/apigee/docs) |  `apigee.googleapis.com`  
|  None   
[App Hub](https://docs.cloud.google.com/app-hub/docs/overview) |  `apphub.googleapis.com`  
|  None   
[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) |  `artifactregistry.googleapis.com`  
|  None   
[Audit Manager](https://docs.cloud.google.com/audit-manager/docs/overview) |  `auditmanager.googleapis.com`  
|  None   
[AutoML Tables](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide) |  `automl.googleapis.com`  
|  None   
[Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) |  `backupdr.googleapis.com`  
|  None   
[Backup for Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke) |  `gkebackup.googleapis.com`  
|  None   
[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) |  `bigquery.googleapis.com`  
`bigqueryconnection.googleapis.com`  
`bigquerydatapolicy.googleapis.com`  
`bigquerymigration.googleapis.com`  
`bigqueryreservation.googleapis.com`  
`bigquerystorage.googleapis.com`  
|  Affected features  
[BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) |  `bigquerydatatransfer.googleapis.com`  
|  None   
[Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) |  `bigtable.googleapis.com`  
`bigtableadmin.googleapis.com`  
|  None   
[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) |  `binaryauthorization.googleapis.com`  
|  None   
[Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) |  `privateca.googleapis.com`  
|  None   
[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) |  `certificatemanager.googleapis.com`  
|  None   
[Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) |  `cloudasset.googleapis.com`  
|  None   
[Cloud Build](https://docs.cloud.google.com/build/docs/overview) |  `cloudbuild.googleapis.com`  
|  None   
[Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) |  `dns.googleapis.com`  
|  None   
[Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview) |  `datafusion.googleapis.com`  
|  None   
[Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) |  `clouddeploy.googleapis.com`  
|  None   
[Cloud Domains](https://docs.cloud.google.com/domains/docs/overview) |  `domains.googleapis.com`  
|  None   
[Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) |  `cloudkms.googleapis.com`  
|  None   
[Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) |  `cloudkms.googleapis.com`  
|  None   
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) |  `compute.googleapis.com`  
|  None   
[Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/key-management-service) |  `cloudkms.googleapis.com`  
|  None   
[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) |  `compute.googleapis.com`  
|  None   
[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) |  `logging.googleapis.com`  
|  Affected features  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) |  `monitoring.googleapis.com`  
|  None   
[Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) |  `compute.googleapis.com`  
|  None   
[Cloud OS Login API](https://docs.cloud.google.com/compute/docs/oslogin) |  `oslogin.googleapis.com`  
|  None   
[Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router) |  `compute.googleapis.com`  
|  None   
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) |  `run.googleapis.com`  
|  Affected features  
[Cloud Run functions](https://docs.cloud.google.com/functions/docs) |  `run.googleapis.com`  
|  None   
[Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) |  `sqladmin.googleapis.com`  
|  None   
[Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres) |  `sqladmin.googleapis.com`  
|  None   
[Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) |  `cloudscheduler.googleapis.com`  
|  None   
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) |  `storage.googleapis.com`  
|  None   
[Cloud Tasks](https://docs.cloud.google.com/tasks/docs/dual-overview) |  `cloudtasks.googleapis.com`  
|  None   
[Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) |  `cloudtrace.googleapis.com`  
|  None   
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  `compute.googleapis.com`  
|  None   
[Cloud Vision API](https://docs.cloud.google.com/vision/docs/features-list) |  `vision.googleapis.com`  
|  None   
[Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) |  `workstations.googleapis.com`  
|  None   
[Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview) |  `cloudsecuritycompliance.googleapis.com`  
|  None   
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview) |  `compute.googleapis.com`  
|  Affected features and organization policy constraints  
[Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) |  `anthosconfigmanagement.googleapis.com`  
|  None   
[Google Kubernetes Engine (GKE) Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect) |  `gkeconnect.googleapis.com`  
|  None   
[Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs) |  `dialogflow.googleapis.com`  
|  None   
[Customer Experience Insights](https://docs.cloud.google.com/contact-center/insights/docs) |  `contactcenterinsights.googleapis.com`  
|  None   
[Data Security Posture Management](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) |  `Not applicable`  
|  None   
[Database Center](https://docs.cloud.google.com/database-center/docs/overview) |  `Not applicable`  
|  None   
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) |  `dataflow.googleapis.com`  
`datapipelines.googleapis.com`  
|  None   
[Dataform](https://docs.cloud.google.com/dataform/docs/overview) |  `dataform.googleapis.com`  
|  None   
[Document AI](https://docs.cloud.google.com/document-ai/docs) |  `documentai.googleapis.com`  
|  None   
[Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) |  `essentialcontacts.googleapis.com`  
|  None   
[Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) |  `eventarc.googleapis.com`  
|  None   
[Filestore](https://docs.cloud.google.com/filestore/docs/overview) |  `file.googleapis.com`  
|  None   
[Firebase Security Rules](https://firebase.google.com/docs/rules) |  `firebaserules.googleapis.com`  
|  None   
[Firestore](https://docs.cloud.google.com/firestore/native/docs/overview) |  `firestore.googleapis.com`  
|  None   
[Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview) |  `networkmanagement.googleapis.com`  
|  None   
[Google Kubernetes Engine (GKE) Hub](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview) |  `gkehub.googleapis.com`  
|  None   
[Google Kubernetes Engine (GKE) Identity Service](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication) |  `anthosidentityservice.googleapis.com`  
|  None   
[Google Kubernetes Engine (GKE) Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) |  `containerfilesystem.googleapis.com`  
|  None   
[Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs) |  `discoveryengine.googleapis.com`  
|  Affected features  
[Gemini Enterprise Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction) |  `aiplatform.googleapis.com`  
|  None   
[Generative AI on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview) |  `aiplatform.googleapis.com`  
|  None   
[Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) |  `compute.googleapis.com`  
`networksecurity.googleapis.com`  
|  Affected features  
[Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview) |  `managedkafka.googleapis.com`  
|  None   
[Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs) |  `netapp.googleapis.com`  
|  Affected features  
[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) |  `container.googleapis.com`  
`containersecurity.googleapis.com`  
|  None   
[Google Security Operations SIEM](https://docs.cloud.google.com/security/products/security-information-event-management) |  `chronicle.googleapis.com`  
`chronicleservicemanager.googleapis.com`  
|  None   
[Google Security Operations SOAR](https://docs.cloud.google.com/chronicle/docs/soar) |  `Not applicable`  
|  None   
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) |  `iam.googleapis.com`  
|  None   
[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) |  `iap.googleapis.com`  
|  None   
[Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs) |  `config.googleapis.com`  
|  None   
[Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview) |  `connectors.googleapis.com`  
|  None   
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) |  `dataplex.googleapis.com`  
`datalineage.googleapis.com`  
|  Affected features  
[Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) |  `looker.googleapis.com`  
|  None   
[Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview) |  `composer.googleapis.com`  
|  None   
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview) |  `dataproc-control.googleapis.com`  
`dataproc.googleapis.com`  
|  None   
[Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis) |  `redis.googleapis.com`  
|  None   
[Migrate to Containers](https://docs.cloud.google.com/migrate/containers/docs/getting-started) |  `Not applicable`  
|  None   
[Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) |  `modelarmor.googleapis.com`  
|  None   
[Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) |  `networkconnectivity.googleapis.com`  
|  None   
[Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) |  `orgpolicy.googleapis.com`  
|  None   
[Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) |  `compute.googleapis.com`  
|  None   
[Personalized Service Health](https://docs.cloud.google.com/service-health/docs/overview) |  `servicehealth.googleapis.com`  
|  None   
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) |  `pubsub.googleapis.com`  
|  None   
[Resource Manager](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview) |  `cloudresourcemanager.googleapis.com`  
|  None   
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) |  `secretmanager.googleapis.com`  
|  None   
[Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview) |  `securesourcemanager.googleapis.com`  
|  None   
[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) |  `networkservices.googleapis.com`  
`networksecurity.googleapis.com`  
|  None   
[Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) |  `securitycenter.googleapis.com`  
`securitycentermanagement.googleapis.com`  
`securityposture.googleapis.com`  
`websecurityscanner.googleapis.com`  
|  None   
[Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) |  `dlp.googleapis.com`  
|  None   
[Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) |  `vpcaccess.googleapis.com`  
|  None   
[Spanner](https://docs.cloud.google.com/spanner/docs/editions-overview) |  `spanner.googleapis.com`  
|  None   
[Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/overview) |  `speech.googleapis.com`  
|  None   
[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) |  `storagetransfer.googleapis.com`  
|  None   
[Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs/basics) |  `texttospeech.googleapis.com`  
|  None   
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) |  `trafficdirector.googleapis.com`  
|  None   
[VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/overview) |  `osconfig.googleapis.com`  
|  None   
[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) |  `accesscontextmanager.googleapis.com`  
`accesscontextintelligence.googleapis.com`  
|  None   
[Vertex AI Batch prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-batch-predictions) |  `aiplatform.googleapis.com`  
|  None   
[Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring) |  `aiplatform.googleapis.com`  
|  None   
[Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry) |  `aiplatform.googleapis.com`  
|  None   
[Vertex AI Online prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-online-predictions) |  `aiplatform.googleapis.com`  
|  None   
[Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines) |  `aiplatform.googleapis.com`  
|  None   
[Agent Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/vertex-ai-search) |  `discoveryengine.googleapis.com`  
|  None   
[Vertex AI Training](https://docs.cloud.google.com/vertex-ai/docs/training-overview) |  `aiplatform.googleapis.com`  
|  None   
[Vertex AI Tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models) |  `aiplatform.googleapis.com`  
|  None   
[Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) |  `compute.googleapis.com`  
|  None   
[Web Risk](https://docs.cloud.google.com/web-risk/docs/overview) |  `webrisk.googleapis.com`  
|  None   
[Workflows](https://docs.cloud.google.com/workflows/docs/overview) |  `workflows.googleapis.com`  
|  None   
[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) |  `iam.googleapis.com`  
`sts.googleapis.com`  
|  None   
  
## Restrictions and limitations

The following sections describe Google Cloud-wide or product-specific restrictions or limitations for features, including any organization policy constraints that are set by default on US Data Boundary and Support folders. Other applicable organization policy constraints—even if not set by default—can provide additional defense-in-depth to further protect your organization's Google Cloud resources.

We strongly recommend not changing the values of the required organization policy constraints listed in the following sections. Doing so may undermine data residency. When such a change has been made, the effects of the change are difficult or impossible to reverse. Ensure that you understand the ramifications of changing an organization policy constraint's value before proceeding.   
  
Additionally, ensure that any automated mechanisms your organization uses to manage organization policies are updated to prevent these values from being changed unintentionally.

### Google Cloud-wide

#### Google Cloud-wide organization policy constraints

The following [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) apply across Google Cloud. 

Organization policy constraint | Description  
---|---  
[`gcp.resourceLocations`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) | Set to the following locations in the `allowedValues` list: 

  * `us-central1`
  * `us-central2`
  * `us-east4`
  * `us-east1`
  * `us-west1`
  * `us-west4`
  * `us-west3`
  * `us-west2`
  * `us-south1`
  * `us-east5`

This value restricts creation of new resources to the selected values. When set, no resources can be created in any other regions, multi-regions, or locations outside of the selection. See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and cannot be restricted.  
  
Changing this value by making it less restrictive potentially undermines data residency by allowing data to be created or stored outside of a compliant data boundary.   
[`gcp.restrictServiceUsage`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) | Set to allow all supported products and API endpoints.  
  
Determines which services can be used by restricting runtime access to their resources. For more information, see [Restricting resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources).   
[`gcp.restrictTLSVersion`](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions) | Set to deny the following TLS versions:  


  * `TLS_1_0`
  * `TLS_1_1`

For more information, see [Restrict TLS versions](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions).   
  
### BigQuery

#### Affected BigQuery features

Feature | Description  
---|---  
Enabling BigQuery on a new folder | BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  


  1. In the Google Cloud console, go to the **Assured Workloads** page.  [ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)
  2. Select your new Assured Workloads folder from the list.
  3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
  4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder. Gemini in BigQuery is not supported by Assured Workloads.  
Unsupported features | The following BigQuery features are not supported and should not be used in the BigQuery CLI. It is your responsibility not to use them in BigQuery for Assured Workloads.  


  * Interaction with remote data sources
  * [ Externally-trained BQML models](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#externally_trained_models) are not supported. [ Internally-trained BQML models](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#internally_trained_models) are supported.
  * [Data masking with policy tags](https://docs.cloud.google.com/bigquery/docs/column-data-masking#mask_data_with_policy_tags) is not supported. [Data masking by applying data policies directly to columns](https://docs.cloud.google.com/bigquery/docs/column-data-masking#data-policies-on-column) is supported. 
  * GDrive export
  * [Remote functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions#overview)
  * [Saved queries](https://docs.cloud.google.com/bigquery/docs/work-with-saved-queries)
  * Workflow scheduling
  * For BigQuery Studio, [notebooks](https://docs.cloud.google.com/bigquery/docs/create-notebooks) are unsupported.
  * Gemini in BigQuery is not supported.

  
[BigQuery CLI](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool) | The BigQuery CLI is supported.   
  
  
Google Cloud SDK | You must use Google Cloud SDK version 403.0.0 or newer to maintain data regionalization guarantees for technical data. To verify your current Google Cloud SDK version, run `gcloud --version` and then `gcloud components update` to update to the newest version.   
Administrator controls | BigQuery will disable unsupported APIs but administrators with sufficient permissions to create Assured Workloads folders can enable an unsupported API. If this occurs, you will be notified of potential non-compliance through the [Assured Workloads monitoring dashboard](https://docs.cloud.google.com/assured-workloads/docs/monitor-folder).   
Loading data | [BigQuery Data Transfer Service connectors](https://docs.cloud.google.com/bigquery/docs/dts-introduction#supported_data_sources) for Google Software as a Service (SaaS) apps, external cloud storage providers, and data warehouses are not supported. It is your responsibility not to use BigQuery Data Transfer Service connectors for US Data Boundary and Support workloads.   
[Third-party transfers](https://docs.cloud.google.com/bigquery/docs/third-party-transfer) | BigQuery doesn't verify support for third-party transfers for the BigQuery Data Transfer Service. It is your responsibility to verify support when using any third-party transfer for the BigQuery Data Transfer Service.   
Non-compliant BQML models | [Externally-trained BQML models](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#externally_trained_models) are not supported.   
Query jobs | Query jobs should only be created within Assured Workloads folders.   
Queries on datasets in other projects | BigQuery doesn't prevent Assured Workloads datasets from being queried from non-Assured Workloads projects. You should ensure that any query that has a read or a join on Assured Workloads data be placed in Assured Workloads folders. You can specify a [fully-qualified table name](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_query) for their query result using `projectname.dataset.table` in the BigQuery CLI.   
Cloud Logging | BigQuery utilizes Cloud Logging for some of your log data. You should disable your `_default` logging buckets or restrict `_default` buckets to in-scope regions to maintain compliance using the following command:  
  
`gcloud alpha logging settings update --organization=ORGANIZATION_ID --disable-default-sink`   
  
For more information, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).   
  
### Cloud Logging

#### Affected Cloud Logging features

To use Cloud Logging with Customer-managed encryption keys (CMEK), you must complete the steps in the [Enable CMEK for an organization](https://docs.cloud.google.com/logging/docs/routing/managed-encryption#enable) page in the Cloud Logging documentation. Feature | Description  
---|---  
[Log sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) | Filters shouldn't contain Customer Data.  
  
Log sinks include filters which are stored as configuration. Don't create filters that contain Customer Data.   
[Live tailing log entries](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) | Filters shouldn't contain Customer Data.  
  
A live tailing session includes a filter which is stored as configuration. Tailing logs doesn't store any log entry data itself, but can query and transmit data across regions. Don't create filters that contain Customer Data.   
[SQL-based alerting policies](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting) | This feature is disabled.  
  
You cannot use the SQL-based alerting policies feature.   
  
### Compute Engine

#### Affected Compute Engine features

Feature | Description  
---|---  
[ Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) | It is possible for scripts, daemons, and binaries that are included with the guest environment to access unencrypted at-rest and in-use data. Depending on your VM configuration, updates to this software may be installed by default. See [Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) for specific information about each package's contents, source code, and more.  
  
These components help you meet data sovereignty through internal security controls and processes. However, if you want additional control, you can also curate your own images or agents and optionally use the `compute.trustedImageProjects` organization policy constraint.   
  
For more information, see [Building a custom image](https://docs.cloud.google.com/compute/docs/images/building-custom-os).   
[ OS policies in VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies) |  Inline scripts and binary output files within the OS policy files are not encrypted using customer-managed encryption keys (CMEK). Don't include any sensitive information in these files. Consider storing these scripts and output files in Cloud Storage buckets. For more information, see [Example OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).  
  
If you want to restrict the creation or modification of OS policy resources that use inline scripts or binary output files, enable the `constraints/osconfig.restrictInlineScriptAndOutputFileUsage` organization policy constraint.  
  
For more information, see [Constraints for OS Config](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).   
  
#### Compute Engine organization policy constraints

Organization policy constraint | Description  
---|---  
`compute.disableGlobalCloudArmorPolicy` | Set to **True**.  
  
Disables the creation of new global [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview) and the addition or modification of rules to existing global Google Cloud Armor security policies. This constraint doesn't restrict the removal of rules or the ability to remove or change the description and listing of global Google Cloud Armor security policies. Regional Google Cloud Armor security policies are unaffected by this constraint. All global and regional security policies that exist prior to the enforcement of this constraint remain in effect.  
  
  
`compute.restrictNonConfidentialComputing`  
  
| (Optional) Value is not set. Set this value to provide additional defense-in-depth. For more information, see the [Confidential VM documentation](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm).   
`compute.trustedImageProjects`  
  
| (Optional) Value is not set. Set this value to provide additional defense-in-depth.   
  
Setting this value constrains image storage and disk instantiation to the specified list of projects. This value affects data sovereignty by preventing use of any unauthorized images or agents.   
  
### Knowledge Catalog

#### Knowledge Catalog features

Feature | Description  
---|---  
[Attribute Store](https://docs.cloud.google.com/dataplex/docs/attribute-store) | This feature is deprecated and disabled.  
[Data Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview) | This feature is deprecated and disabled. You cannot search through nor manage your metadata in Data Catalog.  
[Lakes and Zones](https://docs.cloud.google.com/dataplex/docs/metadata) | This feature is disabled. You cannot manage lakes, zones and tasks.  
  
### Gemini Enterprise

#### Gemini Enterprise features

Feature | Description  
---|---  
Web Grounding for Enterprise | Gemini Enterprise includes support for the Web Grounding for Enterprise feature.   
  
### Google Cloud NetApp Volumes

#### Affected Google Cloud NetApp Volumes features

Feature | Description  
---|---  
[Supported service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels) | US Data Boundary and Support supports the following service levels:  


  * Standard
  * Premium
  * Extreme

  
  
## What's next

  * Learn how to [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder)
  * Learn about the [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) control package
  * Understand [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
