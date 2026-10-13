---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinitionOrBuilder
title: Interface ReportDefinitionOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:36.499445+00:00
---

# Interface ReportDefinitionOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinitionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReportDefinitionOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ReportDefinitionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCmsMetadataDimensionKeyIds(int index)
    
    
    public abstract long getCmsMetadataDimensionKeyIds(int index)

Optional. CMS Metadata Dimension keys that represent CMS_METADATA_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, cms_metadata_dimension_key_ids[0] describes CMS_METADATA_DIMENSION_0_VALUE_ID and CMS_METADATA_DIMENSION_0_VALUE.

` repeated int64 cms_metadata_dimension_key_ids = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cmsMetadataDimensionKeyIds at the given index.  
  
### getCmsMetadataDimensionKeyIdsCount()
    
    
    public abstract int getCmsMetadataDimensionKeyIdsCount()

Optional. CMS Metadata Dimension keys that represent CMS_METADATA_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, cms_metadata_dimension_key_ids[0] describes CMS_METADATA_DIMENSION_0_VALUE_ID and CMS_METADATA_DIMENSION_0_VALUE.

` repeated int64 cms_metadata_dimension_key_ids = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of cmsMetadataDimensionKeyIds.  
  
### getCmsMetadataDimensionKeyIdsList()
    
    
    public abstract List<Long> getCmsMetadataDimensionKeyIdsList()

Optional. CMS Metadata Dimension keys that represent CMS_METADATA_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, cms_metadata_dimension_key_ids[0] describes CMS_METADATA_DIMENSION_0_VALUE_ID and CMS_METADATA_DIMENSION_0_VALUE.

` repeated int64 cms_metadata_dimension_key_ids = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the cmsMetadataDimensionKeyIds.  
  
### getComparisonDateRange()
    
    
    public abstract ReportDefinition.DateRange getComparisonDateRange()

Optional. The comparison date range of this report. If unspecified, the report won't have any comparison metrics.

` optional .google.ads.admanager.v1.ReportDefinition.DateRange comparison_date_range = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.DateRange](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.DateRange)` | The comparisonDateRange.  
  
### getComparisonDateRangeOrBuilder()
    
    
    public abstract ReportDefinition.DateRangeOrBuilder getComparisonDateRangeOrBuilder()

Optional. The comparison date range of this report. If unspecified, the report won't have any comparison metrics.

` optional .google.ads.admanager.v1.ReportDefinition.DateRange comparison_date_range = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.DateRangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.DateRangeOrBuilder)` |   
  
### getCreativeCustomFieldIds(int index)
    
    
    public abstract long getCreativeCustomFieldIds(int index)

Optional. Custom field IDs that represent CREATIVE_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, creative_custom_field_ids[0] describes CREATIVE_CUSTOM_FIELD_0_OPTION_ID and CREATIVE_CUSTOM_FIELD_0_VALUE.

`repeated int64 creative_custom_field_ids = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The creativeCustomFieldIds at the given index.  
  
### getCreativeCustomFieldIdsCount()
    
    
    public abstract int getCreativeCustomFieldIdsCount()

Optional. Custom field IDs that represent CREATIVE_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, creative_custom_field_ids[0] describes CREATIVE_CUSTOM_FIELD_0_OPTION_ID and CREATIVE_CUSTOM_FIELD_0_VALUE.

`repeated int64 creative_custom_field_ids = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of creativeCustomFieldIds.  
  
### getCreativeCustomFieldIdsList()
    
    
    public abstract List<Long> getCreativeCustomFieldIdsList()

Optional. Custom field IDs that represent CREATIVE_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, creative_custom_field_ids[0] describes CREATIVE_CUSTOM_FIELD_0_OPTION_ID and CREATIVE_CUSTOM_FIELD_0_VALUE.

`repeated int64 creative_custom_field_ids = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the creativeCustomFieldIds.  
  
### getCurrencyCode()
    
    
    public abstract String getCurrencyCode()

Optional. The ISO 4217 currency code for this report. Defaults to publisher currency code if not specified.

`string currency_code = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The currencyCode.  
  
### getCurrencyCodeBytes()
    
    
    public abstract ByteString getCurrencyCodeBytes()

Optional. The ISO 4217 currency code for this report. Defaults to publisher currency code if not specified.

`string currency_code = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for currencyCode.  
  
