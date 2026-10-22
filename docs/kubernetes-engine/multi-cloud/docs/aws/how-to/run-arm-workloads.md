---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/run-arm-workloads/
title: Run Arm workloads in GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:01.577208+00:00
---

# Run Arm workloads in GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/run-arm-workloads/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Run Arm workloads in GKE on AWS Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS lets you run Arm workloads built for Arm-based [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/).

## Limitations

  * Arm node pools running Kubernetes versions earlier than 1.24.8-gke.1300 automatically add a taint during node pool creation to prevent Arm workloads from being scheduled on non-Arm nodes. Arm node pools in clusters at version 1.24.8-gke.1300 or higher no longer add this taint. If you're upgrading from a cluster earlier than 1.24.8-gke.1300, you must create this taint yourself or otherwise take this into account when upgrading.

  * Arm node pools on GKE on AWS don't support Cloud Service Mesh, Config Sync, or Policy Controller. You must run these products on an x86 node pool.

  * Clusters running Kubernetes version 1.24 need an x86 node pool to run the [Connect Agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent). If your cluster runs Kubernetes version 1.25 or later, you don't need an x86 node pool.




This page explains how to create an Arm node pool, why multi-architecture images are the recommended way to deploy Arm workloads, and how to schedule Arm workloads.

### Before you begin

Before you create node pools for your Arm workloads, you need the following resources:

  * An existing AWS cluster to create the node pool in. This cluster must run Kubernetes version 1.24 or later.
  * An [IAM instance profile](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_a_node_pool_iam_role) for the node pool VMs.
  * A [subnet](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-vpc#create_the_node_pool_subnets) where the node pool VMs will run.
  * If your cluster is running Kubernetes version 1.24, an x86 node pool to run the [Connect Agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent).

For details on how to create a node pool in GKE on AWS, see [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool). 




### Create an Arm node pool

GKE on AWS supports node pools built on the Canonical Ubuntu arm64 minimal node image and `containerd` runtime.

To create an Arm node pool and add it to an existing cluster, run the following command:
    
    
    gcloud container aws node-pools create NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --instance-type INSTANCE_TYPE \
        --root-volume-size ROOT_VOLUME_SIZE \
        --iam-instance-profile NODEPOOL_PROFILE \
        --node-version NODE_VERSION \
        --min-nodes MIN_NODES \
        --max-nodes MAX_NODES \
        --max-pods-per-node MAX_PODS_PER_NODE \
        --location GOOGLE_CLOUD_LOCATION \
        --subnet-id NODEPOOL_SUBNET \
        --ssh-ec2-key-pair SSH_KEY_PAIR_NAME \
        --config-encryption-kms-key-arn CONFIG_KMS_KEY_ARN
    

Replace the following:

  * `NODE_POOL_NAME`: the name you choose for your node pool
  * `CLUSTER_NAME`: the name of the cluster to attach the node pool to
  * `INSTANCE_TYPE`: one of the following instance types:

    * `m6g`
    * `m6gd`
    * `t4g`
    * `r6g`
    * `r6gd`
    * `c6g`
    * `c6gd`
    * `c6gn`
    * `x2gd`
    * `c7g`
    * `im4gn`
    * `g5g`

These instance types are powered by Arm-based AWS Graviton processors. You also need to specify the instance size that you want. For example, `m6g.medium`. For a complete list, see [Supported AWS instance types](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-instance-types#supported_instance_types).

  * `ROOT_VOLUME_SIZE`: the desired size for each node's root volume, in Gb

  * `NODEPOOL_PROFILE`: the IAM instance profile for node pool VMs

  * `NODE_VERSION`: the Kubernetes version to install on each node in the node pool, which must be version 1.24 or later. For example, `1.24.3-gke.200`.

  * `MIN_NODES`: the minimum number of nodes the node pool can contain

  * `MAX_NODES`: the maximum number of nodes the node pool can contain

  * `MAX_PODS_PER_NODE`: the maximum number of Pods that can be created on any single node in the pool

  * `GOOGLE_CLOUD_LOCATION`: the name of the Google Cloud

location from which this node pool will be managed

  * `NODEPOOL_SUBNET`: the ID of the subnet the node pool will run on. If this subnet is outside of the VPC's primary CIDR block, you need to take additional steps. For more information, see [security groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups).

  * `SSH_KEY_PAIR_NAME`: the name of the AWS SSH key pair created for SSH access (optional)

  * `CONFIG_KMS_KEY_ARN`: the Amazon Resource Name (ARN) of the AWS KMS key that encrypts user data




## Understand multi-architecture images

Container images must be compatible with the architecture of the node where you intend to run the Arm workloads. To ensure that your container image is Arm-compatible, we recommend that you use multi-architecture ("multi-arch") images.

A multi-arch image is an image that can support multiple architectures. It looks like a single image with a single tag, but contains a set of images to run on different machine architectures. Multi-arch images are compatible with the Docker Image Manifest V2 Scheme 2 or OCI Image Index Specifications.

When you deploy a multi-arch image to a cluster, the container runtime automatically chooses the image that is compatible with the architecture of the node you're deploying to. Once you have a multi-arch image for a workload, you can deploy this workload across multiple architectures. Scheduling a single-architecture image onto an incompatible node causes an error at load time.

To learn more about how to use multi-arch images with Arm workloads, see [Build multi-architecture images for Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm) in the Google Kubernetes Engine (GKE) documentation.

## What's next

  * [Troubleshoot Arm workloads](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshooting#troubleshoot-arm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
