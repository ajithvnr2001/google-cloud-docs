---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-parse-files/
title: Parse files \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:28.379814+00:00
---

# Parse files  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-parse-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Parse files Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to parse files when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio. Wrangler lets you parse a file before loading it into the Wrangler workspace:

  * Wrangler infers data types and maps each column to the inferred data type in the same way file source plugins do in the Pipeline Studio.
  * When schema inference isn't possible, you can import the schema for a file format, such as JSON.
  * The recipe doesn't include the parse directive, which reduces transformation logic during pipeline runs.
  * When you create a pipeline from Wrangler, the source plugin includes all the same parsing properties and values that you set in Wrangler.



## Create a file connection

To parse a file before loading it into Wrangler, you must use a file connection, such as File, Cloud Storage, or Amazon S3.

  1. [Go to the Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. Click the **Select data** expander arrow to view the available connections.
  3. Add a connection for File, Cloud Storage, or S3. For more information, see [Create and manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).
  4. To open the parsing options dialog, go to the **Select data** panel and click the name of the file.
  5. In the **Parsing options** dialog, enter the following information:

     1. In the **Format** field, choose the file format of the data being read—for example, **csv**. For more information, see Supported formats.

        * If you choose the delimiter format, in the **Delimiter** field that appears, enter the delimiter information.
        * If you choose CSV, TSV, or delimiter format, an **Enable quoted values** field appears. If your data is wrapped in quotation marks, select **True**. This setting trims quotation marks from the parsed output. For example, the following input, `1, "a, b, c"`, parses into two fields. The first field has the value: `1`. The second field has the value: `a, b, c`. The newline delimiter cannot be within quotes.
        * If you chose text, CSV, TSV, or delimiter format, a **Use first row as header** field appears. To use the first line of each file as a column header, select **True**.
     2. In the **File encoding** field, choose the file encoding type of the source file—for example, **UTF-8**.

     3. Optional: to import the schema or override the inferred schema for the file, click **Import Schema**. You import the schema for formats, such as JSON and some Avro files, where schema inference isn't possible. The schema must be in the Avro format.

     4. Click **Confirm**. The parsed file appears in the Wrangler workspace.




## Supported formats

The following formats are supported for file parsing:

  * Avro
  * Blob (the blob format requires a schema that contains a field named `body` of type `bytes`)
  * CSV
  * Delimited
  * JSON
  * Parquet
  * Text (the text format requires a schema that contains a field named `body` of type `string`)
  * TSV



## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
