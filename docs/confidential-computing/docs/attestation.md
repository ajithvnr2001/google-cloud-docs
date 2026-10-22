---
url: https://docs.cloud.google.com/confidential-computing/docs/attestation/
title: Google Cloud Attestation \u00a0|\u00a0 Confidential Computing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:01.856114+00:00
---

# Google Cloud Attestation  |  Confidential Computing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/docs/attestation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Computing ](https://docs.cloud.google.com/confidential-computing/docs)



Send feedback 

#  Google Cloud Attestation Stay organized with collections  Save and categorize content based on your preferences. 

Attestation is the process that establishes trust in [Confidential Computing](https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview). Attestation acts as a digital verification mechanism, ensuring that confidential data is only processed within hardware-based Trusted Execution Environments (TEEs) that have been rigorously vetted.

Google Cloud Attestation provides a unified solution for remotely verifying the trustworthiness of all Google confidential environments. The service supports attestation of confidential environments backed by a Virtual Trusted Platform Module (vTPM) for SEV and the TDX Module for Intel TDX.

Google Cloud Attestation can be applied across the following Google Cloud services:

Confidential Computing service | Confidential Computing technology | Google Cloud Attestation support |  [ **Confidential VM**](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) | AMD SEV |   
---|---|---  
AMD SEV-SNP |   
Intel TDX on C3 machine types |   
[ **Confidential Space**](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview) | AMD SEV |   
Intel TDX |   
[ **Confidential GKE Nodes**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes) | AMD SEV |   
  
While Google Cloud Attestation is convenient, open-source tools can also obtain attestation reports directly for Confidential VM instances. For more details, see [Request an attestation report](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation#request_an_attestation_report).

## How Google Cloud Attestation works

Google Cloud Attestation internally gathers endorsements directly from hardware vendors and upholds its own set of reference values and appraisal policies specifically tailored for each confidential environment. It provides APIs for Google Cloud users to fetch attestation result claims tokens.

Google Cloud Attestation collects information from your confidential environment and checks it against approved values and Google-maintained policies. These checks are converted into verifiable claims that adhere to the [IETF Remote ATtestation ProcedureS (RATS) Entity Attestation Token (EAT)](https://datatracker.ietf.org/doc/draft-ietf-rats-eat/) standard. Then, Google Cloud Attestation provides cryptographic proofs of these claims that can be used by services relying on such claims, such as Secret Manager and Google [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs).

The cryptographic proofs can be validated in the following ways:

  1. Using a public key. For more information, see [OIDC tokens](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/token-validation-endpoint-fields#oidc). This is the simpler option and works natively with OIDC compatible applications.

  2. Using a root certificate. For more information, see [PKI tokens](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/token-validation-endpoint-fields#pki). This option allows offline verification, without the need for each relying party to discover the verification key. For an end-to-end example of offline validation, see the [Use Confidential Space with protected resources that aren't stored with a cloud provider](https://codelabs.developers.google.com/confidential-space-pki#0) codelab.




## RATS architecture overview

The Remote ATtestation ProcedureS (RATS) architecture involves the following primary entities:

  * Attester: An entity providing evidence of its trustworthiness. In Google Cloud, this is a confidential environment (for example, Confidential VM, Confidential GKE Nodes, or Confidential Space).

  * Verifier: An entity evaluating the evidence and generating attestation results. This is Google Cloud Attestation.

  * Relying party: An entity relying on the attestation results to make decisions (for example, a mobile app, storage bucket, or key management system).




The RATS architecture encompasses the following key roles:

  * Relying party owner: An entity configuring the appraisal policy for the relying party.

  * Verifier owner: An entity configuring the appraisal policy for the verifier (for example, Google).

  * Endorser: An entity providing endorsements validating the attester's capabilities (for example, hardware OEMs like AMD, Intel, or NVIDIA).

  * Reference value provider: An entity providing reference values for the verifier to validate the attester's claims.




When used in combination with Confidential Space, Google Cloud Attestation uses the [passport model](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview#passport-model). However, depending on how you've set up your attester and relying party, Google Cloud Attestation can also be integrated into a [background check model](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview#background-check-model).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
