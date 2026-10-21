---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-sqladmin/
title: Connector for Cloud SQL Admin \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:23.597718+00:00
---

# Connector for Cloud SQL Admin  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-sqladmin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud SQL Admin Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud SQL Admin within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud SQL Admin API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/sqladmin/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud SQL connector.
    # The workflow creates an SQL instance and an SQL database in the SQL instance.
    # Then it deletes the database and the instance. Each of these steps waits
    # until the long-running operation of creating or deleting the SQL database completes.
    # Expected successful output: "SUCCESS"
    
    - init:
        assign:
          - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - instance: "[fill in an instance name]"
          - tier: "db-n1-standard-1"
          - database_name: "[fill in an instance name]"
    - create_instance:
        call: googleapis.sqladmin.v1beta4.instances.insert
        args:
          project: ${project}
          body:
            kind: "sql#database"
            settings:
              tier: ${tier}
            project: ${project}
            backendType: "SECOND_GEN"
            name: ${instance}
    - create_database:
        call: googleapis.sqladmin.v1beta4.databases.insert
        args:
          project: ${project}
          instance: ${instance}
          body:
            kind: "sql#database"
            charset: "utf8"
            collation: "utf8_general_ci"
            name: ${database_name}
            instance: ${instance}
            project: ${project}
            sqlserverDatabaseDetails:
              compatibilityLevel: 5
              recoveryModel: "Simple"
    - get_database:
        call: googleapis.sqladmin.v1beta4.databases.get
        args:
          project: ${project}
          instance: ${instance}
          database: ${database_name}
    - delete_database:
        call: googleapis.sqladmin.v1beta4.databases.delete
        args:
          project: ${project}
          instance: ${instance}
          database: ${database_name}
    - delete_instance:
        call: googleapis.sqladmin.v1beta4.instances.delete
        args:
          project: ${project}
          instance: ${instance}
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