### getCustomDimensionKeyIds(int index)
    
    
    public abstract long getCustomDimensionKeyIds(int index)

Optional. Custom Dimension keys that represent CUSTOM_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, custom_dimension_key_ids[0] describes CUSTOM_DIMENSION_0_VALUE_ID and CUSTOM_DIMENSION_0_VALUE.

`repeated int64 custom_dimension_key_ids = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The customDimensionKeyIds at the given index.  
  
### getCustomDimensionKeyIdsCount()
    
    
    public abstract int getCustomDimensionKeyIdsCount()

Optional. Custom Dimension keys that represent CUSTOM_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, custom_dimension_key_ids[0] describes CUSTOM_DIMENSION_0_VALUE_ID and CUSTOM_DIMENSION_0_VALUE.

`repeated int64 custom_dimension_key_ids = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of customDimensionKeyIds.  
  
### getCustomDimensionKeyIdsList()
    
    
    public abstract List<Long> getCustomDimensionKeyIdsList()

Optional. Custom Dimension keys that represent CUSTOM_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, custom_dimension_key_ids[0] describes CUSTOM_DIMENSION_0_VALUE_ID and CUSTOM_DIMENSION_0_VALUE.

`repeated int64 custom_dimension_key_ids = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the customDimensionKeyIds.  
  
### getDateRange()
    
    
    public abstract ReportDefinition.DateRange getDateRange()

Required. The primary date range of this report.

` .google.ads.admanager.v1.ReportDefinition.DateRange date_range = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.DateRange](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.DateRange)` | The dateRange.  
  
### getDateRangeOrBuilder()
    
    
    public abstract ReportDefinition.DateRangeOrBuilder getDateRangeOrBuilder()

Required. The primary date range of this report.

` .google.ads.admanager.v1.ReportDefinition.DateRange date_range = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.DateRangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.DateRangeOrBuilder)` |   
  
### getDimensions(int index)
    
    
    public abstract ReportDefinition.Dimension getDimensions(int index)

Required. The list of dimensions to report on. If empty, the report will have no dimensions, and any metrics will be totals.

` repeated .google.ads.admanager.v1.ReportDefinition.Dimension dimensions = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.Dimension](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Dimension)` | The dimensions at the given index.  
  
### getDimensionsCount()
    
    
    public abstract int getDimensionsCount()

Required. The list of dimensions to report on. If empty, the report will have no dimensions, and any metrics will be totals.

` repeated .google.ads.admanager.v1.ReportDefinition.Dimension dimensions = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of dimensions.  
  
### getDimensionsList()
    
    
    public abstract List<ReportDefinition.Dimension> getDimensionsList()

Required. The list of dimensions to report on. If empty, the report will have no dimensions, and any metrics will be totals.

` repeated .google.ads.admanager.v1.ReportDefinition.Dimension dimensions = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Dimension](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Dimension)>` | A list containing the dimensions.  
  
### getDimensionsValue(int index)
    
    
    public abstract int getDimensionsValue(int index)

Required. The list of dimensions to report on. If empty, the report will have no dimensions, and any metrics will be totals.

` repeated .google.ads.admanager.v1.ReportDefinition.Dimension dimensions = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of dimensions at the given index.  
  
### getDimensionsValueList()
    
    
    public abstract List<Integer> getDimensionsValueList()

Required. The list of dimensions to report on. If empty, the report will have no dimensions, and any metrics will be totals.

` repeated .google.ads.admanager.v1.ReportDefinition.Dimension dimensions = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for dimensions.  
  
### getEkvDimensionKeyIds(int index)
    
    
    public abstract long getEkvDimensionKeyIds(int index)

Optional. Enhanced Key-values Dimension keys that represent EKV_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, ekv_dimension_key_ids[0] describes EKV_DIMENSION_0_VALUE_ID and EKV_DIMENSION_0_VALUE.

`repeated int64 ekv_dimension_key_ids = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ekvDimensionKeyIds at the given index.  
  
### getEkvDimensionKeyIdsCount()
    
    
    public abstract int getEkvDimensionKeyIdsCount()

Optional. Enhanced Key-values Dimension keys that represent EKV_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, ekv_dimension_key_ids[0] describes EKV_DIMENSION_0_VALUE_ID and EKV_DIMENSION_0_VALUE.

`repeated int64 ekv_dimension_key_ids = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of ekvDimensionKeyIds.  
  
