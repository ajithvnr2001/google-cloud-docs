---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Document.Layout.TextSegmentType
title: Class TextSegmentType (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:25.887397+00:00
---

# Class TextSegmentType (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Document.Layout.TextSegmentType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TextSegmentType (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    TextSegmentType(value)

The type of TextSegment in the context of the original document.

## Enums  
  
---  
**Name** | **Description**  
`TEXT_SEGMENT_TYPE_UNSPECIFIED` | Should not be used.  
`TOKEN` | The text segment is a token. e.g. word.  
`PARAGRAPH` | The text segment is a paragraph.  
`FORM_FIELD` | The text segment is a form field.  
`FORM_FIELD_NAME` | The text segment is the name part of a form field. It will be treated as child of another FORM_FIELD TextSegment if its span is subspan of another TextSegment with type FORM_FIELD.  
`FORM_FIELD_CONTENTS` | The text segment is the text content part of a form field. It will be treated as child of another FORM_FIELD TextSegment if its span is subspan of another TextSegment with type FORM_FIELD.  
`TABLE` | The text segment is a whole table, including headers, and all rows.  
`TABLE_HEADER` | The text segment is a table's headers. It will be treated as child of another TABLE TextSegment if its span is subspan of another TextSegment with type TABLE.  
`TABLE_ROW` | The text segment is a row in table. It will be treated as child of another TABLE TextSegment if its span is subspan of another TextSegment with type TABLE.  
`TABLE_CELL` | The text segment is a cell in table. It will be treated as child of another TABLE_ROW TextSegment if its span is subspan of another TextSegment with type TABLE_ROW.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
