---
url: https://docs.cloud.google.com/bigquery/docs/best-practices-policy-tags/
title: Best practices for using policy tags in BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:46:55.938161+00:00
---

# Best practices for using policy tags in BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/best-practices-policy-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Best practices for using policy tags in BigQuery

Policy tags in BigQuery let you enforce [column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) and [dynamic data masking](https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro) on sensitive table data. Structuring policy tags into a hierarchical taxonomy helps you manage permissions across numerous columns with a minimal set of classifications. Policy tags are an alternative to [data governance tags](https://docs.cloud.google.com/bigquery/docs/tags#data-governance-tags). To apply policy tags directly to columns, see [Set a policy tag on a column](https://docs.cloud.google.com/bigquery/docs/column-level-security#set_policy).

## Build a hierarchy of data classes

Build a hierarchy of data classes that makes sense for your business.

First, consider what kinds of data the organization processes. Usually there are a small number of data classes managed by an organization. For example, an organization could have data classes such as:

  * PII data
  * Financial data
  * Customer order history



A single data class can be applied to multiple data columns using a policy tag. You should use this level of abstraction to efficiently manage many columns with only a few policy tags.

Second, consider if there are groups of people who need different access to different data classes. For example, one group needs access to business- sensitive data such as revenues and customer history. Another group needs access to personally identifiable data (PII) like phone numbers and addresses.

Keep in mind that you can group policy tags together in a tree. Sometimes it is helpful to create a root policy tag that contains all of the other policy tags.

The following figure shows an example taxonomy. This hierarchy groups all data types into three top-level policy tags: **High** , **Medium** , and **Low**.

![Data hierarchy.](https://docs.cloud.google.com/static/bigquery/images/data-hierarchy.png)

Each of the top-level policy tags contains leaf policy tags. For example, the **High** policy tag contains the **Credit card** , **Government ID** , and **Biometric** policy tags. The **Medium** and **Low** similarly have leaf policy tags.

This structure has several benefits:

  * You can grant access to an entire group of policy tags at once. For example, you can grant the Data Catalog Fine-Grained Reader role on the **Low** tier.

  * You can move policy tags from one tier to another. For example, you can move **Address** from the **Low** tier to the **Medium** tier to further restrict its access, without needing to reclassify all **Address** columns. **Note:** You can move a policy tag only through the Data Catalog `PolicyTagManager.UpdatePolicyTag` method.

  * With this fine-grained access, you can manage access to many columns by controlling only a small number of data classification policy tags.




For more information about policy tags in BigQuery, see:

  * [Introduction to column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro)
  * [Restricting access with column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security)
  * [Introduction to dynamic data masking](https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro)
  * [Mask column data by user role](https://docs.cloud.google.com/bigquery/docs/column-data-masking)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
