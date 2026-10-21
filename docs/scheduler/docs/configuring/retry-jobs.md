---
url: https://docs.cloud.google.com/scheduler/docs/configuring/retry-jobs/
title: Retry jobs \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:00.461872+00:00
---

# Retry jobs  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/configuring/retry-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Retry jobs Stay organized with collections  Save and categorize content based on your preferences. 

By default, if a Cloud Scheduler job doesn't receive an acknowledgement from its handler, the job is considered to have failed, and will retry according to the exponential backoff you have configured. You can determine this retry behavior in the following ways when creating or updating a Cloud Scheduler job:

  * [Using the Google Cloud console](https://console.cloud.google.com/cloudscheduler)

  * [Using the Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs)

  * [Making a direct API request](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs#retryconfig) and configuring the `RetryConfig`settings of a `Job` resource




## Retry settings

The following tables describe the retry settings that you can configure.

### Maximum retry attempts

The number of attempts that the system will make to run a job using the exponential backoff procedure described by `maxDoublings`.

**Note:** Setting `retryCount` to 0 doesn't prevent failed jobs from running according to schedule after the failure.Description | If `retryCount` is set to a non-zero number, Cloud Scheduler will retry the failed job, using exponential backoff, for `retryCount` times until the job succeeds or the number of retries is exhausted. Note that the next scheduled execution time might be skipped if the retries continue through that time. If `retryCount` is 0 (and if `maxRetryDuration` is also 0), a job attempt _won't be retried if it fails_. Instead, Cloud Scheduler will wait for the next scheduled execution time. Values greater than 5 and negative values are not allowed.  
---|---  
Default | Default is 0.  
Console label | **Max retry attempts**  
CLI flag | `--max-retry-attempts`  
API field | `retryCount`  
  
### Maximum retry duration

The time limit for retrying a failed job, measured from the time when an execution was first attempted. If specified with `retryCount`, the job will be retried until _both limits are reached_.

Description | A duration in seconds with up to nine fractional digits, ending with "s"—for example, "3.5s". A duration of 0 means that the retry duration is unlimited. However, if `retryCount` is also 0, a job attempt _won't be retried if it fails_.  
---|---  
Default | Default is 0 seconds.  
Console label | **Max retry duration**  
CLI flag | `--max-retry-duration`  
API field | `maxRetryDuration`  
  
### Minimum backoff duration

The minimum amount of time to wait before retrying a job after it fails.

Description | A duration in seconds with up to nine fractional digits, ending with "s"—for example, "3.5s".  
---|---  
Default | Default is 5 seconds.  
Console label | **Min backoff duration**  
CLI flag | `--min-backoff`  
API field | `minBackoffDuration`  
  
### Maximum backoff duration

The maximum amount of time to wait before retrying a job after it fails.

Description | A duration in seconds with up to nine fractional digits, ending with "s"—for example, "3.5s".  
---|---  
Default | Default is 3600 seconds (1 hour).  
Console label | **Max backoff duration**  
CLI flag | `--max-backoff`  
API field | `maxBackoffDuration`  
  
### Maximum doublings

Maximum number of times that the interval between failed job retries will be doubled before the increase becomes constant.

Description | The time between retries will double `maxDoublings` times. A job's retry interval starts at `minBackoffDuration`, then doubles `maxDoublings` times, then increases linearly, and finally retries at intervals of `maxBackoffDuration` up to `retryCount` times. For example: If `minBackoffDuration` is 10s, `maxBackoffDuration` is 300s, and `maxDoublings` is 3: 

  1. The job will first be retried in 10s.
  2. The retry interval will double three times.
  3. The retry interval will then increase linearly by 2^3 * 10s.
  4. If applicable, the job will retry at intervals of `maxBackoffDuration` until the job has been attempted `retryCount` times (to a maximum of 5 times).

Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s. If `minBackoffDuration` is 10s, `maxBackoffDuration` is 120s, and `maxDoublings` is 2: 

  1. The job will first be retried in 10s.
  2. The retry interval will double two times.
  3. The retry interval will then increase linearly by 2^2 * 10s.
  4. If applicable, the job will retry at intervals of `maxBackoffDuration` until the job has been attempted `retryCount` times (to a maximum of 5 times).

Thus, the requests will retry at 10s, 20s, 40s, 80s, 120s.  
---|---  
Default | Default is 5.  
Console label | **Max doublings**  
CLI flag | `--max-doublings`  
API field | `maxDoublings`  
  
## Retry examples

The following examples demonstrate the retry behavior when a Cloud Scheduler job doesn't complete successfully.

If both `retryCount` and `maxRetryDuration` are not set
    

Both settings default to 0 and the job doesn't retry at all.

Note that Cloud Scheduler will try to run the job at the next scheduled execution time.

If both `retryCount` and `maxRetryDuration` are set
    

The job will retry at least `retryCount` number of times until reaching `maxRetryDuration`.

Note that the job could retry more times than the `retryCount`.

If `retryCount` is set and `maxRetryDuration` is not set
    

The `maxRetryDuration` setting defaults to 0 and the job will retry exactly `retryCount` number of times.

If `retryCount` is not set and `maxRetryDuration` is set
    

The job will retry any number of times (up to a maximum of 5 times) or until reaching `maxRetryDuration`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
