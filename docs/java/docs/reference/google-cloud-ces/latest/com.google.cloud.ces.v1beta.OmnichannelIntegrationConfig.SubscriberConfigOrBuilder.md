---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OmnichannelIntegrationConfig.SubscriberConfigOrBuilder
title: Interface OmnichannelIntegrationConfig.SubscriberConfigOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:58.726649+00:00
---

# Interface OmnichannelIntegrationConfig.SubscriberConfigOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OmnichannelIntegrationConfig.SubscriberConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OmnichannelIntegrationConfig.SubscriberConfigOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public static interface OmnichannelIntegrationConfig.SubscriberConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCesAppConfig()
    
    
    public abstract OmnichannelIntegrationConfig.CesAppConfig getCesAppConfig()

Ces app config.

`.google.cloud.ces.v1beta.OmnichannelIntegrationConfig.CesAppConfig ces_app_config = 1; `

**Returns**  
---  
**Type** | **Description**  
`[OmnichannelIntegrationConfig.CesAppConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OmnichannelIntegrationConfig.CesAppConfig)` | The cesAppConfig.  
  
### getCesAppConfigOrBuilder()
    
    
    public abstract OmnichannelIntegrationConfig.CesAppConfigOrBuilder getCesAppConfigOrBuilder()

Ces app config.

`.google.cloud.ces.v1beta.OmnichannelIntegrationConfig.CesAppConfig ces_app_config = 1; `

**Returns**  
---  
**Type** | **Description**  
`[OmnichannelIntegrationConfig.CesAppConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OmnichannelIntegrationConfig.CesAppConfigOrBuilder)` |   
  
### getSubscriberConfigCase()
    
    
    public abstract OmnichannelIntegrationConfig.SubscriberConfig.SubscriberConfigCase getSubscriberConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[OmnichannelIntegrationConfig.SubscriberConfig.SubscriberConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OmnichannelIntegrationConfig.SubscriberConfig.SubscriberConfigCase)` |   
  
### hasCesAppConfig()
    
    
    public abstract boolean hasCesAppConfig()

Ces app config.

`.google.cloud.ces.v1beta.OmnichannelIntegrationConfig.CesAppConfig ces_app_config = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cesAppConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