### getEkvDimensionKeyIdsList()
    
    
    public abstract List<Long> getEkvDimensionKeyIdsList()

Optional. Enhanced Key-values Dimension keys that represent EKV_DIMENSION_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, ekv_dimension_key_ids[0] describes EKV_DIMENSION_0_VALUE_ID and EKV_DIMENSION_0_VALUE.

`repeated int64 ekv_dimension_key_ids = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the ekvDimensionKeyIds.  
  
### getExpandedCompatibility()
    
    
    public abstract boolean getExpandedCompatibility()

Optional. Whether to use expanded compatibility for this report.

If true, this setting enables certain combinations of dimensions and metrics for this report that would otherwise be incompatible. Enabling this will collapse reservation data into a single row even if the report's dimensions would normally result in multiple rows for reservation data. This impacts dimensions related to line items, orders, creatives, and advertisers.

This is equivalent to the "Access more dimension and metric combinations" setting in the Interactive Reports UI. For more details, see: <https://support.google.com/admanager/answer/16865393#combinations>

`bool expanded_compatibility = 22 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The expandedCompatibility.  
  
### getFilters(int index)
    
    
    public abstract ReportDefinition.Filter getFilters(int index)

Optional. The filters for this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Filter filters = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.Filter](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Filter)` |   
  
### getFiltersCount()
    
    
    public abstract int getFiltersCount()

Optional. The filters for this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Filter filters = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFiltersList()
    
    
    public abstract List<ReportDefinition.Filter> getFiltersList()

Optional. The filters for this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Filter filters = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Filter](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Filter)>` |   
  
### getFiltersOrBuilder(int index)
    
    
    public abstract ReportDefinition.FilterOrBuilder getFiltersOrBuilder(int index)

Optional. The filters for this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Filter filters = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.FilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.FilterOrBuilder)` |   
  
### getFiltersOrBuilderList()
    
    
    public abstract List<? extends ReportDefinition.FilterOrBuilder> getFiltersOrBuilderList()

Optional. The filters for this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Filter filters = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.ads.admanager.v1.ReportDefinition.FilterOrBuilder>` |   
  
### getFlags(int index)
    
    
    public abstract ReportDefinition.Flag getFlags(int index)

Optional. List of flags for this report. Used to flag rows in a result set based on a set of defined filters.

` repeated .google.ads.admanager.v1.ReportDefinition.Flag flags = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.Flag](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Flag)` |   
  
### getFlagsCount()
    
    
    public abstract int getFlagsCount()

Optional. List of flags for this report. Used to flag rows in a result set based on a set of defined filters.

` repeated .google.ads.admanager.v1.ReportDefinition.Flag flags = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFlagsList()
    
    
    public abstract List<ReportDefinition.Flag> getFlagsList()

Optional. List of flags for this report. Used to flag rows in a result set based on a set of defined filters.

` repeated .google.ads.admanager.v1.ReportDefinition.Flag flags = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Flag](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Flag)>` |   
  
### getFlagsOrBuilder(int index)
    
    
    public abstract ReportDefinition.FlagOrBuilder getFlagsOrBuilder(int index)

Optional. List of flags for this report. Used to flag rows in a result set based on a set of defined filters.

` repeated .google.ads.admanager.v1.ReportDefinition.Flag flags = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.FlagOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.FlagOrBuilder)` |   
  
### getFlagsOrBuilderList()
    
    
    public abstract List<? extends ReportDefinition.FlagOrBuilder> getFlagsOrBuilderList()

Optional. List of flags for this report. Used to flag rows in a result set based on a set of defined filters.

` repeated .google.ads.admanager.v1.ReportDefinition.Flag flags = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.ads.admanager.v1.ReportDefinition.FlagOrBuilder>` |   
  
### getLineItemCustomFieldIds(int index)
    
    
    public abstract long getLineItemCustomFieldIds(int index)

Optional. Custom field IDs that represent LINE_ITEM_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, line_item_custom_field_ids[0] describes LINE_ITEM_CUSTOM_FIELD_0_OPTION_ID and LINE_ITEM_CUSTOM_FIELD_0_VALUE.

`repeated int64 line_item_custom_field_ids = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The lineItemCustomFieldIds at the given index.  
  
