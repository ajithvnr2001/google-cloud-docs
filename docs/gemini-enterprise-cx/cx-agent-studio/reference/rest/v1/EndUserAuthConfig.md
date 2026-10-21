---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/EndUserAuthConfig/
title: EndUserAuthConfig \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:40.033861+00:00
---

# EndUserAuthConfig  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/EndUserAuthConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  EndUserAuthConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EndUserAuthConfig.Oauth2AuthCodeConfig
    * JSON representation
  * EndUserAuthConfig.Oauth2JwtBearerConfig
    * JSON representation



End-user authentication configuration used for Connection calls. The field values must be the names of context variables in the format `$context.variables.<name_of_variable>`.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "oauth2AuthCodeConfig": {
        object ([EndUserAuthConfig.Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/EndUserAuthConfig#EndUserAuthConfig.Oauth2AuthCodeConfig))
      },
      "oauth2JwtBearerConfig": {
        object ([EndUserAuthConfig.Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/EndUserAuthConfig#EndUserAuthConfig.Oauth2JwtBearerConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The auth configuration. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`oauth2AuthCodeConfig` |  `object (`[EndUserAuthConfig.Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/EndUserAuthConfig#EndUserAuthConfig.Oauth2AuthCodeConfig)`)` Oauth 2.0 Authorization Code authentication.  
`oauth2JwtBearerConfig` |  `object (`[EndUserAuthConfig.Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/EndUserAuthConfig#EndUserAuthConfig.Oauth2JwtBearerConfig)`)` JWT Profile Oauth 2.0 Authorization Grant authentication.  
End of mutually exclusive fields.  
  
## EndUserAuthConfig.Oauth2AuthCodeConfig

Oauth 2.0 Authorization Code authentication configuration.

JSON representation  
---  
      
    
    {
      "oauthToken": string
    }  
  
Fields  
---  
`oauthToken` |  `string` Required. Oauth token parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
## EndUserAuthConfig.Oauth2JwtBearerConfig

JWT Profile Oauth 2.0 Authorization Grant authentication configuration.

JSON representation  
---  
      
    
    {
      "issuer": string,
      "subject": string,
      "clientKey": string
    }  
  
Fields  
---  
`issuer` |  `string` Required. Issuer parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`subject` |  `string` Required. Subject parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`clientKey` |  `string` Required. Client parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
