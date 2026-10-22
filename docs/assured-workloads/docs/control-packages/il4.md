---
url: https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4/
title: Data Boundary for Impact Level 4 (IL4) \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:41.506159+00:00
---

# Data Boundary for Impact Level 4 (IL4)  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data Boundary for Impact Level 4 (IL4)

**Important:** Before following the guidance on this page, we recommend that you seek independent legal advice relating to your responsibilities under Data Boundary for IL4. Nothing in this document is intended to provide you with or should be used as a substitute for legal advice.

This page describes the set of controls that are applied on Data Boundary for IL4 workloads in Assured Workloads. It provides detailed information about [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency), supported Google Cloud products and their API endpoints, and any applicable restrictions or limitations on those products. The following additional information applies to Data Boundary for IL4:

  * **Data residency** : The Data Boundary for IL4 control package sets data location controls to support [US-only regions](https://docs.cloud.google.com/assured-workloads/docs/locations#americas). For more information, see the Google Cloud-wide organization policy constraints section.
  * **Support** : Technical support services for Data Boundary for IL4 workloads are available with Enhanced or Premium [Cloud Customer Care](https://docs.cloud.google.com/support) subscriptions. Data Boundary for IL4 workloads support cases are routed to US Persons located in the US. For more information, see [Getting support](https://docs.cloud.google.com/assured-workloads/docs/getting-support#il4).
  * **Pricing** : The Data Boundary for IL4 control package is included in Assured Workloads' _Premium tier_ , which incurs an additional 20% charge. For more information, see [Assured Workloads pricing](https://docs.cloud.google.com/assured-workloads/pricing).



## Prerequisites

To remain compliant as a user of the Data Boundary for IL4 control package, verify that you satisfy and adhere to the following prerequisites:

  * Create a Data Boundary for IL4 folder using Assured Workloads and deploy your IL4 workloads only in that folder.
  * Only enable and use in-scope services for Data Boundary for IL4 workloads.
  * Don't use [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) unless otherwise noted. Data Boundary for IL4 doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM page](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page.
  * Don't change the default organization policy constraint values unless you understand and are willing to accept the data residency risks that might occur.
  * For all services used in a Data Boundary for IL4 folder, don't store technical data in the following user-defined or security configuration information types: 
    * Error messages
    * Console output
    * Attribute data
    * Service configuration data
    * Network packet headers
    * Resource identifiers
    * Data labels
  * Consider adopting the general security best practices provided in the [Google Cloud security best practices center](https://cloud.google.com/security/best-practices).
  * Review the [U.S. Department of Defense (DoD) Provisional Authorization](https://cloud.google.com/security/compliance/disa) page for additional information about deploying IL4 workloads in Google Cloud.
  * When accessing the Google Cloud console, you have the option of using the [Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console). You are not required to use the Jurisdictional Google Cloud console for Data Boundary for IL4. It can be accessed at one of the following URLs: 
    * [console.us.cloud.google.com](https://console.us.cloud.google.com)
    * [console.us.cloud.google](https://console.us.cloud.google) for federated identity users



## Supported products and API endpoints

Unless otherwise noted, users can access all supported products through the Google Cloud console. Restrictions or limitations that affect the features of a supported product, including those that are enforced through [organization policy constraint settings](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#how_organization_policy_works), are listed in the following table.

If a product is not listed, that product is unsupported and has not met the control requirements for Data Boundary for IL4. Unsupported products are not recommended for use without due diligence and a thorough understanding of your responsibilities in the [shared responsibility model](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility). Before using an unsupported product, ensure that you are aware of and are willing to accept any associated risks involved, such as negative impacts to data residency or data sovereignty. Additionally, review any usage of an unsupported product with your authorizing agency prior to accepting the risk. 

**Note** : Unsupported products may share an API service endpoint with supported products, making them available to all users.**Important** : [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) aren't supported for any Data Boundary for IL4 products unless otherwise noted. Data Boundary for IL4 doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. It's your responsibility to ensure that Google Cloud MCP servers endpoints aren't used with any Data Boundary for IL4 products. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page. 

Supported product | API endpoints | Restrictions or limitations  
---|---|---  
[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) |  `accesscontextmanager.googleapis.com`  
|  None   
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) |  `alloydb.googleapis.com`  
|  None   
[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) |  `artifactregistry.googleapis.com`  
|  None   
[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) |  `bigquery.googleapis.com`  
`bigqueryconnection.googleapis.com`  
`bigquerydatapolicy.googleapis.com`  
`bigquerymigration.googleapis.com`  
`bigqueryreservation.googleapis.com`  
`bigquerystorage.googleapis.com`  
|  Affected features and organization policy constraints  
[Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) |  `privateca.googleapis.com`  
|  None   
[Cloud Build](https://docs.cloud.google.com/build/docs/overview) |  `cloudbuild.googleapis.com`  
|  None   
[Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) |  `dns.googleapis.com`  
|  None   
[Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview) |  `datafusion.googleapis.com`  
|  None   
[Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) |  `cloudkms.googleapis.com`  
|  None   
[Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) |  `cloudkms.googleapis.com`  
|  None   
[Cloud Identity](https://docs.cloud.google.com/identity) |  `cloudidentity.googleapis.com`  
|  None   
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) |  `compute.googleapis.com`  
|  Affected features  
[Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/key-management-service) |  `cloudkms.googleapis.com`  
|  Organization policy constraints  
[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) |  `logging.googleapis.com`  
`monitoring.googleapis.com`  
|  Affected features  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) |  `monitoring.googleapis.com`  
|  Affected features  
[Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) |  `compute.googleapis.com`  
|  None   
[Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router) |  `compute.googleapis.com`  
|  None   
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) |  `run.googleapis.com`  
|  Affected features  
[Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) |  `sqladmin.googleapis.com`  
|  None   
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) |  `mesh.googleapis.com`  
`meshca.googleapis.com`  
`meshconfig.googleapis.com`  
`trafficdirector.googleapis.com`  
|  None   
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) |  `storage.googleapis.com`  
|  None   
[Cloud Tasks](https://docs.cloud.google.com/tasks/docs/dual-overview) |  `cloudtasks.googleapis.com`  
|  None   
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  `compute.googleapis.com`  
|  Affected features  
[Cloud Vision API](https://docs.cloud.google.com/vision/docs/features-list) |  `vision.googleapis.com`  
|  Affected features  
[Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) |  `workstations.googleapis.com`  
|  Affected features  
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview) |  `compute.googleapis.com`  
|  Affected features and organization policy constraints  
[Google Kubernetes Engine (GKE) Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent) |  `connectgateway.googleapis.com`  
`gkeconnect.googleapis.com`  
|  None   
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) |  `dataflow.googleapis.com`  
`datapipelines.googleapis.com`  
|  None   
[Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) |  `eventarc.googleapis.com`  
|  None   
[External passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) |  `compute.googleapis.com`  
|  None   
[Filestore](https://docs.cloud.google.com/filestore/docs/overview) |  `file.googleapis.com`  
|  None   
[Google Kubernetes Engine (GKE) Hub](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview) |  `gkehub.googleapis.com`  
|  None   
[Google Kubernetes Engine (GKE) Identity Service](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication) |  `anthosidentityservice.googleapis.com`  
|  None   
[Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs) |  `discoveryengine.googleapis.com`  
|  Affected features  
[Generative AI on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview) |  `aiplatform.googleapis.com`  
|  None   
[Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) |  `compute.googleapis.com`  
|  Affected features  
[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) |  `container.googleapis.com`  
`containersecurity.googleapis.com`  
|  None   
[Google Security Operations SIEM](https://docs.cloud.google.com/security/products/security-information-event-management) |  `chronicle.googleapis.com`  
`chronicleservicemanager.googleapis.com`  
|  None   
[Google Security Operations SOAR](https://docs.cloud.google.com/chronicle/docs/soar) |  `Not applicable`  
|  None   
[Google Admin console](https://support.google.com/a/topic/2413312?ref_topic=4388346) |  `Not applicable`  
|  None   
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) |  `iam.googleapis.com`  
`policytroubleshooter.googleapis.com`  
|  None   
[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) |  `iap.googleapis.com`  
|  Affected features  
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) |  `compute.googleapis.com`  
|  None   
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) |  `dataplex.googleapis.com`  
`datalineage.googleapis.com`  
|  Affected features  
[Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview) |  `composer.googleapis.com`  
|  None   
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview) |  `dataproc-control.googleapis.com`  
`dataproc.googleapis.com`  
|  None   
[Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis) |  `redis.googleapis.com`  
|  None   
[Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) |  `networkconnectivity.googleapis.com`  
|  None   
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
[Resource Manager](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview) |  `cloudresourcemanager.googleapis.com`  
|  None   
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) |  `secretmanager.googleapis.com`  
|  None   
[Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) |  `dlp.googleapis.com`  
|  None   
[Spanner](https://docs.cloud.google.com/spanner/docs) |  `spanner.googleapis.com`  
|  None   
[Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/overview) |  `speech.googleapis.com`  
|  Affected features  
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
[Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) |  `compute.googleapis.com`  
`servicenetworking.googleapis.com`  
|  None   
  
## Restrictions and limitations

The following sections describe Google Cloud-wide or product-specific restrictions or limitations for features, including any organization policy constraints that are set by default on Data Boundary for IL4 folders. Other applicable organization policy constraints—even if not set by default—can provide additional defense-in-depth to further protect your organization's Google Cloud resources.

We strongly recommend not changing the values of the required organization policy constraints listed in the following sections. Doing so may undermine data residency. When such a change has been made, the effects of the change are difficult or impossible to reverse. Ensure that you understand the ramifications of changing an organization policy constraint's value before proceeding, and review any such changes with your authorizing agency prior to making the change.   
  
Additionally, ensure that any automated mechanisms your organization uses to manage organization policies are updated to prevent these values from being changed unintentionally.

### Google Cloud-wide

#### Affected Google Cloud-wide features

Feature | Description  
---|---  
Google Cloud console | To access the Google Cloud console when using the Data Boundary for IL4 control package, you have the option of using the [Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console#us). The Jurisdictional Google Cloud console is not required for Data Boundary for IL4, and can be accessed using one of the following URLs:  


  * [console.us.cloud.google.com](https://console.us.cloud.google.com)
  * [console.us.cloud.google](https://console.us.cloud.google) for federated identity users

  
  
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
Compliant BigQuery APIs | The following BigQuery APIs are IL4-compliant:  


  * [`bigquery.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#bigquery-api)
  * [`bigquerydatapolicy.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#data-api)
  * [`bigqueryconnection.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#connection-api)
  * [`bigquerymigration.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#migration-api)
  * [`bigquerystorage.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#storage-api)
  * [`bigqueryreservation.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#reservations-api)
  * [`bigquerydatatransfer.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#dts-api)

The Reservations API is not enabled by default. For more information, see [Enabling an API in your Google Cloud project](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).   
Regions | BigQuery is IL4-compliant for all BigQuery US regions except the US multi-region. IL4 compliance cannot be guaranteed if a dataset is created in a US multi-region, non-US region, or non-US multi-region. It is your responsibility to specify an IL4-compliant region when creating BigQuery datasets.   
Queries on IL4 datasets from non-IL4 projects | BigQuery doesn't prevent IL4 datasets from being queried from non-IL4 projects. Ensure that any query that uses a read or a join operation on IL4 technical data is in an IL4-compliant folder.   
Connections to external data sources |  Google's compliance responsibility is limited to the [BigQuery Connection API](https://docs.cloud.google.com/bigquery/docs/connections-api-intro) capability. It is your responsibility to ensure the compliance of the source products that are used with the BigQuery Connection API.   
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
Loading data | [BigQuery Data Transfer Service connectors](https://docs.cloud.google.com/bigquery/docs/dts-introduction#supported_data_sources) for Google Software as a Service (SaaS) apps, external cloud storage providers, and data warehouses are not supported. It is your responsibility not to use BigQuery Data Transfer Service connectors for Data Boundary for IL4 workloads.   
[Third-party transfers](https://docs.cloud.google.com/bigquery/docs/third-party-transfer) | BigQuery doesn't verify support for third-party transfers for the BigQuery Data Transfer Service. It is your responsibility to verify support when using any third-party transfer for the BigQuery Data Transfer Service.   
Non-compliant BQML models | [Externally-trained BQML models](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#externally_trained_models) are not supported.   
Query jobs | Query jobs should only be created within Assured Workloads folders.   
Queries on datasets in other projects | BigQuery doesn't prevent Assured Workloads datasets from being queried from non-Assured Workloads projects. You should ensure that any query that has a read or a join on Assured Workloads data be placed in Assured Workloads folders. You can specify a [fully-qualified table name](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_query) for their query result using `projectname.dataset.table` in the BigQuery CLI.   
Cloud Logging | BigQuery utilizes Cloud Logging for some of your log data. You should disable your `_default` logging buckets or restrict `_default` buckets to in-scope regions to maintain compliance using the following command:  
  
`gcloud alpha logging settings update --organization=ORGANIZATION_ID --disable-default-sink`   
  
For more information, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).   
  
### Cloud Interconnect

#### Affected Cloud Interconnect features

Feature | Description  
---|---  
High-availability (HA) VPN | You must enable high-availability (HA) VPN functionality when using Cloud Interconnect with Cloud VPN. Additionally, you must adhere to the encryption and regionalization requirements listed in the Affected Cloud VPN features section.   
  
### Cloud KMS

#### Cloud KMS organization policy constraints

Organization policy constraint | Description  
---|---  
`cloudkms.allowedProtectionLevels` | Set to allow creation of Cloud Key Management Service CryptoKeys with the following protection levels:  


  * `SOFTWARE`
  * `HSM`
  * `EXTERNAL`
  * `EXTERNAL_VPC`

See [Protection levels](https://docs.cloud.google.com/kms/docs/algorithms#protection_levels) for more information.   
  
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
IL4-compliant Cloud Vision API endpoints | It is your responsibility to use only the US region API endpoint (`us-vision.googleapis.com`) for the Cloud Vision API. The global endpoint (`vision.googleapis.com`) is not IL4-compliant and using it may undermine your workload's data residency.   
  
### Cloud VPN

#### Affected Cloud VPN features

Feature | Description  
---|---  
VPN endpoints | You must use only Cloud VPN endpoints that are located in an in-scope region. Ensure that your VPN gateway is configured for use in an in-scope region only.   
  
### Cloud Workstations

#### Affected Cloud Workstations features

Feature | Description  
---|---  
Creating a workstation cluster | When creating a workstation cluster, it is your responsibility to configure it in the following way to ensure data residency:

  * Select only a [Private gateway](https://docs.cloud.google.com/workstations/docs/create-cluster#workstation-cluster) when creating a workstation cluster. Using a private gateway provides data residency in transit. 
  * Use only a [regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#load-balancer-mode) when setting up a [custom domain](https://docs.cloud.google.com/workstations/docs/set-up-custom-domains-for-cloud-workstations#neg-published-service). Using a regional external Application Load Balancer provides data residency in transit. 

  
  
### Compute Engine

#### Affected Compute Engine features

Feature | Description  
---|---  
[Adding an instance group to a global load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#global-regional) | You cannot add an instance group to a global load balancer.  
  
This feature is disabled by the `compute.disableGlobalLoadBalancing` organization policy constraint.   
[ Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) | It is possible for scripts, daemons, and binaries that are included with the guest environment to access unencrypted at-rest and in-use data. Depending on your VM configuration, updates to this software may be installed by default. See [Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) for specific information about each package's contents, source code, and more.  
  
These components help you meet data sovereignty through internal security controls and processes. However, if you want additional control, you can also curate your own images or agents and optionally use the `compute.trustedImageProjects` organization policy constraint.   
  
For more information, see [Building a custom image](https://docs.cloud.google.com/compute/docs/images/building-custom-os).   
[ OS policies in VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies) |  Inline scripts and binary output files within the OS policy files are not encrypted using customer-managed encryption keys (CMEK). Don't include any sensitive information in these files. Consider storing these scripts and output files in Cloud Storage buckets. For more information, see [Example OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).  
  
If you want to restrict the creation or modification of OS policy resources that use inline scripts or binary output files, enable the `constraints/osconfig.restrictInlineScriptAndOutputFileUsage` organization policy constraint.  
  
For more information, see [Constraints for OS Config](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).   
`[instances.getSerialPortOutput()](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/getSerialPortOutput)` | This API is disabled. You will be unable to get serial port output from the specified instance using this API.  
  
Change the `compute.disableInstanceDataAccessApis` organization policy constraint value to **False** to enable this API. You can also enable and use the interactive serial port by following the instructions in [Enabling access for a project](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#enable_project_access).   
`[instances.getScreenshot()](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/getScreenshot)` | This API is disabled. You will be unable to get a screenshot from the specified instance using this API.  
  
Change the `compute.disableInstanceDataAccessApis` organization policy constraint value to **False** to enable this API. You can also enable and use the interactive serial port by following the instructions in [Enabling access for a project](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#enable_project_access).   
  
#### Compute Engine organization policy constraints

Organization policy constraint | Description  
---|---  
`compute.disableGlobalCloudArmorPolicy` | Set to **True**.  
  
Disables the creation of new global [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview) and the addition or modification of rules to existing global Google Cloud Armor security policies. This constraint doesn't restrict the removal of rules or the ability to remove or change the description and listing of global Google Cloud Armor security policies. Regional Google Cloud Armor security policies are unaffected by this constraint. All global and regional security policies that exist prior to the enforcement of this constraint remain in effect.  
  
  
`compute.disableGlobalLoadBalancing` | Set to **True**.  
  
Disables creation of global load balancing products.  
  
Changing this value may affect your workload's data residency or data sovereignty.   
`compute.disableInstanceDataAccessApis` | Set to **True**.  
  
Globally disables the `instances.getSerialPortOutput()` and `instances.getScreenshot()` APIs.  
  
Enabling this constraint prevents you from [generating credentials on Windows Server VMs](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials#generate_credentials).   
  
If you need to manage a username and password on a Windows VM, do the following: 

  1. [Enable SSH for Windows VMs](https://docs.cloud.google.com/compute/docs/connect/windows-ssh#enable).
  2. Run the following command to change the VM's password: 
         
         gcloud compute ssh
           VM_NAME --command "net user USERNAME PASSWORD"
           

Replace the following: 
     * VM_NAME: The name of the VM you're setting the password for.
     * USERNAME: The username of the user who you're setting the password for.
     * PASSWORD: The new password.

  
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
[Data insights](https://docs.cloud.google.com/dataplex/docs/data-insights) | This feature is disabled. You cannot generate data insights for your catalogs.  
[Lakes and Zones](https://docs.cloud.google.com/dataplex/docs/metadata) | This feature is disabled. You cannot manage lakes, zones and tasks.  
  
### Gemini Enterprise

#### Gemini Enterprise features

Feature | Description  
---|---  
Web Grounding for Enterprise | Gemini Enterprise includes support for the Web Grounding for Enterprise feature.   
  
### Google Cloud Armor

#### Affected Google Cloud Armor features

Feature | Description  
---|---  
[Globally scoped security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types) | This feature is disabled by the `compute.disableGlobalCloudArmorPolicy` organization policy constraint.   
  
### Identity-Aware Proxy

#### Affected Identity-Aware Proxy features

Feature | Description  
---|---  
[Using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) | It is your responsibility not to use IAP for TCP forwarding because it is not compliant with Data Boundary for IL4.   
  
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
  
### Speech-to-Text

#### Affected Speech-to-Text features

Feature | Description  
---|---  
[Custom Speech-to-Text models](https://docs.cloud.google.com/speech-to-text/v2/docs/custom-speech-models/overview) | It is your responsibility not to use Custom Speech-to-Text models because they are not compliant with Data Boundary for IL4.   
  
## What's next

  * Learn how to [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder)
  * Understand [Assured Workloads pricing](https://docs.cloud.google.com/assured-workloads/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
