---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryRequest.CompletionType
title: Class CompletionType (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:00:36.543837+00:00
---

# Class CompletionType (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryRequest.CompletionType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CompletionType (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 
    
    
    CompletionType(value)

Enum to specify auto-completion topics.
    
    
        For
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType.JOB_TITLE">CompletionType.JOB_TITLE</xref>
        type, only open jobs with the same
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    COMPANY_NAME (2):
        Suggest company names for jobs autocomplete.
    
        For
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType.COMPANY_NAME">CompletionType.COMPANY_NAME</xref>
        type, only companies having open jobs with the same
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    COMBINED (3):
        Suggest both job titles and company names for jobs
        autocomplete.
    
        For
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType.COMBINED">CompletionType.COMBINED</xref>
        type, only open jobs with the same
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.language_codes">language_codes</xref>
        or companies having open jobs with the same
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    

## Enums  
  
---  
**Name** | **Description**  
`COMPLETION_TYPE_UNSPECIFIED` | Default value.  
`JOB_TITLE` | Suggest job titles for jobs autocomplete.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
