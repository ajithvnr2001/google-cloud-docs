---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/improve-job-search-results-ml/
title: Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:45.764916+00:00
---

# Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/improve-job-search-results-ml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Improve job search results using ML and Talent Solution

This page shows you how to improve search results by using Cloud Talent Solution, machine learning (ML), and client event data.

[Cloud Talent Solution](https://docs.cloud.google.com/talent-solution/job-search/v3) is a service that brings machine learning to your job search experience, returning high quality results to job seekers far beyond the limitations of typical keyword-based methods. Right out of the box, CTS applies relevance models and job/skill ontologies to your job details. You can improve the results returned to job seekers by recording client events based on the activity of the job seeker.

There are two methods for leveraging this feature, both outlined in this quickstart. We recommend that you use the `createClientEventRequest` API method, which bypasses the authentication challenges of sending messages to Cloud Talent Solution using [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs) and provides a clean set of APIs to implement the [analytics framework](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/improve-job-search-results-ml).

You'll begin publishing client event data by the end of the tutorial.

## Record client events using `createClientEventRequest` (recommended)

When a job seeker performs a specific action, you can use the API to record that action. For example, the job seeker or other entity interacting with the service has had a job (or a list of jobs) rendered in their view, such as in a list of search results in a compressed or clipped format. In this case you can send an IMPRESSION event to Cloud Talent Solution to provide the context of the search results and what a job seeker can see. Further, when the job seeker clicks on a job result to view the full job description, you can send a VIEW event to register the interest of this job seeker in this position.

### Usage

The following example illustrates how to send a message to Cloud Talent Solution using the API. The job seeker or other entity interacting with the service has had a job (or a list of jobs) rendered in their view, such as in a list of search results in a compressed or clipped format. This event is typically associated with the viewing of a jobs list on a single page by a job seeker.

Please visit [Event Types](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/client-event#EventType) for a full listing of available event types.

## Record client event requests using Cloud Pub/Sub

### Requirements

In order to publish pubsub messages it is required that you publish messages __ONLY__ to the project `p-jobs` and the topic `cloud-jobs-events`.

_Any pubsub message that does not contain a requestId is dropped._

## Before you begin

You have:

  * set up a [Cloud Talent Solution project](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/before-you-begin) in the Google Cloud Platform Console,
  * [created companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/create-company-job) and have successfully [searched](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/quickstart-searching) for your jobs,
  * installed the [Cloud Pub/Sub client library](https://docs.cloud.google.com/pubsub/docs/reference/libraries),

  * set up your environment using [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials),

  * enabled the [Google Cloud Pub/Sub API](https://console.cloud.google.com/apis/library/pubsub.googleapis.com) on your Google Cloud Project,

  * basic familiarity with Java programming.


**Note:** Critical in the above list is setting the environment variable [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries#setting_up_authentication) to the path of the credentials file created when setting up the service account. See the [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs/publisher#publish-messages-to-a-topic) documentation for more information on how to publish data to a project and topic.

This tutorial covers the integration instructions to create a publisher client, publish client events through Cloud Pub/Sub, and clean up. We demonstrate the integration by stepping through a Cloud Talent Solution application using Java code, that focuses on explaining how to make calls to Cloud Talent Solution, rather than explaining the Java client libraries.

### Publish client event data to Cloud Talent Solution

This section walks you through publishing client event data to Cloud Talent Solution, which can be used to improve relevance for your specific business and job seeker needs.

Follow the Google Cloud Pub/Sub [Publisher Guide](https://docs.cloud.google.com/pubsub/docs/publisher#publish-messages-to-a-topic) to publish messages to Cloud Talent Solution.

**Note:** The project-id (`p-jobs`) and topic-id (`cloud-jobs-events`) are automatically created for you to publish messages to. Ensure that all messages are only published to this project and topic. You don't have permission to list topics, or perform any action apart from publishing to this project and topic.

Check that the actual messages sent follow the pattern as described below.

### Sample messages

#### IMPRESSION event

### JSON
    
    
        {
          "eventId": "857523730h91wrgkih9qpl12z8bf",
          "eventType": "IMPRESSION",
          "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
          "relatedJobNames": [
            "jobs/4000000000",
            "jobs/4000000001"
          ],
          "eventTimestampMillis": 1518200614309,
        }
        

#### VIEW event

### JSON
    
    
        {
          "eventId": "9q9wa69qgfx1q1xzwn3zo25z",
          "eventType": "VIEW",
          "requestId": "248pla4w-8wpl-87rt-15rt-430ue8u541m8",
          "relatedJobNames": [
            "jobs/8000000000",
            "jobs/8000000001"
          ],
          "eventTimestampMillis": 1518200617426,
        }
        

### Verify implementation using the Cloud Talent Solution management tools

Cloud Talent Solution provides users of the API with tools to verify your implementation by providing you with [self service tools](https://console.cloud.google.com/job-discovery/overview). 

To learn more about the self service tools, see [Cloud Talent Solution management tools](https://docs.cloud.google.com/talent-solution/docs/management-tools).

## What's next

[Improve pre-trained model with client event data](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/events). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
