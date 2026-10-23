---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/evaluate/
title: Evaluate result and quality \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:46.742018+00:00
---

# Evaluate result and quality  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/evaluate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Evaluate result and quality Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this product as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Understand the result

Enterprise Knowledge Graph writes results into a new BigQuery table for every job. This is a snapshot of the data at the time the job is executed. By default, every job generates a random `cluster_id` for each entity cluster. However, if you want to keep the ID stable among different job runs, use the `previous BigQuery result table` advanced option.

![Examine the result table](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/result_bq_table.png)

**Key Point:** The reconciliation confidence score can help you evaluate records that are less likely in the same entity cluster. For information about how the confidence scores are calculated, see [Understand the reconciliation confidence score](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/confidence-score). 

### Output Schema

Field name | Type | Description  
---|---|---  
cluster_id | STRING | This cluster ID is a private knowledge graph machine ID (MID) assigned to this cluster of records. It can be used to uniquely identify the record in your dataset. You can use the **Previous BigQuery table** in the Advanced Options to keep this `cluster_id` stable and consistent across multiple runs.  
source_name | STRING | The source name specified in the input configuration, to help you join dataset together.  
source_key | STRING | The unique key in your source table, to help you join dataset together.  
confidence | FLOAT | Confidence score that determines how strongly these records belong to this cluster.  
assignment_age | INTEGER | Used internally for cluster_id (MID) stabilization across different jobs.  
cloud_kg_mid | STRING | The Google Cloud Knowledge Graph linked entity MID. You could use this MID as your permanent ID or look up additional details from Cloud Knowledge Graph API.  
  
**Key Point:** Use [Cloud Knowledge Graph API](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/search-api) to look up the cloud_kg_mid that can help you further disambiguate the entity. **Note:** The Cloud Knowledge Graph API only links places and point of interest today. The linking will expand to more entities soon.

## Use SQL to join the dataset together

Enterprise Knowledge Graph outputs grouped entities by cluster ID. The simplest way to view the result is by using the cluster ID to "group by" your result. The following example performs a quick sanity check by joining the output table with the original table.
    
    
    # get all entity clusters
    SELECT distinct (cluster_id) FROM `ekg-test.<dataset>.clusters_9425187210682344597` order by cluster_id LIMIT 1000;
     
    # join data with original table
    SELECT confidence, RS., SRC. FROM `ekg-test.<dataset>.clusters_9425187210682344597` as RS join `ekg-api-test.demo.organization` as SRC
    on RS.source_key = SRC.source_key where cluster_id = "r-02b72jsgrbws18";
    

This entity cluster represents two different records that belong to the same cluster. This same `cluster_id` signals that these two records should be joined and merged.

![Use SQL to join the results](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/joint_bq_table.png)

## Measure success

**Pair-wise**

  * Precision: Ratio of distinct entities incorrectly identified as similar false positives (easier to detect by manual inspection).

  * Recall: Ratio of similar entities that aren't identified as false negatives or harder to detect.




**Cluster V-measure**

  * Cluster V-measure: (1 + beta) * homogeneity * completeness / (beta * homogeneity + completeness) where beta=1.

  * Cluster Homogeneity: Ratio of clusters that have entities belonging to the same entity.

  * Cluster Completeness: Ratio of clusters in which all entities belonging to the same entity are placed into the same cluster.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
