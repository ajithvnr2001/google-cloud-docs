---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups/
title: Security groups rules \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:35.975445+00:00
---

# Security groups rules  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Security groups rules Stay organized with collections  Save and categorize content based on your preferences. 

This topic explains how GKE on AWS manages [AWS security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) rules for the cluster, and how to modify the firewall rules for node pools and control plane replicas.

## Security groups and hosted DNS

If you use a hosted DNS server instead of the AWS-provided DNS, your control plane and node pool security groups must allow outbound traffic on TCP and UDP port 53.

## Control plane security groups

The control plane security groups define the firewall rules for inbound and outbound TCP traffic for each control plane replica.

The control plane consists of three [EC2](https://aws.amazon.com/ec2/) instances behind an AWS Network Load Balancer ([NLB](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)). These instances accept connections from etcd instances on other nodes, node pool nodes, and the NLB. Control plane instances also make outbound HTTPS connections to Google and AWS services.

GKE on AWS creates and attaches a managed control plane security group to all control plane instances. You should not modify the rules in this group. If you need to add more security group rules, you can instead specify additional security group IDs to attach to the control plane when you [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster).

### Default control plane security group rules

These are the default rules GKE on AWS attaches to the control plane. These rules will not match your security groups exactly; each row in the table might expand to multiple AWS security group rules.

**Type** | **Protocol** | **Port** | **Address ranges or SG** | **Description**  
---|---|---|---|---  
Inbound | TCP (cluster version < 1.26) | 443 | VPC Primary CIDR range | Allow HTTPS from node pool nodes  
Inbound | TCP (cluster version >= 1.26) | 443 | Subnet CIDR range of node pool | Allow HTTPS from node pool nodes (one rule per subnet used by node pools)  
Inbound | TCP | 2380 | Control plane SG | Allow control plane etcd replication  
Inbound | TCP | 2381 | Control plane SG | Allow control plane etcd event replication  
Inbound | TCP (cluster version < 1.26) | 8132 | VPC Primary CIDR range | Allow Konnectivity connections from node pools  
Inbound | TCP (cluster version >= 1.26) | 8132 | Subnet CIDR range of node pool | Allow Konnectivity connections from node pool nodes (one rule per subnet used by node pools)  
Inbound | TCP | 11872 | Control plane CIDR ranges | HTTP health check for load balancer  
Outbound | TCP | 443 | 0.0.0.0/0 | Allow outbound HTTPS  
Outbound | TCP | 2380 | Control plane SG | Allow control plane etcd replication  
Outbound | TCP | 2381 | Control plane SG | Allow control plane etcd event replication  
  
## Node pool security groups

The node pool security groups define the firewall rules for inbound and outbound TCP traffic for the VMs in node pools.

GKE on AWS creates and attaches a managed node pool security group to all node pool instances. You should not modify the rules in this group. If you need to add more security group rules, you can instead specify additional security group IDs to attach to instances when you [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool).

By default, node pool VMs do not have any open ports. To allow incoming traffic, you add a node pool security group when creating the node pool, and manage any desired inbound/outbound rules for the node pool through that security group.

### Default node pool security group rules

These are the default rules GKE on AWS attaches to node pools. These rules will not match your security groups exactly; each row in the table might expand to multiple AWS security group rules.

**Type** | **Protocol** | **Port** | **Address range or SG** | **Description**  
---|---|---|---|---  
Inbound | TCP | All | Node pool SG | Allow pod-to-pod communication  
Outbound | TCP | All | Node pool SG | Allow pod-to-pod communication  
Outbound | TCP | 443 | 0.0.0.0/0 | Allow outbound HTTPS  
Outbound | TCP | 8132 | Control plane SG | Allow Konnectivity connections to the control plane  
Outbound | TCP | 8132 | Control plane CIDR ranges | Allow Konnectivity connections to the control plane  
  
### Node pools in VPC Secondary CIDR blocks

GKE on AWS version 1.26 and later automatically creates and manages the necessary security group rules to support node pools using subnets in secondary VPC CIDR blocks. If you're using one of these versions, you don't need to create custom security groups or update them manually.

However, when creating managed control plane security groups, earlier versions of GKE on AWS don't create rules that support node pools with subnets in a [secondary VPC CIDR block](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html).

To work around this limitation, create a custom security group for your control plane. You pass the security group ID when creating a cluster using the [`--security-group-ids`](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--security-group-ids) flag. Alternatively, you can [Update your cluster's security groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-cluster#update_your_clusters_security_groups).

Create the security group with the following rules:

**Type** | **Protocol** | **Port** | **Address ranges or SG** | **Description**  
---|---|---|---|---  
Inbound | TCP | 443 | Node pool ranges (in VPC secondary CIDR blocks) | Allow HTTPS from node pool nodes  
Inbound | TCP | 8132 | Node pool ranges (in VPC secondary CIDR blocks) | Allow Konnectivity connections from node pools  
  
## What's next

  * [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster).
  * [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
