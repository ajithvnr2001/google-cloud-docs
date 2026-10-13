---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings
title: Google Analytics Admin V1alpha Client - Class AttributionSettings (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:49.286009+00:00
---

# Google Analytics Admin V1alpha Client - Class AttributionSettings (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class AttributionSettings (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class AttributionSettings.

The attribution settings used for a given property. This is a singleton resource.

Generated from protobuf message `google.analytics.admin.v1alpha.AttributionSettings`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Output only. Resource name of this attribution settings resource. Format: properties/{property_id}/attributionSettings Example: "properties/1000/attributionSettings"  
`↳ acquisition_conversion_event_lookback_window` |  `int`   
Required. The lookback window configuration for acquisition conversion events. The default window size is 30 days.  
`↳ other_conversion_event_lookback_window` |  `int`   
Required. The lookback window for all other, non-acquisition conversion events. The default window size is 90 days.  
`↳ reporting_attribution_model` |  `int`   
Required. The reporting attribution model used to calculate conversion credit in this property's reports. Changing the attribution model will apply to both historical and future data. These changes will be reflected in reports with conversion and revenue data. User and session data will be unaffected.  
`↳ ads_web_conversion_data_export_scope` |  `int`   
Required. The Conversion Export Scope for data exported to linked Ads Accounts.  
  
### getName

Output only. Resource name of this attribution settings resource.

Format: properties/{property_id}/attributionSettings Example: "properties/1000/attributionSettings"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Resource name of this attribution settings resource.

Format: properties/{property_id}/attributionSettings Example: "properties/1000/attributionSettings"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAcquisitionConversionEventLookbackWindow

Required. The lookback window configuration for acquisition conversion events. The default window size is 30 days.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [AcquisitionConversionEventLookbackWindow](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings.AcquisitionConversionEventLookbackWindow).  
  
### setAcquisitionConversionEventLookbackWindow

Required. The lookback window configuration for acquisition conversion events. The default window size is 30 days.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [AcquisitionConversionEventLookbackWindow](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings.AcquisitionConversionEventLookbackWindow).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOtherConversionEventLookbackWindow

Required. The lookback window for all other, non-acquisition conversion events. The default window size is 90 days.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [OtherConversionEventLookbackWindow](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings.OtherConversionEventLookbackWindow).  
  
### setOtherConversionEventLookbackWindow

Required. The lookback window for all other, non-acquisition conversion events. The default window size is 90 days.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [OtherConversionEventLookbackWindow](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings.OtherConversionEventLookbackWindow).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReportingAttributionModel

Required. The reporting attribution model used to calculate conversion credit in this property's reports.

Changing the attribution model will apply to both historical and future data. These changes will be reflected in reports with conversion and revenue data. User and session data will be unaffected.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ReportingAttributionModel](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings.ReportingAttributionModel).  
  
### setReportingAttributionModel

Required. The reporting attribution model used to calculate conversion credit in this property's reports.

Changing the attribution model will apply to both historical and future data. These changes will be reflected in reports with conversion and revenue data. User and session data will be unaffected.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ReportingAttributionModel](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings.ReportingAttributionModel).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdsWebConversionDataExportScope

Required. The Conversion Export Scope for data exported to linked Ads Accounts.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [AdsWebConversionDataExportScope](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings.AdsWebConversionDataExportScope).  
  
### setAdsWebConversionDataExportScope

Required. The Conversion Export Scope for data exported to linked Ads Accounts.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [AdsWebConversionDataExportScope](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings.AdsWebConversionDataExportScope).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
