---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-iam-authn/
title: Connect using IAM database authentication \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:55.001645+00:00
---

# Connect using IAM database authentication  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-iam-authn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Connect using IAM database authentication Stay organized with collections  Save and categorize content based on your preferences. 

This snippet creates a SQLAlchemy connection pool that uses the AlloyDB Connector to connect to a database. It demonstrates how to enable IAM database authentication, allowing for secure, password-less connections.

## Code sample

### Python

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import sqlalchemy
    
    from google.cloud.alloydbconnector import Connector
    
    
    def create_sqlalchemy_engine(
        inst_uri: str, user: str, db: str, refresh_strategy: str = "background"
    ) -> tuple[sqlalchemy.engine.Engine, Connector]:
        """Creates a connection pool for an AlloyDB instance and returns the pool
        and the connector. Callers are responsible for closing the pool and the
        connector.
    
        A sample invocation looks like:
    
            engine, connector = create_sqlalchemy_engine(
                inst_uri,
                user,
                db,
            )
            with engine.connect() as conn:
                time = conn.execute(sqlalchemy.text("SELECT NOW()")).fetchone()
                conn.commit()
                curr_time = time[0]
                # do something with query result
                connector.close()
    
        Args:
            instance_uri (str):
                The instance URI specifies the instance relative to the project,
                region, and cluster. For example:
                "projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance"
            user (str):
                The formatted IAM database username.
                e.g., my-email@test.com, service-account@project-id.iam
            db (str):
                The name of the database, e.g., mydb
            refresh_strategy (Optional[str]):
                Refresh strategy for the AlloyDB Connector. Can be one of "lazy"
                or "background". For serverless environments use "lazy" to avoid
                errors resulting from CPU being throttled.
        """
        connector = Connector(refresh_strategy=refresh_strategy)
    
        # create SQLAlchemy connection pool
        engine = sqlalchemy.create_engine(
            "postgresql+psycopg://",
            creator=lambda: connector.connect(
                inst_uri,
                "psycopg",
                user=user,
                db=db,
                enable_iam_auth=True,
            ),
        )
        return engine, connector
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
