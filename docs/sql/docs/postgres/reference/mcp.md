---
url: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/
title: MCP server overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:47.388280+00:00
---

# MCP server overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  MCP server overview Stay organized with collections  Save and categorize content based on your preferences. 

The [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) standardizes how AI applications and agents connect to outside data sources. MCP servers can be local or remote. Local MCP servers typically run on your local machine and use the standard input and output streams (stdio) for communication between services on the same device. Remote MCP servers run on the service's infrastructure and offer an HTTP endpoint to AI applications for communication between the AI MCP client and the MCP server.

For more information, see [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

Cloud SQL for PostgreSQL supports two remote servers for usage with MCP:

  * **Cloud SQL for PostgreSQL server** : Provides tools for managing Cloud SQL for PostgreSQL instances, and executing SQL queries.

    * Learn how to [Use the Cloud SQL for PostgreSQL MCP server](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp).
    * View the detailed [Cloud SQL for PostgreSQL MCP tool reference](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp).
  * **Database Insights server** : Provides tools for querying and analyzing database performance and system metrics.

    * Learn how to [Use the Database Insights MCP server](https://docs.cloud.google.com/sql/docs/postgres/use-database-insights-mcp).
    * View the detailed [Database Insights MCP tool reference](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/databaseinsights/mcp).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
