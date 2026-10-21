---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster/
title: Create a cluster \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:05.171677+00:00
---

# Create a cluster  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Create a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a GKE on AWS cluster. You can also [Create a VPC and cluster with Terraform](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster-with-terraform).

This page is for Admins and architects and Operators who want to set up, monitor, and manage cloud infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before creating a cluster, you must complete the [prerequisites](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/prerequisites). In particular, you must provide the following resources:

  * An AWS VPC where the cluster will run.
  * Up to three AWS subnets for the three control plane replicas. Each must be in a different AWS Availability Zone.
  * The AWS IAM role that GKE on AWS assumes when managing your cluster. This requires a specific set of [IAM permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles).
  * KMS symmetric CMK keys for at-rest encryption of cluster data (etcd) and configuration.
  * The AWS IAM instance profile for each control plane replica. This requires a specific set of [IAM permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles).
  * An EC2 SSH key pair (optional) if you need SSH access to the EC2 instances that run each control plane replica.



It is your responsibility to create and manage these resources, which can be shared between all your GKE clusters. All other underlying cluster-scoped AWS resources are managed by GKE on AWS.

### Select CIDR ranges for your cluster

When you create a cluster in GKE on AWS, you need to provide IPv4 address ranges to use for Pods and Services.

These IP ranges are specified using Classless Inter-Domain Routing ([CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing)) notation—for example, `100.64.0.0/16`.

**Note:** After you create a cluster, you can't change these ranges.

### Recommended ranges

We recommend the following CIDR ranges for Services and Pods:

  * Services: 100.64.0.0/16
  * Pods: 100.96.0.0/11



These ranges are large enough for you to grow your cluster without any issues.

The following sections provide more details.

#### Details about selecting ranges

GKE on AWS uses an overlay network for Pods and Services, so the IP ranges for these networks don't need to be routable within the VPC. Any IP ranges that you use must be guaranteed available. For more information, see [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/dataplane-v2).

  * The Pod and Service IP ranges can overlap with the VPC network, provided either doesn't include the control plane or node pool subnet IP ranges.

  * The Pod and Service IP range must fall within one of the following private IP ranges:

    * `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` — Private IP addresses (RFC 1918)
    * `100.64.0.0/10` — Shared address space (RFC 6598)
    * `192.0.0.0/24` — IETF protocol assignments (RFC 6890)
    * `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` — Documentation (RFC 5737)
    * `192.88.99.0/24` — IPv6 to IPv4 relay (deprecated) (RFC 7526)
    * `198.18.0.0/15` — Benchmark testing (RFC 2544)



We recommend IP ranges within `100.64.0.0/10` (RFC 6598). This range is reserved for carrier-grade NAT, which is likely not used in your VPC.

For example, the following is a valid configuration where the Pod, Service, and Node networks don't overlap (the VPC is using RFC 1918 private IP addresses, whereas the Pod and Service networks are overlaid onto RFC 6598 private IPs).

  * VPC network: `10.0.0.0/16`, `172.16.1.0/24`, `172.16.2.0/24`
  * Pod network: `100.65.0.0/16`
  * Service network: `100.66.0.0/16`



The following is also a valid configuration despite the Pod and Service networks overlap with the VPC network since there is no overlap with the control plane replicas.

  * VPC network: `10.0.0.0/16`
  * Pod network: `10.0.1.0/24`
  * Service network: `10.0.2.0/24`
  * Control Plane Replica subnets: `10.0.3.0/24`, `10.0.4.0/24`, `10.0.5.0/24`



The following configuration is _invalid_ , because the Pod IP range overlaps with the control plane network. This overlap might prevent workloads from communicating with the control plane replica in the VPC network:

  * VPC network: `10.0.0.0/16`
  * Pod network: `10.0.1.0/24`
  * Service network: `10.1.0.0/24`
  * Control Plane Replica subnets: `10.0.1.0/24`, `10.0.2.0/24`, `10.0.3.0/24`



#### Details about the Pod address range

