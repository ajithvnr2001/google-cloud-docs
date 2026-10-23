---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-app-env-vars/
title: Set up environment variables needed for task creation \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:51.968564+00:00
---

# Set up environment variables needed for task creation  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-app-env-vars/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Set up environment variables needed for task creation Stay organized with collections  Save and categorize content based on your preferences. 

Sets up environment variables needed for task creation.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Trigger Cloud Run functions using Cloud Tasks](https://docs.cloud.google.com/tasks/docs/tutorial-gcf)



## Code sample

### YAML
    
    
    env_variables:
      QUEUE_NAME: "my-queue"
      QUEUE_LOCATION: "us-central1"
      FUNCTION_URL: "https://<region>-<project_id>.cloudfunctions.net/sendEmail"
      SERVICE_ACCOUNT_EMAIL: "<member>@<project_id>.iam.gserviceaccount.com"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
