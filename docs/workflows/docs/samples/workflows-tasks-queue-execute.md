---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-tasks-queue-execute/
title: Use a Cloud Tasks queue to buffer your workflow executions \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:43.315000+00:00
---

# Use a Cloud Tasks queue to buffer your workflow executions  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-tasks-queue-execute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Use a Cloud Tasks queue to buffer your workflow executions Stay organized with collections  Save and categorize content based on your preferences. 

Creates and adds a large number of tasks to the Cloud Tasks queue to execute a child workflow. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use a Cloud Tasks queue to buffer your workflow executions](https://docs.cloud.google.com/workflows/docs/tutorials/buffer-workflows-executions)



## Code sample

### YAML
    
    
    main:
      steps:
        - init:
            assign:
              - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - project_number: ${sys.get_env("GOOGLE_CLOUD_PROJECT_NUMBER")}
              - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
              - workflow_child_name: "workflow-child"
              - queue_name: "queue-workflow-child"
        - enqueue_tasks_to_execute_child_workflow:
            for:
              value: iteration
              range: [1, 100]
              steps:
                  - iterate:
                      assign:
                        - data:
                            iteration: ${iteration}
                        - exec:
                            # Encode object to JSON string in expression for workflow argument
                            argument: ${json.encode_to_string(data)}
                  - create_task_to_execute_child_workflow:
                      call: googleapis.cloudtasks.v2.projects.locations.queues.tasks.create
                      args:
                          parent: ${"projects/" + project_id + "/locations/" + location + "/queues/" + queue_name}
                          body:
                            task:
                              httpRequest:
                                body: ${base64.encode(json.encode(exec))}
                                url: ${"https://workflowexecutions.googleapis.com/v1/projects/" + project_id + "/locations/" + location + "/workflows/" + workflow_child_name + "/executions"}
                                oauthToken:
                                  serviceAccountEmail: ${project_number + "-compute@developer.gserviceaccount.com"}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
