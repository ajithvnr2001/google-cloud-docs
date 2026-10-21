---
url: https://docs.cloud.google.com/bigtable/docs/authorized-views/
title: Authorized views overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:13.509816+00:00
---

# Authorized views overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/authorized-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authorized views overview

_Authorized views_ in Bigtable let you grant fine-grained access to specific subsets of table data separately from the underlying table.

You can use these views to isolate data in multi-tenant tables and control both read and write access. You can also create thousands of views programmatically, similar to updateable views or filtered aliases in other storage systems.

Before you begin, make sure that you're familiar with the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model). For setup instructions, see [Create and manage authorized views](https://docs.cloud.google.com/bigtable/docs/authorized-views-create-manage).

## What defines an authorized view

When you create an authorized view, you define it by specifying the data to include in the authorized view using one of the following parameters:

  * Row key prefix - for example, all rows that start with `examplepetstore1#`
  * Column qualifier prefix - for example, all columns whose qualifiers start with `order#` in the specified column family
  * Column qualifier - for example, only the `order-examplepetstore` column in the specified column family
  * A combination of row key prefix and column qualifier



If the same column qualifier is used in multiple column families and you want to include _all_ columns with that qualifier in the view, you must specify every combination of column qualifier and column family separately when you define the view.

The row key and column qualifier values that you use to define an authorized view are treated as service data. For this reason, don't create an authorized view using row key or column qualifier values that contain [sensitive information](https://docs.cloud.google.com/bigtable/docs/schema-design#privacy). For information about how service data is handled, see the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

### Inclusion of columns in a family or all rows

If you want to make sure that any column that is added to a column family in the underlying table is also included in your authorized view, then you should specify the empty string (`""`) as a column qualifier prefix. For example, a definition file would include this in the family subset: `"qualifierPrefixes": [""]`.

Similarly, if you want to define an authorized view that includes all rows in the table, specify the empty string (`""`) as a row key prefix. In a definition file, this is written as `"rowPrefixes": [""]` in the view subset.

To avoid excessively complex authorized views, Bigtable lets you specify at most 10 distinct qualifier prefixes. This means that an authorized view can specify one column family with 10 qualifier prefixes, 10 column families with a single qualifier prefix, or anywhere in between as long as the total number of qualifiers is at most 10.

As a best practice, specify a key only once per JSON object. If you specify a key, such as a column family name, more than once, the final entry for the key overwrites any previous entries for the key.

## Definition file examples

This section presents JSON-formatted examples of authorized view definition files.

The following is an example of a definition file for an authorized view that includes the `address` column of the `customer` column family and columns that begin with `tel` for rows with a row key prefix of `examplepetstore1#`.
    
    
        {
          "subsetView":
          {
            "rowPrefixes": ["examplepetstore1#"],
            "familySubsets":
            {
              "customer":
              {
                "qualifiers":["address"],
                "qualifierPrefixes":["tel"]
              }
            }
          },
          "deletionProtection": true
        }
    

The following is an example of a definition file for an authorized view that includes the `skus` column in the `order` column family and all columns in the `customer` column family.
    
    
        {
          "subsetView": {
            "rowPrefixes": [""],
            "familySubsets": {
              "order": {
                "qualifiers": ["skus"]
              },
              "customer": {
                "qualifierPrefixes": [""]
              }
            }
          }
        }
    

The following is an example of a definition file for an authorized view that includes only data in the `skus` column in the `order` column family in rows that have a row key prefix of `examplepetstore1#`.
    
    
        {
          "subsetView": {
            "rowPrefixes": ["examplepetstore1#"]
            "familySubsets": {
              "order": {
                "qualifiers": ["skus"]
              }
            }
          }
        }
    

The following is an example of a definition file for an authorized view that includes only data in the `skus` and `agents` columns in the `order` column family and the `dog`, `cat`, and `bird` columns in the `pet_id` column family.
    
    
        {
          "subsetView": {
            "rowPrefixes": [""]
            "familySubsets": {
              "order": {
                "qualifiers": ["skus", "agents"]
              "pet_id": {
                "qualifiers": ["dog", "cat", "bird"]
              }
              }
            }
          }
        }
    

## What's next

  * [Delete data through an authorized view.](https://docs.cloud.google.com/bigtable/docs/delete-data#delete-authorized-view)
  * [Learn how to tag Bigtable resources.](https://docs.cloud.google.com/bigtable/docs/tags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
