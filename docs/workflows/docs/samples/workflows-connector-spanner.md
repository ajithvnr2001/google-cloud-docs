---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-spanner/
title: Connector for Cloud Spanner \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:22.508364+00:00
---

# Connector for Cloud Spanner  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Spanner Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Spanner within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Spanner API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/spanner/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Spanner connector:
    # Write entries to an existing Spanner database
    # Your database should have the same schema described in the
    # `create_transaction` step
    # Expected output: "SUCCESS"
    - create_table_entry:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - spanner_inst: "SPANNER_INSTANCE"  # replace SPANNER_INSTANCE placeholder
          - spanner_db: "SPANNER_DATABASE"  # replace SPANNER_DATABASE placeholder
          - entry: ["123"]
    - create_transaction:
        assign:
          - req:
              mutations:
                - insert:
                    columns:
                      - ID
                    table: Contacts
                    values:
                      - ${entry}
              singleUseTransaction:
                readWrite: {}
    - create_spanner_session:
        call: googleapis.spanner.v1.projects.instances.databases.sessions.create
        args:
          database: ${"projects/" + project_id + "/instances/" + spanner_inst + "/databases/" + spanner_db}
        result: session
    - write_entry:
        call: googleapis.spanner.v1.projects.instances.databases.sessions.commit
        args:
          session: ${session.name}
          body: ${req}
    - delete_spanner_session:
        call: googleapis.spanner.v1.projects.instances.databases.sessions.delete
        args:
          name: ${session.name}
    - the_end:
        return: SUCCESS

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
