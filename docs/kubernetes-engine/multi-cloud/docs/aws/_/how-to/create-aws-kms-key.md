---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws//how-to/create-aws-kms-key/
title: Create an AWS KMS key \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:41:27.278540+00:00
---

# Create an AWS KMS key  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws//how-to/create-aws-kms-key/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Create an AWS KMS key Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

GKE on AWS uses customer-managed [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) (KMS) symmetric keys to encrypt:

  * Kubernetes state data in [etcd](https://kubernetes.io/docs/concepts/overview/components/#etcd)
  * EC2 instance [user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
  * EBS volumes for [at-rest encryption](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/security#at-rest_data_encryption) of control plane and node pool data



For production environments, we recommend using different keys for configuration and volume encryption. To further minimize risks if a key is compromised, you can also create different keys for each of the following:

  * Cluster control plane [configuration](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--config-encryption-kms-key-arn)
  * Cluster control plane [database](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--database-encryption-kms-key-arn)
  * Cluster control plane [main volume](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--main-volume-kms-key-arn)
  * Cluster control plane [root volume](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--root-volume-kms-key-arn)
  * Node pool [configuration](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--config-encryption-kms-key-arn)
  * Node pool [root volume](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--root-volume-kms-key-arn)



For additional security, you can create an AWS KMS key policy that assigns only the minimum required set of permissions. For more information, see [Creating KMS keys with specific permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-kms-key#specific-permissions).

## Create an AWS KMS key

To create a key, run the following command:
    
    
    aws --region AWS_REGION kms create-key \
        --description "KEY_DESC"
    

Replace the following:

  * `AWS_REGION` with the name of your AWS region
  * `KEY_DESC` with a text description of your key



For each key you create, save the value named `KeyMetadata.Arn` in the output of this command for later use.

## Creating KMS keys with specific permissions

If you create separate keys for different functions, you need to provide a [KMS key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) for each key that grants appropriate permissions on that key. If you don't specify a key policy when you create a key, AWS KMS will create a default key policy that gives all [principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) in the owning account unlimited access to all operations for the key.

When you create a key policy, you must allow an AWS IAM policy access to the key policy. The key policy must also give your account permissions to use IAM policies. Without permission from the key policy, IAM policies that allow permissions have no effect. For more information, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html).

The following table describes the permissions for each of the [AWS IAM roles](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/aws-iam-roles) GKE on AWS uses.

| GKE Multi-Cloud API service agent role | Control plane role | Node pool role | AWS Service Role For AutoScaling  
---|---|---|---|---  
Cluster control plane configuration encryption | kms:Encrypt | kms:Decrypt | N/A | N/A  
Cluster control plane database encryption | N/A | [kms:Encrypt](https://github.com/kubernetes-sigs/aws-encryption-provider#permissions)  
[kms:Decrypt](https://github.com/kubernetes-sigs/aws-encryption-provider#permissions) | N/A | N/A  
Cluster control plane main volume encryption | kms:GenerateDataKeyWithoutPlaintext | kms:CreateGrant | N/A | N/A  
Cluster control plane root volume encryption | N/A | N/A | N/A | See [Key policy sections that allow access to the customer managed key](https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html#policy-example-cmk-access)  
Node pool configuration encryption | kms:Encrypt | N/A | kms:Decrypt | N/A  
Node pool root volume encryption | N/A | N/A | N/A | See [Key policy sections that allow access to the customer managed key](https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html#policy-example-cmk-access)  
Other requirements | kms:DescribeKey | N/A | N/A | N/A  
  
## What's next

  * [Create an SSH key pair](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-ssh-keypair).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
