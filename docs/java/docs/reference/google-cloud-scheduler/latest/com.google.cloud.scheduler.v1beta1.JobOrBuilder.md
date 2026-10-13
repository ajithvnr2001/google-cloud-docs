---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.JobOrBuilder
title: Interface JobOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:58.489821+00:00
---

# Interface JobOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.JobOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface JobOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.13  2.2.0  2.1.23 
    
    
    public interface JobOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAppEngineHttpTarget()
    
    
    public abstract AppEngineHttpTarget getAppEngineHttpTarget()

App Engine HTTP target.

`.google.cloud.scheduler.v1beta1.AppEngineHttpTarget app_engine_http_target = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AppEngineHttpTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.AppEngineHttpTarget)` | The appEngineHttpTarget.  
  
### getAppEngineHttpTargetOrBuilder()
    
    
    public abstract AppEngineHttpTargetOrBuilder getAppEngineHttpTargetOrBuilder()

App Engine HTTP target.

`.google.cloud.scheduler.v1beta1.AppEngineHttpTarget app_engine_http_target = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AppEngineHttpTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.AppEngineHttpTargetOrBuilder)` |   
  
### getAttemptDeadline()
    
    
    public abstract Duration getAttemptDeadline()

The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. The failed attempt can be viewed in execution logs. Cloud Scheduler will retry the job according to the RetryConfig.

The default and the allowed values depend on the type of target:

  * For HTTP targets, the default is 3 minutes. The deadline must be in the interval [15 seconds, 30 minutes].

  * For App Engine HTTP targets, 0 indicates that the request has the default deadline. The default deadline depends on the scaling type of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds].

  * For Pub/Sub targets, this field is ignored.




`.google.protobuf.Duration attempt_deadline = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The attemptDeadline.  
  
### getAttemptDeadlineOrBuilder()
    
    
    public abstract DurationOrBuilder getAttemptDeadlineOrBuilder()

The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. The failed attempt can be viewed in execution logs. Cloud Scheduler will retry the job according to the RetryConfig.

The default and the allowed values depend on the type of target:

  * For HTTP targets, the default is 3 minutes. The deadline must be in the interval [15 seconds, 30 minutes].

  * For App Engine HTTP targets, 0 indicates that the request has the default deadline. The default deadline depends on the scaling type of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds].

  * For Pub/Sub targets, this field is ignored.




`.google.protobuf.Duration attempt_deadline = 22;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optionally caller-specified in CreateJob or UpdateJob.

A human-readable description for the job. This string must not contain more than 500 characters.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optionally caller-specified in CreateJob or UpdateJob.

A human-readable description for the job. This string must not contain more than 500 characters.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getHttpTarget()
    
    
    public abstract HttpTarget getHttpTarget()

HTTP target.

`.google.cloud.scheduler.v1beta1.HttpTarget http_target = 6;`

**Returns**  
---  
**Type** | **Description**  
`[HttpTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.HttpTarget)` | The httpTarget.  
  
### getHttpTargetOrBuilder()
    
    
    public abstract HttpTargetOrBuilder getHttpTargetOrBuilder()

HTTP target.

`.google.cloud.scheduler.v1beta1.HttpTarget http_target = 6;`

**Returns**  
---  
**Type** | **Description**  
`[HttpTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.HttpTargetOrBuilder)` |   
  
### getLastAttemptTime()
    
    
    public abstract Timestamp getLastAttemptTime()

Output only. The time the last job attempt started.

`.google.protobuf.Timestamp last_attempt_time = 18;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastAttemptTime.  
  
### getLastAttemptTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastAttemptTimeOrBuilder()

Output only. The time the last job attempt started.

`.google.protobuf.Timestamp last_attempt_time = 18;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLegacyAppEngineCron()
    
    
    public abstract boolean getLegacyAppEngineCron()

Immutable. This field is used to manage the legacy App Engine Cron jobs using the Cloud Scheduler API. If the field is set to true, the job will be considered a legacy job. Note that App Engine Cron jobs have fewer features than Cloud Scheduler jobs, e.g., are only limited to App Engine targets.

