---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/bring-your-own-key/
title: Bring your own key from a hardware security module \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:00:36.295951+00:00
---

# Bring your own key from a hardware security module  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/bring-your-own-key/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bring your own key from a hardware security module

This topic explains how you can use your own Azure Key Vault hardware security module (HSM) key for at-rest encryption on GKE on Azure.

## Before you begin

Before performing these steps, ensure that you're familiar with the [Security](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/security) architecture of GKE on Azure.

To perform these steps, you must have the following:

  * An [Azure-supported HSM](https://docs.microsoft.com/en-us/azure/key-vault/keys/hsm-protected-keys#supported-hsms)

  * An Azure Key Vault with the [Azure role-based access control](https://docs.microsoft.com/en-us/azure/key-vault/general/rbac-guide) permission model.

  * An [HSM-protected key imported into Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/keys/hsm-protected-keys-byok)

  * Your GKE on Azure [service principal](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application) with permissions to manage the Azure Key Vault authorization and encrypt data with the provided key.

The easiest way to grant these permissions is to assign the `Key Vault Crypto Officer` and `User Access Administrator` [Azure built-in roles](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) to the service principal.




### Bring your own key

To bring your own key, perform the following steps:

  1. Save your Azure Key Vault key ID into an environment variable.
         
         export KEY_VAULT_ID="$(az keyvault show --name ${KEY_VAULT_NAME} \
             --resource-group ${RESOURCE_GROUP} --query id -otsv)"
         export KEY_VAULT_KEY_ID="${KEY_VAULT_ID}/keys/${KEY_NAME}"
         

  2. Pass the key's IDs in the [`--config-encryption-key-id`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--config-encryption-key-id) parameter when you [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster).
         
         gcloud container azure clusters create CLUSTER_NAME \
             --config-encryption-key-id  ${KEY_VAULT_KEY_ID} \
             ...
         

  3. Continue with the steps in [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster).




## What's next

See [About keys](https://docs.microsoft.com/azure/key-vault/keys/about-keys) in the Azure documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
