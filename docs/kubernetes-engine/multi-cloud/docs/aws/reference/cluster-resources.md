---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/cluster-resources/
title: Cluster resources \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:38:43.185815+00:00
---

# Cluster resources  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/cluster-resources/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/apis)



Send feedback 

#  Cluster resources Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the default resources that are created with an GKE on AWS cluster.

You might want to know about the resources that are created with a cluster for the following reasons:

  * Resources are associated with costs.
  * AWS quotas might limit the number of resources you can create.
  * Your organization might have policies that dictate the resources you are allowed to launch.



## Compute resources

Resource | Quantity  
---|---  
AWS Virtual Private Cloud (optional) | 1  
EC2 instance | At least 3  
  
The default number of control plane EC2 instances in a cluster is three. At least one additional instance is created for each node pool.

## Storage resources

Resource | Quantity  
---|---  
Main volume | 1  
Root volume | 1  
  
## Network resources

Resource | Type | Quantity  
---|---|---  
NAT gateway |  | 3  
Internet gateway |  | 1  
Subnet | Public | 3  
| Private | 3  
Route table | Public | 3  
| Private | 3  
Route | Public internet gateway | 3  
| Private NAT gateway | 3  
Route table association | Public | 3  
| Private | 3  
Elastic IP address | NAT | 3  
  
## Security and IAM resources

Resource | Quantity | Usage  
---|---|---  
KMS key | 6 | Database encryption   
Control plane configuration encryption   
Control plane main volume encryption   
Control plane root volume encryption   
Node pool configuration encryption   
Node pool root volume encryption  
KMS alias | 6 | Database encryption   
Control plane configuration encryption   
Control plane main volume encryption   
Control plane root volume encryption   
Node pool configuration encryption   
Node pool root volume encryption  
IAM role | 3 | Node pool   
Control plane   
API  
IAM policy | 3 | Node pool   
Control plane   
API  
IAM instance profile | 2 | Node pool   
Control plane  
IAM role policy attachment | 3 | Node pool   
Control plane   
API  
  
If you are using a proxy, GKE on AWS needs the following resources:

Resource | Quantity  
---|---  
Secret manager secret | 1  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
