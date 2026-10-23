---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-parent-execute/
title: Run a workflow that executes other workflows in parallel \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:33.023522+00:00
---

# Run a workflow that executes other workflows in parallel  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-parent-execute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Run a workflow that executes other workflows in parallel Stay organized with collections  Save and categorize content based on your preferences. 

Uses a parent workflow that invokes a child workflow through a connector. Each iteration of the child workflow is passed an iteration argument. The parent workflow waits for and stores the result of each child workflow execution.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Run a workflow that executes other workflows in parallel](https://docs.cloud.google.com/workflows/docs/tutorials/execute-workflows-from-workflow)



## Code sample

### YAML
    
    
    try:
      steps:
        - execute_child_workflow:
            call: googleapis.workflowexecutions.v1.projects.locations.workflows.executions.run
            args:
              workflow_id: workflow-child
              #location: ...
              #project_id: ...
              argument:
                iteration: ${iteration}
            result: execution_result
        - save_successful_execution:
            assign:
              - execution_results.success[string(iteration)]: ${execution_result}
    except:
        as: e
        steps:
          - save_failed_execution:
              assign:
                - execution_results.failure[string(iteration)]: ${e}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
