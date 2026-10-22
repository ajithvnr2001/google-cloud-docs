---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture/
title: GKE on AWS architecture \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:24.179502+00:00
---

# GKE on AWS architecture  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  GKE on AWS architecture Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS is a managed service that helps you provision, operate, and scale Kubernetes clusters in your AWS account.

This page is for Admins and architects and Operators who want to define IT solutions and system architecture in accordance with company strategy and requirements. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Resource management

GKE on AWS uses AWS APIs to provision the resources needed by your cluster, including virtual machines, managed disks, Auto Scaling group, security groups, and load balancers.

You can create, describe, and delete clusters with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws) or [GKE Multi-Cloud API](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest).

### Authenticating to AWS

When you set up GKE on AWS, you create an AWS IAM role in your AWS account with the required permissions. You also create a service account in your Google Cloud project to establish a trust relationship for [AWS IAM identity federation](https://aws.amazon.com/identity/federation/). 

For more information, see [Authentication overview](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/authentication).

### Resources on Google Cloud

GKE on AWS uses a Google Cloud project to store cluster configuration information on Google Cloud.

**Warning:** Soon after you delete a Google Cloud project, any cluster resources in AWS are permanently deleted. To safeguard against the accidental deletion of a Google Cloud project, use [Project liens](https://docs.cloud.google.com/resource-manager/docs/project-liens).

## Fleets and Connect

GKE on AWS registers each cluster with a [Fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) when it is created. [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview) enables access to cluster and workload management features from Google Cloud. A cluster's Fleet membership name is the same as its cluster name.

You can enable features such as Config Management and Cloud Service Mesh within your Fleet.

## Cluster architecture

GKE on AWS provisions clusters using private subnets inside your AWS Virtual Private Cloud. Each cluster consists of the following components:

  * **Control plane** : The Kubernetes control plane uses a high-availability architecture with three replicas. Each replica runs all Kubernetes components including `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, and `etcd`. Each `etcd` instance stores data in an EBS volume, and uses a network interface to communicate with other `etcd` instances. A standard load balancer is used to balance traffic to the Kubernetes API endpoint, `kube-apiserver`.

  * **Node pools** : A node pool is a group of Kubernetes worker nodes with the same configuration, including instance type, disk configuration, and instance profile. All nodes in a node pool run on the same subnet. For high availability, you can provision multiple node pools across different subnets in the same AWS region.




The following diagram shows a sample VPC, node pool, and control plane structure, including network address translation (NAT) gateway and load balancer. You create this infrastructure with the instructions to [Create an AWS VPC](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-vpc) and [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quickstart).

![Sample VPC](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/images/vpc-with-nat-and-load-balancer.svg)

## What's next

  * Complete the [Prerequisites](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
