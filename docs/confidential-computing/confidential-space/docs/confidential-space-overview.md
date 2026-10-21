---
url: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview/
title: Confidential Space overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:22.007712+00:00
---

# Confidential Space overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Space ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview)



Send feedback 

#  Confidential Space overview Stay organized with collections  Save and categorize content based on your preferences. 

Confidential Space provides an isolated environment to operate on sensitive data from multiple parties, so the owners of that data can keep it confidential. Sensitive data might include personally identifiable information (PII), protected health information (PHI), intellectual property, cryptographic secrets, machine learning (ML) models, or interactions with large language models (LLMs).

You might use Confidential Space to operate on sensitive data that's only visible to its original owners and a mutually agreed-upon workload. Alternatively, you could use it to offer end customers stronger data privacy, as the operator or owner of a Confidential Space environment can't access the data that is being processed.

Confidential Space is a trusted execution environment (TEE) that can be used to release your secrets only to authorized workloads. An attestation process and hardened OS image help protect the workload and the data that the workload processes from an operator.

For more detail about Confidential Space's use cases and security model, see [Confidential Space security overview](https://docs.cloud.google.com/docs/security/confidential-space).

## Confidential Space components

A Confidential Space system has three core components:

  * **A workload** : A containerized image containing code that processes the protected resources. This is run on top of a [Confidential Space image](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images), a hardened OS based on [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits). This in turn runs on a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs) that offers hardware isolation and remote attestation capabilities. The workload is typically located in a separate project from the protected resources.

  * **An attestation service** : A remote verifier that returns attestation evidence from an entity in the form of identity tokens. The tokens contain identification attributes for the workload. Confidential Space supports the following attestation services:

    * [Google Cloud Attestation](https://docs.cloud.google.com/confidential-computing/docs/attestation): Supports AMD SEV and Intel TDX VM instances. Runs in the same region that the workload runs in.

    * [Intel Trust Authority](https://www.intel.com/content/www/us/en/security/trust-authority.html): Supports Intel TDX VM instances. Runs in an Intel Trust Authority region that you define.

  * **Protected resources** : Managed resources that are protected by an authentication and authorization system. If the resources are in Google Cloud, they can be managed cloud resources such as Cloud Key Management Service (Cloud KMS) keys or Cloud Storage buckets. If the resources aren't in Google Cloud (for example, in an on-premises environment or in another cloud), then they can be any resource.




## Confidential Space roles

The components in a Confidential Space system are managed by people with three distinct roles:

  * **Data collaborators** : The people or organizations who own the protected resources being operated on by the workload. Data collaborators can access their own data, set permissions on that data, and depending on the workload's output might access results based on that data.

Data collaborators can't access each other's data or modify the workload code.

See [Create and grant access to confidential resources](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources) to learn more about the role of data collaborators.

  * **Workload author** : The person who creates the application that accesses and processes the confidential data. They add the application to a containerized image, for example, using [Docker](https://www.docker.com/), and upload the image to a repository such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).

The workload author has no access to the data or the results, and can't control access to them either.

See [Create and customize workloads](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads) to learn more about the workload author's role.

  * **Workload operator** : The person who runs the workload. The workload operator typically has full administrative privileges on the project they run the workload in. For example, they can manage resources in their project (such as Compute Engine instances, disks, and networking rules) and can interact with any Google Cloud API that acts on them.

The workload operator has no access to the data, and can't control access to it either. They can't influence or modify the workload code or execution environment.

See [Deploy workloads](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads) to learn more about the workload operator's role.




A person can assume one or more of these roles. For the highest security, Confidential Space supports a trust model where data collaborators, workload authors, and workload operators are separate, mutually distrusting parties. All roles must collaborate with each other to get the results they need.

## An example Confidential Space flow

Confidential Space makes use of multiple Google Cloud services to help private information be operated on confidentially. In general, setting up a Confidential Space might look similar to the following process:

  1. Multiple data collaborators store encrypted confidential data in their own isolated Google Cloud projects, often in different organizations. They want to compare and process that data without revealing it to each other or external parties. The encrypted data might live in [Cloud Storage](https://docs.cloud.google.com/storage/docs), [BigQuery](https://docs.cloud.google.com/bigquery/docs), or another service.

  2. The data collaborators create mock, non-confidential data for a test workload to operate on. This data might be different files, or live in a different place like a separate Cloud Storage bucket.

  3. The data collaborators create a [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation) (WIP). Later, a workload running in a workload operator's separate, isolated project can use that WIP to access the collaborators' confidential data.

  4. The workload author writes code to process the confidential data. In a project separate from the data collaborators and workload operator, they build a containerized image with Docker and upload it to [Artifact Registry](https://docs.cloud.google.com/artifact-registry).

  5. The workload operator creates a service account in an isolated project that has read access to where the data collaborators' encrypted confidential data is stored, and write access to somewhere (for example, a Cloud Storage bucket) to output the result of operating on the decrypted data. Later, this service account is attached to a Confidential VM which runs the workload.

  6. The data collaborators add a [provider](https://docs.cloud.google.com/iam/docs/workload-identity-federation#providers) to their workload identity pools. They add details to the provider like the attestation service that must be used, [attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) to create an audit trail in logs, and [attribute conditions](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions). These details verify the [assertions](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/attestation-assertions) made by the Confidential Space image, the workload container, and the workload VM instance. If the workload passes this verification, it's allowed to access and decrypt the confidential data.

  7. The workload is tested on the non-confidential data by starting a Confidential VM instance in the workload operator's project. The VM is based on a debug version of the Confidential Space image which loads the containerized workload.

After the VM's attestations are verified and the workload passes the data collaborators' conditions, the service account attached to the VM is allowed to access the confidential data, process it, and output a result.

  8. After [monitoring and debugging](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/monitor-debug) is complete, the workload is updated for production use. The data collaborators update and lock down their workload identity providers further if required, and they might choose to test the production workload on non-confidential data first.

  9. All parties sign off on the production workload, and it's ready to begin working on confidential data.




## Requirements

Confidential Space requires Confidential VM to work. Confidential VM instances must use AMD SEV, Intel TDX, or Intel TDX with NVIDIA Confidential Computing as the Confidential Computing technology. See [Supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations) to learn about hardware configuration options, and what locations Confidential VM instances can be created in.

## What's next

  * Learn more about [Confidential Space images](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images).

  * [Create your first Confidential Space environment](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-your-first-confidential-space-environment).

  * Use the [Prompt Encryption SDK](https://github.com/google/prompt-encryption-sdk) to serve an LLM in a TEE. See the [codelab](https://codelabs.developers.google.com/prompt-encryption-sdk) for instructions.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
