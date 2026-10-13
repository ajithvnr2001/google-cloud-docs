---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChangeHistoryChange.ChangeHistoryResource
title: Google Analytics Admin V1alpha Client - Class ChangeHistoryResource (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:54.716297+00:00
---

# Google Analytics Admin V1alpha Client - Class ChangeHistoryResource (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChangeHistoryChange.ChangeHistoryResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class ChangeHistoryResource (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class ChangeHistoryResource.

A snapshot of a resource as before or after the result of a change in change history.

Generated from protobuf message `google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource`

## Namespace

Google \ Analytics \ Admin \ V1alpha \ ChangeHistoryChange

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ account` |  `[Google\Analytics\Admin\V1alpha\Account](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Account)`   
A snapshot of an Account resource in change history.  
`↳ property` |  `[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)`   
A snapshot of a Property resource in change history.  
`↳ firebase_link` |  `[Google\Analytics\Admin\V1alpha\FirebaseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.FirebaseLink)`   
A snapshot of a FirebaseLink resource in change history.  
`↳ google_ads_link` |  `[Google\Analytics\Admin\V1alpha\GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink)`   
A snapshot of a GoogleAdsLink resource in change history.  
`↳ google_signals_settings` |  `[Google\Analytics\Admin\V1alpha\GoogleSignalsSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleSignalsSettings)`   
A snapshot of a GoogleSignalsSettings resource in change history.  
`↳ display_video_360_advertiser_link` |  `[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)`   
A snapshot of a DisplayVideo360AdvertiserLink resource in change history.  
`↳ display_video_360_advertiser_link_proposal` |  `[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)`   
A snapshot of a DisplayVideo360AdvertiserLinkProposal resource in change history.  
`↳ conversion_event` |  `[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)`   
A snapshot of a ConversionEvent resource in change history.  
`↳ measurement_protocol_secret` |  `[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)`   
A snapshot of a MeasurementProtocolSecret resource in change history.  
`↳ custom_dimension` |  `[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)`   
A snapshot of a CustomDimension resource in change history.  
`↳ custom_metric` |  `[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)`   
A snapshot of a CustomMetric resource in change history.  
`↳ data_retention_settings` |  `[Google\Analytics\Admin\V1alpha\DataRetentionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings)`   
A snapshot of a data retention settings resource in change history.  
`↳ search_ads_360_link` |  `[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)`   
A snapshot of a SearchAds360Link resource in change history.  
`↳ data_stream` |  `[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)`   
A snapshot of a DataStream resource in change history.  
`↳ attribution_settings` |  `[Google\Analytics\Admin\V1alpha\AttributionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings)`   
A snapshot of AttributionSettings resource in change history.  
`↳ expanded_data_set` |  `[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)`   
A snapshot of an ExpandedDataSet resource in change history.  
`↳ channel_group` |  `[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)`   
A snapshot of a ChannelGroup resource in change history.  
`↳ bigquery_link` |  `[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)`   
A snapshot of a BigQuery link resource in change history.  
`↳ enhanced_measurement_settings` |  `[Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings)`   
A snapshot of EnhancedMeasurementSettings resource in change history.  
`↳ data_redaction_settings` |  `[Google\Analytics\Admin\V1alpha\DataRedactionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRedactionSettings)`   
A snapshot of DataRedactionSettings resource in change history.  
`↳ skadnetwork_conversion_value_schema` |  `[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)`   
A snapshot of SKAdNetworkConversionValueSchema resource in change history.  
`↳ adsense_link` |  `[Google\Analytics\Admin\V1alpha\AdSenseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AdSenseLink)`   
A snapshot of an AdSenseLink resource in change history.  
`↳ audience` |  `[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)`   
A snapshot of an Audience resource in change history.  
`↳ event_create_rule` |  `[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)`   
A snapshot of an EventCreateRule resource in change history.  
`↳ key_event` |  `[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)`   
A snapshot of a KeyEvent resource in change history.  
`↳ calculated_metric` |  `[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)`   
A snapshot of a CalculatedMetric resource in change history.  
`↳ reporting_data_annotation` |  `[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)`   
A snapshot of a ReportingDataAnnotation resource in change history.  
`↳ subproperty_sync_config` |  `[Google\Analytics\Admin\V1alpha\SubpropertySyncConfig](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertySyncConfig)`   
A snapshot of a SubpropertySyncConfig resource in change history.  
`↳ reporting_identity_settings` |  `[Google\Analytics\Admin\V1alpha\ReportingIdentitySettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingIdentitySettings)`   
A snapshot of a ReportingIdentitySettings resource in change history.  
`↳ user_provided_data_settings` |  `[Google\Analytics\Admin\V1alpha\UserProvidedDataSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UserProvidedDataSettings)`   
A snapshot of a UserProvidedDataSettings resource in change history.  
  
### getAccount

A snapshot of an Account resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Account](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Account)|null` |   
  
### hasAccount

### setAccount

A snapshot of an Account resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\Account](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Account)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProperty

A snapshot of a Property resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)|null` |   
  
### hasProperty

### setProperty

A snapshot of a Property resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFirebaseLink

A snapshot of a FirebaseLink resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\FirebaseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.FirebaseLink)|null` |   
  
### hasFirebaseLink

### setFirebaseLink

A snapshot of a FirebaseLink resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\FirebaseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.FirebaseLink)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGoogleAdsLink

A snapshot of a GoogleAdsLink resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink)|null` |   
  
### hasGoogleAdsLink

### setGoogleAdsLink

A snapshot of a GoogleAdsLink resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGoogleSignalsSettings

A snapshot of a GoogleSignalsSettings resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\GoogleSignalsSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleSignalsSettings)|null` |   
  
