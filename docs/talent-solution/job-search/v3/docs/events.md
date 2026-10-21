---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/events/
title: Improve pre-trained model with client event data (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:21.987642+00:00
---

# Improve pre-trained model with client event data (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Improve pre-trained model with client event data (v3) Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Talent Solution](https://docs.cloud.google.com/talent-solution/job-search/v3) is a service that brings machine learning to your job search experience, returning high quality results to job seekers far beyond the limitations of typical keyword-based methods. Right out of the box, CTS applies relevance models and job/skill ontologies to your job details. You can improve the results returned to job seekers by recording client events based on the activity of the job seeker.

There are two methods for leveraging this feature, both outlined in this guide. We recommend that you use the `createClientEventRequest` API method, which bypasses the authentication challenges of sending messages to Cloud Talent Solution using [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs) and provides a clean set of APIs to implement the [analytics framework](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/improve-job-search-results-ml).

## Record client events using `createClientEventRequest` (recommended)

When a job seeker performs a specific action, you can use the API to record that action. For example, the job seeker or other entity interacting with the service has had a job (or a list of jobs) rendered in their view, such as in a list of search results in a compressed or clipped format. In this case you can send an IMPRESSION event to Cloud Talent Solution to provide the context of the search results and what a job seeker can see. Further, when the job seeker clicks on a job result to view the full job description, you can send a VIEW event to register the interest of this job seeker in this position.

## Record client events using Cloud Pub/Sub

To leverage this method, send structured messages to Cloud Talent Solution that capture the job seeker's reactions to results based on their queries. These messages are sent to Cloud Talent Solution using [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs). From there, Cloud Talent Solution parses the messages from the tenant site and feeds them to the machine learning model.

The message format and Pub/Sub requests are described below.

### Various scenarios and workflow

The following are two examples showing various scenarios of the job seeker searching, viewing, and applying for a job.

Please note that you should __ONLY__ publish to the project `p-jobs` and the topic `cloud-jobs-events`.

#### Workflow 1

  1. Job seeker performs a search. For example: _Product mgr SF_

Search results are returned to the job seeker.

The job search response object sent back to the customer's server contains a unique `requestId` (for example: `8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==`). Use this `requestId` for all future messages related to this particular SearchJobsRequest API call.

Send Cloud Talent Solution an [`IMPRESSION`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/client-event#EventType.ENUM_VALUES.IMPRESSION) message.

Sample event message:
         
         {
           "eventId": "ID1",
           "eventType": "IMPRESSION",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000000", "jobs/4000000001","jobs/4000000002",
           "jobs/4000000003", "jobs/4000000004"]
           "eventTimestampMillis": 1494379614309
         }
         

  2. Job seeker selects a result (a job posting) to view the full details of the job.

Send Cloud Talent Solution a `VIEW` message.
         
         {
           "eventId": "ID2",
           "eventType": "VIEW",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000000"]
           "eventTimestampMillis": 1494379614311
         }
         

**Note:** A `VIEW` event follows an `IMPRESSION` event.
  3. Job seeker applies to the viewed job posting.

a. If the job seeker is redirected to a page within the same domain (an internal application page), send Cloud Talent Solution an `APPLICATION_START` message.
         
         {
           "eventId": "ID3",
           "eventType": "APPLICATION_START",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000000"]
           "eventTimestampMillis": 1494379614310
         }
         

b. If the job seeker is redirected to an external application page, send Cloud Talent Solution an `APPLICATION_REDIRECT` message.
         
         {
              "eventId": "ID3",
              "eventType": "APPLICATION_REDIRECT",
              "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
              "relatedJobNames": ["jobs/4000000000"]
              "eventTimestampMillis": 1494379614310
            }
         

  4. When the job seeker completes an internal application, send Cloud Talent Solution an `APPLICATION_FINISH` message:
         
         {
           "eventId": "ID4",
           "eventType": "APPLICATION_FINISH",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000000"]
           "eventTimestampMillis": 1494379614311
         }
         

  5. The job seeker goes back to the search results - or if they never clicked a job posting - and continues to page 2 of the results.

Send Cloud Talent Solution an `IMPRESSION` message with the next set of results from page 2. Note: There's a new `requestId` that is generated in the response of the `SearchJobsRequest` API call that generates the second page of results. (for example,`99e5b99c-f1ba-4f85-b17d-ccf878f451f9:APAb7IRESj+/Hzwa3bBd54P3qPx2yOWm5w==`).
         
         {
           "eventId": "ID5",
           "eventType": "IMPRESSION",
           "requestId": "99e5b99c-f1ba-4f85-b17d-ccf878f451f9:APAb7IRESj+/Hzwa3bBd54P3qPx2yOWm5w==",
           "relatedJobNames": ["jobs/4000000005", "jobs/4000000006","jobs/4000000007",
           "jobs/4000000008", "jobs/4000000009"]
           "eventTimestampMillis": 1494379614400
         }
         

  6. Job seeker continues to page 3 of the search results.

Send Cloud Talent Solution an `IMPRESSION` message with the next set of results. NOTE: There's a new `requestId` (for example,`e2d2b916-78c3-4c65-aecc-d8452bc0afb0:APAb7IRvCsNPiRXYkgF8PN5e8BkbFzKOyg==`).
         
         {
           "eventId": "ID6",
           "eventType": "IMPRESSION",
           "requestId": "e2d2b916-78c3-4c65-aecc-d8452bc0afb0:APAb7IRvCsNPiRXYkgF8PN5e8BkbFzKOyg==",
           "relatedJobNames": ["jobs/4000000010", "jobs/4000000011","jobs/4000000012",
           "jobs/400000013", "jobs/4000000014"]
           "eventTimestampMillis": 1494379614500
         }
         




#### Workflow 2

  1. Job seeker performs a search. For example: _Product mgr SF_

Search results are returned to the job seeker.

The job search response object contains a unique `requestId` (for example: `a2179a9b-cf73-413e-8076-98af08b991ad`). Use this `requestId` for all future messages related to this `SearchJobsRequest` API call.

Send Cloud Talent Solution an `IMPRESSION` message.
         
         {
           "eventId": "ID1",
           "eventType": "IMPRESSION",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000000", "jobs/4000000001","jobs/4000000002",
           "jobs/4000000003", "jobs/4000000004"]
         , "eventTimestampMillis": 1494379614309
         }
         

  2. Job seeker selects a result (a job posting) to view the full details of the job.

