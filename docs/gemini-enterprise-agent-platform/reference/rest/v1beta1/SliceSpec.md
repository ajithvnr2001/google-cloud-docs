---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec/
title: SliceSpec \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:42:30.954213+00:00
---

# SliceSpec  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  SliceSpec Stay organized with collections  Save and categorize content based on your preferences. 

Specification for how the data should be sliced.

Fields  
  
`configs` `map (key: string, value: object (`[SliceConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec#SliceConfig)`))` Mapping configuration for this SliceSpec. The key is the name of the feature. By default, the key will be prefixed by "instance" as a dictionary prefix for Vertex Batch Predictions output format. | JSON representation  
---  
      
    
    {
      "configs": {
        string: {
          object ([SliceConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec#SliceConfig))
        },
        ...
      }
    }  
  
## SliceConfig

Specification message containing the config for this SliceSpec. When `kind` is selected as `value` and/or `range`, only a single slice will be computed. When `allValues` is present, a separate slice will be computed for each possible label/value for the corresponding key in `config`. Examples, with feature zip_code with values 12345, 23334, 88888 and feature country with values "US", "Canada", "Mexico" in the dataset:

Example 1:
    
    
    {
      "zip_code": { "value": { "floatValue": 12345.0 } }
    }
    

A single slice for any data with zip_code 12345 in the dataset.

Example 2:
    
    
    {
      "zip_code": { "range": { "low": 12345, "high": 20000 } }
    }
    

A single slice containing data where the zip_codes between 12345 and 20000 For this example, data with the zip_code of 12345 will be in this slice.

Example 3:
    
    
    {
      "zip_code": { "range": { "low": 10000, "high": 20000 } },
      "country": { "value": { "stringValue": "US" } }
    }
    

A single slice containing data where the zip_codes between 10000 and 20000 has the country "US". For this example, data with the zip_code of 12345 and country "US" will be in this slice.

Example 4:
    
    
    { "country": {"allValues": { "value": true } } }
    

Three slices are computed, one for each unique country in the dataset.

Example 5:
    
    
    {
      "country": { "allValues": { "value": true } },
      "zip_code": { "value": { "floatValue": 12345.0 } }
    }
    

Three slices are computed, one for each unique country in the dataset where the zip_code is also 12345. For this example, data with zip_code 12345 and country "US" will be in one slice, zip_code 12345 and country "Canada" in another slice, and zip_code 12345 and country "Mexico" in another slice, totaling 3 slices.

Fields  
  
`kind` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`value` `object (`[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec#Value)`)` A unique specific value for a given feature. Example: `{ "value": { "stringValue": "12345" } }` | `range` `object (`[Range](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec#Range)`)` A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice. | `allValues` `boolean` If allValues is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"allValues":{"value":true}}` End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // kind
      "value": {
        object ([Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec#Value))
      },
      "range": {
        object ([Range](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec#Range))
      },
      "allValues": boolean
      // Union type
    }  
  
## Value

Single value that supports strings and floats.

Fields  
  
`kind` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`stringValue` `string` String type. | `floatValue` `number` Float type. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // kind
      "stringValue": string,
      "floatValue": number
      // Union type
    }  
  
## Range

A range of values for slice(s). `low` is inclusive, `high` is exclusive.

Fields  
  
`low` `number` Inclusive low value for the range. | `high` `number` Exclusive high value for the range. | JSON representation  
---  
      
    
    {
      "low": number,
      "high": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