`bool legacy_app_engine_cron = 23 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The legacyAppEngineCron.  
  
### getName()
    
    
    public abstract String getName()

Optionally caller-specified in CreateJob, after which it becomes output only.

The job name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID`.

  * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `LOCATION_ID` is the canonical ID for the job's location. The list of available locations can be obtained by calling ListLocations. For more information, see <https://cloud.google.com/about/locations/>.
  * `JOB_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Optionally caller-specified in CreateJob, after which it becomes output only.

The job name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID`.

  * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `LOCATION_ID` is the canonical ID for the job's location. The list of available locations can be obtained by calling ListLocations. For more information, see <https://cloud.google.com/about/locations/>.
  * `JOB_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPubsubTarget()
    
    
    public abstract PubsubTarget getPubsubTarget()

Pub/Sub target.

`.google.cloud.scheduler.v1beta1.PubsubTarget pubsub_target = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PubsubTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.PubsubTarget)` | The pubsubTarget.  
  
### getPubsubTargetOrBuilder()
    
    
    public abstract PubsubTargetOrBuilder getPubsubTargetOrBuilder()

Pub/Sub target.

`.google.cloud.scheduler.v1beta1.PubsubTarget pubsub_target = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PubsubTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.PubsubTargetOrBuilder)` |   
  
### getRetryConfig()
    
    
    public abstract RetryConfig getRetryConfig()

Settings that determine the retry behavior.

`.google.cloud.scheduler.v1beta1.RetryConfig retry_config = 19;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.RetryConfig)` | The retryConfig.  
  
### getRetryConfigOrBuilder()
    
    
    public abstract RetryConfigOrBuilder getRetryConfigOrBuilder()

Settings that determine the retry behavior.

`.google.cloud.scheduler.v1beta1.RetryConfig retry_config = 19;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.RetryConfigOrBuilder)` |   
  
### getSchedule()
    
    
    public abstract String getSchedule()

Required, except when used with UpdateJob.

Describes the schedule on which the job will be executed.

The schedule can be either of the following types:

  * [Crontab](https://en.wikipedia.org/wiki/Cron#Overview)
  * English-like [schedule](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules)

As a general rule, execution `n + 1` of a job will not begin until execution `n` has finished. Cloud Scheduler will never allow two simultaneously outstanding executions. For example, this implies that if the `n+1`th execution is scheduled to run at 16:00 but the `n`th execution takes until 16:15, the `n+1`th execution will not start until `16:15`. A scheduled start time will be delayed if the previous execution has not ended when its scheduled time occurs.

If retry_count > 0 and a job attempt fails, the job will be tried a total of retry_count times, with exponential backoff, until the next scheduled start time.




`string schedule = 20;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The schedule.  
  
### getScheduleBytes()
    
    
    public abstract ByteString getScheduleBytes()

Required, except when used with UpdateJob.

Describes the schedule on which the job will be executed.

