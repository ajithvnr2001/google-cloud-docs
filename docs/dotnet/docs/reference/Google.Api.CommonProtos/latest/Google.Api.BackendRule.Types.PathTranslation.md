---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BackendRule.Types.PathTranslation
title: Enum BackendRule.Types.PathTranslation (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:42.072757+00:00
---

# Enum BackendRule.Types.PathTranslation (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BackendRule.Types.PathTranslation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Enum BackendRule.Types.PathTranslation (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BackendRule.Types.PathTranslation)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.BackendRule.Types.PathTranslation)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.BackendRule.Types.PathTranslation)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.BackendRule.Types.PathTranslation)


    
    
    public enum BackendRule.Types.PathTranslation

Path Translation specifies how to combine the backend address with the request path in order to produce the appropriate forwarding URL for the request.

Path Translation is applicable only to HTTP-based backends. Backends which do not accept requests over HTTP/HTTPS should leave `path_translation` unspecified.

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Fields   
  
---  
**Name** | **Description**  
`AppendPathToAddress` | The request path will be appended to the backend address.

# Examples

Given the following operation config:
    
    
    Method path:        /api/company/{cid}/user/{uid}
    Backend address:    https://example.appspot.com
    

Requests to the following request paths will call the backend at the translated path:
    
    
    Request path: /api/company/widgetworks/user/johndoe
    Translated:
    https://example.appspot.com/api/company/widgetworks/user/johndoe
    
    Request path: /api/company/widgetworks/user/johndoe?timezone=EST
    Translated:
    https://example.appspot.com/api/company/widgetworks/user/johndoe?timezone=EST
      
  
`ConstantAddress` | Use the backend address as-is, with no modification to the path. If the URL pattern contains variables, the variable names and values will be appended to the query string. If a query string parameter and a URL pattern variable have the same name, this may result in duplicate keys in the query string.

# Examples

Given the following operation config:
    
    
    Method path:        /api/company/{cid}/user/{uid}
    Backend address:    https://example.cloudfunctions.net/getUser
    

Requests to the following request paths will call the backend at the translated path:
    
    
    Request path: /api/company/widgetworks/user/johndoe
    Translated:
    https://example.cloudfunctions.net/getUser?cid=widgetworks&uid=johndoe
    
    Request path: /api/company/widgetworks/user/johndoe?timezone=EST
    Translated:
    https://example.cloudfunctions.net/getUser?timezone=EST&cid=widgetworks&uid=johndoe
      
  
`Unspecified` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
