---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority/
title: About GKE control plane authority \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:57.916938+00:00
---

# About GKE control plane authority  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  About GKE control plane authority Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** This document uses a [general availability](https://cloud.google.com/products#product-launch-stages) feature named _GKE control plane authority_ that's only available for eligible Google Cloud customers. To request access to this feature, contact your Google Cloud account team.

This document describes the options that Google Kubernetes Engine (GKE) offers to improve your visibility and control over the security of the managed control plane. These options are collectively referred to as _GKE control plane authority_. This document is intended for information security leaders, compliance administrators, and analysts who want to meet strict privacy and security needs for handling sensitive data.

## About GKE control plane authority features

In GKE, Google Cloud fully manages the security configuration of the control plane, including [encryption of storage at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption), and configuring the keys and certificate authorities (CAs) that sign and verify credentials in your clusters. The control plane nodes for GKE clusters exist in projects that Google Cloud manages. For details about what Google Cloud does, see [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).

GKE control plane authority is an _optional_ set of visibility and control capabilities that let you verify and manage specific aspects of these fully-managed control plane nodes. These capabilities are ideal if you have requirements like the following:

  * You operate in a highly regulated industry like finance, healthcare, or government with specific compliance requirements
  * You handle sensitive data that has strict security and encryption requirements
  * You want enhanced visibility over GKE to improve your confidence when running critical workloads
  * You have to meet specific compliance or auditing requirements related to data encryption, software integrity, or logging
  * You have highly-sensitive workloads that process critical data, and you want visibility into the encryption of and access to that data
  * You want to enforce custom security policies that meet specific organizational or regulatory requirements
  * You want an enhanced level of transparency and visibility into your GKE environments, especially related to actions that Google Cloud takes in the control plane



### Benefits of GKE control plane authority

GKE control plane authority capabilities are ideal in highly regulated environments that have strict security policies or strict audit requirements. Using these capabilities grants benefits like the following:

  * **Enhanced visibility and control** : use additional visibility, control, and encryption capabilities for your GKE control plane.
  * **Streamlined compliance** : meet regulatory and industry requirements with granular audit logs and customizable security policies.
  * **Increased trust and transparency** : gain insights into the actions that Google Cloud takes in the control plane when resolving customer support cases.
  * **Risk mitigation** : proactively detect and respond to potential threats to the managed control plane with comprehensive logs.
  * **Standardized CA and key management** : manage your GKE cluster CAs using Certificate Authority Service, letting you delegate certificate management to specific teams and letting you comprehensively enforce CA policies. Additionally, manage your control plane disk encryption keys using Cloud KMS for similar management delegation.



### Availability of GKE control plane authority

