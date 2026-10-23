---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-public-ip/
title: Connect with a public IP using SQLAlchemy \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:15.142574+00:00
---

# Connect with a public IP using SQLAlchemy  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-public-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Connect with a public IP using SQLAlchemy Stay organized with collections  Save and categorize content based on your preferences. 

This snippet shows how to create a SQLAlchemy connection pool for an instance that has a public IP address. Use this approach to securely connect to your instance using the AlloyDB Connector from an environment that cannot access its private IP.

## Code sample

### Python

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import sqlalchemy
    
    from google.cloud.alloydbconnector import Connector
    
    
    def create_sqlalchemy_engine(
        inst_uri: str,
        user: str,
        password: str,
        db: str,
    ) -> tuple[sqlalchemy.engine.Engine, Connector]:
        """Creates a connection pool for an AlloyDB instance and returns the pool
        and the connector. Callers are responsible for closing the pool and the
        connector.
    
        A sample invocation looks like:
    
            engine, connector = create_sqlalchemy_engine(
                    inst_uri,
                    user,
                    password,
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
                The database user name, e.g., postgres
            password (str):
                The database user's password, e.g., secret-password
            db_name (str):
                The name of the database, e.g., mydb
        """
        connector = Connector()
    
        # create SQLAlchemy connection pool
        engine = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=lambda: connector.connect(
                inst_uri,
                "pg8000",
                user=user,
                password=password,
                db=db,
                ip_type="PUBLIC",
            ),
        )
        return engine, connector
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
