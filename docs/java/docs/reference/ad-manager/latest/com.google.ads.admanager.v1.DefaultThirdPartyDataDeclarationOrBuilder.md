---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DefaultThirdPartyDataDeclarationOrBuilder
title: Interface DefaultThirdPartyDataDeclarationOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:35.725167+00:00
---

# Interface DefaultThirdPartyDataDeclarationOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DefaultThirdPartyDataDeclarationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DefaultThirdPartyDataDeclarationOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DefaultThirdPartyDataDeclarationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the `DefaultThirdPartyDataDeclaration`. Format: `networks/{network_code}/defaultThirdPartyDataDeclaration`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the `DefaultThirdPartyDataDeclaration`. Format: `networks/{network_code}/defaultThirdPartyDataDeclaration`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getThirdPartyDataDeclaration()
    
    
    public abstract ThirdPartyDataDeclaration getThirdPartyDataDeclaration()

Optional. Returns the default [ThirdPartyDataDeclaration] for this network. If this setting has never been updated on your network, then this API response will be unset.

` optional .google.ads.admanager.v1.ThirdPartyDataDeclaration third_party_data_declaration = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyDataDeclaration](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyDataDeclaration)` | The thirdPartyDataDeclaration.  
  
### getThirdPartyDataDeclarationOrBuilder()
    
    
    public abstract ThirdPartyDataDeclarationOrBuilder getThirdPartyDataDeclarationOrBuilder()

Optional. Returns the default [ThirdPartyDataDeclaration] for this network. If this setting has never been updated on your network, then this API response will be unset.

` optional .google.ads.admanager.v1.ThirdPartyDataDeclaration third_party_data_declaration = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyDataDeclarationOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyDataDeclarationOrBuilder)` |   
  
### hasThirdPartyDataDeclaration()
    
    
    public abstract boolean hasThirdPartyDataDeclaration()

Optional. Returns the default [ThirdPartyDataDeclaration] for this network. If this setting has never been updated on your network, then this API response will be unset.

` optional .google.ads.admanager.v1.ThirdPartyDataDeclaration third_party_data_declaration = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the thirdPartyDataDeclaration field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
