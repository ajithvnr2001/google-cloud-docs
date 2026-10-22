---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotate-ksa-signing-key/
title: Rotate KSA signing keys \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:53.231877+00:00
---

# Rotate KSA signing keys  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotate-ksa-signing-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Rotate KSA signing keys Stay organized with collections  Save and categorize content based on your preferences. 

A [Kubernetes service account (KSA)](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/) provides an identity for processes that run in a Pod.

Kubernetes service accounts are different from the [Google Cloud service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) that applications use to make authorized calls to Google Cloud APIs.

Google Distributed Cloud uses a private cryptographic key to sign the KSA tokens that it issues to Pods. It uses the corresponding public key to validate the tokens when Pods send requests to the Kubernetes API server. When a Pod uses [Workload Identity](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) to call Google Cloud APIs, Google Cloud uses the same public key to authenticate the Pod's identity.

During user cluster creation, Google Distributed Cloud generates the private and public keys. Also during cluster creation, Google Distributed Cloud [registers the cluster to a fleet](https://docs.cloud.google.com/anthos/fleet-management/docs) and provides the public key to Google Cloud.

At a later time, you can rotate the private/public key pair. The rotation automatically issues new tokens signed by the new private key. At the end of the rotation, the cluster has a new private key, a new public key, and refreshed tokens. Also, Google Cloud has the new public key.

## Bound tokens and legacy tokens

A Pod can use either a [legacy token or a bound token](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-bound-service-account-tokens) for authentication and authorization when it calls the Kubernetes API server. Bound tokens have a limited lifetime and are distributed to Pods using [projected volumes](https://kubernetes.io/docs/concepts/storage/projected-volumes/#serviceaccounttoken). Legacy tokens never expire and are held in Kubernetes [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/). We recommend bound tokens because they are more secure.

Both bound tokens and legacy tokens are refreshed during a key rotation.

**Important:** If you are using third-party tokens, they are not automatically refreshed during a rotation. To generate new third-party tokens, you will need to restart the Pods using these tokens.

## Limitations

  * If you created the cluster with [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) set to `true` (which is required for [setting up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), key rotation isn't supported.



## Start a key rotation

Before you start a key rotation, consider these points:

  * During a key rotation, you cannot start another key rotation, certificate authority rotation, or cluster update.

  * Key rotation cannot be paused or rolled back. All old keys are deleted.

  * A key rotation deletes existing cluster nodes and creates new nodes.




To start a key rotation:
    
    
    gkectl update credentials ksa-signing-key rotate \
        --config USER_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONIFG \
        [--skip-prompt]
    

Replace the following:

  * USER_CLUSTER_CONFIG: The path of the user cluster configuration file

  * ADMIN_KUBECONFIG_FILE: The path of the admin cluster kubeconfig file




Include `--skip-prompt` if you do not want to be prompted.

## View the status of a key rotation

To view the status of a key rotation:
    
    
    gkectl update credentials ksa-signing-key status \
        --config USER_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONIFG
    

If the key rotation has already completed, you will see a message similar to this:
    
    
    State of KSASigningKeyRotation with KSASigningKeyVersion 2 is -
    status: True,
    reason: KSASigningKeyRotationCompleted,
    message:{"tokenVersion":2,"privateKeyVersion":2,"publicKeyVersions":[2]}
    

If the KSA Signing Key rotation rotation is still in progress, you will see a message similar to this:
    
    
    State of KSASigningKeyRotation with KSASigningKeyVersion 2 is -
    status: False,
    reason: KSASigningKeyRotationProcessedReason,
    message:{"tokenVersion":2,"privateKeyVersion":2,"publicKeyVersions":[1,2]}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
