---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchOrBuilder
title: Interface BranchOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:38.745455+00:00
---

# Interface BranchOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BranchOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public interface BranchOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDisplayName()
    
    
    public abstract String getDisplayName()

Output only. Human readable name of the branch to display in the UI.

`string display_name = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Output only. Human readable name of the branch to display in the UI.

`string display_name = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getIsDefault()
    
    
    public abstract boolean getIsDefault()

Output only. Indicates whether this branch is set as the default branch of its parent catalog.

`bool is_default = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isDefault.  
  
### getLastProductImportTime()
    
    
    public abstract Timestamp getLastProductImportTime()

Output only. Timestamp of last import through ProductService.ImportProducts. Empty value means no import has been made to this branch.

` .google.protobuf.Timestamp last_product_import_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastProductImportTime.  
  
### getLastProductImportTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastProductImportTimeOrBuilder()

Output only. Timestamp of last import through ProductService.ImportProducts. Empty value means no import has been made to this branch.

` .google.protobuf.Timestamp last_product_import_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getName()
    
    
    public abstract String getName()

Immutable. Full resource name of the branch, such as `projects/*/locations/global/catalogs/default_catalog/branches/branch_id`.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Immutable. Full resource name of the branch, such as `projects/*/locations/global/catalogs/default_catalog/branches/branch_id`.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getProductCountStats(int index)
    
    
    public abstract Branch.ProductCountStatistic getProductCountStats(int index)

Output only. Statistics for number of products in the branch, provided for different scopes.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.ProductCountStatistic product_count_stats = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Branch.ProductCountStatistic](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch.ProductCountStatistic)` |   
  
### getProductCountStatsCount()
    
    
    public abstract int getProductCountStatsCount()

Output only. Statistics for number of products in the branch, provided for different scopes.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.ProductCountStatistic product_count_stats = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getProductCountStatsList()
    
    
    public abstract List<Branch.ProductCountStatistic> getProductCountStatsList()

Output only. Statistics for number of products in the branch, provided for different scopes.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.ProductCountStatistic product_count_stats = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProductCountStatistic](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch.ProductCountStatistic)>` |   
  
### getProductCountStatsOrBuilder(int index)
    
    
    public abstract Branch.ProductCountStatisticOrBuilder getProductCountStatsOrBuilder(int index)

Output only. Statistics for number of products in the branch, provided for different scopes.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.ProductCountStatistic product_count_stats = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Branch.ProductCountStatisticOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch.ProductCountStatisticOrBuilder)` |   
  
### getProductCountStatsOrBuilderList()
    
    
    public abstract List<? extends Branch.ProductCountStatisticOrBuilder> getProductCountStatsOrBuilderList()

Output only. Statistics for number of products in the branch, provided for different scopes.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.ProductCountStatistic product_count_stats = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.retail.v2alpha.Branch.ProductCountStatisticOrBuilder>` |   
  
### getQualityMetrics(int index)
    
    
    public abstract Branch.QualityMetric getQualityMetrics(int index)

Output only. The quality metrics measured among products of this branch.

See QualityMetric.requirement_key for supported metrics. Metrics could be missing if failed to retrieve.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.QualityMetric quality_metrics = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Branch.QualityMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch.QualityMetric)` |   
  
### getQualityMetricsCount()
    
    
    public abstract int getQualityMetricsCount()

Output only. The quality metrics measured among products of this branch.

See QualityMetric.requirement_key for supported metrics. Metrics could be missing if failed to retrieve.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.QualityMetric quality_metrics = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getQualityMetricsList()
    
    
    public abstract List<Branch.QualityMetric> getQualityMetricsList()

Output only. The quality metrics measured among products of this branch.

See QualityMetric.requirement_key for supported metrics. Metrics could be missing if failed to retrieve.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.QualityMetric quality_metrics = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[QualityMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch.QualityMetric)>` |   
  
### getQualityMetricsOrBuilder(int index)
    
    
    public abstract Branch.QualityMetricOrBuilder getQualityMetricsOrBuilder(int index)

Output only. The quality metrics measured among products of this branch.

See QualityMetric.requirement_key for supported metrics. Metrics could be missing if failed to retrieve.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.QualityMetric quality_metrics = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Branch.QualityMetricOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch.QualityMetricOrBuilder)` |   
  
### getQualityMetricsOrBuilderList()
    
    
    public abstract List<? extends Branch.QualityMetricOrBuilder> getQualityMetricsOrBuilderList()

Output only. The quality metrics measured among products of this branch.

See QualityMetric.requirement_key for supported metrics. Metrics could be missing if failed to retrieve.

This field is not populated in [BranchView.BASIC][] view.

` repeated .google.cloud.retail.v2alpha.Branch.QualityMetric quality_metrics = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.retail.v2alpha.Branch.QualityMetricOrBuilder>` |   
  
### hasLastProductImportTime()
    
    
    public abstract boolean hasLastProductImportTime()

Output only. Timestamp of last import through ProductService.ImportProducts. Empty value means no import has been made to this branch.

` .google.protobuf.Timestamp last_product_import_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastProductImportTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
