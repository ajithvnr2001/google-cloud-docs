---
url: https://docs.cloud.google.com/python/docs/reference/privateca/latest/google.cloud.security.privateca_v1.types.CertificateRevocationList
title: Class CertificateRevocationList (1.20.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:27.004154+00:00
---

# Class CertificateRevocationList (1.20.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/privateca/latest/google.cloud.security.privateca_v1.types.CertificateRevocationList

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CertificateRevocationList (1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.3  1.13.1  1.12.2  1.11.0  1.10.3  1.9.0  1.8.1  1.7.1  1.6.1  1.5.0  1.4.3  1.3.2  1.2.4  1.1.0  1.0.6  0.4.0  0.3.0  0.1.1 
    
    
    CertificateRevocationList(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A CertificateRevocationList corresponds to a signed X.509 certificate Revocation List (CRL). A CRL contains the serial numbers of certificates that should no longer be trusted.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`.   
`sequence_number` |  `int`   
Output only. The CRL sequence number that appears in pem_crl.   
`revoked_certificates` |  `MutableSequence[[google.cloud.security.privateca_v1.types.CertificateRevocationList.RevokedCertificate](https://docs.cloud.google.com/python/docs/reference/privateca/latest/google.cloud.security.privateca_v1.types.CertificateRevocationList.RevokedCertificate)]`   
Output only. The revoked serial numbers that appear in pem_crl.   
`pem_crl` |  `str`   
Output only. The PEM-encoded X.509 CRL.   
`access_url` |  `str`   
Output only. The location where 'pem_crl' can be accessed.   
`state` |  `[google.cloud.security.privateca_v1.types.CertificateRevocationList.State](https://docs.cloud.google.com/python/docs/reference/privateca/latest/google.cloud.security.privateca_v1.types.CertificateRevocationList.State)`   
Output only. The State for this CertificateRevocationList.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which this CertificateRevocationList was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which this CertificateRevocationList was updated.   
`revision_id` |  `str`   
Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels with user-defined metadata.   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### RevokedCertificate
    
    
    RevokedCertificate(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes a revoked Certificate.

### State
    
    
    State(value)

The state of a CertificateRevocationList, indicating if it is current.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
