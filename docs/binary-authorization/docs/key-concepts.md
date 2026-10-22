---
url: https://docs.cloud.google.com/binary-authorization/docs/key-concepts/
title: Binary Authorization concepts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:37.727568+00:00
---

# Binary Authorization concepts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/key-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Binary Authorization concepts Stay organized with collections  Save and categorize content based on your preferences. 

This page contains information about concepts related to Binary Authorization.

## Policies

A Binary Authorization _policy_ , also known as a _project-singleton policy_ , is a set of rules that govern the deployment of container images.

[Continuous validation (CV)](https://docs.cloud.google.com/binary-authorization/docs/overview-cv), uses a different type of policy, called a [platform policy](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#platform-policies).

A policy has the following parts:

  * Deployment rules
  * List of exempt images



You can configure a policy using one of the following:

  * Google Cloud console
  * `gcloud` commands



When you use `gcloud` commands, you export and modify a definition of the policy in YAML format before importing it back to your project. The YAML format reflects the internal structure of a policy in Binary Authorization storage. For more information about this format, see [Policy YAML Reference](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference).

Each Google Cloud project can have exactly one policy. You must configure the policy in the project where you run your deployment platform. In a _single-project configuration_ , the policy and all subordinate resources—attestors and attestations—reside in the same project. To establish [separation of duties](https://docs.cloud.google.com/binary-authorization/docs/reference/organizational-and-iam-roles), you can use a _multi-project configuration_. In this configuration, the deployment platform can run in one project, attestors can reside in another project, and attestations can reside in still another project.

To set up and use Binary Authorization on supported platforms, see [Set up by platform](https://docs.cloud.google.com/binary-authorization/docs/set-up-platform).

See an example [multi-project setup for GKE](https://docs.cloud.google.com/binary-authorization/docs/multi-project-setup-cli).

## Rules

When you configure a policy, you define its rules. Rules define constraints that images must satisfy before they can be deployed. A policy has one default rule and it can have specific rules, depending on the platform. For more information, see Supported rule types by platform.

Each rule can be configured with an evaluation mode and an enforcement mode, for example, a rule can require that an image have a signed attestation before it can be deployed.

### Default rule

Each policy has a _default rule_. This rule applies to any deployment request that doesn't match a specific rule. In a policy YAML file, the default rule is specified in the [`defaultAdmissionRule`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#defaultadmissionrule) node.

For more information about configuring the default rule, see [Configuring a policy](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#default-rule).

### Specific rules

One or more _specific rules_ can be added to a policy. This type of rule applies to images that are to be deployed to specific clusters, service account, or identity. Support for specific rules varies by platform. For more information, see Supported rule types by platform.

In a policy YAML file, each cluster-specific rule is specified in a [`clusterAdmissionRule`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#clusteradmissionrules) node.

### Supported rule types by platform

The following table shows which rule types are supported for each deployment platform.

Platform | Default rule | Specific rule  
---|---|---  
GKE | Supported | Clusters  
Kubernetes Namespaces  
Kubernetes Service Accounts  
Cloud Run | Supported | Not supported  
GKE attached clusters | Supported | Clusters  
Kubernetes Namespaces  
Kubernetes Service Accounts  
GKE on AWS | Supported | Clusters  
Kubernetes Namespaces  
Kubernetes Service Accounts  
Google Distributed Cloud | Supported | Clusters  
Kubernetes Namespaces  
Kubernetes Service Accounts  
Google Distributed Cloud | Supported | Clusters  
Kubernetes Namespaces  
Kubernetes Service Accounts  
Cloud Service Mesh | Supported | Cloud Service Mesh Service Identities  
  
### Evaluation modes

Each rule has an _evaluation mode_ that specifies the type of constraint that Binary Authorization enforces for the rule. The evaluation mode for a rule is specified using the [`evaluationMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) property in the policy YAML file.

There are three evaluation modes:

  * **Allow all images:** allows all images to be deployed.
  * **Disallow all images:** disallows all images from being deployed.
  * **Require attestations:** requires a signer to digitally sign the image digest and create an attestation before deployment. At deploy time, the Binary Authorization enforcer uses an attestor to verify the signature in the attestation before deploying the associated image.



### Enforcement modes

Each rule also has an _enforcement mode_ , which specifies the action that is taken by GKE when an image does not conform to the rule. A rule can have the following enforcement modes:

  * **Block and Audit Log** : Blocks the deployment of images that do not conform to the rule and writes a message to the audit log to indicate why the image was not deployed.

  * **Dry Run: Audit Log Only** : Dry run mode is an enforcement mode in a policy that allows non-conformant images to be deployed, but writes details about the deployment to the Cloud Audit Logs. Dry run mode allows you to test a policy, for example in your production environment, before enforcement actually goes into effect.




Most production rules use the **Block and Audit Log** enforcement mode. **Dry Run: Audit Log Only** is primarily used for testing a policy in your environment before it goes into effect.

The enforcement mode for a rule is specified using the [`enforcementMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) property in the policy YAML file.

For more information about messages written to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs), see [View audit logs (GKE, Google Distributed Cloud, Cloud Service Mesh)](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs) or [View audit logs (Cloud Run)](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run).

## Continuous Validation

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Continuous Validation (CV) is a feature of Binary Authorization that periodically checks images associated with running Pods for continued policy conformance.

[Learn more about CV](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).

## Exempt images

**Note:** Using `exemptImages` to allowlist Google-managed system images is not recommended. To allowlist Google-managed system images, `globalPolicyEvaluationMode` should be set to `ENABLE`. See `globalPolicyEvaluationMode` for details.

An _exempt image_ is an image that is exempt from policy rules. Binary Authorization always allows exempt images to be deployed. Each project has an allowlist of exempt images specified by registry path. Images in the path `gcr.io/google_containers/*`, `k8s.gcr.io/**`, and additional paths are exempt by default, as these contain resources required so that GKE can start a cluster successfully with the default policy active.

To add an exempt image to the allowlist, add the following to the policy file: 
    
    
    admissionWhitelistPatterns:
      - namePattern: EXEMPT_IMAGE_PATH

Replace `EXEMPT_IMAGE_PATH` with the path to am image to exempt. To exempt additional images, add additional `- namePattern` entries. Learn more about [`admissionWhitelistPatterns`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#allowlistpatterns). 

### Allowlist patterns

  1. To allowlist all images whose registry location matches the specified path:
         
         gcr.io/example-project/*
         

  2. To allowlist all images whose registry location is any subdirectory of the specified path (e.g. `gcr.io/example-project/my-directory/helloworld`):
         
         gcr.io/example-project/**
         

  3. To allowlist a specific image:
         
         gcr.io/example-project/helloworld
         

  4. To allowlist a specific version of an image by tag:
         
         gcr.io/example-project/helloworld:latest
         gcr.io/example-project/helloworld:my-tag
         

  5. To allowlist all versions and tags of an image:
         
         gcr.io/example-project/helloworld@*
         

  6. To allowlist a specific version of an image by its digest:
         
         gcr.io/example-project/helloworld@sha256:77b0b75136b9bd0fd36fb50f4c92ae0dbdbbe164ab67885e736fa4374e0cbb8c
         




Learn more about [using container image digests](https://docs.cloud.google.com/architecture/using-container-images).

Learn how to manage exempt images in the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#manage_exempt_images), using the [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#manage_exempt_images), or using the [REST API](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-rest#manage_exempt_images).

### Google-maintained system images

_Trust all Google-maintained system images_ causes Binary Authorization to exempt a list of Google-maintained system images from further policy evaluation. When you have this setting enabled, images that are required by GKE are not blocked by policy enforcement. The system policy is evaluated prior to and in addition to user policy evaluation.

You can enable or disable this setting using the [`globalPolicyEvaluationMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#globalpolicyevaluationmode) property in the policy YAML file. You can view the contents of the system policy using the following command:
    
    
    gcloud alpha container binauthz policy export-system-policy
    

## Attestations

An _attestation_ is a digital document that certifies an image. During deployment, Binary Authorization verifies the attestation before it allows the image to be deployed.

The process of creating an attestation is sometimes called _signing an image_. An attestation is created after an image is built. Each such image has a globally unique digest. A signer signs the image digest by using a private key from a key pair and uses the signature to create the attestation. At deploy time, the Binary Authorization enforcer uses the attestor's public key to verify the signature in the attestation. Typically one attestor corresponds to exactly one signer.

An attestation signifies that the associated image was built by successfully executing a specific, required process. For example, if the signer is a representative of your quality assurance (QA) function, the attestation might indicate that the image has passed all required end-to-end functional testing in a staging environment.

To enable attestations in Binary Authorization, your policy's `evaluationMode` is set to `REQUIRE_ATTESTATION`.

Learn how to [create and use attestors and attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).

### Signers

A _signer_ is a person or automated process that creates an attestation by signing a unique image descriptor with a _private key_. The attestation is verified at deploy time by the corresponding _public key_ stored in an attestor before the associated image is deployed.

Learn how to [create and use attestors and attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).

### Attestors

An _attestor_ is a Google Cloud resource that Binary Authorization uses to verify the attestation at image deploy time. Attestors contain the public key that corresponds to the private key used by a signer to sign the image digest and create the attestation. The Binary Authorization enforcer uses the attestor at deploy time to limit which images are allowed to be deployed to those with an accompanying, verifiable attestation created prior to deployment.

Attestors are often managed by security operations personnel who also manage the public and private key pairs, whereas signers are typically software engineers or DevOps QA or compliance personnel responsible for producing deployable images, signing them with the private key and creating the attestations before attempting to deploy them.

Attestors have the following:

  * A corresponding Artifact Analysis note
  * One or more cryptographic public keys that correspond to the private key the signer used to create an attestation.



When you set up a policy that contains a **Require Attestations** rule, you must add an attestor for each person or process who is required to verify that the image is ready for deployment. You can add attestors using the Google Cloud console, the `gcloud` interface, or the Binary Authorization REST API.

Learn how to [create and use attestors and attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).

### Cryptographic keys

Binary Authorization uses digital signatures to verify images at deploy time when the policy contains a **Require Attestations** rule.

A key pair is generated. The _private key_ is used by the signer to sign an image descriptor. This creates an _attestation_.

Then, an attestor is created and stored in the policy. The _public key_ that corresponds to the private key used for signing is uploaded and attached to the attestor.

When an attempt is made to deploy an image, Binary Authorization uses attestors in the policy to verify the image's attestations. If the attestation can be verified, the image is deployed.

Binary Authorization supports two types of keys:

  * Public-Key Infrastructure (X.509) (PKIX) (which supports both classical algorithms and [post-quantum cryptography (PQC) algorithms](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli#set-up-cryptographic-keys))
  * [PGP](https://www.ietf.org/rfc/rfc4880.txt)



PKIX keys can be stored locally, externally, or in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs).

[Create a cryptographic key and an attestor](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console).

### Artifact Analysis notes

Binary Authorization uses [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) to store trusted metadata used in the authorization process. For each attestor you create, you must create one Artifact Analysis [note](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#note). Each [attestation](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations) is stored as an occurrence of this note.

When Binary Authorization evaluates a rule that requires that attestors have verified an image, it checks Artifact Analysis storage to see whether the required attestations are present.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
