---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-async-connector/
title: Connect asynchronously with SQLAlchemy \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:46.321556+00:00
---

# Connect asynchronously with SQLAlchemy  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-async-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Connect asynchronously with SQLAlchemy Stay organized with collections  Save and categorize content based on your preferences. 

This snippet shows how to create a SQLAlchemy `AsyncEngine` to connect securely to your database. It uses the AlloyDB Python Connector's `AsyncConnector` to automatically handle secure, authorized database connections.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Connect using the AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors)



## Code sample

### Python

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import asyncpg
    import sqlalchemy
    import sqlalchemy.ext.asyncio
    
    from google.cloud.alloydbconnector import AsyncConnector
    
    
    async def create_sqlalchemy_engine(
        inst_uri: str,
        user: str,
        password: str,
        db: str,
        refresh_strategy: str = "background",
        ip_type: str = "PRIVATE",
    ) -> tuple[sqlalchemy.ext.asyncio.engine.AsyncEngine, AsyncConnector]:
        """Creates a connection pool for an AlloyDB instance and returns the pool
        and the connector. Callers are responsible for closing the pool and the
        connector.
    
        A sample invocation looks like:
    
            engine, connector = await create_sqlalchemy_engine(
                inst_uri,
                user,
                password,
                db,
            )
            async with engine.connect() as conn:
                time = await conn.execute(sqlalchemy.text("SELECT NOW()")).fetchone()
                curr_time = time[0]
                # do something with query result
                await connector.close()
    
        Args:
            instance_uri (str):
                The instance URI specifies the instance relative to the project,
                region, and cluster. For example:
                "projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance"
            user (str):
                The database user name, e.g., postgres
            password (str):
                The database user's password, e.g., secret-password
            db (str):
                The name of the database, e.g., mydb
            refresh_strategy (Optional[str]):
                Refresh strategy for the AlloyDB Connector. Can be one of "lazy"
                or "background". For serverless environments use "lazy" to avoid
                errors resulting from CPU being throttled.
            ip_type (str):
                IP type used to connect. One of "PUBLIC", "PRIVATE" or "PSC".
        """
        connector = AsyncConnector(refresh_strategy=refresh_strategy)
    
        # create SQLAlchemy connection pool
        engine = sqlalchemy.ext.asyncio.create_async_engine(
            "postgresql+asyncpg://",
            async_creator=lambda: connector.connect(
                inst_uri,
                "asyncpg",
                user=user,
                password=password,
                db=db,
                ip_type=ip_type,
            ),
            execution_options={"isolation_level": "AUTOCOMMIT"},
        )
        return engine, connector
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
