---
url: https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar/
title: Data Boundary for International Traffic in Arms Regulations (ITAR) \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:15.866520+00:00
---

# Data Boundary for International Traffic in Arms Regulations (ITAR)  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data Boundary for International Traffic in Arms Regulations (ITAR)

**Important:** Before following the guidance on this page, you should seek independent legal advice relating to your responsibilities under ITAR. Nothing in this document is intended to provide you with or should be used as a substitute for legal advice.

This page describes the set of controls that are applied on ITAR workloads in Assured Workloads. It provides detailed information about [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency), supported Google Cloud products and their API endpoints, and any applicable restrictions or limitations on those products. The following additional information applies to ITAR:

  * **Data residency** : The ITAR control package sets data location controls to support [US-only regions](https://docs.cloud.google.com/assured-workloads/docs/locations#americas). See the Google Cloud-wide organization policy constraints section for more information.
  * **Support** : Technical support services for ITAR workloads are available with Enhanced or Premium [Cloud Customer Care](https://docs.cloud.google.com/support) subscriptions. ITAR workloads support cases are routed to US Persons located in the US. For more information, see [Getting support](https://docs.cloud.google.com/assured-workloads/docs/getting-support#itar).
  * **Pricing** : The ITAR control package is included in Assured Workloads' _Premium tier_ , which incurs an 20% additional charge. See [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing) for more information.



## Prerequisites

To remain compliant as a user of the ITAR control package, verify that you satisfy and adhere to the following prerequisites:

  * Create an ITAR folder using Assured Workloads and deploy your ITAR workloads only in that folder.
  * Only enable and use in-scope ITAR services for ITAR workloads.
  * Don't use [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) unless otherwise noted. ITAR doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM page](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page.
  * Don't change the default organization policy constraint values unless you understand and are willing to accept the data residency risks that might occur.
  * When accessing the Google Cloud console for ITAR workloads, you must use one of the following [Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console) URLs: 
    * [console.us.cloud.google.com](https://console.us.cloud.google.com)
    * [console.us.cloud.google](https://console.us.cloud.google) for federated identity users
  * When connecting to Google Cloud service endpoints, you must use [regional endpoints](https://docs.cloud.google.com/assured-workloads/docs/api-endpoints) for services that offer them. In addition: 
    * When connecting to Google Cloud service endpoints from non-Google Cloud VMs —such as on-premises or other cloud providers' VMs— you must use one of the available [private access options](https://docs.cloud.google.com/vpc/docs/private-access-options#connect-google-apis) that support connections to non-Google Cloud VMs to route the non-Google Cloud traffic into Google Cloud.
    * When connecting to Google Cloud service endpoints from Google Cloud VMs, you can use any of the available [private access options](https://docs.cloud.google.com/vpc/docs/private-access-options#connect-google-apis).
    * When connecting to Google Cloud VMs that have been exposed with external IP addresses, refer to [Access APIs from VMs with external IP addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip).
  * For all services used in an ITAR folder, don't store technical data in the following user-defined or security configuration information types: 
    * Error messages
    * Console output
    * Attribute data
    * Service configuration data
    * Network packet headers
    * Resource identifiers
    * Data labels
  * Use only the specified regional endpoints for services that offer them. For more information, see in-scope ITAR services.
  * Consider adopting the general security best practices provided in the [Google Cloud security best practices center](https://cloud.google.com/security/best-practices).



## Supported products and API endpoints

Unless otherwise noted, users can access all supported products through the Google Cloud console. Restrictions or limitations that affect the features of a supported product, including those that are enforced through [organization policy constraint settings](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#how_organization_policy_works), are listed in the following table.

If a product is not listed, that product is unsupported and has not met the control requirements for ITAR. Unsupported products are not recommended for use without due diligence and a thorough understanding of your responsibilities in the [shared responsibility model](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility). Before using an unsupported product, ensure that you are aware of and are willing to accept any associated risks involved, such as negative impacts to data residency or data sovereignty. 

**Note** : Unsupported products may share an API service endpoint with supported products, making them available to all users.**Important** : [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) aren't supported for any ITAR products unless otherwise noted. ITAR doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. It's your responsibility to ensure that Google Cloud MCP servers endpoints aren't used with any ITAR products. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page. 

Services that interact with Customer Data in their API operations provide [regional API endpoints](https://docs.cloud.google.com/docs/security/compliance/endpoints#regional-endpoints). Use these endpoints instead of the service's [global API endpoint](https://docs.cloud.google.com/docs/security/compliance/endpoints#global-endpoints) to maintain ITAR compliance. For services whose API operations aren't intended to interact with Customer Data, global API endpoints are available. It's your responsibility to ensure that you don't transmit ITAR-regulated technical data through these global API endpoints. See [Data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) for more information about Customer Data and Service Data.

### Supported products with regional API endpoints

A list of supported products and their [regional API endpoints](https://docs.cloud.google.com/docs/security/compliance/endpoints#regional-endpoints) is provided in the following table. These API endpoints are designed to process and transmit Customer Data. To support your ITAR compliance requirements when using these products, you must use an available regional API endpoint instead of a global API endpoint.

Supported product | Regional API endpoints | Restrictions or limitations  
---|---|---  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) | 

`alloydb.us-central1.rep.googleapis.com`  
`alloydb.us-central2.rep.googleapis.com`  
`alloydb.us-east1.rep.googleapis.com`  
`alloydb.us-east4.rep.googleapis.com`  
`alloydb.us-east5.rep.googleapis.com`  
`alloydb.us-east7.rep.googleapis.com`  
`alloydb.us-south1.rep.googleapis.com`  
`alloydb.us-west1.rep.googleapis.com`  
`alloydb.us-west2.rep.googleapis.com`  
`alloydb.us-west3.rep.googleapis.com`  
`alloydb.us-west4.rep.googleapis.com`  

  
|  None   
[Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) | 

`apigee.us.rep.googleapis.com`  

  
|  None   
[Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) | 

`containeranalysis.us.rep.googleapis.com`  
`containeranalysis.us-central1.rep.googleapis.com`  
`containeranalysis.us-central2.rep.googleapis.com`  
`containeranalysis.us-east1.rep.googleapis.com`  
`containeranalysis.us-east4.rep.googleapis.com`  
`containeranalysis.us-east5.rep.googleapis.com`  
`containeranalysis.us-east7.rep.googleapis.com`  
`containeranalysis.us-south1.rep.googleapis.com`  
`containeranalysis.us-west1.rep.googleapis.com`  
`containeranalysis.us-west2.rep.googleapis.com`  
`containeranalysis.us-west3.rep.googleapis.com`  
`containeranalysis.us-west4.rep.googleapis.com`  

  
|  None   
[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) | 

`artifactregistry.us.rep.googleapis.com`  
`artifactregistry.us-central1.rep.googleapis.com`  
`artifactregistry.us-central2.rep.googleapis.com`  
`artifactregistry.us-east1.rep.googleapis.com`  
`artifactregistry.us-east4.rep.googleapis.com`  
`artifactregistry.us-east5.rep.googleapis.com`  
`artifactregistry.us-east7.rep.googleapis.com`  
`artifactregistry.us-south1.rep.googleapis.com`  
`artifactregistry.us-west1.rep.googleapis.com`  
`artifactregistry.us-west2.rep.googleapis.com`  
`artifactregistry.us-west3.rep.googleapis.com`  
`artifactregistry.us-west4.rep.googleapis.com`  
`artifactregistry.us-west8.rep.googleapis.com`  

  
|  None   
[Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) | 

`backupdr.us.rep.googleapis.com`  
`backupdr.us-central1.rep.googleapis.com`  
`backupdr.us-central2.rep.googleapis.com`  
`backupdr.us-east1.rep.googleapis.com`  
`backupdr.us-east4.rep.googleapis.com`  
`backupdr.us-east5.rep.googleapis.com`  
`backupdr.us-east7.rep.googleapis.com`  
`backupdr.us-south1.rep.googleapis.com`  
`backupdr.us-west1.rep.googleapis.com`  
`backupdr.us-west2.rep.googleapis.com`  
`backupdr.us-west3.rep.googleapis.com`  
`backupdr.us-west4.rep.googleapis.com`  
`backupdr.us-west8.rep.googleapis.com`  

  
|  None   
[Backup for Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke) | 

`gkebackup.us-central1.rep.googleapis.com`  
`gkebackup.us-east1.rep.googleapis.com`  
`gkebackup.us-east4.rep.googleapis.com`  
`gkebackup.us-east5.rep.googleapis.com`  
`gkebackup.us-east7.rep.googleapis.com`  
`gkebackup.us-south1.rep.googleapis.com`  
`gkebackup.us-west1.rep.googleapis.com`  
`gkebackup.us-west2.rep.googleapis.com`  
`gkebackup.us-west3.rep.googleapis.com`  
`gkebackup.us-west4.rep.googleapis.com`  
`gkebackup.us-west8.rep.googleapis.com`  

  
|  None   
[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) | 

`bigquery.us-central1.rep.googleapis.com`  
`bigquery.us-central2.rep.googleapis.com`  
`bigquery.us-east1.rep.googleapis.com`  
`bigquery.us-east4.rep.googleapis.com`  
`bigquery.us-east5.rep.googleapis.com`  
`bigquery.us-east7.rep.googleapis.com`  
`bigquery.us-south1.rep.googleapis.com`  
`bigquery.us-west1.rep.googleapis.com`  
`bigquery.us-west2.rep.googleapis.com`  
`bigquery.us-west3.rep.googleapis.com`  
`bigquery.us-west4.rep.googleapis.com`  
`bigquery.us-west8.rep.googleapis.com`  
`bigquerymigration.us-central1.rep.googleapis.com`  
`bigquerymigration.us-central2.rep.googleapis.com`  
`bigquerymigration.us-east1.rep.googleapis.com`  
`bigquerymigration.us-east4.rep.googleapis.com`  
`bigquerymigration.us-east5.rep.googleapis.com`  
`bigquerymigration.us-east7.rep.googleapis.com`  
`bigquerymigration.us-south1.rep.googleapis.com`  
`bigquerymigration.us-west1.rep.googleapis.com`  
`bigquerymigration.us-west2.rep.googleapis.com`  
`bigquerymigration.us-west3.rep.googleapis.com`  
`bigquerymigration.us-west4.rep.googleapis.com`  
`bigquerymigration.us-west8.rep.googleapis.com`  
`bigqueryreservation.us-central1.rep.googleapis.com`  
`bigqueryreservation.us-central2.rep.googleapis.com`  
`bigqueryreservation.us-east1.rep.googleapis.com`  
`bigqueryreservation.us-east4.rep.googleapis.com`  
`bigqueryreservation.us-east5.rep.googleapis.com`  
`bigqueryreservation.us-east7.rep.googleapis.com`  
`bigqueryreservation.us-south1.rep.googleapis.com`  
`bigqueryreservation.us-west1.rep.googleapis.com`  
`bigqueryreservation.us-west2.rep.googleapis.com`  
`bigqueryreservation.us-west3.rep.googleapis.com`  
`bigqueryreservation.us-west4.rep.googleapis.com`  
`bigqueryreservation.us-west8.rep.googleapis.com`  
`bigquerystorage.us-central1.rep.googleapis.com`  
`bigquerystorage.us-central2.rep.googleapis.com`  
`bigquerystorage.us-east1.rep.googleapis.com`  
`bigquerystorage.us-east4.rep.googleapis.com`  
`bigquerystorage.us-east5.rep.googleapis.com`  
`bigquerystorage.us-east7.rep.googleapis.com`  
`bigquerystorage.us-south1.rep.googleapis.com`  
`bigquerystorage.us-west1.rep.googleapis.com`  
`bigquerystorage.us-west2.rep.googleapis.com`  
`bigquerystorage.us-west3.rep.googleapis.com`  
`bigquerystorage.us-west4.rep.googleapis.com`  
`bigquerystorage.us-west8.rep.googleapis.com`  

  
|  Affected features  
[BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) | 

`bigquerydatatransfer.us-central1.rep.googleapis.com`  
`bigquerydatatransfer.us-central2.rep.googleapis.com`  
`bigquerydatatransfer.us-east1.rep.googleapis.com`  
`bigquerydatatransfer.us-east4.rep.googleapis.com`  
`bigquerydatatransfer.us-east5.rep.googleapis.com`  
`bigquerydatatransfer.us-east7.rep.googleapis.com`  
`bigquerydatatransfer.us-south1.rep.googleapis.com`  
`bigquerydatatransfer.us-west1.rep.googleapis.com`  
`bigquerydatatransfer.us-west2.rep.googleapis.com`  
`bigquerydatatransfer.us-west3.rep.googleapis.com`  
`bigquerydatatransfer.us-west4.rep.googleapis.com`  
`bigquerydatatransfer.us-west8.rep.googleapis.com`  

  
|  None   
[Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) | 

`bigtable.us-central1.rep.googleapis.com`  
`bigtable.us-central2.rep.googleapis.com`  
`bigtable.us-east1.rep.googleapis.com`  
`bigtable.us-east4.rep.googleapis.com`  
`bigtable.us-east5.rep.googleapis.com`  
`bigtable.us-east7.rep.googleapis.com`  
`bigtable.us-south1.rep.googleapis.com`  
`bigtable.us-west1.rep.googleapis.com`  
`bigtable.us-west2.rep.googleapis.com`  
`bigtable.us-west3.rep.googleapis.com`  
`bigtable.us-west4.rep.googleapis.com`  
`bigtable.us-west8.rep.googleapis.com`  

  
|  None   
[Cloud Build](https://docs.cloud.google.com/build/docs/overview) | 

`cloudbuild.us-central1.rep.googleapis.com`  
`cloudbuild.us-central2.rep.googleapis.com`  
`cloudbuild.us-east1.rep.googleapis.com`  
`cloudbuild.us-east4.rep.googleapis.com`  
`cloudbuild.us-east5.rep.googleapis.com`  
`cloudbuild.us-east7.rep.googleapis.com`  
`cloudbuild.us-south1.rep.googleapis.com`  
`cloudbuild.us-west1.rep.googleapis.com`  
`cloudbuild.us-west2.rep.googleapis.com`  
`cloudbuild.us-west3.rep.googleapis.com`  
`cloudbuild.us-west4.rep.googleapis.com`  
`cloudbuild.us-west8.rep.googleapis.com`  

  
|  None   
[Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) | 

`clouddeploy.us-central1.rep.googleapis.com`  
`clouddeploy.us-east1.rep.googleapis.com`  
`clouddeploy.us-east4.rep.googleapis.com`  
`clouddeploy.us-east5.rep.googleapis.com`  
`clouddeploy.us-east7.rep.googleapis.com`  
`clouddeploy.us-south1.rep.googleapis.com`  
`clouddeploy.us-west1.rep.googleapis.com`  
`clouddeploy.us-west2.rep.googleapis.com`  
`clouddeploy.us-west3.rep.googleapis.com`  
`clouddeploy.us-west4.rep.googleapis.com`  

  
|  None   
[Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) | 

`cloudkms.us.rep.googleapis.com`  
`cloudkms.us-central1.rep.googleapis.com`  
`cloudkms.us-central2.rep.googleapis.com`  
`cloudkms.us-east1.rep.googleapis.com`  
`cloudkms.us-east4.rep.googleapis.com`  
`cloudkms.us-east5.rep.googleapis.com`  
`cloudkms.us-east7.rep.googleapis.com`  
`cloudkms.us-south1.rep.googleapis.com`  
`cloudkms.us-west1.rep.googleapis.com`  
`cloudkms.us-west2.rep.googleapis.com`  
`cloudkms.us-west3.rep.googleapis.com`  
`cloudkms.us-west4.rep.googleapis.com`  
`cloudkms.us-west8.rep.googleapis.com`  

  
|  None   
[Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) | 

`cloudkms.us.rep.googleapis.com`  
`cloudkms.us-central1.rep.googleapis.com`  
`cloudkms.us-central2.rep.googleapis.com`  
`cloudkms.us-east1.rep.googleapis.com`  
`cloudkms.us-east4.rep.googleapis.com`  
`cloudkms.us-east5.rep.googleapis.com`  
`cloudkms.us-east7.rep.googleapis.com`  
`cloudkms.us-south1.rep.googleapis.com`  
`cloudkms.us-west1.rep.googleapis.com`  
`cloudkms.us-west2.rep.googleapis.com`  
`cloudkms.us-west3.rep.googleapis.com`  
`cloudkms.us-west4.rep.googleapis.com`  
`cloudkms.us-west8.rep.googleapis.com`  

  
|  None   
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/key-management-service) | 

`cloudkms.us.rep.googleapis.com`  
`cloudkms.us-central1.rep.googleapis.com`  
`cloudkms.us-central2.rep.googleapis.com`  
`cloudkms.us-east1.rep.googleapis.com`  
`cloudkms.us-east4.rep.googleapis.com`  
`cloudkms.us-east5.rep.googleapis.com`  
`cloudkms.us-east7.rep.googleapis.com`  
`cloudkms.us-south1.rep.googleapis.com`  
`cloudkms.us-west1.rep.googleapis.com`  
`cloudkms.us-west2.rep.googleapis.com`  
`cloudkms.us-west3.rep.googleapis.com`  
`cloudkms.us-west4.rep.googleapis.com`  
`cloudkms.us-west8.rep.googleapis.com`  

  
|  None   
[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) | 

`logging.us.rep.googleapis.com`  
`logging.us-central1.rep.googleapis.com`  
`logging.us-central2.rep.googleapis.com`  
`logging.us-east1.rep.googleapis.com`  
`logging.us-east4.rep.googleapis.com`  
`logging.us-east5.rep.googleapis.com`  
`logging.us-east7.rep.googleapis.com`  
`logging.us-south1.rep.googleapis.com`  
`logging.us-west1.rep.googleapis.com`  
`logging.us-west2.rep.googleapis.com`  
`logging.us-west3.rep.googleapis.com`  
`logging.us-west4.rep.googleapis.com`  
`logging.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) | 

`run.us-central1.rep.googleapis.com`  
`run.us-central2.rep.googleapis.com`  
`run.us-east1.rep.googleapis.com`  
`run.us-east4.rep.googleapis.com`  
`run.us-east5.rep.googleapis.com`  
`run.us-east7.rep.googleapis.com`  
`run.us-south1.rep.googleapis.com`  
`run.us-west1.rep.googleapis.com`  
`run.us-west2.rep.googleapis.com`  
`run.us-west3.rep.googleapis.com`  
`run.us-west4.rep.googleapis.com`  
`run.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) | 

`sqladmin.us-central1.rep.googleapis.com`  
`sqladmin.us-central2.rep.googleapis.com`  
`sqladmin.us-east1.rep.googleapis.com`  
`sqladmin.us-east4.rep.googleapis.com`  
`sqladmin.us-east5.rep.googleapis.com`  
`sqladmin.us-east7.rep.googleapis.com`  
`sqladmin.us-south1.rep.googleapis.com`  
`sqladmin.us-west1.rep.googleapis.com`  
`sqladmin.us-west2.rep.googleapis.com`  
`sqladmin.us-west3.rep.googleapis.com`  
`sqladmin.us-west4.rep.googleapis.com`  
`sqladmin.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) | 

`trafficdirector.us-central1.rep.googleapis.com`  
`trafficdirector.us-central2.rep.googleapis.com`  
`trafficdirector.us-east1.rep.googleapis.com`  
`trafficdirector.us-east4.rep.googleapis.com`  
`trafficdirector.us-east5.rep.googleapis.com`  
`trafficdirector.us-east7.rep.googleapis.com`  
`trafficdirector.us-south1.rep.googleapis.com`  
`trafficdirector.us-west1.rep.googleapis.com`  
`trafficdirector.us-west2.rep.googleapis.com`  
`trafficdirector.us-west3.rep.googleapis.com`  
`trafficdirector.us-west4.rep.googleapis.com`  
`trafficdirector.us-west8.rep.googleapis.com`  

  
|  None   
[Spanner](https://docs.cloud.google.com/spanner/docs) | 

`spanner.us.rep.googleapis.com`  
`spanner.us-central1.rep.googleapis.com`  
`spanner.us-central2.rep.googleapis.com`  
`spanner.us-east1.rep.googleapis.com`  
`spanner.us-east4.rep.googleapis.com`  
`spanner.us-east5.rep.googleapis.com`  
`spanner.us-east7.rep.googleapis.com`  
`spanner.us-south1.rep.googleapis.com`  
`spanner.us-west1.rep.googleapis.com`  
`spanner.us-west2.rep.googleapis.com`  
`spanner.us-west3.rep.googleapis.com`  
`spanner.us-west4.rep.googleapis.com`  
`spanner.us-west8.rep.googleapis.com`  

  
|  Affected features and organization policy constraints  
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) | 

`storage.us.rep.googleapis.com`  
`storage.us-central1.rep.googleapis.com`  
`storage.us-central2.rep.googleapis.com`  
`storage.us-east1.rep.googleapis.com`  
`storage.us-east4.rep.googleapis.com`  
`storage.us-east5.rep.googleapis.com`  
`storage.us-east7.rep.googleapis.com`  
`storage.us-south1.rep.googleapis.com`  
`storage.us-west1.rep.googleapis.com`  
`storage.us-west2.rep.googleapis.com`  
`storage.us-west3.rep.googleapis.com`  
`storage.us-west4.rep.googleapis.com`  
`storage.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  Affected features and organization policy constraints  
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) | 

`dataflow.us-central1.rep.googleapis.com`  
`dataflow.us-central2.rep.googleapis.com`  
`dataflow.us-east1.rep.googleapis.com`  
`dataflow.us-east4.rep.googleapis.com`  
`dataflow.us-east5.rep.googleapis.com`  
`dataflow.us-east7.rep.googleapis.com`  
`dataflow.us-south1.rep.googleapis.com`  
`dataflow.us-west1.rep.googleapis.com`  
`dataflow.us-west2.rep.googleapis.com`  
`dataflow.us-west3.rep.googleapis.com`  
`dataflow.us-west4.rep.googleapis.com`  
`dataflow.us-west8.rep.googleapis.com`  

  
|  None   
[Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) | 

`eventarc.us.rep.googleapis.com`  
`eventarc.us-central1.rep.googleapis.com`  
`eventarc.us-central2.rep.googleapis.com`  
`eventarc.us-east1.rep.googleapis.com`  
`eventarc.us-east4.rep.googleapis.com`  
`eventarc.us-east5.rep.googleapis.com`  
`eventarc.us-east7.rep.googleapis.com`  
`eventarc.us-south1.rep.googleapis.com`  
`eventarc.us-west1.rep.googleapis.com`  
`eventarc.us-west2.rep.googleapis.com`  
`eventarc.us-west3.rep.googleapis.com`  
`eventarc.us-west4.rep.googleapis.com`  
`eventarc.us-west8.rep.googleapis.com`  

  
|  None   
[External passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  None   
[Filestore](https://docs.cloud.google.com/filestore/docs/overview) | 

`file.us-central1.rep.googleapis.com`  
`file.us-central2.rep.googleapis.com`  
`file.us-east1.rep.googleapis.com`  
`file.us-east4.rep.googleapis.com`  
`file.us-east5.rep.googleapis.com`  
`file.us-east7.rep.googleapis.com`  
`file.us-south1.rep.googleapis.com`  
`file.us-west1.rep.googleapis.com`  
`file.us-west2.rep.googleapis.com`  
`file.us-west3.rep.googleapis.com`  
`file.us-west4.rep.googleapis.com`  
`file.us-west8.rep.googleapis.com`  

  
|  None   
[Firestore](https://docs.cloud.google.com/firestore/native/docs/overview) | 

`datastore.us.rep.googleapis.com`  
`datastore.us-central1.rep.googleapis.com`  
`datastore.us-east1.rep.googleapis.com`  
`datastore.us-east4.rep.googleapis.com`  
`datastore.us-east5.rep.googleapis.com`  
`datastore.us-east7.rep.googleapis.com`  
`datastore.us-south1.rep.googleapis.com`  
`datastore.us-west1.rep.googleapis.com`  
`datastore.us-west2.rep.googleapis.com`  
`datastore.us-west3.rep.googleapis.com`  
`datastore.us-west4.rep.googleapis.com`  
`datastore.us-west8.rep.googleapis.com`  
`firestore.us.rep.googleapis.com`  
`firestore.us-central1.rep.googleapis.com`  
`firestore.us-east1.rep.googleapis.com`  
`firestore.us-east4.rep.googleapis.com`  
`firestore.us-east5.rep.googleapis.com`  
`firestore.us-east7.rep.googleapis.com`  
`firestore.us-south1.rep.googleapis.com`  
`firestore.us-west1.rep.googleapis.com`  
`firestore.us-west2.rep.googleapis.com`  
`firestore.us-west3.rep.googleapis.com`  
`firestore.us-west4.rep.googleapis.com`  
`firestore.us-west8.rep.googleapis.com`  

  
|  Organization policy constraints  
[Google Kubernetes Engine (GKE) Hub (fleets)](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview) | 

`gkehub.us-central1.rep.googleapis.com`  
`gkehub.us-central2.rep.googleapis.com`  
`gkehub.us-east1.rep.googleapis.com`  
`gkehub.us-east4.rep.googleapis.com`  
`gkehub.us-east5.rep.googleapis.com`  
`gkehub.us-east7.rep.googleapis.com`  
`gkehub.us-south1.rep.googleapis.com`  
`gkehub.us-west1.rep.googleapis.com`  
`gkehub.us-west2.rep.googleapis.com`  
`gkehub.us-west3.rep.googleapis.com`  
`gkehub.us-west4.rep.googleapis.com`  
`gkehub.us-west8.rep.googleapis.com`  

  
|  None   
[Generative AI on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/overview) | 

`aiplatform.us.rep.googleapis.com`  

  
|  Organization policy constraints  
[Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  Affected features  
[Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview) | 

`managedkafka.us-central1.rep.googleapis.com`  
`managedkafka.us-east1.rep.googleapis.com`  
`managedkafka.us-east4.rep.googleapis.com`  
`managedkafka.us-east5.rep.googleapis.com`  
`managedkafka.us-east7.rep.googleapis.com`  
`managedkafka.us-south1.rep.googleapis.com`  
`managedkafka.us-west1.rep.googleapis.com`  
`managedkafka.us-west2.rep.googleapis.com`  
`managedkafka.us-west3.rep.googleapis.com`  
`managedkafka.us-west4.rep.googleapis.com`  

  
|  None   
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  None   
[Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) | 

`cloudkms.us.rep.googleapis.com`  
`cloudkms.us-central1.rep.googleapis.com`  
`cloudkms.us-central2.rep.googleapis.com`  
`cloudkms.us-east1.rep.googleapis.com`  
`cloudkms.us-east4.rep.googleapis.com`  
`cloudkms.us-east5.rep.googleapis.com`  
`cloudkms.us-east7.rep.googleapis.com`  
`cloudkms.us-south1.rep.googleapis.com`  
`cloudkms.us-west1.rep.googleapis.com`  
`cloudkms.us-west2.rep.googleapis.com`  
`cloudkms.us-west3.rep.googleapis.com`  
`cloudkms.us-west4.rep.googleapis.com`  
`cloudkms.us-west8.rep.googleapis.com`  

  
|  None   
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) | 

`dataplex.us.rep.googleapis.com`  
`dataplex.us-central1.rep.googleapis.com`  
`dataplex.us-central2.rep.googleapis.com`  
`dataplex.us-east1.rep.googleapis.com`  
`dataplex.us-east4.rep.googleapis.com`  
`dataplex.us-east5.rep.googleapis.com`  
`dataplex.us-east7.rep.googleapis.com`  
`dataplex.us-south1.rep.googleapis.com`  
`dataplex.us-west1.rep.googleapis.com`  
`dataplex.us-west2.rep.googleapis.com`  
`dataplex.us-west3.rep.googleapis.com`  
`dataplex.us-west4.rep.googleapis.com`  
`dataplex.us-west8.rep.googleapis.com`  
`datalineage.us.rep.googleapis.com`  
`datalineage.us-central1.rep.googleapis.com`  
`datalineage.us-central2.rep.googleapis.com`  
`datalineage.us-east1.rep.googleapis.com`  
`datalineage.us-east4.rep.googleapis.com`  
`datalineage.us-east5.rep.googleapis.com`  
`datalineage.us-east7.rep.googleapis.com`  
`datalineage.us-south1.rep.googleapis.com`  
`datalineage.us-west1.rep.googleapis.com`  
`datalineage.us-west2.rep.googleapis.com`  
`datalineage.us-west3.rep.googleapis.com`  
`datalineage.us-west4.rep.googleapis.com`  

  
|  Affected features  
[Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) | 

`looker.us-central1.rep.googleapis.com`  
`looker.us-east1.rep.googleapis.com`  
`looker.us-east4.rep.googleapis.com`  
`looker.us-east5.rep.googleapis.com`  
`looker.us-east7.rep.googleapis.com`  
`looker.us-south1.rep.googleapis.com`  
`looker.us-west1.rep.googleapis.com`  
`looker.us-west2.rep.googleapis.com`  
`looker.us-west3.rep.googleapis.com`  
`looker.us-west4.rep.googleapis.com`  

  
|  None   
[Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview) | 

`composer.us-central1.rep.googleapis.com`  
`composer.us-east1.rep.googleapis.com`  
`composer.us-east4.rep.googleapis.com`  
`composer.us-east5.rep.googleapis.com`  
`composer.us-east7.rep.googleapis.com`  
`composer.us-south1.rep.googleapis.com`  
`composer.us-west1.rep.googleapis.com`  
`composer.us-west2.rep.googleapis.com`  
`composer.us-west3.rep.googleapis.com`  
`composer.us-west4.rep.googleapis.com`  

  
|  None   
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview) | 

`dataproc-control.us-central1.rep.googleapis.com`  
`dataproc-control.us-central2.rep.googleapis.com`  
`dataproc-control.us-east1.rep.googleapis.com`  
`dataproc-control.us-east4.rep.googleapis.com`  
`dataproc-control.us-east5.rep.googleapis.com`  
`dataproc-control.us-east7.rep.googleapis.com`  
`dataproc-control.us-south1.rep.googleapis.com`  
`dataproc-control.us-west1.rep.googleapis.com`  
`dataproc-control.us-west2.rep.googleapis.com`  
`dataproc-control.us-west3.rep.googleapis.com`  
`dataproc-control.us-west4.rep.googleapis.com`  
`dataproc-control.us-west8.rep.googleapis.com`  
`dataproc.us-central1.rep.googleapis.com`  
`dataproc.us-central2.rep.googleapis.com`  
`dataproc.us-east1.rep.googleapis.com`  
`dataproc.us-east4.rep.googleapis.com`  
`dataproc.us-east5.rep.googleapis.com`  
`dataproc.us-east7.rep.googleapis.com`  
`dataproc.us-south1.rep.googleapis.com`  
`dataproc.us-west1.rep.googleapis.com`  
`dataproc.us-west2.rep.googleapis.com`  
`dataproc.us-west3.rep.googleapis.com`  
`dataproc.us-west4.rep.googleapis.com`  
`dataproc.us-west8.rep.googleapis.com`  

  
|  None   
[Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis) | 

`redis.us-central1.rep.googleapis.com`  
`redis.us-central2.rep.googleapis.com`  
`redis.us-east1.rep.googleapis.com`  
`redis.us-east4.rep.googleapis.com`  
`redis.us-east5.rep.googleapis.com`  
`redis.us-east7.rep.googleapis.com`  
`redis.us-south1.rep.googleapis.com`  
`redis.us-west1.rep.googleapis.com`  
`redis.us-west2.rep.googleapis.com`  
`redis.us-west3.rep.googleapis.com`  
`redis.us-west4.rep.googleapis.com`  
`redis.us-west8.rep.googleapis.com`  

  
|  None   
[Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  None   
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) | 

`pubsub.us-central1.rep.googleapis.com`  
`pubsub.us-central2.rep.googleapis.com`  
`pubsub.us-east1.rep.googleapis.com`  
`pubsub.us-east4.rep.googleapis.com`  
`pubsub.us-east5.rep.googleapis.com`  
`pubsub.us-east7.rep.googleapis.com`  
`pubsub.us-south1.rep.googleapis.com`  
`pubsub.us-west1.rep.googleapis.com`  
`pubsub.us-west2.rep.googleapis.com`  
`pubsub.us-west3.rep.googleapis.com`  
`pubsub.us-west4.rep.googleapis.com`  
`pubsub.us-west8.rep.googleapis.com`  

  
|  Organization policy constraints  
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#regional-td) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  None   
[Regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp#regional-external-proxy-network-load-balancer) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  None   
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  None   
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp#regional-internal-proxy-network-load-balancer) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  None   
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) | 

`secretmanager.us.rep.googleapis.com`  
`secretmanager.us-central1.rep.googleapis.com`  
`secretmanager.us-central2.rep.googleapis.com`  
`secretmanager.us-east1.rep.googleapis.com`  
`secretmanager.us-east4.rep.googleapis.com`  
`secretmanager.us-east5.rep.googleapis.com`  
`secretmanager.us-east7.rep.googleapis.com`  
`secretmanager.us-south1.rep.googleapis.com`  
`secretmanager.us-west1.rep.googleapis.com`  
`secretmanager.us-west2.rep.googleapis.com`  
`secretmanager.us-west3.rep.googleapis.com`  
`secretmanager.us-west4.rep.googleapis.com`  

  
|  None   
[Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview) | 

`securesourcemanager.us-central1.rep.googleapis.com`  
`securesourcemanager.us-east1.rep.googleapis.com`  
`securesourcemanager.us-east4.rep.googleapis.com`  
`securesourcemanager.us-east7.rep.googleapis.com`  
`securesourcemanager.us-west2.rep.googleapis.com`  

  
|  None   
[Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) | 

`securitycenter.us.rep.googleapis.com`  

  
|  Affected features  
[Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) | 

`dlp.us.rep.googleapis.com`  
`dlp.us-central1.rep.googleapis.com`  
`dlp.us-central2.rep.googleapis.com`  
`dlp.us-east1.rep.googleapis.com`  
`dlp.us-east4.rep.googleapis.com`  
`dlp.us-east5.rep.googleapis.com`  
`dlp.us-south1.rep.googleapis.com`  
`dlp.us-west1.rep.googleapis.com`  
`dlp.us-west2.rep.googleapis.com`  
`dlp.us-west3.rep.googleapis.com`  
`dlp.us-west4.rep.googleapis.com`  
`dlp.us-west8.rep.googleapis.com`  

  
|  None   
[Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) | 

`servicedirectory.us-central1.rep.googleapis.com`  
`servicedirectory.us-central2.rep.googleapis.com`  
`servicedirectory.us-east1.rep.googleapis.com`  
`servicedirectory.us-east4.rep.googleapis.com`  
`servicedirectory.us-east5.rep.googleapis.com`  
`servicedirectory.us-east7.rep.googleapis.com`  
`servicedirectory.us-south1.rep.googleapis.com`  
`servicedirectory.us-west1.rep.googleapis.com`  
`servicedirectory.us-west2.rep.googleapis.com`  
`servicedirectory.us-west3.rep.googleapis.com`  
`servicedirectory.us-west4.rep.googleapis.com`  
`servicedirectory.us-west8.rep.googleapis.com`  

  
|  None   
[Vertex AI Online prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-online-predictions) | 

`aiplatform.us.rep.googleapis.com`  

  
|  Organization policy constraints  
[VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/overview) | 

`osconfig.us-central1.rep.googleapis.com`  
`osconfig.us-central2.rep.googleapis.com`  
`osconfig.us-east1.rep.googleapis.com`  
`osconfig.us-east4.rep.googleapis.com`  
`osconfig.us-east5.rep.googleapis.com`  
`osconfig.us-east7.rep.googleapis.com`  
`osconfig.us-south1.rep.googleapis.com`  
`osconfig.us-west1.rep.googleapis.com`  
`osconfig.us-west2.rep.googleapis.com`  
`osconfig.us-west3.rep.googleapis.com`  
`osconfig.us-west4.rep.googleapis.com`  
`osconfig.us-west8.rep.googleapis.com`  

  
|  None   
[Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) | 

`compute.us-central1.rep.googleapis.com`  
`compute.us-central2.rep.googleapis.com`  
`compute.us-east1.rep.googleapis.com`  
`compute.us-east4.rep.googleapis.com`  
`compute.us-east5.rep.googleapis.com`  
`compute.us-east7.rep.googleapis.com`  
`compute.us-south1.rep.googleapis.com`  
`compute.us-west1.rep.googleapis.com`  
`compute.us-west2.rep.googleapis.com`  
`compute.us-west3.rep.googleapis.com`  
`compute.us-west4.rep.googleapis.com`  
`compute.us-west8.rep.googleapis.com`  

  
|  Affected features  
  
### Supported products with global API endpoints

A list of supported products and their [global API endpoints](https://docs.cloud.google.com/docs/security/compliance/endpoints#global-endpoints) is provided in the following table. These global API endpoints are designed to process Service Data, such as configuration data, metadata, or resource identifiers, and aren't intended for handling Customer Data. It's your responsibility to ensure that you don't transmit ITAR-regulated technical data through these global API endpoints.

Supported product | Global API endpoints | Restrictions or limitations  
---|---|---  
[Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) | 

`accessapproval.googleapis.com`  

|  None   
[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) | 

`accesscontextmanager.googleapis.com`  

|  None   
[Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) | 

`privateca.googleapis.com`  

|  None   
[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs) | 

`certificatemanager.googleapis.com`  

|  None   
[Cloud Billing API](https://docs.cloud.google.com/billing/docs/concepts) | 

`billingbudgets.googleapis.com`  
`cloudbilling.googleapis.com`  

|  None   
[Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) | 

`dns.googleapis.com`  

|  Affected features  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) | 

`monitoring.googleapis.com`  

|  Affected features  
[Cloud OS Login API](https://docs.cloud.google.com/compute/docs/oslogin) | 

`oslogin.googleapis.com`  

|  None   
[Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) | 

`essentialcontacts.googleapis.com`  

|  None   
[Firebase Security Rules](https://firebase.google.com/docs/rules) | 

`firebaserules.googleapis.com`  

|  None   
[Google Kubernetes Engine (GKE) Identity Service](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication) | 

`anthosidentityservice.googleapis.com`  

|  None   
[GKE Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) | 

`containerfilesystem.googleapis.com`  

|  None   
[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) | 

`container.googleapis.com`  
`containersecurity.googleapis.com`  

|  Affected features and organization policy constraints  
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) | 

`iam.googleapis.com`  
`policytroubleshooter.googleapis.com`  

|  None   
[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) | 

`iap.googleapis.com`  

|  None   
[Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console) | 

`Not applicable`  

|  None   
[Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) | 

`networkconnectivity.googleapis.com`  

|  Affected features  
[Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) | 

`orgpolicy.googleapis.com`  

|  None   
[Resource Manager](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview) | 

`cloudresourcemanager.googleapis.com`  

|  None   
[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) | 

`accesscontextmanager.googleapis.com`  
`accesscontextintelligence.googleapis.com`  

|  None   
  
## Restrictions and limitations

The following sections describe Google Cloud-wide or product-specific restrictions or limitations for features, including any organization policy constraints that are set by default on ITAR folders. Other applicable organization policy constraints—even if not set by default—can provide additional defense-in-depth to further protect your organization's Google Cloud resources.

We strongly recommend not changing the values of the required organization policy constraints listed in the following sections. Doing so may undermine data residency. When such a change has been made, the effects of the change are difficult or impossible to reverse. Ensure that you understand the ramifications of changing an organization policy constraint's value before proceeding.   
  
Additionally, ensure that any automated mechanisms your organization uses to manage organization policies are updated to prevent these values from being changed unintentionally.

### Google Cloud-wide

#### Affected Google Cloud-wide features

Feature | Description  
---|---  
Google Cloud console | To access the Google Cloud console when using the ITAR control package, you must use one of the following URLs:  


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
`gcp.restrictCmekCryptoKeyProjects` | Set to `under:organizations/your-organization-name`, which is your Assured Workloads organization. You can further restrict this value by specifying a project or folder.  
  
Limits the scope of approved folders or projects that can provide [Cloud KMS keys](https://docs.cloud.google.com/kms/docs/algorithms) for encrypting at-rest data using CMEK. This constraint prevents unapproved folders or projects from providing encryption keys, thus helping to guarantee data sovereignty for in-scope services' at-rest data.   
[`gcp.restrictNonCmekServices`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek) | Set to a list of all in-scope [API service names](https://docs.cloud.google.com/iam/docs/full-resource-names), including: 

  * `aiplatform.googleapis.com`
  * `alloydb.googleapis.com`
  * `apigee.googleapis.com`
  * `artifactregistry.googleapis.com`
  * `backupdr.googleapis.com`
  * `bigquery.googleapis.com`
  * `bigquerydatatransfer.googleapis.com`
  * `bigtable.googleapis.com`
  * `cloudfunctions.googleapis.com`
  * `cloudtasks.googleapis.com`
  * `composer.googleapis.com`
  * `compute.googleapis.com`
  * `contactcenterinsights.googleapis.com`
  * `container.googleapis.com`
  * `dataflow.googleapis.com`
  * `dataform.googleapis.com`
  * `datafusion.googleapis.com`
  * `dataplex.googleapis.com`
  * `dataproc.googleapis.com`
  * `dialogflow.googleapis.com`
  * `discoveryengine.googleapis.com`
  * `documentai.googleapis.com`
  * `eventarc.googleapis.com`

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


  1. In the Google Cloud console, go to the **Assured Workloads** page.  [ Go to Assured Workloads](https://console.us.cloud.google.com/compliance/assuredworkloads)
  2. Select your new Assured Workloads folder from the list.
  3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
  4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder. Gemini in BigQuery is not supported by Assured Workloads.  
Compliant BigQuery APIs | The following BigQuery APIs are ITAR-compliant:  


  * [`bigquery.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#bigquery-api)
  * [`bigquerydatapolicy.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#data-api)
  * [`bigqueryconnection.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#connection-api)
  * [`bigquerymigration.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#migration-api)
  * [`bigquerystorage.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#storage-api)
  * [`bigqueryreservation.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#reservations-api)
  * [`bigquerydatatransfer.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview#dts-api)

The Reservations API is not enabled by default. For more information, see [Enabling an API in your Google Cloud project](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).   
Regions | BigQuery is ITAR-compliant for all BigQuery US regions except the US multi-region. ITAR compliance cannot be guaranteed if a dataset is created in a US multi-region, non-US region, or non-US multi-region. It is your responsibility to specify an ITAR-compliant region when creating BigQuery datasets.   
Queries on ITAR datasets from non-ITAR projects | BigQuery doesn't prevent ITAR datasets from being queried from non-ITAR projects. Ensure that any query that uses a read or a join operation on ITAR technical data is in an ITAR-compliant folder.   
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
Loading data | [BigQuery Data Transfer Service connectors](https://docs.cloud.google.com/bigquery/docs/dts-introduction#supported_data_sources) for Google Software as a Service (SaaS) apps, external cloud storage providers, and data warehouses are not supported. It is your responsibility not to use BigQuery Data Transfer Service connectors for ITAR workloads.   
[Third-party transfers](https://docs.cloud.google.com/bigquery/docs/third-party-transfer) | BigQuery doesn't verify support for third-party transfers for the BigQuery Data Transfer Service. It is your responsibility to verify support when using any third-party transfer for the BigQuery Data Transfer Service.   
Non-compliant BQML models | [Externally-trained BQML models](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#externally_trained_models) are not supported.   
Query jobs | Query jobs should only be created within Assured Workloads folders.   
Queries on datasets in other projects | BigQuery doesn't prevent Assured Workloads datasets from being queried from non-Assured Workloads projects. You should ensure that any query that has a read or a join on Assured Workloads data be placed in Assured Workloads folders. You can specify a [fully-qualified table name](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_query) for their query result using `projectname.dataset.table` in the BigQuery CLI.   
Cloud Logging | BigQuery utilizes Cloud Logging for some of your log data. You should disable your `_default` logging buckets or restrict `_default` buckets to in-scope regions to maintain compliance using the following command:  
  
`gcloud alpha logging settings update --organization=ORGANIZATION_ID --disable-default-sink`   
  
For more information, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).   
  
### Cloud DNS

#### Affected Cloud DNS features

Feature | Description  
---|---  
Google Cloud console | Cloud DNS features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/dns/docs/apis) instead.  
  
### Cloud Interconnect

#### Affected Cloud Interconnect features

Feature | Description  
---|---  
Google Cloud console | Cloud Interconnect features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/network-connectivity/docs/interconnect/apis) instead.   
High-availability (HA) VPN | You must enable high-availability (HA) VPN functionality when using Cloud Interconnect with Cloud VPN. Additionally, you must adhere to the encryption and regionalization requirements listed in the Affected Cloud VPN features section.   
  
### Cloud Load Balancing

#### Affected Cloud Load Balancing features

Feature | Description  
---|---  
Google Cloud console | Cloud Load Balancing features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/load-balancing/docs/apis) instead.  
Regional load balancers | You must use only regional load balancers with ITAR. For more information about configuring regional load balancers, see the following pages:  


  * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)
  * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [Regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network)

  
  
### Cloud Logging

#### Affected Cloud Logging features

To use Cloud Logging with Customer-managed encryption keys (CMEK), you must complete the steps in the [Enable CMEK for an organization](https://docs.cloud.google.com/logging/docs/routing/managed-encryption#enable) page in the Cloud Logging documentation. Feature | Description  
---|---  
[Log sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) | Filters shouldn't contain Customer Data.  
  
Log sinks include filters which are stored as configuration. Don't create filters that contain Customer Data.   
[Live tailing log entries](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) | Filters shouldn't contain Customer Data.  
  
A live tailing session includes a filter which is stored as configuration. Tailing logs doesn't store any log entry data itself, but can query and transmit data across regions. Don't create filters that contain Customer Data.   
[Log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) | This feature is disabled.  
  
You cannot create log-based alerts in the Google Cloud console.   
[Shortened URLs for Logs Explorer queries](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#action-bar) | This feature is disabled.  
  
You cannot create shortened URLs of queries in the Google Cloud console.   
[Saving queries in Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries#saved-queries) | This feature is disabled.  
  
You cannot save any queries in the Google Cloud console.   
[SQL-based alerting policies](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting) | This feature is disabled.  
  
You cannot use the SQL-based alerting policies feature.   
  
### Cloud Monitoring

#### Affected Cloud Monitoring features

Feature | Description  
---|---  
[Synthetic Monitor](https://docs.cloud.google.com/monitoring/uptime-checks/introduction#about-sm) | This feature is disabled.  
[Uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/introduction#about-uptime) | This feature is disabled.  
[Log panel widgets](https://docs.cloud.google.com/monitoring/charts/view-logs#display-and-configure) in [Dashboards](https://docs.cloud.google.com/monitoring/dashboards) | This feature is disabled.  
  
You cannot add a log panel to a dashboard.   
[Error reporting panel widgets](https://docs.cloud.google.com/monitoring/charts/view-logs#add-er-widget) in [Dashboards](https://docs.cloud.google.com/monitoring/dashboards) | This feature is disabled.  
  
You cannot add an error reporting panel to a dashboard.   
Filter in `[EventAnnotation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#eventannotation)` for [Dashboards](https://docs.cloud.google.com/monitoring/dashboards) | This feature is disabled.  
  
Filter of `[EventAnnotation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#eventannotation)` cannot be set in a dashboard.   
`[SqlCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#sqlcondition)` in `[alertPolicies](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)` | This feature is disabled.  
  
You cannot add a `[SqlCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#sqlcondition)` to an `[alertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)`.   
  
### Cloud NAT

#### Affected Cloud NAT features

Feature | Description  
---|---  
Google Cloud console | Cloud NAT features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/nat/docs/apis) instead.  
  
### Cloud Router

#### Affected Cloud Router features

Feature | Description  
---|---  
Google Cloud console | Cloud Router features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/network-connectivity/docs/router/reference/apis) instead.   
  
### Cloud Run

#### Affected Cloud Run features

Feature | Description  
---|---  
Unsupported features | The following Cloud Run features aren't supported:  


  * [Cloud Trace integration](https://docs.cloud.google.com/run/docs/trace)
  * [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview)
  * [Eventarc triggers](https://docs.cloud.google.com/functions/docs/calling/eventarc)

  
  
### Cloud SQL

#### Affected Cloud SQL features

Feature | Description  
---|---  
Exporting to CSV | Don't use the [Exporting to CSV](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv#export_data_to_a_csv_file_from) feature as it's not compliant with ITAR. This feature is disabled in the Google Cloud console.   
`executeSql` | Don't use the `executeSql` method of the Cloud SQL API as it's not compliant with ITAR.  
  
### Cloud Storage

#### Affected Cloud Storage features

Feature | Description  
---|---  
Google Cloud console | To maintain ITAR compliance, it is your responsibility to use the [Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console). The Jurisdictional console prevents uploading and downloading Cloud Storage objects. To upload and download Cloud Storage objects, see the Compliant API endpoints row in this section.   
Compliant API endpoints | You must use one of the ITAR-compliant regional endpoints with Cloud Storage. See [Cloud Storage regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints) and [Cloud Storage locations](https://docs.cloud.google.com/storage/docs/locations) for more information.   
Restrictions | You must use Cloud Storage regional endpoints to be ITAR-compliant. For more information about Cloud Storage regional endpoints for ITAR, see [Cloud Storage regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints).  
  
The following operations are not supported by regional endpoints. However, these operations don't carry Customer Data as defined in the [data residency service terms](https://docs.cloud.google.com/assured-workloads/docs/data-residency#note_on_service_data). Therefore, you can use global endpoints for these operations as necessary without violating ITAR compliance: 

  * [HMAC key operations](https://docs.cloud.google.com/storage/docs/authentication/hmackeys)
  * [IAM service account operations](https://docs.cloud.google.com/iam/docs/service-accounts)
  * [Pub/Sub notifications](https://docs.cloud.google.com/storage/docs/pubsub-notifications)

If a user tries to perform an unsupported operation using regional endpoints, Cloud Storage will return a 400 HTTP error code with error message: `This endpoint does not implement this operation. Please use the global endpoint.`  
Copy and rewrite for objects | Copy and rewrite operations for objects are supported by regional endpoints if both the source and destination buckets are located in the region specified in the endpoint. However, you cannot use regional endpoints to copy or rewrite an object from one bucket to another if the buckets exist in different locations. It is possible to use global endpoints to copy or rewrite across locations, but we don't recommend it as it and may violate ITAR compliance.   
  
### Cloud VPN

#### Affected Cloud VPN features

Feature | Description  
---|---  
Google Cloud console | Cloud VPN features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/network-connectivity/docs/vpn/apis) instead.  
Encryption | You must use only FIPS 140-2 compliant ciphers when creating certificates and configuring your IP security. See the [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers) page for more information about supported ciphers in Cloud VPN. For guidance about selecting a cipher that conforms to FIPS 140-2 standards, see the [FIPS 140-2 Validated](https://cloud.google.com/security/compliance/fips-140-2-validated) page.  
  
You cannot change an existing cipher in Google Cloud. Ensure that you configure your cipher on your third-party appliance that's used with Cloud VPN.   
VPN endpoints | You must use only Cloud VPN endpoints that are located in an in-scope region. Ensure that your VPN gateway is configured for use in an in-scope region only.   
  
### Compute Engine

#### Affected Compute Engine features

Feature | Description  
---|---  
[ Suspending and resuming a VM instance](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) | This feature is disabled.  
  
Suspending and resuming a VM instance requires persistent disk storage, and persistent disk storage used for storing the suspended VM state cannot currently be encrypted by using CMEK. See the `gcp.restrictNonCmekServices` organization policy constraint in the section above to understand the data sovereignty and data residency implications of enabling this feature.   
[ Local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds) | This feature is disabled.  
  
You will be unable to create an instance with Local SSDs because they cannot be encrypted by using CMEK. See the `gcp.restrictNonCmekServices` organization policy constraint in the section above to understand the data sovereignty and data residency implications of enabling this feature.   
Google Cloud console | The following Compute Engine features are not available in the Google Cloud console. Use the API or Google Cloud CLI instead:

  * [Health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#gcloud)
  * [Network endpoint groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups)

  
[VM metadata security considerations](https://docs.cloud.google.com/compute/docs/metadata/overview#security-considerations) | It's your responsibility not to write sensitive data to the VM metadata server.   
[Bare Metal Solution VMs](https://docs.cloud.google.com/bare-metal/docs/bms-overview) | You cannot use Bare Metal Solution VMs (o2 VMs) because Bare Metal Solution VMs are not compliant with ITAR.   
  
  
[Google Cloud VMware Engine VMs](https://docs.cloud.google.com/vmware-engine/docs/overview) | You cannot use Google Cloud VMware Engine VMs, as Google Cloud VMware Engine VMs are not compliant with ITAR.   
  
  
[Creating a C3 VM instance](https://cloud.google.com/blog/products/compute/introducing-c3-machines-with-googles-custom-intel-ipu) | This feature is disabled.  
  
  
[Using persistent disks or their snapshots without CMEK](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption) | You cannot use persistent disks or their snapshots unless they have been encrypted using CMEK.  
  
  
[Sharing an SSD persistent disk in multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms) | You cannot share an SSD persistent disk in multi-writer mode between VM instances.   
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
`compute.enableComplianceMemoryProtection` | Set to **True**.  
  
Disables some internal diagnostic features to provide additional protection of memory contents when an infrastructure fault occurs.  
  
Changing this value may affect your workload's data residency or data sovereignty.   
`compute.disableGlobalCloudArmorPolicy` | Set to **True**.  
  
Disables the creation of new global [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview) and the addition or modification of rules to existing global Google Cloud Armor security policies. This constraint doesn't restrict the removal of rules or the ability to remove or change the description and listing of global Google Cloud Armor security policies. Regional Google Cloud Armor security policies are unaffected by this constraint. All global and regional security policies that exist prior to the enforcement of this constraint remain in effect.  
  
  
`compute.disableGlobalLoadBalancing` | Set to **True**.  
  
Disables creation of global load balancing products.  
  
Changing this value may affect your workload's data residency or data sovereignty.   
`compute.disableGlobalSelfManagedSslCertificate` | Set to **True**.  
  
Disables creation of global self-managed SSL certificates.  
  
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

  
`compute.requireOsConfig` | Set to **True**.  
  
Enables [VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/overview) (OS Config) on all new projects. All VM instances created in new projects will have VM Manager enabled.   
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
  
### Google Kubernetes Engine

#### Affected Google Kubernetes Engine features

Feature | Description  
---|---  
Cluster resource restrictions | Ensure that your cluster configuration does not use resources for services that are unsupported in ITAR. For example, the following configuration is invalid because it requires enabling or using an unsupported service:  
  
` set `binaryAuthorization.evaluationMode` to `enabled` `  
  
#### Google Kubernetes Engine organization policy constraints

Organization policy constraint | Description  
---|---  
`container.restrictNoncompliantDiagnosticDataAccess` | Set to **True**.  
  
Disables aggregate analysis of kernel issues, which is required to maintain sovereign control of a workload.  
  
Changing this value may affect your workload's data residency or data sovereignty.   
  
### Network Connectivity Center

#### Affected Network Connectivity Center features

Feature | Description  
---|---  
Google Cloud console | Network Connectivity Center features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/network-connectivity/docs/apis) instead.  
  
### Pub/Sub

#### Pub/Sub organization policy constraints

Organization policy constraint | Description  
---|---  
`pubsub.enforceInTransitRegions` | Set to **True**.  
  
Ensures that Customer Data transits only within the allowed regions specified in the message storage policy for the Pub/Sub topic.  
  
Changing this value might affect your workload's data residency or data sovereignty.   
`pubsub.managed.disableSubscriptionMessageTransforms` | Set to **True**.  
  
Disables Pub/Sub subscriptions from being set with [Single Message Transforms (SMTs)](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).  
  
Changing this value might affect your workload's data residency or data sovereignty.   
`pubsub.managed.disableTopicMessageTransforms` | Set to **True**.  
  
Disables Pub/Sub topics from being set with [Single Message Transforms (SMTs)](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).  
  
Changing this value may affect your workload's data residency or data sovereignty.   
  
### Security Command Center Premium

#### Affected Security Command Center Premium features

Feature | Description  
---|---  
Compliance Manager | Compliance Manager is unsupported and has not met the control requirements for ITAR.  
Data Security Posture Management | Data Security Posture Management is unsupported and has not met the control requirements for ITAR.  
  
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
  
### Vertex AI

#### Vertex AI organization policy constraints

Organization policy constraint | Description  
---|---  
`vertexai.allowOnlyITARCompliantAPIs` | Set to **True**.  
  
Allows only ITAR-compliant APIs to be used in Vertex AI APIs. By default, all APIs are allowed.   
  
### Virtual Private Cloud (VPC)

#### Affected VPC features

Feature | Description  
---|---  
Google Cloud console | VPC networking features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/vpc/docs/apis) instead.  
  
## What's next

  * Learn how to [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder)
  * Understand [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
