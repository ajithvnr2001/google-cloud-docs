---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.WebStreamData
title: Google Analytics Admin V1alpha Client - Class WebStreamData (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:01.854401+00:00
---

# Google Analytics Admin V1alpha Client - Class WebStreamData (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.WebStreamData

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class WebStreamData (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class WebStreamData.

Data specific to web streams.

Generated from protobuf message `google.analytics.admin.v1alpha.DataStream.WebStreamData`

## Namespace

Google \ Analytics \ Admin \ V1alpha \ DataStream

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ measurement_id` |  `string`   
Output only. Analytics Measurement ID. Example: "G-1A2BCD345E"  
`↳ firebase_app_id` |  `string`   
Output only. ID of the corresponding web app in Firebase, if any. This ID can change if the web app is deleted and recreated.  
`↳ default_uri` |  `string`   
Domain name of the web app being measured, or empty. Example: "<http://www.google.com>", "<https://www.google.com>"  
  
### getMeasurementId

Output only. Analytics Measurement ID.

Example: "G-1A2BCD345E"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setMeasurementId

Output only. Analytics Measurement ID.

Example: "G-1A2BCD345E"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFirebaseAppId

Output only. ID of the corresponding web app in Firebase, if any.

This ID can change if the web app is deleted and recreated.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFirebaseAppId

Output only. ID of the corresponding web app in Firebase, if any.

This ID can change if the web app is deleted and recreated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDefaultUri

Domain name of the web app being measured, or empty.

Example: "<http://www.google.com>", "<https://www.google.com>"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDefaultUri

Domain name of the web app being measured, or empty.

Example: "<http://www.google.com>", "<https://www.google.com>"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
