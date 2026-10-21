---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig/
title: LoggingConfig \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:07:14.340392+00:00
---

# LoggingConfig  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  LoggingConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * LogGenerationRule
    * JSON representation
  * LoggingLevel
  * ServiceLogGenerationRule
    * JSON representation



Project level logging config to control what level of log will be generated and written to Cloud Logging.

JSON representation  
---  
      
    
    {
      "name": string,
      "defaultLogGenerationRule": {
        object ([LogGenerationRule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#LogGenerationRule))
      },
      "serviceLogGenerationRules": [
        {
          object ([ServiceLogGenerationRule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#ServiceLogGenerationRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. The name of the LoggingConfig singleton resource. Format: projects/*/loggingConfig  
`defaultLogGenerationRule` |  `object (`[LogGenerationRule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#LogGenerationRule)`)` The log generation rule that applies by default to all services supporting log generation. It can be overridden by `[ServiceLogGenerationRule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#ServiceLogGenerationRule)` for service level control.  
`serviceLogGenerationRules[]` |  `object (`[ServiceLogGenerationRule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#ServiceLogGenerationRule)`)` Controls logging configurations more granularly for each supported service.This overrides the `[defaultLogGenerationRule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#FIELDS.default_log_generation_rule)` for the services specified. For those not mentioned, they will fallback to the default log generation rule.  
  
## LogGenerationRule

The logging configurations for services supporting log generation.

JSON representation  
---  
      
    
    {
      "loggingLevel": enum ([LoggingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#LoggingLevel)),
      "infoLogSampleRate": number
    }  
  
Fields  
---  
`loggingLevel` |  `enum (`[LoggingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#LoggingLevel)`)` The logging level.By default it is set to `LOG_WARNINGS_AND_ABOVE`.  
`infoLogSampleRate` |  `number` The log sample rate for INFO level log entries. You can use this to reduce the number of entries generated for INFO level logs.DO NOT set this field if the `[loggingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#LogGenerationRule.FIELDS.logging_level)` is not `[LoggingLevel.LOG_ALL](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#LoggingLevel.ENUM_VALUES.LOG_ALL)`. Otherwise, an INVALID_ARGUMENT error is returned.Sample rate for INFO logs defaults to 1 when unset (generate and send all INFO logs to Cloud Logging). Its value must be greater than 0 and less than or equal to 1.  
  
## LoggingLevel

The setting to control log generation.

Enums  
---  
`LOGGING_LEVEL_UNSPECIFIED` | Default value. Defaults to `LOG_FOR_WARNINGS_AND_ABOVE` if unset.  
`LOGGING_DISABLED` | No log will be generated and sent to Cloud Logging.  
`LOG_ERRORS_AND_ABOVE` | Log for operations resulted in fatal error.  
`LOG_WARNINGS_AND_ABOVE` | In addition to `LOG_ERRORS_AND_ABOVE`, also log for operations that have soft errors, quality suggestions.  
`LOG_ALL` | Log all operations, including successful ones.  
  
## ServiceLogGenerationRule

The granular logging configurations for supported services.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "logGenerationRule": {
        object ([LogGenerationRule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#LogGenerationRule))
      }
    }  
  
Fields  
---  
`serviceName` |  `string` Required. Supported service names: "CatalogService", "CompletionService", "ControlService", "MerchantCenterStreaming", "ModelService", "PredictionService", "ProductService", "ServingConfigService", "UserEventService",  
`logGenerationRule` |  `object (`[LogGenerationRule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig#LogGenerationRule)`)` The log generation rule that applies to this service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
