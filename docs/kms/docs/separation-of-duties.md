---
url: https://docs.cloud.google.com/kms/docs/separation-of-duties/
title: Separation of duties \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:42.193803+00:00
---

# Separation of duties  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/separation-of-duties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Separation of duties Stay organized with collections  Save and categorize content based on your preferences. 

_Separation of duties_ is the concept of ensuring that one principal does not have all necessary permissions required to complete a malicious action. In Cloud Key Management Service, this could be an action such as using a key to access and decrypt data which that user has no valid reason to access.

Separation of duties is a business control typically used in larger organizations, meant to help avoid security or privacy incidents and errors. It is considered a best practice.

In Cloud KMS, separation of duties requires a strict distinction between the following roles:

  * **Key managers** : Principals who are authorized to manage key lifecycles including creation, deletion, rotation, and state changes—for example, users with the **Cloud KMS Admin** role.
  * **Key users** : Principals who are authorized to use keys including encryption, decryption, signing, or signature verification—for example, users with the **Cloud KMS CryptoKey Encrypter/Decrypter** role.



When you use Cloud KMS keys for customer-managed encryption keys, we recommend that the service account is the only principal authorized to use the key for encryption and decryption. For more information about how CMEK integrations handle resource access, see [CMEK-integrated services handle resource access](https://docs.cloud.google.com/kms/docs/cmek#cmek-access).

If you want to create a guardrail to enforce this recommendation, you can use [ IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-access) to remove encryption and decryption permissions from principals other than service accounts. For more information about how to use IAM roles safely, see [Use IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely).

## Key governance

Key governance describes who in an organization is responsible for managing the lifecycle of your Cloud KMS resources and maintaining guardrails to control how Cloud KMS is used. Key governance approaches exist on a spectrum from _centralized governance_ to _delegated governance_ :

  * **Centralized governance** : A dedicated security or platform team is responsible for managing the lifecycle of all cryptographic keys across the organization. This model is often chosen by highly regulated enterprises with strict compliance requirements.
  * **Delegated governance** : A central security team uses guardrails to mandate encryption standards, but delegates the responsibility for key lifecycle operations to application owners within their projects. These guardrails can include organization policies using managed constraints and custom constraints and IAM grants and deny policies. This eliminates central operational bottlenecks.



## Key storage

Key storage describes where Cloud KMS resources are created within an organization. There are two main approaches to key storage: dedicated-project key storage and same-project key storage.

  * **Dedicated-project key storage** : A dedicated key project contains keys used for multiple applications. Usually, each environment folder has its own key project. You can use Autokey with dedicated-project key storage. 

  * **Same-project key storage** : Keys are stored in the same Google Cloud project as the resources that they protect. This is sometimes described as "the key follows the data." You can use Autokey with same-project key storage. 




## Align governance and storage

The following matrix provides examples of how these governance and storage models can be combined to meet different organization needs:

Governance Model | Dedicated-project key storage | Same-project key storage  
---|---|---  
Centralized governance | Fully centralized approach **Recommended use** : Organizations with strict regulatory requirements that mandate project boundary isolation. **Operational impact** : High setup complexity. Requires robust automation (such as a "project factory") to prevent operational delays for development teams. | Governed ownership **Recommended use** : Organizations that require central security oversight but want to maximize developer velocity. **Operational impact** : Low setup complexity. Central security enforces policy by using guardrails, while keys are co-located with the resources that they protect for ease of management.  
Delegated governance | **Not recommended** Introducing cross-project IAM complexity defeats the purpose of delegating key management to application teams. | Autonomous DevOps **Recommended use** : High-velocity, decentralized organizations with a strong DevOps culture. **Operational impact** : Minimal setup complexity. Application teams have full autonomy over both resources and keys within their project boundaries.  
  
### Same-project key storage

Enforcing separation of duties in same-project key management requires keeping IAM roles strictly separated. For example, you can use [ IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-access) to remove encryption and decryption permissions from your key managers.

You can enable Autokey with same-project key storage on a project or folder to allow automated key creation in the same project as the resource the key protects. For more information, see [Enable Autokey with same-project key storage](https://docs.cloud.google.com/kms/docs/enable-autokey#same-project).

### Dedicated-project key storage

In the dedicated-project key storage model, dedicated key projects are managed by a central security team, who have key administration permissions in the key project but are restricted from accessing projects that contain the resources protected by those keys.

You can enable Autokey with dedicated-project key storage on a folder to allow automated key creation using the centralized key storage model. For more information, see [Set up Autokey with dedicated-project key storage](https://docs.cloud.google.com/kms/docs/enable-autokey#dedicated-project).

## Automating and monitoring compliance

Google Cloud provides the following tools to automate and monitor your security boundaries:

  * **Cloud KMS Autokey** : Autokey supports both dedicated-project key storage and same-project key storage. For both, it automates separation of duties by automatically granting the key usage role to the required service agent—not to the person requesting the key. Autokey is designed to support infrastructure-as-code pipelines that don't need elevated privileges for key creation.
  * **Security Command Center** : Monitor for **KMS Role Separation** findings to detect any principal, including a Project Owner or a Google service account, that possesses both administrative and cryptographic permissions on a single key.
  * **CMEK encryption metrics** : Use the **Encryption metrics** dashboard to verify alignment with separation of duties practices across the organization.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
