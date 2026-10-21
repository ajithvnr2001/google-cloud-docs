---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-cloudtasks/
title: Connector for Cloud Tasks \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:25.201303+00:00
---

# Connector for Cloud Tasks  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-cloudtasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Tasks Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Tasks within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Tasks API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudtasks/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Tasks connector:
    # Create a Cloud Tasks queue and create a task in that queue
    # Delete the task and then the queue
    # Expected output: "SUCCESS"
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - location_id: "us-central1"
          - queue_id: "example-queue-id"
          - task_id: "example-task-id"
          # Replace TIME_IN_ZULU_FORMAT and CLOUD_FUNCTION_URL placeholders
          - schedule_time: "TIME_IN_ZULU_FORMAT"  # time in RFC3339 UTC "Zulu" format (eg. "2014-10-02T15:01:23Z")
          - cloud_function_url: "CLOUD_FUNCTION_URL"  # Cloud Function URL to be triggered by the task
    - create_queue:
        call: googleapis.cloudtasks.v2.projects.locations.queues.create
        args:
          parent: ${"projects/" + project_id + "/locations/" + location_id}
          body:
            name: ${"projects/" + project_id + "/locations/" + location_id + "/queues/" + queue_id}
        result: queue
    - create_task:
        call: googleapis.cloudtasks.v2.projects.locations.queues.tasks.create
        args:
          parent: ${queue.name}
          body:
            task:
              name: ${queue.name + "/tasks/" + task_id}
              scheduleTime: ${schedule_time}
              httpRequest:
                url: ${cloud_function_url}
                httpMethod: "GET"
        result: task
    - get_task:
        call: googleapis.cloudtasks.v2.projects.locations.queues.tasks.get
        args:
          name: ${task.name}
    - delete_task:
        call: googleapis.cloudtasks.v2.projects.locations.queues.tasks.delete
        args:
          name: ${task.name}
    - delete_queue:
        call: googleapis.cloudtasks.v2.projects.locations.queues.delete
        args:
          name: ${queue.name}
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
