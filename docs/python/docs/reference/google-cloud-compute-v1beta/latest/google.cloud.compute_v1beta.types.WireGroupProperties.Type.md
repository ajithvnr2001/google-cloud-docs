---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.WireGroupProperties.Type
title: Class Type (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:34.013136+00:00
---

# Class Type (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.WireGroupProperties.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Type (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    Type(value)

The type of the wire group, one of the following:

::

  * WIRE: a single pseudowire over two Interconnect connections with no redundancy.
  * REDUNDANT: two pseudowires over four Interconnect connections, with two connections in one metro and two connections in another metro. Each redundant pair of Interconnect connections spans both edge availability domains of the metro. Each pseudowire connects Interconnect connections in matching edge availability domains of the two metros.
  * BOX_AND_CROSS: four pseudowires over four Interconnect connections, with two connections in one metro and two connections in another metro. Each redundant pair of Interconnect connections spans both edge availability domains of the metro. Two pseudowires connect Interconnect connections in matching edge availability domains of the two metros. Two additional pseudowires connect the non-matching edge availability domains of the two metros.



## Enums  
  
---  
**Name** | **Description**  
`UNDEFINED_TYPE` | A value indicating that the enum field is not set.  
`BOX_AND_CROSS` | Four pseudowires over four Interconnect connections, with two connections in one metro and two connections in another metro. Each redundant pair of Interconnect connections spans both edge availability domains of the metro. Two pseudowires connect Interconnect connections in matching edge availability domains of the two metros. Two additional pseudowires connect the non-matching edge availability domains of the two metros.  
`REDUNDANT` | Two pseudowires over four Interconnect connections, with two connections in one metro and two connections in another metro. Each redundant pair of Interconnect connections spans both edge availability domains of the metro. Each pseudowire connects Interconnect connections in matching edge availability domains of the two metros.  
`WIRE` | A single pseudowire over two Interconnect connections with no redundancy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
