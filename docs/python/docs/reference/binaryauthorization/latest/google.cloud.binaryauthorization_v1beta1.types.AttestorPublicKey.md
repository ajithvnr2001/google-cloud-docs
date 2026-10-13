---
url: https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1beta1.types.AttestorPublicKey
title: Class AttestorPublicKey (1.20.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:53.403928+00:00
---

# Class AttestorPublicKey (1.20.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1beta1.types.AttestorPublicKey

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AttestorPublicKey (1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.1  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.2  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.0  1.6.2  1.5.1  1.4.0  1.3.3  1.2.3  1.1.0  1.0.1  0.6.0  0.5.0  0.4.1  0.3.1  0.2.2  0.1.1 
    
    
    AttestorPublicKey(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An [attestor public key][google.cloud.binaryauthorization.v1beta1.AttestorPublicKey] that will be used to verify attestations signed by this attestor.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`comment` |  `str`   
Optional. A descriptive comment. This field may be updated.   
`id` |  `str`   
The ID of this public key. Signatures verified by BinAuthz must include the ID of the public key that can be used to verify them, and that ID must match the contents of this field exactly. Additional restrictions on this field can be imposed based on which public key type is encapsulated. See the documentation on `public_key` cases below for details.   
`ascii_armored_pgp_public_key` |  `str`   
ASCII-armored representation of a PGP public key, as the entire output by the command `gpg --export --armor foo@example.com` (either LF or CRLF line endings). When using this field, `id` should be left blank. The BinAuthz API handlers will calculate the ID and fill it in automatically. BinAuthz computes this ID as the OpenPGP RFC4880 V4 fingerprint, represented as upper-case hex. If `id` is provided by the caller, it will be overwritten by the API-calculated ID. This field is a member of `oneof`_ `public_key`.   
`pkix_public_key` |  `[google.cloud.binaryauthorization_v1beta1.types.PkixPublicKey](https://docs.cloud.google.com/python/docs/reference/binaryauthorization/latest/google.cloud.binaryauthorization_v1beta1.types.PkixPublicKey)`   
A raw PKIX SubjectPublicKeyInfo format public key. NOTE: `id` may be explicitly provided by the caller when using this type of public key, but it MUST be a valid RFC3986 URI. If `id` is left blank, a default one will be computed based on the digest of the DER encoding of the public key. This field is a member of `oneof`_ `public_key`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
