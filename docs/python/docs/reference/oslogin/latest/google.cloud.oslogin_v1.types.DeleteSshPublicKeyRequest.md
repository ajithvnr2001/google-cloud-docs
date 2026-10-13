---
url: https://docs.cloud.google.com/python/docs/reference/oslogin/latest/google.cloud.oslogin_v1.types.DeleteSshPublicKeyRequest
title: Class DeleteSshPublicKeyRequest (2.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:04.744476+00:00
---

# Class DeleteSshPublicKeyRequest (2.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/oslogin/latest/google.cloud.oslogin_v1.types.DeleteSshPublicKeyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeleteSshPublicKeyRequest (2.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.23.0 (latest)  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.6  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.0  2.7.4  2.6.2  2.5.1  2.4.0  2.3.2  2.2.1  2.1.0  2.0.0  1.0.2  0.3.2  0.2.0 
    
    
    DeleteSshPublicKeyRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A request message for deleting an SSH public key.

## Attribute  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The fingerprint of the public key to update. Public keys are identified by their SHA-256 fingerprint. The fingerprint of the public key is in format `users/{user}/sshPublicKeys/{fingerprint}`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
