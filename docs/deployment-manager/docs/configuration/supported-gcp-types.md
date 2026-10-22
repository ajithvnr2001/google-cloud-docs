---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types/
title: Supported Google Cloud type providers \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:13.552539+00:00
---

# Supported Google Cloud type providers  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Supported Google Cloud type providers Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you want to create a resource using a Google Cloud type provider, use the following syntax in your configuration:
    
    
    resources:
    - name: example-resource
      **type : gcp-types/[PROVIDER]:[RESOURCE]**
      properties:
        ...

Where `[PROVIDER]` is a Google Cloud service, such as `compute-v1`, and `[RESOURCE]` is the resource you want to create, such as `instances`.

For example, if you want to create a reserved IP address using the Compute Engine v1 API, use the following syntax:
    
    
    type: gcp-types/compute-v1:addresses
    

The following is a list of Google Cloud type providers supported for deployments. To speed up creating your deployments, consider using the production-ready templates from the [Cloud Foundation Toolkit Project](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit) in the Deployment Manager GitHub repository.

Depending on the service and its launch stage, you might be able to create additional resource types in your deployments. For a full list of resource types, including resources that are in alpha, run the following command:
    
    
    gcloud beta deployment-manager types list --project gcp-types
    

You can also create your own type providers, such as for third-party APIs. For an overview of creating a type provider, see [Integrating with Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api).

Service | Type provider  
---|---  
App Engine | gcp-types/appengine-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/appengine-v1)  
Access Context Manager | gcp-types/accesscontextmanager-v1beta | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/accesscontextmanager-v1beta1)  
BigQuery | gcp-types/bigquery-v2 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/bigquery-v2)  
Bigtable | gcp-types/bigtableadmin-v2 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/bigtableadmin-v2)  
Cloud Run functions | gcp-types/cloudfunctions-v1 **Note** : As of November 1, 2019, new Functions are private by default, and require appropriate IAM permissions to invoke. [Learn about IAM permissions for Cloud Run functions](https://docs.cloud.google.com/functions/docs/reference/iam/roles). | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/cloudfunctions-v1)  
Cloud Key Management Service | gcp-types/cloudkms-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/cloudkms-v1)  
Resource Manager (v1) | gcp-types/cloudresourcemanager-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/cloudresourcemanager-v1)  
Resource Manager (v2) | gcp-types/cloudresourcemanager-v2 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/cloudresourcemanager-v2)  
Compute Engine (Alpha) | gcp-types/compute-alpha | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/compute-alpha)  
Compute Engine (Beta) | gcp-types/compute-beta | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/compute-beta)  
Compute Engine | gcp-types/compute-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/compute-v1)  
Google Kubernetes Engine | gcp-types/container-v1 **Note** : If you want to create and manage private GKE clusters with Deployment Manager, see the [best practices for setting up options for private clusters](https://docs.cloud.google.com/deployment-manager/docs/best-practices#managing_resources).  | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/container-v1)  
Google Kubernetes Engine (v1 Beta 1) | gcp-types/container-v1beta1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/container-v1beta1)  
Managed Service for Apache Spark | gcp-types/dataproc-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/dataproc-v1)  
Cloud DNS | gcp-types/dns-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/dns-v1)  
Filestore | gcp-types/file-v1beta1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/file-v1beta1)  
Identity and Access Management | gcp-types/iam-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/iam-v1)  
Cloud Logging | gcp-types/logging-v2 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/logging-v2)  
Cloud Monitoring | gcp-types/monitoring-v3 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/monitoring-v3)  
Pub/Sub | gcp-types/pubsub-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/pubsub-v1)  
Memorystore | gcp-types/redis-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/redis-v1)  
Memorystore (v1 Beta 1) | gcp-types/redis-v1beta1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/redis-v1beta1)  
Cloud Runtime Configuration API | gcp-types/runtimeconfig-v1beta1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/runtimeconfig-v1beta1)  
Service Management | gcp-types/servicemanagement-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/servicemanagement-v1)  
Spanner | gcp-types/spanner-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/spanner-v1)  
Cloud SQL (v1 Beta 4) | gcp-types/sqladmin-v1beta4 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/sqladmin-v1beta4)  
Cloud Storage | gcp-types/storage-v1 | [Resource snippets](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/storage-v1)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