Send Cloud Talent Solution a `VIEW` message.
         
         {
           "eventId": "ID2",
           "eventType": "VIEW",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000000"]
           "eventTimestampMillis": 1494379614311
         }
         

**Note:** A `VIEW` event follows an `IMPRESSION` event.
  3. Job seeker performs a single click application to a job, as outlined in [APPLICATION_QUICK_SUBMISSION](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/client-event#eventtype).

Send Cloud Talent Solution an `APPLICATION_QUICK_SUBMISSION` message with the next set of results.
         
         {
           "eventId": "ID3",
           "eventType": "APPLICATION_QUICK_SUBMISSION",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000000"]
           "eventTimestampMillis": 1494379614500
         }
         

  4. Job seeker performs the following actions.

a. Job seeker goes back to the search results applies for a job directly from the search results page. The application process is a longer process than defined in APPLICATION_QUICK_SUBMISSION (that is, it's a multi-step application process).

Send Cloud Talent Solution an `APPLICATION_START_FROM_SERP` message.
         
         {
           "eventId": "ID4",
           "eventType": "APPLICATION_START_FROM_SERP",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000014"]
           "eventTimestampMillis": 1494379927500
         }
         

b. Job seeker completes the application for the job. Send Cloud Talent Solution an `APPLICATION_FINISH` message.
         
         {
           "eventId": "ID5",
           "eventType": "APPLICATION_FINISH",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000014"]
           "eventTimestampMillis": 1494379935500
         

}

  5. Job seeker goes back to the search results and applies to a job directly from the search results page. The application process redirects the job seeker to another domain that is outside the tenant site (external application) from which, the progress of the applicant cannot be tracked.

Send Cloud Talent Solution an `APPLICATION_REDIRECT_FROM_SERP` message.
         
         {
           "eventId": "ID6",
           "eventType": "APPLICATION_START_FROM_SERP",
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "relatedJobNames": ["jobs/4000000017"]
           "eventTimestampMillis": 149438807500
         }
         

This is different from `APPLICATION_REDIRECT` where a job seeker is on the job description page when re-routed.




### Event message

Required fields:

  * `eventId` (Customer defined): Each message sent to Cloud Talent Solution must have a unique `eventId`. As a best practice, incorporate the timestamp while defining this field to ensure non-duplicity. The maximum length of this field is 255 characters.

  * `requestId` is the value of the `requestId` returned by the job search response object. This value is unique to a particular `SearchJobsRequest` API call. It is used for all subsequent messages stemming from the original the search `IMPRESSION` event. When a new `SearchJobsRequest` API call is made (for example: job seeker goes to the next page of results) the `requestId` changes.

_Any pubsub message that does not contain a requestId is dropped._

  * `eventType` is a type of event, such as `VIEW` or `IMPRESSION`. (see [`EventType`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/client-event#eventtype) reference for a complete list of values). The minimum fields required to enable model improvements are `IMPRESSION`, `VIEW`, and `APPLICATION_START` (and/or `APPLICATION_REDIRECT`).

  * `relatedJobNames`: These are the job name values for all jobs displayed to the job seeker at the time of the event. For an `IMPRESSION` event, this is a list of all jobs on the page; for a `VIEW` event, it would be the name of the viewed job. Name values are in the format projects/project-id/jobs/12343213 etc. (see [Job fields](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs#Job.FIELDS) for definitions)

  * `eventTimestampMillis` The timestamp of the event, measured in milliseconds since the epoch. This timestamp should reflect when the event actually occurred, not when the message was sent.




### Send message

Your event message must be sent to the [Cloud Pub/Sub service](https://docs.cloud.google.com/pubsub/docs) using a specific project ID and topic ID. See [Quickstart: Tune with Cloud Talent Solution client events](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/improve-job-search-results-ml) for instructions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
