---
url: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.DataMaskingPolicy.PredefinedExpression
title: Class PredefinedExpression (0.10.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:32.152466+00:00
---

# Class PredefinedExpression (0.10.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.DataMaskingPolicy.PredefinedExpression

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PredefinedExpression (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.0  0.7.0  0.6.16  0.5.3  0.4.0  0.3.2  0.2.0  0.1.1 
    
    
    PredefinedExpression(value)

The available masking rules. Learn more here: <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>.
    
    
        - STRING: ""
        - BYTES: b''
        - INTEGER: 0
        - FLOAT: 0.0
        - NUMERIC: 0
        - BOOLEAN: FALSE
        - TIMESTAMP: 1970-01-01 00:00:00 UTC
        - DATE: 1970-01-01
        - TIME: 00:00:00
        - DATETIME: 1970-01-01T00:00:00
        - GEOGRAPHY: POINT(0 0)
        - BIGNUMERIC: 0
        - ARRAY: []
        - STRUCT: NOT_APPLICABLE
        - JSON: NULL
    LAST_FOUR_CHARACTERS (4):
        Masking expression shows the last four characters of text.
        The masking behavior is as follows:
    
        - If text length > 4 characters: Replace text with XXXXX,
          append last four characters of original text.
        - If text length <= 4 characters: Apply SHA-256 hash.
    FIRST_FOUR_CHARACTERS (5):
        Masking expression shows the first four characters of text.
        The masking behavior is as follows:
    
        - If text length > 4 characters: Replace text with XXXXX,
          prepend first four characters of original text.
        - If text length <= 4 characters: Apply SHA-256 hash.
    EMAIL_MASK (6):
        Masking expression for email addresses. The masking behavior
        is as follows:
    
        - Syntax-valid email address: Replace username with XXXXX.
          For example, cloudysanfrancisco@gmail.com becomes
          XXXXX@gmail.com.
        - Syntax-invalid email address: Apply SHA-256 hash.
    
        For more information, see `Email
        mask <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>`__.
    DATE_YEAR_MASK (7):
        Masking expression to only show the year of `Date`,
        `DateTime` and `TimeStamp`. For example, with the year
        2076:
    
        - DATE : 2076-01-01
        - DATETIME : 2076-01-01T00:00:00
        - TIMESTAMP : 2076-01-01 00:00:00 UTC
    
        Truncation occurs according to the UTC time zone. To change
        this, adjust the default time zone using the `time_zone`
        system variable. For more information, see `System variables
        reference <https://cloud.google.com/bigquery/docs/reference/system-variables>`__.
    RANDOM_HASH (8):
        Masking expression that uses hashing to mask
        column data. It differs from SHA256 in that a
        unique random value is generated for each query
        and is added to the hash input, resulting in the
        hash / masked result to be different for each
        query. Hence the name "random hash".
    

## Enums  
  
---  
**Name** | **Description**  
`PREDEFINED_EXPRESSION_UNSPECIFIED` | Default, unspecified predefined expression. No masking will take place since no expression is specified.  
`SHA256` | Masking expression to replace data with SHA-256 hash.  
`ALWAYS_NULL` | Masking expression to replace data with NULLs.  
`DEFAULT_MASKING_VALUE` | Masking expression to replace data with their default masking values. The default masking values for each type listed as below:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
