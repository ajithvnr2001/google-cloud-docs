---
url: https://docs.cloud.google.com/datastream/docs/work-with-postgresql-partitioned-tables/
title: Work with PostgreSQL partitioned tables \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:49.376496+00:00
---

# Work with PostgreSQL partitioned tables  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/work-with-postgresql-partitioned-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Work with PostgreSQL partitioned tables Stay organized with collections  Save and categorize content based on your preferences. 

Datastream supports replicating partitioned tables for PostgreSQL source databases. You can replicate the tables as a single root table or as separate partitioned tables. If you want to replicate both the root table and the partitioned tables, you must create two different streams, with two different publications.

## Replicate as a single root table

To replicate partitioned tables using the schema of the root table, do the following:

  1. Use a publication with the `publish_via_partition_root` parameter set to `true` or create a new one:
         
         CREATE PUBLICATION PUBLICATION_NAME FOR TABLE
         SCHEMA1.TABLE1, SCHEMA2.TABLE2 WITH (publish_via_partition_root = true);
         

Replace the following:

     * PUBLICATION_NAME: The name of the publication.
     * SCHEMA(n): The name of the schema that contains the table.
     * TABLE(n): The name of the table for which you create the publication.
**Note:** Changing the value of the `publish_via_partition_root` parameter in a publication that's already used in a stream isn't supported and causes the stream to fail permanently.

For more information about creating a publication, see [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).

  2. Complete the following in the **Configure source** step when you create your stream in Google Cloud:

     1. From the **Objects to include** list, select **Specific schemas and tables**.
     2. Select only the root table and make sure that the partitioned tables aren't selected.

For information about creating a stream, see [Create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream).




## Replicate as separate tables

To replicate partitioned tables as separate tables, do the following:

  1. Use a publication with the `publish_via_partition_root` parameter set to `false` or create a new one. `false` is the default setting for the parameter.

**Note:** Changing the value of the `publish_via_partition_root` parameter in a publication that's already used in a stream isn't supported and causes the stream to fail permanently.

For more information about creating a publication, see [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).

  2. When you create your stream in Google Cloud, in the **Configure source** step, do the following:

     1. From the **Objects to include** list, select **Specific schemas and tables**.
     2. Select all partitioned tables and make sure that the root table isn't selected.

For information about creating a stream, see [Create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream).




## What's next

  * Learn more about [PostgreSQL as a source](https://docs.cloud.google.com/datastream/docs/sources-postgresql).
  * Learn more about [configuring a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
