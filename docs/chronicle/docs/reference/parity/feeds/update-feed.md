---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/update-feed/
title: UpdateFeed parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:07.743183+00:00
---

# UpdateFeed parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/update-feed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UpdateFeed parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Feed Management API (**`UpdateFeed`**) to the modern Chronicle API (**`UpdateFeed`**).

## Protocol and mapping overview

Feature | Legacy API (`UpdateFeed`) | Modern Chronicle API (`UpdateFeed`)  
---|---|---  
**HTTP method** | `PATCH` | `PATCH`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/feeds.update`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `UpdateFeedRequest` targets resources using Google Cloud resource name paths and enforces strict validation rules on field masking.

Legacy field (`UpdateFeedRequest` / `Feed`) | Modern field (`UpdateFeedRequest` / `Feed`) | Field type | Parity and migration notes  
---|---|---|---  
`feed.name` | `feed.name` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** The legacy request used path format `feeds/<id>`. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{region}/instances/{instance}/feeds/{id}`.  
`feed.display_name` | `feed.display_name` | `string` | **Parity mapped:** Customer-provided feed name. Rename to `displayName` in JSON payloads. Note: Proto tag number changed from 6 (legacy) to 2 (modern).  
`feed.details` | `feed.details` | `FeedDetails` | **Parity mapped:** Configuration details block for the specific feed source type. Note: Proto tag number changed from 2 (legacy) to 3 (modern).  
`update_mask` | `update_mask` | `FieldMask` | **Parity mapped / restriction note:** Standard FieldMask selecting updated properties. In the modern Chronicle API, to update `displayName`, pass only `displayName` in `update_mask`. To update other parameters, omit `displayName`. Passing an existing `displayName` alongside other updates fails.  
`feed.uid` / `reference_id` | `feed.uid` / `reference_id` | `string` | **Ignored / output-only:** System identifiers generated during creation and ignored in update payloads.  
`feed.feed_state` | `feed.state` | `enum` | **Ignored / output-only:** Ingestion state is managed by pipeline workers. Use EnableFeed/DisableFeed to modify state.  
`feed.read_only` / `failure_msg` / timestamps | — | — | **Ignored / output-only:** Status flags and error details are populated post-execution by backend collectors.  
  
* * *

## Response payload field-by-field parity

Both the legacy Backstory Feed Management API (`UpdateFeed`) and the modern Chronicle API (`UpdateFeed`) responses return the modified Feed message representation.

Legacy field (`Feed` message) | Modern field (`Feed` message) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` | `string` | **Parity mapped:** Contains the standard canonical resource path: `projects/{project}/locations/{location}/instances/{instances}/feeds/{feed_id}`.  
`display_name` | `display_name` | `string` | Rename to `displayName` in JSON responses.  
`details` | `details` | `FeedDetails` | Contains dynamic source-specific configuration properties.  
`feed_state` | `state` | `enum` | **Renamed / value alignment:** Renamed from `feed_state` to `state`. Note enum value changes:  
• `ACTIVE` → `ACTIVE`  
• `INACTIVE` → `INACTIVE`  
• `IN_PROGRESS` → `RUNNING`  
• `COMPLETED` → `SUCCEEDED`  
• `FAILED` → `FAILED`.  
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
  * **Strict fieldmask restrictions:**
    * The modern Chronicle API imposes stricter validation on `update_mask`: updating the display name must be isolated from updating other feed details, preventing unintended name collisions.
  * **State naming and enum shifts:**
    * The status enum field is renamed from `feed_state` to `state`. Ingestion progress stages changed names from `IN_PROGRESS` to `RUNNING`, and from `COMPLETED` to `SUCCEEDED`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