GKE control plane authority is available in any Google Cloud region. However, to encrypt your control plane boot disks and etcd disks with your own keys, you must create the cluster in one of the following regions:

  * `asia-east1`
  * `asia-northeast1`
  * `asia-southeast1`
  * `europe-west1`
  * `europe-west4`
  * `us-central1`
  * `us-central2`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west3`
  * `us-west4`

**Note:** Separately from GKE control plane authority, you can use [Confidential mode for Hyperdisk Balanced for your node disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes). If you plan to use Confidential mode for Hyperdisk Balanced for your nodes in addition to encrypting your control plane disks with your own keys, you must create the cluster in a [region that supports Confidential mode for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/disk-encryption#conf_hdb_regions). If you create the cluster in a different region, you won't be able to use Confidential mode for Hyperdisk Balanced for your nodes.

## How GKE control plane authority works

The capabilities that you can use with the control plane are categorized based on the type of control that you want, as follows. You can use one or more of these capabilities based on your specific requirements.

  * **Key and credential management** : control the keys that GKE uses to encrypt data at rest in the control plane and to issue and verify identities in the cluster.
  * **Access logs and identity issuance logs** : use logs from the network, VM, and Access Transparency to verify GKE control plane access using multiple sources. Use identity issuance logs in Cloud KMS and CA Service to see when identities are created using keys and CAs that you manage. Use detailed Kubernetes API usage logs to track what those identities do in the cluster.



## Key and credential management

By default, Google Cloud manages the keys and CAs in your GKE clusters for you. You can optionally use [Cloud KMS](https://docs.cloud.google.com/kms/docs/key-management-service) and [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) to set up your own keys and CAs, which you then use when creating a new cluster.

GKE uses these keys and CAs instead of the Google Cloud defaults to issue and verify identities in your cluster and to encrypt data in your control plane VMs. Maintaining control over your identity issuance and data encryption keys can help you to do the following:

  * Comply with data sovereignty and privacy regulations that mandate exclusive control over keys
  * Control the encryption of critical sensitive data in Kubernetes by managing your own encryption keys
  * Customize your data encryption strategy based on your organization's policies and requirements, like requirements to use hardware-backed keys.



### Self-managed CAs and service account keys

You can configure the GKE control plane to use Cloud KMS keys and CA Service CAs that you manage. GKE uses these resources to issue and verify identities in your cluster. For example, GKE uses CAs and keys to issue [Kubernetes client certificates](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#x509-client-certificates) and [Kubernetes service account bearer tokens](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens).

You create the following resources for GKE to use when issuing identities:

  1. **Service Account signing keys** : sign the Kubernetes ServiceAccount bearer tokens for service accounts in the cluster. These bearer tokens are JSON Web Tokens (JWTs) that facilitate Pod communication with the Kubernetes API server.
  2. **Service Account verification keys** : verify the Kubernetes Service Account JWTs. This key is normally the same as the signing key, but is configured separately so that you can rotate your keys more safely.
  3. **Cluster CA** : issue signed certificates for purposes like certificate signing requests (CSRs) and kubelet communication.
  4. **etcd peer CA** : Issue signed certificates for communication between etcd instances in the cluster.
  5. **etcd API CA** : issue signed certificates for communication with the etcd API server.
  6. **Aggregation CA** : issue signed certificates for enabling communication between the Kubernetes API server and extension servers.



When GKE issues identities in the cluster, you see the corresponding audit logs in Cloud Logging, which you can use to track issued identities over their lifetime.

To learn more, see [Run your own certificate authorities and signing keys in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys).

### Control plane boot disk and etcd encryption

By default, GKE encrypts the boot disk of a control plane VM. If the control plane runs etcd database instances, GKE also encrypts the following:

  * The disk that stores etcd data.
  * The Google Cloud internal operational backup of etcd.



This default encryption uses encryption keys that Google Cloud manages. For details about this default encryption, see [Default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

You can _optionally_ use your own encryption keys that you manage using Cloud KMS to encrypt the following resources:

  * **Control plane boot disk** : the Compute Engine disk that each control plane VM uses to boot.
  * **etcd disk** : the Compute Engine disk that's attached to each control plane VM and stores data for etcd instances in the cluster.
  * **etcd internal operational backup** : the internal Google Cloud backup of etcd that's used for operational purposes like disaster recovery.

This backup is an emergency measure internal to Google Cloud. If you want to back up and restore your clusters, use [backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) instead.




For instructions, see [Encrypt etcd and control plane boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypt-etcd-control-plane-disks).

This additional optional encryption is ideal if you have to meet specific regulatory or compliance requirements related to controlling the means of encryption in your cluster control plane. You can separately use your own keys to encrypt the boot disks and storage disks of _worker nodes_ in your cluster. For details, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek).

When you use GKE control plane authority to encrypt your control plane boot disks, GKE control plane VMs automatically use Confidential mode for Hyperdisk Balanced in the boot disks. This configuration doesn't change the default boot disks of your worker nodes.

### Rotation of customer-managed credentials

With GKE control plane authority, you can configure clusters to use customer-managed CAs and keys instead of the Google-managed resources that GKE uses by default. A _credential rotation_ is an operation that you perform to refresh one or more of these resources in a cluster. You might perform a credential rotation for reasons like avoiding CA expiry or complying with your organization's credential management requirements.

To perform a credential rotation for a cluster that uses GKE control plane authority, you create new CAs, signing keys, and encryption keys. You then update your cluster to use those new resources.

For more information, see the following pages:

  * [Rotate customer-managed control plane CAs and keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-control-plane-cas-keys).
  * [Rotate etcd and control plane boot disk encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-etcd-kcp-encryption-keys).



## Access logs and identity issuance logs

You can view logs in Logging for all events related to access and identity in the control plane, including the following events:

  * **Direct access** : logs related to direct access attempts (like SSH) to GKE control plane nodes let you verify that the VM SSH logs and VM network connections match the SSH records in Access Transparency logs.
  * **Identity issuance and verification** : logs related to identities that were issued using CAs and keys that you manage in CA Service and Cloud KMS.
  * **Identity usage in Kubernetes** : logs related to the actions that specific identities take against the Kubernetes API server.
  * **Access Transparency** : logs related to connections made to the control plane and actions taken on the control plane by Google Cloud personnel. When Augmented Access Approval is enabled, you get enhanced granularity for access control, including SSH command details within Access Transparency logs and for Access Approval requests. For more information about eligibility and enrollment, contact your Google Cloud account team. 



These logs can help you to do the following:

  * Maintain comprehensive audit trails of all control plane access and identity events for compliance and security.
  * In addition to the built-in Google protections, you can build your own monitoring to identify and investigate any suspicious activity within the control plane.
  * Verify that only authorized entities access and interact with your GKE cluster, which improves your security posture.
  * See when identities are created using keys and CAs that you manage by using identity issuance logs in Cloud KMS and CA Service. Use detailed Kubernetes API usage logs to track what those identities do in the cluster.



The following documents show you how to view and process the various types of control plane logs:

  * [Verify credential issuance and verification operations in GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-identity-issuance-usage)
  * [Verify connections by Google personnel in the cluster control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-google-connections-control-plane)



## Additional resources about control plane security

This section describes other methods that you can use to improve your confidence in your control plane security. You don't need to use GKE control plane authority to use the following resources:

  * **Control plane VM image integrity** : GKE adds detailed logs for node VM creation and boot events to Cloud Logging. Additionally, we [publish SLSA VSAs on GitHub](http://github.com/GoogleCloudPlatform/gke-vsa) that correspond to control plane and worker node machine images. You can verify that your VMs use OS images that have corresponding VSAs and verify the boot integrity of each control plane VM.

To perform VM integrity verification, see [Verify GKE control plane VM integrity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-control-plane-vm-integrity).

  * **Built-in control plane security measures** : GKE performs various hardening measures on the managed control plane. To learn more, see [Control plane security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/control-plane-security).




## What's next

  * [Run your own certificate authorities and signing keys in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys)
  * [Encrypt GKE control plane data at rest with your keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypt-etcd-control-plane-disks)
  * [Verify GKE control plane VM integrity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-control-plane-vm-integrity)
  * [Verify credential issuance and usage in GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-identity-issuance-usage)
  * [Verify connections by Google personnel in the cluster control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-google-connections-control-plane)
  * Learn about [Augmented Administrative Access](https://docs.cloud.google.com/assured-workloads/access-approval/docs/augmented/augmented-access-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
