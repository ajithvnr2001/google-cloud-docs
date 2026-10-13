---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationFilter
title: Class CompensationFilter (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:42.017392+00:00
---

# Class CompensationFilter (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationFilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CompensationFilter (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 
    
    
    CompensationFilter(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Filter on job compensation type and amount.

## Attributes  
  
---  
**Name** | **Description**  
`type_` |  `[google.cloud.talent_v4.types.CompensationFilter.FilterType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationFilter.FilterType)`   
Required. Type of filter.   
`units` |  `MutableSequence[[google.cloud.talent_v4.types.CompensationInfo.CompensationUnit](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationInfo.CompensationUnit)]`   
Required. Specify desired `base compensation entry's` CompensationInfo.CompensationUnit.   
`range_` |  `[google.cloud.talent_v4.types.CompensationInfo.CompensationRange](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationInfo.CompensationRange)`   
Compensation range.   
`include_jobs_with_unspecified_compensation_range` |  `bool`   
If set to true, jobs with unspecified compensation range fields are included.   
  
## Classes 

### FilterType
    
    
    FilterType(value)

Specify the type of filtering.
    
    
        See
        <xref uid="google.cloud.talent.v4.CompensationInfo.CompensationEntry">CompensationInfo.CompensationEntry</xref>
        for definition of base compensation entry.
    UNIT_AND_AMOUNT (2):
        Filter by `base compensation entry's` unit and amount /
        range. A job is a match if and only if the job contains a
        base CompensationEntry, and the base entry's unit matches
        provided
        <xref uid="google.cloud.talent.v4.CompensationInfo.CompensationUnit">CompensationUnit</xref>
        and amount or range overlaps with provided
        <xref uid="google.cloud.talent.v4.CompensationInfo.CompensationRange">CompensationRange</xref>.
    
        See
        <xref uid="google.cloud.talent.v4.CompensationInfo.CompensationEntry">CompensationInfo.CompensationEntry</xref>
        for definition of base compensation entry.
    
        Set exactly one
        <xref uid="google.cloud.talent.v4.CompensationFilter.units">units</xref> and
        populate
        <xref uid="google.cloud.talent.v4.CompensationFilter.range">range</xref>.
    ANNUALIZED_BASE_AMOUNT (3):
        Filter by annualized base compensation amount and
        `base compensation entry's` unit. Populate
        <xref uid="google.cloud.talent.v4.CompensationFilter.range">range</xref> and
        zero or more
        <xref uid="google.cloud.talent.v4.CompensationFilter.units">units</xref>.
    ANNUALIZED_TOTAL_AMOUNT (4):
        Filter by annualized total compensation amount and
        `base compensation entry's` unit . Populate
        <xref uid="google.cloud.talent.v4.CompensationFilter.range">range</xref> and
        zero or more
        <xref uid="google.cloud.talent.v4.CompensationFilter.units">units</xref>.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
