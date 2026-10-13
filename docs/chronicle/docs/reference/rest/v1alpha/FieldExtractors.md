---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors/
title: FieldExtractors \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:02.090547+00:00
---

# FieldExtractors  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  FieldExtractors Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FieldExtractor
    * JSON representation
  * ComparisonOperator
  * LogFormat
  * PreProcessConfig
    * JSON representation



A representation of a parser extension as a set of field extractors.

JSON representation  
---  
      
    
    {
      "extractors": [
        {
          object ([FieldExtractor](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors#FieldExtractor))
        }
      ],
      "transformedCbnSnippet": string,
      "logFormat": enum ([LogFormat](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors#LogFormat)),
      "appendRepeatedFields": boolean,
      "preprocessConfig": {
        object ([PreProcessConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors#PreProcessConfig))
      }
    }  
  
Fields  
---  
`extractors[]` |  `object (`[FieldExtractor](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors#FieldExtractor)`)` List of FieldExtractors.  
`transformedCbnSnippet` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. CBN snippet generated from field extractors.A base64-encoded string.  
`logFormat` |  `enum (`[LogFormat](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors#LogFormat)`)` Format of the log. Ex. CSV,JSON,XML.  
`appendRepeatedFields  
**(deprecated)**` |  `boolean` This item is deprecated!Deprecated: Use ParserExtension.repeated_field_merge_strategy instead. Whether to append repeated fields or not. When false, repeated fields will be replaced.  
`preprocessConfig` |  `object (`[PreProcessConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors#PreProcessConfig)`)` Pre-process configuration.  
  
## FieldExtractor

An extractor for a single log field.

JSON representation  
---  
      
    
    {
      "preconditionPath": string,
      "preconditionValue": string,
      "preconditionOp": enum ([ComparisonOperator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors#ComparisonOperator)),
      "fieldPath": string,
      "destinationPath": string,
      "value": string
    }  
  
Fields  
---  
`preconditionPath` |  `string` Precondition path could be a json path, xml path or csv column name depending on log format. It refers to a section or substring in raw log.  
`preconditionValue` |  `string` Precondition value.  
`preconditionOp` |  `enum (`[ComparisonOperator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FieldExtractors#ComparisonOperator)`)` Operator used for precondition.  
`fieldPath` |  `string` Field path could be a json path, xml path or csv column name depending on log format. It refers to a section or substring in raw log. This is required if the FieldExtractor is used to specify the parser extension.  
`destinationPath` |  `string` Path in generated event which is to be populated. This is required if the FieldExtractor is used to specify the parser extension.  
`value` |  `string` Value to be mapped to the destination path directly.  
  
## ComparisonOperator

Comparison operator used in precondition field.

Enums  
---  
`COMPARISON_OPERATOR_UNSPECIFIED` | Comparison operator was unspecified.  
`EQUALS` | Comparison operator is equals "==".  
`NOT_EQUALS` | Comparison operator is not equals.  
  
## LogFormat

Log format of the raw log. valid log formats are JSON, XML and CSV.

Enums  
---  
`LOG_FORMAT_UNSPECIFIED` | Log format was unspecified.  
`JSON` | Log format was JSON.  
`CSV` | Log format was CSV.  
`XML` | Log format was XML.  
  
## PreProcessConfig

PreProcessConfig holds the GROK expression to extract the syslog header.

JSON representation  
---  
      
    
    {
      "grokRegex": string,
      "target": string
    }  
  
Fields  
---  
`grokRegex` |  `string` GROK Regex to extract the structured part of the log. syntax documentation: www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html  
`target` |  `string` Target field name for the structured part of the log. This should match a SEMANTIC identifier from the grok expression.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
