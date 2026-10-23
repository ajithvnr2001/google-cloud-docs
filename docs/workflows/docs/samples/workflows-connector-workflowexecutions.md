---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-workflowexecutions/
title: Connector for Workflows executions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:11.988208+00:00
---

# Connector for Workflows executions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-workflowexecutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Workflows executions Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Workflows executions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Workflow Executions API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Workflow Executions connector
    # to create an execution for a workflow. Make sure the workflow
    # already exists in your project.
    # Expected successful output: "SUCCESS"
    
    - init:
        assign:
          - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - location: "us-central1"
          - workflow: "[fill in the workflow to execute]"  # Make sure this workflow exists in your project.
          - arguments:
              hello: world
              integer: 100
              boolean: true
    # The run helper method is the preferred way to execute a workflow as it doesn't require
    # encoding the workflow arguments in a JSON-formatted string. To compare
    # the usage, we list two demo steps:
    - run_execution:
        call: googleapis.workflowexecutions.v1.projects.locations.workflows.executions.run
        args:
          workflow_id: ${workflow}
          location: ${location}
          project_id: ${project}
          argument: ${arguments}  # Arguments could be specified inline as a map instead.
        result: r1
    - create_execution:
        call: googleapis.workflowexecutions.v1.projects.locations.workflows.executions.create
        args:
          parent: ${"projects/" + project + "/locations/" + location + "/workflows/" + workflow}
          body:
            argument: ${json.encode_to_string(arguments)}
        result: r2
    - the_end:
        return:
          - ${r1}
          - ${r2}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