Kubernetes allocates addresses to [Pod](https://kubernetes.io/docs/concepts/workloads/pods) objects from the Pod address range. A cluster's Pod range is split into smaller ranges for each node. When a Pod is scheduled on a particular node, Kubernetes assigns a Pod IP address from the node's range.

To calculate the size of the Pod address range, you need to estimate the number of nodes that you want in your cluster and the number of Pods that you want to run on each node.

The following table provides size recommendations for Pod CIDR ranges based on the number of nodes and Pods that you intend to run.

**Pod address ranges table**

Pod address range | Maximum Pod IP addresses | Maximum nodes | Maximum Pods  
---|---|---|---  
/24  
Smallest possible Pod address range | 256 addresses | 1 node | 110 Pods  
/23 | 512 addresses | 2 nodes | 220 Pods  
/22 | 1,024 addresses | 4 nodes | 440 Pods  
/21 | 2,048 addresses | 8 nodes | 880 Pods  
/20 | 4,096 addresses | 16 nodes | 1,760 Pods  
/19 | 8,192 addresses | 32 nodes | 3,520 Pods  
/18 | 16,384 addresses | 64 nodes | 7,040 Pods  
/17 | 32,768 addresses | 128 nodes | 14,080 Pods  
/16  | 65,536 addresses | 256 nodes | 28,160 Pods  
/15 | 131,072 addresses | 512 nodes | 56,320 Pods  
/14 | 262,144 addresses | 1,024 nodes | 112,640 Pods  
  
#### Details about the service address range

Kubernetes allocates virtual IP addresses for [Service objects](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service)— for example, load balancers from this address range.

To calculate the size of the Service address range, you need to estimate the number of services that you want in your cluster.

The following table provides size recommendations for Service CIDR ranges based on the number of Services that you intend to run.

**Service address ranges table**

Service address range | Maximum number of Services  
---|---  
/27  
Smallest possible Service address range | 32 Services  
/26 | 64 Services  
/25 | 128 Services  
/24 | 256 Services  
/23 | 512 Services  
/22 | 1,024 Services  
/21 | 2,048 Services  
/20 | 4,096 Services  
/19 | 8,192 Services  
/18 | 16,384 Services  
/17 | 32,768 Services  
/16  
Largest possible Service address range | 65,536 Services  
  
### Select your Fleet host project

[Fleets](https://docs.cloud.google.com/anthos/multicluster-management/fleets) are a Google Cloud concept to organize clusters into larger groups. With fleets, you can manage multiple clusters across several clouds and apply consistent policies across them. The GKE Multi-Cloud API automatically registers your clusters with a Fleet when the cluster is created.

When you create a cluster, you specify a [Fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project) where the cluster will be managed from. Because GKE on AWS uses the cluster name as the Fleet membership name, you must ensure that your cluster names are unique across your Fleet.

**Note:** Once a cluster has been created, you cannot change its Fleet host project.

#### Cross-project registration

If you want to use a Fleet Host project other than the Google Cloud project where the cluster is located, you must apply an additional IAM policy binding to the Multi-Cloud Service Agent service account. This allows the service account to manage Fleets with the Fleet Host Project.

  1. To add the Service Agent to your project, run this command:
         
         gcloud beta services identity create --service=gkemulticloud.googleapis.com \
           --project=CLUSTER_PROJECT_NUMBER
         

Replace `CLUSTER_PROJECT_NUMBER` with your Google Cloud project number.

  2. Assign this binding with the following command:
         
         gcloud projects add-iam-policy-binding FLEET_PROJECT_ID \
           --member="serviceAccount:service-CLUSTER_PROJECT_NUMBER@gcp-sa-gkemulticloud.iam.gserviceaccount.com" \
           --role="roles/gkemulticloud.serviceAgent"
         

Replace the following:

     * `FLEET_PROJECT_ID`: your Fleet host project's Google Cloud project
     * `CLUSTER_PROJECT_NUMBER`: your Google Cloud project number



The Multi-Cloud Service Agent account name has the following format: `service-CLUSTER_PROJECT_NUMBER@gcp-sa-gkemulticloud.iam.gserviceaccount.com`.

You can find your service accounts on the Google Cloud console [Service account](https://console.cloud.google.com/iam-admin/serviceaccounts) page. For more information on how to find your project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

## Create your cluster

Use the following command to create your cluster under GKE on AWS. For more information about this command including its optional parameters, see the [gcloud container aws](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create) reference page.
    
    
    gcloud container aws clusters create CLUSTER_NAME \
      --aws-region AWS_REGION \
      --location GOOGLE_CLOUD_LOCATION \
      --cluster-version CLUSTER_VERSION \
      --fleet-project FLEET_PROJECT \
      --vpc-id VPC_ID \
      --subnet-ids CONTROL_PLANE_SUBNET_1,CONTROL_PLANE_SUBNET_2,CONTROL_PLANE_SUBNET_3 \
      --pod-address-cidr-blocks POD_ADDRESS_CIDR_BLOCKS \
      --service-address-cidr-blocks SERVICE_ADDRESS_CIDR_BLOCKS \
      --role-arn API_ROLE_ARN \
      --database-encryption-kms-key-arn DB_KMS_KEY_ARN \
      --admin-users ADMIN_USERS_LIST \
      --config-encryption-kms-key-arn CONFIG_KMS_KEY_ARN \
      --iam-instance-profile CONTROL_PLANE_PROFILE \
      --tags "Name=CLUSTER_NAME-cp"
    

Replace the following:

  * `CLUSTER_NAME`: your chosen cluster name
  * `AWS_REGION`: the AWS region to create the cluster in
  * `GOOGLE_CLOUD_LOCATION`: the name of the Google Cloud location from which this cluster will be managed, as defined in [Google Cloud management regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/gcp-managed-regions).
  * `CLUSTER_VERSION`: the Kubernetes version to install on your cluster
  * `FLEET_PROJECT`: the [Fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) host project where the cluster will be registered. If you want to manage this cluster from another Google Cloud project, see Cross-project registration.
  * `VPC_ID`: the ID of the AWS VPC for this cluster
  * `CONTROL_PLANE_SUBNET_1`, `CONTROL_PLANE_SUBNET_2`, `CONTROL_PLANE_SUBNET_3`: the subnet IDs for your cluster's three control plane instances
  * `POD_ADDRESS_CIDR_BLOCKS`: the CIDR address range for your cluster's pods
  * `SERVICE_ADDRESS_CIDR_BLOCKS`: the CIDR address range for your cluster's services
  * `API_ROLE_ARN`: the ARN of the GKE Multi-Cloud API role
  * `CONTROL_PLANE_PROFILE`: the profile of the IAM instance associated with the cluster. For details about how to update an IAM instance profile, see [Update AWS IAM instance profile](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-instance-profile).
  * `DB_KMS_KEY_ARN`: the Amazon Resource Name (ARN) of the [AWS KMS key](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-kms-key) to encrypt the cluster's secrets
  * `CONFIG_KMS_KEY_ARN`: the Amazon Resource Name (ARN) of the AWS KMS key to encrypt user data
  * `ADMIN_USERS_LIST` (optional): a comma-separated list of email addresses of the users to grant administrative privileges to - for example, "kai@example.com,hao@example.com,kalani@example.com". Defaults to the user creating the cluster



If present, the `--tags` parameter applies the given AWS tag to all the underlying AWS resources managed by GKE on AWS. This example tags your control plane nodes with name of the cluster they belong to.

You won't be able to SSH into these control plane nodes unless you specify an SSH keypair with the [`--ssh-ec2-key-pair`](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--ssh-ec2-key-pair) flag.

To see all supported Kubernetes versions on a given Google Cloud location, run the following command.
    
    
    gcloud container aws get-server-config --location GCP_LOCATION
    

## Authorize Cloud Logging / Cloud Monitoring

**Note:** Starting with Kubernetes version 1.28, manual policy binding to authorize the `gke-system/gke-telemetry-agent` service account for log and metric collection is no longer necessary. The required permissions are now automatically granted to this service account. You can therefore disregard this section.

In order for GKE on AWS to create and upload system logs and metrics to Google Cloud, it must be authorized.

To authorize the Kubernetes workload identity `gke-system/gke-telemetry-agent` to write logs to Google Cloud Logging, and metrics to Google Cloud Monitoring, run this command:
    
    
    gcloud projects add-iam-policy-binding GOOGLE_PROJECT_ID \
      --member="serviceAccount:GOOGLE_PROJECT_ID.svc.id.goog[gke-system/gke-telemetry-agent]" \
      --role=roles/gkemulticloud.telemetryWriter
    

Replace `GOOGLE_PROJECT_ID` with the cluster's Google Cloud project ID.

This IAM binding grants access for all clusters in the Google Cloud project project to upload logs and metrics. You only need to run it after creating your first cluster for the project.

Adding this IAM binding will fail unless at least one cluster has been created in your Google Cloud project. This is because the workload identity pool it refers to (`GOOGLE_PROJECT_ID.svc.id.goog`) is not provisioned until cluster creation.

## What's next

  * [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool).
  * [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cluster-access-for-kubectl).
  * Try the [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quickstart) to launch your first workload.
  * Read the reference documentation for [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create).
  * Had a problem creating a cluster? See [Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshooting) for more information.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
