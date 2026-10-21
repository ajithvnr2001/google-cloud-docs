---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/
title: Module: google.appengine.api.croninfo \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:02:48.152535+00:00
---

# Module: google.appengine.api.croninfo  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.croninfo Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/croninfo.py) CronInfo tools. A library for working with CronInfo records, describing cron entries for an application. Supports loading the records from yaml.

## Classes

[`class AttemptDeadlineValidator`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/AttemptDeadlineValidator): Checks that attempt deadline can be correctly parsed. [`class CronEntry`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/CronEntry): A cron entry describes a single cron job. [`class CronInfoExternal`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/CronInfoExternal): CronInfoExternal describes all cron entries for an application. [`class GrocValidator`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/GrocValidator): Checks that a schedule is in valid groc format. [`class MalformedCronfigurationFile`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/MalformedCronfigurationFile): Configuration file for Cron is malformed. [`class RetryParameters`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/RetryParameters): Retry parameters for a single cron job. [`class TimezoneValidator`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/TimezoneValidator): Checks that a timezone can be correctly parsed and is known.

## Functions

[`LoadSingleCron(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/croninfo/LoadSingleCron): Load a cron.yaml file or string and return a CronInfoExternal object. | 

## Other Members  
  
---  
  
ATTEMPT_DEADLINE |  `'attempt_deadline'`  
CRON |  `'cron'`  
DESCRIPTION |  `'description'`  
JOB_AGE_LIMIT |  `'job_age_limit'`  
JOB_RETRY_LIMIT |  `'job_retry_limit'`  
MAX_BACKOFF_SECONDS |  `'max_backoff_seconds'`  
MAX_DOUBLINGS |  `'max_doublings'`  
MIN_BACKOFF_SECONDS |  `'min_backoff_seconds'`  
RETRY_PARAMETERS |  `'retry_parameters'`  
SCHEDULE |  `'schedule'`  
SERVER_ID_RE_STRING |  `'(?!-)[a-z\\d\\-]{1,63}'`  
SERVER_VERSION_RE_STRING |  `'(?!-)[a-z\\d\\-]{1,100}'`  
TARGET |  `'target'`  
TIMEZONE |  `'timezone'`  
URL |  `'url'`  
groc |  `None`  
groctimespecification |  `None`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
