---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult.Severity
title: Class Severity (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:33.620080+00:00
---

# Class Severity (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult.Severity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Severity (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    Severity(value)

Possible Severity values of an issued result.
    
    
        - Unsatisfiable condition: Expired timestamp in date/time
          condition.
        - Ineffective condition: Condition on a <principal, role>
          pair which is granted unconditionally in another binding
          of the same policy.
    NOTICE (3):
        Reserved for the issues that are not severe as
        `ERROR`/`WARNING`, but need special handling. For
        instance, messages about skipped validation units are issued
        as `NOTICE`.
    INFO (4):
        Any informative statement which is not severe enough to
        raise `ERROR`/`WARNING`/`NOTICE`, like auto-correction
        recommendations on the input content. Note that current
        version of the linter does not utilize `INFO`.
    DEPRECATED (5):
        Deprecated severity level.
    

## Enums  
  
---  
**Name** | **Description**  
`SEVERITY_UNSPECIFIED` | Severity is unspecified.  
`ERROR` | A validation unit returns an error only for critical issues. If an attempt is made to set the problematic policy without rectifying the critical issue, it causes the `setPolicy` operation to fail.  
`WARNING` | Any issue which is severe enough but does not cause an error. For example, suspicious constructs in the input object will not necessarily fail `setPolicy`, but there is a high likelihood that they won't behave as expected during policy evaluation in `checkPolicy`. This includes the following common scenarios:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
