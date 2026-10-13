---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.AccessReason
title: Class AccessReason (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:09.265779+00:00
---

# Class AccessReason (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.AccessReason

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AccessReason (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7  0.1.3 
    
    
    AccessReason(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Reason for the access.

## Attributes  
  
---  
**Name** | **Description**  
`type_` |  `[google.cloud.cloudcontrolspartner_v1.types.AccessReason.Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.AccessReason.Type)`   
Type of access justification.   
`detail` |  `str`   
More detail about certain reason types. See comments for each type above.   
  
## Classes 

### Type
    
    
    Type(value)

Type of access justification.
    
    
        - "Feedback Report: #####"
        - "Case Number: #####"
        - "Case ID: #####"
        - "E-PIN Reference: #####"
        - "Google-#####"
        - "T-#####".
    GOOGLE_INITIATED_SERVICE (2):
        The principal accessed customer data in order
        to diagnose or resolve a suspected issue in
        services. Often this access is used to confirm
        that customers are not affected by a suspected
        service issue or to remediate a reversible
        system issue.
    GOOGLE_INITIATED_REVIEW (3):
        Google initiated service for security, fraud,
        abuse, or compliance purposes.
    THIRD_PARTY_DATA_REQUEST (4):
        The principal was compelled to access
        customer data in order to respond to a legal
        third party data request or process, including
        legal processes from customers themselves.
    GOOGLE_RESPONSE_TO_PRODUCTION_ALERT (5):
        The principal accessed customer data in order
        to diagnose or resolve a suspected issue in
        services or a known outage.
    CLOUD_INITIATED_ACCESS (6):
        Similar to 'GOOGLE_INITIATED_SERVICE' or
        'GOOGLE_INITIATED_REVIEW', but with universe agnostic
        naming. The principal accessed customer data in order to
        diagnose or resolve a suspected issue in services or a known
        outage, or for security, fraud, abuse, or compliance review
        purposes.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
