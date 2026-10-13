---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult
title: Class LintResult (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:33.344423+00:00
---

# Class LintResult (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LintResult (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    LintResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Structured response of a single validation unit.

## Attributes  
  
---  
**Name** | **Description**  
`level` |  `[google.cloud.iam_admin_v1.types.LintResult.Level](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult.Level)`   
The validation unit level.   
`validation_unit_name` |  `str`   
The validation unit name, for instance "lintValidationUnits/ConditionComplexityCheck".   
`severity` |  `[google.cloud.iam_admin_v1.types.LintResult.Severity](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult.Severity)`   
The validation unit severity.   
`field_name` |  `str`   
The name of the field for which this lint result is about. For nested messages `field_name` consists of names of the embedded fields separated by period character. The top-level qualifier is the input object to lint in the request. For example, the `field_name` value `condition.expression` identifies a lint result for the `expression` field of the provided condition.   
`location_offset` |  `int`   
0-based character position of problematic construct within the object identified by `field_name`. Currently, this is populated only for condition expression.   
`debug_message` |  `str`   
Human readable debug message associated with the issue.   
  
## Classes 

### Level
    
    
    Level(value)

Possible Level values of a validation unit corresponding to its domain of discourse.

### Severity
    
    
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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
