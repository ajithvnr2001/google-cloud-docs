---
url: https://docs.cloud.google.com/vpc-service-controls/docs/supported-products/
title: Supported products and limitations \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:27:21.649595+00:00
---

# Supported products and limitations  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/supported-products/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Supported products and limitations Stay organized with collections  Save and categorize content based on your preferences. 

This page contains a table of products and services that are supported by VPC Service Controls, as well as a list of known limitations with certain services and interfaces.

## List all supported services

To retrieve the complete list of all VPC Service Controls supported products and services, run the following command:
    
    
    gcloud access-context-manager supported-services list
    

You get a response with a list of products and services.
    
    
    NAME                 TITLE             SERVICE_SUPPORT_STAGE   AVAILABLE_ON_RESTRICTED_VIP      KNOWN_LIMITATIONS
    SERVICE_ADDRESS      SERVICE_NAME      SERVICE_STATUS          RESTRICTED_VIP_STATUS            LIMITATIONS_STATUS
    .
    .
    .
    

This response includes the following values:

Value | Description  
---|---  
`SERVICE_ADDRESS` | Service name of the product or service. For example, `aiplatform.googleapis.com`.   
`SERVICE_NAME` | Name of the product or service. For example, `Gemini Enterprise Agent Platform API`.   
`SERVICE_STATUS` | The status of the service integration with VPC Service Controls. The following are the possible values:  


  * `GA`: The service integration is fully supported by VPC Service Controls perimeters.
  * `PREVIEW`: The service integration is ready for broader testing and use but is not fully supported for production environments by VPC Service Controls perimeters.
  * `DEPRECATED`: The service integration is scheduled to be shut down and removed.

  
`RESTRICTED_VIP_STATUS` | Specifies if the service integration with VPC Service Controls is supported by the [restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity). The following are the possible values:  


  * `TRUE`: The service integration is fully supported by the restricted VIP and can be protected by VPC Service Controls perimeters.
  * `FALSE`: The service integration is not supported by the restricted VIP.

