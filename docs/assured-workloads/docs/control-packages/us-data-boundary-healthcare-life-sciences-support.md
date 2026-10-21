---
url: https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support/
title: US Data Boundary for Healthcare and Life Sciences with Support \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:47.476053+00:00
---

# US Data Boundary for Healthcare and Life Sciences with Support  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# US Data Boundary for Healthcare and Life Sciences with Support

**Important:** Before following the guidance on this page, we recommend that you seek independent legal advice relating to your responsibilities under US Data Boundary for Healthcare and Life Sciences with Support. Nothing in this document is intended to provide you with or should be used as a substitute for legal advice.

This page describes the set of controls that are applied on US Data Boundary for Healthcare and Life Sciences with Support workloads in Assured Workloads. It provides detailed information about [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency), supported Google Cloud products and their API endpoints, and any applicable restrictions or limitations on those products.

US Data Boundary for Healthcare and Life Sciences with Support lets you run workloads that are compliant with requirements for Health Insurance Portability and Accountability Act (HIPAA) and Health Information Trust Alliance (HITRUST). Each supported product is listed on [Google Cloud's HIPAA Business Associate Agreement (BAA) page](https://cloud.google.com/security/compliance/hipaa/#covered-products) and [Google Cloud's HITRUST Common Security Framework (CSF) page](https://cloud.google.com/security/compliance/hitrust).

The following additional information applies to US Data Boundary for Healthcare and Life Sciences with Support:

  * **Data residency** : The US Data Boundary for Healthcare and Life Sciences with Support control package sets data location controls to support [US-only regions](https://docs.cloud.google.com/assured-workloads/docs/locations#americas). For more information, see the Google Cloud-wide organization policy constraints section.
  * **Support** : Technical support services for US Data Boundary for Healthcare and Life Sciences with Support workloads are available with Enhanced or Premium [Cloud Customer Care](https://docs.cloud.google.com/support) subscriptions. US Data Boundary for Healthcare and Life Sciences with Support workloads support cases are routed to US Persons located in the US. For more information, see [Getting support](https://docs.cloud.google.com/assured-workloads/docs/getting-support#hcls-support).
  * **Pricing** : The US Data Boundary for Healthcare and Life Sciences with Support control package is included in Assured Workloads' _Premium tier_ , which incurs a 5% additional charge. For more information, see [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing).



## Prerequisites

To remain compliant as a user of the US Data Boundary for Healthcare and Life Sciences with Support control package, verify that you satisfy and adhere to the following prerequisites:

  * Create a US Data Boundary for Healthcare and Life Sciences with Support folder using Assured Workloads and deploy your HIPAA or HITRUST workloads only in that folder.
  * Only enable and use in-scope services for US Data Boundary for Healthcare and Life Sciences with Support workloads. If you enable any additional services by modifying the [Restrict Service Usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) (`gcp.restrictServiceUsage`) organization policy constraint set on your Assured Workloads folder, you're choosing to accept the associated risks as described in [Shared responsibility in Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility). The following additional prerequisites apply:

    * Each service must be listed on [Google Cloud's HIPAA BAA page](https://cloud.google.com/security/compliance/hipaa/#covered-products) or [Google Cloud's HITRUST CSF page](https://cloud.google.com/security/compliance/hitrust) for you to remain compliant.
    * When you allowlist any additional services by modifying this constraint, Assured Workloads monitoring will report compliance violations. To remove these violations and prevent future notifications for services added to the allowlist, you must [grant an exception](https://docs.cloud.google.com/assured-workloads/docs/monitor-folder#exception) for each violation.
    * Before adding a service to the allowlist, verify that it supports CMEK by reviewing the [Compatible services](https://docs.cloud.google.com/kms/docs/compatible-services) page in the Cloud KMS documentation. If you want to enforce a stricter security posture when using CMEK, see the [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage) page in the Cloud KMS documentation.
    * Before adding a service to the allowlist, verify that it's listed on the [Google Cloud Services with Data Residency](https://cloud.google.com/terms/data-residency) page.
    * Before adding a service to the allowlist, verify that it's supported by VPC Service Controls by reviewing the [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) page in the VPC Service Controls documentation.
    * Before adding a service to the allowlist, verify that it's supported by [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services) and [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/supported-services).
  * Don't use [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) unless otherwise noted. US Data Boundary for Healthcare and Life Sciences with Support doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM page](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page.

  * Don't change the default organization policy constraint values unless you understand and are willing to accept the data residency risks that might occur.

  * Consider adopting the general security best practices provided in the [Google Cloud security best practices center](https://cloud.google.com/security/best-practices).




## Supported products and API endpoints

Unless otherwise noted, users can access all supported products through the Google Cloud console. Restrictions or limitations that affect the features of a supported product, including those that are enforced through [organization policy constraint settings](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#how_organization_policy_works), are listed in the following table.

If a product is not listed, that product is unsupported and has not met the control requirements for US Data Boundary for Healthcare and Life Sciences with Support. Unsupported products are not recommended for use without due diligence and a thorough understanding of your responsibilities in the [shared responsibility model](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility). Before using an unsupported product, ensure that you are aware of and are willing to accept any associated risks involved, such as negative impacts to data residency or data sovereignty. 

**Note** : Unsupported products may share an API service endpoint with supported products, making them available to all users.**Important** : [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) aren't supported for any US Data Boundary for Healthcare and Life Sciences with Support products unless otherwise noted. US Data Boundary for Healthcare and Life Sciences with Support doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. It's your responsibility to ensure that Google Cloud MCP servers endpoints aren't used with any US Data Boundary for Healthcare and Life Sciences with Support products. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page. 

Supported product | API endpoints | Restrictions or limitations  
---|---|---  
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
[Apigee](https://docs.cloud.google.com/apigee/docs) |  `apigee.googleapis.com`  
|  None   
[Application Integration](https://docs.cloud.google.com/application-integration/docs/overview) |  `integrations.googleapis.com`  
|  None   
[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) |  `artifactregistry.googleapis.com`  
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
`bigquerydatatransfer.googleapis.com`  
`bigqueryreservation.googleapis.com`  
`bigquerystorage.googleapis.com`  
|  Affected features  
[BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) |  `bigquerydatatransfer.googleapis.com`  
|  None   
[Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) |  `bigtable.googleapis.com`  
`bigtableadmin.googleapis.com`  
|  Affected features  
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
[Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) |  `cloudkms.googleapis.com`  
|  None   
[Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs) |  `healthcare.googleapis.com`  
|  None   
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) |  `compute.googleapis.com`  
|  Affected features  
[Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/key-management-service) |  `cloudkms.googleapis.com`  
|  None   
[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) |  `logging.googleapis.com`  
|  Affected features  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) |  `monitoring.googleapis.com`  
|  Affected features  
[Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router) |  `compute.googleapis.com`  
|  None   
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) |  `run.googleapis.com`  
|  Affected features  
[Cloud Run functions](https://docs.cloud.google.com/functions/docs) |  `run.googleapis.com`  
|  None   
[Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) |  `sqladmin.googleapis.com`  
|  None   
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) |  `mesh.googleapis.com`  
`meshca.googleapis.com`  
`meshconfig.googleapis.com`  
`trafficdirector.googleapis.com`  
`networkservices.googleapis.com`  
|  None   
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) |  `storage.googleapis.com`  
|  None   
[Cloud Tasks](https://docs.cloud.google.com/tasks/docs/dual-overview) |  `cloudtasks.googleapis.com`  
|  None   
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  `compute.googleapis.com`  
|  Affected features  
[Cloud Vision API](https://docs.cloud.google.com/vision/docs/features-list) |  `vision.googleapis.com`  
|  Affected features  
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview) |  `compute.googleapis.com`  
|  Affected features and organization policy constraints  
[Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs) |  `dialogflow.googleapis.com`  
|  None   
[Customer Experience Insights](https://docs.cloud.google.com/contact-center/insights/docs) |  `contactcenterinsights.googleapis.com`  
|  None   
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) |  `dataflow.googleapis.com`  
`datapipelines.googleapis.com`  
|  None   
[Dataform](https://docs.cloud.google.com/dataform/docs/overview) |  `dataform.googleapis.com`  
|  None   
[Document AI](https://docs.cloud.google.com/document-ai/docs) |  `documentai.googleapis.com`  
|  None   
[Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) |  `eventarc.googleapis.com`  
|  None   
[External passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) |  `compute.googleapis.com`  
|  None   
[Filestore](https://docs.cloud.google.com/filestore/docs/overview) |  `file.googleapis.com`  
|  None   
[Firestore](https://docs.cloud.google.com/firestore/native/docs/overview) |  `firestore.googleapis.com`  
|  None   
[Google Kubernetes Engine (GKE) Hub](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview) |  `gkehub.googleapis.com`  
|  None   
[Generative AI on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview) |  `aiplatform.googleapis.com`  
|  None   
[Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) |  `compute.googleapis.com`  
`networksecurity.googleapis.com`  
|  Affected features  
[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) |  `container.googleapis.com`  
`containersecurity.googleapis.com`  
|  None   
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) |  `iam.googleapis.com`  
`policytroubleshooter.googleapis.com`  
|  None   
[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) |  `iap.googleapis.com`  
|  None   
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) |  `compute.googleapis.com`  
|  None   
[Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) |  `cloudekm.googleapis.com`  
`cloudkms.googleapis.com`  
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
[Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) |  `modelarmor.googleapis.com`  
|  None   
[Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) |  `networkconnectivity.googleapis.com`  
|  Affected features  
[Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) |  `compute.googleapis.com`  
|  None   
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) |  `pubsub.googleapis.com`  
|  Organization policy constraints  
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#regional-td) |  `compute.googleapis.com`  
|  None   
[Regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp#regional-external-proxy-network-load-balancer) |  `compute.googleapis.com`  
|  None   
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) |  `compute.googleapis.com`  
|  None   
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp#regional-internal-proxy-network-load-balancer) |  `compute.googleapis.com`  
|  None   
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) |  `secretmanager.googleapis.com`  
|  None   
[Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview) |  `securesourcemanager.googleapis.com`  
|  None   
[Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) |  `securitycenter.googleapis.com`  
`securitycentermanagement.googleapis.com`  
`securityposture.googleapis.com`  
`websecurityscanner.googleapis.com`  
|  None   
[Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) |  `dlp.googleapis.com`  
|  None   
[Spanner](https://docs.cloud.google.com/spanner/docs) |  `spanner.googleapis.com`  
|  Affected features and organization policy constraints  
[Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/overview) |  `speech.googleapis.com`  
|  None   
[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) |  `storagetransfer.googleapis.com`  
|  None   
[Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs/basics) |  `texttospeech.googleapis.com`  
|  None   
[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) |  `accesscontextmanager.googleapis.com`  
`accesscontextintelligence.googleapis.com`  
|  None   
[Vertex AI Batch prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-batch-predictions) |  `aiplatform.googleapis.com`  
|  None   
[Vertex AI Online prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-online-predictions) |  `aiplatform.googleapis.com`  
|  None   
[Agent Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/vertex-ai-search) |  `discoveryengine.googleapis.com`  
|  None   
[Vertex AI Training](https://docs.cloud.google.com/vertex-ai/docs/training-overview) |  `aiplatform.googleapis.com`  
|  None   
[Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/notebook-solution) |  `notebooks.googleapis.com`  
|  None   
[Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) |  `compute.googleapis.com`  
|  None   
  
## Restrictions and limitations

The following sections describe Google Cloud-wide or product-specific restrictions or limitations for features, including any organization policy constraints that are set by default on US Data Boundary for Healthcare and Life Sciences with Support folders. Other applicable organization policy constraints—even if not set by default—can provide additional defense-in-depth to further protect your organization's Google Cloud resources.

We strongly recommend not changing the values of the required organization policy constraints listed in the following sections. Doing so may undermine data residency. When such a change has been made, the effects of the change are difficult or impossible to reverse. Ensure that you understand the ramifications of changing an organization policy constraint's value before proceeding.   
  
Additionally, ensure that any automated mechanisms your organization uses to manage organization policies are updated to prevent these values from being changed unintentionally.

### Google Cloud-wide

#### Google Cloud-wide organization policy constraints

The following [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) apply across Google Cloud. 

Organization policy constraint | Description  
---|---  
[`gcp.resourceLocations`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) | Set to the following locations in the `allowedValues` list: 

  * `us`
  * `us-central1`
  * `us-central2`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`

This value restricts creation of new resources to the selected values. When set, no resources can be created in any other regions, multi-regions, or locations outside of the selection. See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and cannot be restricted.  
  
Changing this value by making it less restrictive potentially undermines data residency by allowing data to be created or stored outside of a compliant data boundary.   
[`gcp.restrictNonCmekServices`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek) | Set to a list of all in-scope [API service names](https://docs.cloud.google.com/iam/docs/full-resource-names), including: 

  * `bigquerydatatransfer.googleapis.com`

Some features may be affected for each of the services listed above.   
  
Each listed service requires [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). CMEK encrypts at-rest data with a key managed by you, not Google's default encryption mechanisms.   
  
Changing this value by removing one or more in-scope services from the list may undermine data sovereignty, because new at-rest data will be automatically encrypted using Google's own keys instead of yours. Existing at-rest data will remain encrypted by the key you provided.   
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
Loading data | [BigQuery Data Transfer Service connectors](https://docs.cloud.google.com/bigquery/docs/dts-introduction#supported_data_sources) for Google Software as a Service (SaaS) apps, external cloud storage providers, and data warehouses are not supported. It is your responsibility not to use BigQuery Data Transfer Service connectors for US Data Boundary for Healthcare and Life Sciences with Support workloads.   
[Third-party transfers](https://docs.cloud.google.com/bigquery/docs/third-party-transfer) | BigQuery doesn't verify support for third-party transfers for the BigQuery Data Transfer Service. It is your responsibility to verify support when using any third-party transfer for the BigQuery Data Transfer Service.   
Non-compliant BQML models | [Externally-trained BQML models](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#externally_trained_models) are not supported.   
Query jobs | Query jobs should only be created within Assured Workloads folders.   
Queries on datasets in other projects | BigQuery doesn't prevent Assured Workloads datasets from being queried from non-Assured Workloads projects. You should ensure that any query that has a read or a join on Assured Workloads data be placed in Assured Workloads folders. You can specify a [fully-qualified table name](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_query) for their query result using `projectname.dataset.table` in the BigQuery CLI.   
Cloud Logging | BigQuery utilizes Cloud Logging for some of your log data. You should disable your `_default` logging buckets or restrict `_default` buckets to in-scope regions to maintain compliance using the following command:  
  
`gcloud alpha logging settings update --organization=ORGANIZATION_ID --disable-default-sink`   
  
For more information, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).   
  
### Bigtable

#### Affected Bigtable features

Feature | Description  
---|---  
[Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) | This feature is disabled.  
Split boundaries | Bigtable uses a small subset of row keys to define split boundaries, which may include customer data and metadata. A split boundary in Bigtable denotes the location where contiguous ranges of rows in a table are split into tablets.  
  
These split boundaries are accessible by Google personnel for technical support and debugging purposes, and are not subject to administrative access data controls in Assured Workloads.   
  
### Cloud Interconnect

#### Affected Cloud Interconnect features

Feature | Description  
---|---  
High-availability (HA) VPN | You must enable high-availability (HA) VPN functionality when using Cloud Interconnect with Cloud VPN. Additionally, you must adhere to the encryption and regionalization requirements listed in the Affected Cloud VPN features section.   
  
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
  
### Cloud Monitoring

#### Affected Cloud Monitoring features

Feature | Description  
---|---  
[Synthetic Monitor](https://docs.cloud.google.com/monitoring/uptime-checks/introduction#about-sm) | This feature is disabled.  
[Uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/introduction#about-uptime) | This feature is disabled.  
  
### Cloud Run

#### Affected Cloud Run features

Feature | Description  
---|---  
Unsupported features | The following Cloud Run features aren't supported:  


  * [Cloud Trace integration](https://docs.cloud.google.com/run/docs/trace)
  * [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview)
  * [Eventarc triggers](https://docs.cloud.google.com/functions/docs/calling/eventarc)

  
  
### Cloud Vision API

#### Affected Cloud Vision API features

Feature | Description  
---|---  
HCLS with Support-compliant Cloud Vision API endpoints | It is your responsibility to use only the US region API endpoint (`us-vision.googleapis.com`) for the Cloud Vision API. The global endpoint (`vision.googleapis.com`) is not HCLS with Support-compliant and using it may undermine your workload's data residency.   
  
### Cloud VPN

#### Affected Cloud VPN features

Feature | Description  
---|---  
VPN endpoints | You must use only Cloud VPN endpoints that are located in an in-scope region. Ensure that your VPN gateway is configured for use in an in-scope region only.   
  
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
  
### Google Cloud Armor

#### Affected Google Cloud Armor features

Feature | Description  
---|---  
[Globally scoped security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types) | This feature is disabled by the `compute.disableGlobalCloudArmorPolicy` organization policy constraint.   
  
### Network Connectivity Center

#### Affected Network Connectivity Center features

Feature | Description  
---|---  
Google Cloud console | Network Connectivity Center features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/network-connectivity/docs/apis) instead.  
  
### Pub/Sub

#### Pub/Sub organization policy constraints

Organization policy constraint | Description  
---|---  
`pubsub.managed.disableSubscriptionMessageTransforms` | Set to **True**.  
  
Disables Pub/Sub subscriptions from being set with [Single Message Transforms (SMTs)](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).  
  
Changing this value might affect your workload's data residency or data sovereignty.   
`pubsub.managed.disableTopicMessageTransforms` | Set to **True**.  
  
Disables Pub/Sub topics from being set with [Single Message Transforms (SMTs)](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).  
  
Changing this value may affect your workload's data residency or data sovereignty.   
  
### Spanner

#### Affected Spanner features

Feature | Description  
---|---  
Split boundaries | Spanner uses a small subset of primary keys and indexed columns to define [split boundaries](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#database-splits), which may include customer data and metadata. A split boundary in Spanner denotes the location where contiguous ranges of rows are split into smaller pieces.  
  
These split boundaries are accessible by Google personnel for technical support and debugging purposes, and are not subject to administrative access data controls in Assured Workloads.   
  
#### Spanner organization policy constraints

Organization policy constraint | Description  
---|---  
`spanner.assuredWorkloadsAdvancedServiceControls` | Set to **True**.  
  
Applies additional data sovereignty and supportability controls to Spanner resources.   
`spanner.disableMultiRegionInstanceIfNoLocationSelected` | Set to **True**.  
  
Disables the ability to create multi-region Spanner instances to enforce data residency and data sovereignty.   
  
## What's next

  * Learn how to [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder)
  * Learn about the [US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences) control package
  * Understand [Assured Workloads pricing](https://docs.cloud.google.com/assured-workloads/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
