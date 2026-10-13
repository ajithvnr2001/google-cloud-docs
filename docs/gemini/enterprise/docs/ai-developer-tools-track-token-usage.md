---
url: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-track-token-usage/
title: Track third-party model token usage \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:13.711729+00:00
---

# Track third-party model token usage  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-track-token-usage/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Track third-party model token usage Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To use this feature, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

You can calculate token consumption by model, day, and user for third-party models in [AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview), such as **Anthropic Claude Opus 5.5** and **Anthropic Claude Sonnet 5.5** , using Cloud Logging and **Observability Analytics**.

## Quickstart

If your project's `_Default` log bucket is already upgraded for **Observability Analytics** , run the following query in **Logging > Observability Analytics** (replacing `[PROJECT_ID]` with your Google Cloud project ID) to get 30-day token usage across third-party Anthropic models:
    
    
    SELECT
      JSON_VALUE(labels.model) AS model,
      COUNT(*) AS requests,
      SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.promptTokenCount) AS INT64)) AS input_tokens,
      SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.candidatesTokenCount) AS INT64)) AS output_tokens,
      IFNULL(SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.cachedContentTokenCount) AS INT64)), 0) AS cached_tokens,
      IFNULL(SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.thoughtsTokenCount) AS INT64)), 0) AS thoughts_tokens,
      SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS INT64)) AS total_tokens
    FROM
      `[PROJECT_ID].global._Default._Default`
    WHERE
      log_id = "businessaicode.googleapis.com/inference_response"
      AND JSON_VALUE(labels.model_provider) = "Anthropic"
      AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
    GROUP BY
      model
    ORDER BY
      total_tokens DESC
    

## Before you begin

Make sure that your project meets the following requirements before running the tutorial steps:

  * **Metadata logging is enabled.** Your AI developer tools administrator controls must have [**Metadata logging**](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings#configure-compliance-settings) enabled so that `inference_response` records include the `jsonPayload.metadata` token block.
  * **You hold at least the Logs Viewer role (`roles/logging.viewer`).** The standard `roles/logging.viewer` role grants SQL access to the `_Default._Default` log view used throughout this guide. Querying the `_Default._AllLogs` view requires `roles/logging.privateLogViewer` or `roles/logging.viewAccessor`.
  * **Your`_Default` log bucket is upgraded for Observability Analytics.**
    1. In the Google Cloud console, go to **Logging > Logs Storage**, find the `_Default` bucket, and check the **Observability Analytics** column.
    2. If it isn't enabled, click more_vert **More** > **Upgrade to use Observability Analytics**. Upgrading modifies `_Default` in place and can't be undone.
    3. **Allow for initial propagation:** After upgrading a bucket, Cloud Logging takes 30 to 60 minutes to refresh routing caches for new log entries, and several hours to backfill historical logs (backfill begins 1 hour after the upgrade completes).



## How the log record is structured

Every inference call emits a single `InferenceResponseLog` entry to the `businessaicode.googleapis.com%2Finference_response` log. Model identity is recorded in `labels`, and token counts are recorded in `jsonPayload.metadata`:
    
    
    {
      "logName": "projects/[PROJECT_ID]/logs/businessaicode.googleapis.com%2Finference_response",
      "timestamp": "2026-10-07T17:23:03.495323480Z",
      "labels": {
        "model": "claude-sonnet-5-5",
        "model_provider": "Anthropic",
        "client_name": "antigravity_cli",
        "user_id": "user:user@example.com",
        "trajectory_id": "25cd0b58-58ea-4beb-b2d7-42e0d3fdd96d",
        "request_id": "25cd0b58-58ea-4beb-b2d7-42e0d3fdd96d-19"
      },
      "jsonPayload": {
        "@type": "type.googleapis.com/google.cloud.businessaicode.logging.v1.InferenceResponseLog",
        "metadata": {
          "promptTokenCount": "70825",
          "cachedContentTokenCount": "69079",
          "candidatesTokenCount": "14215",
          "totalTokenCount": "85040"
        }
      }
    }
    

### Field reference and counting rules

LogEntry field (Logs Explorer and Log-based metrics) | SQL expression (Observability Analytics) | Description  
---|---|---  
`labels.model` | `JSON_VALUE(labels.model)` | Model identifier (for example, `claude-sonnet-5-5` for Anthropic Claude Sonnet 5.5 or `claude-opus-5-5` for Anthropic Claude Opus 5.5).  
`labels.model_provider` | `JSON_VALUE(labels.model_provider)` | Provider name (for example, `Anthropic` or `Google`).  
`labels.user_id` | `JSON_VALUE(labels.user_id)` | Authenticated principal (for example, `user:user@example.com`).  
`labels.trajectory_id` | `JSON_VALUE(labels.trajectory_id)` | Conversation or agent trajectory ID. One user turn typically spans multiple `request_id` calls under a single `trajectory_id`.  
`jsonPayload.metadata.promptTokenCount` | `SAFE_CAST(JSON_VALUE(json_payload.metadata.promptTokenCount) AS INT64)` | Total input tokens for the call (includes cached tokens).  
`jsonPayload.metadata.cachedContentTokenCount` | `SAFE_CAST(JSON_VALUE(json_payload.metadata.cachedContentTokenCount) AS INT64)` | **Subset of** `promptTokenCount` served from prompt cache. Omitted when zero. **Don't** add to `promptTokenCount` or `totalTokenCount`.  
`jsonPayload.metadata.candidatesTokenCount` | `SAFE_CAST(JSON_VALUE(json_payload.metadata.candidatesTokenCount) AS INT64)` | Output tokens generated by the model.  
`jsonPayload.metadata.thoughtsTokenCount` | `SAFE_CAST(JSON_VALUE(json_payload.metadata.thoughtsTokenCount) AS INT64)` | Reasoning tokens, when applicable. **Omitted for Anthropic models.**  
`jsonPayload.metadata.totalTokenCount` | `SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS INT64)` | **Authoritative total for the call.** Equals `promptTokenCount + candidatesTokenCount` (+ `thoughtsTokenCount` when present).  
  
## Step 1: Verify incoming logs in Logs Explorer

Before running SQL queries, confirm that `inference_response` records with token metadata are arriving in your project:

  1. In the Google Cloud console, open **Logging > Logs Explorer**.
  2. Paste the following query into the query editor, replacing `[PROJECT_ID]` with your project ID:
         
         logName="projects/[PROJECT_ID]/logs/businessaicode.googleapis.com%2Finference_response"
         labels.model_provider="Anthropic"
         

  3. Click **Run query**.

  4. In the **Log fields** pane, click **model** to view the request distribution across Anthropic models. This view counts requests, not tokens.




## Step 2: Sum tokens by model in Observability Analytics

  1. In the Google Cloud console, open **Logging > Observability Analytics**.
  2. Set the **Time-range selector** to **Last 30 days** (the time-range selector bounds your query results in addition to your SQL `WHERE` clause).
  3. Paste and run the following query, replacing `[PROJECT_ID]` with your project ID:
         
         SELECT
           JSON_VALUE(labels.model) AS model,
           COUNT(*) AS requests,
           SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.promptTokenCount) AS INT64)) AS input_tokens,
           SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.candidatesTokenCount) AS INT64)) AS output_tokens,
           IFNULL(SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.cachedContentTokenCount) AS INT64)), 0) AS cached_tokens,
           IFNULL(SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.thoughtsTokenCount) AS INT64)), 0) AS thoughts_tokens,
           SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS INT64)) AS total_tokens
         FROM
           `[PROJECT_ID].global._Default._Default`
         WHERE
           log_id = "businessaicode.googleapis.com/inference_response"
           AND JSON_VALUE(labels.model_provider) = "Anthropic"
           AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
         GROUP BY
           model
         ORDER BY
           total_tokens DESC
         




