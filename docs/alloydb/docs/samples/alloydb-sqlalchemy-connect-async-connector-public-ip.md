---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-async-connector-public-ip/
title: Create an asynchronous connection pool using a public IP address \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:47.962832+00:00
---

# Create an asynchronous connection pool using a public IP address  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-async-connector-public-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Create an asynchronous connection pool using a public IP address Stay organized with collections  Save and categorize content based on your preferences. 

This snippet creates an asynchronous SQLAlchemy connection pool to connect to a database instance using its public IP address. This method provides a secure, encrypted connection without requiring you to manually manage SSL/TLS certificates.

## Code sample

### Python

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import pytest
    import sqlalchemy
    import sqlalchemy.ext.asyncio
    
    from google.cloud.alloydbconnector import AsyncConnector
    
    
    async def create_sqlalchemy_engine(
        inst_uri: str,
        user: str,
        password: str,
        db: str,
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
            db_name (str):
                The name of the database, e.g., mydb
        """
        connector = AsyncConnector()
    
        # create SQLAlchemy connection pool
        engine = sqlalchemy.ext.asyncio.create_async_engine(
            "postgresql+asyncpg://",
            async_creator=lambda: connector.connect(
                inst_uri,
                "asyncpg",
                user=user,
                password=password,
                db=db,
                ip_type="PUBLIC",
            ),
            execution_options={"isolation_level": "AUTOCOMMIT"},
        )
        return engine, connector
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
