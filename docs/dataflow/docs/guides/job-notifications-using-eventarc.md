---
url: https://docs.cloud.google.com/dataflow/docs/guides/job-notifications-using-eventarc/
title: Use Eventarc to manage Dataflow jobs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:52.601129+00:00
---

# Use Eventarc to manage Dataflow jobs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/job-notifications-using-eventarc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Eventarc to manage Dataflow jobs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create event-driven workflows triggered by state changes in your Dataflow jobs.

For example, your workflow might:

  * Send an alert to an on-call engineer if a critical job fails.
  * Notify users when a batch job completes, or start another Dataflow job.
  * Clean up resources used by a job, such as Cloud Storage buckets.



## Overview

[Eventarc](https://docs.cloud.google.com/eventarc/docs) is a Google Cloud service that can listen to events from other services and route them to various destinations.

When you run a Dataflow job, the job transitions through various states, such as `JOB_STATE_QUEUED`, `JOB_STATE_RUNNING`, and `JOB_STATE_DONE`. Dataflow integration with Eventarc lets you trigger an action when a job changes state.

Because Eventarc is a managed service, you don't need to provision or manage the underlying infrastructure.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com&redirect=https%3A//console.cloud.google.com)




To use the Eventarc API, your project must have enough [quota](https://docs.cloud.google.com/eventarc/docs/quotas). Also, the service account associated with the Eventarc trigger must have the [appropriate permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions).

## Choose an event destination

Choose an [event destination](https://docs.cloud.google.com/eventarc/docs/overview#targets) to receive the event. The destination determines the next step in your workflow.

For example:

  * To send an SMS alert, you might use Cloud Run functions to create a standalone HTTP trigger.
  * For a more complex workflow, you might use Workflows.
  * If your Dataflow pipeline is part of a larger solution that runs on Google Kubernetes Engine, the trigger can route the event to a GKE service running in your cluster.



For more information about this style of architecture, see [Event-driven architectures](https://docs.cloud.google.com/eventarc/docs/event-driven-architectures) in the Eventarc documentation.

## Create a trigger

To create an Eventarc trigger for Dataflow job state changes, refer to one of the following documents:

  * [Route Dataflow events to Cloud Run](https://docs.cloud.google.com/eventarc/docs/run/route-trigger-dataflow)
  * [Route Dataflow events to Google Kubernetes Engine](https://docs.cloud.google.com/eventarc/docs/gke/route-trigger-dataflow)
  * [Route Dataflow events to Workflows](https://docs.cloud.google.com/eventarc/docs/workflows/route-trigger-dataflow)
  * [Create a trigger for Cloud Run functions](https://docs.cloud.google.com/eventarc/docs/functions/create-triggers)



Optionally, you can filter events by Dataflow job ID. For example, you can select job IDs that match a regular expression. For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).

## Process events

The event data describes the Dataflow job at the time the event was triggered. The payload is similar to the [`Job`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job) resource type, with the `steps`, `pipeline_description`, and `transform_name_mapping` fields omitted. Also, depending on the job state, some fields might not be present.

The following shows an example payload:
    
    
    {
      "id":"2023-04-13_16_28_37-12345678",
      "projectId":"my-project",
      "name":"job1",
      "currentState":"JOB_STATE_QUEUED",
      "currentStateTime":"2023-04-13T23:28:37.437622Z",
      "createTime":"2023-04-13T23:28:37.437622Z",
      "location":"us-central1",
      "startTime":"2023-04-13T23:28:37.437622Z"
    }
    

For more information about job states, see the following topics:

  * [`JobState`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#jobstate)
  * [Life of a Dataflow job](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-workflows#life-of-a-job)



## What's next

  * [Design Dataflow pipeline workflows](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-workflows).
  * Read the [Eventarc documentation](https://docs.cloud.google.com/eventarc/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