### getLineItemCustomFieldIdsCount()
    
    
    public abstract int getLineItemCustomFieldIdsCount()

Optional. Custom field IDs that represent LINE_ITEM_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, line_item_custom_field_ids[0] describes LINE_ITEM_CUSTOM_FIELD_0_OPTION_ID and LINE_ITEM_CUSTOM_FIELD_0_VALUE.

`repeated int64 line_item_custom_field_ids = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of lineItemCustomFieldIds.  
  
### getLineItemCustomFieldIdsList()
    
    
    public abstract List<Long> getLineItemCustomFieldIdsList()

Optional. Custom field IDs that represent LINE_ITEM_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, line_item_custom_field_ids[0] describes LINE_ITEM_CUSTOM_FIELD_0_OPTION_ID and LINE_ITEM_CUSTOM_FIELD_0_VALUE.

`repeated int64 line_item_custom_field_ids = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the lineItemCustomFieldIds.  
  
### getMetrics(int index)
    
    
    public abstract ReportDefinition.Metric getMetrics(int index)

Required. The list of metrics to report on. If empty, the report will have no metrics.

` repeated .google.ads.admanager.v1.ReportDefinition.Metric metrics = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.Metric](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Metric)` | The metrics at the given index.  
  
### getMetricsCount()
    
    
    public abstract int getMetricsCount()

Required. The list of metrics to report on. If empty, the report will have no metrics.

` repeated .google.ads.admanager.v1.ReportDefinition.Metric metrics = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of metrics.  
  
### getMetricsList()
    
    
    public abstract List<ReportDefinition.Metric> getMetricsList()

Required. The list of metrics to report on. If empty, the report will have no metrics.

` repeated .google.ads.admanager.v1.ReportDefinition.Metric metrics = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Metric)>` | A list containing the metrics.  
  
### getMetricsValue(int index)
    
    
    public abstract int getMetricsValue(int index)

Required. The list of metrics to report on. If empty, the report will have no metrics.

` repeated .google.ads.admanager.v1.ReportDefinition.Metric metrics = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of metrics at the given index.  
  
### getMetricsValueList()
    
    
    public abstract List<Integer> getMetricsValueList()

Required. The list of metrics to report on. If empty, the report will have no metrics.

` repeated .google.ads.admanager.v1.ReportDefinition.Metric metrics = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for metrics.  
  
### getOrderCustomFieldIds(int index)
    
    
    public abstract long getOrderCustomFieldIds(int index)

Optional. Custom field IDs that represent ORDER_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, order_custom_field_ids[0] describes ORDER_CUSTOM_FIELD_0_OPTION_ID and ORDER_CUSTOM_FIELD_0_VALUE.

`repeated int64 order_custom_field_ids = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The orderCustomFieldIds at the given index.  
  
### getOrderCustomFieldIdsCount()
    
    
    public abstract int getOrderCustomFieldIdsCount()

Optional. Custom field IDs that represent ORDER_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, order_custom_field_ids[0] describes ORDER_CUSTOM_FIELD_0_OPTION_ID and ORDER_CUSTOM_FIELD_0_VALUE.

`repeated int64 order_custom_field_ids = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of orderCustomFieldIds.  
  
### getOrderCustomFieldIdsList()
    
    
    public abstract List<Long> getOrderCustomFieldIdsList()

Optional. Custom field IDs that represent ORDER_CUSTOM_FIELD_* dimensions. The index of this repeated field corresponds to the index on each dimension. For example, order_custom_field_ids[0] describes ORDER_CUSTOM_FIELD_0_OPTION_ID and ORDER_CUSTOM_FIELD_0_VALUE.

`repeated int64 order_custom_field_ids = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the orderCustomFieldIds.  
  
### getReportType()
    
    
    public abstract ReportDefinition.ReportType getReportType()

Required. The type of this report.

` .google.ads.admanager.v1.ReportDefinition.ReportType report_type = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.ReportType](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.ReportType)` | The reportType.  
  
### getReportTypeValue()
    
    
    public abstract int getReportTypeValue()

Required. The type of this report.

