---
url: https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types
title: Package types (1.20.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:11.583159+00:00
---

# Package types (1.20.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.1  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.2  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.0  1.6.2  1.5.1  1.4.0  1.3.3  1.2.3  1.1.0  1.0.1  0.6.0  0.5.0  0.4.1  0.3.1  0.2.2  0.1.1 

API documentation for `binaryauthorization_v1.types` package.

## Classes 

### [AdmissionRule](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.AdmissionRule)

An [admission rule][google.cloud.binaryauthorization.v1.AdmissionRule] specifies either that all container images used in a pod creation request must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be denied.

Images matching an [admission allowlist pattern][google.cloud.binaryauthorization.v1.AdmissionWhitelistPattern] are exempted from admission rules and will never block a pod creation.

### [AdmissionWhitelistPattern](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.AdmissionWhitelistPattern)

An [admission allowlist pattern][google.cloud.binaryauthorization.v1.AdmissionWhitelistPattern] exempts images from checks by [admission rules][google.cloud.binaryauthorization.v1.AdmissionRule].

### [Attestor](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.Attestor)

An attestor that attests to container image artifacts. An existing attestor cannot be modified except where indicated.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AttestorPublicKey](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.AttestorPublicKey)

An [attestor public key][google.cloud.binaryauthorization.v1.AttestorPublicKey] that will be used to verify attestations signed by this attestor.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateAttestorRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.CreateAttestorRequest)

Request message for BinauthzManagementServiceV1.CreateAttestor.

### [DeleteAttestorRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.DeleteAttestorRequest)

Request message for BinauthzManagementServiceV1.DeleteAttestor.

### [GetAttestorRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.GetAttestorRequest)

Request message for BinauthzManagementServiceV1.GetAttestor.

### [GetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.GetPolicyRequest)

Request message for BinauthzManagementServiceV1.GetPolicy.

### [GetSystemPolicyRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.GetSystemPolicyRequest)

Request to read the current system policy.

### [ListAttestorsRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.ListAttestorsRequest)

Request message for BinauthzManagementServiceV1.ListAttestors.

### [ListAttestorsResponse](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.ListAttestorsResponse)

Response message for BinauthzManagementServiceV1.ListAttestors.

### [PkixPublicKey](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.PkixPublicKey)

A public key in the PkixPublicKey `format <https://tools.ietf.org/html/rfc5280#section-4.1.2.7>`__. Public keys of this type are typically textually encoded using the PEM format.

### [Policy](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.Policy)

A policy for container image binary authorization.

### [UpdateAttestorRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.UpdateAttestorRequest)

Request message for BinauthzManagementServiceV1.UpdateAttestor.

### [UpdatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.UpdatePolicyRequest)

Request message for BinauthzManagementServiceV1.UpdatePolicy.

### [UserOwnedGrafeasNote](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.UserOwnedGrafeasNote)

An [user owned Grafeas note][google.cloud.binaryauthorization.v1.UserOwnedGrafeasNote] references a Grafeas Attestation.Authority Note created by the user.

### [ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.ValidateAttestationOccurrenceRequest)

Request message for ValidationHelperV1.ValidateAttestationOccurrence.

### [ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1.types.ValidateAttestationOccurrenceResponse)

Response message for ValidationHelperV1.ValidateAttestationOccurrence.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
