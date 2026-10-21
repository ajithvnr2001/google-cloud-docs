---
url: https://docs.cloud.google.com/spanner/docs/use-sqlalchemy-pg/
title: Integrate Spanner with SQLAlchemy 2 ORM (PostgreSQL dialect) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:10.201435+00:00
---

# Integrate Spanner with SQLAlchemy 2 ORM (PostgreSQL dialect)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-sqlalchemy-pg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Integrate Spanner with SQLAlchemy 2 ORM (PostgreSQL dialect) Stay organized with collections  Save and categorize content based on your preferences. 

[SQLAlchemy 2](https://docs.sqlalchemy.org/en/20/) is a Python SQL toolkit and Object Relational Mapper (ORM).

You can use the SQLAlchemy 2 ORM in combination with the standard [PostgreSQL psycopg3 driver](https://www.psycopg.org/psycopg3/) and PGAdapter.

## Set up SQLAlchemy 2 with Spanner PostgreSQL-dialect databases

  1. Ensure that PGAdapter is running on the same machine as the application that is connecting using SQLAlchemy 2 with Spanner.

For more information, see [Start PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter-start).

  2. Add SQLAlchemy 2 and psycopg3 to your `requirements.txt` file.
         
         psycopg~=3.1.8
         sqlalchemy~=2.0.1
         

  3. Specify `postgresql+psycopg`, `localhost` and `5432` as the database dialect, driver, server host and port in the SQLAlchemy 2 connection string. psycopg3 requires a username and password in the connection string. PGAdapter ignores these.

Optionally, specify a different port number if PGAdapter is configured to listen on a port other than the default PostgreSQL port (5432).
         
         conn_string = "postgresql+psycopg://user:password@localhost:5432/my-database"
         engine = create_engine(conn_string)
         




See the [SQLAlchemy 2 with PostgreSQL documentation](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#dialect-postgresql) for more connection options for PostgreSQL.

## Use SQLAlchemy 2 with PostgreSQL-dialect databases

For more information about the features and recommendations for SQLAlchemy 2 with PostgreSQL-dialect databases, please consult the [reference documentation](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/samples/python/sqlalchemy2-sample) on GitHub.

## What's next

  * Check out the [sample-application](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/samples/python/sqlalchemy2-sample/sample.py) using SQLAlchemy 2 with PGAdapter and Spanner.
  * Learn more about [SQLAlchemy](https://docs.sqlalchemy.org/en/20/).
  * Learn more about [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter).
  * [File a GitHub issue](https://github.com/GoogleCloudPlatform/pgadapter/issues) to report a bug or ask a question about Spanner dialect for SQLAlchemy with PGAdapter.
  * See an [overview of drivers and ORMs](https://docs.cloud.google.com/spanner/docs/drivers-overview) supported for Spanner.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