For a complete list of the services available on the restricted VIP, see [Services supported by the restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services).   
`LIMITATIONS_STATUS` | Specifies if the service integration with VPC Service Controls has any limitations. The following are the possible values:  


  * `TRUE`: The service integration with VPC Service Controls has known limitations. You can check the corresponding entry for the service in the [Supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#supported_products) table to learn more about these limitations.
  * `FALSE`: The service integration with VPC Service Controls has no known limitations.

  
  
### List supported methods for a service

To retrieve the list of methods and permissions supported by VPC Service Controls for a service, run the following command:
    
    
    gcloud access-context-manager supported-services describe SERVICE_ADDRESS
    

Replace `SERVICE_ADDRESS` with the service name of the product or service. For example, `aiplatform.googleapis.com`.

You get a response with a list of methods and permissions.
    
    
    availableOnRestrictedVip: RESTRICTED_VIP_STATUS
    knownLimitations: LIMITATIONS_STATUS
    name: SERVICE_ADDRESS
    serviceSupportStage: SERVICE_STATUS
    supportedMethods:
    METHODS_LIST
    .
    .
    .
    title: SERVICE_NAME
    

In this response, `METHODS_LIST` lists all the methods and permissions supported by VPC Service Controls for the specified service. For a complete list of all the supported service methods and permissions, see [Supported service method restrictions](https://docs.cloud.google.com/vpc-service-controls/docs/supported-method-restrictions).

For information about the service methods that VPC Service Controls can't control, see [Service method exceptions](https://docs.cloud.google.com/vpc-service-controls/docs/method-exceptions).

## Supported products

**Note:** This table includes _all_ products that are supported by VPC Service Controls and operate normally _inside_ a service perimeter. However, not all supported products have services that can be _protected_ by a perimeter.

VPC Service Controls supports the following products:

Supported products | Description  
---|---  
  
###  [Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `config.googleapis.com`  
**Details** |  For more information about Infrastructure Manager, refer to the [product documentation](https://docs.cloud.google.com/infrastructure-manager/docs).   
**Limitations** |  To use Infrastructure Manager in a perimeter:

  * You must use a Cloud Build private pool for the worker pool used by Infrastructure Manager. You need to [use the Infra Manager-maintained Terraform provider for Google Cloud](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform-provider) if you don't want to enable [public internet calls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls#enable-public-internet) to download the HashiCorp-maintained Terraform providers and configurations. You cannot use the default Cloud Build worker pool.
  * The following must be in the same perimeter: 
    * The service account that Infrastructure Manager uses.
    * The Cloud Build worker pool that Infrastructure Manager uses.
    * The storage bucket that Infrastructure Manager uses. You can use the default storage bucket.

  
  
###  [App Design Center](https://docs.cloud.google.com/application-design-center/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `designcenter.googleapis.com`  
**Details** |  The API for App Design Center can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about App Design Center, refer to the [product documentation](https://docs.cloud.google.com/application-design-center/docs).   
**Limitations** |  To use App Design Center in a perimeter:

  * You must use a Cloud Build private pool for the worker pool used by App Design Center. Enable [public internet calls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls#enable-public-internet) to download HashiCorp-maintained Terraform providers and configurations. You cannot use the default Cloud Build worker pool.
  * The following resources must be restricted in the same perimeter: 
    * The management project where you set up App Design Center.
    * The Cloud Build worker pool that App Design Center uses.

For more information, see [ Deploy resources in a secure perimeter](https://docs.cloud.google.com/application-design-center/docs/set-up-secure-perimeter).  
  
###  [Workload Identity API](https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `workloadidentity.googleapis.com`  
**Details** |  The Workload Identity API lets you trigger the creation of [service agents](https://docs.cloud.google.com/iam/docs/service-agents) for a specified service in a specified project, folder, or organization. When you restrict the Workload Identity API with a perimeter, you can't trigger service agent creation for projects inside the perimeter. This is true regardless of the service specified in the request.  VPC Service Controls doesn't support adding folder-level or organization-level resources into a service perimeter. As a result, you can't use a perimeter to prevent users from triggering the creation of service agents for folders or organizations.  For more information about Workload Identity API, refer to the [product documentation](https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest).   
**Limitations** |  The Workload Identity API integration with VPC Service Controls has no known limitations.   
  
###  [Workload Manager](https://docs.cloud.google.com/workload-manager/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `workloadmanager.googleapis.com`  
**Details** |  To use Workload Manager in a VPC Service Controls perimeter: 

  * You must use a Cloud Build private worker pool for your deployment environment in Workload Manager. You cannot use the default Cloud Build worker pool.
  * The Cloud Build private pool must have [public internet calls enabled](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls#enable-public-internet) to download the Terraform configuration.

For more information, see [ Use a Cloud Build private worker pool](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#vpc-sc-pool) in the Workload Manager documentation. For more information about Workload Manager, refer to the [product documentation](https://docs.cloud.google.com/workload-manager/docs).   
**Limitations** |  You must ensure that the following resources are in the same [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters): 

  * Workload Manager service account.
  * Cloud Build private worker pool.
  * The Cloud Storage bucket that Workload Manager uses for deployment.

  
  
###  [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `netapp.googleapis.com`  
**Details** |  The API for Google Cloud NetApp Volumes can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Google Cloud NetApp Volumes, refer to the [product documentation](https://docs.cloud.google.com/netapp/volumes/docs).   
**Limitations** |  VPC Service Controls doesn't cover dataplane paths such as Network File System (NFS) and Server Message Block (SMB) reads and writes. Additionally, if your host and service projects are configured in different perimeters, you can experience a break in the implementation of Google Cloud services.  
  
###  [Google Cloud Search](https://developers.google.com/cloud-search)

|  |  **Status** |  GA   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudsearch.googleapis.com`  
**Details** |  Google Cloud Search supports Virtual Private Cloud Security Controls (VPC Service Controls) to enhance the security of your data. VPC Service Controls allows you to define a security perimeter around Google Cloud Platform resources to constrain data and help mitigate data exfiltration risks. For more information about Google Cloud Search, refer to the [product documentation](https://developers.google.com/cloud-search).   
**Limitations** |  Because Cloud Search resources are not stored in a Google Cloud project, you must update the Cloud Search customer settings with the VPC perimeter protected project. The VPC project acts as a virtual project container for all your Cloud Search resources. Without building this mapping, VPC Service Controls won't work for the Cloud Search API. For complete steps to enable VPC Service Controls with Google Cloud Search, refer to [Enhance security for Google Cloud Search](https://developers.google.com/cloud-search/docs/guides/implement-vpc-service-controls).   
  
###  [Cluster Director](https://docs.cloud.google.com/cluster-director/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `hypercomputecluster.googleapis.com`  
**Details** |  VPC Service Controls helps protect the Cluster Director API, letting you use Cluster Director inside service perimeters.  For more information about Cluster Director, refer to the [product documentation](https://docs.cloud.google.com/cluster-director/docs).   
**Limitations** |   
  
###  [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `networkmanagement.googleapis.com`  
**Details** |  The API for Connectivity Tests can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Connectivity Tests, refer to the [product documentation](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests).   
**Limitations** |  The Connectivity Tests integration with VPC Service Controls has no known limitations.   
  
###  [AI Platform Prediction](https://docs.cloud.google.com/ai-platform/prediction/docs/vpc-service-controls)

|  |  **Status** |  **DEPRECATED**. This legacy version of AI Platform Prediction is [deprecated](https://docs.cloud.google.com/ai-platform/prediction/docs/deprecations) and will no longer be available on Google Cloud after January 31, 2025. All models, associated metadata, and deployments will be deleted after January 31, 2025. Migrate your resources to [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/introduction-unified-platform) to get new machine learning features that are unavailable in AI Platform.  
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `ml.googleapis.com`  
**Details** |  VPC Service Controls supports online prediction, but not batch prediction.  For more information about AI Platform Prediction, refer to the [product documentation](https://docs.cloud.google.com/ai-platform/prediction/docs/vpc-service-controls).   
**Limitations** | 

  * To fully protect AI Platform Prediction, add all of the following APIs to the service perimeter:
    * AI Platform Training and Prediction API (`ml.googleapis.com`)
    * Pub/Sub API (`pubsub.googleapis.com`)
    * Cloud Storage API (`storage.googleapis.com`)
    * Google Kubernetes Engine API (`container.googleapis.com`)
    * Container Registry API (`containerregistry.googleapis.com`)
    * Cloud Logging API (`logging.googleapis.com`)
Read more about [setting up VPC Service Controls for AI Platform Prediction](https://docs.cloud.google.com/ai-platform/prediction/docs/vpc-service-controls).
  * [Batch prediction](https://docs.cloud.google.com/ai-platform/prediction/docs/batch-predict) is not supported when you use AI Platform Prediction inside a service perimeter.
  * AI Platform Prediction and AI Platform Training both use the AI Platform Training and Prediction API, so you must configure VPC Service Controls for both products. Read more about [setting up VPC Service Controls for AI Platform Training](https://docs.cloud.google.com/ai-platform/training/docs/vpc-service-controls).

  
  
###  [AI Platform Training](https://docs.cloud.google.com/ai-platform/training/docs/vpc-service-controls)

|  |  **Status** |  **DEPRECATED**. This legacy version of AI Platform Training is [deprecated](https://docs.cloud.google.com/ai-platform/training/docs/deprecations) and will no longer be available on Google Cloud after January 31, 2025. Migrate your resources to [Gemini Enterprise Agent Platform Managed Training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/introduction-unified-platform) to get new machine learning features that are unavailable in AI Platform.  
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `ml.googleapis.com`  
**Details** |  The API for AI Platform Training can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about AI Platform Training, refer to the [product documentation](https://docs.cloud.google.com/ai-platform/training/docs/vpc-service-controls).   
**Limitations** | 

  * To fully protect your AI Platform Training training jobs, add all of the following APIs to the service perimeter:
    * AI Platform Training and Prediction API (`ml.googleapis.com`)
    * Pub/Sub API (`pubsub.googleapis.com`)
    * Cloud Storage API (`storage.googleapis.com`)
    * Google Kubernetes Engine API (`container.googleapis.com`)
    * Container Registry API (`containerregistry.googleapis.com`)
    * Cloud Logging API (`logging.googleapis.com`)
Read more about [setting up VPC Service Controls for AI Platform Training](https://docs.cloud.google.com/ai-platform/training/docs/vpc-service-controls).
  * [Training with TPUs](https://docs.cloud.google.com/ai-platform/training/docs/using-tpus) is not supported when you use AI Platform Training inside a service perimeter.
  * AI Platform Training and AI Platform Prediction both use the AI Platform Training and Prediction API, so you must configure VPC Service Controls for both products. Read more about [setting up VPC Service Controls for AI Platform Prediction](https://docs.cloud.google.com/ai-platform/prediction/docs/vpc-service-controls).

  
  
###  [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `alloydb.googleapis.com`  
**Details** |  VPC Service Controls perimeters protect the AlloyDB API.  For more information about AlloyDB for PostgreSQL, refer to the [product documentation](https://docs.cloud.google.com/alloydb/docs).   
**Limitations** | 

  * Service perimeters protect only the AlloyDB for PostgreSQL Admin API. They don't protect IP-based data access to underlying databases (such as AlloyDB for PostgreSQL instances). To restrict public IP access on AlloyDB for PostgreSQL instances, use an [organization policy constraint](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints#example_constraints).
  * Before you configure VPC Service Controls for AlloyDB for PostgreSQL, enable the Service Networking API.
  * When you use AlloyDB for PostgreSQL with Shared VPC and VPC Service Controls, the host project and service project must be in the same VPC Service Controls service perimeter. 

  
  
###  [Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/agent-builder/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `aiplatform.googleapis.com`  
**Details** |  The API for Agent Runtime on Gemini Enterprise Agent Platform can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Agent Runtime on Gemini Enterprise Agent Platform, refer to the [product documentation](https://docs.cloud.google.com/agent-builder/overview).   
**Limitations** |  For more information about limitations, see [limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls#limitations) in the Agent Platform documentation.  
  
###  [Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `notebooks.googleapis.com`  
**Details** |  The API for Agent Platform Workbench can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Agent Platform Workbench, refer to the [product documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction).   
**Limitations** |  For information about the limitations of using Agent Platform Workbench with VPC Service Controls, see [service perimeters for Agent Platform Workbench instances](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/service-perimeter#limitations), [service perimeters for user-managed notebooks](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/service-perimeter#limitations) (deprecated), and [service perimeters for managed notebooks](https://docs.cloud.google.com/vertex-ai/docs/workbench/managed/service-perimeter#limitations) (deprecated).   
  
###  [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `aiplatform.googleapis.com`  
**Details** |  The API for Agent Platform can be protected by VPC Service Controls and the product can be used normally inside service perimeters. Colab Enterprise is a part of Gemini Enterprise Agent Platform. See Colab Enterprise. For more information about Gemini Enterprise Agent Platform, refer to the [product documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).   
**Limitations** |  For more information about limitations, see [limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls#limitations) in the Agent Platform documentation.  
  
###  [Gemini Enterprise Agent Platform Vision](https://docs.cloud.google.com/vision-ai/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `visionai.googleapis.com`  
**Details** |  The API for Gemini Enterprise Agent Platform Vision can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Gemini Enterprise Agent Platform Vision, refer to the [product documentation](https://docs.cloud.google.com/vision-ai/docs).   
**Limitations** |  When `constraints/visionai.disablePublicEndpoint` is on, we disable the cluster's public endpoint. Users must manually connect to the PSC target and access the service from the private network. You can get the PSC target from the [`cluster` resource](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.clusters#resource:-cluster).   
  
###  [Colab Enterprise](https://docs.cloud.google.com/colab/docs/service-controls)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `aiplatform.googleapis.com`  
**Details** |  The API for Colab Enterprise can be protected by VPC Service Controls and the product can be used normally inside service perimeters. Colab Enterprise is a part of Gemini Enterprise Agent Platform. See Agent Platform. Colab Enterprise uses Dataform for storing notebooks. See Dataform. For more information about Colab Enterprise, refer to the [product documentation](https://docs.cloud.google.com/colab/docs/service-controls).   
**Limitations** |  For information about limitations, see [Known limitations](https://docs.cloud.google.com/colab/docs/service-controls#limitations) in the Colab Enterprise documentation.  
  
###  [Agent Registry](https://docs.cloud.google.com/agent-registry/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `agentregistry.googleapis.com`  
**Details** |  Agent Registry is a centralized catalog for discovering and registering agents and MCP servers.  For more information about Agent Registry, refer to the [product documentation](https://docs.cloud.google.com/agent-registry/overview).   
**Limitations** |  Make sure that your project for Agent Registry and the enabled APIs are included in your VPC Service Controls service perimeter.   
  
###  [Apigee and Apigee hybrid](https://docs.cloud.google.com/apigee/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `apigee.googleapis.com,  
apigeeconnect.googleapis.com`  
**Details** |  The API for Apigee and Apigee hybrid can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Apigee and Apigee hybrid, refer to the [product documentation](https://docs.cloud.google.com/apigee/docs).   
**Limitations** |  Apigee integrations with VPC Service Controls have the following limitations:

  * Integrated portals require [additional steps](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc#portal) to configure.
  * You must deploy Drupal portals within the service perimeter.

  
  
###  [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `apihub.googleapis.com`  
**Details** |  The API for Apigee API hub can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Apigee API hub, refer to the [product documentation](https://docs.cloud.google.com/apigee/docs/apihub).   
**Limitations** |  All Apigee runtime projects associated with an API hub instance must reside within the same VPC Service Controls service perimeter as the API hub host project.   
  
###  [BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `analyticshub.googleapis.com`  
**Details** |  VPC Service Controls protects [data exchanges](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#data_exchanges) and [listings](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#listings). To protect [shared](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#shared_datasets) and [linked datasets](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) using a service perimeter, use the [BigQuery API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_bigquery). For more information, see [sharing VPC Service Controls rules](https://docs.cloud.google.com/bigquery/docs/analytics-hub-vpc-sc-rules).  For more information about BigQuery sharing, refer to the [product documentation](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest).   
**Limitations** |  BigQuery sharing doesn't support method-based rules and you must allow all methods. For more information, see [sharing VPC Service Controls rules limitations](https://docs.cloud.google.com/bigquery/docs/analytics-hub-vpc-sc-rules#limitations).   
  
###  [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `meshca.googleapis.com,  
meshconfig.googleapis.com,  
trafficdirector.googleapis.com,  
networkservices.googleapis.com,  
networksecurity.googleapis.com`  
**Details** |  The API for Cloud Service Mesh can be protected by VPC Service Controls, and the product can be used normally inside service perimeters. You can use `mesh.googleapis.com` to enable the required APIs for Cloud Service Mesh. You don't need to restrict `mesh.googleapis.com` in your perimeter as it doesn't expose any APIs.

  * Learn about [configuring VPC Service Controls for Cloud Service Mesh (Managed)](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc).
  * Learn about [adding Cloud Service Mesh services to the service perimeters](https://docs.cloud.google.com/service-mesh/docs/set-service-perimeter).

For more information about Cloud Service Mesh, refer to the [product documentation](https://docs.cloud.google.com/service-mesh/docs).   
**Limitations** |  The Cloud Service Mesh integration with VPC Service Controls has no known limitations.   
  
###  [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `artifactregistry.googleapis.com`  
**Details** |  In addition to protecting the Artifact Registry API, Artifact Registry can be used inside service perimeters with GKE and Compute Engine.  For more information about Artifact Registry, refer to the [product documentation](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc).   
**Limitations** | 

  * For Artifact Registry repositories that use the `pkg.dev` domain, you must [configure DNS](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring-dns) for `*.pkg.dev` to map to either `private.googleapis.com` or `restricted.googleapis.com`. For more information, see [Securing repositories in a service perimeter](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc).
  * In addition to the artifacts inside a perimeter that are available to Artifact Registry, the following read-only repositories are available to all projects regardless of service perimeters:
    * `gcr.io/anthos-baremetal-release`
    * `gcr.io/asci-toolchain`
    * `gcr.io/cloud-airflow-releaser`
    * `gcr.io/cloud-builders`
    * `gcr.io/cloud-dataflow`
    * `gcr.io/cloud-ingest`
    * `gcr.io/cloud-marketplace`
    * `gcr.io/cloud-ssa`
    * `gcr.io/cloudsql-docker`
    * `gcr.io/config-management-release`
    * `gcr.io/deeplearning-platform-release`
    * `gcr.io/foundry-dev`
    * `gcr.io/fn-img`
    * `gcr.io/gae-runtimes`
    * `gcr.io/serverless-runtimes`
    * `gcr.io/gke-node-images`
    * `gcr.io/gke-release`
    * `gcr.io/gkeconnect`
    * `gcr.io/google-containers`
    * `gcr.io/kubeflow`
    * `gcr.io/kubeflow-images-public`
    * `gcr.io/kubernetes-helm`
    * `gcr.io/istio-release`
    * `gcr.io/ml-pipeline`
    * `gcr.io/projectcalico-org`
    * `gcr.io/rbe-containers`
    * `gcr.io/rbe-windows-test-images`
    * `gcr.io/speckle-umbrella`
    * `gcr.io/stackdriver-agents`
    * `gcr.io/tensorflow`
    * `gcr.io/vertex-ai`
    * `gcr.io/vertex-ai-restricted`
    * `gke.gcr.io`
    * `k8s.gcr.io`
In all cases, the regional versions of these repositories are also available.

  
  
###  [Assured Open Source Software](https://docs.cloud.google.com/assured-open-source-software/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `assuredoss.googleapis.com`  
**Details** |  The API for Assured Open Source Software can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Assured Open Source Software, refer to the [product documentation](https://docs.cloud.google.com/assured-open-source-software/docs).   
**Limitations** |  You must configure egress rules to use Assured Open Source Software within a service perimeter. For more information, see [ Configure Assured Open Source Software support for VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/aoss-configure-support-for-vpc-sc).   
  
###  [Assured Workloads](https://docs.cloud.google.com/assured-workloads)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `assuredworkloads.googleapis.com`  
**Details** |  The API for Assured Workloads can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Assured Workloads, refer to the [product documentation](https://docs.cloud.google.com/assured-workloads).   
**Limitations** |  This entry applies only to the Assured Workloads API. You can't add organization-level Assured Workloads API resources to a service perimeter. However, VPC Service Controls-supported services deployed inside an Assured Workloads folder are restricted by the perimeter. The status of those supported services is indicated by their respective entries on this page.   
  
###  [AutoML Translation](https://docs.cloud.google.com/translate/automl/docs)

|  |  **Status** |  **DEPRECATED**. AutoML Translation API is [deprecated](https://docs.cloud.google.com/translate/automl/docs/deprecations) and will no longer be available on Google Cloud after September 30, 2025. The functionality and management of custom models is available through [Cloud Translation - Advanced API (v3)](https://docs.cloud.google.com/translate/docs).  
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `automl.googleapis.com,  
eu-automl.googleapis.com`  
**Details** |  To fully protect the AutoML API, include all of the following APIs in your perimeter:

  * AutoML API (`automl.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)
  * Compute Engine API (`compute.googleapis.com`)
  * BigQuery API (`bigquery.googleapis.com`)

For more information about AutoML Translation, refer to the [product documentation](https://docs.cloud.google.com/translate/automl/docs).   
**Limitations** | 

  * All AutoML products that are integrated with VPC Service Controls use the same service name.
  * You cannot add the supported [regional endpoints](https://docs.cloud.google.com/natural-language/automl/docs/locations#setting_the_location_using_the_api), such as `eu-automl.googleapis.com`, to the list of restricted services in a perimeter. When you protect the `automl.googleapis.com` service, the perimeter protects the supported regional endpoints, such as `eu-automl.googleapis.com`, as well. 

For more information, see the limitations for using AutoML products with VPC Service Controls.   
  
###  [Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **No.** The API for Bare Metal Solution cannot be protected by service perimeters. However, Bare Metal Solution can be used normally in projects inside a perimeter.   
**Details** |  The Bare Metal Solution API can be added to a secure perimeter. However, the VPC Service Controls perimeters do not extend to the Bare Metal Solution environment in the regional extensions.  For more information about Bare Metal Solution, refer to the [product documentation](https://docs.cloud.google.com/bare-metal/docs).   
**Limitations** |  Connecting VPC Service Controls to your Bare Metal Solution environment doesn't uphold any service control guarantees. For more information about Bare Metal Solution limitation regarding VPC Service Controls, see [Known issues and limitations](https://docs.cloud.google.com/bare-metal/docs/known-issues#bms-vpcsc-limitation).  
  
###  [Batch](https://docs.cloud.google.com/batch/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `batch.googleapis.com`  
**Details** |  The API for Batch can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Batch, refer to the [product documentation](https://docs.cloud.google.com/batch/docs).   
**Limitations** |  To fully protect Batch, you need to include the following APIs in your perimeter: 

  * Batch API (`batch.googleapis.com`)
  * Cloud Logging API (`logging.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)
  * Container Registry API (`containerregistry.googleapis.com`)
  * Artifact Registry API (`artifactregistry.googleapis.com`)
  * Filestore API (`file.googleapis.com`)

  
  
###  [Lakehouse runtime catalog](https://docs.cloud.google.com/bigquery/docs/manage-open-source-metadata)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `biglake.googleapis.com`  
**Details** |  The API for Lakehouse runtime catalog can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Lakehouse runtime catalog, refer to the [product documentation](https://docs.cloud.google.com/bigquery/docs/manage-open-source-metadata).   
**Limitations** |  The Lakehouse runtime catalog integration with VPC Service Controls has no known limitations.   
  
###  [BigQuery](https://docs.cloud.google.com/bigquery/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `bigquery.googleapis.com,  
bigquerystorage.googleapis.com,  
bigqueryreservation.googleapis.com,  
bigqueryconnection.googleapis.com`  
**Details** |  When you protect the BigQuery API using a service perimeter, the BigQuery Storage API (`bigquerystorage.googleapis.com`), BigQuery Reservation API (`bigqueryreservation.googleapis.com`), and BigQuery Connection API (`bigqueryconnection.googleapis.com`) are also protected. You do not need to separately add these APIs to your perimeter's list of protected services. Learn more about configuring [VPC Service Controls for BigQuery](https://docs.cloud.google.com/bigquery/docs/vpc-sc) and how to [allow access to community-contributed functions within a perimeter](https://docs.cloud.google.com/bigquery/docs/user-defined-functions#vpc). For more information about BigQuery, refer to the [product documentation](https://docs.cloud.google.com/bigquery/docs).   
**Limitations** | 

  * BigQuery audit log records don't always include all resources that were used when a request is made, due to the service internally processing access to multiple resources.
  * When accessing a BigQuery instance protected by a service perimeter, the BigQuery job must be run within a project inside the perimeter, or in a project allowed by an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) of the perimeter. By default, the BigQuery client libraries run jobs within the service account or user's project, causing the query to be rejected by VPC Service Controls.
  * When using authorized views with VPC Service Controls, service perimeters are enforced for both the view project and source data projects. For example, if the view project is not in the same perimeter as the source data project, an appropriate egress rule is required. For more information, see [Authorized views and VPC Service Controls](https://docs.cloud.google.com/bigquery/docs/authorized-views#vpcsc-and-views).
  * BigQuery blocks saving query results to Google Drive from the VPC Service Controls protected perimeter. However, VPC Service Controls doesn't block [querying Google Drive data](https://docs.cloud.google.com/bigquery/docs/query-drive-data). For information about restricting access to Google Drive, see [Create and manage trust rules for Drive sharing](https://support.google.com/a/answer/10621317).
  * If you grant access using an ingress rule with user accounts as the identity type, you can't view BigQuery resource utilization or the administrative jobs explorer on the [**Monitoring**](https://docs.cloud.google.com/bigquery/docs/admin-resource-charts) page. To use these features, configure an ingress rule that uses either `ANY_IDENTITY` or [a Google group](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console#creating) that includes the specific users that need access. [Specify the group](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups#configure-identity-group-ingress) in the identities field of the ingress rule using the format `group:GROUP_EMAIL_ADDRESS`.
  * If you grant BigQuery users access to data using an ingress rule, then users can use the Google Cloud console to query and save the results to a local file.
  * Accessing resources in VPC Service Controls perimeters is disallowed in BigQuery Standard edition. VPC Service Controls is only supported when performing analysis through BigQuery Enterprise, Enterprise Plus, or On-Demand.
  * The BigQuery Reservation API is partially supported. The [ BigQuery Reservation API](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations.assignments), which creates the assignment resource, doesn't enforce service perimeter restrictions on the assignment assignees.
  * [BigQuery data preparation](https://docs.cloud.google.com/bigquery/docs/data-prep-introduction) uses Dataform, which has additional access control requirements. See [ Dataform](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dataform).

  
  
###  [BigQuery Data Policy API](https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `bigquerydatapolicy.googleapis.com`  
**Details** |  The BigQuery Data Policy API can be protected by VPC Service Controls, and the product can be used normally inside service perimeters.  For more information about BigQuery Data Policy API, refer to the [product documentation](https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro).   
**Limitations** |  The BigQuery Data Policy API integration with VPC Service Controls has no known limitations.   
  
###  [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery-transfer/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `bigquerydatatransfer.googleapis.com`  
**Details** |  Service perimeter only protects BigQuery Data Transfer Service API. The actual data protection is enforced by BigQuery. It is by design to allow importing data from various external sources outside of Google Cloud, such as Amazon S3, Redshift, Teradata, YouTube, Google Play and Google Ads, into BigQuery datasets. For information about VPC Service Controls requirements to migrate data from Teradata, see [VPC Service controls requirements](https://docs.cloud.google.com/bigquery-transfer/docs/teradata-migration#vpc-service-controls).  For more information about BigQuery Data Transfer Service, refer to the [product documentation](https://docs.cloud.google.com/bigquery-transfer/docs).   
**Limitations** | 

  * The BigQuery Data Transfer Service doesn't support exporting data out of a BigQuery dataset. For more information, see [Exporting table data](https://docs.cloud.google.com/bigquery/docs/exporting-data).
  * To transfer data between projects, the destination project must either be inside the same perimeter as the source project, or else an egress rule must permit the transfer of data out of the perimeter. For information about setting the egress rules, see [Limitations in Manage BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/managing-datasets#limitations).
  * Ingress and egress violations for BigQuery jobs initiated by BigQuery Data Transfer Service recurring offline transfer runs don't contain user context information such as caller IP address and device.
  * The BigQuery Data Transfer Service only supports transferring data into projects protected by a service perimeter using one of the connectors listed in [Supported data sources](https://docs.cloud.google.com/bigquery/docs/dts-introduction#supported_data_sources). The BigQuery Data Transfer Service doesn't support transferring data into projects protected by a service perimeter using a connector provided by other third-party partners. 

  
  
###  [BigQuery Migration API](https://docs.cloud.google.com/bigquery/docs/reference/migration/rest)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `bigquerymigration.googleapis.com`  
**Details** |  The BigQuery Migration API can be protected by VPC Service Controls, and the product can be used normally inside service perimeters.  For more information about BigQuery Migration API, refer to the [product documentation](https://docs.cloud.google.com/bigquery/docs/reference/migration/rest).   
**Limitations** |  The BigQuery Migration API integration with VPC Service Controls has no known limitations.   
  
###  [Bigtable](https://docs.cloud.google.com/bigtable/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `bigtable.googleapis.com,  
bigtableadmin.googleapis.com`  
**Details** |  The `bigtable.googleapis.com` and `bigtableadmin.googleapis.com` services are bundled together. When you restrict the `bigtable.googleapis.com` service in a perimeter, the perimeter restricts the `bigtableadmin.googleapis.com` service by default. You cannot add the `bigtableadmin.googleapis.com` service to the list of restricted services in a perimeter because it is bundled with `bigtable.googleapis.com`.  For more information about Bigtable, refer to the [product documentation](https://docs.cloud.google.com/bigtable/docs).   
**Limitations** |  The Bigtable integration with VPC Service Controls has no known limitations.   
  
###  [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `binaryauthorization.googleapis.com`  
**Details** |  When using multiple projects with Binary Authorization, each project must be included in the VPC Service Controls perimeter. For more information about this use case, see [Multi-project setup](https://docs.cloud.google.com/binary-authorization/docs/multi-project-setup-cli).  With Binary Authorization, you may use Artifact Analysis to store attestors and attestations as notes and occurrences, respectively. In this case, you must also include Artifact Analysis in the VPC Service Controls perimeter. See VPC Service Controls guidance for Artifact Analysis for additional details.  For more information about Binary Authorization, refer to the [product documentation](https://docs.cloud.google.com/binary-authorization/docs).   
**Limitations** |  The Binary Authorization integration with VPC Service Controls has no known limitations.   
  
###  [Blockchain Node Engine](https://docs.cloud.google.com/blockchain-node-engine/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `blockchainnodeengine.googleapis.com`  
**Details** |  The API for Blockchain Node Engine can be protected by VPC Service Controls and used normally inside service perimeters.  For more information about Blockchain Node Engine, refer to the [product documentation](https://docs.cloud.google.com/blockchain-node-engine/docs).   
**Limitations** |  Blockchain Node Engine integrations with VPC Service Controls have the following limitations: 

  * VPC Service Controls only protects the Blockchain Node Engine API. When a node is created, you must still indicate that it is meant for a user-configured private network with [Private Service Connect](https://docs.cloud.google.com/blockchain-node-engine/docs/psc). 
  * The peer-to-peer traffic is not affected by VPC Service Controls or Private Service Connect and will continue to use the public internet. 

  
  
###  [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `privateca.googleapis.com`  
**Details** |  The API for Certificate Authority Service can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Certificate Authority Service, refer to the [product documentation](https://docs.cloud.google.com/certificate-authority-service/docs).   
**Limitations** | 

  * To use Certificate Authority Service in a protected environment, you must also add the Cloud KMS API (`cloudkms.googleapis.com`) and the Cloud Storage API (`storage.googleapis.com`) to your service perimeter. 

  
  
###  [Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `krmapihosting.googleapis.com`  
**Details** |  To use Config Controller with VPC Service Controls, you must enable the following APIs inside your perimeter: 

  * Cloud Monitoring API (`monitoring.googleapis.com`)
  * Container Registry API (`containerregistry.googleapis.com`)
  * Google Cloud Observability API (`logging.googleapis.com`)
  * Security Token Service API (`sts.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)

If you provision resources with Config Controller, you must enable the API for those resources in your service perimeter. For example, if you want to add an IAM service account, you must add the IAM API (`iam.googleapis.com`).  For more information about Config Controller, refer to the [product documentation](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview).   
**Limitations** |  The Config Controller integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/using-vpc-sc)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `datafusion.googleapis.com`  
**Details** |  Cloud Data Fusion requires some [special steps](https://docs.cloud.google.com/data-fusion/docs/how-to/using-vpc-sc#set-up-private-connectivity) to protect using VPC Service Controls.  For more information about Cloud Data Fusion, refer to the [product documentation](https://docs.cloud.google.com/data-fusion/docs/how-to/using-vpc-sc).   
**Limitations** | 

  * Establish the VPC Service Controls security perimeter before creating your Cloud Data Fusion private instance. Perimeter protection for instances created prior to setting up VPC Service Controls is not supported.
  * Currently, the Cloud Data Fusion data plane UI does not support identity based access using [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) or [access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example).

  
  
###  [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `datalineage.googleapis.com`  
**Details** |  The API for Data Lineage API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Data Lineage API, refer to the [product documentation](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage).   
**Limitations** |  The Data Lineage API integration with VPC Service Controls has no known limitations.   
  
###  [Compute Engine](https://docs.cloud.google.com/compute/docs/instances/protecting-resources-vpc-service-controls)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `compute.googleapis.com`  
**Details** |  VPC Service Controls support for Compute Engine offers the following security benefits: 

  * Restricts access to sensitive API operations
  * Restricts persistent disk snapshots and custom images to a perimeter
  * Restricts access to instance metadata

VPC Service Controls support for Compute Engine also enables you to utilize Virtual Private Cloud networks and Google Kubernetes Engine clusters with private nodes inside service perimeters.  For more information about Compute Engine, refer to the [product documentation](https://docs.cloud.google.com/compute/docs/instances/protecting-resources-vpc-service-controls).   
**Limitations** | 

  * Configuring a load balancer to use backend services across different projects poses a potential data exfiltration risk. If you add one of these projects to a perimeter, the cross-project backend attachment can still allow data to move between projects even if you restrict the other project within a different perimeter. To mitigate this risk, we recommend that you enable the `constraints/compute.restrictCrossProjectServices` organization policy when you restrict the Compute Engine API within a perimeter. For more information, see [Restrict cross-project backend buckets and backend services](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints#cross-project-bb-bs).
  * [Hierarchical firewalls](https://docs.cloud.google.com/compute/docs/instances/protecting-resources-vpc-service-controls#hierarchical_firewalls) are not affected by service perimeters.
  * VPC Peering operations do not enforce VPC service perimeter restrictions.
  * The [`projects.ListXpnHosts`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/listXpnHosts) API method for Shared VPC does not enforce service perimeter restrictions on returned projects.
  * To enable creating a Compute Engine image from a Cloud Storage in a project protected by a service perimeter, the user that is creating the image should be added temporarily to an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) of the perimeter.
  * VPC Service Controls does not support using the open-source version of Kubernetes on Compute Engine VMs inside a service perimeter.
  * [SSH-in-browser](https://docs.cloud.google.com/compute/docs/ssh-in-browser) is not supported within the perimeter. Use the gcloud CLI instead. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) or [Connecting to a serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#gcloud_2), depending on your use case.
  * The interactive serial console does not support the [ restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configure-routes). If you need to [troubleshoot your instance using the serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console), configure your on-premises DNS resolution to send your commands to `ssh-serialport.googleapis.com` over the internet.

  
  
###  [Customer Experience Insights](https://docs.cloud.google.com/contact-center/insights/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `contactcenterinsights.googleapis.com`  
**Details** |  To use CX Insights with VPC Service Controls you must have the following additional APIs inside your perimeter, depending on your integration. 

  * To load data into CX Insights, add the Cloud Storage API to your service perimeter.
  * To use [export](https://docs.cloud.google.com/contact-center/insights/docs/export), add the BigQuery API to your service perimeter.
  * To integrate multiple CCAI products, add the Agent Platform API to your service perimeter.

For more information about Customer Experience Insights, refer to the [product documentation](https://docs.cloud.google.com/contact-center/insights/docs).   
**Limitations** |  The Customer Experience Insights integration with VPC Service Controls has no known limitations.   
  
###  [Dataflow](https://docs.cloud.google.com/dataflow/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dataflow.googleapis.com`  
**Details** |  Dataflow supports a number of [ storage service connectors](https://beam.apache.org/documentation/io/built-in/). The following connectors have been verified to work with Dataflow inside a service perimeter: 

  * Cloud Storage ([Java ](https://github.com/apache/beam/tree/master/sdks/java/core/src/main/java/org/apache/beam/sdk/io/TextIO.java), [Python ](https://github.com/apache/beam/blob/master/sdks/python/apache_beam/io/gcp/gcsio.py)) 
  * BigQuery ([Java, Python ](https://beam.apache.org/documentation/io/built-in/google-bigquery/)) 
  * Pub/Sub ( [Java ](https://github.com/apache/beam/tree/master/sdks/java/io/google-cloud-platform/src/main/java/org/apache/beam/sdk/io/gcp/pubsub), [Python ](https://github.com/apache/beam/blob/master/sdks/python/apache_beam/io/gcp/pubsub.py)) 
  * Bigtable ([Java ](https://github.com/apache/beam/tree/master/sdks/java/io/google-cloud-platform/src/main/java/org/apache/beam/sdk/io/gcp/bigtable)) 
  * Spanner ([Java ](https://github.com/apache/beam/tree/master/sdks/java/io/google-cloud-platform/src/main/java/org/apache/beam/sdk/io/gcp/spanner)) 

For more information about Dataflow, refer to the [product documentation](https://docs.cloud.google.com/dataflow/docs).   
**Limitations** | 

  * Custom BIND is not supported when using Dataflow. To customize DNS resolution when using Dataflow with VPC Service Controls, use Cloud DNS [private zones](https://docs.cloud.google.com/dns/docs/overview#dns-private-zones) instead of using custom BIND servers. To use your own on-premises DNS resolution, consider using a Google Cloud [DNS forwarding method](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods).
  * [Vertical Autoscaling](https://docs.cloud.google.com/dataflow/docs/vertical-autoscaling) cannot be protected by a VPC Service Controls perimeter. To use Vertical Autoscaling in a VPC Service Controls perimeter, you must disable the [ VPC accessible services feature](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).
**Caution:** Disabling VPC accessible services reduces the security posture.
  * If you enable Dataflow Prime and launch a new job within a VPC Service Controls perimeter, the job uses [Dataflow Prime without Vertical Autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime#features). 
  * Not all storage service connectors have been verified to work when used with Dataflow inside a service perimeter. For a list of verified connectors, see "Details" in the previous section.
  * When using Python 3.5 with Apache Beam SDK 2.20.0‑2.22.0, Dataflow jobs will fail at startup if the workers have private IP addresses only, such as when using VPC Service Controls to protect resources. If Dataflow workers can only have private IP addresses, such as when using VPC Service Controls to protect resources, do not use Python 3.5 with Apache Beam SDK 2.20.0‑2.22.0. This combination causes jobs to fail at startup. 

  
  
###  [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/vpc-sc)

|  |  **Status** |  GA   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dataplex.googleapis.com`  
**Details** |  The API for Knowledge Catalog can be protected by VPC Service Controls and the product can be used normally inside service perimeters. For more information about Knowledge Catalog, refer to the [product documentation](https://docs.cloud.google.com/dataplex/docs/vpc-sc).   
**Limitations** |  Before creating your Knowledge Catalog resources, set up the VPC Service Controls security perimeter. Otherwise, your resources don't have perimeter protection. Knowledge Catalog supports the following resource types:

  * Lake
  * Data profile scan
  * Data quality scan

To function correctly, Knowledge Catalog interacts with BigQuery and Cloud Storage using internal pathways. If you restrict the Knowledge Catalog API within a perimeter but not the BigQuery API or the Cloud Storage API, you might encounter a violation when you initiate a Knowledge Catalog operation. VPC Service Controls attributes the resulting audit log entries to BigQuery or Cloud Storage. To resolve this violation, add the BigQuery API and the Cloud Storage API to both the restricted services list and the [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) list of the same perimeter.  
  
###  [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dataproc.googleapis.com`  
**Details** |  Managed Service for Apache Spark requires [special steps](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity) to protect using VPC Service Controls.  For more information about Managed Service for Apache Spark, refer to the [product documentation](https://docs.cloud.google.com/dataproc/docs).   
**Limitations** |  To protect a Managed Service for Apache Spark cluster with a service perimeter, follow the [Managed Service for Apache Spark and VPC Service Controls networks](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network#and_vpc-sc_networks) instructions.   
  
###  [Managed Service for Apache Spark for Spark](https://docs.cloud.google.com/dataproc-serverless/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dataproc.googleapis.com`  
**Details** |  Managed Service for Apache Spark requires [special steps](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity) to protect using VPC Service Controls.  For more information about Managed Service for Apache Spark for Spark, refer to the [product documentation](https://docs.cloud.google.com/dataproc-serverless/docs).   
**Limitations** |  To protect your serverless workload with a service perimeter, follow the [Managed Service for Apache Spark and VPC Service Controls networks](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/network#s8s-and-vpc-sc-networks) instructions.   
  
###  [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `metastore.googleapis.com`  
**Details** |  The API for Dataproc Metastore can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Dataproc Metastore, refer to the [product documentation](https://docs.cloud.google.com/dataproc-metastore/docs).   
**Limitations** |  The Dataproc Metastore integration with VPC Service Controls has no known limitations.   
  
###  [Datastream](https://docs.cloud.google.com/datastream/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `datastream.googleapis.com`  
**Details** |  The API for Datastream can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Datastream, refer to the [product documentation](https://docs.cloud.google.com/datastream/docs).   
**Limitations** |  The Datastream integration with VPC Service Controls has no known limitations.   
  
###  [Database Center](https://docs.cloud.google.com/database-center/docs/configure-vpc-service-controls)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `databasecenter.googleapis.com`  
**Details** |  The API for Database Center can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Database Center, refer to the [product documentation](https://docs.cloud.google.com/database-center/docs/configure-vpc-service-controls).   
**Limitations** |  VPC Service Controls doesn't support access to folder-level or organization-level Cloud Asset API resources from resources and clients inside a service perimeter. VPC Service Controls protects project-level Cloud Asset API resources. You can specify an egress policy to allow access to project-level Cloud Asset API resources from projects inside the perimeter. To manage Database Center permissions at the folder level or organizational level, we recommend using IAM.   
  
###  [Database Insights API](https://docs.cloud.google.com/alloydb/docs/vpc-sc/configure-vpc-service-controls)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `databaseinsights.googleapis.com`  
**Details** |  The API for Database Insights API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Database Insights API, refer to the [product documentation](https://docs.cloud.google.com/alloydb/docs/vpc-sc/configure-vpc-service-controls).   
**Limitations** |  The Database Insights API integration with VPC Service Controls has no known limitations.   
  
###  [Database Migration Service](https://docs.cloud.google.com/database-migration/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `datamigration.googleapis.com`  
**Details** |  The API for Database Migration Service can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Database Migration Service, refer to the [product documentation](https://docs.cloud.google.com/database-migration/docs).   
**Limitations** | 

  * Service perimeters protect only the Database Migration Service Admin API. They don't protect IP-based data access to underlying databases (such as Cloud SQL instances). To restrict public IP access on Cloud SQL instances, use an [organization policy constraint](https://docs.cloud.google.com/sql/docs/mysql/connection-org-policy#connection-constraints).
  * When you use a Cloud Storage file in the initial dump phase of the migration, add the Cloud Storage bucket to the same service perimeter.
  * When you use a customer-managed encryption key (CMEK) in the destination database, make sure that the CMEK resides in the same service perimeter as the connection profile that contains the key.

  
  
###  [Dialogflow](https://docs.cloud.google.com/dialogflow/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dialogflow.googleapis.com`  
**Details** |  The API for Dialogflow can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Dialogflow, refer to the [product documentation](https://docs.cloud.google.com/dialogflow/docs).   
**Limitations** | 

  * See [Dialogflow ES limitations](https://docs.cloud.google.com/dialogflow/es/docs/vpc-service-controls#limits).
  * See [Dialogflow CX limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/vpc-service-controls#limits).

  
  
###  [Agent Assist](https://docs.cloud.google.com/agent-assist/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dialogflow.googleapis.com`  
**Details** |  The API for Agent Assist can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Agent Assist, refer to the [product documentation](https://docs.cloud.google.com/agent-assist/docs).   
**Limitations** |   
  
###  [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dlp.googleapis.com`  
**Details** |  For information about how to allow Sensitive Data Protection to discover data within a VPC Service Controls perimeter, see [Allow sensitive data discovery within service perimeters](https://docs.cloud.google.com/sensitive-data-protection/docs/allow-discovery-vpcsc).  For more information about Sensitive Data Protection, refer to the [product documentation](https://docs.cloud.google.com/sensitive-data-protection/docs).   
**Limitations** | 

  * Because VPC Service Controls does not currently support folder and organization resources, Sensitive Data Protection calls may return a 403 response when attempting to access organization-level resources. We recommend that IAM is used to manage Sensitive Data Protection permissions at the folder and organization level.

  
  
###  [Distributed Cloud Edge Container API](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `edgecontainer.googleapis.com`  
**Details** |  The API for Distributed Cloud Edge Container API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Distributed Cloud Edge Container API, refer to the [product documentation](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs).   
**Limitations** | 

  * When you restrict `edgecontainer.googleapis.com` in a perimeter, you must grant access at the IP address level to `gkeconnect.googleapis.com` and `sts.googleapis.com` to all machine IP addresses that need to access these endpoints. This is because the Distributed Cloud Edge Container API relies on Workload Identity Federation for GKE on on-premises machines, which cannot be directly added to an allowlist. For more information, see [Configure VPC Service Controls integration](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/deploy#vpc-sc-integration).

  
  
###  [Cloud DNS](https://docs.cloud.google.com/dns/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dns.googleapis.com`  
**Details** |  The API for Cloud DNS can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud DNS, refer to the [product documentation](https://docs.cloud.google.com/dns/docs).   
**Limitations** | 

  * You can access Cloud DNS through the restricted VIP. However you cannot create or update public DNS zones within projects inside the VPC Service Controls perimeter.

  
  
###  [Document AI](https://docs.cloud.google.com/document-ai/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `documentai.googleapis.com`  
**Details** |  The API for Document AI can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Document AI, refer to the [product documentation](https://docs.cloud.google.com/document-ai/docs).   
**Limitations** |  To allow Document AI to access Cloud Storage buckets protected by a service perimeter, you must create an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). This setting is required for scenarios like using customer-managed buckets with processors or viewing documents in the Google Cloud console. These actions use the [Document AI Core Service Agent](https://docs.cloud.google.com/iam/docs/service-agents) (`service-PROJECT_NUMBER@gcp-sa-prod-dai-core.iam.gserviceaccount.com`) to access objects in the bucket (for example, to generate and cache page images and thumbnails). Because this service agent is not part of your perimeter, requests from the agent will be denied with a `NO_MATCHING_ACCESS_LEVEL` violation unless an ingress rule grants access.  Configure an ingress rule for each project whose service agent needs to access buckets within the perimeter.   
  
###  [Document AI Warehouse](https://docs.cloud.google.com/document-warehouse/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `contentwarehouse.googleapis.com`  
**Details** |  The API for Document AI Warehouse can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Document AI Warehouse, refer to the [product documentation](https://docs.cloud.google.com/document-warehouse/docs).   
**Limitations** |  The Document AI Warehouse integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Domains](https://docs.cloud.google.com/domains/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `domains.googleapis.com`  
**Details** |  The API for Cloud Domains can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Domains, refer to the [product documentation](https://docs.cloud.google.com/domains/docs).   
**Limitations** | 

  * The contact data used in Cloud Domains might be shared with the [domain ending or top-level domain (TLD)](https://docs.cloud.google.com/domains/docs/key-terms#terms-tld) registry and might be publicly accessible for [WHOIS/RDAP](https://lookup.icann.org/) as your settings permit, in compliance with [ICANN](https://www.icann.org) rules. For details, see [Privacy protection](https://docs.cloud.google.com/domains/docs/overview#privacy-protection).
  * The DNS configuration data used in Cloud Domains—[name servers](https://docs.cloud.google.com/domains/docs/key-terms#terms-name-servers) and [ DNSSEC settings](https://docs.cloud.google.com/domains/docs/overview#dns_security_dnssec)—is public. If your domain delegates to a public DNS zone, which is the default, then that zone's DNS configuration data is public too.

  
  
###  [Cloud FTP](https://docs.cloud.google.com/cloud-ftp)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `ftp.googleapis.com`  
**Details** |  We recommend placing your Cloud FTP project within the same service perimeter as your Cloud Storage resources. This approach helps protect both your transfers and your Cloud Storage resources. Cloud FTP also supports scenarios where the Cloud FTP project is not in the same perimeter as your Cloud Storage buckets, using an [ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). For setup information, see [Configure VPC Service Controls for Cloud FTP](https://docs.cloud.google.com/cloud-ftp/configure-vpc-service-controls).  For more information about Cloud FTP, refer to the [product documentation](https://docs.cloud.google.com/cloud-ftp).   
**Limitations** | 

  * To use VPC Service Controls with Cloud FTP, you must add both the Cloud FTP API (`ftp.googleapis.com`) and the Cloud Storage API (`storage.googleapis.com`) to your service perimeter.
  * For internal servers, perimeter enforcement is validated only when the server is created. This behavior means that if you change a perimeter after you create an internal server, any perimeter changes (such as perimeter membership, ingress policies, or network associations) aren't detected or enforced on the existing internal server. You must recreate the internal server to enforce the updated perimeter controls.
  * SFTP and SSH sessions don't carry device posture metadata, such as Chrome Enterprise Premium device attributes or Endpoint Verification certificates. This behavior means that ingress rules can enforce only IP address and identity conditions.

  
  
###  [Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `eventarc.googleapis.com,  
eventarcpublishing.googleapis.com`  
**Details** |  Eventarc Advanced APIs can be protected with VPC Service Controls, and features can be used normally inside service perimeters. An Eventarc Advanced bus outside of a service perimeter can't receive events from Google Cloud projects inside the perimeter. An Eventarc Advanced bus inside of a perimeter can't route events to a consumer outside of the perimeter.

  * To publish to an Eventarc Advanced bus, the source of an event must be inside the same service perimeter as the bus. 
  * To consume a message, an event consumer must be inside the same service perimeter as the bus. 

You can verify VPC Service Controls support for the `Enrollment`, `GoogleApiSource`, `MessageBus`, and `Pipeline` resources by viewing platform logs on ingress. For more information about Eventarc Advanced, refer to the [product documentation](https://docs.cloud.google.com/eventarc/advanced/docs).   
**Limitations** |  The Eventarc Advanced integration with VPC Service Controls has no known limitations.   
  
###  [Eventarc Standard](https://docs.cloud.google.com/eventarc/standard/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `eventarc.googleapis.com,  
eventarcpublishing.googleapis.com`  
**Details** |  Eventarc Standard handles event delivery using Pub/Sub topics and push subscriptions. To access the Pub/Sub API and manage event triggers, the Eventarc API must be protected within the same VPC Service Controls service perimeter as the Pub/Sub API.  For more information about Eventarc Standard, refer to the [product documentation](https://docs.cloud.google.com/eventarc/standard/docs).   
**Limitations** |  In projects protected by a service perimeter, the following limitations apply: 

  * Eventarc Standard is bound by the same limitations as Pub/Sub: 
    * When routing events to Cloud Run targets, new Pub/Sub push subscriptions can't be created unless the push endpoints are set to Cloud Run services with default `run.app` URLs (custom domains don't work).
    * When routing events to Workflows targets for which the Pub/Sub push endpoint is set to a Workflows execution, you can only create new Pub/Sub push subscriptions through Eventarc Standard.
In this document, see the [Pub/Sub limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_pubsub). 
  * VPC Service Controls blocks the creation of Eventarc Standard triggers for [internal HTTP endpoints](https://docs.cloud.google.com/eventarc/docs/vpc-endpoints/route-vpc-internal-endpoint-events). VPC Service Controls protection does not apply when routing events to such destinations. 

  
  
###  [Distributed Cloud Edge Network API](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `edgenetwork.googleapis.com`  
**Details** |  The API for Distributed Cloud Edge Network API can be protected by VPC Service Controls and used normally inside service perimeters.  For more information about Distributed Cloud Edge Network API, refer to the [product documentation](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs).   
**Limitations** |  The Distributed Cloud Edge Network API integration with VPC Service Controls has no known limitations.   
  
###  [Anti Money Laundering AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `financialservices.googleapis.com`  
**Details** |  The API for Anti Money Laundering AI can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Anti Money Laundering AI, refer to the [product documentation](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs).   
**Limitations** |  The Anti Money Laundering AI integration with VPC Service Controls has no known limitations.   
  
###  [Firebase AI Logic](https://firebase.google.com/docs/ai-logic)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `firebasevertexai.googleapis.com`  
**Details** |  The API for Firebase AI Logic can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Firebase AI Logic, refer to the [product documentation](https://firebase.google.com/docs/ai-logic).   
**Limitations** | 

  * The Firebase AI Logic API proxies traffic to the [Agent Platform API (`aiplatform.googleapis.com`)](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=_). 
    * Make sure that `aiplatform.googleapis.com` is also added to the restricted services list in the service perimeter. 
    * Any [known limitations of the Agent Platform API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_agent_platform) apply to the Firebase AI Logic API. 
  * Traffic to the Firebase AI Logic API is intended to originate from a mobile or browser client, which will always be outside the service perimeter. So, you need to configure an explicit ingress policy.  If you need to connect to the Agent Platform API from within the service perimeter _only_ , then consider using the Agent Platform API directly or via one of the available services for accessing the Agent Platform API server-side. 

  
  
###  [Firebase App Check](https://firebase.google.com/docs/app-check)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `firebaseappcheck.googleapis.com`  
**Details** |  When you configure and exchange Firebase App Check tokens, VPC Service Controls protects only the Firebase App Check service. To protect services that rely on Firebase App Check, you must set up service perimeters for those services.  For more information about Firebase App Check, refer to the [product documentation](https://firebase.google.com/docs/app-check).   
**Limitations** |  The Firebase App Check integration with VPC Service Controls has no known limitations.   
  
###  [Firebase App Hosting](https://firebase.google.com/docs/app-hosting)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `firebaseapphosting.googleapis.com`  
**Details** |  VPC Service Controls helps protect requests to the App Hosting API. However, VPC Service Controls restrictions don't apply to requests to websites deployed on App Hosting. For more information about Firebase App Hosting, refer to the [product documentation](https://firebase.google.com/docs/app-hosting).   
**Limitations** |  Sites deployed on App Hosting are available on the public internet and cannot be restricted within a service perimeter.  
  
###  [Cloud Storage for Firebase](https://firebase.google.com/docs/storage)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `firebasestorage.googleapis.com`  
**Details** |  The API for Cloud Storage for Firebase can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Storage for Firebase, refer to the [product documentation](https://firebase.google.com/docs/storage).   
**Limitations** |  The Cloud Storage for Firebase integration with VPC Service Controls has no known limitations.   
  
###  [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `firebasecrashlytics.googleapis.com`  
**Details** |  Restricting Firebase Crashlytics in a perimeter also restricts access to Firebase Crashlytics functionality in the Firebase console.  For more information about Firebase Crashlytics, refer to the [product documentation](https://firebase.google.com/docs/crashlytics).   
**Limitations** |  The Firebase Crashlytics integration with VPC Service Controls has no known limitations.   
  
###  [Firebase Data Connect](https://firebase.google.com/docs/data-connect)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `firebasedataconnect.googleapis.com`  
**Details** |  Service perimeters protect only the Firebase Data Connect API. They don't protect access to the underlying data sources (such as Cloud SQL instances). Restricting access on database instances must be configured separately.  For more information about Firebase Data Connect, refer to the [product documentation](https://firebase.google.com/docs/data-connect).   
**Limitations** |  The Firebase Data Connect integration with VPC Service Controls has no known limitations.   
  
###  [Firebase Phone Number Verification](https://firebase.google.com/docs/phone-number-verification)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `fpnv.googleapis.com`  
**Details** |  Service perimeters protect only the Firebase Phone Number Verification API. If you use this service with other services (such as Firebase Authentication or your custom backend), you must also add those other services to the list of restricted services within the service perimeter to ensure they are also protected by VPC Service Controls.  For more information about Firebase Phone Number Verification, refer to the [product documentation](https://firebase.google.com/docs/phone-number-verification).   
**Limitations** |  Firebase Phone Number Verification works by communicating with the user's mobile carrier to retrieve the phone number. These interactions with external mobile carrier networks fall outside the scope of VPC Service Controls enforcements.   
  
###  [Firebase Security Rules](https://firebase.google.com/docs/rules)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `firebaserules.googleapis.com`  
**Details** |  When you manage Firebase Security Rules policies VPC Service Controls protects only the Firebase Security Rules service. To protect services that rely on Firebase Security Rules, you must set up service permiters for those services.  For more information about Firebase Security Rules, refer to the [product documentation](https://firebase.google.com/docs/rules).   
**Limitations** |  The Firebase Security Rules integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Run functions](https://docs.cloud.google.com/functions/docs/securing/using-vpc-service-controls)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudfunctions.googleapis.com`  
**Details** |  See the [Cloud Run functions documentation](https://docs.cloud.google.com/functions/docs/securing/using-vpc-service-controls) for setup steps. VPC Service Controls protection does not apply to the build phase when Cloud Run functions are built using Cloud Build. For more details, see the known limitations.  For more information about Cloud Run functions, refer to the [product documentation](https://docs.cloud.google.com/functions/docs/securing/using-vpc-service-controls).   
**Limitations** | 

  * Cloud Run functions uses Cloud Build, Container Registry, and Cloud Storage to build and manage your source code in a runnable container. If any of these services are restricted by the service perimeter, VPC Service Controls blocks the Cloud Run functions build, even if Cloud Run functions is not added as a restricted service to the perimeter. To use Cloud Run functions inside a service perimeter, you must configure an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the Cloud Build service account in your service perimeter.
  * To allow your functions to use external dependencies such as npm packages, Cloud Build has unlimited internet access. This internet access could be used to exfiltrate data that is available at build time, such as your uploaded source code. If you want to mitigate this exfiltration vector, we recommend that you only allow trusted developers to deploy functions. Do not grant [Cloud Run functions Owner, Editor, or Developer IAM roles](https://docs.cloud.google.com/functions/docs/concepts/iam#access_control_for_users) to untrusted developers.
  * When you specify an ingress or egress policy for a service perimeter, you cannot use `ANY_SERVICE_ACCOUNT` and `ANY_USER_ACCOUNT` as an identity type to deploy [Cloud Run functions](https://docs.cloud.google.com/functions/docs) from a [local machine](https://docs.cloud.google.com/functions/docs/deploying/filesystem).  As a workaround, use `ANY_IDENTITY` as the identity type. 
  * When Cloud Run functions services are invoked by HTTP triggers, VPC Service Controls policy enforcement does not use the client's IAM authentication information. VPC Service Controls ingress policy rules that use IAM principals are not supported. Access levels for VPC Service Controls perimeters that use IAM principals are not supported.

  
  
###  [Identity and Access Management](https://docs.cloud.google.com/iam/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `iam.googleapis.com`  
**Details** |  When you restrict IAM with a perimeter, only actions that use the Identity and Access Management API are restricted. These actions include the following: 

  * Managing custom IAM roles
  * Managing workload identity pools
  * Managing service accounts and keys
  * Managing deny policies
  * Managing policy bindings for principal access boundary policies

The perimeter _doesn't_ restrict actions related to workforce pools and principal access boundary policies because those resources are created at the organization level.  The perimeter also _doesn't_ restrict allow policy management for resources owned by other services, like Resource Manager projects, folders, and organizations or Compute Engine virtual machine instances. To restrict allow policy management for these resources, create a perimeter that restricts the service that owns the resources. For a list of resources that accept allow policies and the services that own them, see [Resource types that accept allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies).  Additionaly, the perimeter around IAM _doesn't_ restrict actions that use other APIs, including the following: 

  * IAM Policy Simulator API
  * IAM Policy Troubleshooter API
  * Security Token Service API
  * Service Account Credentials API (including the legacy `signBlob` and `signJwt` methods in the IAM API)

For more information about Identity and Access Management, refer to the [product documentation](https://docs.cloud.google.com/iam/docs).   
**Limitations** |  If you are inside the perimeter, you cannot call the [`roles.list`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/list) method with an empty string to list IAM predefined roles. If you need to view predefined roles, see [IAM role documentation](https://docs.cloud.google.com/iam/docs/roles-permissions).   
  
###  [IAP Admin API ](https://docs.cloud.google.com/iap)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `iap.googleapis.com`  
**Details** |  IAP Admin API enables users to configure IAP.  For more information about IAP Admin API , refer to the [product documentation](https://docs.cloud.google.com/iap).   
**Limitations** |  The IAP Admin API integration with VPC Service Controls has no known limitations.   
  
###  [Cloud KMS Inventory API](https://docs.cloud.google.com/kms/docs/reference/inventory/rest)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `kmsinventory.googleapis.com`  
**Details** |  The API for Cloud KMS Inventory API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud KMS Inventory API, refer to the [product documentation](https://docs.cloud.google.com/kms/docs/reference/inventory/rest).   
**Limitations** |  The SearchProtectedResources API method does not enforce service perimeter restrictions on returned projects.   
  
###  [Service Account Credentials](https://docs.cloud.google.com/iam/docs/reference/credentials/rest)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `iamcredentials.googleapis.com`  
**Details** |  The API for Service Account Credentials can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Service Account Credentials, refer to the [product documentation](https://docs.cloud.google.com/iam/docs/reference/credentials/rest).   
**Limitations** |  The Service Account Credentials integration with VPC Service Controls has no known limitations.   
  
###  [Service Metadata API](https://docs.cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloud.googleapis.com`  
**Details** |  The API for Service Metadata API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Service Metadata API, refer to the [product documentation](https://docs.cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest).   
**Limitations** |  The Service Metadata API integration with VPC Service Controls has no known limitations.   
  
###  [Service Networking](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **No.** The API for Service Networking cannot be protected by service perimeters. However, Service Networking can be used normally in projects inside a perimeter.   
**Details** |  If you're using private service access, we recommend enabling VPC Service Controls for the Service Networking connection.When you enable VPC Service Controls, service producers are restricted to access only the APIs supported by VPC Service Controls over the Service Networking connection. You can enable VPC Service Controls for Service Networking only using the [EnableVpcServiceControls API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/enableVpcServiceControls). You can disable VPC Service Controls for Service Networking only using [DisableVpcServiceControls API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/disableVpcServiceControls). For more information about Service Networking, refer to the [product documentation](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started).   
**Limitations** |  The Service Networking integration with VPC Service Controls has no known limitations.   
  
###  [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `vpcaccess.googleapis.com`  
**Details** |  The API for Serverless VPC Access can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Serverless VPC Access, refer to the [product documentation](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access).   
**Limitations** |  The Serverless VPC Access integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudkms.googleapis.com`  
**Details** |  The Cloud KMS API can be protected by VPC Service Controls and the product can be used inside service perimeters. The access to Cloud HSM services is also protected by VPC Service Controls and can be used inside service perimeters.  For more information about Cloud Key Management Service, refer to the [product documentation](https://docs.cloud.google.com/kms/docs).   
**Limitations** |  The Cloud Key Management Service integration with VPC Service Controls has no known limitations.   
  
###  [Game Servers](https://docs.cloud.google.com/game-servers/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `gameservices.googleapis.com`  
**Details** |  The API for Game Servers can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Game Servers, refer to the [product documentation](https://docs.cloud.google.com/game-servers/docs).   
**Limitations** |  The Game Servers integration with VPC Service Controls has no known limitations.   
  
###  [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `geminicloudassist.googleapis.com`  
**Details** |  Gemini Cloud Assist can be protected by VPC Service Controls. Gemini Cloud Assist can only access the data and APIs that also reside within the service perimeter. See [ Gemini Cloud Assist API recommendations](https://docs.cloud.google.com/cloud-assist/api-recommendations) for information about APIs that are important for Gemini Cloud Assist to function. Similarly, any product or service that you want Gemini Cloud Assist to examine should reside within the perimeter for the best results.  For more information about Gemini Cloud Assist, refer to the [product documentation](https://docs.cloud.google.com/cloud-assist/overview).   
**Limitations** |  Gemini Cloud Assist also uses the `cloudaicompanion.googleapis.com` API for some of its functionality. You must also include the `cloudaicompanion.googleapis.com` API in your service perimeter for full functionality of Gemini Cloud Assist. If a project is contained within a service perimeter, but the project hasn't yet enabled Gemini Cloud Assist, attempts to enable it using the Google Cloud console result in an error. This error occurs because the Google Cloud console requires the App Optimize API to also be enabled, but the App Optimize API is not supported by VPC Service Controls. To avoid this error, [enable Gemini Cloud Assist using the gcloud CLI](https://docs.cloud.google.com/cloud-assist/set-up-gemini).  
  
###  [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudaicompanion.googleapis.com`  
**Details** |  The API for Gemini Code Assist can be protected by VPC Service Controls and the product can be used normally inside service perimeters. This includes [code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview).  For more information about Gemini Code Assist, refer to the [product documentation](https://docs.cloud.google.com/gemini/docs/codeassist/overview).   
**Limitations** |  Access control based on device, public IP address, or location is not supported for Gemini in the Google Cloud console.   
  
###  [Identity-Aware Proxy for TCP](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `iaptunnel.googleapis.com`  
**Details** |  The API for Identity-Aware Proxy for TCP can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Identity-Aware Proxy for TCP, refer to the [product documentation](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview).   
**Limitations** | 

  * Only the usage API of IAP for TCP can be protected by a perimeter. The administrative API cannot be protected by a perimeter.
  * To use IAP for TCP within a VPC Service Controls service perimeter, you must [add or configure some DNS entries](https://docs.cloud.google.com/iap/docs/securing-tcp-with-vpc-sc#configure-dns) to point the following domains to the restricted VIP:
    * tunnel.cloudproxy.app
    * *.tunnel.cloudproxy.app

  
  
###  [Cloud Life Sciences](https://docs.cloud.google.com/life-sciences/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `lifesciences.googleapis.com`  
**Details** |  The API for Cloud Life Sciences can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Life Sciences, refer to the [product documentation](https://docs.cloud.google.com/life-sciences/docs).   
**Limitations** |  The Cloud Life Sciences integration with VPC Service Controls has no known limitations.   
  
###  [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `managedidentities.googleapis.com`  
**Details** |  Additional configuration required for: 

  * [On-premises access to the Managed Microsoft AD API](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-vpc-service-controls#on_prem_api)
  * [Shared VPC](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-vpc-service-controls#shared_vpc)

For more information about Managed Service for Microsoft Active Directory, refer to the [product documentation](https://docs.cloud.google.com/managed-microsoft-ad/docs).   
**Limitations** |  The Managed Service for Microsoft Active Directory integration with VPC Service Controls has no known limitations.   
  
###  [Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `recaptchaenterprise.googleapis.com`  
**Details** |  The API for Fraud Defense can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Fraud Defense, refer to the [product documentation](https://docs.cloud.google.com/recaptcha/docs/overview).   
**Limitations** |  The Fraud Defense integration with VPC Service Controls has no known limitations.   
  
###  [Web Risk](https://docs.cloud.google.com/web-risk/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `webrisk.googleapis.com`  
**Details** |  The API for Web Risk can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Web Risk, refer to the [product documentation](https://docs.cloud.google.com/web-risk/docs/overview).   
**Limitations** |  The Evaluate API and the Submission API are not supported by VPC Service Controls.   
  
###  [Recommender](https://docs.cloud.google.com/recommender/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `recommender.googleapis.com`  
**Details** |  The API for Recommender can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Recommender, refer to the [product documentation](https://docs.cloud.google.com/recommender/docs/overview).   
**Limitations** | 

  * VPC Service Controls doesn't support organization, folder, or billing account resources.

  
  
###  [Secret Manager](https://docs.cloud.google.com/secret-manager/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `secretmanager.googleapis.com`  
**Details** |  The API for Secret Manager can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Secret Manager, refer to the [product documentation](https://docs.cloud.google.com/secret-manager/docs).   
**Limitations** |  The Secret Manager integration with VPC Service Controls has no known limitations.   
  
###  [Pub/Sub](https://docs.cloud.google.com/pubsub/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `pubsub.googleapis.com`  
**Details** |  VPC Service Controls protection applies to all administrator operations, publisher operations, and subscriber operations (except for existing push subscriptions).  For more information about Pub/Sub, refer to the [product documentation](https://docs.cloud.google.com/pubsub/docs).   
**Limitations** |  In projects protected by a service perimeter, the following limitations apply: 

  * You must create the subscription in the same perimeter as the topic, or enable egress rules to allow access from the topic to the subscription.
  * New push subscriptions can't be created unless the push endpoints are set to Cloud Run services with default `run.app` URLs or a Workflows execution ([custom domains](https://docs.cloud.google.com/run/docs/mapping-custom-domains) don't work). For more information about integrating with Cloud Run, see [Using VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls).
  * When routing events through Eventarc to Workflows targets for which the push endpoint is set to a Workflows execution, you can only create new push subscriptions through Eventarc.
  * Pub/Sub subscriptions created prior to the service perimeter are not blocked.

  
  
###  [Pub/Sub Lite](https://docs.cloud.google.com/pubsub/lite/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `pubsublite.googleapis.com`  
**Details** |  VPC Service Controls protection applies to all subscriber operations.  For more information about Pub/Sub Lite, refer to the [product documentation](https://docs.cloud.google.com/pubsub/lite/docs).   
**Limitations** |  The Pub/Sub Lite integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Build](https://docs.cloud.google.com/build/docs)

|  |  **Status** |  **GA**. This product integration is supported by VPC Service Controls. Refer to details and limitations for more information.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudbuild.googleapis.com`  
**Details** |  Use [VPC Service Controls with Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls) to add additional security to your builds.  For more information about Cloud Build, refer to the [product documentation](https://docs.cloud.google.com/build/docs).   
**Limitations** | 

  * VPC Service Controls protection is available only for builds run in [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).
  * [Cloud Build Pub/Sub triggers](https://docs.cloud.google.com/build/docs/automate-builds-pubsub-events) are not supported.

  
  
###  [Cloud Deploy](https://docs.cloud.google.com/deploy/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `clouddeploy.googleapis.com`  
**Details** |  The API for Cloud Deploy can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Deploy, refer to the [product documentation](https://docs.cloud.google.com/deploy/docs).   
**Limitations** |  To use Cloud Deploy in a perimeter, you must use a Cloud Build private pool for the target's [execution environments](https://docs.cloud.google.com/deploy/docs/execution-environment). Don't use the default (Cloud Build) worker pool, and don't use a hybrid pool.  
  
###  [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs)

|  |  **Status** |  GA   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `composer.googleapis.com`  
**Details** |  [Configuring Composer for use with VPC Service Controls](https://docs.cloud.google.com/composer/docs/configuring-vpc-sc) For more information about Managed Service for Apache Airflow, refer to the [product documentation](https://docs.cloud.google.com/composer/docs).   
**Limitations** | 

  * Enabling DAG serialization prevents Airflow from displaying a rendered template with functions in the web UI.
  * Setting the `async_dagbag_loader` flag to `True` is not supported while DAG serialization is enabled.
  * Enabling DAG serialization disables all Airflow web server plugins, as they could risk the security of the VPC network where Managed Airflow is deployed. This doesn't impact the behaviour of scheduler or worker plugins, including Airflow operators and sensors.
  * When Managed Airflow is running inside a perimeter, access to public PyPI repositories is restricted. In the Managed Airflow documentation, see [Installing Python dependencies](https://docs.cloud.google.com/composer/docs/how-to/using/installing-python-dependencies#install-private) to learn how to install PyPi modules in Private IP mode.
  * Managed Airflow doesn't support using [third-party identities](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups) in ingress and egress rules for [Apache Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface) operations. However, you can use the `ANY_IDENTITY` identity type in ingress and egress rules to allow access to all identities, including third-party identities. For more information about the `ANY_IDENTITY` identity type, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

  
  
###  [Cloud Quotas](https://docs.cloud.google.com/docs/quotas)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudquotas.googleapis.com`  
**Details** |  The API for Cloud Quotas can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Quotas, refer to the [product documentation](https://docs.cloud.google.com/docs/quotas).   
**Limitations** | 

  * Because VPC Service Controls enforces boundaries at the project level, Cloud Quotas requests that originate from clients within the perimeter can only access organization resources if the organization sets up an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference). 
  * When requesting a [quota decrease](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/patch) , Cloud Quotas executes a service to service (S2S) call to Monitoring. This S2S call does not originate from within the perimeter even if the decrease request does, therefore, it will be blocked by VPC Service Controls. To avoid this issue, you can either:
    * Set the `ignoreSafetyChecks` [query parameter](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/patch#query-parameters) with the value of `[QUOTA_DECREASE_BELOW_USAGE](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/QuotaSafetyCheck)`. 
    * Create an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) that allows the S2S call from your identity and all sources to Monitoring to the project where you request the quota decrease. 

To set up an ingress or egress rule, see the VPC Service Controls instructions for [configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).   
  
###  [Cloud Run](https://docs.cloud.google.com/run/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `run.googleapis.com`  
**Details** |  Additional setup for Cloud Run is required. Follow the instructions at the Cloud Run [VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls) documentation page.  For more information about Cloud Run, refer to the [product documentation](https://docs.cloud.google.com/run/docs).   
**Limitations** | 

  * For Artifact Registry and Container Registry, the registry where you store your container must be in the same VPC Service Controls perimeter as the project that you are deploying to. The code being built must be in the same VPC Service Controls perimeter as the registry that the container is being pushed to.
  * The Cloud Run [continuous deployment](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build) feature is not available for projects inside a VPC Service Controls perimeter.
  * When Cloud Run services are invoked, VPC Service Controls policy enforcement does not use the client's IAM authentication information. Such requests have the following limitations:
    * VPC Service Controls ingress policy rules that use IAM principals are not supported. Only the `ANY_IDENTITY` identity type is supported.
    * Access levels for VPC Service Controls perimeters that use IAM principals are not supported.
  * Enforcement of VPC Service Controls egress policy is only guaranteed when using the [restricted virtual IP (VIP) address](https://cloud.google.com/vpc-service-controls/docs/private-connectivity).
  * Requests from the same project on non-restricted VIPs are allowed, even if Cloud Run is not configured as a [VPC accessible service](https://cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).

  
  
###  [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudscheduler.googleapis.com`  
**Details** |  VPC Service Controls is enforced on the following actions:  


  * Cloud Scheduler job creations
  * Cloud Scheduler job updates

For more information about Cloud Scheduler, refer to the [product documentation](https://docs.cloud.google.com/scheduler/docs).   
**Limitations** |  VPC Service Controls supports Cloud Scheduler jobs only with the following targets:  


  * Cloud Run services—must use the canonical default `run.app` domain. Custom domains and custom DNS are not supported.
  * Cloud Run functions—must use the canonical default `cloudfunctions.net` or `run.app` domain. Custom domains and custom DNS are not supported.
  * Google Cloud APIs that are VPC Service Controls-compliant (either in Preview or GA) can be in a different Google Cloud project from your Cloud Scheduler job. 
    * You must use the global endpoint format (`https://SERVICE.googleapis.com`).
    * Regional endpoints—such as `*.rep.googleapis.com`, `LOCATION.SERVICE.googleapis.com`, and `REGION-SERVICE.googleapis.com`—and mTLS endpoints (`*.mtls.googleapis.com`) are rejected.
  * Pub/Sub

Custom domains for serverless endpoints are not supported, and runtime invocations to custom domains are blocked by the destination service even for pre-existing jobs. For more information, see [Secure cron jobs with VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc).   
  
###  [Spanner](https://docs.cloud.google.com/spanner/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `spanner.googleapis.com`  
**Details** |  The API for Spanner can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Spanner, refer to the [product documentation](https://docs.cloud.google.com/spanner/docs).   
**Limitations** |  The Spanner integration with VPC Service Controls has no known limitations.   
  
###  [Speaker ID](https://docs.cloud.google.com/speaker-id/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `speakerid.googleapis.com`  
**Details** |  The API for Speaker ID can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Speaker ID, refer to the [product documentation](https://docs.cloud.google.com/speaker-id/docs).   
**Limitations** |  The Speaker ID integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Storage](https://docs.cloud.google.com/storage/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `storage.googleapis.com`  
**Details** |  The API for Cloud Storage can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Storage, refer to the [product documentation](https://docs.cloud.google.com/storage/docs).   
**Limitations** | 

  * When using the [Requester Pays feature](https://docs.cloud.google.com/storage/docs/requester-pays) with a storage bucket _inside_ a service perimeter that protects the Cloud Storage service, you cannot identify a project to pay that is _outside_ the perimeter. The target project must be in the same perimeter as the storage bucket or in a perimeter bridge with the bucket's project. For more information about Requester Pays, see the [Requester Pays use and access requirements](https://docs.cloud.google.com/storage/docs/requester-pays#requirements).
  * For projects in a service perimeter, the Cloud Storage page in the Google Cloud console is not accessible if the Cloud Storage API is protected by that perimeter. If you want to grant access to the page, you must create an ingress rule and/or access level that includes the user accounts and/or public IP range that you want to allow to access the Cloud Storage API.
  * In audit log records, the `resourceName` field does not identify the project that owns a bucket. The [project must be discovered separately](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#dataproc_example).
  * In audit log records, the value for `methodName` is not always correct. We recommend that you do _not_ filter Cloud Storage audit log records by `methodName`.
  * In certain cases, Cloud Storage legacy bucket logs can be written to destinations outside of a service perimeter even when access is denied.
  * In certain cases, Cloud Storage objects that were public are accessible even after you enable VPC Service Controls on the objects. The objects are accessible until they expire from the built-in caches and any other upstream caches on the network between the end user and Cloud Storage. Cloud Storage caches publicly accessible data by default in the Cloud Storage network. For more information about how Cloud Storage objects are cached, see [Cloud Storage](https://docs.cloud.google.com/storage/docs/caching) For information about the length of time an object may be cached, see [Cache-control metadata](https://docs.cloud.google.com/storage/docs/metadata#cache-control). 
  * When you specify an ingress or egress policy for a service perimeter, you cannot use `ANY_SERVICE_ACCOUNT` and `ANY_USER_ACCOUNT` as an identity type for all [Cloud Storage](https://docs.cloud.google.com/storage/docs) operations using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).  As a workaround, use `ANY_IDENTITY` as the identity type. 
  * [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) support VPC Service Controls. VPC Service Controls uses the signing credentials of the user or service account that signed the signed URL to evaluate VPC Service Controls checks, not the caller or user credential initiating the connection.  However, VPC Service Controls blocks access to the signed URL from outside the perimeter based on the network origin of the request. To allow this access, you must define an [access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) or [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) in the perimeter.
  * VPC Service Controls protects the [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview) and [Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview) APIs.  VPC Service Controls does not support adding folder-level or organization-level resources to service perimeters. Therefore, while you can enable and use Storage Intelligence and Storage Intelligence advisor at the folder, organization, or project level, VPC Service Controls protects only project-level resources. To control access to Storage Intelligence and Storage Intelligence advisor at the folder or organization level, use IAM. 

  
  
###  [Cloud Tasks](https://docs.cloud.google.com/tasks/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudtasks.googleapis.com`  
**Details** |  The API for Cloud Tasks can be protected by VPC Service Controls and the product can be used normally inside service perimeters. HTTP requests from Cloud Tasks executions are supported as follows: 

  * Authenticated requests to VPC Service Controls-compliant Cloud Run functions and Cloud Run endpoints are allowed.
  * Requests to non-Cloud Run functions and non-Cloud Run endpoints are blocked. 
  * Requests to non-VPC Service Controls-compliant Cloud Run functions and Cloud Run endpoints are blocked.

For more information about Cloud Tasks, refer to the [product documentation](https://docs.cloud.google.com/tasks/docs).   
**Limitations** |  VPC Service Controls only supports Cloud Tasks requests to the following targets: 

  * Cloud Run functions `functions.net` endpoints
  * Cloud Run `run.app` endpoints

For more information, see [Set up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/tasks/docs/use-vpc-service-controls).   
  
###  [Cloud SQL](https://docs.cloud.google.com/sql/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `sqladmin.googleapis.com`  
**Details** |  VPC Service Controls perimeters protect the Cloud SQL Admin API.  For more information about Cloud SQL, refer to the [product documentation](https://docs.cloud.google.com/sql/docs).   
**Limitations** | 

  * Service perimeters protect only the Cloud SQL Admin API. They do not protect IP-based data access to Cloud SQL instances. You need to use an [organization policy constraint](https://docs.cloud.google.com/sql/docs/mysql/connection-org-policy) to restrict public IP access on Cloud SQL instances.
  * Before you configure VPC Service Controls for Cloud SQL, enable the Service Networking API.
  * Cloud SQL imports and exports can only perform reads and writes from a Cloud Storage bucket within the same service perimeter as the Cloud SQL replica instance.
  * In the [external server migration flow](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external#process), you need to add the Cloud Storage bucket to the same service perimeter.
  * In the [key creation](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#key) flow for CMEK, use one of the following configurations:
    * Create the key in the same service perimeter as the resources that use it, such as Cloud SQL.
    * Create the key in a service perimeter that's connected, through a [perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters), to the service perimeter that protects Cloud SQL.
  * When restoring an instance from a backup, the target instance needs to reside in the same service perimeter as the backup.
  * When performing a cross-project [point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr), the target instance needs to reside in the same service perimeter as the source instance.
  * [AI-assisted troubleshooting](https://docs.cloud.google.com/sql/docs/mysql/monitor-troubleshoot-with-ai#limitations) [(Preview) ](https://cloud.google.com/products#product-launch-stages) is not supported for Cloud SQL instances inside a service perimeter.

  
  
###  [Video Intelligence API](https://docs.cloud.google.com/video-intelligence/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `videointelligence.googleapis.com`  
**Details** |  The API for Video Intelligence API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Video Intelligence API, refer to the [product documentation](https://docs.cloud.google.com/video-intelligence/docs).   
**Limitations** |  Video Intelligence API does not enforce VPC Service Controls egress restrictions on the output destination of `videos:annotate` requests. The service agent can write annotation results to the Cloud Storage bucket specified in `outputUri` even when that bucket is outside of the service perimeter. To prevent data exfiltration, ensure that the bucket referenced by `outputUri` is inside the same service perimeter as the input bucket.   
  
###  [Cloud Vision API](https://docs.cloud.google.com/vision/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `vision.googleapis.com`  
**Details** |  The API for Cloud Vision API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Vision API, refer to the [product documentation](https://docs.cloud.google.com/vision/docs).   
**Limitations** |  Even if you create an egress rule to allow calls to public URLs from within VPC Service Controls perimeters, Cloud Vision API blocks calls to public URLs.   
  
###  [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/aa-vpc-sc-service-perimeter)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `containeranalysis.googleapis.com`  
**Details** |  To use Artifact Analysis with VPC Service Controls, you may have to add other services to your VPC perimeter: 

  * If you are using [Pub/Sub notifications](https://docs.cloud.google.com/artifact-analysis/docs/pub-sub-notifications) with Artifact Analysis, add Pub/Sub to your service perimeter. 
  * If you are using the [Container Scanning API](https://docs.cloud.google.com/artifact-analysis/docs/enabling-disabling-container-analysis), add your registry to the perimeter: Artifact Registry or Container Registry. 

Because the Container Scanning API is a surfaceless API that stores the results in Artifact Analysis, you do not need to protect the API with a service perimeter.  For more information about Artifact Analysis, refer to the [product documentation](https://docs.cloud.google.com/artifact-analysis/docs/aa-vpc-sc-service-perimeter).   
**Limitations** |  The Artifact Analysis integration with VPC Service Controls has no known limitations.   
  
###  [Container Registry](https://docs.cloud.google.com/container-registry/docs)

|  |  **Status** |  **Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).  
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `containerregistry.googleapis.com`  
**Details** |  In addition to protecting the Container Registry API, Container Registry can be used inside a service perimeter with GKE and Compute Engine.  For more information about Container Registry, refer to the [product documentation](https://docs.cloud.google.com/container-registry/docs).   
**Limitations** | 

  * When you specify an ingress or egress policy for a service perimeter, you cannot use `ANY_SERVICE_ACCOUNT` and `ANY_USER_ACCOUNT` as an identity type for all [Container Registry](https://docs.cloud.google.com/container-registry/docs) operations.  As a workaround, use `ANY_IDENTITY` as the identity type. 
  * Because Container Registry uses the `gcr.io` domain, you must [configure DNS](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring-dns) for `*.gcr.io` to map to either `private.googleapis.com` or `restricted.googleapis.com`. For more information, see [Securing Container Registry in a service perimeter](https://docs.cloud.google.com/container-registry/docs/securing-with-vpc-sc).
  * In addition to the containers inside a perimeter that are available to Container Registry, the following read-only repositories are available to all projects regardless of any restrictions enforced by service perimeters:
    * `gcr.io/anthos-baremetal-release`
    * `gcr.io/asci-toolchain`
    * `gcr.io/cloud-airflow-releaser`
    * `gcr.io/cloud-builders`
    * `gcr.io/cloud-dataflow`
    * `gcr.io/cloud-ingest`
    * `gcr.io/cloud-marketplace`
    * `gcr.io/cloud-ssa`
    * `gcr.io/cloudsql-docker`
    * `gcr.io/config-management-release`
    * `gcr.io/deeplearning-platform-release`
    * `gcr.io/foundry-dev`
    * `gcr.io/fn-img`
    * `gcr.io/gae-runtimes`
    * `gcr.io/serverless-runtimes`
    * `gcr.io/gke-node-images`
    * `gcr.io/gke-release`
    * `gcr.io/gkeconnect`
    * `gcr.io/google-containers`
    * `gcr.io/kubeflow`
    * `gcr.io/kubeflow-images-public`
    * `gcr.io/kubernetes-helm`
    * `gcr.io/istio-release`
    * `gcr.io/ml-pipeline`
    * `gcr.io/projectcalico-org`
    * `gcr.io/rbe-containers`
    * `gcr.io/rbe-windows-test-images`
    * `gcr.io/speckle-umbrella`
    * `gcr.io/stackdriver-agents`
    * `gcr.io/tensorflow`
    * `gcr.io/vertex-ai`
    * `gcr.io/vertex-ai-restricted`
    * `gke.gcr.io`
    * `k8s.gcr.io`
In all cases, the multi-regional versions of these repositories are also available.

  
  
###  [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `container.googleapis.com`  
**Details** |  The Kubernetes Engine API can be protected by VPC Service Controls and the product can be used normally inside service perimeters. This compatibility includes the protection of the [DNS endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#dns-based_endpoint) for GKE, which is a service for accessing the cluster's control plane and uses the `*.gke.goog` domain. When you restrict the `container.googleapis.com` service in a perimeter, the perimeter also restricts the DNS endpoint for GKE. For more information about Google Kubernetes Engine, refer to the [product documentation](https://docs.cloud.google.com/kubernetes-engine/docs).   
**Limitations** | 

  * To fully protect the GKE API, you must include the Kubernetes Metadata API (`kubernetesmetadata.googleapis.com`) as well in your perimeter.
  * The GKE service entry in this table only specifies the control of the GKE API itself. GKE relies on several other underlying services for its operation, such as Compute Engine, Cloud Logging, Cloud Monitoring, and the Autoscaling API (`autoscaling.googleapis.com`). To effectively secure your GKE environments with VPC Service Controls, you must ensure that all necessary underlying services are also included within your service perimeter. See the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) for a complete list of these services.

  
  
###  [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `chronicle.googleapis.com,  
chronicleservicemanager.googleapis.com`  
**Details** |  The APIs for Google Security Operations can be protected by VPC Service Controls and Google SecOps can be used normally inside service perimeters. To use Google SecOps from within VPC Service Controls perimeters, see [Configure VPC Service Controls for Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops).  For more information about Google Security Operations, refer to the [product documentation](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview).   
**Limitations** |  For information about the limitations of using Google Security Operations with VPC Service Controls, see [VPC Service Controls for Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops#limitations).   
  
###  [Container Security API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `containersecurity.googleapis.com`  
**Details** |  The API for Container Security API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Container Security API, refer to the [product documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard).   
**Limitations** |  The Container Security API integration with VPC Service Controls has no known limitations.   
  
###  [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `containerfilesystem.googleapis.com`  
**Details** |  Image streaming is a data streaming feature that provides shorter container image pull times for images stored in Artifact Registry for products like GKE, Batch, Dataflow, Managed Service for Apache Spark, and Cloud Workstations. If VPC Service Controls protects your container images and you use Image streaming, you must also include the Image streaming API in the service perimeter.  For more information about Image streaming, refer to the [product documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming).   
**Limitations** | 

  * The following read-only repositories are available to all projects regardless of any restrictions enforced by service perimeters:
    * `gcr.io/anthos-baremetal-release`
    * `gcr.io/asci-toolchain`
    * `gcr.io/cloud-airflow-releaser`
    * `gcr.io/cloud-builders`
    * `gcr.io/cloud-dataflow`
    * `gcr.io/cloud-ingest`
    * `gcr.io/cloud-marketplace`
    * `gcr.io/cloud-ssa`
    * `gcr.io/cloudsql-docker`
    * `gcr.io/config-management-release`
    * `gcr.io/deeplearning-platform-release`
    * `gcr.io/foundry-dev`
    * `gcr.io/fn-img`
    * `gcr.io/gae-runtimes`
    * `gcr.io/serverless-runtimes`
    * `gcr.io/gke-node-images`
    * `gcr.io/gke-release`
    * `gcr.io/gkeconnect`
    * `gcr.io/google-containers`
    * `gcr.io/kubeflow`
    * `gcr.io/kubeflow-images-public`
    * `gcr.io/kubernetes-helm`
    * `gcr.io/istio-release`
    * `gcr.io/ml-pipeline`
    * `gcr.io/projectcalico-org`
    * `gcr.io/rbe-containers`
    * `gcr.io/rbe-windows-test-images`
    * `gcr.io/speckle-umbrella`
    * `gcr.io/stackdriver-agents`
    * `gcr.io/tensorflow`
    * `gcr.io/vertex-ai`
    * `gcr.io/vertex-ai-restricted`
    * `gke.gcr.io`
    * `k8s.gcr.io`

  
  
###  [Fleets](https://docs.cloud.google.com/anthos/multicluster-management)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `gkeconnect.googleapis.com,  
gkehub.googleapis.com,  
connectgateway.googleapis.com`  
**Details** |  Fleet management APIs, including the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway), can be protected with VPC Service Controls, and fleet management features can be used normally inside service perimeters. For more information, see the following: 

  * [Use VPC Service Controls with the Connect Agent](https://docs.cloud.google.com/anthos/multicluster-management/connect/security-features#data_security_with)
  * [Use VPC Service Controls with the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway/setup#support)

For more information about Fleets, refer to the [product documentation](https://docs.cloud.google.com/anthos/multicluster-management).   
**Limitations** | 

  * Although all fleet management features can be used normally, enabling a service perimeter around the Stackdriver API restricts the Policy Controller fleet feature from integrating with Security Command Center. 
  * When using the Connect gateway to access GKE clusters, VPC Service Controls perimeter for `container.googleapis.com` is not enforced. 

  
  
###  [`FleetPackage` API](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/fleet-packages)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `configdelivery.googleapis.com`  
**Details** |  The API for `FleetPackage` API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about `FleetPackage` API, refer to the [product documentation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/fleet-packages).   
**Limitations** |  The `FleetPackage` API integration with VPC Service Controls has no known limitations.   
  
###  [Resource Manager](https://docs.cloud.google.com/resource-manager/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudresourcemanager.googleapis.com [ ](https://cloud.google.com/products/#product-launch-stages) `  
**Details** |  The following Cloud Resource Manager API methods can be protected by VPC Service Controls:

  * [v1 `project.setIAMPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)
  * [v1beta1 `project.setIAMPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/setIamPolicy)
  * [v3 `tagKeys.*`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys)
  * [v3 `tagValues.*`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues)
  * [v3 `tagValues.tagHolds.*`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds)
  * [v3 `tagBindings.*`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds)

For more information about Resource Manager, refer to the [product documentation](https://docs.cloud.google.com/resource-manager/docs).   
**Limitations** | 

  * Only tag keys directly parented by a project resource and corresponding tag values can be protected using VPC Service Controls. When a project is added to a VPC Service Controls perimeter, all tag keys and corresponding tag values under the project are considered to be resources within the perimeter. 
  * Tag keys parented by an organization resource and their corresponding tag values can't be included in a VPC Service Controls perimeter and can't be protected using VPC Service Controls. 
  * Clients inside a VPC Service Controls perimeter can't access tag keys and corresponding values parented by an organization resource, unless an egress rule allowing access is set on the perimeter. For more information about setting egress rules, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference). 
  * Tag bindings are considered resources within the same perimeter as the resource to which the tag value is bound. For example, the tag bindings on a Compute Engine instance in a project is considered to belong to that project regardless of where the tag key is defined. 
  * Some services such as Compute Engine allow [creating tag bindings](https://docs.cloud.google.com/compute/docs/tag-resources#adding_tags_to_a_resource_during_resource_creation) using their own service APIs, in addition to the Resource Manager service APIs. For example, adding tags to a Compute Engine VM during resource creation. To protect tag bindings created or deleted using these service APIs, add the corresponding service, such as `compute.googleapis.com`, to the list of restricted services in the perimeter. 
  * Tags support method-level restrictions, so you can scope the `method_selectors` to specific API methods. For a list of restrictable methods, see [Supported service method restrictions](https://docs.cloud.google.com/vpc-service-controls/docs/supported-method-restrictions). 
  * Granting the owner role on a project through Google Cloud console is now supported by VPC Service Controls. You cannot send an owner invitation or accept an invitation outside service perimeters. If you try to accept an invitation from outside the perimeter you will not be granted the owner role and there will not be any error or warning message displayed. 

  
  
###  [Cloud Logging](https://docs.cloud.google.com/logging/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `logging.googleapis.com`  
**Details** |  The API for Cloud Logging can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Logging, refer to the [product documentation](https://docs.cloud.google.com/logging/docs).   
**Limitations** | 

  * Aggregated log sinks (folder or organization sinks where `includeChildren` is `true`) can access data from projects inside a service perimeter. To restrict aggregated log sinks from accessing data inside a perimeter, we recommend using IAM to manage Logging permissions at the folder or organization level.
  * You can't use VPC Service Controls to protect folder-level and organization-level logs, including aggregated logs. Although you can add a folder to a regular service perimeter, doing so protects only the projects within the folder hierarchy, not folder-level resources or logs. You can't add an organization as a protected resource in a service perimeter.
  * If you use an organization-level or folder-level log sink to route logs to a resource protected by a service perimeter, then you must add an ingress rule to the service perimeter. The ingress rule must allow access to the resource from the service account that the log sink uses. This step isn't necessary for project-level sinks. For more information, see the following pages:
    * [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules)
    * [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters)
    * [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)
  * When you specify an ingress or egress policy for a service perimeter, you can't use `ANY_SERVICE_ACCOUNT` or `ANY_USER_ACCOUNT` as the identity type if the log sink routes log entries to a [Cloud Storage](https://docs.cloud.google.com/storage/docs) resource. For this resource, use `ANY_IDENTITY` as the identity type. 
  * If you use VPC Service Controls perimeters and want to upgrade a log bucket to use Observability Analytics, then the following limitations apply:
    1. The perimeter must not restrict the following services:
       * `logging.googleapis.com`
       * `cloudkms.googleapis.com`: Required for log buckets that use CMEK.
    2. You can't use identity-based [ingress or egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to grant cross-perimeter access to the Cloud Key Management Service key when your log bucket and your Cloud KMS key are in different VPC Service Controls perimeters. For this configuration, the ingress rule must set the identity type to `ANY_IDENTITY` and it must also specify the project that contains the log bucket as the source resource. If you configure an egress rule, it must also set `identityType: ANY_IDENTITY`. For more information, see [Cross-perimeter CMEK configurations](https://docs.cloud.google.com/logging/docs/analyze/troubleshoot-upgrade-bucket#vpc-sc-cross-perimeter-cmek).

  
  
###  [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `certificatemanager.googleapis.com`  
**Details** |  The API for Certificate Manager can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Certificate Manager, refer to the [product documentation](https://docs.cloud.google.com/certificate-manager/docs).   
**Limitations** |  The Certificate Manager integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `monitoring.googleapis.com`  
**Details** |  The API for Cloud Monitoring can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Monitoring, refer to the [product documentation](https://docs.cloud.google.com/monitoring/docs).   
**Limitations** | 

  * Notification channels, alerting policies, and custom metrics can be used together to exfiltrate data/metadata. As of today, a user of Monitoring can set up a notification channel that points to an entity outside of the organization e.g. "baduser@badcompany.com". The user then sets up custom metrics and corresponding alert policies that utilize the notification channel. As a result, by manipulating the custom metrics, the user can trigger alerts and send alert firing notifications, exfiltrating sensitive data to baduser@badcompany.com, outside of the VPC Service Controls perimeter.
  * Any Compute Engine or AWS VMs with the [Monitoring Agent](https://docs.cloud.google.com/monitoring/agent) installed must be inside the VPC Service Controls perimeter or agent metric writes will fail.
  * Any [GKE Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod) must be inside the VPC Service Controls perimeter or [GKE Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine) will not work.
  * When querying metrics for a [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope), only the VPC Service Controls perimeter of the scoping project for the metric scope is considered. The perimeters of the individual monitored projects in the metrics scope aren't considered.
  * A project can only be added as a monitored project to an existing [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope) if that project is in the same VPC Service Controls perimeter as the metrics scope's scoping project.
  * To access Monitoring in the Google Cloud console for a host project that is protected by a service perimeter, use an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).
  * When a Google Cloud project is in an enabled VPC Service Controls perimeter, you can't create or modify [public uptime checks or synthetic monitors](https://docs.cloud.google.com/monitoring/uptime-checks/introduction). However, any uptime checks or synthetic monitors that existed before the Google Cloud project was added to the perimeter continue to operate, and you can still view and delete them. You can create and modify private uptime checks.

  
  
###  [Cloud Network Insights](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `networkmanagement.googleapis.com`  
**Details** |  The API for Cloud Network Insights can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Network Insights, refer to the [product documentation](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview).   
**Limitations** |  VPC Service Controls perimeter restrictions are not enforced when the network metadata and probe results are accessed using Broadcom's AppNeta service directly. We recommend using IAM and IAM Deny policies to restrict the access.   
  
###  [Cloud Profiler](https://docs.cloud.google.com/profiler/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudprofiler.googleapis.com`  
**Details** |  The API for Cloud Profiler can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Profiler, refer to the [product documentation](https://docs.cloud.google.com/profiler/docs).   
**Limitations** |  The Cloud Profiler integration with VPC Service Controls has no known limitations.   
  
###  [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `telemetry.googleapis.com`  
**Details** |  The API for Telemetry API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Telemetry API, refer to the [product documentation](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).   
**Limitations** |  The Telemetry API integration with VPC Service Controls has no known limitations.   
  
###  [Timeseries Insights API](https://docs.cloud.google.com/timeseries-insights/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `timeseriesinsights.googleapis.com`  
**Details** |  The API for Timeseries Insights API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Timeseries Insights API, refer to the [product documentation](https://docs.cloud.google.com/timeseries-insights/docs).   
**Limitations** |  The Timeseries Insights API integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Trace](https://docs.cloud.google.com/trace/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudtrace.googleapis.com`  
**Details** |  The API for Cloud Trace can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Trace, refer to the [product documentation](https://docs.cloud.google.com/trace/docs).   
**Limitations** |  The Cloud Trace integration with VPC Service Controls has no known limitations.   
  
###  [Cloud TPU](https://docs.cloud.google.com/tpu/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `tpu.googleapis.com`  
**Details** |  The API for Cloud TPU can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud TPU, refer to the [product documentation](https://docs.cloud.google.com/tpu/docs).   
**Limitations** |  The Cloud TPU integration with VPC Service Controls has no known limitations.   
  
###  [Natural Language API](https://docs.cloud.google.com/natural-language/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `language.googleapis.com`  
**Details** |  For more information about Natural Language API, refer to the [product documentation](https://docs.cloud.google.com/natural-language/docs).   
**Limitations** |  Because Natural Language API is a stateless API and doesn't run on projects, using VPC Service Controls to protect Natural Language API does not have any effect.  
  
###  [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `networkconnectivity.googleapis.com`  
**Details** |  The API for NCC can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about NCC, refer to the [product documentation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center).   
**Limitations** |  The NCC integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Asset API](https://docs.cloud.google.com/asset-inventory/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudasset.googleapis.com`  
**Details** |  The API for Cloud Asset API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Asset API, refer to the [product documentation](https://docs.cloud.google.com/asset-inventory/docs).   
**Limitations** | 

  * VPC Service Controls doesn't support access to folder-level or organization-level Cloud Asset API resources from resources and clients inside a service perimeter. VPC Service Controls restricts project-level Cloud Asset API resources. You can specify an egress policy to prevent access to project-level Cloud Asset API resources from projects inside the perimeter.
  * VPC Service Controls doesn't support adding folder-level or organization-level Cloud Asset API resources into a service perimeter. You cannot use a perimeter to restrict folder-level or organization-level Cloud Asset API resources. To manage Cloud Asset Inventory permissions at the folder or organization level, we recommend using IAM.
  * VPC Service Controls restricts project-level Cloud Asset API resources but doesn't enforce restrictions at the folder-level or organization-level scopes. Querying these resources using a folder or organization scope in the Google Cloud console can expose data from projects inside a service perimeter. To restrict access to these resources, use IAM controls.

  
  
###  [Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `speech.googleapis.com`  
**Details** |  The API for Speech-to-Text can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Speech-to-Text, refer to the [product documentation](https://docs.cloud.google.com/speech-to-text/docs).   
**Limitations** |  The Speech-to-Text integration with VPC Service Controls has no known limitations.   
  
###  [Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `texttospeech.googleapis.com`  
**Details** |  The API for Text-to-Speech can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Text-to-Speech, refer to the [product documentation](https://docs.cloud.google.com/text-to-speech/docs).   
**Limitations** |  The Text-to-Speech integration with VPC Service Controls has no known limitations.   
  
###  [Translation](https://docs.cloud.google.com/translate/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `translate.googleapis.com`  
**Details** |  The API for Translation can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Translation, refer to the [product documentation](https://docs.cloud.google.com/translate/docs).   
**Limitations** |  Cloud Translation - Advanced (v3) supports VPC Service Controls but not Cloud Translation - Basic (v2). To apply VPC Service Controls, you must use Cloud Translation - Advanced (v3). For more information about the different editions, see [Compare Basic and Advanced](https://cloud.google.com/translate/docs/editions).  
  
###  [License Manager](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `licensemanager.googleapis.com`  
**Details** |  [Create a service perimeter for License Manager](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager#create_a_service_perimeter_for_license_manager) with the License Manager API to secure your licenses.  For more information about License Manager, refer to the [product documentation](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager).   
**Limitations** |  The License Manager integration with VPC Service Controls has no known limitations.   
  
###  [Live Stream API](https://docs.cloud.google.com/livestream/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `livestream.googleapis.com`  
**Details** |  [Use VPC Service Controls](https://docs.cloud.google.com/livestream/docs/how-to/vpc/secure-pipeline) with the Live Stream API to secure your pipeline.  For more information about Live Stream API, refer to the [product documentation](https://docs.cloud.google.com/livestream/docs).   
**Limitations** |  To protect input endpoints with a service perimeter, you must follow the instructions for setting up a private pool and send input video streams over a private connection.   
  
###  [Transcoder API](https://docs.cloud.google.com/transcoder/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `transcoder.googleapis.com`  
**Details** |  The API for Transcoder API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Transcoder API, refer to the [product documentation](https://docs.cloud.google.com/transcoder/docs).   
**Limitations** |  The Transcoder API integration with VPC Service Controls has no known limitations.   
  
###  [Video Stitcher API](https://docs.cloud.google.com/video-stitcher/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `videostitcher.googleapis.com`  
**Details** |  The API for Video Stitcher API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Video Stitcher API, refer to the [product documentation](https://docs.cloud.google.com/video-stitcher/docs).   
**Limitations** |  The Video Stitcher API integration with VPC Service Controls has no known limitations.   
  
###  [Access Approval](https://docs.cloud.google.com/access-approval/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `accessapproval.googleapis.com`  
**Details** |  The API for Access Approval can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Access Approval, refer to the [product documentation](https://docs.cloud.google.com/access-approval/docs).   
**Limitations** |  The Access Approval integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `healthcare.googleapis.com`  
**Details** |  The API for Cloud Healthcare API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Healthcare API, refer to the [product documentation](https://docs.cloud.google.com/healthcare-api/docs).   
**Limitations** |  VPC Service Controls doesn't support [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) in the Cloud Healthcare API.   
  
###  [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/transfer-with-vpc-sc)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `storagetransfer.googleapis.com`  
**Details** |  A service perimeter protects the Storage Transfer Service API and Cloud Storage resources. By design, VPC Service Controls does not restrict importing data from external sources outside Google Cloud (such as Amazon S3, Microsoft Azure Blob Storage, and HTTP/HTTPS URLs) into Cloud Storage buckets within a service perimeter.  We recommend placing your Storage Transfer Service project within the same service perimeter as your Cloud Storage resources. This protects both your transfer and your Cloud Storage resources. Storage Transfer Service also supports scenarios where the Storage Transfer Service project is not in the same perimeter as your Cloud Storage buckets, using an [egress policy](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).  For setup information, see [Using Storage Transfer Service with VPC Service Controls](https://docs.cloud.google.com/storage-transfer/docs/transfer-with-vpc-sc) **Transfer service for on-premises data** See [Using Transfer for on-premises with VPC Service Controls](https://docs.cloud.google.com/storage-transfer/docs/on-prem-vpc-sc) for details and setup information for Transfer for on-premises.  For more information about Storage Transfer Service, refer to the [product documentation](https://docs.cloud.google.com/storage-transfer/docs/transfer-with-vpc-sc).   
**Limitations** | 

  * VPC Service Controls does not block importing data from external data sources (such as Amazon S3, Microsoft Azure Blob Storage, or HTTP/HTTPS URLs) into Cloud Storage buckets protected by a service perimeter. To restrict transfers from external sources, use [custom organization policy constraints](https://docs.cloud.google.com/storage-transfer/docs/custom-constraints) or IAM controls. 
  * To transfer data between Cloud Storage buckets in different service perimeters, the source and destination projects must be connected with an ingress/egress rule or perimeter bridge. 

  
  
###  [Service Control](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `servicecontrol.googleapis.com`  
**Details** |  The API for Service Control can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Service Control, refer to the [product documentation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started).   
**Limitations** | 

  * When you call the Service Control API from a VPC network in a service perimeter with Service Control restricted to report billing or analytics metrics, you can only use the [Service Control report](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report) method to report metrics for VPC Service Controls supported services.

  
  
###  [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `redis.googleapis.com`  
**Details** |  The API for Memorystore for Redis can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Memorystore for Redis, refer to the [product documentation](https://docs.cloud.google.com/memorystore/docs/redis).   
**Limitations** | 

  * Service perimeters protect only the Memorystore for Redis API. Perimeters do not protect normal data access on Memorystore for Redis instances within the same network.
  * If the Cloud Storage API is also protected, then Memorystore for Redis import and export operations can only read and write to a Cloud Storage bucket within the same service perimeter as the Memorystore for Redis instance.
  * If you use both Shared VPC and VPC Service Controls, you must have the host project that provides the network and the service project that contains the Redis instance inside the same perimeter in order for Redis requests to succeed. At any time, separating the host project and service project with a perimeter can cause a Redis instance failure, in addition to blocked requests. For more information, see Memorystore for Redis [configuration requirements](https://docs.cloud.google.com/memorystore/docs/redis/using-vpc-service-controls#configuration_requirements).

  
  
###  [Memorystore for Memcached](https://docs.cloud.google.com/memorystore/docs/memcached)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `memcache.googleapis.com`  
**Details** |  The API for Memorystore for Memcached can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Memorystore for Memcached, refer to the [product documentation](https://docs.cloud.google.com/memorystore/docs/memcached).   
**Limitations** | 

  * Service perimeters protect only the Memorystore for Memcached API. Perimeters do not protect normal data access on Memorystore for Memcached instances within the same network.

  
  
###  [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `memorystore.googleapis.com`  
**Details** | 

  * Service perimeters protect only the Memorystore for Valkey API. Perimeters do not protect normal data access on Memorystore for Valkey instances within the same network.
  * If the Cloud Storage API is also protected, then Memorystore for Valkey import and export operations can only read and write to a Cloud Storage bucket within the same service perimeter as the Memorystore for Valkey instance.
  * If you use both Shared VPC and VPC Service Controls, you must have the host project that provides the network and the service project that contains the Redis instance inside the same perimeter in order for Redis requests to succeed. At any time, separating the host project and service project with a perimeter can cause a Redis instance failure, in addition to blocked requests. For more information, see Memorystore for Valkey [configuration requirements](https://docs.cloud.google.com/memorystore/docs/valkey/using-vpc-service-controls#configuration_requirements).
  * The Memorystore for Valkey API is `memorystore.googleapis.com`. For this reason, the display name for Memorystore for Valkey is "Memorystore API" when using the VPC Service Controls in the Google Cloud console.

For more information about Memorystore for Valkey, refer to the [product documentation](https://docs.cloud.google.com/memorystore/docs/valkey).   
**Limitations** |  The Memorystore for Valkey integration with VPC Service Controls has no known limitations.   
  
###  [Service Directory](https://docs.cloud.google.com/service-directory/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `servicedirectory.googleapis.com`  
**Details** |  The API for Service Directory can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Service Directory, refer to the [product documentation](https://docs.cloud.google.com/service-directory/docs).   
**Limitations** |  The Service Directory integration with VPC Service Controls has no known limitations.   
  
###  [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **No.** The API for Transfer Appliance cannot be protected by service perimeters. However, Transfer Appliance can be used normally in projects inside a perimeter.   
**Details** |  Transfer Appliance is fully supported for projects using VPC Service Controls.  Transfer Appliance doesn't offer an API, and therefore does not support API-related features in VPC Service Controls.  For more information about Transfer Appliance, refer to the [product documentation](https://docs.cloud.google.com/transfer-appliance/docs).   
**Limitations** | 

  * When Cloud Storage is protected by VPC Service Controls, the Cloud KMS key you share with the Transfer Appliance Team must be within the same project as the destination Cloud Storage bucket. 

  
  
###  [Oracle Database@Google Cloud](https://docs.cloud.google.com/oracle/database/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `oracledatabase.googleapis.com`  
**Details** |  The API for Oracle Database@Google Cloud can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Oracle Database@Google Cloud, refer to the [product documentation](https://docs.cloud.google.com/oracle/database/docs).   
**Limitations** | 

  * VPC Service Controls perimeters restrict only the Oracle Database@Google Cloud control plane API, that is, `oracledatabase.googleapis.com`. Service perimeters don't restrict data plane access to underlying databases (such as, Exadata Databases or Autonomous Databases) that reside in the Oracle Cloud Infrastructure (OCI) environment.
  * VPC Service Controls perimeters don't restrict [OCI control plane APIs](https://docs.oracle.com/en-us/iaas/Content/database-at-gcp/home.htm).
  * You can't use VPC Service Controls perimeters to restrict Oracle Virtual Cloud Networks (VCNs) directly because the VCNs are located outside of Google Cloud. To learn how to secure ingress and egress traffic on private connections, see [OCI documentation: Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm).
  * You can't use VPC Service Controls perimeters for the networking layer between Google Cloud and OCI. As a result, the establishment of connections to Oracle databases isn't monitored or restricted by service perimeters.

  
  
###  [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `orgpolicy.googleapis.com`  
**Details** |  The API for Organization Policy Service can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Organization Policy Service, refer to the [product documentation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).   
**Limitations** |  VPC Service Controls doesn't support access restrictions to folder-level or organization-level organization policies that are inherited by the project. VPC Service Controls protects project-level Organization Policy Service API resources.  For example, if an ingress rule restricts a user from accessing the Organization Policy Service API, that user gets a 403 error when querying for organization policies enforced on the project. However, the user is still able to access the organization policies of the folder and organization containing the project.   
  
###  [OS Login](https://docs.cloud.google.com/compute/docs/oslogin)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `oslogin.googleapis.com`  
**Details** |  You can call the OS Login API from within VPC Service Controls perimeters. To manage OS Login from within VPC Service Controls perimeters, [set up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access). SSH connections to VM instances are not protected by VPC Service Controls. For more information about OS Login, refer to the [product documentation](https://docs.cloud.google.com/compute/docs/oslogin).   
**Limitations** |  The OS Login methods for reading and writing SSH keys don't enforce VPC Service Controls perimeters. Use VPC accessible services to disable access to OS Login APIs.   
  
###  [Personalized Service Health](https://docs.cloud.google.com/service-health/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `servicehealth.googleapis.com`  
**Details** |  The API for Personalized Service Health can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Personalized Service Health, refer to the [product documentation](https://docs.cloud.google.com/service-health/docs).   
**Limitations** |  VPC Service Controls does not support the `OrganizationEvents` and `OrganizationImpacts` resources of the Service Health API. Therefore, VPC Service Controls policy checks won't occur when you call the methods for these resources. However, you can call the methods from a service perimeter using a restricted VIP.   
  
###  [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `osconfig.googleapis.com`  
**Details** |  You can call the OS Config API from within VPC Service Controls perimeters. To use VM Manager from within VPC Service Controls perimeters, [set up VM Manager](https://docs.cloud.google.com/compute/docs/manage-os). For more information about VM Manager, refer to the [product documentation](https://docs.cloud.google.com/compute/docs/vm-manager).   
**Limitations** |  To fully protect VM Manager, you must include all of the following APIs in your perimeter: 

  * OS Config API (`osconfig.googleapis.com`)
  * Compute Engine API (`compute.googleapis.com`)
  * Artifact Analysis API (`containeranalysis.googleapis.com`)

VM Manager does not host package and patch content. OS patch management uses the update tools for the operating system which require that package updates and patches are retrievable on the VM. For patching to work, you might need to use Cloud NAT or host your own package repository or Windows Server Update Service within your Virtual Private Cloud.   
  
###  [Workflows](https://docs.cloud.google.com/workflows/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `workflows.googleapis.com`  
**Details** |  Workflows is an orchestration platform that can combine Google Cloud services and HTTP-based APIs to execute services in an order that you define. When you protect the Workflows API using a service perimeter, the Workflow Executions API is also protected. You do not need to separately add `workflowexecutions.googleapis.com` to your perimeter's list of protected services.  HTTP requests from a Workflows execution are supported as follows: 

  * [Authenticated requests](https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow#authenticate-apis) to VPC Service Controls-compliant Google Cloud endpoints are allowed.
  * Requests to Cloud Run functions and Cloud Run service endpoints are allowed.
  * Requests to third-party endpoints are blocked.
  * Requests to non-VPC Service Controls-compliant Google Cloud endpoints are blocked.

For more information about Workflows, refer to the [product documentation](https://docs.cloud.google.com/workflows/docs).   
**Limitations** |  The Workflows integration with VPC Service Controls has no known limitations.   
  
###  [Filestore](https://docs.cloud.google.com/filestore)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `file.googleapis.com`  
**Details** |  The API for Filestore can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Filestore, refer to the [product documentation](https://docs.cloud.google.com/filestore).   
**Limitations** | 

  * Service perimeters protect only the Filestore API. Perimeters do not protect normal NFS data access on Filestore instances within the same network.
  * If you use both Shared VPC and VPC Service Controls, you must have the host project that provides the network and the service project that contains the Filestore instance inside the same perimeter for the Filestore instance to function correctly. Separating the host project and service project with a perimeter might cause the existing instances to become unavailable and might not create new instances.

  
  
###  [Parallelstore](https://docs.cloud.google.com/parallelstore)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `parallelstore.googleapis.com`  
**Details** |  For more information about Parallelstore, refer to the [product documentation](https://docs.cloud.google.com/parallelstore).   
**Limitations** | 

  * If you use both Shared VPC and VPC Service Controls, you must have the host project that provides the network and the service project that contains the Parallelstore instance inside the same perimeter for the Parallelstore instance to function correctly. Separating the host project and service project with a perimeter might cause the existing instances to become unavailable and might not create new instances.

  
  
###  [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `containerthreatdetection.googleapis.com`  
**Details** |  The API for Container Threat Detection can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Container Threat Detection, refer to the [product documentation](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).   
**Limitations** |  You must grant ingress access to the service perimeter from the Container Threat Detection service account. For more information, see [ Scanning projects protected by a service perimeter](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#service-perimeter).   
  
###  [Ads Data Hub](https://developers.google.com/ads-data-hub)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `adsdatahub.googleapis.com`  
**Details** |  For more information about Ads Data Hub, refer to the [product documentation](https://developers.google.com/ads-data-hub).   
**Limitations** |  Ads Data Hub and VPC Service Controls are subject to different terms of service. Review the terms of each product for details. Certain Ads Data Hub features (such as custom audience activation, custom bidding, and LiveRamp match tables) require certain user data to be exported outside of the VPC Service Controls perimeter. If Ads Data Hub is added as a restricted service, it will bypass VPC Service Controls policies for these features in order to retain their functionality. All dependent services must be included as allowed services in the same VPC Service Controls perimeter. For example, since Ads Data Hub relies on BigQuery, BigQuery must also be added. In general, VPC Service Controls best practices recommend including all services in the perimeter, i.e. “restricting all services”. Customers with multi-tier Ads Data Hub account structures (such as agencies with subsidiaries) should have all of their admin projects in the same perimeter. For simplicity, Ads Data Hub recommends that customers with multi-tier account structures restrict their admin projects to the same Google Cloud organization.  
  
###  [Security Token Service](https://docs.cloud.google.com/iam/docs/workload-identity-federation)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `sts.googleapis.com`  
**Details** |  VPC Service Controls only restricts token exchanges if the [audience](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1/TopLevel/token#body.request_body.FIELDS.audience) in the request is a project-level resource. For example, VPC Service Controls doesn't restrict requests for [downscoped tokens](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials), because those requests have no audience.  For more information about Security Token Service, refer to the [product documentation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).   
**Limitations** | 

  * When you create an [ingress or egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to allow token exchanges, you must set the identity type to `ANY_IDENTITY` because the [token](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1/TopLevel/token) method has no authorization.
  * Because VPC Service Controls does not support adding organization-level resources directly to perimeters, you must configure egress rules for Security Token Service API requests where the audience is a [Workforce Identity Federation](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#workforce_id_fed) pool.

  
  
###  [Firestore/Datastore](https://docs.cloud.google.com/firestore/docs/securing-with-vpc-sc)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `firestore.googleapis.com, datastore.googleapis.com, firestorekeyvisualizer.googleapis.com`  
**Details** |  The `firestore.googleapis.com`, `datastore.googleapis.com`, and `firestorekeyvisualizer.googleapis.com` services are bundled together. When you restrict the `firestore.googleapis.com` service in a perimeter, the perimeter also restricts the `datastore.googleapis.com` and `firestorekeyvisualizer.googleapis.com` services. You don't need to separately add these services to your perimeter's list of protected services.  To restrict `datastore.googleapis.com` service, [ use the `firestore.googleapis.com` service name](https://docs.cloud.google.com/datastore/docs/securing-with-vpc-sc#restricting-the-datastore.googleapis.com-service).  To get full egress protection on import and export operations, you must use the Firestore service agent. See the following for more information: 

  * [Securing **Firestore** import and export operations with VPC Service Controls](https://docs.cloud.google.com/firestore/docs/securing-with-vpc-sc).
  * [Securing **Datastore** import and export operations with VPC Service Controls](https://docs.cloud.google.com/datastore/docs/securing-with-vpc-sc).

For more information about Firestore/Datastore, refer to the [product documentation](https://docs.cloud.google.com/firestore/docs/securing-with-vpc-sc).   
**Limitations** | 

  * Import and export operations are not fully protected unless you use the Firestore service agent. See the following for more information: 
    * [Securing **Firestore** import and export operations with VPC Service Controls](https://docs.cloud.google.com/firestore/docs/securing-with-vpc-sc).
    * [Securing **Datastore** import and export operations with VPC Service Controls](https://docs.cloud.google.com/datastore/docs/securing-with-vpc-sc).
  * [ App Engine legacy bundled services for Datastore ](https://docs.cloud.google.com/appengine/docs/standard/python/bundled-services-overview) do not support service perimeters. Protecting the Datastore service with a service perimeter blocks traffic from App Engine legacy bundled services. Legacy bundled services include:
    * [ Java 8 Datastore with App Engine APIs ](https://docs.cloud.google.com/appengine/docs/standard/java/datastore)
    * [ Python 2 NDB client library for Datastore ](https://docs.cloud.google.com/appengine/docs/standard/python/ndb/creating-entities)
    * [ Go 1.11 Datastore with App Engine APIs ](https://docs.cloud.google.com/appengine/docs/standard/go111/datastore)
  * To use [ Firestore with MongoDB compatibility](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview) with restricted VIP, you must configure connectivity to `restricted.firestore.goog` as described in [ Configure Private Google Access in Firestore with MongoDB compatibility](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/configure-private-google-access).  This domain and its IP addresses are used only by the Firestore with MongoDB compatibility service and are VPC Service Controls compliant. 

  
  
###  [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/compute-engine)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `vmmigration.googleapis.com`  
**Details** |  The API for Migrate to Virtual Machines can be protected by VPC Service Controls, and the product can be used normally inside service perimeters.  For more information about Migrate to Virtual Machines, refer to the [product documentation](https://docs.cloud.google.com/migrate/compute-engine).   
**Limitations** | 

  * To fully protect Migrate to Virtual Machines, add all of the following APIs to the service perimeter:
    * Artifact Registry API (`artifactregistry.googleapis.com`)
    * Pub/Sub API (`pubsub.googleapis.com`)
    * Cloud Storage API (`storage.googleapis.com`)
    * Cloud Logging API (`logging.googleapis.com`)
    * Container Registry API (`containerregistry.googleapis.com`)
    * Secret Manager API (`secretmanager.googleapis.com`)
    * Compute Engine API (`compute.googleapis.com`)
For more information, see the [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/create-a-service-perimeter) documentation. 

  
  
###  [Migration Center](https://docs.cloud.google.com/migration-center/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `

  * migrationcenter.googleapis.com
  * rapidmigrationassessment.googleapis.com

`  
**Details** |  VPC Service Controls lets you protect the infrastructure data that you collect with Migration Center with a service perimeter.  For more information about Migration Center, refer to the [product documentation](https://docs.cloud.google.com/migration-center/docs).   
**Limitations** |  After you enable the service perimeter, you can't transfer your infrastructure data to StratoZone.   
  
###  [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `backupdr.googleapis.com`  
**Details** |  The API for Backup and DR Service can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Backup and DR Service, refer to the [product documentation](https://docs.cloud.google.com/backup-disaster-recovery/docs).   
**Limitations** |  If you remove the internet default route from the service producer project using the command `gcloud services vpc-peerings enable-vpc-service-controls`, then you may not be able to access or deploy the management console. If you encounter this issue, contact [Google Cloud Customer Care](https://cloud.google.com/support).   
  
###  [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `gkebackup.googleapis.com`  
**Details** |  You can use VPC Service Controls to protect backup for GKE and you can use backup for GKE features normally inside service perimeters.  For more information about Backup for GKE, refer to the [product documentation](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke).   
**Limitations** |  The Backup for GKE integration with VPC Service Controls has no known limitations.   
  
###  [Retail API](https://docs.cloud.google.com/retail/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `retail.googleapis.com`  
**Details** |  The API for Retail API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Retail API, refer to the [product documentation](https://docs.cloud.google.com/retail/docs).   
**Limitations** |  The Retail API integration with VPC Service Controls has no known limitations.   
  
###  [Application Integration](https://docs.cloud.google.com/application-integration/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `integrations.googleapis.com`  
**Details** |  Application Integration is a collaborative workflow management system that allows you to create, augment, debug and understand core business system workflows. The workflows on the Application Integration are made up of triggers and tasks. There are several kinds of triggers such as api trigger/Pub/Sub trigger/cron trigger/sfdc trigger.  For more information about Application Integration, refer to the [product documentation](https://docs.cloud.google.com/application-integration/docs/overview).   
**Limitations** | 

  * VPC Service Controls protects Application Integration logs. If you use Application Integration, verify the support for vpcsc integration with the Application Integration team.

  
  
###  [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `connectors.googleapis.com`  
**Details** |  The API for Integration Connectors can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Integration Connectors, refer to the [product documentation](https://docs.cloud.google.com/integration-connectors/docs).   
**Limitations** | 

  * To connect to non-Google Cloud backends (for example, on-premises systems or services in other clouds), you must use a [Private Service Connect attachment](https://docs.cloud.google.com/integration-connectors/docs/private-connectivity-overview). Doing so keeps the connection within your VPC network and off the public internet. Connections to these backends fail without an attachment. 
  * When using [event subscriptions](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) within a VPC Service Controls perimeter, automatic backend registration isn't supported. You must manually configure the backend to send events to the connection's event listener endpoint. These event subscriptions also require a [Private Service Connect attachment](https://docs.cloud.google.com/integration-connectors/docs/private-connectivity-overview). 

  
  
###  [Error Reporting](https://docs.cloud.google.com/error-reporting/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `clouderrorreporting.googleapis.com`  
**Details** |  The API for Error Reporting can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Error Reporting, refer to the [product documentation](https://docs.cloud.google.com/error-reporting/docs).   
**Limitations** |  Notifications sent when a new or reoccurring error group is found contain information about the error group. To prevent data exfiltration outside of the VPC Service Controls perimeter, ensure that notification channels are within your organization.   
  
###  [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `workstations.googleapis.com`  
**Details** |  The API for Cloud Workstations can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Workstations, refer to the [product documentation](https://docs.cloud.google.com/workstations/docs/overview).   
**Limitations** | 

  * To fully protect Cloud Workstations, you must restrict the Compute Engine API in your service perimeter whenever you restrict the Cloud Workstations API.
  * Ensure that Google Cloud Storage API, Google Container Registry API, and Artifact Registry API are [ VPC accessible](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) in your service perimeter. This is needed to pull images onto your workstation. We also recommended that you allow Cloud Logging API and Cloud Error Reporting API to be VPC accessible in your service perimeter, although this is not required to use Cloud Workstations.
  * Ensure that your workstation cluster is [private](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters#create_a_private_cluster). Configuring a private cluster prevents connections to your workstations from outside your VPC service perimeter.
  * Ensure that you disable public IP addresses in your workstation configuration. Failing to do so results in VMs with public IP addresses in your project. We strongly recommend that you use the `constraints/compute.vmExternalIpAccess` organization policy constraint to disable public IP addresses for all VMs in your VPC service perimeter. For details, see [Restricting external IP addresses to specific VMs](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip). 
  * While connecting to your workstation, access control is only based on whether the private network you are connecting from belongs to the security perimeter. Access control based on device, public IP address, or location is not supported.

  
  
###  [Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `ids.googleapis.com`  
**Details** |  The API for Cloud IDS can be protected by VPC Service Controls, and the product can be used normally inside service perimeters.  For more information about Cloud IDS, refer to the [product documentation](https://docs.cloud.google.com/intrusion-detection-system/docs).   
**Limitations** |  Cloud IDS uses Cloud Logging to create threat logs in your project. If Cloud Logging is restricted by the service perimeter, VPC Service Controls blocks the Cloud IDS threat logs, even if Cloud IDS is not added as a restricted service to the perimeter. To use Cloud IDS inside a service perimeter, you must configure an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the Cloud Logging service account in your service perimeter.   
  
###  [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `beyondcorp.googleapis.com`  
**Details** |  For more information about Chrome Enterprise Premium, refer to the [product documentation](https://docs.cloud.google.com/chrome-enterprise-premium/docs).   
**Limitations** |  The Chrome Enterprise Premium integration with VPC Service Controls has no known limitations.   
  
###  [Policy Troubleshooter](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `policytroubleshooter.googleapis.com`  
**Details** |  When you restrict the Policy Troubleshooter API with a perimeter, principals can troubleshoot IAM allow policies only if all resources involved in the request are in the same perimeter. There are usually two resources involved in a troubleshooting request: 

  * **The resource you're troubleshooting access for.** This resource can be any type. You explicitly specify this resource when you troubleshoot an allow policy. 
  * **The resource you're using to troubleshoot access.** This resource is a project, folder, or organization. In the Google Cloud console and gcloud CLI, this resource is inferred based on the project, folder, or organization you have selected. In the REST API, you specify this resource using the `x-goog-user-project` header.  This resource can be the same as the resource that you're troubleshooting access for, but it doesn't need to be. 

If these resources aren't in the same perimeter, the request fails.  For more information about Policy Troubleshooter, refer to the [product documentation](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access).   
**Limitations** |  The Policy Troubleshooter integration with VPC Service Controls has no known limitations.   
  
###  [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/iam-simulator-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `policysimulator.googleapis.com`  
**Details** |  You can restrict the Policy Simulator API with a perimeter when simulating organization policies or allow and deny policies.  Principals can simulate organization policies as expected inside service perimeters.  Principals can simulate allow policies only if certain resources involved in the simulation are in the same perimeter. There are several resources involved in an allow policy simulation: 

  * **The resource whose allow policy you're simulating.** This resource is also called the _target resource_. In the Google Cloud console, this is the resource whose allow policy you're editing. In the gcloud CLI and REST API, you explicitly specify this resource when you simulate an allow policy. 
  * **The project, folder, or organization that creates and runs the simulation.** This resource is also called the _host resource_. In the Google Cloud console and gcloud CLI, this resource is inferred based on the project, folder, or organization you have selected. In the REST API, you specify this resource using the `x-goog-user-project` header.  This resource can be the same as the resource that you're simulating access for, but it doesn't need to be. 
  * **The resource that provides access logs for the simulation.** In a simulation, there is always one resource that provides access logs for the simulation. This resource varies depending on the target resource type: 
    * If you are simulating an allow policy for a project or organization, Policy Simulator retrieves the access logs for that project or organization. 
    * If you are simulating an allow policy for a different type of resource, Policy Simulator retrieves the access logs for that resource's parent project or organization. 
    * If you are simulating multiple resources' allow policies at once, Policy Simulator retrieves the access logs for the resources' nearest common project or organization. 
  * **All supported resources with relevant allow policies.** When Policy Simulator runs a simulation, it considers all allow policies that might impact the user's access, including allow policies on the target resource's ancestor and descendant resources. As a result, these ancestor and descendant resources are also involved in simulations. 

If the target resource and the host resource aren't in the same perimeter, the request fails.  If the target resource and the resource that provides access logs for the simulation aren't in the same perimeter, the request fails.  If the target resource and some supported resources with relevant allow policies aren't in the same perimeter, the requests succeeds, but the results might be incomplete. For example, if you're simulating a policy for a project in a perimeter, the results won't include the allow policy of the project's parent organization, because organizations are always outside of VPC Service Controls perimeters. To get more complete results, you can configure [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the perimeter.  For more information about Policy Simulator, refer to the [product documentation](https://docs.cloud.google.com/policy-intelligence/docs/iam-simulator-overview).   
**Limitations** | 

  * VPC Service Controls does not support adding folder-level or organization-level resources to service perimeters. Therefore, you cannot use VPC Service Controls to protect folder-level and organization-level simulations of deny policies. Deny policy simulations on resources outside of the service perimeter still return complete results, and deny policy simulations on project-level resources are protected. 

  
  
###  [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `essentialcontacts.googleapis.com`  
**Details** |  The API for Essential Contacts can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Essential Contacts, refer to the [product documentation](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest).   
**Limitations** |  The Essential Contacts integration with VPC Service Controls has no known limitations.   
  
###  [Identity Platform](https://docs.cloud.google.com/identity-platform/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `identitytoolkit.googleapis.com,  
securetoken.googleapis.com`  
**Details** |  The API for Identity Platform can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Identity Platform, refer to the [product documentation](https://docs.cloud.google.com/identity-platform/docs).   
**Limitations** | 

  * To fully protect Identity Platform, add the Secure Token API (`securetoken.googleapis.com`) to the service perimeter to allow token refresh. `securetoken.googleapis.com` is not listed on the VPC Service Controls page of the Google Cloud console. You can only add this service with the [gcloud access-context-manager perimeters update](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update#--add-restricted-services) command. 
  * If your application also integrates with the [blocking functions feature](https://docs.cloud.google.com/identity-platform/docs/blocking-functions), add Cloud Run functions (`cloudfunctions.googleapis.com`) to the service perimeter.
  * The use of SMS-based multi-factor authentication (MFA), email authentication, or third-party identity providers causes data to be sent out of the perimeter. If you don't use MFA with SMS, email authentication, or third-party identity providers, disable these features.

  
  
###  [GKE Multi-Cloud](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `gkemulticloud.googleapis.com`  
**Details** |  The API for GKE Multi-Cloud can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about GKE Multi-Cloud, refer to the [product documentation](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud).   
**Limitations** | 

  * To fully protect the GKE Multi-Cloud API, you must include the Kubernetes Metadata API (`kubernetesmetadata.googleapis.com`) as well in your perimeter.

  
  
###  [GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `gkeonprem.googleapis.com`  
**Details** |  The GKE On-Prem API can be protected by VPC Service Controls, and the API can be used normally inside service perimeters.  For more information about GKE On-Prem API, refer to the [product documentation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview).   
**Limitations** | 

  * To fully protect the GKE On-Prem API, add all of the following APIs to the service perimeter:
    * Kubernetes Metadata API (`kubernetesmetadata.googleapis.com`)
    * Cloud Monitoring API (`monitoring.googleapis.com`)
    * Cloud Logging API (`logging.googleapis.com`)
Note that VPC Service Controls doesn't protect against Cloud Logging log exports on a folder or organization level. 

  
  
###  [Google Distributed Cloud (software only) for bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **No.** The API for Google Distributed Cloud (software only) for bare metal cannot be protected by service perimeters. However, Google Distributed Cloud (software only) for bare metal can be used normally in projects inside a perimeter.   
**Details** |  You can create a cluster in your environment, which is connected to VPC using Cloud Interconnect or Cloud VPN.  For more information about Google Distributed Cloud (software only) for bare metal, refer to the [product documentation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs).   
**Limitations** | 

  * To protect your clusters, use Restricted VIP in Google Distributed Cloud (software only) for bare metal, and add all of the following APIs to the service perimeter:
    * Artifact Registry API (`artifactregistry.googleapis.com`)
    * Google Cloud Resource Manager API (`cloudresourcemanager.googleapis.com`)
    * Compute Engine API (`compute.googleapis.com`)
    * Connect Gateway API (`connectgateway.googleapis.com`)
    * Google Container Registry API (`containerregistry.googleapis.com`)
    * GKE Connect API (`gkeconnect.googleapis.com`)
    * GKE Hub API (`gkehub.googleapis.com`)
    * GKE On-Prem API (`gkeonprem.googleapis.com`)
    * Cloud IAM API (`iam.googleapis.com`)
    * Cloud Logging API (`logging.googleapis.com`)
    * Cloud Monitoring API (`monitoring.googleapis.com`)
    * Config Monitoring for Ops API (`opsconfigmonitoring.googleapis.com`)
    * Service Control API (`servicecontrol.googleapis.com`)
    * Cloud Storage API (`storage.googleapis.com`)

  
  
###  [On-Demand Scanning API](https://docs.cloud.google.com/artifact-analysis/docs/os-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `ondemandscanning.googleapis.com`  
**Details** |  The API for On-Demand Scanning API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about On-Demand Scanning API, refer to the [product documentation](https://docs.cloud.google.com/artifact-analysis/docs/os-overview).   
**Limitations** |  The On-Demand Scanning API integration with VPC Service Controls has no known limitations.   
  
###  [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `looker.googleapis.com`  
**Details** |  The API for Looker (Google Cloud core) can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Looker (Google Cloud core), refer to the [product documentation](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc).   
**Limitations** | 

  * Only **Enterprise** or **Embed** editions of Looker (Google Cloud core) instances using private IP connections support VPC Service Controls compliance. Looker (Google Cloud core) instances with public IP connections or both public and private IP connections do not support VPC Service Controls compliance. To create an instance that uses a private IP connection, select **Private IP** in the **Networking** section of the **Create instance** page of the Google Cloud console.
  * When placing or creating a Looker (Google Cloud core) instance inside a VPC Service Controls service perimeter, you must remove the default route to the internet by calling the [`services.enableVpcServiceControls`](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/enableVpcServiceControls) method or by running the following `gcloud` command:  
  
`gcloud services vpc-peerings enable-vpc-service-controls --network=your-network service=servicenetworking.googleapis.com`  
  
Removing the default route restricts outgoing traffic to only [VPC Service Controls compliant services](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). For example, sending email will fail because the API that is used to send email is not VPC Service Controls compliant.
  * If you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), ensure that you either include the Looker (Google Cloud core) service project in the same service perimeter as the Shared VPC host project or create a [perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters) between the two projects. If the Looker (Google Cloud core) service project and the Shared VPC host project are not in same perimeter or cannot communicate through a perimeter bridge, instance creation could fail or the Looker (Google Cloud core) instance may not function properly.
  * If you're using [Data Studio Pro](https://docs.cloud.google.com/looker/docs/studio/about-looker-studio-pro) or [Studio in Looker}](https://docs.cloud.google.com/looker/docs/studio-in-looker), the Looker connector can't connect to a Looker (Google Cloud core) instance that is inside a VPC Service Controls perimeter. For more information about limitations of the Looker connector, see the [Overview of Looker connector requirements, limits, and feature support](https://docs.cloud.google.com/looker/docs/studio/limits-of-the-looker-connector) documentation page.

  
  
###  [Public Certificate Authority](https://docs.cloud.google.com/certificate-manager/docs/public-ca)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `publicca.googleapis.com`  
**Details** |  The API for Public Certificate Authority can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Public Certificate Authority, refer to the [product documentation](https://docs.cloud.google.com/certificate-manager/docs/public-ca).   
**Limitations** |  The Public Certificate Authority integration with VPC Service Controls has no known limitations.   
  
###  [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `storagebatchoperations.googleapis.com`  
**Details** | 

  * To use VPC Service Controls with storage batch operations, [create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) to protect the following project and Google Cloud services: 
    * Cloud Storage project 
    * Storage batch operations API (`storagebatchoperations.googleapis.com)`
    * Cloud Storage API (`storage.googleapis.com`) 
    * Optional: Cloud KMS API (`cloudkms.googleapis.com)`, if you use the object encryption key updates [job type](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-type).
  * To allow access to storage batch operations from outside the perimeter, you must [configure ingress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

For more information about Storage batch operations, refer to the [product documentation](https://docs.cloud.google.com/storage/docs/batch-operations/overview).   
**Limitations** |  The Storage batch operations integration with VPC Service Controls has no known limitations.   
  
###  [Storage Insights](https://docs.cloud.google.com/storage/docs/insights/inventory-reports)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `storageinsights.googleapis.com`  
**Details** |  The API for Storage Insights can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Storage Insights, refer to the [product documentation](https://docs.cloud.google.com/storage/docs/insights/inventory-reports).   
**Limitations** |  The Storage Insights integration with VPC Service Controls has no known limitations.   
  
###  [Dataflow Data Pipelines](https://docs.cloud.google.com/dataflow/docs/guides/data-pipelines)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `datapipelines.googleapis.com`  
**Details** |  To fully protect Dataflow Data Pipelines, include all of the following APIs in your perimeter:

  * Dataflow API (`dataflow.googleapis.com`)
  * Cloud Scheduler API (`cloudscheduler.googleapis.com`)
  * Container Registry API (`containerregistry.googleapis.com`)

For more information about Dataflow Data Pipelines, refer to the [product documentation](https://docs.cloud.google.com/dataflow/docs/guides/data-pipelines).   
**Limitations** |  The Dataflow Data Pipelines integration with VPC Service Controls has no known limitations.   
  
###  [Security Command Center](https://docs.cloud.google.com/security-command-center/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `securitycenter.googleapis.com,  
securitycentermanagement.googleapis.com`  
**Details** |  The APIs for Security Command Center can be protected by VPC Service Controls, and Security Command Center can be used normally inside service perimeters.  
  
The `securitycenter.googleapis.com` and `securitycentermanagement.googleapis.com` services are bundled together. When you restrict the `securitycenter.googleapis.com` service in a perimeter, the perimeter restricts the `securitycentermanagement.googleapis.com` service by default. You cannot add the `securitycentermanagement.googleapis.com` service to the list of restricted services in a perimeter because it is bundled with `securitycenter.googleapis.com`.  For more information about Security Command Center, refer to the [product documentation](https://docs.cloud.google.com/security-command-center/docs).   
**Limitations** | 

  * VPC Service Controls doesn't support access to folder-level or organization-level Security Command Center API resources from resources and clients inside a service perimeter. VPC Service Controls protects project-level Security Command Center API resources. You can specify an egress policy to prevent access to project-level Security Command Center API resources from projects inside the perimeter.
  * VPC Service Controls doesn't support adding folder-level or organization-level Security Command Center API resources into a service perimeter. You cannot use a perimeter to protect folder-level or organization-level Security Command Center API resources. To manage Security Command Center permissions at the folder or organization level, we recommend using IAM.
  * VPC Service Controls doesn't support the [security posture service](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview) because security posture resources (such as postures, posture deployments, and predefined posture templates) are organization-level resources.
  * You cannot export findings at the folder or organization level into destinations inside a service perimeter.
  * VPC Service Controls doesn't support Google Security Operations (Google Security Operations SIEM and Google Security Operations SOAR). Enabling Security Command Center Enterprise on projects within a service perimeter might lead to violations from unsupported security operations services. If you have VPC Service Controls configured, before you create a Google Security Operations instance, move the Google Cloud project and Cloud Key Management Service (Cloud KMS) for customer-managed encryption keys (CMEK) project outside the VPC Service Controls perimeter.
  * You must enable perimeter access in the following scenarios: 
    * When you [enable finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) at the folder or organization level and the Pub/Sub topic is inside a service perimeter.
    * When you [ export data to BigQuery](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query) from the folder or organization level and BigQuery is inside a service perimeter.
    * When you integrate Security Command Center with a supported third-party SIEM or SOAR product and the product is deployed inside a service perimeter in a Google Cloud environment. Supported SIEMs and SOARs include [Splunk](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-splunk) and [IBM QRadar](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-qradar).
    * When you enable [Assured Open Source Software](https://docs.cloud.google.com/security-command-center/docs/aoss-configure-support-for-vpc-sc) within a service perimeter.
    * When you want [ Virtual Machine Threat Detection to scan VMs in your service perimeters](https://docs.cloud.google.com/security-command-center/docs/vmtd-allow-access-vpcsc). 
    * When you want to [allow Vulnerability Assessment for Google Cloud to scan VMs in your perimeters](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud-vpcsc).
    * To use Container Threat Detection, you must [ grant the service account for Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#service-perimeter) inbound access to that service perimeter. 
    * When you want [ Event Threat Detection to monitor logging streams ](https://docs.cloud.google.com/security-command-center/docs/etd-allow-access-vpcsc) in Security Command Center within VPC Service Controls perimeters. 
    * When you want to use [ Mandiant Attack Surface Management in Security Command Center ](https://docs.cloud.google.com/security-command-center/docs/asm-allow-access-vpcsc) within VPC Service Controls perimeters.

  
  
###  [Cloud Customer Care](https://docs.cloud.google.com/support/docs/reference/support-api)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudsupport.googleapis.com`  
**Details** |  The API for Cloud Customer Care can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Cloud Customer Care, refer to the [product documentation](https://docs.cloud.google.com/support/docs/reference/support-api).   
**Limitations** |  VPC Service Controls protects data accessed through the Cloud Support API but doesn't protect data accessed through the Google Cloud console.  
  
###  [AI Applications - Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `discoveryengine.googleapis.com`  
**Details** |  The API for AI Applications - Agent Search can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about AI Applications - Agent Search, refer to the [product documentation](https://docs.cloud.google.com/generative-ai-app-builder/docs).   
**Limitations** |  If you configure the Agent Search [widget for public access](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget#public-access) (that is, without an OAuth token), then calls to the API backend are made through a Google-managed service agent. Because this traffic doesn't carry your authentication token, the request can effectively bypass your organization's configured VPC Service Controls ingress rules. Even if you protect the `discoveryengine.googleapis.com` service inside a VPC Service Controls perimeter, a widget with public access can still be reached from outside that perimeter. If your organization requires VPC Service Controls enforcement to protect sensitive data, don't enable a widget that has public access.   
  
###  [Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `confidentialcomputing.googleapis.com`  
**Details** |  To ensure that Confidential Space functions correctly across perimeter boundaries, you must configure [ egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference). 

  * If your Confidential Space needs to access Cloud Storage buckets outside your perimeter, create an [ egress rule](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/vpc-service-controls) to allow access to those buckets. 
  * If you are enabling Confidential Space API on Compute Engine resources outside your perimeter, create an [ egress rule](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/vpc-service-controls) to allow access to this API. 

For more information about Confidential Space, refer to the [product documentation](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview).   
**Limitations** |   
  
###  [Serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `ssh-serialport.googleapis.com`  
**Details** |  To use VPC Service Controls protection when connecting to the serial console for a virtual machine (VM) instance, you need to specify an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the service perimeter. When setting up the ingress rule, the access level for the source must be an IP-based value and the service name set to `ssh-serialport.googleapis.com`. The ingress rule is required to access the serial console even if the source request and target resource are in the same perimeter.  For more information about Serial console, refer to the [product documentation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console).   
**Limitations** | 

  * You can't use [SSH-in-browser](https://docs.cloud.google.com/compute/docs/ssh-in-browser) to access the serial console.
  * You cannot access a serial console by using Private Google Access. You can access the serial console only from the public internet.
  * When using a serial console, identity-based ingress or egress rules cannot be used to allow access to the serial console.

  
  
###  [Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `vmwareengine.googleapis.com`  
**Details** |  For more information about VMware Engine Service Controls, refer to [VPC Service Controls with VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls).  For more information about Google Cloud VMware Engine, refer to the [product documentation](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls).   
**Limitations** |  When adding existing VMware Engine networks, Private Clouds, Network Policies, and VPC Peering to a VPC Service Perimeter, previously created resources are not checked again to see if they still comply with the perimeter's policies.   
  
###  [Dataform](https://docs.cloud.google.com/dataform/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `dataform.googleapis.com`  
**Details** |  To learn how to control access to Dataform with VPC Service Controls, see [Configure VPC Service Controls for Dataform](https://docs.cloud.google.com/dataform/docs/vpc-service-controls).  For more information about Dataform, refer to the [product documentation](https://docs.cloud.google.com/dataform/docs).   
**Limitations** |  When you restrict Dataform using VPC Service Controls, you must do the following: 

  * [Set the `dataform.restrictGitRemotes` organization policy](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes).
  * Restrict BigQuery within the same service perimeter as Dataform.
  * Add user identities to ingress rules to allow these users to authenticate with their Google Account user credentials when [scheduling runs](https://docs.cloud.google.com/dataform/docs/schedule-runs), [manually triggering runs](https://docs.cloud.google.com/dataform/docs/trigger-execution), or [running pipelines](https://docs.cloud.google.com/bigquery/docs/create-pipelines#run_a_pipeline). For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#updating) and [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).
  * Ensure that Identity and Access Management permissions granted to the service accounts used in Dataform reflect your security architecture.

  
  
###  [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `websecurityscanner.googleapis.com`  
**Details** |  Web Security Scanner and VPC Service Controls are subject to different terms of service. Review the terms of each product for details. Web Security Scanner sends the findings to Security Command Center on demand. You can view or download the data from the Security Command Center dashboard. For more information about Web Security Scanner, refer to the [product documentation](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview).   
**Limitations** |  The Web Security Scanner integration with VPC Service Controls has no known limitations.   
  
###  [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `securesourcemanager.googleapis.com`  
**Details** | 

  * You need to configure [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs) with a working certificate authority before creating Secure Source Manager VPC Service Controls instances.
  * You need to configure [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) before accessing the Secure Source Manager VPC Service Controls instance.

For more information about Secure Source Manager, refer to the [product documentation](https://docs.cloud.google.com/secure-source-manager/docs).   
**Limitations** | 

  * `SERVICE_NOT_ALLOWED_FROM_VPC` audit log violation caused by GKE limitations can be ignored.
  * To open the VPC Service Controls web interface with a browser, the browser needs access to the following URLs: 
    * `https://accounts.google.com`
    * `https://LOCATION_OF_INSTANCE-sourcemanagerredirector-pa.client6.google.com`
      * For example, `https://us-central1-sourcemanagerredirector-pa.client6.google.com`
    * `https://lh3.googleusercontent.com`

  
  
###  [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `networkservices.googleapis.com,  
networksecurity.googleapis.com`  
**Details** | 

  * The APIs for Secure Web Proxy can be protected by VPC Service Controls and the product can be used normally inside service perimeters. 
  * If you provision your proxy with a [certificate](https://docs.cloud.google.com/certificate-manager/docs/certificates), then you must also include the Certificate Manager API (`certificatemanager.googleapis.com`) in your service perimeter.
  * If you [enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection) for your proxy, then you must also include the [Certificate Authority Service API](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest) (`privateca.googleapis.com`) in your service perimeter.

For more information about Secure Web Proxy, refer to the [product documentation](https://docs.cloud.google.com/secure-web-proxy/docs).   
**Limitations** |  The Secure Web Proxy integration with VPC Service Controls has no known limitations.   
  
###  [API keys](https://docs.cloud.google.com/api-keys/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `apikeys.googleapis.com`  
**Details** |  The API for API keys can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about API keys, refer to the [product documentation](https://docs.cloud.google.com/api-keys/docs/overview).   
**Limitations** |  The API keys integration with VPC Service Controls has no known limitations.   
  
###  [App Lifecycle Manager](https://docs.cloud.google.com/saas-runtime/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `saasservicemgmt.googleapis.com`  
**Details** |  App Lifecycle Manager manages Terraform deployments at scale, and lets you manage both your applications and the infrastructure that they run on. For more information about App Lifecycle Manager, refer to the [product documentation](https://docs.cloud.google.com/saas-runtime/docs/overview).   
**Limitations** |  The App Lifecycle Manager integration with VPC Service Controls has no known limitations.   
  
###  [Partner console in Sovereign Controls by Partners](https://docs.cloud.google.com/security/products/sovereign-controls-by-partners)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudcontrolspartner.googleapis.com`  
**Details** |  The Cloud Controls Partner API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Partner console in Sovereign Controls by Partners, refer to the [product documentation](https://docs.cloud.google.com/security/products/sovereign-controls-by-partners).   
**Limitations** | 

  * This service must be restricted for all non-partners. If you're a partner supporting Sovereign Controls by Partners, you can protect this service using a service perimeter.

  
  
###  [Microservices](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `microservices.googleapis.com`  
**Details** |  The API for Microservices can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Microservices, refer to the [product documentation](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc).   
**Limitations** |  The Microservices integration with VPC Service Controls has no known limitations.   
  
###  [Earth Engine](https://docs.cloud.google.com/earth-engine#documentation)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `earthengine.googleapis.com,  
earthengine-highvolume.googleapis.com`  
**Details** |  The `earthengine.googleapis.com` and `earthengine-highvolume.googleapis.com` services are bundled together. When you restrict the `earthengine.googleapis.com` service in a perimeter, the perimeter restricts the `earthengine-highvolume.googleapis.com` service by default. You cannot add the `earthengine-highvolume.googleapis.com` service to the list of restricted services in a perimeter because it is bundled with `earthengine.googleapis.com`.  For more information about Earth Engine, refer to the [product documentation](https://docs.cloud.google.com/earth-engine#documentation).   
**Limitations** | 

  * The Earth Engine [Code Editor](https://code.earthengine.google.com/), a web-based IDE for the Earth Engine JavaScript API, is not supported and VPC Service Controls doesn't allow using the Earth Engine Code Editor with resources and clients inside a service perimeter.
  * [Legacy assets](https://developers.google.com/earth-engine/cloud/assets#legacy-assets_1) are not protected by VPC Service Controls.
  * [Export to Google Drive](https://developers.google.com/earth-engine/guides/exporting) is not supported by VPC Service Controls.
  * [Earth Engine Apps](https://developers.google.com/earth-engine/guides/apps) are not supported for resources and clients inside a service perimeter.
  * VPC Service Controls is only available for _Premium_ and _Professional_ Earth Engine pricing plans. For more information about pricing plans, see [ Earth Engine plans](https://cloud.google.com/earth-engine/pricing).

For more information about limitations and example workarounds, see Earth Engine [access control documentation](https://developers.google.com/earth-engine/cloud/access-control).  
  
###  [App Hub](https://docs.cloud.google.com/app-hub/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `apphub.googleapis.com`  
**Details** |  App Hub lets you discover and organize infrastructure resources into applications. You can use VPC Service Controls perimeters to restrict the App Hub resources. When you restrict the App Hub API in a perimeter for a management project, we recommend adding all [enabled APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis#apis) in the management project to the same perimeter. For more information about setting up VPC Service Controls for App Hub, see [Use VPC Service Controls with App Hub](https://docs.cloud.google.com/app-hub/docs/using-vpc-service-controls). For more information about App Hub, refer to the [product documentation](https://docs.cloud.google.com/app-hub/docs).   
**Limitations** |  If you use [ App Topology](https://docs.cloud.google.com/app-topology), add the API (`apptopology.googleapis.com`) to the list of restricted services in your service perimeter to maintain consistent restriction. For applications in a [folder boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary), VPC Service Controls restrictions apply only to App Hub interactions in the management project. App Hub can read application data and discover services and workloads for all descendent projects of the app-enabled folder, even if those projects are not in the same perimeter as the management project. For [legacy host projects](https://docs.cloud.google.com/app-hub/docs/key-concepts#host-project), you can only attach a service project if the host project and service project are in the same perimeter. If you move a previously-attached service project outside the perimeter, the service project's resources remain accessible until you detach the service project from the host project.  
  
###  [Cloud Code](https://docs.cloud.google.com/code/docs)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudcode.googleapis.com`  
**Details** |  The Cloud Code API can be protected by VPC Service Controls. To use Gemini-powered features in Cloud Code, an ingress policy must be configured to allow traffic from IDE clients. See the [Gemini documentation](https://docs.cloud.google.com/gemini/docs/configure-vpc-service-controls#configure-perimeter) for details.  For more information about Cloud Code, refer to the [product documentation](https://docs.cloud.google.com/code/docs).   
**Limitations** |  The Cloud Code integration with VPC Service Controls has no known limitations.   
  
###  [Commerce Org Governance API](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `commerceorggovernance.googleapis.com`  
**Details** |  VPC Service Controls perimeter protects the Commerce Org Governance API for Google Private Marketplace. For more information about Commerce Org Governance API, refer to the [product documentation](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace).   
**Limitations** |  Resources such as procurement request and access request, which the Commerce Org Governance API creates at the project level, surface up to the organization level and are reviewed by the Organization Administrator without enforcing VPC Service Controls policies.  
  
###  [Google Cloud Contact Center as a Service](https://docs.cloud.google.com/contact-center/ccai-platform/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `contactcenteraiplatform.googleapis.com`  
**Details** |  To restrict the internet traffic, use organization policies. Invoke the `CREATE` or `UPDATE` methods of the Google Cloud Contact Center as a Service API to [apply the organization policy constraints](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaip-custom-constraints) manually.  For more information about Google Cloud Contact Center as a Service, refer to the [product documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs).   
**Limitations** |  The Google Cloud Contact Center as a Service integration with VPC Service Controls has no known limitations.   
  
###  [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `privilegedaccessmanager.googleapis.com`  
**Details** |  The API for Privileged Access Manager can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Privileged Access Manager, refer to the [product documentation](https://docs.cloud.google.com/iam/docs/pam-overview).   
**Limitations** | 

  * VPC Service Controls doesn't support adding folder-level or organization-level resources into a service perimeter. You can't use a perimeter to protect folder-level or organization-level Privileged Access Manager resources. VPC Service Controls protects project-level Privileged Access Manager resources.
  * To protect Privileged Access Manager, you need to include the following APIs in your perimeter: 
    * Privileged Access Manager API (`privilegedaccessmanager.googleapis.com`)
    * Cloud Resource Manager API (`cloudresourcemanager.googleapis.com`)
    * Cloud Logging API (`logging.googleapis.com`)
    * Cloud Asset API (`cloudasset.googleapis.com`)

  
  
###  [Service Usage](https://docs.cloud.google.com/service-usage/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `serviceusage.googleapis.com`  
**Details** |  The API for Service Usage can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Service Usage, refer to the [product documentation](https://docs.cloud.google.com/service-usage/docs).   
**Limitations** |  VPC Service Controls doesn't support the restriction of [Service Usage API](https://docs.cloud.google.com/service-usage/docs/reference/rest)'s `v1beta1` methods and blocks calls to these methods through the restricted VIP.  
  
###  [Audit Manager](https://docs.cloud.google.com/audit-manager/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `auditmanager.googleapis.com`  
**Details** |  The API for Audit Manager can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Audit Manager, refer to the [product documentation](https://docs.cloud.google.com/audit-manager/docs/overview).   
**Limitations** | 

  * You can't use a perimeter to protect folder-level or organization-level Audit Manager resources. To manage Audit Manager permissions at the folder or organization level, we recommend using IAM.
  * You must enable perimeter access using [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) in the following scenarios: 
    * If you [run an audit](https://docs.cloud.google.com/audit-manager/docs/run-audit) at the folder level and the Cloud Storage bucket is inside a perimeter, configure an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) for the [service account](https://docs.cloud.google.com/audit-manager/docs/enroll-resource).
    * If you [run an audit](https://docs.cloud.google.com/audit-manager/docs/run-audit) at the folder level and the projects inside the folder are protected by a perimeter, configure an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) for the [service account](https://docs.cloud.google.com/audit-manager/docs/enroll-resource).
    * If you [run an audit](https://docs.cloud.google.com/audit-manager/docs/run-audit) at the project level, the project is protected by a perimeter, and the Cloud Storage bucket is not inside the same perimeter, configure an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference) for the project that contains the Cloud Storage bucket.
For more information, see [Configure VPC Service Controls for Audit Manager](https://docs.cloud.google.com/audit-manager/docs/configure-vpcsc). 
  
  
###  [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `discoveryengine.googleapis.com`  
**Details** |  The API for Gemini Enterprise can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Gemini Enterprise, refer to the [product documentation](https://docs.cloud.google.com/gemini/enterprise/docs).   
**Limitations** |  When you enable VPC Service Controls on a Google Cloud project that contains a Gemini Enterprise app, you're blocked from creating or using Gemini Enterprise actions by default, and any attempt to create an action in the UI is prohibited. To enable and use actions for specific services within your VPC Service Controls perimeter, you must contact your Google representative and request to be added to the allowlist.  You can't enforce a VPC Service Controls perimeter on a project that has existing data stores. To enforce VPC Service Controls restrictions on an existing data store, delete and then recreate the data store.   
  
###  [Google Antigravity in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `businessaicode.googleapis.com`  
**Details** |  The API for Google Antigravity in Gemini Enterprise can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Google Antigravity in Gemini Enterprise, refer to the [product documentation](https://docs.cloud.google.com/gemini/enterprise/docs).   
**Limitations** |  The Google Antigravity in Gemini Enterprise integration with VPC Service Controls has no known limitations.   
  
###  [Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `discoveryengine.googleapis.com`  
**Details** |  The API for Gemini Notebook Enterprise can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Gemini Notebook Enterprise, refer to the [product documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview).   
**Limitations** |  If your project has VPC Service Controls enabled, you can't add website URLs as notebook sources in Gemini Notebook Enterprise. This is because, if you ingest a website directly, it causes the system perform a live web crawl and generate outbound traffic, which violates VPC Service Controls perimeter policies. Other source types, such as Google Docs and YouTube URLs, can be added to notebooks in projects where VPC Service Controls is enabled.   
  
###  [Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `developerconnect.googleapis.com`  
**Details** |  The API for Developer Connect can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Developer Connect, refer to the [product documentation](https://docs.cloud.google.com/developer-connect/docs/overview).   
**Limitations** | 

  * To restrict access to third-party source code management tools, you can create a [custom organization policy](https://docs.cloud.google.com/developer-connect/docs/custom-constraints). [Learn more](https://docs.cloud.google.com/developer-connect/docs/vpc-service-controls#org-policy-scms). 
  * To disallow egress traffic to the internet using Developer Connect HTTP proxies, add [custom organization policies](https://docs.cloud.google.com/developer-connect/docs/custom-constraints) that either prevent creating connections without Service Directory or that restrict creating connections to certain SCMSs. 
  * [Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/insights) depends on [App Hub](https://docs.cloud.google.com/app-hub/docs/using-vpc-service-controls) and delivers artifact and deployment metadata to [App Topology](https://docs.cloud.google.com/app-topology). Please see [known limitations](https://docs.cloud.google.com/developer-connect/docs/vpc-service-controls#insights-known-limitations) for more information. 

  
  
###  [Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `parametermanager.googleapis.com`  
**Details** |  The API for Parameter Manager can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Parameter Manager, refer to the [product documentation](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview).   
**Limitations** |  Parameter Manager must be in the same VPC Service Controls perimeter as Secret Manager.   
  
###  [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `modelarmor.googleapis.com`  
**Details** |  The API for Model Armor can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Model Armor, refer to the [product documentation](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview).   
**Limitations** |  Model Armor uses regional endpoints, which aren't supported by Private Google Access. When you restrict Model Armor within a perimeter, you must use a Private Service Connect endpoint for Model Armor to function as expected with VPC Service Controls.  
  
###  Autoscaling 

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `autoscaling.googleapis.com`  
**Details** |  The API for Autoscaling can be protected by VPC Service Controls and the product can be used normally inside service perimeters.   
**Limitations** |  The Autoscaling integration with VPC Service Controls has no known limitations.   
  
###  [Address Validation](https://developers.google.com/maps/documentation/address-validation)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `addressvalidation.googleapis.com`  
**Details** |  The API for Address Validation can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Address Validation, refer to the [product documentation](https://developers.google.com/maps/documentation/address-validation).   
**Limitations** |  The Address Validation integration with VPC Service Controls has no known limitations.   
  
###  [Places (New)](https://developers.google.com/maps/documentation/places/web-service)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `places.googleapis.com`  
**Details** |  The API for Places (New) can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Places (New), refer to the [product documentation](https://developers.google.com/maps/documentation/places/web-service).   
**Limitations** |  The Places (New) integration with VPC Service Controls has no known limitations.   
  
###  [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `managedkafka.googleapis.com`  
**Details** |  The API for Google Cloud Managed Service for Apache Kafka can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Google Cloud Managed Service for Apache Kafka, refer to the [product documentation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview).   
**Limitations** | 

  * Managed Service for Apache Kafka relies on underlying networking services. To help protect this service, make sure that all necessary services are also included within your service perimeter: 
    * Compute Engine API (`compute.googleapis.com`)
    * Cloud DNS API (`dns.googleapis.com`)
    * Secret Manager API (`secretmanager.googleapis.com`) for clusters created as of September 2026 or later.
  * To help protect a Kafka Connect connector, include any services the connector calls in your perimeter. Depending on the connector type, the connector might call one of the following services: 
    * BigQuery API (`bigquery.googleapis.com`)
    * Cloud Storage API (`storage.googleapis.com`)
    * Pub/Sub API (`pubsub.googleapis.com`)

  
  
###  [Geocoding](https://developers.google.com/maps/documentation/geocoding)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **No.** The API for Geocoding cannot be protected by service perimeters. However, Geocoding can be used normally in projects inside a perimeter.   
**Details** |  VPC Service Controls only protect [the Geocoding API](https://developers.google.com/maps/documentation/geocoding) and don't support [the Geocoding API v4](https://developers.google.com/maps/documentation/geocoding/geocoding-v4-overview) (`geocoding.googleapis.com`). Because the Geocoding API is a stateless API, you can't enforce the VPC Service Controls restrictions on the Geocoding API by adding it to a perimeter.  For more information about Geocoding, refer to the [product documentation](https://developers.google.com/maps/documentation/geocoding).   
**Limitations** |  The Geocoding integration with VPC Service Controls has no known limitations.   
  
###  [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudsecuritycompliance.googleapis.com`  
**Details** |  The API for Compliance Manager can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Compliance Manager, refer to the [product documentation](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview).   
**Limitations** | 

  * You must configure egress and ingress rules to use Compliance Manager within a service perimeter. For more information, see [ Configure Compliance Manager support for VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc).
  * You can't use a perimeter to help protect Compliance Manager resources at the folder level or organization level. To manage Compliance Manager permissions at the folder or organization level, [use IAM](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  
  
###  [Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `maintenance.googleapis.com`  
**Details** |  Unified Maintenance provides a centralized view of planned disruptive maintenance events across supported Google Cloud products.  Resource maintenance activities in individual projects are accessible through the [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) configured for the given scope. If you want to restrict access through the management project, [add the management project to the same VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) as individual projects, or [remove IAM permissions](https://docs.cloud.google.com/app-hub/docs/grant-access-applications) on the management project level.  For more information about Unified Maintenance, refer to the [product documentation](https://docs.cloud.google.com/unified-maintenance/docs/overview).   
**Limitations** |  The Unified Maintenance integration with VPC Service Controls has no known limitations.   
  
###  [Cloud Location Finder](https://docs.cloud.google.com/location-finder/docs/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `cloudlocationfinder.googleapis.com`  
**Details** |  Cloud Location Finder lets you identify and filter cloud locations in regions and zones across Google Cloud, Google Distributed Cloud, Microsoft Azure, Amazon Web Services, and Oracle Cloud Infrastructure based on proximity, geographic location, and carbon footprint.  You can protect the Cloud Location Finder API with VPC Service Controls, and use the Cloud Location Finder API normally inside service perimeters.  For more information about Cloud Location Finder, refer to the [product documentation](https://docs.cloud.google.com/location-finder/docs/overview).   
**Limitations** |  The Cloud Location Finder integration with VPC Service Controls has no known limitations.   
  
###  [Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `geminidataanalytics.googleapis.com`  
**Details** |  A service perimeter can restrict only the Conversational Analytics API service endpoint. To enforce data protection for the Conversational Analytics API's data sources such as BigQuery and Looker, you must also restrict these data sources and the corresponding services in the service perimeter.  For more information about Conversational Analytics API, refer to the [product documentation](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview).   
**Limitations** |  The service perimeter helps protect the Conversational Analytics API, whereas IAM helps govern access to the API and its underlying data sources. To restrict the data that you use with the Conversational Analytics API within the perimeter, you must have the [necessary IAM permissions to access the API and the data sources from within the API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api#grant-required-roles).  
  
###  [Customer Experience Agent Studio](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `ces.googleapis.com`  
**Details** |  When you restrict the CX Agent Studio API (`ces.googleapis.com`) in a service perimeter, add the CX Insights API (`contactcenterinsights.googleapis.com`) as well to the restricted services list of the perimeter configuration. For more information, see [Configure VPC Service Controls for CX Agent Studio](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/vpc-service-controls).  For more information about Customer Experience Agent Studio, refer to the [product documentation](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps).   
**Limitations** |  Understand the [limitations](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/vpc-service-controls#limits) of using CX Agent Studio with VPC Service Controls.   
  
###  [Vector Search 2.0](https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `vectorsearch.googleapis.com`  
**Details** |  The API for Vector Search 2.0 can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Vector Search 2.0, refer to the [product documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview).   
**Limitations** |  To help protect Vector Search 2.0, add the following services to the restricted services list of your perimeter configuration:

  * Agent Platform API (`aiplatform.googleapis.com`) is used for auto-embedding.
  * Cloud Storage (`storage.googleapis.com`) is used for bulk object operations.

  
  
###  [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `lustre.googleapis.com`  
**Details** |  The API for Google Cloud Managed Lustre can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Google Cloud Managed Lustre, refer to the [product documentation](https://docs.cloud.google.com/managed-lustre/docs).   
**Limitations** | 

  * To transfer data between Managed Lustre and Cloud Storage, the project containing the Cloud Storage bucket must be within the same service perimeter as the Managed Lustre instance. To import or export data outside the perimeter, you must configure an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to allow the Managed Lustre service agent (`service-PROJECT_NUMBER@gcp-sa-lustre.iam.gserviceaccount.com`) to access the bucket.
  * If you use both Shared VPC and VPC Service Controls, the host project that contains the network and the service project that contains the Managed Lustre instance must both be inside the same perimeter. Separating the host project and service project with a perimeter can cause existing instances to become unavailable and can prevent creation of new instances.

  
  
###  [App Topology](https://docs.cloud.google.com/app-topology)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `apptopology.googleapis.com`  
**Details** |  The API for App Topology can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about App Topology, refer to the [product documentation](https://docs.cloud.google.com/app-topology).   
**Limitations** |  When you enable the App Topology API, App Topology adds an access path for limited metadata for App Hub applications, Cloud Trace traces, and Cloud Monitoring alerts. Examples of metadata include trace span start and end times and App Topology application IDs. For applications in a [folder boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary), VPC Service Controls restrictions for App Hub apply only to App Hub interactions in the management project. As a result, App Topology can read data for applications and discovered services and workloads for all descendent projects of the app-enabled folder, even if those projects are not in the same perimeter as the management project.  
  
###  [Universal Ledger](https://docs.cloud.google.com/universal-ledger)

|  |  **Status** |  **Preview**. The integration of this product with VPC Service Controls is in Preview and is ready for broader testing and use, but is not fully supported for production environments.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `universalledger.googleapis.com`  
**Details** |  The Universal Ledger API operates on shared, multi-tenant networks where data submitted to the ledger is classified as _Transaction Data_. Under the service-specific terms, Transaction Data — which includes transaction payloads, public keys, and cryptographic signatures — is explicitly excluded from the definition of Customer Data. Because of the shared nature of the ledger network, Transaction Data submitted to the ledger will become accessible to all authorized ledger participants. Consequently, this data cannot be restricted or contained by a customer's individual VPC Service Controls perimeter configuration.  For more information about Universal Ledger, refer to the [product documentation](https://docs.cloud.google.com/universal-ledger).   
**Limitations** |  Although VPC Service Controls protects API ingress and egress traffic, it does not enforce data visibility after transactions are committed to the shared ledger. To help prevent data exfiltration, use IAM deny policies to restrict methods that modify data, such as `universalledger.endpoints.submitTransaction`. This approach blocks unauthorized users from publishing data from inside the perimeter and allows for read-only access.   
  
###  [Agent Identity API](https://docs.cloud.google.com/iam/docs/agent-identity-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `agentidentity.googleapis.com`  
**Details** |  To use this API within a service perimeter, clients must route requests through the Restricted VIP (`restricted.googleapis.com`).  For more information about Agent Identity API, refer to the [product documentation](https://docs.cloud.google.com/iam/docs/agent-identity-overview).   
**Limitations** |  The Agent Identity API integration with VPC Service Controls has no known limitations.   
  
###  [Agent Identity Credentials API](https://docs.cloud.google.com/iam/docs/agent-identity-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `agentidentitycredentials.googleapis.com`  
**Details** |  To use this API within a service perimeter, clients must route requests through the Restricted VIP (`restricted.googleapis.com`).  For more information about Agent Identity Credentials API, refer to the [product documentation](https://docs.cloud.google.com/iam/docs/agent-identity-overview).   
**Limitations** |  The Agent Identity Credentials API integration with VPC Service Controls has no known limitations.   
  
###  [Observability API](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)

|  |  **Status** |  **GA**. This product integration is fully supported by VPC Service Controls.   
---|---  
**Protect with perimeters?** |  **Yes.** You can configure your perimeters to protect this service.   
**Service name** |  `observability.googleapis.com`  
**Details** |  The API for Observability API can be protected by VPC Service Controls and the product can be used normally inside service perimeters.  For more information about Observability API, refer to the [product documentation](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview).   
**Limitations** |  The Observability API integration with VPC Service Controls has no known limitations.   
  
For more information, read about [supported and unsupported services](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#services). 

## Manage access to unsupported services

Google services not listed on this page are not fully integrated with VPC Service Controls. Your [private connectivity configuration](https://docs.cloud.google.com/vpc/docs/private-service-connect) determines how you manage access to these unsupported services:

  * **Using Restricted VIP (`restricted.googleapis.com`)** or **Private Service Connect with`vpc-sc` bundle**: Access to unsupported services is blocked.

  * **Using Private VIP (`private.googleapis.com`)** or **Private Service Connect with`all-apis` bundle**: Access to unsupported services is allowed by default. To control this access and mitigate exfiltration risks, you must configure [VPC Service Controls service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services#service-patterns). Service patterns let you explicitly define which URL patterns for unsupported services are permitted from within your service perimeters.




For more details, see [Private connectivity for VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity).

## Restricted VIP supported services

The restricted virtual IP (VIP) provides a way for VMs that are inside a service perimeter to make calls to Google Cloud services without exposing the requests to the internet. For a complete list of the services available on the restricted VIP, see [Services supported by the restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services).

## Unsupported services

**Warning:** While it may be possible to enable unsupported services to access the data of supported products and services, we recommend that you do not. Unexpected issues might occur when attempting to access a supported service using an unsupported service, especially within the same project. 

Unsupported services may not function at all when enabled in a project protected by VPC Service Controls, especially when low-level storage services like Cloud Storage or Pub/Sub are restricted. We recommend deploying unsupported services in projects outside perimeters. To allow these services to access data in resources within a perimeter, [create an access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) that includes the service account for that service and [apply it to perimeters as needed](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add-access-level). 

Attempting to restrict an unsupported service using the `gcloud` command-line tool or the Access Context Manager API will result in an error. 

Cross-project access to data of supported services will be blocked by VPC Service Controls. Additionally, the restricted VIP can be used to block the ability of workloads to call unsupported services. 

## Other known limitations

This section describes known limitations with certain Google Cloud services, products, and interfaces that can be encountered when using VPC Service Controls.

For limitations with products that are supported by VPC Service Controls, refer to the Supported Products table.

For more information about resolving issues with VPC Service Controls, refer to the [Troubleshooting](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting) page.

### AutoML API

AutoML Translation API is [ deprecated](https://docs.cloud.google.com/translate/automl/docs/deprecations) and will no longer be available on Google Cloud after September 30, 2025. The functionality and management of custom models is available through [ Cloud Translation - Advanced API (v3)](https://docs.cloud.google.com/translate/docs).

When you use the AutoML API with VPC Service Controls, the following limitations apply:

  * You cannot add the supported [regional endpoints](https://docs.cloud.google.com/natural-language/automl/docs/locations#setting_the_location_using_the_api), such as `eu-automl.googleapis.com`, to the list of restricted services in a perimeter. When you protect the `automl.googleapis.com` service, the perimeter protects the supported regional endpoints, such as `eu-automl.googleapis.com`, as well.

  * When you use a service perimeter to protect `automl.googleapis.com`, access to all of the AutoML products that are integrated with VPC Service Controls and used inside the perimeter are impacted. You must configure your VPC Service Controls perimeter for all integrated AutoML products that are used inside that perimeter.

To fully protect the AutoML API, include all of the following APIs in your perimeter:

    * AutoML API (`automl.googleapis.com`)
    * Cloud Storage API (`storage.googleapis.com`)
    * Compute Engine API (`compute.googleapis.com`)
    * BigQuery API (`bigquery.googleapis.com`)



### App Engine

  * App Engine (both standard environment and flexible environment) is not supported by VPC Service Controls. Don't include App Engine projects in service perimeters.

However, it is possible to allow App Engine apps created in projects _outside_ service perimeters to read and write data to protected services _inside_ perimeters. To allow your app to access the data of protected services, [create an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example) that includes the project's App Engine service account. This does not enable App Engine to be used inside service perimeters.




### Bare Metal Solution

  * Connecting VPC Service Controls to your Bare Metal Solution environment doesn't uphold any service control guarantees.

  * The Bare Metal Solution API can be added to a secure perimeter. However, the VPC Service Controls perimeters don't extend to the Bare Metal Solution environment in the regional extensions.




### Blockchain Node Engine

  * VPC Service Controls only protects the Blockchain Node Engine API. When a node is created, you must still indicate that it is meant for a user-configured private network with [Private Service Connect](https://docs.cloud.google.com/blockchain-node-engine/docs/psc).

  * The peer-to-peer traffic is not affected by VPC Service Controls or Private Service Connect and will continue to use the public internet.




### Client libraries

  * Clients must use client libraries that have been updated as of November 1, 2018 or later.

  * Service account keys or OAuth2 client metadata used by clients must be updated as of November 1, 2018 or later. Older clients using the token endpoint must change to the endpoint specified in newer key material or client metadata.




### Cloud Billing

  * VPC Service Controls doesn't support Cloud Billing. You can export Cloud Billing data to a Cloud Storage bucket or BigQuery instance in a project that is protected by a service perimeter without configuring an access level or ingress rule.



### Cloud Deployment Manager

  * Deployment Manager is not supported by VPC Service Controls. Users may be able to call into services that are compliant with VPC Service Controls, but they shouldn't rely on this because it might break.

  * As a workaround, you can add the Deployment Manager service account (`PROJECT_NUMBER`@cloudservices.gserviceaccount.com) to the access levels to allow calls to APIs protected by VPC Service Controls.




### Cloud Shell

VPC Service Controls doesn't support Cloud Shell. VPC Service Controls treats Cloud Shell as outside of service perimeters and denies access to data that VPC Service Controls protects. However, VPC Service Controls allows access to Cloud Shell if a device that meets the [access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#device-example) requirements of the service perimeter initiates Cloud Shell.

### Gemini Cloud Assist

VPC Service Controls support for the Gemini Cloud Assist investigations (Preview) feature will be deprecated starting on April 13, 2026. This change will roll out over the course of one week. Access to Gemini Cloud Assist investigations (Preview) from within a VPC Service Controls perimeter is blocked. To continue using this feature, you must make requests from outside any VPC Service Controls perimeter. For more information, see [Deprecated VPC Service Controls support for Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/deprecations/vpcsc-support).

### Firebase

  * If your project is within a perimeter that restricts `apikeys.googleapis.com`, enabling Firebase on the project results in a `NO_MATCHING_ACCESS_LEVEL` violation. To resolve this violation, create an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) that grants the [Firebase service accounts](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_what-happens-when-add-firebase) access to `apikeys.googleapis.com`.



### Google Cloud console

  * Because the Google Cloud console is only accessible over the internet, it is treated as outside of service perimeters. When you apply a service perimeter, the Google Cloud console interface for the services that you protected may become partially or fully inaccessible. For example, if you protected Logging with the perimeter, you won't be able to access the Logging interface in the Google Cloud console.

To allow access from the Google Cloud console to resources protected by a perimeter, you need to create an access level for a public IP range that includes the machines of users who want to use the Google Cloud console with protected APIs. For example, you could add the public IP range of the NAT gateway of your private network to an access level, and then assign that access level to the service perimeter.

If you want to limit Google Cloud console access to the perimeter to only a specific set of users, you can also add those users to an access level. In that case, only the specified users would be able to access the Google Cloud console.

  * Requests through Google Cloud console from a network that is Private Google Access enabled, including networks implicitly enabled by Cloud NAT, might be blocked even if the requesting source network and target resource are in the same perimeter. This is because Google Cloud console access through Private Google Access is not supported by VPC Service Controls.




### Google Cloud metadata server

  * For [Compute Engine](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_computeengine) VM instances and [GKE](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gke) nodes, VPC Service Controls protection doesn't apply to the incoming traffic to or the outgoing traffic from [Google Cloud metadata server](https://docs.cloud.google.com/firewall/docs/firewalls#gcp-metadata-server).



### Private services access

  * [Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) supports deploying a service instance in a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#shared_vpc_scenario). If you use this configuration with VPC Service Controls, ensure that the host project that provides the network and the service project that contains the service instance are inside the same VPC Service Controls perimeter. Otherwise, requests might be blocked and service instances might not work correctly.

For more information about services that support private services access, see [Supported services](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services).




### GKE Multi-Cloud

  * VPC Service Controls only applies to resources within your Google Cloud project. The third-party cloud environment that hosts your GKE Multi-Cloud clusters does not uphold any service control guarantees.



### Google Distributed Cloud

  * VPC Service Controls only applies to bare metal machines connected to VPC network projects that use Restricted VIP.

  * [OpenID Connect (OIDC)](https://openid.net/connect/) and [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/) services need to be in the same VPC Service Controls perimeter. The requests to external endpoints are blocked.




### Migration Center

  * After you enable the service perimeter, you can't transfer your infrastructure data to StratoZone.



### Workforce Identity Federation

Workforce Identity Federation administrative features, including workforce pool configuration APIs don't support VPC Service Controls. However, Google Cloud products that support both [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services) and [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) operate as documented and are subject to VPC Service Controls policy checks. Additionally, you can use [third-party identities](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups) such as workforce pool users and workload identities in the ingress or egress rules of VPC Service Controls.

For Security Token Service API requests where the audience is a [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services) pool (which is an organization-level resource), you must configure egress rules. This is necessary because VPC Service Controls does not support adding organization-level resources directly to perimeters. The following egress rules allow requests originating from the perimeter to reach the Workforce STS APIs that interact with organization-level Workforce pools:
    
    
    - egressTo:
        operations:
          - serviceName: 'sts.googleapis.com'
            methodSelectors:
              - method: '*'
        resources:
          - '*'
      egressFrom:
        identityType: ANY_IDENTITY
    

## What's next

  * [Troubleshoot common VPC Service Controls issues](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting)
  * [Troubleshoot common issues related to other Google Cloud services](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshoot-services-within-perimeter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
