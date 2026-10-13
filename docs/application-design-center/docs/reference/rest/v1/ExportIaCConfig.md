---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ExportIaCConfig/
title: ExportIaCConfig \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:19.690229+00:00
---

# ExportIaCConfig  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ExportIaCConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  ExportIaCConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TerraformConfig
    * JSON representation
  * TerraformModuleConfig
    * JSON representation



Configuration for exporting a resource as IAC.

JSON representation  
---  
      
    
    {
      "iacFormat": enum ([IACFormat](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/IACFormat)),
    
      // Union field config_payload can be only one of the following:
      "tfConfig": {
        object ([TerraformConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ExportIaCConfig#TerraformConfig))
      }
      // End of list of possible types for union field config_payload.
    }  
  
Fields  
---  
`iacFormat` |  `enum (`[IACFormat](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/IACFormat)`)` Optional. IaC format of the export. Default is [IACFormat.TERRAFORM].  
Union field `config_payload`. Configuration for the export based on the IaC format. `config_payload` can be only one of the following:  
`tfConfig` |  `object (`[TerraformConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ExportIaCConfig#TerraformConfig)`)` Optional. Configuration on how to handle terraform IaC export.  
  
## TerraformConfig

Configuration for exporting a resource as Terraform IAC.

JSON representation  
---  
      
    
    {
      "tfModuleConfig": {
        object ([TerraformModuleConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ExportIaCConfig#TerraformModuleConfig))
      }
    }  
  
Fields  
---  
`tfModuleConfig` |  `object (`[TerraformModuleConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/ExportIaCConfig#TerraformModuleConfig)`)` Optional. Configuration on how terraform module should be handled during export.  
  
## TerraformModuleConfig

Configuration on how terraform module should be handled during export.

JSON representation  
---  
      
    
    {
    
      // Union field source_override can be only one of the following:
      "gitProxyEnabled": boolean,
      "localReferencesEnabled": boolean
      // End of list of possible types for union field source_override.
    }  
  
Fields  
---  
Union field `source_override`. Specifies an override for the default module source handling. If no override is set, the default behavior is to keep the original module references. `source_override` can be only one of the following:  
`gitProxyEnabled` |  `boolean` Optional. This is typically only valid for 3P components if ingested via devconnect URI. Typically, for 1P components, since they are sourced from public git repos, this field is not applicable.  
`localReferencesEnabled` |  `boolean` Optional. If set, all the dependent modules will be downloaded from the target repository and referenced locally.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
