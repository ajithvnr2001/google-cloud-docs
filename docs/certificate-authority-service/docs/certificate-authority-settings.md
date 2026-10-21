---
url: https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-settings/
title: Determine certificate authority settings \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:27:19.859799+00:00
---

# Determine certificate authority settings  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Determine certificate authority settings

This page provides information about the various settings of a certificate authority (CA).

## Permanent settings

You cannot change the settings mentioned in this section after creating the CA.

### Service-specific settings

**Type of CA**

CA Service lets you create both root CAs and subordinate CAs.

Root CA | Subordinate CA  
---|---  
A root CA is a self-signed CA. Parties that need to authenticate certificates created from a root CA (a _relying party_) must know its CA certificate in advance. The root CA certificate is often referred to as a _trust anchor_.  
  
Frequently changing a root CA is difficult. To change the root CA, you must first update all relying parties about the new trust anchor. Otherwise, they won't be able to authenticate certificates from the new root CA.  
  
Root CAs cannot be revoked using the CRLs of the issuing CA because root CAs are self-signed. To revoke a root CA, you must remove it from the trust store of every single client that trusts it. This process can be long and tedious. Hence, we recommend protecting the root CAs. | A subordinate CA is a CA that is signed by a root CA or another subordinate CA. Following a chain of subordinate CAs, the chain always ends with a root CA.  
  
A relying party that only knows about a root CA can also implicitly trust a subordinate CA that _chains_ to the explicitly trusted root CA certificate. The subordinate CA can be trusted only if the relying party is able to cryptographically validate the certificate chain that forms a path to the root CA certificate.  
  
A chain containing a root and one or more subordinate CAs can include CAs that are managed in CA Service and CAs that aren't.   
  
**Cloud KMS key**

By default, new CAs use a Google-managed Cloud Key Management Service (Cloud KMS) key. You can choose a specific key algorithm for the Google-managed Cloud KMS key. Alternatively, you can grant CA Service access to a key that already exists. For more information, see [Choose a key algorithm](https://docs.cloud.google.com/certificate-authority-service/docs/choosing-key-algorithm).

For more information about the management models for Cloud KMS keys and Cloud Storage buckets, see [Manage resources](https://docs.cloud.google.com/certificate-authority-service/docs/managed-resources).

**Cloud Storage bucket**

By default, CA Service creates a new Google-managed Cloud Storage bucket in the same location as the CA. You can also choose to use an existing self-managed bucket or [create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). To minimize latency while publishing CRLs, we recommend creating the Cloud Storage bucket in the same location as your CA. For more information, see [Manage resources](https://docs.cloud.google.com/certificate-authority-service/docs/managed-resources).

## CA certificate settings

The following settings are directly reflected in the CA's own certificate:

Setting | Description  
---|---  
Lifetime  | Specifies a CA's lifetime. Lifetime is the amount of time, starting from the CA's creation, that the CA is valid for.  
Subject  | A CA can specify a distinguished name and subject alternative names. In many cases, these fields are purely informational. However, a relying party can choose to treat certificates issued from a CA with particular subject attributes differently.  
  
If you want to specify a subject alternative name for your CA's certificate, you must use the Google Cloud CLI.  
  
## Optional CA settings

The following CA settings are optional. You can change the following setting after creating the CA.

Setting | Description  
---|---  
Label  | A CA can have one or more user labels attached to it. Labels have no semantic meaning to CA Service.  
  
## What's next

  * Learn how to [create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca).
  * Learn how to [create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca).
  * Learn how to [create a subordinate CA from an external CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-sub-ca-from-external-ca).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
