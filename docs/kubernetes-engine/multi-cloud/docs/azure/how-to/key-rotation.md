---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/key-rotation/
title: Rotate your cluster's security keys \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:10.933734+00:00
---

# Rotate your cluster's security keys  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/key-rotation/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Rotate your cluster's security keys

## Key Rotation

Key rotation is the act of changing the underlying cryptographic material contained in a _key encryption key (KEK)_. It can be triggered manually, usually after a security incident where keys might have been compromised. Key rotation replaces only the single field in the key that contains the raw encryption/decryption key data.

To rotate the customer-managed encryption keys, perform the following steps:

  1. [Create a new Azure Key Vault key version](https://docs.microsoft.com/en-us/azure/key-vault/keys/quick-create-cli).

  2. After a key rotation, new Secrets will be encrypted using the new key. Old Secrets will still be decrypted using old keys. The cluster stores key information along with the cipher to aid decryption after key rotation.

Force the cluster to re-encrypt all secrets using the new key:
         
         kubectl get secrets --all-namespaces -o json | \
         kubectl annotate --overwrite -f - encryption-key-rotation-time=`date +"%Y%m%d-%H%M%S"`
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