` .google.ads.admanager.v1.ReportDefinition.ReportType report_type = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for reportType.  
  
### getSorts(int index)
    
    
    public abstract ReportDefinition.Sort getSorts(int index)

Optional. Default sorts to apply to this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Sort sorts = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.Sort](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Sort)` |   
  
### getSortsCount()
    
    
    public abstract int getSortsCount()

Optional. Default sorts to apply to this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Sort sorts = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSortsList()
    
    
    public abstract List<ReportDefinition.Sort> getSortsList()

Optional. Default sorts to apply to this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Sort sorts = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Sort](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.Sort)>` |   
  
### getSortsOrBuilder(int index)
    
    
    public abstract ReportDefinition.SortOrBuilder getSortsOrBuilder(int index)

Optional. Default sorts to apply to this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Sort sorts = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.SortOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.SortOrBuilder)` |   
  
### getSortsOrBuilderList()
    
    
    public abstract List<? extends ReportDefinition.SortOrBuilder> getSortsOrBuilderList()

Optional. Default sorts to apply to this report.

` repeated .google.ads.admanager.v1.ReportDefinition.Sort sorts = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.ads.admanager.v1.ReportDefinition.SortOrBuilder>` |   
  
### getTimePeriodColumn()
    
    
    public abstract ReportDefinition.TimePeriodColumn getTimePeriodColumn()

Optional. Include a time period column to introduce comparison columns in the report for each generated period. For example, set to "QUARTERS" here to have a column for each quarter present in the primary date range. If "PREVIOUS PERIOD" is specified in comparison_date_range, then each quarter column will also include comparison values for its relative previous quarter.

` .google.ads.admanager.v1.ReportDefinition.TimePeriodColumn time_period_column = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.TimePeriodColumn](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.TimePeriodColumn)` | The timePeriodColumn.  
  
### getTimePeriodColumnValue()
    
    
    public abstract int getTimePeriodColumnValue()

Optional. Include a time period column to introduce comparison columns in the report for each generated period. For example, set to "QUARTERS" here to have a column for each quarter present in the primary date range. If "PREVIOUS PERIOD" is specified in comparison_date_range, then each quarter column will also include comparison values for its relative previous quarter.

` .google.ads.admanager.v1.ReportDefinition.TimePeriodColumn time_period_column = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for timePeriodColumn.  
  
### getTimeZone()
    
    
    public abstract String getTimeZone()

Optional. If time_zone_source is PROVIDED, this is the time zone to use for this report. Leave empty for any other time zone source. Time zone in IANA format. For example, "America/New_York".

`string time_zone = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The timeZone.  
  
### getTimeZoneBytes()
    
    
    public abstract ByteString getTimeZoneBytes()

Optional. If time_zone_source is PROVIDED, this is the time zone to use for this report. Leave empty for any other time zone source. Time zone in IANA format. For example, "America/New_York".

`string time_zone = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for timeZone.  
  
### getTimeZoneSource()
    
    
    public abstract ReportDefinition.TimeZoneSource getTimeZoneSource()

Optional. Where to get the time zone for this report. Defaults to using the network time zone setting (PUBLISHER). If source is PROVIDED, the time_zone field in the report definition must also set a time zone.

` .google.ads.admanager.v1.ReportDefinition.TimeZoneSource time_zone_source = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportDefinition.TimeZoneSource](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportDefinition.TimeZoneSource)` | The timeZoneSource.  
  
### getTimeZoneSourceValue()
    
    
    public abstract int getTimeZoneSourceValue()

Optional. Where to get the time zone for this report. Defaults to using the network time zone setting (PUBLISHER). If source is PROVIDED, the time_zone field in the report definition must also set a time zone.

` .google.ads.admanager.v1.ReportDefinition.TimeZoneSource time_zone_source = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for timeZoneSource.  
  
### hasComparisonDateRange()
    
    
    public abstract boolean hasComparisonDateRange()

Optional. The comparison date range of this report. If unspecified, the report won't have any comparison metrics.

` optional .google.ads.admanager.v1.ReportDefinition.DateRange comparison_date_range = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the comparisonDateRange field is set.  
  
### hasDateRange()
    
    
    public abstract boolean hasDateRange()

Required. The primary date range of this report.

` .google.ads.admanager.v1.ReportDefinition.DateRange date_range = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dateRange field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
