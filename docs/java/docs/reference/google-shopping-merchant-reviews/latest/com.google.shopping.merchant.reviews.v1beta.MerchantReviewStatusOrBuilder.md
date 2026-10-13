---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatusOrBuilder
title: Interface MerchantReviewStatusOrBuilder (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:35.323760+00:00
---

# Interface MerchantReviewStatusOrBuilder (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatusOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MerchantReviewStatusOrBuilder (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface MerchantReviewStatusOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Date on which the item has been created, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Date on which the item has been created, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDestinationStatuses(int index)
    
    
    public abstract MerchantReviewStatus.MerchantReviewDestinationStatus getDestinationStatuses(int index)

Output only. The intended destinations for the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatus destination_statuses = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewStatus.MerchantReviewDestinationStatus](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatus)` |   
  
### getDestinationStatusesCount()
    
    
    public abstract int getDestinationStatusesCount()

Output only. The intended destinations for the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatus destination_statuses = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDestinationStatusesList()
    
    
    public abstract List<MerchantReviewStatus.MerchantReviewDestinationStatus> getDestinationStatusesList()

Output only. The intended destinations for the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatus destination_statuses = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MerchantReviewDestinationStatus](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatus)>` |   
  
### getDestinationStatusesOrBuilder(int index)
    
    
    public abstract MerchantReviewStatus.MerchantReviewDestinationStatusOrBuilder getDestinationStatusesOrBuilder(int index)

Output only. The intended destinations for the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatus destination_statuses = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewStatus.MerchantReviewDestinationStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatusOrBuilder)` |   
  
### getDestinationStatusesOrBuilderList()
    
    
    public abstract List<? extends MerchantReviewStatus.MerchantReviewDestinationStatusOrBuilder> getDestinationStatusesOrBuilderList()

Output only. The intended destinations for the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatus destination_statuses = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatusOrBuilder>` |   
  
### getItemLevelIssues(int index)
    
    
    public abstract MerchantReviewStatus.MerchantReviewItemLevelIssue getItemLevelIssues(int index)

Output only. A list of all issues associated with the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssue item_level_issues = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewStatus.MerchantReviewItemLevelIssue](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssue)` |   
  
### getItemLevelIssuesCount()
    
    
    public abstract int getItemLevelIssuesCount()

Output only. A list of all issues associated with the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssue item_level_issues = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getItemLevelIssuesList()
    
    
    public abstract List<MerchantReviewStatus.MerchantReviewItemLevelIssue> getItemLevelIssuesList()

Output only. A list of all issues associated with the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssue item_level_issues = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MerchantReviewItemLevelIssue](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssue)>` |   
  
### getItemLevelIssuesOrBuilder(int index)
    
    
    public abstract MerchantReviewStatus.MerchantReviewItemLevelIssueOrBuilder getItemLevelIssuesOrBuilder(int index)

Output only. A list of all issues associated with the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssue item_level_issues = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewStatus.MerchantReviewItemLevelIssueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssueOrBuilder)` |   
  
### getItemLevelIssuesOrBuilderList()
    
    
    public abstract List<? extends MerchantReviewStatus.MerchantReviewItemLevelIssueOrBuilder> getItemLevelIssuesOrBuilderList()

Output only. A list of all issues associated with the merchant review.

` repeated .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssue item_level_issues = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssueOrBuilder>` |   
  
### getLastUpdateTime()
    
    
    public abstract Timestamp getLastUpdateTime()

Output only. Date on which the item has been last updated, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

` .google.protobuf.Timestamp last_update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastUpdateTime.  
  
### getLastUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastUpdateTimeOrBuilder()

Output only. Date on which the item has been last updated, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

` .google.protobuf.Timestamp last_update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Date on which the item has been created, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasLastUpdateTime()
    
    
    public abstract boolean hasLastUpdateTime()

Output only. Date on which the item has been last updated, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

` .google.protobuf.Timestamp last_update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastUpdateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
