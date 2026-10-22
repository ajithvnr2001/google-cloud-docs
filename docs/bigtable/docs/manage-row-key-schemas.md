---
url: https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas/
title: Manage row key schemas \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:19.588011+00:00
---

# Manage row key schemas  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage row key schemas

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Structured row keys_ let you access your Bigtable data using multi-part keys, similar to composite keys in relational databases. Defining structured row keys for a table lets you access specific parts of the row keys using GoogleSQL for Bigtable queries.

By creating a _row key schema_ , you can define the data type of each segment of a row key and how it is encoded. Bigtable stores the row keys as lexicographically sorted bytes, and the row key schema tells GoogleSQL for Bigtable how to decode and interpret those bytes.

The best practices for designing row keys apply whether you're using structured row keys or not. For more information, see [Row keys](https://docs.cloud.google.com/bigtable/docs/schema-design#row-keys).

**Important:** If any row keys in a table don't conform to the row key schema, queries that select structured row key columns fail and return an error.

Consider the following sample row key, which has delimiters between values for device type, country, manufacturer ID, and serial number:
    
    
    `phone#india#pke5preri2eru#8923695`
    

In the row key schema, you might identify `#` as the delimiter and define the row key segments as follows:

**Row key segment** | **Type** | **Encoding**  
---|---|---  
Device type (phone) | STRING | UTF-8  
Country (India) | STRING | UTF-8  
Manufacturer ID (pke5preri2eru) | STRING | UTF-8  
Serial number (8923695) | BYTES | Raw  
  
## Required permissions

The permissions that you need depend on the action that you want to perform.

To gain these permissions, ask your administrator to grant you a role on the table that includes the permissions:

  * View a row key schema: `bigtable.tables.get`
  * Create a row key schema: `bigtable.tables.update`
  * Delete a row key schema: `bigtable.tables.update`



For more information about granting access, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create a row key schema

When you create a continuous materialized view, Bigtable automatically creates a row key schema for the view. For more information, see [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views).

To define a row key schema for a table that is not a continuous materialized view, you update the table by adding a `RowKeySchema` field that is stored as part of the table.

###  Console 

To define a row key schema using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, open the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**.

The **Explorer** pane displays a list of tables, views, and queries in the instance.

  4. In the **Tables** list, for the table where you want to create a row key schema, click the more_vert **View actions** menu, and then click **Create row key schema**.

The **Row key schema** tab opens.

  5. In the **Encoding** list, select a type of encoding for your row key schema.

  6. If you selected **DelimitedBytes** , in the **Delimiter** field, enter a delimiter that separates the segments in your existing row keys. The default value is a hash symbol (`#`).

  7. In the **Segment** field, enter a name for the segment, such as `device_type`.

  8. In the **Type** list, select the data type of the row key segment.

  9. Depending on the data type selected, in the **Byte encoding** list, leave the default encoding type of the row key segment or change it.

  10. Optional: if your row key segment has more than one part, click **Add row key segment** to add additional fields.

  11. Click **Save**.




###  gcloud 

To define a row key schema using the gcloud CLI, use the [`gcloud beta bigtable tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/tables/update) command with a YAML or JSON file that defines the schema.
    
    
    gcloud beta bigtable tables update TABLE_ID \
      --instance=INSTANCE_ID \
      --row-key-schema-definition-file=ROW_KEY_SCHEMA_DEFINITION_FILE \
      --row-key-schema-pre-encoded-bytes
    

Replace the following:

  * TABLE_ID: the unique ID of the table you want to update
  * INSTANCE_ID: the ID of the instance where the table is located
  * ROW_KEY_SCHEMA_DEFINITION_FILE: the path to your YAML or JSON file that defines the row key schema. For examples of what those files should look like, see Example-schema-files.



By default, Base64 encoding is applied to all binary fields in a YAML or JSON file, such as `encoding.delimitedBytes.delimiter` for the row key delimiter. The flag `--row-key-schema-pre-encoded-bytes` tells Bigtable that binary fields are encoded in the file and shouldn't be encoded again.

###  Go 

Use the `UpdateTableWithRowKeySchema` function to create a row key schema for a table.
    
    
    func (ac *AdminClient) UpdateTableWithRowKeySchema(ctx context.Context, tableID
    string, rowKeySchema StructType) error
    

The following example creates a schema called `rks` and adds it to the table.
    
    
    rks := StructType{
    Fields: []StructField{
        {FieldName: "key1", FieldType: Int64Type{Encoding: Int64OrderedCodeBytesEncoding{}}},
        {FieldName: "key2", FieldType: StringType{Encoding: StringUtf8BytesEncoding{}}},
      },
      Encoding: StructDelimitedBytesEncoding{Delimiter: []byte{'#'}}}
    
    err := c.UpdateTableWithRowKeySchema(context.Background(), "my-table", rks)
    

## Delete a row key schema

**Warning:** If you delete a row key schema, then SQL queries that depend on it no longer work as expected. Delete a row key schema only when you plan to immediately replace it.

###  Console 

To delete a table's row key schema using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, open the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**.

The **Explorer** pane displays a list of tables, views, and queries in the instance.

  4. In the list of tables, click the table with the row key schema that you want to delete.

  5. Click the more_vert **View actions** menu for the row key schema that you want to delete.

  6. Click **Delete**.




###  gcloud 

To delete a table's row key schema, use the [`gcloud beta bigtable tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/tables/update) command with the `--clear-row-key-schema` flag.
    
    
      gcloud beta bigtable tables update TABLE_NAME \
        --instance=INSTANCE_ID \
        --clear-row-key-schema
    

