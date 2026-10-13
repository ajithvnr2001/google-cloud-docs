---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/enable-feed/
title: EnableFeed parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:18.094392+00:00
---

# EnableFeed parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/enable-feed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# EnableFeed parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Feed Management API (**`EnableFeed`**) to the modern Chronicle API (**`EnableFeed`**).

## Protocol and mapping overview

Feature | Legacy API (`EnableFeed`) | Modern Chronicle API (`EnableFeed`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/feeds.enable`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `EnableFeedRequest` targets resources using Google Cloud resource name paths.

Legacy field (`EnableFeedRequest`) | Modern field (`EnableFeedRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** The legacy request used path format `feeds/<id>`. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{region}/instances/{instance}/feeds/{id}`.  
  
* * *

## Response payload field-by-field parity

Both the legacy Backstory Feed Management API (`EnableFeed`) and the modern Chronicle API (`EnableFeed`) return the modified Feed message representation upon enabling.

Legacy field (`Feed` message) | Modern field (`Feed` message) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` | `string` | **Parity mapped:** Contains the standard canonical resource path: `projects/{project}/locations/{location}/instances/{instances}/feeds/{feed_id}`.  
`display_name` | `display_name` | `string` | Rename to `displayName` in JSON responses.  
`details` | `details` | `FeedDetails` | Contains dynamic source-specific configuration properties.  
`feed_state` | `state` | `enum` | **Renamed / value alignment:** Renamed from `feed_state` to `state`. In both systems, enabling a feed transitions its state out of `INACTIVE` and into `ACTIVE` or `RUNNING` (Legacy `IN_PROGRESS`).  
`uid` | `uid` | `string` | Unique UUID4 identifier for the feed.  
`reference_id` | `reference_id` | `string` | Reference identifier containing legacy ID references.  
`read_only` | `read_only` | `bool` | Rename to `readOnly` in JSON.  
`failure_msg` | `failure_msg` | `string` | Rename to `failureMsg` in JSON.  
`failure_details` | `failure_details` | `FeedFailureDetails` | Structured error details (`error_code`, `http_error_code`, `error_cause`, `error_action`). Rename to `failureDetails` in JSON.  
`last_feed_initiation_time` | `last_feed_initiation_time` | `Timestamp` | Rename to `lastFeedInitiationTime` in JSON.  
  
* * *

## Key differences between the Backstory and Chronicle APIs

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Resource path renaming:**
    * Legacy path formats `feeds/<id>` are migrated to standard Google Cloud path parameters `projects/*/locations/*/instances/*/feeds/<id>`.
  * **State field naming:**
    * The status enum field is renamed from `feed_state` to `state`. Upon enabling, the returned feed state transitions out of `INACTIVE` and into active and running queues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
