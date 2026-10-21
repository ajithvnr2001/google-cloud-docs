---
url: https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/logs-metrics/
title: Logs and metrics \u00a0|\u00a0 Gemini on GDC API on GDC connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:12:57.099553+00:00
---

# Logs and metrics  |  Gemini on GDC API on GDC connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/logs-metrics/

**Gemini on GDC API on GDC connected Public Preview (current)**

For version information, see the [Gemini on GDC API on GDC connected release notes](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/release-notes). 

Available versions: **Public Preview**

  * [ Home ](https://docs.cloud.google.com/)
  * [ Gemini on GDC API on GDC connected ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest)
  * [ Documentation ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/overview)



Send feedback 

#  Logs and metrics Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Warning:** During the Preview period, you may only use Gemini on GDC connected API for evaluation and testing purposes. You may not use the Preview release of Gemini on GDC connected API for commercial or production purposes, or disclose generated output to a third party.

This document describes the logs and metrics that Gemini on Google Distributed Cloud connected API collects and exports.

## Configure logging and monitoring

Before you can start gathering logs and metrics, you must do the following:

  1. Enable the logging APIs by using the following commands:
         
         gcloud services enable opsconfigmonitoring.googleapis.com --project PROJECT_ID
         gcloud services enable logging.googleapis.com --project PROJECT_ID
         gcloud services enable monitoring.googleapis.com --project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the target Google Cloud project.

  2. Grant the roles required to write logs and metrics:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --role roles/opsconfigmonitoring.resourceMetadata.writer \
             --member "serviceAccount:PROJECT_ID.svc.id.goog[kube-system/metadata-agent]"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --role roles/logging.logWriter \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[kube-system/stackdriver-log-forwarder]"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --role roles/monitoring.metricWriter \
             --member "serviceAccount:PROJECT_ID.svc.id.goog[kube-system/gke-metrics-agent]"
         

Replace `PROJECT_ID` with the ID of the target Google Cloud project.




## Logs

This section lists the Cloud Logging resource types supported by Gemini on GDC connected API. To view Gemini on GDC connected API logs, use the [Logs Explorer](https://console.cloud.google.com/logs) in the Google Cloud console. Gemini on GDC connected API} logging is always enabled.

The Gemini on GDC connected API connected logged resource type is `aiplatform.googleapis.com/Endpoint`.

You can also capture and retrieve Gemini on GDC connected API connected logs by using the Cloud Logging API. For information about how to configure this logging mechanism, see the documentation for [Cloud Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries).

## Metrics

This section lists the Cloud Monitoring metrics supported by Gemini on GDC connected API. To view Gemini on GDC connected API metrics, use the [Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer) in the Google Cloud console.

## Distributed Cloud connected cluster metrics

Gemini on GDC connected API endpoints are deployed on Distributed Cloud connected clusters. See [Logs and metrics](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/logs-metrics) for information on logs and metrics for Distributed Cloud connected.

## Inference Gateway metrics

Prometheus Metric Name | Metrics Type | Datatype | Labels | Chemist type | Chemist metric_kind | Chemist value_type | Chemist labels  
---|---|---|---|---|---|---|---  
ig_ops_successful_incoming_requests | Counter |  | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/successful_requests | CUMULATIVE | INT64 | model  
ig_ops_unique_users | Counter |  | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/unique_users | CUMULATIVE | INT64 | model  
ig_tokens_per_minute | Histogram | double | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/tokens_per_min | CUMULATIVE | DISTRIBUTION | model  
ig_total_response_time | Histogram | double | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/response_time | CUMULATIVE | DISTRIBUTION | model  
ig_ops_ffmpeg_image_latency | Histogram | double | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/ffmpeg_image_latencies | CUMULATIVE | DISTRIBUTION | model  
ig_ops_ffmpeg_video_latency | Histogram | double | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/ffmpeg_video_latencies | CUMULATIVE | DISTRIBUTION | model  
ig_ops_ffmpeg_audio_latency | Histogram | double | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/ffmpeg_audio_latencies | CUMULATIVE | DISTRIBUTION | model  
ig_time_to_first_token | Histogram | double | model context_window | aiplatform.googleapis.com/prediction/internal/gdc/ig/ttft | CUMULATIVE | DISTRIBUTION | model context_window  
ig_time_per_output_token | Histogram | double | model context_window | aiplatform.googleapis.com/prediction/internal/gdc/ig/tpot | CUMULATIVE | DISTRIBUTION | model context_window  
ig_cache_hit | Counter |  | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/cache_hit_count | CUMULATIVE | DISTRIBUTION | model _gdch_project  
ig_cache_miss | Counter |  | model | aiplatform.googleapis.com/prediction/internal/gdc/ig/cache_miss_count | CUMULATIVE | DISTRIBUTION | model _gdch_project  
  
## GenAI Router metrics

Prometheus Metric Name | Metrics Type | Datatype | Labels | Chemist type | Chemist metric_kind | Chemist value_type | Chemist labels  
---|---|---|---|---|---|---|---  
llm_total_request_latency_milliseconds | Histogram | double | context_window model | aiplatform.googleapis.com/prediction/internal/gdc/gair/total_request_latencies | CUMULATIVE | DISTRIBUTION | context_window model  
llm_unary_request_latency_milliseconds | Histogram | double | context_window model | aiplatform.googleapis.com/prediction/internal/gdc/gair/unary_request_latencies | CUMULATIVE | DISTRIBUTION | context_window model  
llm_streaming_ttft_milliseconds | Histogram | double | context_window model | aiplatform.googleapis.com/prediction/internal/gdc/gair/ttft_ms | CUMULATIVE | DISTRIBUTION | context_window model  
llm_streaming_tpot_milliseconds | Histogram | double | context_window model | aiplatform.googleapis.com/prediction/internal/gdc/gair/tpot_ms | CUMULATIVE | DISTRIBUTION | context_window model  
llm_input_token_count | Histogram | double | model | aiplatform.googleapis.com/prediction/internal/gdc/gair/input_token_count | CUMULATIVE | DISTRIBUTION | model  
llm_output_token_count | Histogram | double | model | aiplatform.googleapis.com/prediction/internal/gdc/gair/output_token_count | CUMULATIVE | DISTRIBUTION | model  
llm_success_response_count | Counter | double | model | aiplatform.googleapis.com/prediction/internal/gdc/gair/success_response_count | CUMULATIVE | INT64 | model  
llm_failure_response_count | Counter | double | model | aiplatform.googleapis.com/prediction/internal/gdc/gair/failure_response_count | CUMULATIVE | INT64 | model  
llm_text_tokenization_latency_milliseconds | Histogram | double | model | aiplatform.googleapis.com/prediction/internal/gdc/gair/text_tokenization_latencies | CUMULATIVE | DISTRIBUTION | model  
llm_image_tokenization_latency_milliseconds | Histogram | double |  | aiplatform.googleapis.com/prediction/internal/gdc/gair/image_tokenization_latencies | CUMULATIVE | DISTRIBUTION |   
llm_audio_tokenization_latency_milliseconds | Histogram | double |  | aiplatform.googleapis.com/prediction/internal/gdc/gair/audio_tokenization_latencies | CUMULATIVE | DISTRIBUTION |   
  
## GPU metrics

Prometheus Metric Name | Metrics Type | Datatype | Labels | Chemist type | Chemist metric_kind | Chemist value_type | Chemist labels  
---|---|---|---|---|---|---|---  
DCGM_FI_DEV_MEM_COPY_UTIL | Gauge | int64 | gpu UUID pci_bus_id device modelName Hostname DCGM_FI_DRIVER_VERSION | aiplatform.googleapis.com/prediction/internal/gdc/gpu/memory_util | GAUGE | INT64 | uuid gpu_model  
DCGM_FI_DEV_MEMORY_TEMP | Gauge | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/memory_temp | GAUGE | INT64 | Same as Above  
DCGM_FI_DEV_POWER_USAGE | Gauge | double | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/power_usage | GAUGE | DOUBLE | Same as Above  
DCGM_FI_DEV_GPU_TEMP | Gauge | double | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/gpu_temp | GAUGE | INT64 | Same as Above  
DCGM_FI_DEV_GPU_UTIL | Gauge | double | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/gpu_util | GAUGE | INT64 | Same as Above  
DCGM_FI_DEV_ENC_UTIL | Gauge | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/encode_util | GAUGE | INT64 | Same as Above  
DCGM_FI_DEV_XID_ERRORS | Counter | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/xid_errors | CUMULATIVE | INT64 | Same as Above  
DCGM_FI_DEV_POWER_VIOLATION | Counter | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/violation_power | CUMULATIVE | INT64 | Same as Above  
DCGM_FI_DEV_THERMAL_VIOLATION | Counter | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/violation_thermal | CUMULATIVE | INT64 | Same as Above  
DCGM_FI_DEV_SYNC_BOOST_VIOLATION | Counter | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/violation_sync_boost | CUMULATIVE | INT64 | Same as Above  
DCGM_FI_DEV_BOARD_LIMIT_VIOLATION | Counter | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/violation_board_limit | CUMULATIVE | INT64 | Same as Above  
DCGM_FI_DEV_LOW_UTIL_VIOLATION | Counter | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/violation_low_util | CUMULATIVE | INT64 | Same as Above  
DCGM_FI_DEV_RELIABILITY_VIOLATION | Counter | int64 | Same as Above | aiplatform.googleapis.com/prediction/internal/gdc/gpu/violation_reliability | CUMULATIVE | INT64 | Same as Above  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
