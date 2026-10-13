---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.DeltaPresenceEstimationConfigOrBuilder
title: Interface PrivacyMetric.DeltaPresenceEstimationConfigOrBuilder (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:41.751248+00:00
---

# Interface PrivacyMetric.DeltaPresenceEstimationConfigOrBuilder (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrivacyMetric.DeltaPresenceEstimationConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PrivacyMetric.DeltaPresenceEstimationConfigOrBuilder (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.7  3.5.0  3.4.0  3.3.2  3.2.1  3.1.4 
    
    
    public static interface PrivacyMetric.DeltaPresenceEstimationConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuxiliaryTables(int index)
    
    
    public abstract StatisticalTable getAuxiliaryTables(int index)

Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers field must appear in exactly one field of one auxiliary table.

`repeated .google.privacy.dlp.v2.StatisticalTable auxiliary_tables = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StatisticalTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StatisticalTable)` |   
  
### getAuxiliaryTablesCount()
    
    
    public abstract int getAuxiliaryTablesCount()

Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers field must appear in exactly one field of one auxiliary table.

`repeated .google.privacy.dlp.v2.StatisticalTable auxiliary_tables = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAuxiliaryTablesList()
    
    
    public abstract List<StatisticalTable> getAuxiliaryTablesList()

Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers field must appear in exactly one field of one auxiliary table.

`repeated .google.privacy.dlp.v2.StatisticalTable auxiliary_tables = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StatisticalTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StatisticalTable)>` |   
  
### getAuxiliaryTablesOrBuilder(int index)
    
    
    public abstract StatisticalTableOrBuilder getAuxiliaryTablesOrBuilder(int index)

Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers field must appear in exactly one field of one auxiliary table.

`repeated .google.privacy.dlp.v2.StatisticalTable auxiliary_tables = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StatisticalTableOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StatisticalTableOrBuilder)` |   
  
### getAuxiliaryTablesOrBuilderList()
    
    
    public abstract List<? extends StatisticalTableOrBuilder> getAuxiliaryTablesOrBuilderList()

Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers field must appear in exactly one field of one auxiliary table.

`repeated .google.privacy.dlp.v2.StatisticalTable auxiliary_tables = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.privacy.dlp.v2.StatisticalTableOrBuilder>` |   
  
### getQuasiIds(int index)
    
    
    public abstract QuasiId getQuasiIds(int index)

Required. Fields considered to be quasi-identifiers. No two fields can have the same tag.

` repeated .google.privacy.dlp.v2.QuasiId quasi_ids = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuasiId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.QuasiId)` |   
  
### getQuasiIdsCount()
    
    
    public abstract int getQuasiIdsCount()

Required. Fields considered to be quasi-identifiers. No two fields can have the same tag.

` repeated .google.privacy.dlp.v2.QuasiId quasi_ids = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getQuasiIdsList()
    
    
    public abstract List<QuasiId> getQuasiIdsList()

Required. Fields considered to be quasi-identifiers. No two fields can have the same tag.

` repeated .google.privacy.dlp.v2.QuasiId quasi_ids = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[QuasiId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.QuasiId)>` |   
  
### getQuasiIdsOrBuilder(int index)
    
    
    public abstract QuasiIdOrBuilder getQuasiIdsOrBuilder(int index)

Required. Fields considered to be quasi-identifiers. No two fields can have the same tag.

` repeated .google.privacy.dlp.v2.QuasiId quasi_ids = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuasiIdOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.QuasiIdOrBuilder)` |   
  
### getQuasiIdsOrBuilderList()
    
    
    public abstract List<? extends QuasiIdOrBuilder> getQuasiIdsOrBuilderList()

Required. Fields considered to be quasi-identifiers. No two fields can have the same tag.

` repeated .google.privacy.dlp.v2.QuasiId quasi_ids = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.privacy.dlp.v2.QuasiIdOrBuilder>` |   
  
### getRegionCode()
    
    
    public abstract String getRegionCode()

ISO 3166-1 alpha-2 region code to use in the statistical modeling. Set if no column is tagged with a region-specific InfoType (like US_ZIP_5) or a region code.

`string region_code = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The regionCode.  
  
### getRegionCodeBytes()
    
    
    public abstract ByteString getRegionCodeBytes()

ISO 3166-1 alpha-2 region code to use in the statistical modeling. Set if no column is tagged with a region-specific InfoType (like US_ZIP_5) or a region code.

`string region_code = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for regionCode.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
