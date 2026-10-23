---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/gcp-managed-regions/
title: Google Cloud management regions overview \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:46.905782+00:00
---

# Google Cloud management regions overview  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/gcp-managed-regions/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Google Cloud management regions overview Stay organized with collections  Save and categorize content based on your preferences. 

## Google Cloud management regions and locations

Clusters created with GKE on AWS are located in a AWS region. When you create a cluster, you specify both an AWS region for your cluster and a Google Cloud region that manages the cluster.

Each Google Cloud region can manage clusters in a specific set of nearby AWS regions. For example, the Google Cloud region `us-west1`, located in Oregon, manages clusters in two AWS regions: `us-west-1` in Northern California and `us-west-2` in Oregon. Managing your clusters from nearby Google Cloud regions improves availability and reduces the latency of cluster management operations.

GKE on AWS includes the cluster's Google Cloud region in the cluster's resource name. For example, a cluster named `my-cluster` created in project `my-project` on region `us-west1` has a resource name of `projects/my-project/locations/us-west1/awsClusters/my-cluster`. By contrast, the AWS region is part of the cluster resource. You can specify it in the `aws_region` field of API calls.

## Data locality

To manage your clusters, the GKE Multi-Cloud API must store information about your cluster's state in the Google Cloud region you specified when creating the cluster. This data doesn't include workload-specific data (which is stored in your cluster's region) but does include information such as AWS resource IDs and public key infrastructure (PKI) data.

If your application needs to store its data in a particular geographic region, specify an AWS region and its associated Google Cloud management region that comply with your requirements when you create your clusters.

## Google Cloud regions and nearby AWS regions

The following table lists the Google Cloud regions currently supported by GKE on AWS and the nearby regions they can manage. Google Cloud Region | AWS region  
---|---  
`asia-east2` | `ap-east-1`  
`asia-northeast2` | `ap-northeast-1`  
`ap-northeast-2`  
`ap-northeast-3`  
`asia-south1` | `ap-south-1`  
`asia-southeast1` | `ap-east-1`  
`ap-northeast-1`  
`ap-southeast-1`  
`asia-southeast2` | `ap-southeast-3`  
`australia-southeast1` | `ap-southeast-2`  
`europe-north1` | `eu-north-1`  
`europe-west1` | `eu-central-1`  
`eu-north-1`  
`eu-south-1`  
`eu-west-1`  
`eu-west-2`  
`eu-west-3`  
`europe-west2` | `eu-west-2`  
`europe-west3` | `eu-central-1`  
`europe-west9` | `eu-west-3`  
`northamerica-northeast1` | `ca-central-1`  
`southamerica-east1` | `sa-east-1`  
`us-east4` | `ca-central-1`  
`us-east-1`  
`us-east-2`  
`us-west1` | `us-west-1`  
`us-west-2`  
  
You can fetch the most up-to-date list of current AWS regions supported by a [Google Cloud region](https://cloud.google.com/compute/docs/regions-zones#available) by running the following gcloud command:
    
    
    gcloud container aws get-server-config --location GOOGLE_CLOUD_REGION
    

Replace `GOOGLE_CLOUD_REGION` with the name of the Google Cloud region you're querying.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