The schedule can be either of the following types:

  * [Crontab](https://en.wikipedia.org/wiki/Cron#Overview)
  * English-like [schedule](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules)

As a general rule, execution `n + 1` of a job will not begin until execution `n` has finished. Cloud Scheduler will never allow two simultaneously outstanding executions. For example, this implies that if the `n+1`th execution is scheduled to run at 16:00 but the `n`th execution takes until 16:15, the `n+1`th execution will not start until `16:15`. A scheduled start time will be delayed if the previous execution has not ended when its scheduled time occurs.

If retry_count > 0 and a job attempt fails, the job will be tried a total of retry_count times, with exponential backoff, until the next scheduled start time.




`string schedule = 20;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for schedule.  
  
### getScheduleTime()
    
    
    public abstract Timestamp getScheduleTime()

Output only. The next time the job is scheduled. Note that this may be a retry of a previously failed attempt or the next execution time according to the schedule.

`.google.protobuf.Timestamp schedule_time = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The scheduleTime.  
  
### getScheduleTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getScheduleTimeOrBuilder()

Output only. The next time the job is scheduled. Note that this may be a retry of a previously failed attempt or the next execution time according to the schedule.

`.google.protobuf.Timestamp schedule_time = 17;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getState()
    
    
    public abstract Job.State getState()

Output only. State of the job.

`.google.cloud.scheduler.v1beta1.Job.State state = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Job.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.Job.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. State of the job.

`.google.cloud.scheduler.v1beta1.Job.State state = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getStatus()
    
    
    public abstract Status getStatus()

Output only. The response from the target for the last attempted execution.

`.google.rpc.Status status = 11;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The status.  
  
### getStatusOrBuilder()
    
    
    public abstract StatusOrBuilder getStatusOrBuilder()

Output only. The response from the target for the last attempted execution.

`.google.rpc.Status status = 11;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getTargetCase()
    
    
    public abstract Job.TargetCase getTargetCase()

**Returns**  
---  
**Type** | **Description**  
`[Job.TargetCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1beta1.Job.TargetCase)` |   
  
### getTimeZone()
    
    
    public abstract String getTimeZone()

Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the [tz database](http://en.wikipedia.org/wiki/Tz_database).

Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT).

`string time_zone = 21;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The timeZone.  
  
### getTimeZoneBytes()
    
    
    public abstract ByteString getTimeZoneBytes()

Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the [tz database](http://en.wikipedia.org/wiki/Tz_database).

Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT).

`string time_zone = 21;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for timeZone.  
  
### getUserUpdateTime()
    
    
    public abstract Timestamp getUserUpdateTime()

Output only. The creation time of the job.

`.google.protobuf.Timestamp user_update_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The userUpdateTime.  
  
### getUserUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUserUpdateTimeOrBuilder()

Output only. The creation time of the job.

`.google.protobuf.Timestamp user_update_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasAppEngineHttpTarget()
    
    
    public abstract boolean hasAppEngineHttpTarget()

App Engine HTTP target.

`.google.cloud.scheduler.v1beta1.AppEngineHttpTarget app_engine_http_target = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the appEngineHttpTarget field is set.  
  
### hasAttemptDeadline()
    
    
    public abstract boolean hasAttemptDeadline()

The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. The failed attempt can be viewed in execution logs. Cloud Scheduler will retry the job according to the RetryConfig.

The default and the allowed values depend on the type of target:

  * For HTTP targets, the default is 3 minutes. The deadline must be in the interval [15 seconds, 30 minutes].

  * For App Engine HTTP targets, 0 indicates that the request has the default deadline. The default deadline depends on the scaling type of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds].

  * For Pub/Sub targets, this field is ignored.




`.google.protobuf.Duration attempt_deadline = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the attemptDeadline field is set.  
  
### hasHttpTarget()
    
    
    public abstract boolean hasHttpTarget()

HTTP target.

`.google.cloud.scheduler.v1beta1.HttpTarget http_target = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the httpTarget field is set.  
  
### hasLastAttemptTime()
    
    
    public abstract boolean hasLastAttemptTime()

Output only. The time the last job attempt started.

`.google.protobuf.Timestamp last_attempt_time = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastAttemptTime field is set.  
  
### hasPubsubTarget()
    
    
    public abstract boolean hasPubsubTarget()

Pub/Sub target.

`.google.cloud.scheduler.v1beta1.PubsubTarget pubsub_target = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pubsubTarget field is set.  
  
### hasRetryConfig()
    
    
    public abstract boolean hasRetryConfig()

Settings that determine the retry behavior.

`.google.cloud.scheduler.v1beta1.RetryConfig retry_config = 19;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the retryConfig field is set.  
  
### hasScheduleTime()
    
    
    public abstract boolean hasScheduleTime()

Output only. The next time the job is scheduled. Note that this may be a retry of a previously failed attempt or the next execution time according to the schedule.

`.google.protobuf.Timestamp schedule_time = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the scheduleTime field is set.  
  
### hasStatus()
    
    
    public abstract boolean hasStatus()

Output only. The response from the target for the last attempted execution.

`.google.rpc.Status status = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the status field is set.  
  
### hasUserUpdateTime()
    
    
    public abstract boolean hasUserUpdateTime()

Output only. The creation time of the job.

`.google.protobuf.Timestamp user_update_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userUpdateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
