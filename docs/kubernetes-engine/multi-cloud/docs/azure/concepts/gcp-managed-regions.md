---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/gcp-managed-regions/
title: Google Cloud management regions overview \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:16.129333+00:00
---

# Google Cloud management regions overview  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/gcp-managed-regions/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Cloud management regions overview

## Google Cloud management regions and locations

Clusters created with GKE on Azure are located in a Azure region. When you create a cluster, you specify both an Azure region for your cluster and a Google Cloud region that manages the cluster.

Each Google Cloud region can manage clusters in a specific set of nearby Azure regions. For example, the Google Cloud region `us-east4`, located in Oregon, manages clusters in the Azure regions `canadacentral` in Ontario, `centralus` in Iowa, `eastus` in Virginia, `eastus2` in Virginia and `southcentralus` in Texas. Managing your clusters from nearby Google Cloud regions improves availability and reduces the latency of cluster management operations.

GKE on Azure includes the cluster's Google Cloud region in the cluster's resource name. For example, a cluster named `my-cluster` created in project `my-project` on region `us-west1` has a resource name of `projects/my-project/locations/us-west1/azureClusters/my-cluster`. By contrast, the Azure region is part of the cluster resource. You can specify it in the `azure_region` field of API calls.

## Data locality

To manage your clusters, the GKE Multi-Cloud API must store information about your cluster's state in the Google Cloud region you specified when creating the cluster. This data doesn't include workload-specific data (which is stored in your cluster's region) but does include information such as Azure resource IDs and public key infrastructure (PKI) data.

If your application needs to store its data in a particular geographic region, specify an Azure region and its associated Google Cloud management region that comply with your requirements when you create your clusters.

## Google Cloud regions and nearby Azure regions

Google Cloud Region | Azure region  
---|---  
`asia-east2` | `eastasia`  
`asia-northeast2` | `japaneast`  
`asia-south1` | `centralindia`  
`asia-southeast1` | `australiaeast`  
`japaneast`  
`southeastasia`  
`australia-southeast1` | `australiaeast`  
`europe-north1` | `northeurope`  
`norwayeast`  
`europe-west1` | `francecentral`  
`germanywestcentral`  
`northeurope`  
`uksouth`  
`westeurope`  
`europe-west2` | `uksouth`  
`europe-west3` | `germanywestcentral`  
`europe-west4` | `westeurope`  
`europe-west6` | `switzerlandnorth`  
`europe-west9` | `francecentral`  
`northamerica-northeast1` | `canadacentral`  
`southamerica-east1` | `brazilsouth`  
`us-east4` | `canadacentral`  
`centralus`  
`eastus`  
`eastus2`  
`southcentralus`  
`us-west1` | `westus2`  
`westus3`  
  
You can fetch the most up-to-date list of current Azure regions supported by a [Google Cloud region](https://cloud.google.com/compute/docs/regions-zones#available) by running the following gcloud command:
    
    
    gcloud container azure get-server-config --location GOOGLE_CLOUD_REGION
    

Replace `GOOGLE_CLOUD_REGION` with the name of the Google Cloud region you're querying.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
