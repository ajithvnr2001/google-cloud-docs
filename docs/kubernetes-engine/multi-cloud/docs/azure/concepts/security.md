---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/security/
title: Security overview \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:26.529617+00:00
---

# Security overview  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/security/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security overview

This page describes the security architecture of GKE on Azure , including encryption and node configuration.

GKE clusters offer features to help secure your workloads, including the contents of your container image, the container runtime, the cluster network, and access to the cluster API server.

When you use GKE clusters, you agree to take on certain responsibilities for your clusters. For more information, see [GKE clusters shared responsibilities](https://docs.cloud.google.com/anthos/docs/concepts/gke-shared-responsibility).

## At-rest data Encryption

At-rest data encryption is the encryption of stored data, as distinct from data in transit. By default, GKE on Azure encrypts data in etcd and storage volumes at rest using Azure platform-managed keys.

GKE on Azure clusters store data in Azure Disk volumes. These volumes are always encrypted at rest using Azure Key Vault keys. When you create clusters and node pools, you can provide a Customer-Managed Keyvault Key to encrypt the cluster's underlying Disk volumes. If you don't specify a key, Azure uses the [default Azure-managed key](https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest) within the Azure region where the cluster runs. 

In addition, all GKE clusters enable _Application-layer Secrets Encryption_ for sensitive data, such as Kubernetes [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) objects, which are stored in [etcd](https://kubernetes.io/docs/concepts/overview/components/#etcd). Even if attackers gain access to the underlying volume where etcd data is stored, these data is encrypted.

When you create a cluster, you can provide an Azure Key Vault key in the [`--database-encryption-kms-key-arn`](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--database-encryption-key-id) parameter. This key is used for encryption of your application's data. If you don't provide a key during cluster creation, GKE on Azure creates one for your cluster automatically. This resource field is immutable and cannot be modified once the cluster is created. 

You can also manually create a Key Vault key or bring your own key (BYOK) with a hardware security module (HSM). For more information, see [Bring your own key](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/bring-your-own-key).

### How application level encryption works

Kubernetes offers application-level encryption with a technique known as _envelope encryption_. A local key, commonly called a [data encryption key (DEK)](https://www.techopedia.com/definition/5660/data-encryption-key-dek), is used to encrypt a Secret. The DEK itself is then encrypted with a second key called the [key encryption key (KEK)](https://csrc.nist.gov/glossary/term/key_encryption_key). The KEK is not stored by Kubernetes. When you create a new Kubernetes Secret, your cluster does the following:

  1. The Kubernetes API server generates a unique DEK for the Secret using a random number generator.

  2. The Kubernetes API server encrypts the Secret locally with the DEK.

  3. The Kubernetes API server sends the DEK to Azure Key Vault for encryption.

  4. Azure Key Vault uses a pre-generated KEK to encrypt the DEK and returns the encrypted DEK to the Kubernetes API server's Azure Key Vault plugin.

  5. The Kubernetes API server saves the encrypted Secret and the encrypted DEK to etcd. The plaintext DEK is not saved to disk.

  6. The Kubernetes API server creates an in-memory cache entry to map the encrypted DEK to the plaintext DEK. This lets the API Server decrypt recently-accessed Secrets without querying the Azure Key Vault.




When a client requests a Secret from the Kubernetes API server, here's what happens:

  1. The Kubernetes API server retrieves the encrypted Secret and the encrypted DEK from etcd.

  2. The Kubernetes API server checks the cache for an existing map entry and if found, decrypts the Secret with it.

  3. If there is no matching cache entry, the API server sends the DEK to Azure Key Vault for decryption using the KEK. The decrypted DEK is then used to decrypt the Secret.

  4. Finally, the Kubernetes API server returns the decrypted Secret to the client.




### Config Encryption with Key Vault Firewall

If you pass a public key for encryption, the service principal doesn't need the permission to encrypt, but it does need the permission to manage role assignments. The easiest way to do this is to assign the Azure `User Access Administrator` built-in role to your service principal.

To further secure your Azure Key Vault, you can enable [Azure Key Vault firewall](https://docs.microsoft.com/en-us/azure/key-vault/general/network-security). GKE on Azure can then use a public key for encryption and avoid network access to the key vault.

To configure the firewall, you [download the Key Vault Key with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/keyvault/key?view=azure-cli-latest#az_keyvault_key_download). You pass the key to the [`--config-encryption-public-key`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--config-encryption-public-key) when you create a cluster with the Google Cloud CLI.

You still need to enable service endpoints for Key Vault in all the subnets used for your cluster. For more information, see [Virtual network service endpoints for Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview-vnet-service-endpoints).

## Key Rotation

In contrast to certificate rotation, key rotation is the act of changing the underlying cryptographic material contained in a _key encryption key (KEK)_. It can be triggered automatically as part of a scheduled rotation, or manually, usually after a security incident where keys might have been compromised. Key rotation replaces only the single field in the key that contains the raw encryption/decryption key data.

For more information, see [Key rotation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/key-rotation).

## Cluster trust

All cluster communication uses Transport Layer Security (TLS). Each cluster is provisioned with the following main self-signed root certificate authorities (CAs):

  * The cluster root CA is used to validate requests sent to the API server.
  * The etcd root CA is used to validate requests sent to etcd replicas.



Each cluster has a unique root CA. If one cluster's CA is compromised, no other cluster's CA is affected. All root CAs have a validity period of 30 years.

## Node security

GKE on Azure deploys your workloads onto node pools of Azure VM instances. The following section explains security features of nodes.

### Ubuntu

Your nodes run an optimized version of the [Ubuntu](http://www.ubuntu.com/) OS to run the Kubernetes control plane and nodes. For more information, see [security features](https://wiki.ubuntu.com/Security/Features) in the Ubuntu documentation.

GKE clusters implement several security features, including the following:

  * Optimized [package set](https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64-root.manifest)

  * Google Cloud-tailored [Linux kernel](https://git.launchpad.net/%7Ecanonical-kernel/ubuntu/+source/linux-gcp/+git/bionic/)

  * Limited user accounts and disabled root login




Additional security guides are available for Ubuntu, such as the following:

  * [CIS Benchmark](https://www.cisecurity.org/benchmark/ubuntu_linux/)

  * [DISA STIG](https://public.cyber.mil/stigs/)

  * [FIPS 140-2](https://wiki.ubuntu.com/Security/Certification)




## Secure your workloads

Kubernetes allows users to quickly provision, scale, and update container-based workloads. This section describes tactics that you can use to limit the side-effects of running containers on cluster and Google Cloud services.

### Limit Pod container process privileges

Limiting the privileges of containerized processes is important for your cluster's security. You can set security-related options with a [security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/). These settings let you change the security settings of your processes such as the following:

  * User and group running the process
  * Available Linux capabilities
  * Privilege escalation



The default GKE on Azure node operating system, Ubuntu, uses default [Docker AppArmor security policies](https://docs.cloud.google.com/container-optimized-os/docs/how-to/secure-apparmor#using_the_default_docker_apparmor_security_profile) for all containers. You can view the profile's template on [GitHub](https://github.com/moby/moby/blob/master/profiles/apparmor/template.go). Among other things, this profile denies containers the following abilities:

  * Writing to files directly in a process ID directory (`/proc/`)
  * Writing to files that are not in `/proc/`
  * Writing to files in `/proc/sys` other than `/proc/sys/kernel/shm*`
  * Mounting file systems



### Restrict the ability for workloads to self-modify

Certain Kubernetes workloads, especially system workloads, have permission to self-modify. For example, some workloads vertically autoscale themselves. While convenient, this can allow an attacker who has already compromised a node to escalate further in the cluster. For example, an attacker could have a workload on the node change itself to run as a more privileged service account that exists in the same namespace.

Ideally, workloads should not be granted the permission to modify themselves in the first place. When self-modification is necessary, you can limit permissions by installing [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller) or [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/install/) in your cluster and applying constraints, such as [NoUpdateServiceAccount](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/noupdateserviceaccount) from the open source Gatekeeper library, which provides several useful security policies.

When you deploy policies, it is usually necessary to allow the controllers that manage the cluster lifecycle to bypass the policies. This is necessary so that the controllers can make changes to the cluster, such as applying cluster upgrades. For example, if you deploy the `NoUpdateServiceAccount` policy on GKE on Azure, you must set the following parameters in the `Constraint`:
    
    
    parameters:
      allowedGroups: []
      allowedUsers:
      - service-PROJECT_NUMBER@gcp-sa-gkemulticloud.iam.gserviceaccount.com
    

Replace `PROJECT_NUMBER` with the number (not ID) of the project that hosts the cluster.

### Isolate workloads on dedicated node pools

You can use Kubernetes taints and tolerations to designate specific node pools to run specific types of workloads. For example, you can tell GKE on Azure to schedule user workloads away from most system-managed workloads, or place workloads with different trust levels on different node pools.

Workload isolation using taints and tolerations isn't a guaranteed security measure. Only use this alongside the other hardening measures that GKE on Azure offers.

To learn more, see [Isolate workloads in dedicated node pools](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/isolate-workloads-dedicated-nodes).

## What's next

  * Learn about [Key rotation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/key-rotation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
