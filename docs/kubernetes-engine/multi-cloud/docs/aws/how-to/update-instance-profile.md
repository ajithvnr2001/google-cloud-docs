---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-instance-profile/
title: Update AWS IAM instance profile \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:57.492399+00:00
---

# Update AWS IAM instance profile  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-instance-profile/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Update AWS IAM instance profile Stay organized with collections  Save and categorize content based on your preferences. 

This page explains what an AWS IAM instance profile is, why it's important in the context of GKE on AWS, and how to update the instance profile.

## What is an AWS IAM instance profile?

An instance profile is an AWS-specific concept. It consists of a set of credentials that an Amazon EC2 instance uses to access various AWS resources. More specifically, an instance profile is a kind of container for an IAM role that can be attached to an EC2 instance. An instance profile confers permissions to the EC2 instance, allowing the instance to interact with various AWS services under the defined permissions. For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html).

## How are instance profiles used in GKE on AWS?

Each control plane and each node pool within a GKE on AWS cluster is associated with a unique AWS instance profile. Instance profiles in GKE on AWS serve a dual purpose:

  1. An instance profile grants GKE on AWS the permissions needed to manage AWS resources. For example, they give the cluster autoscaler the necessary permissions to scale the cluster by adding or removing EC2 instances based on workload demands.
  2. An instance profile grants EC2 instances access to Google Cloud services. For example the `kubelet`, running on an AWS machine, requires specific permissions to supply image pull credentials to `containerd`. These credentials are necessary for accessing and pulling images from Google's private Artifact Registry or from Container Registry. In the context of GKE on AWS, the EC2 instance profile associated with the cluster is configured to impersonate Google's Machine Service Agents (such as the Node Pool Machine Service Agent or the Control Plane Machine Service Agent). This impersonation allows the cluster's EC2 instances to automatically authenticate with Google's Artifact Registry or Container Registry.



## Update instance profile

Updating the instance profile involves creating a new instance profile in AWS with specific permissions, and then associating it with your GKE on AWS cluster or node pool.

To correctly update the instance profile for your cluster or node pool, follow these steps:

  1. Create an IAM instance profile for your Amazon EC2 instances and add the IAM role you need to the instance profile. For details, see [Using instance profiles](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-iam-instance-profile.html).
  2. Link the new instance profile to your GKE on AWS cluster or node pool by running the following command in your Google Cloud CLI:

###  Link profile to cluster 
         
         gcloud container aws clusters update CLUSTER_NAME \
           --update-instance-profile \
           --instance-profile-name NEW_INSTANCE_PROFILE_NAME \
           ...
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster
     * `NEW_INSTANCE_PROFILE_NAME`: the name of the new AWS instance profile you created

###  Link profile to node pool 
    
    gcloud container aws node-pools update NODE_POOL_NAME \
      --update-instance-profile \
      --instance-profile-name NEW_INSTANCE_PROFILE_NAME \
      ...
    

Replace the following:

     * `NODE_POOL_NAME`: the name of your node pool
     * `NEW_INSTANCE_PROFILE_NAME`: the name of the new AWS instance profile you created

These commands show only the relevant flags for updating the instance profile, but you need to provide additional flags in order to run the `update` command. For details, see [Update your AWS cluster parameters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-cluster) or [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool).




### The incorrect update method

Understanding the wrong way to update an instance profile is important, because it's an easy mistake to make that can cause cluster failures.

The wrong way to update an instance profile is to directly modify an existing instance profile using the AWS Management Console or AWS CLI. Such changes can disrupt GKE on AWS interaction with AWS resources. GKE on AWS expects instance profiles to remain as they were when first linked to the cluster or node pool. Altering them outside of GKE on AWS's management tools can create a mismatch with the ID of the IAM role that's in the instance profile. This mismatch can create a cluster failure.

The approach described in the preceding section ensures that updates are made without disrupting GKE on AWS's integration with AWS.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