Replace the following:

  * TABLE_NAME: the unique name of the table from which you want to delete the row key schema
  * INSTANCE_ID: the ID of the instance where the table is located



###  Go 

Use the `UpdateTableRemoveRowKeySchema` function to clear the row key schema for a table:
    
    
    func (ac *AdminClient) UpdateTableRemoveRowKeySchema(ctx context.Context,
    tableID string) error
    

## Modify a row key schema

You can't modify a row key schema directly. To change a row key schema, you must delete the schema and create a new one that includes your changes.

## View a row key schema

###  Console 

To view a table's row key schema using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, open the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

  2. Click the instance whose table's row key schema you want to view.

  3. In the navigation menu, click **Bigtable Studio**.

The **Explorer** pane displays a list of tables, views, and queries in the instance.

  4. In the list of tables, click the table with the row key schema that you want to view.

  5. Click the row key schema.

The details tab opens.




###  gcloud 

To view a row key schema, use the [`gcloud beta bigtable tables describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/tables/describe) command:
    
    
      gcloud bigtable tables describe TABLE_NAME \
        --instance=INSTANCE_ID
    

Replace the following:

  * TABLE_NAME: the unique name of the table whose row key schema you want to view
  * INSTANCE_ID: the ID of the instance where the table is located



The response in the terminal is similar to the following. If the table doesn't have a row key schema, the response doesn't include a `rowKeySchema` section.
    
    
    columnFamilies:
      cf: {}
    createTime: '2025-05-28T17:25:39.433058Z'
    granularity: MILLIS
    name: projects/<project>/instances/<instance>/tables/<table>
    rowKeySchema:
      encoding:
        delimitedBytes:
          delimiter: Iw==
      fields:
      - fieldName: <field_name_1>
        type:
          stringType:
            encoding:
              utf8Bytes: {}
      - fieldName: <field_name_2>
        type:
          intType:
            encoding:
              bigEndianBytes: {}
      - fieldName: <field_name_3>
        type:
          timestampType:
            encoding:
              unixMicrosInt64: {
                  encoding: {
                      orderedCodeBytes: {}
                  }
              }
    updateTime: '2025-05-28T17:25:39.433058Z'
    

###  Go 

The `RowKeySchema` field is available as part of the `TableInfo` object, and you retrieve it using the `.TableInfo()` method.
    
    
    type TableInfo struct {
      ...
      RowKeySchema          *StructType
    }
    
    func (ac *AdminClient) TableInfo(ctx context.Context, table string) (*TableInfo, error)
    

## Querying structured row keys

To query the columns in structured row keys, you must use SQL. The Bigtable Data API `ReadRows` method ignores a row key schema when it reads from a table.

For examples of queries selecting structured row keys, see [Structured row key queries](https://docs.cloud.google.com/bigtable/docs/structured-row-key-queries).

For a list of Bigtable client libraries that support SQL queries, including code samples, see [Use SQL with a Bigtable client library](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#client-libraries).

## Example schema files

When you create a row key schema using the gcloud CLI, you can define the structured row keys using either a YAML file or a JSON file.

###  YAML 
    
    
    fields:
      - fieldName: "user_id"
        type:
          stringType:
            encoding:
              utf8Bytes: {}
      - fieldName: "purchase_date"
        type:
          stringType:
            encoding:
              utf8Bytes: {}
      - fieldName: "order_number"
        type:
          stringType:
            encoding:
              utf8Bytes: {}
    encoding:
      delimitedBytes:
        delimiter: "Iw=="
    

###  JSON 
    
    
    {
      "fields": [
        {
          "fieldName": "user_id",
          "type": {
            "stringType": {
              "encoding": {
                "utf8Bytes": {}
              }
            }
          }
        },
        {
          "fieldName": "purchase_date",
          "type": {
            "stringType": {
              "encoding": {
                "utf8Bytes": {}
              }
            }
          }
        },
        {
          "fieldName": "order_number",
          "type": {
            "stringType": {
              "encoding": {
                "utf8Bytes": {}
              }
            }
          }
        }
      ],
      "encoding": {
        "delimitedBytes": {
          "delimiter": "Iw=="
        }
      }
    }
    

## What's next

  * [Create and manage continuous materialized views](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views)
  * [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
