---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-instance-types/
title: Supported instance types \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:45.563594+00:00
---

# Supported instance types  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-instance-types/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/apis)



Send feedback 

#  Supported instance types Stay organized with collections  Save and categorize content based on your preferences. 

This page is for Admins and architects and Operators who want to define IT solutions and system architecture in accordance with company strategy and requirements. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Minimum supported cluster configuration

Clusters managed by GKE on AWS must meet the following minimum requirements. Your clusters might need more powerful control plane and node pool instances depending on the demands of your workloads.

Cluster size (nodes) | Control plane instances | Node pool instances  
---|---|---  
Demo | 3 x [t3.medium](https://aws.amazon.com/ec2/instance-types/t3/) | 2 x [t3.medium](https://aws.amazon.com/ec2/instance-types/t3/)  
1-10 nodes | 3 x [m5.large](https://aws.amazon.com/ec2/instance-types/m5/) | workload dependent  
11-100 nodes | 3 x [m5.xlarge](https://aws.amazon.com/ec2/instance-types/m5/) | workload dependent  
101-200 nodes | 3 x [m5.2xlarge](https://aws.amazon.com/ec2/instance-types/m5/) | workload dependent  
  
## Supported AWS instance types

GKE on AWS supports x86 instance types for control planes. For node pools, GKE on AWS supports both x86 and Arm instance types. For both control planes and node pools, GKE on AWS supports only Nitro-based instance types. GKE on AWS expands the list of supported instance types as AWS launches new ones. For more information, see [Instance types](https://aws.amazon.com/ec2/instance-types/) in the AWS documentation.

To learn how to use instances that have Arm architectures, see [Run Arm workloads in GKE on AWS](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/run-arm-workloads).

Instance Type | Model | Architecture | Minimum Supported Cluster Version | Minimum Supported Node Pool Version  
---|---|---|---|---  
[C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5.12xlarge | X86_64 | 1.21 | 1.21  
[C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5.18xlarge | X86_64 | 1.21 | 1.21  
[C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5.24xlarge | X86_64 | 1.21 | 1.21  
[C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5.2xlarge | X86_64 | 1.21 | 1.21  
[C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5.4xlarge | X86_64 | 1.21 | 1.21  
[C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5.9xlarge | X86_64 | 1.21 | 1.21  
[C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5.large | X86_64 | 1.21 | 1.21  
[C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5.xlarge | X86_64 | 1.21 | 1.21  
[C5a Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5a.12xlarge | X86_64 | 1.21 | 1.21  
[C5a Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5a.16xlarge | X86_64 | 1.21 | 1.21  
[C5a Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5a.24xlarge | X86_64 | 1.21 | 1.21  
[C5a Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5a.2xlarge | X86_64 | 1.21 | 1.21  
[C5a Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5a.4xlarge | X86_64 | 1.21 | 1.21  
[C5a Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5a.8xlarge | X86_64 | 1.21 | 1.21  
[C5a Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5a.large | X86_64 | 1.21 | 1.21  
[C5a Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5a.xlarge | X86_64 | 1.21 | 1.21  
[C5ad Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5ad.12xlarge | X86_64 | 1.21 | 1.21  
[C5ad Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5ad.16xlarge | X86_64 | 1.21 | 1.21  
[C5ad Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5ad.24xlarge | X86_64 | 1.21 | 1.21  
[C5ad Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5ad.2xlarge | X86_64 | 1.21 | 1.21  
[C5ad Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5ad.4xlarge | X86_64 | 1.21 | 1.21  
[C5ad Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5ad.8xlarge | X86_64 | 1.21 | 1.21  
[C5ad Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5ad.large | X86_64 | 1.21 | 1.21  
[C5ad Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5ad.xlarge | X86_64 | 1.21 | 1.21  
[C5d Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5d.12xlarge | X86_64 | 1.21 | 1.21  
[C5d Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5d.18xlarge | X86_64 | 1.21 | 1.21  
[C5d Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5d.24xlarge | X86_64 | 1.21 | 1.21  
[C5d Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5d.2xlarge | X86_64 | 1.21 | 1.21  
[C5d Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5d.4xlarge | X86_64 | 1.21 | 1.21  
[C5d Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5d.9xlarge | X86_64 | 1.21 | 1.21  
[C5d Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5d.large | X86_64 | 1.21 | 1.21  
[C5d Instances](https://aws.amazon.com/ec2/instance-types/c5/) | c5d.xlarge | X86_64 | 1.21 | 1.21  
[C6g Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6g.12xlarge | ARM64 | Not Supported | 1.25  
[C6g Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6g.16xlarge | ARM64 | Not Supported | 1.25  
[C6g Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6g.2xlarge | ARM64 | Not Supported | 1.25  
[C6g Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6g.4xlarge | ARM64 | Not Supported | 1.25  
[C6g Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6g.8xlarge | ARM64 | Not Supported | 1.25  
[C6g Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6g.large | ARM64 | Not Supported | 1.25  
[C6g Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6g.medium | ARM64 | Not Supported | 1.25  
[C6g Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6g.xlarge | ARM64 | Not Supported | 1.25  
[C6gd Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gd.12xlarge | ARM64 | Not Supported | 1.25  
[C6gd Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gd.16xlarge | ARM64 | Not Supported | 1.25  
[C6gd Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gd.2xlarge | ARM64 | Not Supported | 1.25  
[C6gd Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gd.4xlarge | ARM64 | Not Supported | 1.25  
[C6gd Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gd.8xlarge | ARM64 | Not Supported | 1.25  
[C6gd Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gd.large | ARM64 | Not Supported | 1.25  
[C6gd Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gd.medium | ARM64 | Not Supported | 1.25  
[C6gd Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gd.xlarge | ARM64 | Not Supported | 1.25  
[C6gn Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gn.12xlarge | ARM64 | Not Supported | 1.25  
[C6gn Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gn.16xlarge | ARM64 | Not Supported | 1.25  
[C6gn Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gn.2xlarge | ARM64 | Not Supported | 1.25  
[C6gn Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gn.4xlarge | ARM64 | Not Supported | 1.25  
[C6gn Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gn.8xlarge | ARM64 | Not Supported | 1.25  
[C6gn Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gn.large | ARM64 | Not Supported | 1.25  
[C6gn Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gn.medium | ARM64 | Not Supported | 1.25  
[C6gn Instances](https://aws.amazon.com/ec2/instance-types/c6g/) | c6gn.xlarge | ARM64 | Not Supported | 1.25  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.12xlarge | X86_64 | Not Supported | 1.26  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.16xlarge | X86_64 | Not Supported | 1.26  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.24xlarge | X86_64 | Not Supported | 1.26  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.2xlarge | X86_64 | Not Supported | 1.26  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.32xlarge | X86_64 | Not Supported | 1.26  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.4xlarge | X86_64 | Not Supported | 1.26  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.8xlarge | X86_64 | Not Supported | 1.26  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.large | X86_64 | Not Supported | 1.26  
[C6i Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6i.xlarge | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.12xlarge | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.16xlarge | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.24xlarge | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.2xlarge | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.32xlarge | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.4xlarge | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.8xlarge | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.large | X86_64 | Not Supported | 1.26  
[C6id Instances](https://aws.amazon.com/ec2/instance-types/c6i/) | c6id.xlarge | X86_64 | Not Supported | 1.26  
[C7g Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7g.12xlarge | ARM64 | Not Supported | 1.25  
[C7g Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7g.16xlarge | ARM64 | Not Supported | 1.25  
[C7g Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7g.2xlarge | ARM64 | Not Supported | 1.25  
[C7g Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7g.4xlarge | ARM64 | Not Supported | 1.25  
[C7g Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7g.8xlarge | ARM64 | Not Supported | 1.25  
[C7g Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7g.large | ARM64 | Not Supported | 1.25  
[C7g Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7g.medium | ARM64 | Not Supported | 1.25  
[C7g Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7g.xlarge | ARM64 | Not Supported | 1.25  
[C7gn Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7gn.12xlarge | ARM64 | Not Supported | 1.25  
[C7gn Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7gn.16xlarge | ARM64 | Not Supported | 1.25  
[C7gn Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7gn.2xlarge | ARM64 | Not Supported | 1.25  
[C7gn Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7gn.4xlarge | ARM64 | Not Supported | 1.25  
[C7gn Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7gn.8xlarge | ARM64 | Not Supported | 1.25  
[C7gn Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7gn.large | ARM64 | Not Supported | 1.25  
[C7gn Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7gn.medium | ARM64 | Not Supported | 1.25  
[C7gn Instances](https://aws.amazon.com/ec2/instance-types/c7g/) | c7gn.xlarge | ARM64 | Not Supported | 1.25  
[G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) | g5.12xlarge | X86_64 | Not Supported | 1.26  
[G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) | g5.16xlarge | X86_64 | Not Supported | 1.26  
[G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) | g5.24xlarge | X86_64 | Not Supported | 1.26  
[G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) | g5.2xlarge | X86_64 | Not Supported | 1.26  
[G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) | g5.48xlarge | X86_64 | Not Supported | 1.26  
[G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) | g5.4xlarge | X86_64 | Not Supported | 1.26  
[G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) | g5.8xlarge | X86_64 | Not Supported | 1.26  
[G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) | g5.xlarge | X86_64 | Not Supported | 1.26  
[G5g Instances](https://aws.amazon.com/ec2/instance-types/g5g/) | g5g.16xlarge | ARM64 | Not Supported | 1.25  
[G5g Instances](https://aws.amazon.com/ec2/instance-types/g5g/) | g5g.2xlarge | ARM64 | Not Supported | 1.25  
[G5g Instances](https://aws.amazon.com/ec2/instance-types/g5g/) | g5g.4xlarge | ARM64 | Not Supported | 1.25  
[G5g Instances](https://aws.amazon.com/ec2/instance-types/g5g/) | g5g.8xlarge | ARM64 | Not Supported | 1.25  
[G5g Instances](https://aws.amazon.com/ec2/instance-types/g5g/) | g5g.xlarge | ARM64 | Not Supported | 1.25  
[I3en Instances](https://aws.amazon.com/ec2/instance-types/i3en/) | i3en.12xlarge | X86_64 | 1.21 | 1.21  
[I3en Instances](https://aws.amazon.com/ec2/instance-types/i3en/) | i3en.24xlarge | X86_64 | 1.21 | 1.21  
[I3en Instances](https://aws.amazon.com/ec2/instance-types/i3en/) | i3en.2xlarge | X86_64 | 1.21 | 1.21  
[I3en Instances](https://aws.amazon.com/ec2/instance-types/i3en/) | i3en.3xlarge | X86_64 | 1.21 | 1.21  
[I3en Instances](https://aws.amazon.com/ec2/instance-types/i3en/) | i3en.6xlarge | X86_64 | 1.21 | 1.21  
[I3en Instances](https://aws.amazon.com/ec2/instance-types/i3en/) | i3en.large | X86_64 | 1.21 | 1.21  
[I3en Instances](https://aws.amazon.com/ec2/instance-types/i3en/) | i3en.metal | X86_64 | Not Supported | 1.26  
[I3en Instances](https://aws.amazon.com/ec2/instance-types/i3en/) | i3en.xlarge | X86_64 | 1.21 | 1.21  
[I4g Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | i4g.16xlarge | ARM64 | Not Supported | 1.28  
[I4g Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | i4g.2xlarge | ARM64 | Not Supported | 1.28  
[I4g Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | i4g.4xlarge | ARM64 | Not Supported | 1.28  
[I4g Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | i4g.8xlarge | ARM64 | Not Supported | 1.28  
[I4g Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | i4g.large | ARM64 | Not Supported | 1.28  
[I4g Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | i4g.xlarge | ARM64 | Not Supported | 1.28  
[I4i Instances](https://aws.amazon.com/ec2/instance-types/i4i/) | i4i.16xlarge | X86_64 | Not Supported | 1.26  
[I4i Instances](https://aws.amazon.com/ec2/instance-types/i4i/) | i4i.2xlarge | X86_64 | Not Supported | 1.26  
[I4i Instances](https://aws.amazon.com/ec2/instance-types/i4i/) | i4i.32xlarge | X86_64 | Not Supported | 1.26  
[I4i Instances](https://aws.amazon.com/ec2/instance-types/i4i/) | i4i.4xlarge | X86_64 | Not Supported | 1.26  
[I4i Instances](https://aws.amazon.com/ec2/instance-types/i4i/) | i4i.8xlarge | X86_64 | Not Supported | 1.26  
[I4i Instances](https://aws.amazon.com/ec2/instance-types/i4i/) | i4i.large | X86_64 | Not Supported | 1.26  
[I4i Instances](https://aws.amazon.com/ec2/instance-types/i4i/) | i4i.xlarge | X86_64 | Not Supported | 1.26  
[Im4gn Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | im4gn.16xlarge | ARM64 | Not Supported | 1.25  
[Im4gn Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | im4gn.2xlarge | ARM64 | Not Supported | 1.25  
[Im4gn Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | im4gn.4xlarge | ARM64 | Not Supported | 1.25  
[Im4gn Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | im4gn.8xlarge | ARM64 | Not Supported | 1.25  
[Im4gn Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | im4gn.large | ARM64 | Not Supported | 1.25  
[Im4gn Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | im4gn.xlarge | ARM64 | Not Supported | 1.25  
[Is4gen Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | is4gen.2xlarge | ARM64 | Not Supported | 1.25  
[Is4gen Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | is4gen.4xlarge | ARM64 | Not Supported | 1.25  
[Is4gen Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | is4gen.8xlarge | ARM64 | Not Supported | 1.25  
[Is4gen Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | is4gen.large | ARM64 | Not Supported | 1.25  
[Is4gen Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | is4gen.medium | ARM64 | Not Supported | 1.25  
[Is4gen Instances](https://aws.amazon.com/ec2/instance-types/i4g/) | is4gen.xlarge | ARM64 | Not Supported | 1.25  
[M5 Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5.12xlarge | X86_64 | 1.21 | 1.21  
[M5 Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5.16xlarge | X86_64 | 1.21 | 1.21  
[M5 Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5.24xlarge | X86_64 | 1.21 | 1.21  
[M5 Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5.2xlarge | X86_64 | 1.21 | 1.21  
[M5 Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5.4xlarge | X86_64 | 1.21 | 1.21  
[M5 Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5.8xlarge | X86_64 | 1.21 | 1.21  
[M5 Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5.large | X86_64 | 1.21 | 1.21  
[M5 Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5.xlarge | X86_64 | 1.21 | 1.21  
[M5a Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5a.12xlarge | X86_64 | 1.21 | 1.21  
[M5a Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5a.16xlarge | X86_64 | 1.21 | 1.21  
[M5a Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5a.24xlarge | X86_64 | 1.21 | 1.21  
[M5a Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5a.2xlarge | X86_64 | 1.21 | 1.21  
[M5a Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5a.4xlarge | X86_64 | 1.21 | 1.21  
[M5a Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5a.8xlarge | X86_64 | 1.21 | 1.21  
[M5a Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5a.large | X86_64 | 1.21 | 1.21  
[M5a Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5a.xlarge | X86_64 | 1.21 | 1.21  
[M5ad Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5ad.12xlarge | X86_64 | 1.21 | 1.21  
[M5ad Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5ad.16xlarge | X86_64 | 1.21 | 1.21  
[M5ad Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5ad.24xlarge | X86_64 | 1.21 | 1.21  
[M5ad Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5ad.2xlarge | X86_64 | 1.21 | 1.21  
[M5ad Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5ad.4xlarge | X86_64 | 1.21 | 1.21  
[M5ad Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5ad.8xlarge | X86_64 | 1.21 | 1.21  
[M5ad Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5ad.large | X86_64 | 1.21 | 1.21  
[M5ad Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5ad.xlarge | X86_64 | 1.21 | 1.21  
[M5d Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5d.12xlarge | X86_64 | 1.21 | 1.21  
[M5d Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5d.16xlarge | X86_64 | 1.21 | 1.21  
[M5d Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5d.24xlarge | X86_64 | 1.21 | 1.21  
[M5d Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5d.2xlarge | X86_64 | 1.21 | 1.21  
[M5d Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5d.4xlarge | X86_64 | 1.21 | 1.21  
[M5d Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5d.8xlarge | X86_64 | 1.21 | 1.21  
[M5d Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5d.large | X86_64 | 1.21 | 1.21  
[M5d Instances](https://aws.amazon.com/ec2/instance-types/m5/) | m5d.xlarge | X86_64 | 1.21 | 1.21  
[M6g Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6g.12xlarge | ARM64 | Not Supported | 1.24  
[M6g Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6g.16xlarge | ARM64 | Not Supported | 1.24  
[M6g Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6g.2xlarge | ARM64 | Not Supported | 1.24  
[M6g Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6g.4xlarge | ARM64 | Not Supported | 1.24  
[M6g Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6g.8xlarge | ARM64 | Not Supported | 1.24  
[M6g Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6g.large | ARM64 | Not Supported | 1.24  
[M6g Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6g.medium | ARM64 | Not Supported | 1.24  
[M6g Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6g.xlarge | ARM64 | Not Supported | 1.24  
[M6gd Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6gd.12xlarge | ARM64 | Not Supported | 1.24  
[M6gd Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6gd.16xlarge | ARM64 | Not Supported | 1.24  
[M6gd Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6gd.2xlarge | ARM64 | Not Supported | 1.24  
[M6gd Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6gd.4xlarge | ARM64 | Not Supported | 1.24  
[M6gd Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6gd.8xlarge | ARM64 | Not Supported | 1.24  
[M6gd Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6gd.large | ARM64 | Not Supported | 1.24  
[M6gd Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6gd.medium | ARM64 | Not Supported | 1.24  
[M6gd Instances](https://aws.amazon.com/ec2/instance-types/m6g/) | m6gd.xlarge | ARM64 | Not Supported | 1.24  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.12xlarge | X86_64 | 1.26 | 1.26  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.16xlarge | X86_64 | 1.26 | 1.26  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.24xlarge | X86_64 | 1.26 | 1.26  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.2xlarge | X86_64 | 1.26 | 1.26  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.32xlarge | X86_64 | 1.26 | 1.26  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.4xlarge | X86_64 | 1.26 | 1.26  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.8xlarge | X86_64 | 1.26 | 1.26  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.large | X86_64 | 1.26 | 1.26  
[M6i Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6i.xlarge | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.12xlarge | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.16xlarge | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.24xlarge | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.2xlarge | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.32xlarge | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.4xlarge | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.8xlarge | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.large | X86_64 | 1.26 | 1.26  
[M6id Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6id.xlarge | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.12xlarge | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.16xlarge | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.24xlarge | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.2xlarge | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.32xlarge | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.4xlarge | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.8xlarge | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.large | X86_64 | 1.26 | 1.26  
[M6idn Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6idn.xlarge | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.12xlarge | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.16xlarge | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.24xlarge | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.2xlarge | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.32xlarge | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.4xlarge | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.8xlarge | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.large | X86_64 | 1.26 | 1.26  
[M6in Instances](https://aws.amazon.com/ec2/instance-types/m6i/) | m6in.xlarge | X86_64 | 1.26 | 1.26  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.12xlarge | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.16xlarge | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.24xlarge | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.2xlarge | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.32xlarge | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.48xlarge | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.4xlarge | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.8xlarge | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.large | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.medium | X86_64 | Not Supported | 1.28  
[M7a Instances](https://aws.amazon.com/ec2/instance-types/m7a/) | m7a.xlarge | X86_64 | Not Supported | 1.28  
[M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7g.12xlarge | ARM64 | Not Supported | 1.28  
[M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7g.16xlarge | ARM64 | Not Supported | 1.28  
[M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7g.2xlarge | ARM64 | Not Supported | 1.28  
[M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7g.4xlarge | ARM64 | Not Supported | 1.28  
[M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7g.8xlarge | ARM64 | Not Supported | 1.28  
[M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7g.large | ARM64 | Not Supported | 1.28  
[M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7g.medium | ARM64 | Not Supported | 1.28  
[M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7g.xlarge | ARM64 | Not Supported | 1.28  
[M7gd Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7gd.12xlarge | ARM64 | Not Supported | 1.28  
[M7gd Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7gd.16xlarge | ARM64 | Not Supported | 1.28  
[M7gd Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7gd.2xlarge | ARM64 | Not Supported | 1.28  
[M7gd Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7gd.4xlarge | ARM64 | Not Supported | 1.28  
[M7gd Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7gd.8xlarge | ARM64 | Not Supported | 1.28  
[M7gd Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7gd.large | ARM64 | Not Supported | 1.28  
[M7gd Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7gd.medium | ARM64 | Not Supported | 1.28  
[M7gd Instances](https://aws.amazon.com/ec2/instance-types/m7g/) | m7gd.xlarge | ARM64 | Not Supported | 1.28  
[M7i-Flex Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i-flex.2xlarge | X86_64 | 1.26 | 1.26  
[M7i-Flex Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i-flex.4xlarge | X86_64 | 1.26 | 1.26  
[M7i-Flex Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i-flex.8xlarge | X86_64 | 1.26 | 1.26  
[M7i-Flex Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i-flex.large | X86_64 | 1.26 | 1.26  
[M7i-Flex Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i-flex.xlarge | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.12xlarge | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.16xlarge | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.24xlarge | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.2xlarge | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.48xlarge | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.4xlarge | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.8xlarge | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.large | X86_64 | 1.26 | 1.26  
[M7i Instances](https://aws.amazon.com/ec2/instance-types/m7i/) | m7i.xlarge | X86_64 | 1.26 | 1.26  
[R5 Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5.12xlarge | X86_64 | 1.21 | 1.21  
[R5 Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5.16xlarge | X86_64 | 1.21 | 1.21  
[R5 Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5.24xlarge | X86_64 | 1.21 | 1.21  
[R5 Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5.2xlarge | X86_64 | 1.21 | 1.21  
[R5 Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5.4xlarge | X86_64 | 1.21 | 1.21  
[R5 Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5.8xlarge | X86_64 | 1.21 | 1.21  
[R5 Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5.large | X86_64 | 1.21 | 1.21  
[R5 Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5.xlarge | X86_64 | 1.21 | 1.21  
[R5a Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5a.12xlarge | X86_64 | 1.21 | 1.21  
[R5a Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5a.16xlarge | X86_64 | 1.21 | 1.21  
[R5a Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5a.24xlarge | X86_64 | 1.21 | 1.21  
[R5a Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5a.2xlarge | X86_64 | 1.21 | 1.21  
[R5a Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5a.4xlarge | X86_64 | 1.21 | 1.21  
[R5a Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5a.8xlarge | X86_64 | 1.21 | 1.21  
[R5a Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5a.large | X86_64 | 1.21 | 1.21  
[R5a Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5a.xlarge | X86_64 | 1.21 | 1.21  
[R5ad Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5ad.12xlarge | X86_64 | 1.21 | 1.21  
[R5ad Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5ad.16xlarge | X86_64 | 1.21 | 1.21  
[R5ad Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5ad.24xlarge | X86_64 | 1.21 | 1.21  
[R5ad Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5ad.2xlarge | X86_64 | 1.21 | 1.21  
[R5ad Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5ad.4xlarge | X86_64 | 1.21 | 1.21  
[R5ad Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5ad.8xlarge | X86_64 | 1.21 | 1.21  
[R5ad Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5ad.large | X86_64 | 1.21 | 1.21  
[R5ad Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5ad.xlarge | X86_64 | 1.21 | 1.21  
[R5d Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5d.12xlarge | X86_64 | 1.21 | 1.21  
[R5d Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5d.16xlarge | X86_64 | 1.21 | 1.21  
[R5d Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5d.24xlarge | X86_64 | 1.21 | 1.21  
[R5d Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5d.2xlarge | X86_64 | 1.21 | 1.21  
[R5d Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5d.4xlarge | X86_64 | 1.21 | 1.21  
[R5d Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5d.8xlarge | X86_64 | 1.21 | 1.21  
[R5d Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5d.large | X86_64 | 1.21 | 1.21  
[R5d Instances](https://aws.amazon.com/ec2/instance-types/r5/) | r5d.xlarge | X86_64 | 1.21 | 1.21  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.12xlarge | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.16xlarge | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.24xlarge | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.2xlarge | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.32xlarge | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.48xlarge | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.4xlarge | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.8xlarge | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.large | X86_64 | Not Supported | 1.26  
[R6a Instances](https://aws.amazon.com/ec2/instance-types/r6a/) | r6a.xlarge | X86_64 | Not Supported | 1.26  
[R6g Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6g.12xlarge | ARM64 | Not Supported | 1.24  
[R6g Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6g.16xlarge | ARM64 | Not Supported | 1.24  
[R6g Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6g.2xlarge | ARM64 | Not Supported | 1.24  
[R6g Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6g.4xlarge | ARM64 | Not Supported | 1.24  
[R6g Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6g.8xlarge | ARM64 | Not Supported | 1.24  
[R6g Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6g.large | ARM64 | Not Supported | 1.24  
[R6g Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6g.medium | ARM64 | Not Supported | 1.24  
[R6g Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6g.xlarge | ARM64 | Not Supported | 1.24  
[R6gd Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6gd.12xlarge | ARM64 | Not Supported | 1.24  
[R6gd Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6gd.16xlarge | ARM64 | Not Supported | 1.24  
[R6gd Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6gd.2xlarge | ARM64 | Not Supported | 1.24  
[R6gd Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6gd.4xlarge | ARM64 | Not Supported | 1.24  
[R6gd Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6gd.8xlarge | ARM64 | Not Supported | 1.24  
[R6gd Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6gd.large | ARM64 | Not Supported | 1.24  
[R6gd Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6gd.medium | ARM64 | Not Supported | 1.24  
[R6gd Instances](https://aws.amazon.com/ec2/instance-types/r6g/) | r6gd.xlarge | ARM64 | Not Supported | 1.24  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.12xlarge | X86_64 | Not Supported | 1.26  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.16xlarge | X86_64 | Not Supported | 1.26  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.24xlarge | X86_64 | Not Supported | 1.26  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.2xlarge | X86_64 | Not Supported | 1.26  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.32xlarge | X86_64 | Not Supported | 1.26  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.4xlarge | X86_64 | Not Supported | 1.26  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.8xlarge | X86_64 | Not Supported | 1.26  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.large | X86_64 | Not Supported | 1.26  
[R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6i.xlarge | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.12xlarge | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.16xlarge | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.24xlarge | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.2xlarge | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.32xlarge | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.4xlarge | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.8xlarge | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.large | X86_64 | Not Supported | 1.26  
[R6id Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6id.xlarge | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.12xlarge | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.16xlarge | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.24xlarge | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.2xlarge | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.32xlarge | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.4xlarge | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.8xlarge | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.large | X86_64 | Not Supported | 1.26  
[R6idn Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6idn.xlarge | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.12xlarge | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.16xlarge | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.24xlarge | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.2xlarge | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.32xlarge | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.4xlarge | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.8xlarge | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.large | X86_64 | Not Supported | 1.26  
[R6in Instances](https://aws.amazon.com/ec2/instance-types/r6i/) | r6in.xlarge | X86_64 | Not Supported | 1.26  
[R7g Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7g.12xlarge | ARM64 | Not Supported | 1.28  
[R7g Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7g.16xlarge | ARM64 | Not Supported | 1.28  
[R7g Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7g.2xlarge | ARM64 | Not Supported | 1.28  
[R7g Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7g.4xlarge | ARM64 | Not Supported | 1.28  
[R7g Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7g.8xlarge | ARM64 | Not Supported | 1.28  
[R7g Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7g.large | ARM64 | Not Supported | 1.28  
[R7g Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7g.medium | ARM64 | Not Supported | 1.28  
[R7g Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7g.xlarge | ARM64 | Not Supported | 1.28  
[R7gd Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7gd.12xlarge | ARM64 | Not Supported | 1.28  
[R7gd Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7gd.16xlarge | ARM64 | Not Supported | 1.28  
[R7gd Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7gd.2xlarge | ARM64 | Not Supported | 1.28  
[R7gd Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7gd.4xlarge | ARM64 | Not Supported | 1.28  
[R7gd Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7gd.8xlarge | ARM64 | Not Supported | 1.28  
[R7gd Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7gd.large | ARM64 | Not Supported | 1.28  
[R7gd Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7gd.medium | ARM64 | Not Supported | 1.28  
[R7gd Instances](https://aws.amazon.com/ec2/instance-types/r7g/) | r7gd.xlarge | ARM64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.12xlarge | X86_64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.16xlarge | X86_64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.24xlarge | X86_64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.2xlarge | X86_64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.48xlarge | X86_64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.4xlarge | X86_64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.8xlarge | X86_64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.large | X86_64 | Not Supported | 1.28  
[R7i Instances](https://aws.amazon.com/ec2/instance-types/r7i/) | r7i.xlarge | X86_64 | Not Supported | 1.28  
[R7iz Instances](https://aws.amazon.com/ec2/instance-types/r7iz/) | r7iz.12xlarge | X86_64 | Not Supported | 1.28  
[R7iz Instances](https://aws.amazon.com/ec2/instance-types/r7iz/) | r7iz.16xlarge | X86_64 | Not Supported | 1.28  
[R7iz Instances](https://aws.amazon.com/ec2/instance-types/r7iz/) | r7iz.2xlarge | X86_64 | Not Supported | 1.28  
[R7iz Instances](https://aws.amazon.com/ec2/instance-types/r7iz/) | r7iz.32xlarge | X86_64 | Not Supported | 1.28  
[R7iz Instances](https://aws.amazon.com/ec2/instance-types/r7iz/) | r7iz.4xlarge | X86_64 | Not Supported | 1.28  
[R7iz Instances](https://aws.amazon.com/ec2/instance-types/r7iz/) | r7iz.8xlarge | X86_64 | Not Supported | 1.28  
[R7iz Instances](https://aws.amazon.com/ec2/instance-types/r7iz/) | r7iz.large | X86_64 | Not Supported | 1.28  
[R7iz Instances](https://aws.amazon.com/ec2/instance-types/r7iz/) | r7iz.xlarge | X86_64 | Not Supported | 1.28  
[T3 Instances](https://aws.amazon.com/ec2/instance-types/t3/) | t3.2xlarge | X86_64 | 1.21 | 1.21  
[T3 Instances](https://aws.amazon.com/ec2/instance-types/t3/) | t3.large | X86_64 | 1.21 | 1.21  
[T3 Instances](https://aws.amazon.com/ec2/instance-types/t3/) | t3.medium | X86_64 | 1.21 | 1.21  
[T3 Instances](https://aws.amazon.com/ec2/instance-types/t3/) | t3.xlarge | X86_64 | 1.21 | 1.21  
[T3a Instances](https://aws.amazon.com/ec2/instance-types/t3/) | t3a.2xlarge | X86_64 | 1.21 | 1.21  
[T3a Instances](https://aws.amazon.com/ec2/instance-types/t3/) | t3a.large | X86_64 | 1.21 | 1.21  
[T3a Instances](https://aws.amazon.com/ec2/instance-types/t3/) | t3a.medium | X86_64 | 1.21 | 1.21  
[T3a Instances](https://aws.amazon.com/ec2/instance-types/t3/) | t3a.xlarge | X86_64 | 1.21 | 1.21  
[T4g Instances](https://aws.amazon.com/ec2/instance-types/t4/) | t4g.2xlarge | ARM64 | Not Supported | 1.24  
[T4g Instances](https://aws.amazon.com/ec2/instance-types/t4/) | t4g.large | ARM64 | Not Supported | 1.24  
[T4g Instances](https://aws.amazon.com/ec2/instance-types/t4/) | t4g.medium | ARM64 | Not Supported | 1.24  
[T4g Instances](https://aws.amazon.com/ec2/instance-types/t4/) | t4g.xlarge | ARM64 | Not Supported | 1.24  
[X2gd Instances](https://aws.amazon.com/ec2/instance-types/x2g/) | x2gd.12xlarge | ARM64 | Not Supported | 1.25  
[X2gd Instances](https://aws.amazon.com/ec2/instance-types/x2g/) | x2gd.16xlarge | ARM64 | Not Supported | 1.25  
[X2gd Instances](https://aws.amazon.com/ec2/instance-types/x2g/) | x2gd.2xlarge | ARM64 | Not Supported | 1.25  
[X2gd Instances](https://aws.amazon.com/ec2/instance-types/x2g/) | x2gd.4xlarge | ARM64 | Not Supported | 1.25  
[X2gd Instances](https://aws.amazon.com/ec2/instance-types/x2g/) | x2gd.8xlarge | ARM64 | Not Supported | 1.25  
[X2gd Instances](https://aws.amazon.com/ec2/instance-types/x2g/) | x2gd.large | ARM64 | Not Supported | 1.25  
[X2gd Instances](https://aws.amazon.com/ec2/instance-types/x2g/) | x2gd.medium | ARM64 | Not Supported | 1.25  
[X2gd Instances](https://aws.amazon.com/ec2/instance-types/x2g/) | x2gd.xlarge | ARM64 | Not Supported | 1.25  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