## Step 3: Common SQL recipes

Use the following SQL queries in **Logging > Observability Analytics** to analyze daily token trends and per-user token attribution.

### Daily token trend by model
    
    
    SELECT
      TIMESTAMP_TRUNC(timestamp, DAY) AS day,
      JSON_VALUE(labels.model) AS model,
      COUNT(*) AS requests,
      SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS INT64)) AS total_tokens
    FROM
      `[PROJECT_ID].global._Default._Default`
    WHERE
      log_id = "businessaicode.googleapis.com/inference_response"
      AND JSON_VALUE(labels.model_provider) = "Anthropic"
      AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
    GROUP BY
      day, model
    ORDER BY
      day DESC, total_tokens DESC
    

### Per-user, per-model attribution
    
    
    SELECT
      JSON_VALUE(labels.user_id) AS user_id,
      JSON_VALUE(labels.model) AS model,
      COUNT(*) AS requests,
      SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS INT64)) AS total_tokens
    FROM
      `[PROJECT_ID].global._Default._Default`
    WHERE
      log_id = "businessaicode.googleapis.com/inference_response"
      AND JSON_VALUE(labels.model_provider) = "Anthropic"
      AND JSON_VALUE(labels.user_id) IS NOT NULL
      AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
    GROUP BY
      user_id, model
    ORDER BY
      total_tokens DESC
    

## Step 4: Pin to a Cloud Monitoring dashboard

You have two options for dashboarding, depending on whether you need historical or ad hoc SQL breakdowns, or a lightweight continuous metric:

Approach | Best for | Retains history beyond 30 days? | Supports `user_id` grouping?  
---|---|---|---  
**Option A: Save SQL chart from Observability Analytics** | Per-model, daily, and per-user tables and charts with zero metric setup | Bounded by log bucket retention (default 30 days) | Yes (no cardinality limit)  
**Option B: Log-based distribution metric** | Continuous Monitoring time series and alerting on low-cardinality labels | Yes (stored in Monitoring) | **No** (high cardinality exhausts metric quota)  
  
### Option A: Save directly from Observability Analytics

  1. Run the query from Step 2 or the Daily token trend by model query in **Observability Analytics**.
  2. Switch the results pane from **Table** to **Chart** if you want a visual time series or bar chart.
  3. In the results pane toolbar, click **Save to dashboard** , and then choose an existing Monitoring dashboard or create a new one.



### Option B: Create a log-based distribution metric

  1. In the Google Cloud console, go to **Logging > Log-based metrics**, and then click **Create metric**.
  2. Select **Distribution** as the metric type.
  3. Paste the query from Step 1 into the **Filter** field, and set **Field name** to `jsonPayload.metadata.totalTokenCount`.
  4. Add two labels: 
     * `model` mapped to `labels.model`
     * `model_provider` mapped to `labels.model_provider`



## What's next

  * [View AI developer tools metrics](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics)
  * [Configure AI developer tools model availability](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings#configure-model-availability)
  * [Configure AI developer tools compliance settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings#configure-compliance-settings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
