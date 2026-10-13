---
url: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.MaintenanceUpdatePolicy.DenyMaintenancePeriod
title: Class DenyMaintenancePeriod (0.11.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:28.350589+00:00
---

# Class DenyMaintenancePeriod (0.11.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.MaintenanceUpdatePolicy.DenyMaintenancePeriod

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DenyMaintenancePeriod (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.11.2  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.9  0.3.16  0.2.1  0.1.1 
    
    
    DenyMaintenancePeriod(mapping=None, *, ignore_unknown_fields=False, **kwargs)

DenyMaintenancePeriod definition. Excepting emergencies, maintenance will not be scheduled to start within this deny period. The start_date must be less than the end_date.

## Attributes  
  
---  
**Name** | **Description**  
`start_date` |  `google.type.date_pb2.Date`   
Deny period start date. This can be: \- A full date, with non-zero year, month and day values OR \- A month and day value, with a zero year for recurring   
`end_date` |  `google.type.date_pb2.Date`   
Deny period end date. This can be: \- A full date, with non-zero year, month and day values OR \- A month and day value, with a zero year for recurring   
`time` |  `google.type.timeofday_pb2.TimeOfDay`   
Time in UTC when the deny period starts on start_date and ends on end_date. This can be: \- Full time OR \- All zeros for 00:00:00 UTC   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
