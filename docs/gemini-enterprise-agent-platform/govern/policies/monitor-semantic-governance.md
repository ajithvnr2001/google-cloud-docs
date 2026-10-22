---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/monitor-semantic-governance/
title: Monitor semantic governance policies \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:53.017566+00:00
---

# Monitor semantic governance policies  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/monitor-semantic-governance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Monitor semantic governance policies Stay organized with collections  Save and categorize content based on your preferences. 

The semantic governance policy engine automatically collects and processes operational metrics whenever it inspects an agent request. You can use these metrics to observe how many agent requests were governed, which verdicts the policies produced, how much LLM inference the policy evaluations consumed, and how the enforcement pipeline is performing end-to-end.

## Before you begin

Enable the Cloud Monitoring API (`monitoring.googleapis.com`) on the project where the policy engine runs. See [Enable APIs](https://docs.cloud.google.com/monitoring/api/enable-api) for details.

## Overview

The semantic governance policy engine exports metrics to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) automatically. Data points are emitted at two layers:

  * **Request layer** — every agent request the policy engine inspects. Reported as `semantic_governance/request_*`.
  * **Evaluation layer** — every semantic policy evaluation the policy engine performs on inspected traffic. A single evaluation may internally consider multiple attached policies, but is counted once. Reported as `semantic_governance/evaluation_*`.



## Supported built-in metrics

All metrics are associated with the semantic governance policy engine monitored resource [`aiplatform.googleapis.com/SemanticGovernancePolicyEngine`](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/SemanticGovernancePolicyEngine) and are identified by the following resource labels:

  * `resource_container`: the consumer project number.
  * `location`: the region the policy engine runs in, for example `us-central1`.

Metric | Kind | Unit | What it measures  
---|---|---|---  
`aiplatform.googleapis.com/semantic_governance/request_count` | `DELTA` `INT64` | `1{request}` | Number of agent requests the policy engine inspected in the region. The `request_type` label distinguishes LLM calls, tool calls, and other traffic.  
`aiplatform.googleapis.com/semantic_governance/request_latencies` | `DELTA` `DISTRIBUTION` | `s` | Distribution of end-to-end wall-clock latency added by the policy engine per inspected request.  
`aiplatform.googleapis.com/semantic_governance/evaluation_count` | `DELTA` `INT64` | `1{evaluation}` | Number of semantic policy evaluations the policy engine performed. One evaluation is counted per inspected model response, regardless of how many attached policies were considered.  
`aiplatform.googleapis.com/semantic_governance/evaluation_latencies` | `DELTA` `DISTRIBUTION` | `s` | Distribution of latency per policy engine evaluation.  
`aiplatform.googleapis.com/semantic_governance/evaluation_token_count` | `DELTA` `INT64` | `1{token}` | Number of LLM tokens consumed by policy engine evaluations.  
  
### Per-metric labels

Each metric carries additional labels for slicing:

Metric | Labels | Values  
---|---|---  
`request_count` | `method` | HTTP method, for example `"POST"`, `"GET"`.  
| `status_code` | HTTP status code, for example `"200"`.  
| `status` | Semantic evaluation outcome, for example `"OK"`, `"MODEL_ERROR"`, `"EVALUATION_ERROR"`, `"INTERNAL_ERROR"`.  
| `request_type` | Kind of intercepted egress, for example `"LLM"`, `"TOOL"`, `"OTHER"`, `"UNKNOWN"`.  
`request_latencies` | `method`, `status`, `request_type` | Same as `request_count`.  
`evaluation_count` | `final_verdict` | Verdict returned by the engine: `"ALLOW"` or `"DENY"`.  
`evaluation_latencies` | `final_verdict` | Same as `evaluation_count`.  
`evaluation_token_count` | `category` | Kind of token used, for example `"INPUT"`, `"OUTPUT"`, `"THINKING"`.  
  
The generic per-resource labels (`resource_container`, `location`) are available on every metric.

## View metrics

You can view the built-in policy engine metrics in the Google Cloud console using the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer):

  1. To get permission to view metrics in **Metrics Explorer** , ask your administrator to grant you the [Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#monitoring.viewer) role (`roles/monitoring.viewer`) on your project.

  2. Go to **Metrics Explorer** in the Google Cloud console:

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  3. Select your Google Cloud project.

  4. Click **Select a metric** to open a search bar.

  5. Enter **Semantic Governance Policy Engine** in the search bar and click the resource.

  6. Click the **semantic_governance** metric category, then click a metric, such as **Evaluation Count**.

  7. Optionally, filter by labels (for example `final_verdict = DENY`), aggregate across labels, and adjust the time range.




## Query metrics through the API

You can also query the metrics with the [Cloud Monitoring v3 API](https://docs.cloud.google.com/monitoring/api/v3) or [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql).

**Tip:** For `curl` examples, this shell alias may come in handy: `alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'`.

### List the available metric definitions
    
    
    gcurl "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/metricDescriptors?filter=metric.type=starts_with(%22aiplatform.googleapis.com/semantic_governance%22)"

The response should include the definitions for the five metrics listed in the preceding table.

### Query the DENY rate for a region

The following PromQL query returns the fraction of policy evaluations that resulted in `DENY` over a 5-minute rolling window for one region:
    
    
    sum(
      rate(
        aiplatform_googleapis_com:semantic_governance_evaluation_count{
          monitored_resource='aiplatform.googleapis.com/SemanticGovernancePolicyEngine',
          location='REGION',
          final_verdict='DENY'
        }
        [5m]
      )
    )
    /
    sum(
      rate(
        aiplatform_googleapis_com:semantic_governance_evaluation_count{
          monitored_resource='aiplatform.googleapis.com/SemanticGovernancePolicyEngine',
          location='REGION'
        }
        [5m]
      )
    )
    

For divide-by-zero handling on windows with no traffic, and other ratio-metric best practices, see [About ratios of metrics](https://docs.cloud.google.com/monitoring/charts/metric-ratios).

## Create alerts

You can use any of these metrics in an alerting policy. Common examples:

  * **Elevated`MODEL_ERROR` rate**: alert when the fraction of `request_count` samples with `status = MODEL_ERROR` exceeds a threshold over a rolling window.
  * **Latency SLO breach** : alert when the 99th percentile of `evaluation_latencies` exceeds a target latency for a specified duration.
  * **Unexpected DENY spike** : alert when the DENY rate (see the preceding PromQL example) exceeds a threshold, indicating a possible policy misconfiguration or a change in traffic pattern.



For a step-by-step walkthrough on building a threshold alert on any of these metrics, see the alerting example in [Set up monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/monitoring#create-alerts) for Agent Runtime on Gemini Enterprise Agent Platform. The instructions apply unchanged; substitute the policy engine monitored resource and one of the preceding metrics wherever the example uses a Agent Runtime on Gemini Enterprise Agent Platform metric.

See also [Alerting overview](https://docs.cloud.google.com/monitoring/alerts) for the general Cloud Monitoring alerting concepts and [Sample policies in JSON](https://docs.cloud.google.com/monitoring/alerts/policies-in-json) for more example alert policies.

## Related documentation

  * [Semantic governance policies overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/semantic-governance-overview)
  * [Full list of AI Platform metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-aiplatform)
  * [Metric kinds and types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types)
  * [Components of the metric model](https://docs.cloud.google.com/monitoring/api/v3/metric-model)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
