---
url: https://docs.cloud.google.com/bigtable/docs/structured-row-key-queries/
title: Structured row key queries \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:29.492775+00:00
---

# Structured row key queries  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/structured-row-key-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Structured row key queries

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If a table has a row key schema that defines _structured row keys_ , you can use SQL to query the individual segments – or columns – of the row key.

Continuous materialized views, including asynchronous secondary indexes, generate structured row keys by default. You can also define a structured row key for any Bigtable table that you want to query with SQL by creating a _row key schema_ for the table. For more information, see [Manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas).

## Keys

In a Bigtable table without a structured row key schema, each row is indexed by a single row key. When you query the table with SQL, the row key is a column named `_key` that SQL uses as the primary key. It's not a pseudocolumn, so values in the `_key` column are returned when you execute a `SELECT *` query on the table.

On the other hand, in a table that has a row key schema, the row key (primary key) is the combination of all the columns named as fields in the row key schema. When you add a row key schema to a table, the `_key` column becomes a pseudocolumn, which means it won't show up in a `SELECT *` query, but you can select it explicitly with a `SELECT _key` statement.

**Important:** If any row keys in a table don't conform to the row key schema, queries that select structured row key columns fail and return an error.

## Sample queries

The examples in this section assume that a table named `sales` has the following schema:
    
    
      field {
        field_name: "user_id"
        type: { bytes_type { encoding { raw {} } } }
      }
      field {
        field_name: "purchase_date"
        type: { string_type { encoding { utf8_bytes {} } } }
      }
      field {
        field_name: "order_number"
        type: { string_type { encoding { utf8_bytes {} } } }
      }
      encoding {
        delimited_bytes { delimiter "#" }
      }
    

The `sales` table contains the following data. The `product` column family has two columns.

row key | product  
---|---  
| **product_type** | **product_name**  
"user1#2025-05-20#abcd1233" | "phone" | "iPhone16_pro_max"  
"user1#2025-05-20#abcd1235" | "shoes" | "nike_hyperdunk"  
"user2#2025-05-24#defg456" | "headphones" | "sony_wh_1000mx5"  
  
### Structured row key query results

Because the `sales` table has structured row keys, if you query the table with a `SELECT *` statement, the query returns each segment of the row key as a separate column. As in any SQL query to a Bigtable table, columns in a column family are expressed as maps.
    
    
      SELECT * from sales
    

Results look like the following:

user_id | purchase_date | order_number | product  
---|---|---|---  
user1 | 2025-05-20 | "abcd1233" | { product_type: "phone", product_name: "iPhone16_pro_max" }  
user1 | 2025-05-20 | "abcd1235" | { product_type: "shoes", product_name: "nike_hyperdunk" }  
user2 | 2025-05-24 | "defg456" | { product_type: "headphones", product_name: "sony_wh_1000mx5" }  
  
You can also specify the row key columns in your query, as shown in the following example:
    
    
      SELECT
        product[product_type] AS product_type,
        product[product_name] AS product_name
      FROM sales
      WHERE user_id = b"user1"
    

The results look like the following:

product_type | product_name  
---|---  
"phone" | "iphone16_pro_max"  
"shoes" | "nike_hyperdunk"  
  
### Filters

You can filter on the row key schema columns using SQL functions. The following example assumes that `CURRENT_DATE()` returns `2025-05-24`:
    
    
      SELECT
        user_id,
        product["product_name"] AS product_name
      FROM
        sales
      WHERE
        PARSE_DATE("YYYY-MM-DD", purchase_date) = CURRENT_DATE()
        AND user_id = b"user2"
    

The results are as follows:

user_id | product_name  
---|---  
user2 | "sony_wh_1000mx5"  
  
### Aggregate queries

The following example shows how use an aggregate query on structured row key fields:
    
    
      SELECT
        user_id,
        product[product_type] AS product_type,
        count(*) AS count
      FROM sales
      GROUP BY 1, 2
    

The query results are as follows:

user_id | product_type | count  
---|---|---  
user1 | phone | 1  
user1 | shoes | 1  
user2 | headphones | 1  
  
### Original row key

To retrieve the original row key in a table with structured row keys, specify the `_key` column in your query.

**Note:** This query works for a continuous materialized view only if `_key` was selected in the [query that defines the view](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries).
    
    
      SELECT
        _key, user_id
      FROM sales
    

The query returns the following:

_key | user_id  
---|---  
"user1#2025-05-20#abcd1233" | user1  
"user1#2025-05-20#abcd1235" | user1  
"user2#2025-05-24#defg456" | user2  
  
## What's next

  * [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview)
  * [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
