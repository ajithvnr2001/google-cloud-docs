---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/key-rotation/
title: Rotate your cluster's security keys \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:20.507615+00:00
---

# Rotate your cluster's security keys  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/key-rotation/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Rotate your cluster's security keys Stay organized with collections  Save and categorize content based on your preferences. 

## Key Rotation

Key rotation is the act of changing the underlying cryptographic material contained in a _key encryption key (KEK)_. It can be triggered automatically as part of a scheduled rotation, or manually, usually after a security incident where keys might have been compromised. Key rotation replaces only the single field in the key that contains the raw encryption/decryption key data.

### Automatic Key Rotation

The AWS Key Management Service (KMS) supports [automatic rotation of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html). When enabled, AWS automatically generates new cryptographic key material for your key once a year. No manual actions are required.

After a key rotation, GKE on AWS encrypts each new Secret with the new key. Any previously-created Secret is still decrypted with its original key. For this reason, AWS keeps CMK's older key material in perpetuity, allowing old DEKs to be decrypted when old Secrets are read.

You can see whether a KMS key has automatic rotation enabled or not with the following command:
    
    
    aws kms get-key-rotation --key-id KMS_KEY_ID
    

Replace `KMS_KEY_ID` with your AWS KMS key ID.

You can enable automatic key rotation by running this command:
    
    
    aws kms enable-key-rotation --key-id KMS_KEY_ID
    

### Manual Key Rotation

This section explains how to manually rotate your control plane or node pool configuration keys.

### Control plane configuration key

To manually rotate your [control plane configuration](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--config-encryption-kms-key-arn) key, perform the following steps:

  1. [Create a new Cloud Key Management Service key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html). Save the value of your KMS key ARN. You'll use it later.

  2. Ensure the IAM role associated with the cluster has permissions to encrypt and decrypt using the new key.

  3. Use the [`gcloud container aws clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update) command to update the encryption key.
         
         gcloud container aws clusters update CLUSTER_NAME \
             --location=GOOGLE_CLOUD_LOCATION \
             --config-encryption-kms-key-arn=CONFIG_ENCRYPTION_KMS_KEY_ARN
         

Replace the following:

     * `CLUSTER_NAME`: your cluster's name
     * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster—for example, `us-west1`
     * `CONFIG_ENCRYPTION_KMS_KEY_ARN`: your new KMS key ARN



### Control plane root volume

To manually rotate your [control plane root volume](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--root-volume-kms-key-arn) key, perform the following steps:

  1. [Create a new Cloud Key Management Service key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html). Save the value of your KMS key ARN. You'll use it later.

  2. Ensure the IAM role associated with the cluster has permissions to encrypt and decrypt using the new key.

  3. Use the [`gcloud container aws clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/update) command to update the encryption key.
         
         gcloud container aws clusters update CLUSTER_NAME \
             --location=GOOGLE_CLOUD_LOCATION \
             --root-volume-kms-key-arn=ROOT_VOLUME_KMS_KEY_ARN
         

Replace the following:

     * `CLUSTER_NAME`: your cluster's name
     * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster—for example, `us-west1`
     * `ROOT_VOLUME_KMS_KEY_ARN`: Amazon Resource Name (ARN) of the AWS KMS key to encrypt the root volume



### Node pool configuration key

To manually rotate your [Node pool configuration](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--config-encryption-kms-key-arn) key, perform the following steps:

  1. [Create a new Cloud Key Management Service key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).

  2. Ensure the IAM role associated with the cluster has permissions to encrypt and decrypt using the new key.

  3. Update the KMS alias in use:
         
         aws kms update-alias --alias-name KEY_ALIAS \
              --target-key-id CONFIG_ENCRYPTION_KMS_KEY_ARN
         

Replace the following:

     * `KEY_ALIAS`: your existing key's alias
     * `CONFIG_ENCRYPTION_KMS_KEY_ARN`: your new KMS key ARN
  4. Force the cluster to re-encrypt all cluster Secrets using the new encryption key:
         
         kubectl get secrets --all-namespaces -o json | \
          kubectl annotate --overwrite -f - encryption-key-rotation-time=`date +"%Y%m%d-%H%M%S"`
         

  5. Disable the old AWS KMS key. For more information, see [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html).




### Node pool root volumes

To manually rotate your [Node pool root volume](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/create#--root-volume-kms-key-arn) key, perform the following steps:

  1. [Create a new Cloud Key Management Service key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).

  2. Ensure the IAM role associated with the cluster has permissions to encrypt and decrypt using the new key.

  3. Update the KMS alias in use:
         
         aws kms update-alias --alias-name KEY_ALIAS \
              --target-key-id ROOT_VOLUME_KMS_KEY_ARN
         

Replace the following:

     * `KEY_ALIAS`: your existing key's alias
     * `ROOT_ENCRYPTION_KMS_KEY_ARN`: your new KMS key ARN
  4. Update your node pool:
         
         gcloud container aws node-pools update NODE_POOL_NAME \
              --root-volume-kms-key-arn=ROOT_VOLUME_KMS_KEY_ARN
         

Replace the following:

     * `NODE_POOL_NAME`: name of your node pool
     * `ROOT_VOLUME_KMS_KEY_ARN`: Amazon Resource Name (ARN) of the AWS KMS key to encrypt the root volume
  5. Disable the old AWS KMS key. For more information, see [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