### hasGoogleSignalsSettings

### setGoogleSignalsSettings

A snapshot of a GoogleSignalsSettings resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\GoogleSignalsSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleSignalsSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayVideo360AdvertiserLink

A snapshot of a DisplayVideo360AdvertiserLink resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)|null` |   
  
### hasDisplayVideo360AdvertiserLink

### setDisplayVideo360AdvertiserLink

A snapshot of a DisplayVideo360AdvertiserLink resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayVideo360AdvertiserLinkProposal

A snapshot of a DisplayVideo360AdvertiserLinkProposal resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)|null` |   
  
### hasDisplayVideo360AdvertiserLinkProposal

### setDisplayVideo360AdvertiserLinkProposal

A snapshot of a DisplayVideo360AdvertiserLinkProposal resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getConversionEvent

A snapshot of a ConversionEvent resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)|null` |   
  
### hasConversionEvent

### setConversionEvent

A snapshot of a ConversionEvent resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMeasurementProtocolSecret

A snapshot of a MeasurementProtocolSecret resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)|null` |   
  
### hasMeasurementProtocolSecret

### setMeasurementProtocolSecret

A snapshot of a MeasurementProtocolSecret resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCustomDimension

A snapshot of a CustomDimension resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)|null` |   
  
### hasCustomDimension

### setCustomDimension

A snapshot of a CustomDimension resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCustomMetric

A snapshot of a CustomMetric resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)|null` |   
  
### hasCustomMetric

### setCustomMetric

A snapshot of a CustomMetric resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataRetentionSettings

A snapshot of a data retention settings resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataRetentionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings)|null` |   
  
### hasDataRetentionSettings

### setDataRetentionSettings

A snapshot of a data retention settings resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\DataRetentionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSearchAds360Link

A snapshot of a SearchAds360Link resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)|null` |   
  
### hasSearchAds360Link

### setSearchAds360Link

A snapshot of a SearchAds360Link resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataStream

A snapshot of a DataStream resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)|null` |   
  
### hasDataStream

### setDataStream

A snapshot of a DataStream resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAttributionSettings

A snapshot of AttributionSettings resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AttributionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings)|null` |   
  
### hasAttributionSettings

### setAttributionSettings

A snapshot of AttributionSettings resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\AttributionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpandedDataSet

A snapshot of an ExpandedDataSet resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)|null` |   
  
### hasExpandedDataSet

### setExpandedDataSet

A snapshot of an ExpandedDataSet resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getChannelGroup

A snapshot of a ChannelGroup resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)|null` |   
  
### hasChannelGroup

### setChannelGroup

A snapshot of a ChannelGroup resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBigqueryLink

A snapshot of a BigQuery link resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)|null` |   
  
### hasBigqueryLink

### setBigqueryLink

A snapshot of a BigQuery link resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEnhancedMeasurementSettings

A snapshot of EnhancedMeasurementSettings resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings)|null` |   
  
### hasEnhancedMeasurementSettings

### setEnhancedMeasurementSettings

A snapshot of EnhancedMeasurementSettings resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataRedactionSettings

A snapshot of DataRedactionSettings resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataRedactionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRedactionSettings)|null` |   
  
### hasDataRedactionSettings

### setDataRedactionSettings

A snapshot of DataRedactionSettings resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\DataRedactionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRedactionSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSkadnetworkConversionValueSchema

A snapshot of SKAdNetworkConversionValueSchema resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)|null` |   
  
### hasSkadnetworkConversionValueSchema

### setSkadnetworkConversionValueSchema

A snapshot of SKAdNetworkConversionValueSchema resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdsenseLink

A snapshot of an AdSenseLink resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AdSenseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AdSenseLink)|null` |   
  
### hasAdsenseLink

### setAdsenseLink

A snapshot of an AdSenseLink resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\AdSenseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AdSenseLink)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAudience

A snapshot of an Audience resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)|null` |   
  
### hasAudience

### setAudience

A snapshot of an Audience resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventCreateRule

A snapshot of an EventCreateRule resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)|null` |   
  
### hasEventCreateRule

### setEventCreateRule

A snapshot of an EventCreateRule resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getKeyEvent

A snapshot of a KeyEvent resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)|null` |   
  
### hasKeyEvent

### setKeyEvent

A snapshot of a KeyEvent resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCalculatedMetric

A snapshot of a CalculatedMetric resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)|null` |   
  
### hasCalculatedMetric

### setCalculatedMetric

A snapshot of a CalculatedMetric resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReportingDataAnnotation

A snapshot of a ReportingDataAnnotation resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)|null` |   
  
### hasReportingDataAnnotation

### setReportingDataAnnotation

A snapshot of a ReportingDataAnnotation resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSubpropertySyncConfig

A snapshot of a SubpropertySyncConfig resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SubpropertySyncConfig](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertySyncConfig)|null` |   
  
### hasSubpropertySyncConfig

### setSubpropertySyncConfig

A snapshot of a SubpropertySyncConfig resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\SubpropertySyncConfig](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertySyncConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReportingIdentitySettings

A snapshot of a ReportingIdentitySettings resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ReportingIdentitySettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingIdentitySettings)|null` |   
  
### hasReportingIdentitySettings

### setReportingIdentitySettings

A snapshot of a ReportingIdentitySettings resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\ReportingIdentitySettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingIdentitySettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUserProvidedDataSettings

A snapshot of a UserProvidedDataSettings resource in change history.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\UserProvidedDataSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UserProvidedDataSettings)|null` |   
  
### hasUserProvidedDataSettings

### setUserProvidedDataSettings

A snapshot of a UserProvidedDataSettings resource in change history.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\UserProvidedDataSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UserProvidedDataSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResource

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
