---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-cloudscheduler/
title: Connector for Cloud Scheduler \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:50.474294+00:00
---

# Connector for Cloud Scheduler  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-cloudscheduler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Scheduler Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Scheduler within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Scheduler API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudscheduler/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Scheduler connector:
    # Create a Pub/Sub topic and subscription for notifications
    # Create a Cloud Scheduler job that runs every minute and publishes
    # a message to the Pub/Sub topic when finished
    # Retrieve message from the subscription and then delete all resources
    # Expected output: "SUCCESS"
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - location_id: "us-central1"
          - job_id: "example-job-id"
          - topic: "example-topic-id"
          - subscription: "example-subscription-id"
    - create_topic:
        call: googleapis.pubsub.v1.projects.topics.create
        args:
          name: ${"projects/" + project_id + "/topics/" + topic}
    - create_subscription_to_topic:
        call: googleapis.pubsub.v1.projects.subscriptions.create
        args:
          name: ${"projects/" + project_id + "/subscriptions/" + subscription}
          body:
            name: ${"projects/" + project_id + "/subscriptions/" + subscription}
            topic: ${"projects/" + project_id + "/topics/" + topic}
    - create_job:
        call: googleapis.cloudscheduler.v1.projects.locations.jobs.create
        args:
          parent: ${"projects/" + project_id + "/locations/" + location_id}
          body:
            name: ${"projects/" + project_id + "/locations/" + location_id + "/jobs/" + job_id}
            description: "An example job created by Workflows to test the Cloud Scheduler connector."
            schedule: "* * * * *"  # runs job every minute
            pubsubTarget:
              topicName: ${"projects/" + project_id + "/topics/" + topic}
              attributes:
                job: "finished!"
    - sleep:
        call: sys.sleep
        args:
          seconds: 100  # sleeps for 100 seconds to allow job to run
    - pull_message:
        call: googleapis.pubsub.v1.projects.subscriptions.pull
        args:
          subscription: ${"projects/" + project_id + "/subscriptions/" + subscription}
          body:
            maxMessages: 1
    - delete_job:
        call: googleapis.cloudscheduler.v1.projects.locations.jobs.delete
        args:
          name: ${"projects/" + project_id + "/locations/" + location_id + "/jobs/" + job_id}
    - delete_subscription:
        call: googleapis.pubsub.v1.projects.subscriptions.delete
        args:
          subscription: ${"projects/" + project_id + "/subscriptions/" + subscription}
    - delete_topic:
        call: googleapis.pubsub.v1.projects.topics.delete
        args:
          topic: ${"projects/" + project_id + "/topics/" + topic}
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
