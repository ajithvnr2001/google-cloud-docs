---
url: https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b/
title: Google Cloud metrics: A or B \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:31.516059+00:00
---

# Google Cloud metrics: A or B  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Google Cloud metrics: A or B Stay organized with collections  Save and categorize content based on your preferences. 

These tables list the Google Cloud metric types whose service domain name begins with the letters `a` or `b`, such as `artifactregistry.googleapis.com`. For information about other metric types, see [Google Cloud metrics overview](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

## About the tables of metrics

The tables of metrics provide formatted versions of the publicly available [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor). This section provides additional information to help you interpret and use these descriptors.

  * For a general explanation of the entries in the tables, including information about values like `DELTA` and `GAUGE`, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

To chart or monitor metric types with values of type `STRING`, you must use Monitoring Query Language (MQL), and you must convert the value into a numeric value. For information about MQL string-conversion methods, see [`String`](https://docs.cloud.google.com/monitoring/mql/reference#string-group).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * The resource-hierarchy level tells you if the metric is written at the project, organization, or folder level(s). When the level is not specified in the metric descriptor, the metric writes at the project level by default.



  * For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).


  * For information about the meaning of launch stages such as `GA` (General Availability) and `BETA` (Preview), see [Product launch stages](https://cloud.google.com/products#product-launch-stages).



**Cloud Endpoints** : APIs managed by Cloud Endpoints write [ `serviceruntime`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime) metrics against the [`api`](https://docs.cloud.google.com/monitoring/api/resources#tag_api) monitored-resource type.

**Note:** To monitor the availability of a service, create an uptime check. These checks create [`monitoring.googleapis.com/uptime_check/check_passed`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/check_passed) metric data. Don't configure an alerting policy to track a metric type such as `compute.googleapis.com/instance/uptime` if your goal is to monitor the availability of a service. For information about why such alerting policies might not function as you expect, see [Uptime policy doesn't create expected alerts](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#use-uptime-check). For information about how to create an uptime check, see [Managing uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks).

## Google Cloud metrics

Metrics from [Google Cloud](https://docs.cloud.google.com/docs).

The following list was last generated at 2026-10-14 20:24:33 UTC. For more information about this process, see [ About the lists](https://docs.cloud.google.com/monitoring/api/metrics#generated).

### actions

Metrics from [Google Assistant Smart Home](https://developers.google.com/assistant/smarthome/overview). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `actions.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`smarthome_action/agent_device_level` GA ** _(project)_**   
Agent device level metrics.   
`GAUGE`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily snapshots of the 30-day trailing window of the device level overall integration. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`overall_level`: Integration overall level.   
`smarthome_action/agent_level_google_to_partner_execution_p90_latency` GA ** _(project)_**   
Agent level google to partner execution p90 latency.   
`GAUGE`, `INT64`, `ms`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily snapshots of the 30-day trailing window for the google to partner execution P90 latency. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`smarthome_action/agent_level_google_to_partner_execution_success_rate` GA ** _(project)_**   
Agent level google to partner execution success rate.   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily snapshots of the 30-day trailing window for the google to partner execution success rate. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`smarthome_action/agent_level_google_to_partner_query_p90_latency` GA ** _(project)_**   
Agent level google to partner query p90 latency.   
`GAUGE`, `INT64`, `ms`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily snapshots of the 30-day trailing window for Google to partner query P90 latency. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`smarthome_action/agent_level_google_to_partner_query_success_rate` GA ** _(project)_**   
Agent level google to partner query success rate.   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily snapshots of the 30-day trailing window for the google to partner query success rate. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`smarthome_action/agent_level_partner_to_google_success_rate` GA ** _(project)_**   
Agent level partner to google success rate.   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily snapshots of the 30-day trailing window for the partner to google success rate. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`integration_type`: Integration type, one of [local, cloud, matter].   
`smarthome_action/agent_level_report_state_accuracy` GA ** _(project)_**   
Agent level report state accuracy.   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily snapshots of the 30-day trailing window for the report state accuracy. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`smarthome_action/agent_official_partner_level` GA ** _(project)_**   
Agent official partner level metrics.   
`GAUGE`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _The official partner level. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`overall_level`: Integration overall level.   
`smarthome_action/agent_provisional_partner_level` GA ** _(project)_**   
Agent provisional partner level metrics.   
`GAUGE`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily snapshots of the 30-day trailing window for the partner level which takes into account device level and partner level actions. Sampled every 3600 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`overall_level`: Integration overall level.   
`smarthome_action/camerastream/first_frame_latencies` BETA ** _(project)_**   
First frame latency   
`DELTA`, `DISTRIBUTION`, `milliseconds`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Latency for first frame to arrive. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`stream_status`: The canonical code that represents the result, for example, "COMPLETED" or "FAILED".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`smarthome_action/camerastream/frame_display_rates` BETA ** _(project)_**   
Frame display rate   
`DELTA`, `DISTRIBUTION`, `frames/seconds`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Rate at which camerastream frames are displayed. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`stream_status`: The canonical code that represents the result, for example, "COMPLETED" or "FAILED".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`smarthome_action/camerastream/frame_drop_rates` BETA ** _(project)_**   
Frame drop rate   
`DELTA`, `DISTRIBUTION`, `frames/seconds`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Rate at which camerastream frames are dropped. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`stream_status`: The canonical code that represents the result, for example, "COMPLETED" or "FAILED".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`smarthome_action/camerastream/frame_skip_rates` BETA ** _(project)_**   
Frame skip rate   
`DELTA`, `DISTRIBUTION`, `frames/seconds`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Rate at which camerastream frames are skipped. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`stream_status`: The canonical code that represents the result, for example, "COMPLETED" or "FAILED".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`smarthome_action/camerastream/request_count` BETA ** _(project)_**   
Camerastream request count   
`DELTA`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Number of camerastream requests since the last sample period. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`status`: The canonical code that represents the result, for example, "SUCCESS" or "OFFLINE".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`surface_type`: The surface that initiated the request (e.g. "SMART_DISPLAY", "MOBILE")   
`smarthome_action/camerastream/request_latencies` BETA ** _(project)_**   
Camerastream request latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Latency for camerastream to start. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`status`: The canonical code that represents the result, for example, "SUCCESS" or "OFFLINE".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`surface_type`: The surface that initiated the request (e.g. "SMART_DISPLAY", "MOBILE")   
`smarthome_action/camerastream/signaling_latencies` BETA ** _(project)_**   
Signaling latency   
`DELTA`, `DISTRIBUTION`, `milliseconds`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Camerastream signaling latency. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`stream_status`: The canonical code that represents the result, for example, "COMPLETED" or "FAILED".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`smarthome_action/camerastream/stream_durations` BETA ** _(project)_**   
Stream duration   
`DELTA`, `DISTRIBUTION`, `milliseconds`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Duration of a camerastream. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`stream_status`: The canonical code that represents the result, for example, "COMPLETED" or "FAILED".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`smarthome_action/camerastream/webrtc_request_count` BETA ** _(project)_**   
Webrtc request count   
`DELTA`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Number of camerastream requests since the last sample period. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, one of [CAMERA, DOORBELL]   
`stream_status`: The canonical code that represents the result, for example, "COMPLETED" or "FAILED".   
`stream_protocol`: Underlying protocol used for camerastream, for example, "webrtc" or "hls".   
`is_battery_powered`: (BOOL) Whether the device is battery powered or not.   
`smarthome_action/device_count` ALPHA ** _(project)_**   
Device count   
`GAUGE`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Counts the device_count based on device_type, software_version, hardware_version, integration_type and is_online. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT", "LOCK" or "CAMERA".   
`software_version`: The software version of the device, for example, "1.00.062", "1.00.64", "1.00.68", "1.1.1".   
`hardware_version`: The hardware version of the device, for example, "1", "1.0", "1.0.0", "1.0.7".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`is_online`: (BOOL) Whether the device is online or not.   
`smarthome_action/execution_success_confidence` BETA ** _(project)_**   
Execution success confidence   
`GAUGE`, `DOUBLE`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Confidence metric (normalized) for current execution success rate compared with past performance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`smarthome_action/local_event_count` BETA ** _(project)_**   
Local event count   
`DELTA`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Count of events that only happens in LocalHomePlatform. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`intent`: Intent used in SmartHome integration, for example, "EXECUTE", "QUERY", "SYNC".   
`status`: The canonical code that represents the result, for example, "SUCCESS" or "OFFLINE".   
`app_version`: The version of the Local Home SDK app, for example, "0.0.1" or "0.1.2".   
`model`: Model is equivalent to product ID.   
`smarthome_action/matter_setup_event_count` BETA ** _(project)_**   
Matter setup event count   
`DELTA`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Counts of Setup Events for Matter Launch. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`setup_status`: The setup status has detailed information about state of setup (commisssioning complete, etc.)   
`setup_state`: The setup state is either Success or Failure.   
`smarthome_action/num_active_users` BETA ** _(project)_**   
Daily active users   
`GAUGE`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Daily active users count. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`locale`: locale, for example, "en-US" or "fr-CA".   
`trait`: Assistant Smarthome trait, for example, "onOff" or "lockUnlock".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`smarthome_action/report_state_accuracy` BETA ** _(project)_**   
Report state accuracy   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _The accuracy of the states reported by the partner to HomeGraph compared to the states retrieved by sending a QUERY to the partner. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`trait`: Assistant Smarthome trait, for example, "onOff" or "lockUnlock".   
`result`: The canonical code that represents the result, for example, "ACCURATE", "ACCURATE_BUT_LATE", "INACCURATE".   
`smarthome_action/report_state_accuracy_raw` BETA ** _(project)_**   
Report state accuracy (raw)   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _The accuracy of the states reported by the partner to HomeGraph compared to the states retrieved by sending a QUERY to the partner (raw Monarch query)._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`trait`: Assistant Smarthome trait, for example, "onOff" or "lockUnlock".   
`result`: The canonical code that represents the result, for example, "ACCURATE", "ACCURATE_BUT_LATE", "INACCURATE".   
`smarthome_action/request_count` BETA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Request count. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`status`: The canonical code that represents the result, for example, "SUCCESS" or "OFFLINE".   
`trait`: Assistant Smarthome trait, for example, "onOff" or "lockUnlock".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`is_local`: (BOOL) Whether the request routed locally or through cloud endpoint.   
`execution_type`: Execution type, one of [execute, query].   
`smarthome_action/request_latencies` BETA ** _(project)_**   
Request latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _Distribution of request latencies. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`status`: The canonical code that represents the result, for example, "SUCCESS" or "OFFLINE".   
`trait`: Assistant Smarthome trait, for example, "onOff" or "lockUnlock".   
`is_local`: (BOOL) Whether the request routed locally or through cloud endpoint.   
`execution_type`: Execution type, one of [execute, query].   
`integration_type`: Integration type, one of [local, cloud, matter].   
`smarthome_action/seven_day_active_users` BETA ** _(project)_**   
7 day active users   
`GAUGE`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _7 day active users count. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`locale`: locale, for example, "en-US" or "fr-CA".   
`trait`: Assistant Smarthome trait, for example, "onOff" or "lockUnlock".   
`integration_type`: Integration type, one of [local, cloud, matter].   
`smarthome_action/twenty_eight_day_active_users` BETA ** _(project)_**   
28 day active users   
`GAUGE`, `INT64`, `1`   
**[assistant_action_project](https://docs.cloud.google.com/monitoring/api/resources#tag_assistant_action_project)** |  _28 day active users count. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`device_type`: Device type, for example, "LIGHT" or "LOCK".   
`locale`: locale, for example, "en-US" or "fr-CA".   
`trait`: Assistant Smarthome trait, for example, "onOff" or "lockUnlock".   
`integration_type`: Integration type, one of [local, cloud, matter].   
  
### aiplatform

Metrics from [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `aiplatform.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`eu_multi_region_online_prediction_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
EU multi-region online prediction input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _EU multi-region online prediction input tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`eu_multi_region_online_prediction_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
EU multi-region online prediction output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _EU multi-region online prediction output tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`eu_multi_region_online_prediction_requests_per_base_model` BETA ** _(project)_**   
EU multi-region online prediction requests per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _EU multi-region online prediction requests per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`eu_multi_region_online_prediction_web_search_requests_per_publisher` BETA ** _(project)_**   
EU multi-region online prediction web search requests per publisher   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _EU multi-region online prediction web search requests per project per publisher._   
`publisher`: The multi-region publisher custom dimension.   
`eu_multi_region_responses_image_inputs_per_base_model_per_minute` BETA ** _(project)_**   
Olympus EU multi-region responses image inputs per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus EU multi-region responses image inputs per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`eu_multi_region_responses_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus EU multi-region responses input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus EU multi-region responses input tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`eu_multi_region_responses_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus EU multi-region responses output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus EU multi-region responses output tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`eu_multi_region_responses_requests_per_minute_per_base_model` BETA ** _(project)_**   
Olympus EU multi-region responses requests per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus EU multi-region responses requests per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`eu_multi_region_responses_total_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus EU multi-region responses total tokens (input + output) per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus EU multi-region responses total tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`executing_vertexai_pipeline_jobs` BETA ** _(project)_**   
Executing PipelineJobs   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of pipeline jobs being executed._  
`executing_vertexai_pipeline_tasks` BETA ** _(project)_**   
Executing PipelineTasks   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of pipeline tasks being executed._  
`featureonlinestore/online_serving/request_count` BETA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _Number of requests received._   
`method`: Online serving method [FetchFeatureValues, SearchNearestEntities].   
`feature_view_id`: The ID of FeatureView.   
`error_code`: Error code.   
`storage_type`: FeatureOnlineStore storage type, one of [bigtable, optimized].   
`featureonlinestore/online_serving/serving_bytes_count` BETA ** _(project)_**   
Response bytes count   
`DELTA`, `INT64`, `By`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _Serving response bytes count._   
`method`: Online serving method [FetchFeatureValues, SearchNearestEntities].   
`feature_view_id`: The ID of FeatureView.   
`storage_type`: FeatureOnlineStore storage type, one of [bigtable, optimized].   
`featureonlinestore/online_serving/serving_latencies` BETA ** _(project)_**   
Request latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _Server side request latency._   
`method`: Online serving method [FetchFeatureValues, SearchNearestEntities].   
`feature_view_id`: The ID of FeatureView.   
`storage_type`: FeatureOnlineStore storage type, one of [bigtable, optimized].   
`featureonlinestore/running_sync` BETA ** _(project)_**   
Running sycs   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _Number of running syncs at given point of time._   
`feature_view_id`: FeatureView ID of running sync.   
`storage_type`: FeatureOnlineStore storage type, one of [bigtable, optimized].   
`sync_type`: Type of running sync [Full, On-demand].   
`featureonlinestore/serving_data_ages` BETA ** _(project)_**   
Serving data ages   
`DELTA`, `DISTRIBUTION`, `s`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _Measure of the serving data age in seconds. Current time minus synced time._   
`feature_view_id`: FeatureView being requested.   
`method`: Online serving method [FetchFeatureValues].   
`storage_type`: FeatureOnlineStore storage type, one of [bigtable, optimized].   
`featureonlinestore/serving_data_by_sync_time` BETA ** _(project)_**   
Serving data by synced time   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _Breakdown of data in Feature Online Store by synced timestamp. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`sync_time`: Timestamp of sync time.   
`featureonlinestore/storage/bigtable_cpu_load` BETA ** _(project)_**   
CPU load   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _The average CPU load of nodes in the Feature Online Store. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`feature_view_id`: FeatureView ID.   
`operation_type`: Operation to Cloud Bigtable, one of [read, write].   
`featureonlinestore/storage/bigtable_cpu_load_hottest_node` BETA ** _(project)_**   
CPU load (hottest node)   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _The CPU load of the hottest node in the Feature Online Store. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`feature_view_id`: FeatureView ID.   
`featureonlinestore/storage/bigtable_nodes` BETA ** _(project)_**   
Node count   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _The number of nodes for the Feature Online Store(Bigtable). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`featureonlinestore/storage/multi_region_bigtable_cpu_load` BETA ** _(project)_**   
CPU load (multi-regional)   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _The average CPU load of nodes in the Feature Online Store with multi-regional replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`cluster_type`: Type of the underlying Bigtable cluster, one of [primary, replica].   
`featureonlinestore/storage/multi_region_bigtable_nodes` BETA ** _(project)_**   
Node count (multi-regional)   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _The number of nodes for the Feature Online Store(Bigtable) with multi-regional replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`cluster_type`: Type of the underlying Bigtable cluster, one of [primary, replica].   
`featureonlinestore/storage/optimized_nodes` BETA ** _(project)_**   
Optimized node count   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _The number of nodes for the Feature Online Store(Optimized). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`feature_view_id`: FeatureView ID.   
`featureonlinestore/storage/stored_bytes` BETA ** _(project)_**   
Bytes stored   
`GAUGE`, `INT64`, `By`   
**[aiplatform.googleapis.com/FeatureOnlineStore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/FeatureOnlineStore)** |  _Bytes stored in the Feature Online Store. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`featurestore/cpu_load` BETA ** _(project)_**   
CPU load   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _The average CPU load for a node in the Featurestore online storage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`featurestore/cpu_load_hottest_node` BETA ** _(project)_**   
CPU load (hottest node)   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _The CPU load for the hottest node in the Featurestore online storage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`featurestore/node_count` BETA ** _(project)_**   
Node count   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _The number of nodes for the Featurestore online storage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`featurestore/online_entities_updated` BETA ** _(project)_**   
Entities updated on the Featurestore online storage.   
`DELTA`, `INT64`, `By`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Number of entities updated on the Featurestore online storage._   
`type`: The type of update: 'WRITE', 'DELETE'.   
`featurestore/online_serving/latencies` BETA ** _(project)_**   
Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Online serving latencies by EntityType._   
`entity_type_id`: EntityType being requested.   
`method`: Online serving method, one of [ReadFeatureValues, StreamingReadFeatureValues].   
`featurestore/online_serving/request_bytes_count` BETA ** _(project)_**   
Request size   
`DELTA`, `INT64`, `By`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Request size by EntityType._   
`entity_type_id`: EntityType being requested.   
`method`: Streaming write method, one of [ReadFeatureValues, StreamingReadFeatureValues, WriteFeatureValues].   
`featurestore/online_serving/request_count` BETA ** _(project)_**   
Serving count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Featurestore online serving count by EntityType._   
`entity_type_id`: EntityType being requested.   
`method`: Online serving method, one of [ReadFeatureValues, StreamingReadFeatureValues].   
`error_code`: Error code.   
`featurestore/online_serving/response_size` BETA ** _(project)_**   
Response size   
`DELTA`, `INT64`, `By`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Response size by EntityType._   
`entity_type_id`: EntityType being requested.   
`method`: Online serving method, one of [ReadFeatureValues, StreamingReadFeatureValues].   
`featurestore/storage/billable_processed_bytes` BETA ** _(project)_**   
Billable bytes   
`GAUGE`, `INT64`, `By`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Number of bytes billed for offline data processed. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Batch read method, one of [BatchReadFeatureValues, ExportFeatureValues].   
`featurestore/storage/stored_bytes` BETA ** _(project)_**   
Bytes stored   
`GAUGE`, `INT64`, `By`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Bytes stored in Featurestore. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_type`: Storage type of Feature Store, one of [ONLINE, BATCH].   
`featurestore/streaming_write/offline_processed_count` BETA ** _(project)_**   
Offline storage write for streaming write   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Number of streaming write requests processed for offline storage._   
`entity_type_id`: EntityType being requested.   
`method`: Streaming write method, one of [WriteFeatureValues].   
`error_code`: Error code.   
`featurestore/streaming_write/offline_write_delays` BETA ** _(project)_**   
Streaming write to offline storage delay time   
`DELTA`, `DISTRIBUTION`, `s`   
**[aiplatform.googleapis.com/Featurestore](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Featurestore)** |  _Time (in second) since the write API is called until it is written to offline storage._   
`entity_type_id`: EntityType being requested.   
`method`: Streaming write method, one of [WriteFeatureValues].   
`generate_content_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Generate content input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Generate content input tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`generate_content_requests_per_minute_per_project_per_base_model` ALPHA ** _(project)_**   
Generate content requests per minute per project per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Generate content requests per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_embed_content_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Global embed content input tokens   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Global embed content input tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_embed_content_requests_per_minute_per_base_model` BETA ** _(project)_**   
Global embed content requests   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Global embed content requests per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_generate_content_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Global generate content input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Global generate content input tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_generate_content_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Global generate content output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Global generate content output tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_generate_content_requests_per_minute_per_project_per_base_model` BETA ** _(project)_**   
Global generate content requests per minute per project per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Global generate content requests per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_online_prediction_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Global online prediction input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Global online prediction input tokens per minute per project per base model._   
`base_model`: The global base model custom dimension.   
`global_online_prediction_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Global online prediction output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Global online prediction output tokens per minute per project per base model._   
`base_model`: The global base model custom dimension.   
`global_online_prediction_requests_per_base_model` BETA ** _(project)_**   
Global online prediction requests per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Global online prediction requests per minute per project per base model._   
`base_model`: The global base model custom dimension.   
`global_responses_image_inputs_per_base_model_per_minute` BETA ** _(project)_**   
Olympus global responses image inputs per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus global responses image inputs per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_responses_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus global responses input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus global responses input tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_responses_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus global responses output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus global responses output tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_responses_requests_per_minute_per_project_per_base_model` BETA ** _(project)_**   
Olympus global responses requests per minute per project per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus global responses requests per minute per project per base model._   
`base_model`: The base model custom dimension.   
`global_responses_total_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus global responses total tokens (input + output) per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus global responses total tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`matching_engine/cpu/request_utilization` ALPHA ** _(project)_**   
CPU request utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/IndexEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/IndexEndpoint)** |  _The fraction of the requested CPU that is currently in use on a match server container._   
`deployed_index_id`: The ID of the target DeployedIndex.   
`node_id`: The ID of the target node: _.   
`candidate_name`: The name of the container release candidate.   
`matching_engine/current_replicas` BETA ** _(project)_**   
Current replicas   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/IndexEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/IndexEndpoint)** |  _Number of active replicas used by the DeployedIndex._   
`deployed_index_id`: The ID of the target DeployedIndex.   
`matching_engine/current_shards` BETA ** _(project)_**   
Current shards   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/IndexEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/IndexEndpoint)** |  _Number of shards of the DeployedIndex._   
`deployed_index_id`: The ID of the target DeployedIndex.   
`matching_engine/memory/used_bytes` ALPHA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[aiplatform.googleapis.com/IndexEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/IndexEndpoint)** |  _The memory used in bytes for a match server container._   
`deployed_index_id`: The ID of the target DeployedIndex.   
`node_id`: The ID of the target node: _.   
`candidate_name`: The name of the container release candidate.   
`matching_engine/query/latencies` BETA ** _(project)_**   
Request latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/IndexEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/IndexEndpoint)** |  _Server side request latency._   
`deployed_index_id`: The ID of the target DeployedIndex.   
`method`: Query method.   
`response_code`: Response code for the query.   
`index_type`: The type of the match server's index, 'sparse' or 'dense'.   
`candidate_name`: The name of the container release candidate.   
`matching_engine/query/request_count` BETA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/IndexEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/IndexEndpoint)** |  _Number of requests received._   
`deployed_index_id`: The ID of the target DeployedIndex.   
`method`: Query method.   
`response_code`: Response code for the query.   
`is_private_endpoint`: True for private endpoint, set to false for public endpoint.   
`candidate_name`: The name of the container release candidate.   
`matching_engine/stream_update/datapoint_count` BETA ** _(project)_**   
Datapoint count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Index)** |  _Number of successfully upserted or removed datapoints._   
`index_endpoint_id`: The ID of the target index endpoint.   
`deployed_index_id`: The ID of the target DeployedIndex.   
`node_id`: The ID of the target node: _.   
`request_type`: Request type for stream update (upsert or remove).   
`index_type`: The type of target Index.   
`candidate_name`: The name of the container release candidate.   
`matching_engine/stream_update/latencies` BETA ** _(project)_**   
Stream update latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Index)** |  _The latencies between the user receives a UpsertDatapointsResponse or RemoveDatapointsResponse and that update takes effect._   
`index_endpoint_id`: The ID of the target index endpoint.   
`deployed_index_id`: The ID of the target DeployedIndex.   
`node_id`: The ID of the target node: _.   
`request_type`: Request type for stream update (upsert or remove).   
`index_type`: The type of target Index.   
`candidate_name`: The name of the container release candidate.   
`matching_engine/stream_update/request_count` BETA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Index)** |  _Number of stream update requests._   
`index_endpoint_id`: The ID of the target index endpoint.   
`deployed_index_id`: The ID of the target DeployedIndex.   
`node_id`: The ID of the target node: _.   
`request_type`: Request type for stream update (upsert or remove).   
`response_code`: Response code.   
`index_type`: The type of target Index.   
`candidate_name`: The name of the container release candidate.   
`model_monitoring/feature_attribution_deviation` BETA ** _(project)_**   
Feature attribution deviation   
`GAUGE`, `DOUBLE`, `1`   
**[aiplatform.googleapis.com/Model](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Model)** |  _The feature attribution deviation value of the given feature._   
`schedule_id`: The identifier of the Vertex schedule. For scheduled continuous monitoring only.   
`feature_name`: The feature name in user's dataset.   
`algorithm`: The metric calculate method.   
`model_monitoring/feature_drift_deviation` BETA ** _(project)_**   
Feature drift deviation   
`GAUGE`, `DOUBLE`, `1`   
**[aiplatform.googleapis.com/Model](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Model)** |  _The drift deviation value of the given feature._   
`schedule_id`: The identifier of the Vertex schedule. For scheduled continuous monitoring only.   
`feature_name`: The feature name in user's dataset.   
`algorithm`: The metric calculate method.   
`model_monitoring/prediction_output_drift_deviation` BETA ** _(project)_**   
Prediction output drift deviation   
`GAUGE`, `DOUBLE`, `1`   
**[aiplatform.googleapis.com/Model](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Model)** |  _The drift deviation value of the prediction output._   
`schedule_id`: The identifier of the Vertex schedule. For scheduled continuous monitoring only.   
`feature_name`: The feature name in user's dataset.   
`algorithm`: The metric calculate method.   
`online_evaluator/evaluations_count` BETA ** _(project)_**   
Evaluations Count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/OnlineEvaluator](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/OnlineEvaluator)** |  _The number of evaluations of the Online Evaluator resource._   
`agent_resource_name`: The resource name of the agent.   
`evaluation_metric_name`: The name of the evaluation metric.   
`evaluation_status`: The status of the evaluation.   
`runtime_revision_id`: The AE runtime revision id that produced the evaluated sample.   
`online_evaluator/scores` BETA ** _(project)_**   
Scores   
`DELTA`, `DISTRIBUTION`, `1`   
**[aiplatform.googleapis.com/OnlineEvaluator](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/OnlineEvaluator)** |  _The distribution of scores of the Online Evaluator._   
`agent_resource_name`: The resource name of the agent.   
`evaluation_metric_name`: The name of the evaluation metric.   
`runtime_revision_id`: The AE runtime revision id that produced the evaluated sample.   
`online_prediction_dedicated_requests_per_base_model_version` BETA ** _(project)_**   
Online prediction dedicated requests per base model version   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Online prediction dedicated requests per minute per project per base model version._   
`base_model_version`: The base model version custom dimension.   
`online_prediction_dedicated_tokens_per_base_model_version` BETA ** _(project)_**   
Online prediction dedicated tokens per minute per base model version   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Online prediction dedicated tokens per minute per project per base model version._   
`base_model_version`: The base model version custom dimension.   
`online_prediction_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Online prediction input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Online prediction input tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`online_prediction_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Online prediction output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Online prediction output tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`online_prediction_requests_per_base_model` BETA ** _(project)_**   
Regional online prediction requests per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Regional online prediction requests per minute per project per base model._   
`base_model`: The regional base model custom dimension.   
`online_prediction_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Regional online prediction tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Regional online prediction tokens per minute per project per base model._   
`base_model`: The regional base model custom dimension.   
`pipelinejob/duration` BETA ** _(project)_**   
PipelineJob duration   
`GAUGE`, `INT64`, `s`   
**[aiplatform.googleapis.com/PipelineJob](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PipelineJob)** |  _Runtime seconds of the pipeline job being executed (from creation to end)._  
`pipelinejob/task_completed_count` BETA ** _(project)_**   
Completed PipelineTasks   
`CUMULATIVE`, `INT64`, `1`   
**[aiplatform.googleapis.com/PipelineJob](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PipelineJob)** |  _Total number of completed PipelineTasks._  
`prediction/gdc/gpu_temperature` BETA ** _(project)_**   
GPU temperature   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Temperature of the GPU serving the user requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`uuid`: uuid of the GPU unit.   
`gpu_model`: GPU model name.   
`prediction/gdc/gpu_utilization` BETA ** _(project)_**   
GPU utilization   
`GAUGE`, `INT64`, `%`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Current utilization of the GPU. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`uuid`: uuid of the GPU unit.   
`gpu_model`: GPU model name.   
`prediction/gdc/input_tokens_per_minute` BETA ** _(project)_**   
Input Tokens Per Minute   
`DELTA`, `DISTRIBUTION`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _A distribution of the number of LLM input tokens per minute. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`model`: The model name of the request.   
`context_window`: The context window of the request.   
`api_name`: The API name.   
`modality`: The modality of the request.   
`protocol`: The protocol used.   
`prediction/gdc/output_tokens_per_minute` BETA ** _(project)_**   
Output Tokens Per Minute   
`DELTA`, `DISTRIBUTION`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _A distribution of the number of LLM output tokens per minute. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`model`: The model name of the request.   
`context_window`: The context window of the request.   
`api_name`: The API name.   
`modality`: The modality of the request.   
`protocol`: The protocol used.   
`prediction/gdc/power_usage` BETA ** _(project)_**   
GPU power usage   
`GAUGE`, `DOUBLE`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Power usage of the GPU serving the user requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`uuid`: uuid of the GPU unit.   
`gpu_model`: GPU model name.   
`prediction/gdc/request_count` BETA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Total number of user LLM requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`model`: The model name of the request.   
`api_name`: The API name of the request.   
`response_code`: The response code of the request.   
`modality`: The modality of the request.   
`protocol`: The protocol used for the request.   
`prediction/gdc/response_time` BETA ** _(project)_**   
Response Time   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Distribution of times to process LLM requests and return the full responses. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`model`: The model name of the request.   
`context_window`: The context window of the request.   
`api_name`: The API name.   
`modality`: The modality of the request.   
`protocol`: The protocol used.   
`prediction/gdc/time_to_first_token` BETA ** _(project)_**   
Time to First Token   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Distribution of times between a user submitting a request and the first token responded back. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`model`: The model name of the request.   
`context_window`: The context window of the request.   
`api_name`: The API name.   
`modality`: The modality of the request.   
`protocol`: The protocol used.   
`prediction/online/accelerator/duty_cycle` BETA ** _(project)_**   
Accelerator duty cycle   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Average fraction of time over the past sample period during which the accelerator(s) were actively processing. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`deployed_model_id`: The ID of the deployed model which serves the prediction request.   
`replica_id`: Unique ID corresponding to the deployed model replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/accelerator/memory/bytes_used` BETA ** _(project)_**   
Accelerator memory usage   
`GAUGE`, `INT64`, `By`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Amount of accelerator memory allocated by the deployed model replica. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`deployed_model_id`: The ID of the deployed model which serves the prediction request.   
`replica_id`: Unique ID corresponding to the deployed model replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/cpu/utilization` BETA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Fraction of CPU allocated by the deployed model replica and currently in use. May exceed 100% if the machine type has multiple CPUs. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`deployed_model_id`: The ID of the deployed model which serves the prediction request.   
`replica_id`: Unique ID corresponding to the deployed model replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/deployment_resource_pool/accelerator/duty_cycle` BETA ** _(project)_**   
Accelerator duty cycle   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/DeploymentResourcePool](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/DeploymentResourcePool)** |  _Average fraction of time over the past sample period during which the accelerator(s) were actively processing. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`replica_id`: Unique ID corresponding to the deployment resource pool replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/deployment_resource_pool/accelerator/memory/bytes_used` BETA ** _(project)_**   
Accelerator memory usage   
`GAUGE`, `INT64`, `By`   
**[aiplatform.googleapis.com/DeploymentResourcePool](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/DeploymentResourcePool)** |  _Amount of accelerator memory allocated by the deployment resource pool replica. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`replica_id`: Unique ID corresponding to the deployment resource pool replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/deployment_resource_pool/cpu/utilization` BETA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[aiplatform.googleapis.com/DeploymentResourcePool](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/DeploymentResourcePool)** |  _Fraction of CPU allocated by the deployment resource pool replica and currently in use. May exceed 100% if the machine type has multiple CPUs. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`replica_id`: Unique ID corresponding to the deployment resource pool replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/deployment_resource_pool/memory/bytes_used` BETA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[aiplatform.googleapis.com/DeploymentResourcePool](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/DeploymentResourcePool)** |  _Amount of memory allocated by the deployment resource pool replica and currently in use. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`replica_id`: Unique ID corresponding to the deployment resource pool replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/deployment_resource_pool/network/received_bytes_count` BETA ** _(project)_**   
Network bytes received   
`DELTA`, `INT64`, `By`   
**[aiplatform.googleapis.com/DeploymentResourcePool](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/DeploymentResourcePool)** |  _Number of bytes received over the network by the deployment resource pool replica._   
`replica_id`: Unique ID corresponding to the deployment resource pool replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/deployment_resource_pool/network/sent_bytes_count` BETA ** _(project)_**   
Network bytes sent   
`DELTA`, `INT64`, `By`   
**[aiplatform.googleapis.com/DeploymentResourcePool](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/DeploymentResourcePool)** |  _Number of bytes sent over the network by the deployment resource pool replica._   
`replica_id`: Unique ID corresponding to the deployment resource pool replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/deployment_resource_pool/replicas` BETA ** _(project)_**   
Replica count   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/DeploymentResourcePool](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/DeploymentResourcePool)** |  _Number of active replicas used by the deployment resource pool. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/deployment_resource_pool/target_replicas` BETA ** _(project)_**   
Replica target   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/DeploymentResourcePool](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/DeploymentResourcePool)** |  _Target number of active replicas needed for the deployment resource pool. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/error_count` BETA ** _(project)_**   
Error count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Number of online prediction errors._   
`deployed_model_id`: The ID of the DeployedModel which serves the prediction request.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`model_display_name`: The display name of the model specified by the user.   
`endpoint_display_name`: The display name of the endpoint specified by the user.   
`prediction/online/machine_count` BETA ** _(project)_**   
Machine count   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Number of machines used by the deployed model. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`deployed_model_id`: The ID of the DeployedModel which serves the prediction request.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`model_display_name`: The display name of the model specified by the user.   
`endpoint_display_name`: The display name of the endpoint specified by the user.   
`prediction/online/memory/bytes_used` BETA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Amount of memory allocated by the deployed model replica and currently in use. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`deployed_model_id`: The ID of the deployed model which serves the prediction request.   
`replica_id`: Unique ID corresponding to the deployed model replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/network/received_bytes_count` GA ** _(project)_**   
Network bytes received   
`DELTA`, `INT64`, `By`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Number of bytes received over the network by the deployed model replica. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`deployed_model_id`: The ID of the deployed model which serves the prediction request.   
`replica_id`: Unique ID corresponding to the deployed model replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/network/sent_bytes_count` BETA ** _(project)_**   
Network bytes sent   
`DELTA`, `INT64`, `By`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Number of bytes sent over the network by the deployed model replica. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`deployed_model_id`: The ID of the deployed model which serves the prediction request.   
`replica_id`: Unique ID corresponding to the deployed model replica.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`prediction/online/prediction_count` BETA ** _(project)_**   
Prediction count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Number of online predictions._   
`deployed_model_id`: The ID of the DeployedModel which serves the prediction request.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`model_display_name`: The display name of the model specified by the user.   
`endpoint_display_name`: The display name of the endpoint specified by the user.   
`prediction/online/prediction_latencies` BETA ** _(project)_**   
Prediction Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Online prediction latency of the deployed model._   
`deployed_model_id`: The ID of the DeployedModel which serves the prediction request.   
`latency_type`: One of the following "overhead", "model" or "total". The "total" latency type will always be populated. And the "overhead" and "model" latency type only get populated for custom-trained models and AutoML tabular models.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`model_display_name`: The display name of the model specified by the user.   
`endpoint_display_name`: The display name of the endpoint specified by the user.   
`prediction/online/private/prediction_latencies` BETA ** _(project)_**   
Private endpoint prediction latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Online prediction latency of the private deployed model. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`deployed_model_id`: The ID of the deployed model which serves the prediction request.   
`prediction/online/private/response_count` BETA ** _(project)_**   
Private endpoint response count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Online prediction response count of the private deployed model. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`deployed_model_id`: The ID of the deployed model which serves the prediction request.   
`response_code`: (INT64) HTTP response code.   
`prediction/online/replicas` BETA ** _(project)_**   
Replica count   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Number of active replicas used by the deployed model. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`deployed_model_id`: The ID of the DeployedModel which serves the prediction request.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`model_display_name`: The display name of the model specified by the user.   
`endpoint_display_name`: The display name of the endpoint specified by the user.   
`prediction/online/response_count` BETA ** _(project)_**   
Response count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Number of different online prediction response codes._   
`deployed_model_id`: The ID of the DeployedModel which serves the prediction request.   
`response_code`: HTTP response code (1xx, 2xx, 3xx, 4xx, 5xx).   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`model_display_name`: The display name of the model specified by the user.   
`endpoint_display_name`: The display name of the endpoint specified by the user.   
`prediction/online/target_replicas` BETA ** _(project)_**   
Replica target   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Target number of active replicas needed for the deployed model. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`deployed_model_id`: The ID of the DeployedModel which serves the prediction request.   
`spot`: Whether this deployment is on Spot VMs. Has values of True or False.   
`model_display_name`: The display name of the model specified by the user.   
`endpoint_display_name`: The display name of the endpoint specified by the user.   
`publisher/online_serving/character_count` BETA ** _(project)_**   
Character count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Accumulated input/output character count._   
`type`: Type of character (input/output).   
`request_type`: Type of request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`modality`: Modality of the characters.   
`publisher/online_serving/characters` BETA ** _(project)_**   
Characters   
`DELTA`, `DISTRIBUTION`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Input/output character count distribution._   
`type`: Type of character (input/output).   
`request_type`: Type of request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`modality`: Modality of the input/output characters.   
`publisher/online_serving/consumed_throughput` BETA ** _(project)_**   
Character Throughput   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Overall throughput used (accounting for burndown rate) in terms of characters._   
`request_type`: Type of request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`modality`: Modality of the consumed characters.   
`publisher/online_serving/consumed_token_throughput` BETA ** _(project)_**   
Token Throughput   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Overall throughput used (accounting for burndown rate) in terms of tokens._   
`request_type`: Type of request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`modality`: Modality of the consumed tokens.   
`publisher/online_serving/dedicated_character_limit` BETA ** _(project)_**   
Limit (characters per second)   
`GAUGE`, `INT64`, `1/s`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Dedicated limit in characters per second._  
`publisher/online_serving/dedicated_character_project_max_limit` BETA ** _(project)_**   
Project Max Limit (characters per second)   
`GAUGE`, `INT64`, `1/s`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Project max limit in characters per second that can be consumed._   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`publisher/online_serving/dedicated_gsu_limit` BETA ** _(project)_**   
Limit (GSU)   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Dedicated limit in GSU._  
`publisher/online_serving/dedicated_gsu_project_max_limit` BETA ** _(project)_**   
Project Max Limit (GSU)   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Project max limit in GSU that can be consumed._   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`publisher/online_serving/dedicated_token_limit` BETA ** _(project)_**   
Limit (tokens per second)   
`GAUGE`, `INT64`, `1/s`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Dedicated limit in tokens per second._  
`publisher/online_serving/dedicated_token_project_max_limit` BETA ** _(project)_**   
Project Max Limit (tokens per second)   
`GAUGE`, `INT64`, `1/s`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Project max limit in tokens per second that can be consumed._   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`publisher/online_serving/first_token_latencies` BETA ** _(project)_**   
First token latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Duration from request received to first token sent back to the client._   
`input_token_size`: The bucketized size of number of tokens in the prediction request.   
`output_token_size`: The bucketized size of number of tokens in the prediction response.   
`max_token_size`: The bucketized max size of number of tokens in the prediction request/response.   
`request_type`: The type of traffic of the request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`explicit_caching`: Whether the request uses explicit caching feature.   
`publisher/online_serving/model_invocation_count` BETA ** _(project)_**   
Model invocation count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Number of model invocations (prediction requests)._   
`input_token_size`: The bucketized size of number of tokens in the prediction request.   
`output_token_size`: The bucketized size of number of tokens in the prediction response.   
`max_token_size`: The bucketized max size of number of tokens in the prediction request/response.   
`response_code`: Responce code of prediction request.   
`request_type`: The type of traffic of the request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`method`: The type of method of the request (RawPredict/StreamRawPredict/ChatCompletions/etc).   
`error_category`: Response error category of the request (user/system/capacity).   
`explicit_caching`: Whether the request uses explicit caching feature.   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`source`: The source/surface that the request is originated from. For global endpoint, this is 'global'; for us/eu multi-regional endpoint, this is 'us' or 'eu'; otherwise, this is the region where a request is served. The label can also have prefix, such as 'batch_', to indicate product breakdown.   
`publisher/online_serving/model_invocation_latencies` BETA ** _(project)_**   
Model invocation latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Model invocation latencies (prediction latencies)._   
`input_token_size`: The bucketized size of number of tokens in the prediction request.   
`output_token_size`: The bucketized size of number of tokens in the prediction response.   
`max_token_size`: The bucketized max size of number of tokens in the prediction request/response.   
`latency_type`: The type of latency for the prediction request (either model or overhead).   
`request_type`: The type of traffic of the request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`explicit_caching`: Whether the request uses explicit caching feature.   
`source`: The source/surface that the request is originated from. For global endpoint, this is 'global'; for us/eu multi-regional endpoint, this is 'us' or 'eu'; otherwise, this is the region where a request is served. The label can also have prefix, such as 'batch_', to indicate product breakdown.   
`publisher/online_serving/token_count` BETA ** _(project)_**   
Token count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Accumulated input/output token count._   
`max_token_size`: The bucketized max size of number of tokens in the prediction request/response.   
`type`: Type of token (input/output).   
`request_type`: The type of traffic of the request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`explicit_caching`: Whether the request uses explicit caching feature.   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`modality`: Modality of the input/output tokens.   
`source`: The source/surface that the token consumption is originated from. For global endpoint, this is 'global'; for us/eu multi-regional endpoint, this is 'us' or 'eu'; otherwise, this is the region where a request is served. The label can also have prefix, such as 'batch_', to indicate product breakdown.   
`publisher/online_serving/tokens` BETA ** _(project)_**   
Tokens   
`DELTA`, `DISTRIBUTION`, `1`   
**[aiplatform.googleapis.com/PublisherModel](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/PublisherModel)** |  _Input/output token count distribution._   
`max_token_size`: The bucketized max size of number of tokens in the prediction request/response.   
`type`: Type of token (input/output).   
`request_type`: The type of traffic of the request (dedicated/shared).   
`shared_request_type`: The breakdown of shared requests, such as priority/flex/standard.   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`modality`: Modality of the input/output tokens.   
`quota/concurrent/bidi_gen_concurrent_reqs_per_project_per_base_model/exceeded` ALPHA ** _(project)_**   
Bidi generate content concurrent requests per project per region per base model concurrent quota exceeded   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Concurrent exceeded on quota metric aiplatform.googleapis.com/bidi_gen_concurrent_reqs_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`base_model`: The base model custom dimension.   
`quota/concurrent/bidi_gen_concurrent_reqs_per_project_per_base_model/limit` ALPHA ** _(project)_**   
Bidi generate content concurrent requests per project per region per base model concurrent quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Concurrent limit on quota metric aiplatform.googleapis.com/bidi_gen_concurrent_reqs_per_project_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`base_model`: The base model custom dimension.   
`quota/concurrent/bidi_gen_concurrent_reqs_per_project_per_base_model_global/exceeded` ALPHA ** _(project)_**   
Bidi generate content concurrent requests per project per base model for global endpoint concurrent quota exceeded   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Concurrent exceeded on quota metric aiplatform.googleapis.com/bidi_gen_concurrent_reqs_per_project_per_base_model_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`base_model`: The base model custom dimension.   
`quota/concurrent/bidi_gen_concurrent_reqs_per_project_per_base_model_global/limit` ALPHA ** _(project)_**   
Bidi generate content concurrent requests per project per base model for global endpoint concurrent quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Concurrent limit on quota metric aiplatform.googleapis.com/bidi_gen_concurrent_reqs_per_project_per_base_model_global. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`base_model`: The base model custom dimension.   
`quota/eu_multi_region_online_prediction_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
EU multi-region online prediction input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
EU multi-region online prediction input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
EU multi-region online prediction input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
EU multi-region online prediction output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
EU multi-region online prediction output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
EU multi-region online prediction output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_requests_per_base_model/exceeded` BETA ** _(project)_**   
EU multi-region online prediction requests per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_requests_per_base_model/limit` BETA ** _(project)_**   
EU multi-region online prediction requests per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_requests_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_requests_per_base_model/usage` BETA ** _(project)_**   
EU multi-region online prediction requests per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_online_prediction_web_search_requests_per_publisher/exceeded` BETA ** _(project)_**   
EU multi-region online prediction web search requests per publisher quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_web_search_requests_per_publisher. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`publisher`: The multi-region publisher custom dimension.   
`quota/eu_multi_region_online_prediction_web_search_requests_per_publisher/limit` BETA ** _(project)_**   
EU multi-region online prediction web search requests per publisher quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_web_search_requests_per_publisher. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`publisher`: The multi-region publisher custom dimension.   
`quota/eu_multi_region_online_prediction_web_search_requests_per_publisher/usage` BETA ** _(project)_**   
EU multi-region online prediction web search requests per publisher quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_online_prediction_web_search_requests_per_publisher. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`publisher`: The multi-region publisher custom dimension.   
`quota/eu_multi_region_responses_image_inputs_per_base_model_per_minute/exceeded` BETA ** _(project)_**   
Olympus EU multi-region responses image inputs per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_image_inputs_per_base_model_per_minute. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_image_inputs_per_base_model_per_minute/limit` BETA ** _(project)_**   
Olympus EU multi-region responses image inputs per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_image_inputs_per_base_model_per_minute. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_image_inputs_per_base_model_per_minute/usage` BETA ** _(project)_**   
Olympus EU multi-region responses image inputs per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_responses_image_inputs_per_base_model_per_minute. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus EU multi-region responses input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus EU multi-region responses input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus EU multi-region responses input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_responses_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus EU multi-region responses output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus EU multi-region responses output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus EU multi-region responses output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_responses_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_requests_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus EU multi-region responses requests per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_requests_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_requests_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus EU multi-region responses requests per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_requests_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_requests_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus EU multi-region responses requests per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_responses_requests_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_total_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus EU multi-region responses total tokens (input + output) per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_total_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_total_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus EU multi-region responses total tokens (input + output) per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/eu_multi_region_responses_total_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/eu_multi_region_responses_total_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus EU multi-region responses total tokens (input + output) per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/eu_multi_region_responses_total_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/flex_requests_per_minute_per_project_per_base_model/exceeded` BETA ** _(project)_**   
Flex API requests per minute per project per base model. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/flex_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/flex_requests_per_minute_per_project_per_base_model/limit` BETA ** _(project)_**   
Flex API requests per minute per project per base model. quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/flex_requests_per_minute_per_project_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/flex_requests_per_minute_per_project_per_base_model/usage` BETA ** _(project)_**   
Flex API requests per minute per project per base model. quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/flex_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/generate_content_audio_input_per_base_model_id_and_resolution/exceeded` ALPHA ** _(project)_**   
Generate content requests with audio input per minute per project per region per base model and resolution quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_audio_input_per_base_model_id_and_resolution. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_audio_input_per_base_model_id_and_resolution/limit` ALPHA ** _(project)_**   
Generate content requests with audio input per minute per project per region per base model and resolution quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_audio_input_per_base_model_id_and_resolution. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_audio_input_per_base_model_id_and_resolution/usage` ALPHA ** _(project)_**   
Generate content requests with audio input per minute per project per region per base model and resolution quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_audio_input_per_base_model_id_and_resolution. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_audio_input_per_base_model_id_and_resolution_global/exceeded` ALPHA ** _(project)_**   
Generate content requests with audio input per minute per project per region per base model and resolution for global endpoint quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_audio_input_per_base_model_id_and_resolution_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_audio_input_per_base_model_id_and_resolution_global/limit` ALPHA ** _(project)_**   
Generate content requests with audio input per minute per project per region per base model and resolution for global endpoint quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_audio_input_per_base_model_id_and_resolution_global. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_audio_input_per_base_model_id_and_resolution_global/usage` ALPHA ** _(project)_**   
Generate content requests with audio input per minute per project per region per base model and resolution for global endpoint quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_audio_input_per_base_model_id_and_resolution_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_document_input_per_base_model_id_and_resolution/exceeded` ALPHA ** _(project)_**   
Generate content requests with document input per minute per project per region per base model and resolution quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_document_input_per_base_model_id_and_resolution. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_document_input_per_base_model_id_and_resolution/limit` ALPHA ** _(project)_**   
Generate content requests with document input per minute per project per region per base model and resolution quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_document_input_per_base_model_id_and_resolution. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_document_input_per_base_model_id_and_resolution/usage` ALPHA ** _(project)_**   
Generate content requests with document input per minute per project per region per base model and resolution quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_document_input_per_base_model_id_and_resolution. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_document_input_per_base_model_id_and_resolution_global/exceeded` ALPHA ** _(project)_**   
Generate content requests with document input per minute per project per region per base model and resolution for global endpoint quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_document_input_per_base_model_id_and_resolution_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_document_input_per_base_model_id_and_resolution_global/limit` ALPHA ** _(project)_**   
Generate content requests with document input per minute per project per region per base model and resolution for global endpoint quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_document_input_per_base_model_id_and_resolution_global. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_document_input_per_base_model_id_and_resolution_global/usage` ALPHA ** _(project)_**   
Generate content requests with document input per minute per project per region per base model and resolution for global endpoint quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_document_input_per_base_model_id_and_resolution_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_image_input_per_base_model_id_and_resolution/exceeded` ALPHA ** _(project)_**   
Generate content requests with image input per minute per project per region per base model and resolution quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_image_input_per_base_model_id_and_resolution. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_image_input_per_base_model_id_and_resolution/limit` ALPHA ** _(project)_**   
Generate content requests with image input per minute per project per region per base model and resolution quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_image_input_per_base_model_id_and_resolution. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_image_input_per_base_model_id_and_resolution/usage` ALPHA ** _(project)_**   
Generate content requests with image input per minute per project per region per base model and resolution quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_image_input_per_base_model_id_and_resolution. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_image_input_per_base_model_id_and_resolution_global/exceeded` ALPHA ** _(project)_**   
Generate content requests with image input per minute per project per region per base model and resolution for global endpoint quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_image_input_per_base_model_id_and_resolution_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_image_input_per_base_model_id_and_resolution_global/limit` ALPHA ** _(project)_**   
Generate content requests with image input per minute per project per region per base model and resolution for global endpoint quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_image_input_per_base_model_id_and_resolution_global. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_image_input_per_base_model_id_and_resolution_global/usage` ALPHA ** _(project)_**   
Generate content requests with image input per minute per project per region per base model and resolution for global endpoint quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_image_input_per_base_model_id_and_resolution_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Generate content input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/generate_content_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Generate content input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/generate_content_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Generate content input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/generate_content_requests_per_minute_per_project_per_base_model/exceeded` ALPHA ** _(project)_**   
Generate content requests per minute per project per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/generate_content_requests_per_minute_per_project_per_base_model/limit` ALPHA ** _(project)_**   
Generate content requests per minute per project per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_requests_per_minute_per_project_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/generate_content_requests_per_minute_per_project_per_base_model/usage` ALPHA ** _(project)_**   
Generate content requests per minute per project per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/generate_content_video_input_per_base_model_id_and_resolution/exceeded` ALPHA ** _(project)_**   
Generate content requests with video input per minute per project per region per base model and resolution quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_video_input_per_base_model_id_and_resolution. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_video_input_per_base_model_id_and_resolution/limit` ALPHA ** _(project)_**   
Generate content requests with video input per minute per project per region per base model and resolution quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_video_input_per_base_model_id_and_resolution. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_video_input_per_base_model_id_and_resolution/usage` ALPHA ** _(project)_**   
Generate content requests with video input per minute per project per region per base model and resolution quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_video_input_per_base_model_id_and_resolution. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_video_input_per_base_model_id_and_resolution_global/exceeded` ALPHA ** _(project)_**   
Generate content requests with video input per minute per project per region per base model and resolution for global endpoint quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/generate_content_video_input_per_base_model_id_and_resolution_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_video_input_per_base_model_id_and_resolution_global/limit` ALPHA ** _(project)_**   
Generate content requests with video input per minute per project per region per base model and resolution for global endpoint quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/generate_content_video_input_per_base_model_id_and_resolution_global. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/generate_content_video_input_per_base_model_id_and_resolution_global/usage` ALPHA ** _(project)_**   
Generate content requests with video input per minute per project per region per base model and resolution for global endpoint quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/generate_content_video_input_per_base_model_id_and_resolution_global. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_id_and_resolution`: The base model and resolution custom dimension.   
`mime_type`: The mimetype of the input.   
`quota/global_embed_content_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Global embed content input tokens quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_embed_content_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_embed_content_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Global embed content input tokens quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_embed_content_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_embed_content_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Global embed content input tokens quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_embed_content_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_embed_content_requests_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Global embed content requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_embed_content_requests_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_embed_content_requests_per_minute_per_base_model/limit` BETA ** _(project)_**   
Global embed content requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_embed_content_requests_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_embed_content_requests_per_minute_per_base_model/usage` BETA ** _(project)_**   
Global embed content requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_embed_content_requests_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Global generate content input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_generate_content_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Global generate content input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_generate_content_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Global generate content input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_generate_content_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_input_tokens_per_minute_per_base_model_and_tier/exceeded` DEPRECATED ** _(project)_**   
Global generate content input tokens for DevX users per min per project per base model and tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_generate_content_input_tokens_per_minute_per_base_model_and_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_and_tier`: The base model and tier custom dimension.   
`quota/global_generate_content_input_tokens_per_minute_per_base_model_and_tier/limit` DEPRECATED ** _(project)_**   
Global generate content input tokens for DevX users per min per project per base model and tier quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_generate_content_input_tokens_per_minute_per_base_model_and_tier. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_and_tier`: The base model and tier custom dimension.   
`quota/global_generate_content_input_tokens_per_minute_per_base_model_and_tier/usage` DEPRECATED ** _(project)_**   
Global generate content input tokens for DevX users per min per project per base model and tier quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_generate_content_input_tokens_per_minute_per_base_model_and_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_and_tier`: The base model and tier custom dimension.   
`quota/global_generate_content_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Global generate content output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_generate_content_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Global generate content output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_generate_content_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Global generate content output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_generate_content_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_requests_per_minute_per_project_per_base_model/exceeded` BETA ** _(project)_**   
Global generate content requests per minute per project per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_generate_content_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_requests_per_minute_per_project_per_base_model/limit` BETA ** _(project)_**   
Global generate content requests per minute per project per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_generate_content_requests_per_minute_per_project_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_requests_per_minute_per_project_per_base_model/usage` BETA ** _(project)_**   
Global generate content requests per minute per project per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_generate_content_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_generate_content_requests_per_minute_per_project_per_base_model_and_tier/exceeded` DEPRECATED ** _(project)_**   
Global generate content requests for DevX users per min per project per base model and tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_generate_content_requests_per_minute_per_project_per_base_model_and_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_and_tier`: The base model and tier custom dimension.   
`quota/global_generate_content_requests_per_minute_per_project_per_base_model_and_tier/limit` DEPRECATED ** _(project)_**   
Global generate content requests for DevX users per min per project per base model and tier quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_generate_content_requests_per_minute_per_project_per_base_model_and_tier. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_and_tier`: The base model and tier custom dimension.   
`quota/global_generate_content_requests_per_minute_per_project_per_base_model_and_tier/usage` DEPRECATED ** _(project)_**   
Global generate content requests for DevX users per min per project per base model and tier quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_generate_content_requests_per_minute_per_project_per_base_model_and_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_and_tier`: The base model and tier custom dimension.   
`quota/global_online_prediction_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Global online prediction input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_online_prediction_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The global base model custom dimension.   
`quota/global_online_prediction_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Global online prediction input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_online_prediction_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The global base model custom dimension.   
`quota/global_online_prediction_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Global online prediction input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_online_prediction_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The global base model custom dimension.   
`quota/global_online_prediction_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Global online prediction output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_online_prediction_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The global base model custom dimension.   
`quota/global_online_prediction_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Global online prediction output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_online_prediction_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The global base model custom dimension.   
`quota/global_online_prediction_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Global online prediction output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_online_prediction_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The global base model custom dimension.   
`quota/global_online_prediction_requests_per_base_model/exceeded` BETA ** _(project)_**   
Global online prediction requests per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The global base model custom dimension.   
`quota/global_online_prediction_requests_per_base_model/limit` BETA ** _(project)_**   
Global online prediction requests per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_online_prediction_requests_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The global base model custom dimension.   
`quota/global_online_prediction_requests_per_base_model/usage` BETA ** _(project)_**   
Global online prediction requests per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The global base model custom dimension.   
`quota/global_responses_image_inputs_per_base_model_per_minute/exceeded` BETA ** _(project)_**   
Olympus global responses image inputs per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_responses_image_inputs_per_base_model_per_minute. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_image_inputs_per_base_model_per_minute/limit` BETA ** _(project)_**   
Olympus global responses image inputs per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_responses_image_inputs_per_base_model_per_minute. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_image_inputs_per_base_model_per_minute/usage` BETA ** _(project)_**   
Olympus global responses image inputs per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_responses_image_inputs_per_base_model_per_minute. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_responses_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus global responses input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_responses_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus global responses input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_responses_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus global responses input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_responses_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_responses_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus global responses output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_responses_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus global responses output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_responses_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus global responses output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_responses_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_responses_requests_per_minute_per_project_per_base_model/exceeded` BETA ** _(project)_**   
Olympus global responses requests per minute per project per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_responses_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_requests_per_minute_per_project_per_base_model/limit` BETA ** _(project)_**   
Olympus global responses requests per minute per project per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_responses_requests_per_minute_per_project_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_requests_per_minute_per_project_per_base_model/usage` BETA ** _(project)_**   
Olympus global responses requests per minute per project per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_responses_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/global_responses_total_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus global responses total tokens (input + output) per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/global_responses_total_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_total_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus global responses total tokens (input + output) per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/global_responses_total_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/global_responses_total_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus global responses total tokens (input + output) per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/global_responses_total_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/long_running_online_prediction_requests_per_base_model/exceeded` ALPHA ** _(project)_**   
Long running online prediction requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/long_running_online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/long_running_online_prediction_requests_per_base_model/limit` ALPHA ** _(project)_**   
Long running online prediction requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/long_running_online_prediction_requests_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/long_running_online_prediction_requests_per_base_model/usage` ALPHA ** _(project)_**   
Long running online prediction requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/long_running_online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/non_regional_a2a_agent_get_requests/exceeded` ALPHA ** _(project)_**   
A2A Agent get requests like getTask, agent card, getPushNotificationConfigs. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_get_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_a2a_agent_get_requests/limit` ALPHA ** _(project)_**   
A2A Agent get requests like getTask, agent card, getPushNotificationConfigs. quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_get_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_a2a_agent_get_requests/usage` ALPHA ** _(project)_**   
A2A Agent get requests like getTask, agent card, getPushNotificationConfigs. quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_get_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_a2a_agent_post_requests/exceeded` ALPHA ** _(project)_**   
A2A Agent post requests like sendMessage, cancelTask, and createPushNotificationConfig. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_post_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_a2a_agent_post_requests/limit` ALPHA ** _(project)_**   
A2A Agent post requests like sendMessage, cancelTask, and createPushNotificationConfig. quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_post_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_a2a_agent_post_requests/usage` ALPHA ** _(project)_**   
A2A Agent post requests like sendMessage, cancelTask, and createPushNotificationConfig. quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_post_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_a2a_agent_stream_requests/exceeded` ALPHA ** _(project)_**   
A2A Agent stream post requests like sendMessageStream, resubscribe. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_stream_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_a2a_agent_stream_requests/limit` ALPHA ** _(project)_**   
A2A Agent stream post requests like sendMessageStream, resubscribe. quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_stream_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_a2a_agent_stream_requests/usage` ALPHA ** _(project)_**   
A2A Agent stream post requests like sendMessageStream, resubscribe. quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_a2a_agent_stream_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_internal_requests/exceeded` BETA ** _(project)_**   
Non-regional requests to internal API. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_internal_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_internal_requests/limit` BETA ** _(project)_**   
Non-regional requests to internal API. quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_internal_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_internal_requests/usage` BETA ** _(project)_**   
Non-regional requests to internal API. quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_internal_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_job_or_lro_submission_requests/exceeded` BETA ** _(project)_**   
Non-regional job or LRO submission requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_job_or_lro_submission_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_job_or_lro_submission_requests/limit` BETA ** _(project)_**   
Non-regional job or LRO submission requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_job_or_lro_submission_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_job_or_lro_submission_requests/usage` BETA ** _(project)_**   
Non-regional job or LRO submission requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_job_or_lro_submission_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_memory_bank_read_requests/exceeded` BETA ** _(project)_**   
Memory Bank Read Requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_memory_bank_read_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_memory_bank_read_requests/limit` BETA ** _(project)_**   
Memory Bank Read Requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_memory_bank_read_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_memory_bank_read_requests/usage` BETA ** _(project)_**   
Memory Bank Read Requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_memory_bank_read_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_memory_bank_write_requests/exceeded` BETA ** _(project)_**   
Memory Bank Write Requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_memory_bank_write_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_memory_bank_write_requests/limit` BETA ** _(project)_**   
Memory Bank Write Requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_memory_bank_write_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_memory_bank_write_requests/usage` BETA ** _(project)_**   
Memory Bank Write Requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_memory_bank_write_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_reasoning_engine_service_entities/exceeded` BETA ** _(project)_**   
Reasoning Engine Service Entities quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_entities. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_reasoning_engine_service_entities/limit` BETA ** _(project)_**   
Reasoning Engine Service Entities quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_entities. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_reasoning_engine_service_entities/usage` BETA ** _(project)_**   
Reasoning Engine Service Entities quota usage   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_entities. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_reasoning_engine_service_query_requests/exceeded` ALPHA ** _(project)_**   
Query Reasoning Engine requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_query_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_reasoning_engine_service_query_requests/limit` ALPHA ** _(project)_**   
Query Reasoning Engine requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_query_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_reasoning_engine_service_query_requests/usage` ALPHA ** _(project)_**   
Query Reasoning Engine requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_query_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_reasoning_engine_service_write_requests/exceeded` ALPHA ** _(project)_**   
Reasoning Engine Write Requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_write_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_reasoning_engine_service_write_requests/limit` ALPHA ** _(project)_**   
Reasoning Engine Write Requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_write_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_reasoning_engine_service_write_requests/usage` ALPHA ** _(project)_**   
Reasoning Engine Write Requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_reasoning_engine_service_write_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_resource_management_requests/exceeded` BETA ** _(project)_**   
Non-regional resource management (CRUD) requests (not for model serving) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_resource_management_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_resource_management_requests/limit` BETA ** _(project)_**   
Non-regional resource management (CRUD) requests (not for model serving) quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_resource_management_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_resource_management_requests/usage` BETA ** _(project)_**   
Non-regional resource management (CRUD) requests (not for model serving) quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_resource_management_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_session_event_append_requests/exceeded` ALPHA ** _(project)_**   
Session Event Append Requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_session_event_append_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_session_event_append_requests/limit` ALPHA ** _(project)_**   
Session Event Append Requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_session_event_append_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_session_event_append_requests/usage` ALPHA ** _(project)_**   
Session Event Append Requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_session_event_append_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/non_regional_session_write_requests/exceeded` ALPHA ** _(project)_**   
Vertex Session Write Requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/non_regional_session_write_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_session_write_requests/limit` ALPHA ** _(project)_**   
Vertex Session Write Requests quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/non_regional_session_write_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/non_regional_session_write_requests/usage` ALPHA ** _(project)_**   
Vertex Session Write Requests quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/non_regional_session_write_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/online_prediction_dedicated_requests_per_base_model_version/exceeded` BETA ** _(project)_**   
Online prediction dedicated requests per base model version quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/online_prediction_dedicated_requests_per_base_model_version. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_version`: The base model version custom dimension.   
`quota/online_prediction_dedicated_requests_per_base_model_version/limit` BETA ** _(project)_**   
Online prediction dedicated requests per base model version quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/online_prediction_dedicated_requests_per_base_model_version. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_version`: The base model version custom dimension.   
`quota/online_prediction_dedicated_requests_per_base_model_version/usage` BETA ** _(project)_**   
Online prediction dedicated requests per base model version quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/online_prediction_dedicated_requests_per_base_model_version. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_version`: The base model version custom dimension.   
`quota/online_prediction_dedicated_tokens_per_base_model_version/exceeded` BETA ** _(project)_**   
Online prediction dedicated tokens per minute per base model version quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/online_prediction_dedicated_tokens_per_base_model_version. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_version`: The base model version custom dimension.   
`quota/online_prediction_dedicated_tokens_per_base_model_version/limit` BETA ** _(project)_**   
Online prediction dedicated tokens per minute per base model version quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/online_prediction_dedicated_tokens_per_base_model_version. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model_version`: The base model version custom dimension.   
`quota/online_prediction_dedicated_tokens_per_base_model_version/usage` BETA ** _(project)_**   
Online prediction dedicated tokens per minute per base model version quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/online_prediction_dedicated_tokens_per_base_model_version. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model_version`: The base model version custom dimension.   
`quota/online_prediction_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Online prediction input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/online_prediction_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/online_prediction_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Online prediction input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/online_prediction_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/online_prediction_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Online prediction input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/online_prediction_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/online_prediction_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Online prediction output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/online_prediction_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/online_prediction_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Online prediction output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/online_prediction_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/online_prediction_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Online prediction output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/online_prediction_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/online_prediction_requests_per_base_model/exceeded` BETA ** _(project)_**   
Regional online prediction requests per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The regional base model custom dimension.   
`quota/online_prediction_requests_per_base_model/limit` BETA ** _(project)_**   
Regional online prediction requests per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/online_prediction_requests_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The regional base model custom dimension.   
`quota/online_prediction_requests_per_base_model/usage` BETA ** _(project)_**   
Regional online prediction requests per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The regional base model custom dimension.   
`quota/online_prediction_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Regional online prediction tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/online_prediction_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The regional base model custom dimension.   
`quota/online_prediction_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Regional online prediction tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/online_prediction_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The regional base model custom dimension.   
`quota/online_prediction_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Regional online prediction tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/online_prediction_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The regional base model custom dimension.   
`quota/responses_image_inputs_per_base_model_per_minute/exceeded` BETA ** _(project)_**   
Olympus responses image inputs per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/responses_image_inputs_per_base_model_per_minute. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_image_inputs_per_base_model_per_minute/limit` BETA ** _(project)_**   
Olympus responses image inputs per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/responses_image_inputs_per_base_model_per_minute. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_image_inputs_per_base_model_per_minute/usage` BETA ** _(project)_**   
Olympus responses image inputs per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/responses_image_inputs_per_base_model_per_minute. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/responses_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus responses input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/responses_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus responses input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/responses_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus responses input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/responses_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/responses_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus responses output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/responses_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus responses output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/responses_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus responses output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/responses_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/responses_requests_per_minute_per_project_per_base_model/exceeded` BETA ** _(project)_**   
Olympus responses requests per minute per project per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/responses_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_requests_per_minute_per_project_per_base_model/limit` BETA ** _(project)_**   
Olympus responses requests per minute per project per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/responses_requests_per_minute_per_project_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_requests_per_minute_per_project_per_base_model/usage` BETA ** _(project)_**   
Olympus responses requests per minute per project per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/responses_requests_per_minute_per_project_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/responses_total_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus responses total tokens (input + output) per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/responses_total_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_total_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus responses total tokens (input + output) per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/responses_total_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/responses_total_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus responses total tokens (input + output) per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/responses_total_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/us_multi_region_online_prediction_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
US multi-region online prediction input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
US multi-region online prediction input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
US multi-region online prediction input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
US multi-region online prediction output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
US multi-region online prediction output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
US multi-region online prediction output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_requests_per_base_model/exceeded` BETA ** _(project)_**   
US multi-region online prediction requests per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_requests_per_base_model/limit` BETA ** _(project)_**   
US multi-region online prediction requests per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_requests_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_requests_per_base_model/usage` BETA ** _(project)_**   
US multi-region online prediction requests per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_requests_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_online_prediction_web_search_requests_per_publisher/exceeded` BETA ** _(project)_**   
US multi-region online prediction web search requests per publisher quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_web_search_requests_per_publisher. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`publisher`: The multi-region publisher custom dimension.   
`quota/us_multi_region_online_prediction_web_search_requests_per_publisher/limit` BETA ** _(project)_**   
US multi-region online prediction web search requests per publisher quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_web_search_requests_per_publisher. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`publisher`: The multi-region publisher custom dimension.   
`quota/us_multi_region_online_prediction_web_search_requests_per_publisher/usage` BETA ** _(project)_**   
US multi-region online prediction web search requests per publisher quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_online_prediction_web_search_requests_per_publisher. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`publisher`: The multi-region publisher custom dimension.   
`quota/us_multi_region_responses_image_inputs_per_base_model_per_minute/exceeded` BETA ** _(project)_**   
Olympus US multi-region responses image inputs per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_image_inputs_per_base_model_per_minute. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_image_inputs_per_base_model_per_minute/limit` BETA ** _(project)_**   
Olympus US multi-region responses image inputs per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_image_inputs_per_base_model_per_minute. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_image_inputs_per_base_model_per_minute/usage` BETA ** _(project)_**   
Olympus US multi-region responses image inputs per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_responses_image_inputs_per_base_model_per_minute. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_input_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus US multi-region responses input tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_input_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus US multi-region responses input tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_input_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_input_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus US multi-region responses input tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_responses_input_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_output_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus US multi-region responses output tokens per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_output_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus US multi-region responses output tokens per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_output_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_output_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus US multi-region responses output tokens per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_responses_output_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_requests_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus US multi-region responses requests per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_requests_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_requests_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus US multi-region responses requests per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_requests_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_requests_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus US multi-region responses requests per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_responses_requests_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_total_tokens_per_minute_per_base_model/exceeded` BETA ** _(project)_**   
Olympus US multi-region responses total tokens (input + output) per minute per base model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_total_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_total_tokens_per_minute_per_base_model/limit` BETA ** _(project)_**   
Olympus US multi-region responses total tokens (input + output) per minute per base model quota limit   
`GAUGE`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current limit on quota metric aiplatform.googleapis.com/us_multi_region_responses_total_tokens_per_minute_per_base_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The multi-region base model custom dimension.   
`quota/us_multi_region_responses_total_tokens_per_minute_per_base_model/usage` BETA ** _(project)_**   
Olympus US multi-region responses total tokens (input + output) per minute per base model quota usage   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Current usage on quota metric aiplatform.googleapis.com/us_multi_region_responses_total_tokens_per_minute_per_base_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The multi-region base model custom dimension.   
`reasoning_engine/cpu/allocation_time` BETA ** _(project)_**   
Container CPU Allocation   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[aiplatform.googleapis.com/ReasoningEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/ReasoningEngine)** |  _Container CPU allocation in seconds._  
`reasoning_engine/memory/allocation_time` BETA ** _(project)_**   
Container Memory Allocation   
`DELTA`, `DOUBLE`, `GiBy.s`   
**[aiplatform.googleapis.com/ReasoningEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/ReasoningEngine)** |  _Container memory allocation in Gigabytes-seconds._  
`reasoning_engine/memory_bank/generate_memories_token_count` BETA ** _(project)_**   
Generate Memories Token Count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/ReasoningEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/ReasoningEngine)** |  _The number of tokens used in memory generation requests per Reasoning Engine._   
`type`: Type of token (input/output).   
`reasoning_engine/memory_bank/memory_lro_latency` BETA ** _(project)_**   
Memory LRO Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/ReasoningEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/ReasoningEngine)** |  _The total latency of memory LROs._   
`type`: Type of LRO i.e. generate_memories.   
`reasoning_engine/memory_bank/memory_mutation_count` BETA ** _(project)_**   
Memory Mutation Count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/ReasoningEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/ReasoningEngine)** |  _The number of memory mutation operations on the Reasoning Engine._   
`type`: Type of memory mutation operation. Generated labels: created/updated/deleted. CRUD labels: create_api/update_api/delete_api.   
`reasoning_engine/memory_bank/memory_retrieval_count` BETA ** _(project)_**   
Retrieved Memories Count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/ReasoningEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/ReasoningEngine)** |  _The number of memory entities retrieved per Reasoning Engine._  
`reasoning_engine/request_count` BETA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/ReasoningEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/ReasoningEngine)** |  _Number of requests reaching the instance._   
`type`: Type of request.   
`response_code`: HTTP response code.   
`response_code_class`: HTTP response code class.   
`reasoning_engine/request_latencies` BETA ** _(project)_**   
Request Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/ReasoningEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/ReasoningEngine)** |  _Distribution of request latency in milliseconds reaching the instance._   
`type`: Type of request.   
`response_code`: HTTP response code.   
`response_code_class`: HTTP response code class.   
`responses_image_inputs_per_base_model_per_minute` BETA ** _(project)_**   
Olympus responses image inputs per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus responses image inputs per minute per project per base model._   
`base_model`: The base model custom dimension.   
`responses_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus responses input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus responses input tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`responses_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus responses output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus responses output tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`responses_requests_per_minute_per_project_per_base_model` BETA ** _(project)_**   
Olympus responses requests per minute per project per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus responses requests per minute per project per base model._   
`base_model`: The base model custom dimension.   
`responses_total_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus responses total tokens (input + output) per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus responses total tokens per minute per project per base model._   
`base_model`: The base model custom dimension.   
`semantic_governance/evaluation_count` BETA ** _(project)_**   
Semantic Governance Policy Engine Evaluation Count   
`DELTA`, `INT64`, `1{evaluation}`   
**[aiplatform.googleapis.com/SemanticGovernancePolicyEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/SemanticGovernancePolicyEngine)** |  _Number of evaluations performed by the Semantic Governance Policy Engine in a given region._   
`final_verdict`: The verdict returned by the engine, for example, "ALLOW" or "DENY".   
`semantic_governance/evaluation_latencies` BETA ** _(project)_**   
Semantic Governance Policy Engine Evaluation Latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[aiplatform.googleapis.com/SemanticGovernancePolicyEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/SemanticGovernancePolicyEngine)** |  _Latency distribution of evaluations performed by the Semantic Governance Policy Engine in a given region._   
`final_verdict`: The verdict returned by the engine, for example, "ALLOW" or "DENY".   
`semantic_governance/evaluation_token_count` BETA ** _(project)_**   
Semantic Governance Policy Engine Evaluation Token Count   
`DELTA`, `INT64`, `1{token}`   
**[aiplatform.googleapis.com/SemanticGovernancePolicyEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/SemanticGovernancePolicyEngine)** |  _Number of tokens consumed during evaluations performed by the Semantic Governance Policy Engine in a given region._   
`category`: Kind of token used during evaluation, for example, "INPUT", "OUTPUT", or "THINKING".   
`semantic_governance/request_count` BETA ** _(project)_**   
Semantic Governance Policy Engine Request Count   
`DELTA`, `INT64`, `1{request}`   
**[aiplatform.googleapis.com/SemanticGovernancePolicyEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/SemanticGovernancePolicyEngine)** |  _Number of requests inspected by the Semantic Governance Policy Engine in a given region._   
`method`: HTTP method, for example, "POST", "GET", "DELETE", or "PUT".   
`status_code`: HTTP status code, for example, "200".   
`status`: Semantic outcome of the request, for example, "OK", "MODEL_ERROR", "EVALUATION_ERROR", or "INTERNAL_ERROR".   
`request_type`: Kind of intercepted egress, for example, "LLM", "TOOL", "OTHER", or "UNKNOWN".   
`semantic_governance/request_latencies` BETA ** _(project)_**   
Semantic Governance Policy Engine Request Latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[aiplatform.googleapis.com/SemanticGovernancePolicyEngine](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/SemanticGovernancePolicyEngine)** |  _Latency distribution of requests inspected by the Semantic Governance Policy Engine in a given region._   
`method`: HTTP method, for example, "POST".   
`status`: Semantic outcome of the request, for example, "OK", "MODEL_ERROR", "EVALUATION_ERROR", or "INTERNAL_ERROR".   
`request_type`: Kind of intercepted egress, for example, "LLM", "TOOL", "OTHER", or "UNKNOWN".   
`shared_generate_content_multimodal_per_continent_per_mimetype` BETA ** _(project)_**   
Generate content requests with multimodal input per minute per continent per mime type across all user projects   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Generate content requests with multimodal input per minute per continent per mime type across all user projects._   
`continent`: The continent custom dimension.   
`mime_type`: The mime type of the input.   
`shared_generate_content_multimodal_per_mimetype_per_base_model` BETA ** _(project)_**   
Generate content requests with multimodal input per mime type per minute per region per base model across all user projects   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Generate content requests with multimodal input per mime type per minute per region per base model across all user projects._   
`base_model`: The base model custom dimension.   
`mime_type`: The mime type of the input.   
`shared_generate_content_requests_per_minute_per_base_model` BETA ** _(project)_**   
Shared generate content requests per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Generate content requests per minute per base model across all user projects._   
`base_model`: The base model custom dimension.   
`shared_online_prediction_requests_per_base_model` BETA ** _(project)_**   
Shared online prediction requests per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Online prediction requests per minute per base model across all user projects._   
`base_model`: The base model custom dimension.   
`tuned_model/online_serving/consumed_token_throughput` BETA ** _(project)_**   
Token Throughput   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Overall throughput used (accounting for burndown rate) in terms of tokens for GenAI tuned models._   
`request_type`: Type of request (dedicated/shared).   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`modality`: Modality of the consumed tokens.   
`tuned_model/online_serving/first_token_latencies` BETA ** _(project)_**   
First token latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Distribution for the duration from request received to first token sent back to the client for GenAI tuned models since the last sample._   
`input_token_size`: The bucketized size of number of tokens in the prediction request.   
`output_token_size`: The bucketized size of number of tokens in the prediction response.   
`request_type`: The type of traffic of the request (dedicated/shared).   
`explicit_caching`: Whether the request uses explicit caching feature.   
`tuned_model/online_serving/model_invocation_latencies` BETA ** _(project)_**   
Model invocation latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Model invocation latencies (prediction latencies) for fine-tuned GenAI models._   
`input_token_size`: The bucketized size of number of tokens in the prediction request.   
`output_token_size`: The bucketized size of number of tokens in the prediction response.   
`latency_type`: The type of latency for the prediction request (either model or overhead).   
`request_type`: The type of traffic of the request (dedicated/shared).   
`explicit_caching`: Whether the request uses explicit caching feature.   
`tuned_model/online_serving/tokens` BETA ** _(project)_**   
Tokens   
`DELTA`, `DISTRIBUTION`, `1`   
**[aiplatform.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Endpoint)** |  _Input/output token count distribution for GenAI tuned models since the last sample._   
`max_token_size`: The bucketized max size of number of tokens in the prediction request/response.   
`type`: Type of token (input/output).   
`request_type`: The type of traffic of the request (dedicated/shared).   
`accounting_resource`: The identifier of the GCP project/folder/org to which quota is accounted to. Available for Provisioned Throughput only.   
`modality`: Modality of the input/output tokens.   
`us_multi_region_online_prediction_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
US multi-region online prediction input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _US multi-region online prediction input tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`us_multi_region_online_prediction_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
US multi-region online prediction output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _US multi-region online prediction output tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`us_multi_region_online_prediction_requests_per_base_model` BETA ** _(project)_**   
US multi-region online prediction requests per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _US multi-region online prediction requests per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`us_multi_region_online_prediction_web_search_requests_per_publisher` BETA ** _(project)_**   
US multi-region online prediction web search requests per publisher   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _US multi-region online prediction web search requests per project per publisher._   
`publisher`: The multi-region publisher custom dimension.   
`us_multi_region_responses_image_inputs_per_base_model_per_minute` BETA ** _(project)_**   
Olympus US multi-region responses image inputs per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus US multi-region responses image inputs per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`us_multi_region_responses_input_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus US multi-region responses input tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus US multi-region responses input tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`us_multi_region_responses_output_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus US multi-region responses output tokens per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus US multi-region responses output tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`us_multi_region_responses_requests_per_minute_per_base_model` BETA ** _(project)_**   
Olympus US multi-region responses requests per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus US multi-region responses requests per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
`us_multi_region_responses_total_tokens_per_minute_per_base_model` BETA ** _(project)_**   
Olympus US multi-region responses total tokens (input + output) per minute per base model   
`DELTA`, `INT64`, `1`   
**[aiplatform.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_aiplatform.googleapis.com/Location)** |  _Olympus US multi-region responses total tokens per minute per project per base model._   
`base_model`: The multi-region base model custom dimension.   
  
### alloydb

Metrics from [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `alloydb.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`cluster/last_backup_timestamp` GA ** _(project)_**   
Creation timestamp of the latest backup for the cluster   
`GAUGE`, `INT64`, `us`   
**[alloydb.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Cluster)** |  _Creation timestamp of the latest backup for the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`backup_type`: Type of backup (continuous, automated, on-demand)   
`cluster/storage/usage` GA ** _(project)_**   
Cluster storage usage   
`GAUGE`, `INT64`, `By`   
**[alloydb.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Cluster)** |  _The total AlloyDB storage in bytes across the entire cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/conn_pool/client_connections` GA ** _(project)_**   
Client connections   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Number of client connections per database grouped by status._   
`status`: Status of the client connection, one [ACTIVE, WAITING].   
`pooler`: Pooler id for differentiating individual connection pool instances.   
`database/conn_pool/client_connections_avg_wait_time` GA ** _(project)_**   
Average wait time   
`GAUGE`, `INT64`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Average wait time spent by clients waiting for a server connection per database in microseconds._   
`pooler`: Pooler id for differentiating individual connection pool instances.   
`database/conn_pool/num_pools` GA ** _(project)_**   
Number of connection pools   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Number of connection pools per database._   
`pooler`: Pooler id for differentiating individual connection pool instances.   
`database/conn_pool/server_connections` GA ** _(project)_**   
Server connections   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Number of server connections per database grouped by status._   
`status`: Status of the server connection, one of [ACTIVE, IDLE].   
`pooler`: Pooler id for differentiating individual connection pool instances.   
`database/postgresql/backends_for_top_databases` GA ** _(project)_**   
Number of connections to the instance per database   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The current number of connections per database to the instance for top 500 dbs. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/blks_hit_for_top_databases` GA ** _(project)_**   
Blocks hit per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Number of times Postgres found the requested block in the buffer cache per database for top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/blks_read_for_top_databases` GA ** _(project)_**   
Blocks miss per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Number of blocks read by Postgres that were not in the buffer cache per database for top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/committed_transactions_for_top_databases` GA ** _(project)_**   
Number of committed transactions per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Total number of transactions committed per database for top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/deadlock_count_for_top_databases` GA ** _(project)_**   
Number of deadlocks per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Total number of deadlocks detected in the instance per database for top 500 dbs. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/deleted_tuples_count_for_top_databases` GA ** _(project)_**   
Number of tuples deleted per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The total number of rows deleted per db for top 500 dbs as a result of the queries in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/fetched_tuples_count_for_top_databases` GA ** _(project)_**   
Number of tuples fetched per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The total number of rows fetched per db for top 500 dbs as a result of the queries in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/inserted_tuples_count_for_top_databases` GA ** _(project)_**   
Number of tuples inserted per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The total number of rows inserted per db for top 500 dbs as a result of the queries in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/insights/aggregate/execution_time` GA ** _(project)_**   
Execution time   
`DELTA`, `INT64`, `us{CPU}`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated query execution time since the last sample.This is the sum of CPU time, IO wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/io_time` GA ** _(project)_**   
IO time   
`DELTA`, `INT64`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated IO time since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`io_type`: The IO type (read/write).   
`database/postgresql/insights/aggregate/latencies` GA ** _(project)_**   
Latency   
`DELTA`, `DISTRIBUTION`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Query latency distribution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/lock_time` GA ** _(project)_**   
Lock time   
`DELTA`, `INT64`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated lock wait time since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`database/postgresql/insights/aggregate/row_count` GA ** _(project)_**   
Affected rows   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The number of retrieved or affected rows since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/shared_blk_access_count` GA ** _(project)_**   
Shared blocks cache access   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Shared blocks (regular tables and indexed) accessed by statement execution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`access_type`: The block access type, which can be one of ["hit" - Read from cache; "miss" - Read from disk].   
`database/postgresql/insights/perquery/execution_time` GA ** _(project)_**   
Execution time per query   
`DELTA`, `INT64`, `us{CPU}`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated execution times per user per database per query.This is the sum of CPU time, IO wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/io_time` GA ** _(project)_**   
IO time per query   
`DELTA`, `INT64`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated IO time since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`io_type`: The IO type (read/write).   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/latencies` GA ** _(project)_**   
Latency per query   
`DELTA`, `DISTRIBUTION`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Query latency distribution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/lock_time` GA ** _(project)_**   
Lock time per query   
`DELTA`, `INT64`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated lock wait time since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/row_count` GA ** _(project)_**   
Affected rows per query   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The number of retrieved or affected rows since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/shared_blk_access_count` GA ** _(project)_**   
Shared blocks cache access per query   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Shared blocks (regular tables & indexed) accessed by statement execution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`access_type`: The block access type, which can be one of ["hit" - Read from cache; "miss" - Read from disk].   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/pertag/execution_time` GA ** _(project)_**   
Execution time per tag   
`DELTA`, `INT64`, `us{CPU}`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated execution times since the last sample.This is the sum of CPU time, IO wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/io_time` GA ** _(project)_**   
IO time per tag   
`DELTA`, `INT64`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated IO time since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`io_type`: The IO type (read/write).   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/latencies` GA ** _(project)_**   
Latency per tag   
`DELTA`, `DISTRIBUTION`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Query latency distribution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/lock_time` GA ** _(project)_**   
Lock time per tag   
`DELTA`, `INT64`, `us`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Accumulated lock wait time since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/row_count` GA ** _(project)_**   
Affected rows per tag   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The number of retrieved or affected rows since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/shared_blk_access_count` GA ** _(project)_**   
Shared blocks cache accessed per tag   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Shared blocks (regular tables & indexed) accessed by statement execution. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`access_type`: The block access type, which can be one of ["hit" - Read from cache; "miss" - Read from disk].   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/new_connections_for_top_databases` GA ** _(project)_**   
Number of connections added per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Total number of new connections added per database for top 500 databases to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/returned_tuples_count_for_top_databases` GA ** _(project)_**   
Number of tuples scanned per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The total number of rows scanned per database for top 500 dbs while processing the queries in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/rolledback_transactions_for_top_databases` GA ** _(project)_**   
Number of rolledback transactions per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Total number of transactions rolledback per database for top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/statements_executed_count` GA ** _(project)_**   
Statements executed count   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Total count of statements executed in the instance per database per operation_type. Only available for instances with Query insights enabled. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`operation_type`: Name of the operation, one of [SELECT, UPDATE, INSERT, DELETE, MERGE, UTILITY, NOTHING, UNKNOWN].   
`database/postgresql/temp_bytes_written_for_top_databases` GA ** _(project)_**   
Bytes written to temporary files per database   
`DELTA`, `INT64`, `By`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The total amount of data(in bytes) written to temporary files by the queries per database for top 500 dbs. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/temp_files_written_for_top_databases` GA ** _(project)_**   
Temporary files used for writing data per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The number of temporary files used for writing data per database while performing internal algorithms like join, sort etc for top 500 dbs. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/tuples` GA ** _(project)_**   
Number of tuples (rows) in the database.   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _Number of tuples (rows) by state per database in the instance. This metric will only be exposed when the number of db’s is less than 50. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`state`: State of the tuples, one of [live, dead].   
`database/postgresql/updated_tuples_count_for_top_databases` GA ** _(project)_**   
Number of tuples updated per database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The total number of rows updated per db for top 500 dbs as a result of the queries in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/vacuum/oldest_transaction_age` GA ** _(project)_**   
Oldest transaction age   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Current age of the oldest uncommitted transaction. It's measured in the number of transactions that started since the oldest transaction. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`type`: type can be one of [running, prepared, replication_slot, replica].   
`database/postgresql/vacuum/transaction_id_utilization` GA ** _(project)_**   
Transaction ID utilization   
`GAUGE`, `DOUBLE`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The current percentage of transaction ID space consumed by the AlloyDB instance. It records the number of unvacuumed transactions as a percentage of the 2-billion maximum. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`database/postgresql/written_tuples_count_for_top_databases` GA ** _(project)_**   
Number of tuples written   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Database)** |  _The total number of rows written(inserted,updated,deleted) per db for top 500 dbs as a result of the queries in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/cpu/average_utilization` GA ** _(project)_**   
Mean CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Mean CPU utilization across all currently serving nodes of the instance from 0 to 100. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`instance/cpu/maximum_utilization` GA ** _(project)_**   
Maximum CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Maximum CPU utilization across all currently serving nodes of the instance from 0 to 100. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`instance/cpu/vcpus` GA ** _(project)_**   
vCPUs allocated per node   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of vCPUs allocated to each node in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/memory/min_available_memory` GA ** _(project)_**   
Minimum available memory   
`GAUGE`, `INT64`, `By`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The minimum available memory across all currently serving nodes of the instance. The available memory is an estimate of memory in bytes available for allocation on the VM including memory that is currently used, but can be potentially freed. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgres/abort_count` GA ** _(project)_**   
Instance abort count   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of transactions that were rolled back across all serving nodes of the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgres/autoscaler_total_connections` BETA ** _(project)_**   
Total connections per instance, used by the autoscaler   
`GAUGE`, `INT64`, `1`   
**[generic_node](https://docs.cloud.google.com/monitoring/api/resources#tag_generic_node)** |  _The number of active and idle connections to the AlloyDB instance across serving nodes of the instance, used by the autoscaler. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgres/average_connections` GA ** _(project)_**   
Mean connections per node   
`GAUGE`, `DOUBLE`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The mean number of active and idle connections to AlloyDB across serving nodes of the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgres/commit_count` GA ** _(project)_**   
Instance commit count   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of committed transactions across all serving nodes of the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgres/connections_limit` GA ** _(project)_**   
Limit on connections per node   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The current limit on the number of connections per node of the AlloyDB instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgres/instances` GA ** _(project)_**   
Number and status of nodes   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of nodes in the instance, along with their status, which can be either up or down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: The status of nodes in the instance, which can be one of [up, down].   
`instance/postgres/replication/maximum_lag` GA ** _(project)_**   
Maximum replication lag   
`GAUGE`, `INT64`, `ms`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The maximum replication time lag calculated across all serving read replicas of the instance. The replication time lag is derived from the replay_lag value. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`replica_instance_id`: The ID of the replica instance.   
`instance/postgres/replication/maximum_secondary_lag` GA ** _(project)_**   
Maximum secondary cluster replication lag   
`GAUGE`, `INT64`, `ms`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The maximum replication time lag calculated from primary to secondary cluster. The replication time lag is derived from the replay_lag value. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`application_name`: Application name.   
`client_addr`: Client address.   
`secondary_project`: The project of the secondary cluster.   
`secondary_location`: The location of the secondary cluster.   
`secondary_cluster_id`: The ID of the secondary cluster.   
`secondary_instance_id`: The ID of the secondary instance.   
`instance/postgres/replication/network_lag` GA ** _(project)_**   
Network lag   
`GAUGE`, `INT64`, `ms`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Time elapsed between flushing recent WAL locally and receiving notification that this standby server has written and flushed it (but not yet applied it). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`client_addr`: The IP address of the database client.   
`application_name`: The name of the database client application.   
`secondary_project`: Project of the secondary.   
`secondary_location`: Location of the secondary.   
`secondary_cluster_id`: Cluster ID of the secondary.   
`secondary_instance_id`: Instance ID of the secondary.   
`instance/postgres/replication/replicas` GA ** _(project)_**   
AlloyDB replica count   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of read replicas connected to the primary instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`state`: State of the replication, one of ["startup" - WAL sender is starting up; "catchup" - Connected standby of WAL sender is catching up with the primary; "streaming" - WAL sender is streaming changes after its connected standby server has caught up with the primary; "backup" - WAL sender is sending a backup; "stopping" - WAL sender is stopping].   
`replica_instance_id`: The ID of the replica instance.   
`instance/postgres/total_connections` GA ** _(project)_**   
Total connections per instance   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of active and idle connections to the AlloyDB instance across serving nodes of the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgres/transaction_count` GA ** _(project)_**   
Instance transaction count   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of committed and rolled back transactions across all serving nodes of the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgres/ultrafastcache_hitrate` GA ** _(project)_**   
Ultra Fast Cache hit rate per instance   
`GAUGE`, `DOUBLE`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Rate of hits in the Ultra Fast Cache for an instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/backends_by_state` GA ** _(project)_**   
Number of connections to the instance per connection state   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The current number of connections to the instance grouped by the state: idle, active, idle_in_transaction, idle_in_transaction_aborted, disabled, and fastpath_function_call. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`state`: State of the connection, one of [idle, active, idle_in_transaction, idle_in_transaction_aborted, disabled, fastpath_function_call].   
`instance/postgresql/backends_for_top_applications` GA ** _(project)_**   
Number of connections to the instance per application   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The current number of connections to the AlloyDB instance, grouped by applications for top 500 applications. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`application_name`: Name of the application connected to the instance.   
`instance/postgresql/blks_hit` GA ** _(project)_**   
Blocks hit   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of times Postgres found the requested block in the buffer cache. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/blks_read` GA ** _(project)_**   
Blocks miss   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of blocks read by Postgres that were not in the buffer cache. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/deadlock_count` GA ** _(project)_**   
Number of deadlocks   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of deadlocks detected in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/deleted_tuples_count` GA ** _(project)_**   
Number of tuples deleted   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of rows deleted while processing the queries in the instance since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/fetched_tuples_count` GA ** _(project)_**   
Number of tuples fetched   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of rows fetched while processing the queries in the instance since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/inserted_tuples_count` GA ** _(project)_**   
Number of tuples inserted   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of rows inserted while processing the queries in the instance since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/new_connections_count` GA ** _(project)_**   
Number of new connections added to the instance   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of new connections added to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/returned_tuples_count` GA ** _(project)_**   
Number of tuples scanned   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of rows scanned while processing the queries in the instance since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/temp_bytes_written_count` GA ** _(project)_**   
Bytes written to temporary files   
`DELTA`, `INT64`, `By`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The total amount of data(in bytes) written to temporary files by the queries while performing internal algorithms like join, sort etc. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/temp_files_written_count` GA ** _(project)_**   
Temporary files used for writing data   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The number of temporary files used for writing data in the instance while performing internal algorithms like join, sort etc. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/updated_tuples_count` GA ** _(project)_**   
Number of tuples updated   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of rows updated while processing the queries in the instance since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/postgresql/version` GA ** _(project)_**   
The version of the Postgres database.   
`GAUGE`, `STRING`, ``   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _The version of the Postgres database (e.g. POSTGRES_14, POSTGRES_15 etc)._  
`instance/postgresql/wait_count` GA ** _(project)_**   
Wait count   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Total number of times processes waited for each wait event in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`wait_event_type`: Type of the wait event.   
`wait_event_name`: Name of the wait event.   
`instance/postgresql/wait_time` GA ** _(project)_**   
Wait time   
`DELTA`, `DOUBLE`, `us`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Total elapsed wait time for each wait event in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`wait_event_type`: Type of the wait event.   
`wait_event_name`: Name of the wait event.   
`instance/postgresql/written_tuples_count` GA ** _(project)_**   
Number of tuples written   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Instance)** |  _Number of rows written while processing the queries in the instance since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/cpu/usage_time` GA ** _(project)_**   
Node CPU usage   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Rate of CPU utilization in the node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/database/logging/audit/backlog_bytes_count` BETA ** _(project)_**   
Audit log backlog size   
`GAUGE`, `INT64`, `By`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Audit log backlog size in bytes that have not yet been processed and uploaded to Cloud Logging. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/database/logging/audit/processed_bytes_count` BETA ** _(project)_**   
Processed audit log bytes   
`DELTA`, `INT64`, `By`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Total number of bytes of audit log data successfully processed. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/database/logging/audit/processed_entries_count` BETA ** _(project)_**   
Processed audit log entries   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Total number of entries of audit log data successfully processed. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/database/postgresql/backends_for_top_databases` BETA ** _(project)_**   
Number of connections to the node for each database   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The current number of connections to the node for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/blks_hit_for_top_databases` BETA ** _(project)_**   
Blocks hit for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The number of times Postgres found the requested block in the buffer cache for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/blks_read_for_top_databases` BETA ** _(project)_**   
Blocks miss for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The number of blocks read by Postgres that were not in the buffer cache for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/committed_transactions_for_top_databases` BETA ** _(project)_**   
Number of committed transactions for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The total number of transactions committed for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/deadlock_count_for_top_databases` BETA ** _(project)_**   
Number of deadlocks for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The total number of deadlocks detected in the node for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/fetched_tuples_count_for_top_databases` BETA ** _(project)_**   
Number of rows fetched for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The total number of rows fetched for database in the top 500 databases as a result of the queries in the node. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/insights/aggregate/execution_time` BETA ** _(project)_**   
Execution time   
`DELTA`, `INT64`, `us{CPU}`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The accumulated query execution time for each database since the last sample. This is the sum of CPU time, IO wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`node/database/postgresql/insights/aggregate/io_time` BETA ** _(project)_**   
IO time   
`DELTA`, `INT64`, `us`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The accumulated IO time since the last sample for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`io_type`: The IO type (read/write).   
`node/database/postgresql/insights/aggregate/latencies` BETA ** _(project)_**   
Latency   
`DELTA`, `DISTRIBUTION`, `us`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _Query latency distribution. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`node/database/postgresql/new_connections_for_top_databases` BETA ** _(project)_**   
Number of connections added for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The total number of new connections added for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/returned_tuples_count_for_top_databases` BETA ** _(project)_**   
Number of rows scanned for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The total number of rows scanned for each database in the top 500 databases while processing the queries in the node. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/rolledback_transactions_for_top_databases` BETA ** _(project)_**   
Number of rolled back transactions for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The total number of transactions rolled back for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/temp_bytes_written_for_top_databases` BETA ** _(project)_**   
Bytes written to temporary files for each database   
`DELTA`, `INT64`, `By`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The total amount of data (in bytes) written to temporary files by the queries for each database in the top 500 databases. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/database/postgresql/temp_files_written_for_top_databases` BETA ** _(project)_**   
Temporary files used for writing data for each database   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/NodeDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/NodeDatabase)** |  _The number of temporary files used for writing data for each database in the top 500 databases while performing internal algorithms such as join, sort, and so on. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/memory/available_memory` BETA ** _(project)_**   
Available memory   
`GAUGE`, `INT64`, `By`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _An estimate of memory in bytes available for allocation on the VM including memory that is currently used, but can be potentially freed. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/network/received_bytes_count` BETA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Received bytes over the network, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/network/sent_bytes_count` BETA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Sent bytes over the network, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/backends` GA ** _(project)_**   
Total connections per node   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The total number of connections across all databases for this node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/postgres/backends_by_state` GA ** _(project)_**   
Number of connections to the node per connection state   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The current number of connections to the node grouped by the state: idle, active, idle_in_transaction, idle_in_transaction_aborted, disabled, and fastpath_function_call. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`state`: State of the connection, one of [idle, active, idle_in_transaction, idle_in_transaction_aborted, disabled, fastpath_function_call].   
`node/postgres/backends_for_top_applications` BETA ** _(project)_**   
Number of connections to the node per application   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The current number of connections to the AlloyDB node, grouped by applications for top 500 applications. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`application_name`: Name of the application connected to the node.   
`node/postgres/blks_hit` BETA ** _(project)_**   
Blocks hit   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of times Postgres found the requested block in the buffer cache. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/blks_read` BETA ** _(project)_**   
Blocks miss   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of blocks read by Postgres that were not in the buffer cache. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/deadlock_count` BETA ** _(project)_**   
Number of deadlocks   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of deadlocks detected in the node. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/deleted_tuples_count` BETA ** _(project)_**   
Number of tuples deleted   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of rows deleted while processing the queries in the node since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/fetched_tuples_count` BETA ** _(project)_**   
Number of tuples fetched   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of rows fetched while processing the queries in the node since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/inserted_tuples_count` BETA ** _(project)_**   
Number of tuples inserted   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of rows inserted while processing the queries in the node since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/new_connections_count` BETA ** _(project)_**   
Number of new connections added to the node   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The number of new connections added to the node. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/replay_lag` GA ** _(project)_**   
Node replication lag   
`GAUGE`, `INT64`, `ms`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The lag in milliseconds for the individual node, comes from replay_lag in pg_stat_replication. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/postgres/returned_tuples_count` BETA ** _(project)_**   
Number of tuples scanned   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of rows scanned while processing the queries in the node since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/temp_bytes_written_count` BETA ** _(project)_**   
Bytes written to temporary files   
`DELTA`, `INT64`, `By`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The total amount of data (in bytes) written to temporary files by the queries while performing internal algorithms like join, sort etc. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/temp_files_written_count` BETA ** _(project)_**   
Temporary files used for writing data   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The number of temporary files used for writing data in the node while performing internal algorithms like join, sort etc. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/transaction_count` BETA ** _(project)_**   
Node transaction count   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The number of committed and rolled back transactions in the node since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/ultrafastcache_hitrate` GA ** _(project)_**   
Ultra Fast Cache hit rate per node   
`GAUGE`, `DOUBLE`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Rate of hits in the Ultra Fast Cache for a node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/postgres/updated_tuples_count` BETA ** _(project)_**   
Number of tuples updated   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of rows updated while processing the queries in the node since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/postgres/uptime` GA ** _(project)_**   
Node database availability   
`GAUGE`, `DOUBLE`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Rate of database availability in the node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/postgres/wait_count` GA ** _(project)_**   
Node Wait count   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Total number of times processes waited for each wait event in the node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`wait_event_type`: Type of the wait event.   
`wait_event_name`: Name of the wait event.   
`node/postgres/wait_time` GA ** _(project)_**   
Node Wait time   
`DELTA`, `DOUBLE`, `us`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Total elapsed wait time for each wait event in the node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`wait_event_type`: Type of the wait event.   
`wait_event_name`: Name of the wait event.   
`node/postgres/workload/distributed/tqf_query_count` BETA ** _(project)_**   
TQF query count   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _The cumulative count of queries handled by transparent query forwarding. Available on Postgres 16 and newer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: How the query was handled by transparent query forwarding. One of ["completed" - executed on a replica; "fallback" - executed on the primary; "disqualified" - could not be forwarded].   
`node/postgres/written_tuples_count` BETA ** _(project)_**   
Number of tuples written   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/InstanceNode)** |  _Number of rows written while processing the queries in the node since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`quota/storage_usage_per_cluster/exceeded` ALPHA ** _(project)_**   
Storage usage per cluster. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[alloydb.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric alloydb.googleapis.com/storage_usage_per_cluster. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`cluster`: The AlloyDB cluster.   
`quota/storage_usage_per_cluster/limit` ALPHA ** _(project)_**   
Storage usage per cluster. quota limit   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Location)** |  _Current limit on quota metric alloydb.googleapis.com/storage_usage_per_cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`cluster`: The AlloyDB cluster.   
`quota/storage_usage_per_cluster/usage` ALPHA ** _(project)_**   
Storage usage per cluster. quota usage   
`GAUGE`, `INT64`, `1`   
**[alloydb.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_alloydb.googleapis.com/Location)** |  _Current usage on quota metric alloydb.googleapis.com/storage_usage_per_cluster. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`cluster`: The AlloyDB cluster.   
  
### apigateway

Metrics from [API Gateway](https://docs.cloud.google.com/api-gateway/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `apigateway.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`proxy/request_count` BETA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[apigateway.googleapis.com/Gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_apigateway.googleapis.com/Gateway)** |  _Number of requests served by API gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code_class`: HTTP response code class (1xx, 2xx, 3xx, 4xx, 5xx).   
`api_config`: The name of API Config resource hosted by the Gateway.   
  
### apigee

Metrics from [Apigee](https://docs.apigee.com/). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `apigee.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`apihub/security/score` GA ** _(project)_**   
Security score   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/APIHubDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/APIHubDeployment)** |  _Current security score of an API Hub deployment based on an API Hub Security Profile. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`security_profile_id`: The ID of the API Hub Security Profile used to calculate the score.   
`cassandra/clientrequest_latency` BETA ** _(project)_**   
Apigee Cassandra client request latency   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Average read request latency in the 75th percentile range in microseconds for Apigee Cassandra. Sampled every 60 seconds._   
`scope`: Scope of the request.   
`unit`: Unit of the metric.   
`cassandra/compaction_pendingtasks` BETA ** _(project)_**   
Apigee Cassandra pending compaction tasks   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of pending compaction tasks for Apigee Cassandra. Sampled every 60 seconds._   
`unit`: unit of the metric.   
`cassandra/jvm_memory_bytes_committed` BETA ** _(project)_**   
Apigee Cassandra bytes committed per area   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of bytes committed for Apigee Cassandra JVM heap. Sampled every 60 seconds._   
`area`: Area of the memory such as heap or non-heap.   
`cassandra/jvm_memory_bytes_init` BETA ** _(project)_**   
Apigee Cassandra initial memory bytes   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Initial memory usage in bytes for Apigee Cassandra JVM heap. Sampled every 60 seconds._   
`area`: Area of the memory such as heap or non-heap.   
`cassandra/jvm_memory_bytes_max` BETA ** _(project)_**   
Apigee Cassandra max bytes of memory   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Maximum memory usage in bytes for Apigee Cassandra JVM heap. Sampled every 60 seconds._   
`area`: Area of the memory such as heap or non-heap.   
`cassandra/jvm_memory_bytes_used` BETA ** _(project)_**   
Apigee Cassandra used JVM memory bytes   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Memory usage in bytes for Apigee Cassandra JVM heap. Sampled every 60 seconds._   
`area`: Area of the memory such as heap or non-heap.   
`cassandra/jvm_memory_pool_bytes_committed` BETA ** _(project)_**   
Apigee Cassandra bytes committed per memory pool   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Memory usage in bytes committed per Apigee Cassandra JVM pool. Sampled every 60 seconds._   
`pool`: Name of the cassandra memory pool.   
`cassandra/jvm_memory_pool_bytes_init` BETA ** _(project)_**   
Apigee Cassandra initial bytes of JVM memory pool   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Initial memory usage in bytes for Apigee Cassandra JVM pool. Sampled every 60 seconds._   
`pool`: Name of the cassandra memory pool.   
`cassandra/jvm_memory_pool_bytes_max` BETA ** _(project)_**   
Apigee Cassandra JVM memory pool bytes max   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Maximum memory usage in bytes for Apigee Cassandra JVM pool. Sampled every 60 seconds._   
`pool`: Name of the cassandra memory pool.   
`cassandra/jvm_memory_pool_bytes_used` BETA ** _(project)_**   
Apigee Cassandra bytes per memory pool   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Memory usage in bytes per Apigee Cassandra JVM pool. Sampled every 60 seconds._   
`pool`: Name of the cassandra memory pool.   
`cassandra/process_cpu_seconds_total` BETA ** _(project)_**   
Apigee Cassandra user and system CPU in seconds   
`CUMULATIVE`, `DOUBLE`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _User and system CPU time spent in seconds for Apigee Cassandra. Sampled every 60 seconds._  
`cassandra/process_max_fds` BETA ** _(project)_**   
Apigee Cassandra process max file descriptors   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Maximum number of open file descriptors for Apigee Cassandra. Sampled every 60 seconds._  
`cassandra/process_open_fds` BETA ** _(project)_**   
Apigee Cassandra process open file descriptors   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of open file descriptors for Apigee Cassandra. Sampled every 60 seconds._  
`cassandra/tablerequests_latency` ALPHA ** _(project)_**   
Apigee Cassandra table level requests latency   
`GAUGE`, `DOUBLE`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Read and Write Request latency for all the tablesin Apigee Cassandra. Sampled every 60 seconds._   
`keyspace`: Keyspace name of the request.   
`table`: Table name of the request.   
`scope`: Scope of the request.   
`percentile`: Type of latency.   
`cassandra/tablerequests_rate` ALPHA ** _(project)_**   
Apigee Cassandra table level requests rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Read and Write Request rate for all the tablesin Apigee Cassandra. Sampled every 60 seconds._   
`keyspace`: Keyspace name of the request.   
`table`: Table name of the request.   
`scope`: Scope of the request.   
`connectagent/completed_rpcs_count` ALPHA ** _(project)_**   
Apigee Connect Agent completed RPCs count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of RPCs completed by Apigee Connect Agent. Sampled every 60 seconds._   
`method`: GRPC client method.   
`status`: GRPC client Status.   
`connectagent/dropped_requests` ALPHA ** _(project)_**   
Apigee Connect Agent dropped requests   
`CUMULATIVE`, `DISTRIBUTION`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of dropped requests by Apigee Connect Agent per RPC. Sampled every 60 seconds._   
`method`: GRPC client method.   
`connectagent/dropped_responses` ALPHA ** _(project)_**   
Apigee Connect Agent dropped responses   
`CUMULATIVE`, `DISTRIBUTION`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of dropped responses by Apigee Connect Agent per RPC. Sampled every 60 seconds._   
`method`: GRPC client method.   
`connectagent/received_bytes` ALPHA ** _(project)_**   
Apigee Connect Agent received bytes   
`CUMULATIVE`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of bytes received by Apigee Connect Agent per RPC. Sampled every 60 seconds._   
`method`: GRPC client method.   
`connectagent/received_messages` ALPHA ** _(project)_**   
Apigee Connect Agent received messages   
`CUMULATIVE`, `DISTRIBUTION`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of messages received by Apigee Connect Agent per RPC. Sampled every 60 seconds._   
`method`: GRPC client method.   
`connectagent/sent_bytes` ALPHA ** _(project)_**   
Apigee Connect Agent sent bytes   
`CUMULATIVE`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of bytes sent by Apigee Connect Agent per RPC. Sampled every 60 seconds._   
`method`: GRPC client method.   
`connectagent/sent_messages` ALPHA ** _(project)_**   
Apigee Connect Agent sent messages   
`CUMULATIVE`, `DISTRIBUTION`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of messages sent by Apigee Connect Agent per RPC. Sampled every 60 seconds._   
`method`: GRPC client method.   
`connectagent/stream_liveness_time` ALPHA ** _(project)_**   
Apigee Connect Agent stream liveness time   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of stream liveness time by Apigee Connect Agent per RPC. Sampled every 60 seconds._   
`method`: GRPC client method.   
`environment/active` BETA ** _(project)_**   
Apigee active environment   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Environment)** |  _Number of current environments attached to Apigee instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`type`: Type of the Apigee environment.   
`analytics_state`: State of the Apigee Analytics add-on, one of [ENABLED, ENABLING, DISABLED, DISABLING].   
`api_security_state`: State of the Apigee API Security add-on, one of [ENABLED, ENABLING, DISABLED, DISABLING].   
`environment/anomaly_count` BETA ** _(project)_**   
Apigee anomaly event count   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Environment)** |  _Total number of anomalies observed in the Apigee environment. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`severity`: Anomaly severity (slight, moderate, severe).   
`direction`: Anomaly direction (jump/drop).   
`anomaly_type`: Type of Apigee anomaly (example: traffic_5xx).   
`environment/api_call_count` BETA ** _(project)_**   
Apigee environment API call count   
`DELTA`, `INT64`, `1`   
**[apigee.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Environment)** |  _Number of API calls processed by an Apigee environment since the last sample was recorded. Sampled every 60 seconds._   
`proxy_deployment_type`: Type of the Apigee environment.   
`environment/instance/gateway_nodes` BETA ** _(project)_**   
Apigee gateway nodes   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/EnvironmentInstance](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/EnvironmentInstance)** |  _Number of Apigee gateway nodes in an environment attached to an instance. Sampled every 60 seconds._   
`node`: Apigee node.   
`envoy/redis/commands/evalsha/error` ALPHA ** _(project)_**   
Apigee Redis Envoy evalsha error   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of error evalsha commands to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/commands/evalsha/latency` ALPHA ** _(project)_**   
Apigee Redis Envoy evalsha latency   
`CUMULATIVE`, `DISTRIBUTION`, `usec`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total amount of time in microseconds for execution of evalsha command. Sampled every 60 seconds._  
`envoy/redis/commands/evalsha/success` ALPHA ** _(project)_**   
Apigee Redis Envoy evalsha success   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of successful evalsha commands to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/commands/evalsha/total` ALPHA ** _(project)_**   
Apigee Redis Envoy evalsha Total   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of evalsha commands to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/commands/get/error` ALPHA ** _(project)_**   
Apigee Redis Envoy get error   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of error get commands to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/commands/get/latency` ALPHA ** _(project)_**   
Apigee Redis Envoy get latency   
`CUMULATIVE`, `DISTRIBUTION`, `usec`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total amount of time in microseconds for execution of get command. Sampled every 60 seconds._  
`envoy/redis/commands/get/success` ALPHA ** _(project)_**   
Apigee Redis Envoy get success   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of successful get commands to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/commands/get/total` ALPHA ** _(project)_**   
Apigee Redis Envoy get total   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of get commands to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/downstream_cx_active` ALPHA ** _(project)_**   
Apigee Redis Envoy active connections   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of current active connections to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/downstream_cx_total` ALPHA ** _(project)_**   
Apigee Redis Envoy total connections   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of connections to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/downstream_rq_active` ALPHA ** _(project)_**   
Apigee Redis Envoy active requests   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of current active requests to Apigee Redis Envoy. Sampled every 60 seconds._  
`envoy/redis/downstream_rq_total` ALPHA ** _(project)_**   
Apigee Redis Envoy total requests   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of requests received by Apigee Redis Envoy. Sampled every 60 seconds._  
`mint/latencies_percentile` BETA ** _(project)_**   
Percentile of Apigee Monetization response latencies   
`GAUGE`, `DOUBLE`, `ms`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)** |  _Percentile of all Monetized response latencies to a request. Sampled every 60 seconds._   
`mint_status`: Status of Monetized request.   
`percentile`: Apigee proxy response latencies Percentile.   
`time_window`: Apigee Proxy response latencies percentile aggregation time window.   
`mint/request_count` BETA ** _(project)_**   
Apigee Monetization request cumulative count   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)** |  _Total number of requests received by the Montized Api Proxy. Sampled every 60 seconds._  
`mint/response_count` BETA ** _(project)_**   
Apigee Monetization response cumulative count   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)** |  _Total number of complete Monetized requests processed by API proxy. Sampled every 60 seconds._   
`mint_status`: Status of Monetized request.   
`policyv2/latencies_percentile` BETA ** _(project)_**   
Percentile of Apigee policy response latencies   
`GAUGE`, `DOUBLE`, `ms`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)** |  _Percentile of all API policy responseto a request. Sampled every 60 seconds._   
`policy_name`: Name of the policy.   
`percentile`: Apigee policy response latencies Percentile.   
`time_window`: Apigee policy response latencies percentile aggregation time window.   
`proxy/details` BETA ** _(project)_**   
Apigee proxy details   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/Proxy](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Proxy)** |  _Details relevant to the proxy that is deployed to an Apigee environment. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`proxy_deployment_type`: Deployment type of the Apigee proxy.   
`proxy/latencies` BETA ** _(project)_**   
Apigee proxy latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[apigee.googleapis.com/Proxy](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Proxy)** |  _A distribution of the latency calculated from when the request was received by the Apigee proxy until the response sent from the Apigee proxy to the client. Time includes the Apigee proxy overhead and the target server time. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`method`: HTTP method.   
`proxy/request_count` BETA ** _(project)_**   
Apigee proxy request count   
`DELTA`, `INT64`, `1`   
**[apigee.googleapis.com/Proxy](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Proxy)** |  _Number of requests sent to the Apigee proxy since the last sample was recorded. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`method`: HTTP method.   
`proxy/response_count` BETA ** _(project)_**   
Apigee proxy response count   
`DELTA`, `INT64`, `1`   
**[apigee.googleapis.com/Proxy](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Proxy)** |  _Number of responses sent by the Apigee API proxy since the last sample was recorded. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`method`: HTTP method.   
`response_code`: (INT64) HTTP status code of the response.   
`fault_code`: Apigee fault code to help you diagnose issues.   
`fault_source`: Suspected cause of the fault, one of [apigee, target, policy].   
`apigee_fault`: (BOOL) Indicates whether Apigee caused the fault.   
`proxyv2/details` BETA ** _(project)_**   
Apigee proxy details   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)** |  _Apigee proxy details deployed to an Apigee environment. Sampled every 60 seconds._   
`proxy_deployment_type`: Deployment type of the Apigee proxy.   
`proxyv2/latencies_percentile` BETA ** _(project)_**   
Percentile of Apigee proxy response latencies   
`GAUGE`, `DOUBLE`, `ms`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)** |  _Percentile of all API proxy responseto a request. Sampled every 60 seconds._   
`method`: HTTP method.   
`percentile`: Apigee proxy response latencies Percentile.   
`time_window`: Apigee Proxy response latencies percentile aggregation time window.   
`proxyv2/request_count` ALPHA ** _(project)_**   
Apigee proxy request cumulative count   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)** |  _Total number of requests received by the Apigee API proxy. Sampled every 60 seconds._   
`method`: HTTP method.   
`proxyv2/response_count` ALPHA ** _(project)_**   
Apigee proxy response cumulative count   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)** |  _Total number of responses sent by the Apigee API proxy. Sampled every 60 seconds._   
`method`: HTTP method.   
`response_code`: HTTP response code.   
`fault_code`: Apigee fault code that provides useful information to help you diagnose issues.   
`fault_source`: Information about the suspected cause of the fault, such as API proxy, target, or the Apigee infrastructure.   
`apigee_fault`: Boolean that is "true" if the fault is apigee caused and "false" otherwise.   
`security/detected_request_count` BETA ** _(project)_**   
Apigee API Security detected request count   
`DELTA`, `INT64`, `1`   
**[apigee.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Environment)** |  _Number of API requests detected by Apigee Advanced API Security abuse detection, since the last sample. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`proxy`: Apigee API proxy.   
`security/detected_request_count_by_rule` BETA ** _(project)_**   
Apigee API Security detected request count by rule   
`DELTA`, `INT64`, `1`   
**[apigee.googleapis.com/SecurityDetectionRule](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/SecurityDetectionRule)** |  _Number of API requests detected by Apigee Advanced API Security abuse detection and grouped by detection rule, since the last sample. Note: Sum of request count across detection_rule label does not produce total detected request count, instead to get the total number of detected requests use apigee.googleapis.com/security/detected_request_count. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`proxy`: Apigee API proxy.   
`security/environment_score` BETA ** _(project)_**   
Security score of Apigee environment   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/SecurityProfileEnvironmentAssociation](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/SecurityProfileEnvironmentAssociation)** |  _Current security score of Apigee environment based on Advanced API Security assessment. This value is measured at least once every 3 hours. There might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval until the next measurement. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._  
`security/incident_request_count` BETA ** _(project)_**   
Apigee API Security incident request count   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/SecurityIncident](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/SecurityIncident)** |  _Total Number of API requests detected to be a part of an Apigee API Security incident. This value is measured once every hour. There might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval throughout the hour. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`proxy`: Apigee API proxy.   
`security/incident_request_count_by_rule` BETA ** _(project)_**   
Apigee API Security incident request count by detection rule   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/SecurityIncident](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/SecurityIncident)** |  _Total number of API requests detected to be a part of an Apigee API Security incident grouped by detection rule. This value is measured once every hour. There might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval throughout the hour. For this metric, the sampling period is a reporting period, not a measurement period. Note: Sum of request count across detection_rule label does not produce total request count for a security incident, instead to get the total number of requests in a security incident use apigee.googleapis.com/security/incident_request_count. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`detection_rule`: Apigee API Security detection rule, such as "Flooder" or "Static Content Scraper".   
`security/proxy_score` BETA ** _(project)_**   
Security score of Apigee API proxy   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/SecurityProfileEnvironmentAssociation](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/SecurityProfileEnvironmentAssociation)** |  _Current security score of Apigee API proxy based on Advanced API Security proxy assessment. This value is measured at least once every 3 hours. There might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval until the next measurement. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`proxy`: Apigee API proxy.   
`security/request_count` BETA ** _(project)_**   
Apigee API Security request count   
`DELTA`, `INT64`, `1`   
**[apigee.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Environment)** |  _Number of API requests processed by Apigee Advanced API Security, since the last sample. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`proxy`: Apigee API proxy.   
`security/score` GA ** _(project)_**   
Security score   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/SecurityAssessmentResult](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/SecurityAssessmentResult)** |  _Current security score of a deployed resource based on an Apigee Risk Assessment V2 Security profile. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._  
`security/source_score` BETA ** _(project)_**   
Security score of Apigee sources   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/SecurityProfileEnvironmentAssociation](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/SecurityProfileEnvironmentAssociation)** |  _Current security score of Apigee environment based on Advanced API Security source assessment. This value is measured at least once every 3 hours. There might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval until the next measurement. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._  
`security/target_score` BETA ** _(project)_**   
Security score of Apigee target server   
`GAUGE`, `INT64`, `1`   
**[apigee.googleapis.com/SecurityProfileEnvironmentAssociation](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/SecurityProfileEnvironmentAssociation)** |  _Current security score of Apigee target server based on Advanced API Security target assessment. This value is measured at least once every 3 hours. There might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval until the next measurement. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`target_server`: Apigee target server.   
`server/fault_count` BETA ** _(project)_**   
Apigee server fault count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of faults returned by the Apigee server application. For example, the apigee-runtime, apigee--synchronizer, or apigee-udca server application. Sampled every 60 seconds._   
`source`: Source of the fault.   
`server/latencies` BETA ** _(project)_**   
Apigee server latencies   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total amount of time in milliseconds for the Apigee application server to process the requests and responses. For example, the apigee-runtime, apigee-synchronizer, or apigee-udca server application. Sampled every 60 seconds._   
`method`: HTTP method.   
`response_code`: HTTP response code.   
`type`: Type of service.   
`server/nio` BETA ** _(project)_**   
Apigee server nio   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of open sockets. Sampled every 60 seconds._   
`state`: State of the NIO threads.   
`server/num_threads` BETA ** _(project)_**   
Apigee server thread count   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of active non-daemon threads in the Apigee server. Sampled every 60 seconds._  
`server/request_count` BETA ** _(project)_**   
Apigee server request count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of requests received by the Apigee server application. For example, the apigee-runtime, apigee-synchronizer, or apigee-udca server application. Sampled every 60 seconds._   
`method`: HTTP method.   
`type`: Type of service.   
`server/response_count` BETA ** _(project)_**   
Apigee server response count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of responses sent by the Apigee server application. For example, the apigee-runtime, apigee-synchronizer, or apigee-udca server application. Sampled every 60 seconds._   
`method`: HTTP method.   
`response_code`: HTTP response code.   
`type`: Type of service.   
`target/latencies` BETA ** _(project)_**   
Apigee target latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[apigee.googleapis.com/Target](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Target)** |  _A distribution of the latency calculated from when the request was sent to the Apigee target until the response was received by the Apigee proxy. Time does not include the Apigee API proxy overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`type`: Type of target interaction, one of [target, service_callout, external_callout].   
`method`: HTTP method.   
`target/request_count` BETA ** _(project)_**   
Apigee target request count   
`DELTA`, `INT64`, `1`   
**[apigee.googleapis.com/Target](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Target)** |  _Number of requests sent to the Apigee target since the last sample was recorded. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`type`: Type of target interaction, one of [target, service_callout, external_callout].   
`method`: HTTP method.   
`target/response_count` BETA ** _(project)_**   
Apigee target response count   
`DELTA`, `INT64`, `1`   
**[apigee.googleapis.com/Target](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Target)** |  _Number of responses received from the Apigee target since the last sample was recorded. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`type`: Type of target interaction, one of [target, service_callout, external_callout].   
`method`: HTTP method.   
`response_code`: (INT64) HTTP status code of the response.   
`targetv2/latencies_percentile` BETA ** _(project)_**   
Percentile of Apigee proxy target response latencies   
`GAUGE`, `DOUBLE`, `ms`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)**   
**[apigee.googleapis.com/TargetV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/TargetV2)** |  _Percentile of all API proxy target responseto a request. Sampled every 60 seconds._   
`method`: HTTP method.   
`percentile`: Apigee proxy target response latencies Percentile.   
`time_window`: Apigee Proxy target response latencies percentile aggregation time window.   
`targetv2/request_count` ALPHA ** _(project)_**   
Apigee target request cumulative count   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)**   
**[apigee.googleapis.com/TargetV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/TargetV2)** |  _Total number of requests received by the Apigee API proxy target. Sampled every 60 seconds._   
`method`: HTTP method.   
`target_type`: Type of target such as service callout.   
`target_endpoint`: Target endpoint URL.   
`targetv2/response_count` ALPHA ** _(project)_**   
Apigee target response cumulative count   
`CUMULATIVE`, `INT64`, `1`   
**[apigee.googleapis.com/ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2)**   
**[apigee.googleapis.com/TargetV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/TargetV2)** |  _Total number of responses sent by the Apigee API proxy target. Sampled every 60 seconds._   
`method`: HTTP method.   
`target_type`: Type of target such as service callout.   
`target_endpoint`: Target endpoint URL.   
`response_code`: HTTP response code.   
`udca/disk/used_bytes` BETA ** _(project)_**   
Apigee UDCA disk used bytes   
`GAUGE`, `DOUBLE`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Amount of bytes used by the data files on the data collection pod's disk. Sampled every 60 seconds._   
`dataset`: Type of data.   
`state`: State of the data file.   
`udca/server/local_file_count` BETA ** _(project)_**   
Apigee UDCA server local file count   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of files on disk in the data collection pod. Ideally, the value will be close to 0. A consistently high value indicates that files are not being uploaded or that the Apigee Universal Data Collection Agent (UDCA) server application is not able to upload them fast enough. This value is computed every 60 seconds and does not reflect the state of the Apigee UDCA server application in real time. Sampled every 60 seconds._   
`dataset`: Type of data.   
`state`: State of the data file.   
`udca/server/local_file_latest_ts` BETA ** _(project)_**   
Apigee UDCA server timestamp difference between current time and latest file   
`GAUGE`, `INT64`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Apigee Universal Data Collection Agent (UDCA) server timestamp difference between current time and latest file. Sampled every 60 seconds._   
`dataset`: Type of data.   
`state`: State of the data file.   
`udca/server/local_file_oldest_ts` BETA ** _(project)_**   
Apigee UDCA server timestamp difference between current time and oldest file   
`GAUGE`, `INT64`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Time that the oldest file in the dataset was created in seconds since epoch. If the Apigee Universal Data Collection Agent (UDCA) server application is up to date and there are no files waiting to be uploaded when this metric is computed, then this value will be 0. If this value increases, it indicates that old files are still on disk. The metric is computed every 60 seconds and does not reflect the state of the Apigee UDCA server application in real time. Sampled every 60 seconds._   
`dataset`: Type of data.   
`state`: State of the data file.   
`udca/server/pruned_file_count` BETA ** _(project)_**   
Apigee UDCA pruned file count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of files that have been deleted because their Time To Life (TTL) was beyond a set threshold. The dataset can include API, trace, and others, and state can be UPLOADED, FAILED, or DISCARDED. Sampled every 60 seconds._   
`dataset`: Type of data.   
`state`: State of the data file.   
`udca/server/retry_cache_size` BETA ** _(project)_**   
Apigee UDCA outstanding number of entries in retry cache   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of files, by dataset, that the Apigee Universal Data Collection Agent (UDCA) server application is retrying to upload. After 3 retries per file, the UDCA moves the file to the /failed subdirectory and removes it from this cache. An increase in this value over time implies that the cache is not being cleared. Sampled every 60 seconds._   
`dataset`: Type of data.   
`udca/server/total_latencies` BETA ** _(project)_**   
Apigee UDCA server total latencies   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total amount of time in seconds for a data file to be created and uploaded successfully by the Apigee Universal Data Collection Agent (UDCA) server application. Buckets will be 100 ms, 250 ms, 500 ms, 1 s, 2 s, 4 s, 8 s, 16 s, 32 s, and 64 s. The metrics will display a histogram for total latency from file creation time to successful upload time. Sampled every 60 seconds._   
`dataset`: Type of data.   
`udca/server/upload_latencies` BETA ** _(project)_**   
Apigee UDCA server upload latencies   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total amount of time in seconds that the Apigee Universal Data Collection Agent (UDCA) server application required to upload a data file. Buckets will be 100 ms, 250 ms, 500 ms, 1 s, 2 s, 4 s, 8 s500 ms, 1 s, 2 s, 4 s, 8 s, 16 s, 32 s, and 64 s. The metrics will display a histogram for total latency from file creation time to successful upload time. Sampled every 60 seconds._   
`dataset`: Type of data.   
`udca/upstream/http_error_count` BETA ** _(project)_**   
Apigee UDCA server HTTP error count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of HTTP errors encountered by the Apigee Universal Data Collection Agent (UDCA) server application. This metric is useful to help determine in which part of the UDCA external dependencies are failing and for what reason. These errors can arise for various services (such as getDataLocation, Cloud storage, token generator) and for various datasets (such as API and trace) with different response codes. Sampled every 60 seconds._   
`dataset`: Type of data.   
`service`: Upstream service name.   
`response_code`: HTTP response code.   
`udca/upstream/http_latencies` BETA ** _(project)_**   
Apigee UDCA server HTTP latencies   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total amount of time in seconds required for upstream services. Buckets will be 100 ms, 250 ms, 500 ms, 1 s, 2 s, 4 s, 8 s, 16 s, 32 s, and 64 s. The metrics will display a histogram for latency from upstream services. Sampled every 60 seconds._   
`dataset`: Type of data.   
`service`: Upstream service name.   
`udca/upstream/uploaded_file_count` BETA ** _(project)_**   
Apigee UDCA uploaded file count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of files being uploaded to the Apigee Universal Data Collection Agent (UDCA) server application. Note that the event dataset value should keep growing, the API dataset value should keep growing if the organization and environment have constant traffic, and the trace dataset value should increase when you use the Apigee trace tools to debug or inspect your requests. Sampled every 60 seconds._   
`dataset`: Type of data.   
`udca/upstream/uploaded_file_sizes` BETA ** _(project)_**   
Apigee UDCA uploaded file size distribution   
`CUMULATIVE`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total file size in bytes uploaded to the Apigee Universal Data Collection Agent (UDCA) server application. Buckets will be 1 KB, 10 KB, 100 KB, 1 MB, 10 MB, 100 MB, and 1 GB. The metrics will display a histogram for file size by dataset, organization, and environment. Sampled every 60 seconds._   
`dataset`: Type of data.   
`upstream/latencies` BETA ** _(project)_**   
Apigee upstream latencies   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total amount of time in milliseconds incurred by the upstream Apigee server application. For apigee-synchronizer this metric indicates the latency from the control plane. Sampled every 60 seconds._   
`method`: HTTP method.   
`response_code`: HTTP response code.   
`type`: Type of service.   
`upstream/request_count` BETA ** _(project)_**   
Apigee upstream request count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of requests sent by the Apigee server application to its upstream application. For example, for the apigee-synchronizer the control plane is upstream. Sampled every 60 seconds._   
`method`: HTTP method.   
`type`: Type of service.   
`upstream/response_count` BETA ** _(project)_**   
Apigee upstream response count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of responses received by the Apigee server application from its upstream application. For example, for the apigee-synchronizer the control plane is upstream. Sampled every 60 seconds._   
`method`: HTTP method.   
`response_code`: HTTP response code.   
`type`: Type of service.   
  
### appengine

Metrics from [App Engine](https://docs.cloud.google.com/appengine/docs). **Note:** If you use App Engine flexible environment in combination with Cloud Load Balancing, then certain metrics in the following table are reported as metrics from the [`loadbalancing` table](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-loadbalancing) instead. For more information, see [External Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `appengine.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`flex/autoscaler/capacity` GA ** _(project)_**   
Autoscaling Metrics Utilization Capacity   
`GAUGE`, `DOUBLE`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Utilization capacity multiplied by number of serving VMs. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/autoscaler/connections/current` GA ** _(project)_**   
Writing and reading connections   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of current reading and writing connections per App Engine flexible environment instance. Intended to be used for autoscaling. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`service_id`: The service/module name.   
`state`: State of the connection (writing or reading).   
`version_id`: The version name.   
`instance_name`: The VM instance name.   
`flex/autoscaler/current_utilization` GA ** _(project)_**   
Autoscaling Metrics Current Utilization   
`GAUGE`, `DOUBLE`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _The sum of the utilization of a specified metric for all serving VMs. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`metric_type`: The target autoscaling metric type. For example, cpu.   
`flex/autoscaler/server/request_count` GA ** _(project)_**   
Request counts   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Request counts for an App Engine flexible environment instance.Intended to be used for autoscaling. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`service_id`: The service/module name.   
`version_id`: The version name.   
`instance_name`: The VM instance name.   
`flex/connections/current` GA ** _(project)_**   
Connections   
`GAUGE`, `DOUBLE`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Number of current active connections per App Engine flexible environment version. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/cpu/reserved_cores` GA ** _(project)_**   
Reserved cores   
`GAUGE`, `DOUBLE`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Total number of CPU cores allocated to an App Engine flexible environment version. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Fractional utilization of allocated CPU across an App Engine flexible environment version. Values are typically numbers between 0.0 and 1.0 (but some machine types allow bursting above 1.0). Charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/disk/read_bytes_count` GA ** _(project)_**   
Disk bytes read   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta count of bytes read from disk across an App Engine flexible environment version. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/disk/write_bytes_count` GA ** _(project)_**   
Disk bytes written   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta count of bytes written from disk across an App Engine flexible environment version. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/connections/current` GA ** _(project)_**   
Connections   
`GAUGE`, `DOUBLE`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Number of current active connections per App Engine flexible environment instance. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/container/cpu/limit` ALPHA ** _(project)_**   
Container CPU limit   
`GAUGE`, `DOUBLE`, `s{CPU}/s`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _CPU time limit (where applicable). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container (or ID if name is not available).   
`flex/instance/container/cpu/usage_time` ALPHA ** _(project)_**   
Container CPU usage   
`GAUGE`, `DOUBLE`, `s{CPU}`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Per container CPU usage in CPU seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container (or ID if name is not available).   
`flex/instance/container/memory/limit` ALPHA ** _(project)_**   
Container memory limit   
`GAUGE`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Total memory the container is allowed to use. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container (or ID if name is not available).   
`flex/instance/container/memory/usage` ALPHA ** _(project)_**   
Container memory usage   
`GAUGE`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Total memory the container is using. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container (or ID if name is not available).   
`flex/instance/container/network/received_bytes_count` ALPHA ** _(project)_**   
Container network bytes received   
`DELTA`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Bytes received by container over all network interfaces. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container (or ID if name is not available).   
`flex/instance/container/network/sent_bytes_count` ALPHA ** _(project)_**   
Container network bytes sent   
`DELTA`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Bytes sent by container over all network interfaces. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container (or ID if name is not available).   
`flex/instance/container/restart_count` ALPHA ** _(project)_**   
Container restart count   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Number of times the container has been restarted. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container (or ID if name is not available).   
`flex/instance/container/uptime` ALPHA ** _(project)_**   
Container uptime   
`GAUGE`, `INT64`, `s`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Time for which the container has been up. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container (or ID if name is not available).   
`flex/instance/cpu/usage_time` GA ** _(project)_**   
CPU Usage   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Delta vCPU usage for all vCPUs, in vCPU-seconds. This value is reported by the hypervisor for the VM. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/cpu/utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Fractional CPU utilization for all cores on a single App Engine flexible instance. Values are typically numbers between 0.0 and 1.0 for a single core (but might exceed 1.0 in total). Charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/disk/io/read_bytes_count` GA ** _(project)_**   
Disk read bytes   
`DELTA`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Delta count of bytes read from disk. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/disk/io/write_bytes_count` GA ** _(project)_**   
Disk write bytes   
`DELTA`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Delta count of bytes written to disk. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/guest/disk/bytes_used` GA ** _(project)_**   
Disk usage   
`GAUGE`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Number of bytes used on disk for file systems. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`state`: Type of usage (free, used, reserved).   
`flex/instance/guest/memory/bytes_used` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Memory usage by each memory state, in Bytes. Summing values of all states yields the total memory on the machine. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`state`: One of the following: buffered, cached, free, slab, used. Buffered consists of temporary storage for raw disk blocks. Cached consists of the pagecache and tmpfs usage. Free consists of total free memory. Slab consists of memory used for caching in-kernel data structures. Used is calculated by subtracting the values for the other states from the total available memory.   
`flex/instance/healthcheck/liveness/request_count` GA ** _(project)_**   
Liveness check   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Number of liveness health-check requests for a Flex instance with status and error code. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`status`: Status of healthcheck request.   
`error_code`: Error code when status is 'fail'.   
`flex/instance/healthcheck/readiness/request_count` GA ** _(project)_**   
Readiness check   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Number of readiness health-check requests for a Flex instance with status and error code. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`status`: Status of healthcheck request.   
`error_code`: Error code when status is 'fail'.   
`flex/instance/jvm/gc/count` ALPHA ** _(project)_**   
GC count   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The total number of garbage collections that have occurred. Sampled every 60 seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`gc_name`: The name of the garbage collector involved.   
`flex/instance/jvm/gc/time` ALPHA ** _(project)_**   
GC Time   
`DELTA`, `INT64`, `ms`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The accumulated garbage collection elapsed time in milliseconds. Sampled every 60 seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`gc_name`: The name of the garbage collector involved.   
`flex/instance/jvm/memory/usage` ALPHA ** _(project)_**   
Memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The memory usage. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`memory_type`: The type of the memory.   
`usage_kind`: The kind of memory usage.   
`flex/instance/jvm/os/cpu_time` ALPHA ** _(project)_**   
CPU time   
`DELTA`, `INT64`, `ns`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The CPU time used by the process on which the Java virtual machine is running. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/jvm/thread/num_live` ALPHA ** _(project)_**   
Threads   
`GAUGE`, `DOUBLE`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The current number of live threads. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/jvm/thread/peak` ALPHA ** _(project)_**   
Max threads   
`GAUGE`, `DOUBLE`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The peak number of live threads. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/jvm/uptime` ALPHA ** _(project)_**   
Uptime   
`DELTA`, `INT64`, `ms`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The uptime of the Java virtual machine. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/log_entry_count` GA ** _(project)_**   
Logging Agent Log Entry Count   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Count of log entries written by the Logging agent. Sampled every 60 seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: (INT64) Numeric response code from both the gRPC and HTTP error spaces.   
`flex/instance/log_entry_retry_count` ALPHA ** _(project)_**   
Logging Agent Retried Log Entry Writes Count   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Count of log-entry writes that were retried by the Logging agent. Sampled every 60 seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: (INT64) Numeric response code from both the gRPC and HTTP error spaces.   
`flex/instance/network/received_bytes_count` GA ** _(project)_**   
Network bytes received   
`DELTA`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Delta count of incoming network bytes in an App Engine flexible instance. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/network/sent_bytes_count` GA ** _(project)_**   
Network bytes sent   
`DELTA`, `INT64`, `By`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Delta count of outgoing network bytes in an App Engine flexible instance. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/nginx/connections/accepted_count` GA ** _(project)_**   
Accepted connections   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Total connections accepted. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/nginx/connections/current` GA ** _(project)_**   
Active connections   
`GAUGE`, `DOUBLE`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The number of connections currently attached to Nginx. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`state`: The Nginx connection state.   
`flex/instance/nginx/connections/handled_count` GA ** _(project)_**   
Handled connections   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Total connections handled. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/uptime` GA ** _(project)_**   
Uptime   
`GAUGE`, `DOUBLE`, `s`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _How long the VM has been running, in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/web_socket/closed_connections_count` GA ** _(project)_**   
Websocket connections closed   
`DELTA`, `INT64`, `1`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Count of websocket connections closed. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/web_socket/durations` BETA ** _(project)_**   
Websocket duration   
`DELTA`, `DISTRIBUTION`, `s`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _The durations of websocket connections measured at nginx. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/instance/ws/avg_duration` GA ** _(project)_**   
Websocket average duration   
`GAUGE`, `DOUBLE`, `s`   
**[gae_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance)** |  _Average of websocket requests for a given App Engine Flexible instance. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/network/received_bytes_count` GA ** _(project)_**   
Network bytes received.   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta count of incoming network bytes across all VMs in an App Engine flexible environment version. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`flex/network/sent_bytes_count` GA ** _(project)_**   
Network bytes sent.   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta count of outgoing network bytes across all VMs in an App Engine flexible environment version. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`http/server/dos_intercept_count` GA ** _(project)_**   
Interception count   
`DELTA`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta count of interceptions performed to prevent DoS attacks. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`http/server/quota_denial_count` GA ** _(project)_**   
Quota denial count   
`DELTA`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta count of requests that failed due to the app being over quota. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`http/server/response_count` GA ** _(project)_**   
Response count   
`DELTA`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta HTTP response count. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`loading`: (BOOL) Indicates whether the request was loading.   
`response_code`: (INT64) HTTP status code for the request.   
`http/server/response_latencies` GA ** _(project)_**   
Response latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _HTTP response latency. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`loading`: (BOOL) Indicates whether the request was loading.   
`response_code`: (INT64) HTTP status code for the request.   
`http/server/response_style_count` GA ** _(project)_**   
Response count by style   
`DELTA`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta counts on the HTTP serve style. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`dynamic`: (BOOL) Indicates if the request was a static or dynamic request.   
`cached`: (BOOL) Indicates if the response was cached.   
`infrastructure/cloudsql/connection_latencies` GA ** _(project)_**   
CloudSQL connection latency   
`DELTA`, `DISTRIBUTION`, `us`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Distribution of latency in microseconds for connections originating from App Engine to CloudSQL. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/connection_refused_count` GA ** _(project)_**   
CloudSQL connection refused count   
`DELTA`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Total number of connections refused originating from App Engine to CloudSQL. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/connection_request_count` GA ** _(project)_**   
CloudSQL connection request count   
`DELTA`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Total number of connection requests originating from App Engine to CloudSQL. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/received_bytes_count` GA ** _(project)_**   
CloudSQL bytes received   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Number of bytes received by App Engine from Cloud SQL over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/sent_bytes_count` GA ** _(project)_**   
CloudSQL bytes sent   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Number of bytes sent by App Engine to Cloud SQL over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`memcache/access_ages` GA ** _(project)_**   
Ages at Access   
`DELTA`, `DISTRIBUTION`, `s`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Ages of cached items when they are accessed. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`memcache/backend_request_count` GA ** _(project)_**   
Backend Requests   
`DELTA`, `INT64`, `{requests}`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Count of cache requests as recorded by the backends. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`memcache/cache_size_limit` GA ** _(project)_**   
Memcache Size Limit   
`GAUGE`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Expected maximum possible cache size based on app's configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`memcache/centi_mcu_count` GA ** _(project)_**   
Memcache utilization   
`DELTA`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Memcache utilization in one hundredth of Memcache Compute Unit grouped by command. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`command`: Name of the memcache command.   
`memcache/centi_mcu_limit` GA ** _(project)_**   
Memcache Compute Unit Limit   
`GAUGE`, `INT64`, `c{MCU}`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Expected maximum memcache size in one hundredth of Memcache Compute Units. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`memcache/eviction_count` GA ** _(project)_**   
Rate of evictions   
`DELTA`, `INT64`, `{item}`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Rate of items evicted from the cache due to space constraints. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`memcache/hit_bytes_count` GA ** _(project)_**   
Hit Bytes Count   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Count of bytes served from cache hits. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`memcache/hit_count` GA ** _(project)_**   
Cache Hits   
`DELTA`, `INT64`, `{request}`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Rate of cache hits. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`memcache/hit_ratio` GA ** _(project)_**   
Hit ratio   
`GAUGE`, `DOUBLE`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Percentage of successful hits compared to all memcache operations. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`memcache/hot_keys` GA ** _(project)_**   
Hot Keys   
`DELTA`, `DISTRIBUTION`, `{request}`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Distribution of hot key qps. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`memcache/miss_count` GA ** _(project)_**   
Cache Misses   
`DELTA`, `INT64`, `{request}`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Rate of cache misses. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`memcache/operation_count` GA ** _(project)_**   
Memcache operations   
`DELTA`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Count of memcache key operations, grouped by command and status. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`command`: Name of the memcache command.   
`status`: Whether the operation succeeded or not, e.g. HIT or MISS. This is currently unpopulated (always an empty string).   
`memcache/received_bytes_count` GA ** _(project)_**   
Memcache received bytes   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Number of bytes received by app from the memcache API, grouped by status and memcache command. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`status`: RPC status of the request.   
`command`: Name of the memcache command.   
`memcache/sent_bytes_count` GA ** _(project)_**   
Memcache sent bytes   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Number of bytes sent by app through the memcache API, grouped by memcache command. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`command`: Name of the memcache command.   
`memcache/set_bytes_count` GA ** _(project)_**   
Set Bytes Count   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Count of bytes received from sets. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`memcache/used_cache_size` GA ** _(project)_**   
Used Cache Size   
`GAUGE`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Size of the cache, calculated as the total size of all items stored. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`system/billed_instance_estimate_count` GA ** _(project)_**   
Estimated instance count   
`GAUGE`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Estimate of the number of instances that the customer is charged for. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`system/cpu/usage` GA ** _(project)_**   
CPU megacycles   
`GAUGE`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _CPU usage in megacycles over all instances. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`source`: The source of the CPU usage (api or runtime).   
`system/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _CPU utilization average over all active instances. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`system/instance_count` GA ** _(project)_**   
Instance count   
`GAUGE`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Number of instances that exist. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`state`: State of instance (active, idle, etc).   
`system/memory/usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Total memory used by running instances. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`system/network/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta count of incoming network bandwidth. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`cached`: (BOOL) Indicates if response was cached.   
`system/network/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Delta count of outgoing network bandwidth. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`cached`: (BOOL) Indicates if response was cached.   
`system/pending_queue/pending_requests` GA ** _(project)_**   
Pending Requests   
`GAUGE`, `INT64`, `1`   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)** |  _Number of pending requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
  
### apphub

Metrics from [App Hub](https://docs.cloud.google.com/app-hub/docs/overview). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `apphub.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`application/services` BETA ** _(project)_**   
Registered Services   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Number of Registered Services in a host project per location per application._   
`criticality_level`: Criticality level enum for the service.   
`environment`: Environment attribute enum for the service.   
`service_project_id`: The Service Project ID for the underlying infrastructure resource. This is different from the GCP project in resource_container. Each GCP project might contains multiple service projects.   
`application/workloads` BETA ** _(project)_**   
Registered Workloads   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Number of Registered Workloads in a host project per location per application._   
`criticality_level`: Criticality level enum for the workload.   
`environment`: Environment attribute enum for the workload.   
`service_project_id`: The Service Project ID for the underlying infrastructure resource. This is different from the GCP project in resource_container. Each GCP project might contains multiple service projects.   
`applications` BETA ** _(project)_**   
Applications   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Location)** |  _Number of Applications in a host project per location._   
`criticality_level`: Criticality level enum for the application.   
`environment`: Environment attribute enum for the application.   
`discovered/services` BETA ** _(project)_**   
Discovered Services   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Location)** |  _Number of Discovered Services in a host project per location._   
`service_project_id`: The Service Project ID for the underlying infrastructure resource. This is different from the GCP project in resource_container. Each GCP project might contains multiple service projects.   
`discovered/workloads` BETA ** _(project)_**   
Discovered Workloads   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Location)** |  _Number of Discovered Workloads in a host project per location._   
`service_project_id`: The Service Project ID for the underlying infrastructure resource. This is different from the GCP project in resource_container. Each GCP project might contains multiple service projects.   
`quota/service_per_global_application/exceeded` ALPHA ** _(project)_**   
Global Registered Services quota exceeded error   
`DELTA`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Number of attempts to exceed the limit on quota metric apphub.googleapis.com/service_per_global_application. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/service_per_global_application/limit` ALPHA ** _(project)_**   
Global Registered Services quota limit   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Current limit on quota metric apphub.googleapis.com/service_per_global_application. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/service_per_global_application/usage` ALPHA ** _(project)_**   
Global Registered Services quota usage   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Current usage on quota metric apphub.googleapis.com/service_per_global_application. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/service_per_region_per_application/exceeded` GA ** _(project)_**   
Registered Services quota exceeded error   
`DELTA`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Number of attempts to exceed the limit on quota metric apphub.googleapis.com/service_per_region_per_application. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/service_per_region_per_application/limit` GA ** _(project)_**   
Registered Services quota limit   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Current limit on quota metric apphub.googleapis.com/service_per_region_per_application. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/service_per_region_per_application/usage` GA ** _(project)_**   
Registered Services quota usage   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Current usage on quota metric apphub.googleapis.com/service_per_region_per_application. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/workload_per_global_application/exceeded` ALPHA ** _(project)_**   
Global Registered Workloads quota exceeded error   
`DELTA`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Number of attempts to exceed the limit on quota metric apphub.googleapis.com/workload_per_global_application. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/workload_per_global_application/limit` ALPHA ** _(project)_**   
Global Registered Workloads quota limit   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Current limit on quota metric apphub.googleapis.com/workload_per_global_application. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/workload_per_global_application/usage` ALPHA ** _(project)_**   
Global Registered Workloads quota usage   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Current usage on quota metric apphub.googleapis.com/workload_per_global_application. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/workload_per_region_per_application/exceeded` GA ** _(project)_**   
Registered Workloads quota exceeded error   
`DELTA`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Number of attempts to exceed the limit on quota metric apphub.googleapis.com/workload_per_region_per_application. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/workload_per_region_per_application/limit` GA ** _(project)_**   
Registered Workloads quota limit   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Current limit on quota metric apphub.googleapis.com/workload_per_region_per_application. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/workload_per_region_per_application/usage` GA ** _(project)_**   
Registered Workloads quota usage   
`GAUGE`, `INT64`, `1`   
**[apphub.googleapis.com/Application](https://docs.cloud.google.com/monitoring/api/resources#tag_apphub.googleapis.com/Application)** |  _Current usage on quota metric apphub.googleapis.com/workload_per_region_per_application. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
  
### artifactregistry

Metrics from [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `artifactregistry.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`project/api/request_count` GA ** _(project)_**   
Control plane API request count per project   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Project)** |  _Request count for all requests sent to Artifact Registry control plane API for the current project._   
`method`: The name of the called control plane API. For the list of available APIs see https://cloud.google.com/artifact-registry/docs/audit-logging#api-interface-reference.   
`version`: The version of the called control plane API.   
`response_code`: The HTTP response code of the request.   
`status`: The status of the request.   
`project/api/request_latencies` GA ** _(project)_**   
Control plane API request latency per project   
`DELTA`, `DISTRIBUTION`, `us`   
**[artifactregistry.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Project)** |  _The latency distribution for the requests sent to Artifact Registry control plane API for the current project in microseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: The name of the called control plane API. For the list of available APIs see https://cloud.google.com/artifact-registry/docs/audit-logging#api-interface-reference.   
`version`: The version of the called control plane API.   
`response_code`: The HTTP response code of the request.   
`status`: The status of the request.   
`project/request_count` GA ** _(project)_**   
Data plane API request count per project   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Project)** |  _Request count for all requests sent to Artifact Registry data plane API for the current project. For example requests made by Docker, Maven, Pip, Twine, or Gradle tools are data plane requests._   
`method`: The name of the called data plane API. For the list of available APIs see https://cloud.google.com/artifact-registry/docs/audit-logging#Data%20plane%20API.   
`type`: The type of the called API: PREAMPLE, READ or WRITE.   
`response_code`: The HTTP response code of the request.   
`status`: The status of the request.   
`project/request_latencies` GA ** _(project)_**   
Data plane API request latency per project   
`DELTA`, `DISTRIBUTION`, `us`   
**[artifactregistry.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Project)** |  _The latency distribution for the requests sent to Artifact Registry data plane API for the current project in microseconds. For example requests made by Docker, Maven, Pip, Twine, or Gradle tools are data plane requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: The name of the called data plane API. For the list of available APIs see https://cloud.google.com/artifact-registry/docs/audit-logging#Data%20plane%20API.   
`type`: The type of the called API: PREAMPLE, READ or WRITE.   
`response_code`: The HTTP response code of the request.   
`status`: The status of the request.   
`quota/asia_multi_region_upstream_host_reads/exceeded` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the Asia multi-region quota exceeded error   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric artifactregistry.googleapis.com/asia_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/asia_multi_region_upstream_host_reads/limit` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the Asia multi-region quota limit   
`GAUGE`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current limit on quota metric artifactregistry.googleapis.com/asia_multi_region_upstream_host_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/asia_multi_region_upstream_host_reads/usage` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the Asia multi-region quota usage   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current usage on quota metric artifactregistry.googleapis.com/asia_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`host`: External upstream host label.   
`quota/europe_multi_region_upstream_host_reads/exceeded` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the Europe multi-region quota exceeded error   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric artifactregistry.googleapis.com/europe_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/europe_multi_region_upstream_host_reads/limit` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the Europe multi-region quota limit   
`GAUGE`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current limit on quota metric artifactregistry.googleapis.com/europe_multi_region_upstream_host_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/europe_multi_region_upstream_host_reads/usage` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the Europe multi-region quota usage   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current usage on quota metric artifactregistry.googleapis.com/europe_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`host`: External upstream host label.   
`quota/project_asia_multi_region_upstream_host_reads/exceeded` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the Asia multi-region quota exceeded error   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric artifactregistry.googleapis.com/project_asia_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/project_asia_multi_region_upstream_host_reads/limit` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the Asia multi-region quota limit   
`GAUGE`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current limit on quota metric artifactregistry.googleapis.com/project_asia_multi_region_upstream_host_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/project_asia_multi_region_upstream_host_reads/usage` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the Asia multi-region quota usage   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current usage on quota metric artifactregistry.googleapis.com/project_asia_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`host`: External upstream host label.   
`quota/project_europe_multi_region_upstream_host_reads/exceeded` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the Europe multi-region quota exceeded error   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric artifactregistry.googleapis.com/project_europe_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/project_europe_multi_region_upstream_host_reads/limit` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the Europe multi-region quota limit   
`GAUGE`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current limit on quota metric artifactregistry.googleapis.com/project_europe_multi_region_upstream_host_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/project_europe_multi_region_upstream_host_reads/usage` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the Europe multi-region quota usage   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current usage on quota metric artifactregistry.googleapis.com/project_europe_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`host`: External upstream host label.   
`quota/project_region_upstream_host_reads/exceeded` GA ** _(project)_**   
Read requests to external upstream hosts per project per region per host quota exceeded error   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric artifactregistry.googleapis.com/project_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/project_region_upstream_host_reads/limit` GA ** _(project)_**   
Read requests to external upstream hosts per project per region per host quota limit   
`GAUGE`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current limit on quota metric artifactregistry.googleapis.com/project_region_upstream_host_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/project_region_upstream_host_reads/usage` GA ** _(project)_**   
Read requests to external upstream hosts per project per region per host quota usage   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current usage on quota metric artifactregistry.googleapis.com/project_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`host`: External upstream host label.   
`quota/project_us_multi_region_upstream_host_reads/exceeded` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the US multi-region quota exceeded error   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric artifactregistry.googleapis.com/project_us_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/project_us_multi_region_upstream_host_reads/limit` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the US multi-region quota limit   
`GAUGE`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current limit on quota metric artifactregistry.googleapis.com/project_us_multi_region_upstream_host_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/project_us_multi_region_upstream_host_reads/usage` GA ** _(project)_**   
Read requests to external upstream hosts per project per host in the US multi-region quota usage   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current usage on quota metric artifactregistry.googleapis.com/project_us_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`host`: External upstream host label.   
`quota/region_upstream_host_reads/exceeded` GA ** _(project)_**   
Read requests to external upstream hosts per organization per region per host quota exceeded error   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric artifactregistry.googleapis.com/region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/region_upstream_host_reads/limit` GA ** _(project)_**   
Read requests to external upstream hosts per organization per region per host quota limit   
`GAUGE`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current limit on quota metric artifactregistry.googleapis.com/region_upstream_host_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/region_upstream_host_reads/usage` GA ** _(project)_**   
Read requests to external upstream hosts per organization per region per host quota usage   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current usage on quota metric artifactregistry.googleapis.com/region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`host`: External upstream host label.   
`quota/us_multi_region_upstream_host_reads/exceeded` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the US multi-region quota exceeded error   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric artifactregistry.googleapis.com/us_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/us_multi_region_upstream_host_reads/limit` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the US multi-region quota limit   
`GAUGE`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current limit on quota metric artifactregistry.googleapis.com/us_multi_region_upstream_host_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`host`: External upstream host label.   
`quota/us_multi_region_upstream_host_reads/usage` GA ** _(project)_**   
Read requests to external upstream hosts per organization per host in the US multi-region quota usage   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Location)** |  _Current usage on quota metric artifactregistry.googleapis.com/us_multi_region_upstream_host_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`host`: External upstream host label.   
`repository/api/request_count` GA ** _(project)_**   
Control plane API request count per repository   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Repository](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Repository)** |  _Request count for all requests sent to Artifact Registry control plane API for a repository._   
`method`: The name of the called control plane API. For the list of available APIs see https://cloud.google.com/artifact-registry/docs/audit-logging#api-interface-reference.   
`version`: The version of the called control plane API.   
`response_code`: The HTTP response code of the request.   
`status`: The status of the request.   
`repository/api/request_latencies` GA ** _(project)_**   
Control plane API request latency per repository   
`DELTA`, `DISTRIBUTION`, `us`   
**[artifactregistry.googleapis.com/Repository](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Repository)** |  _The latency distribution for the requests sent to Artifact Registry control plane API for a repository in microseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: The name of the called control plane API. For the list of available APIs see https://cloud.google.com/artifact-registry/docs/audit-logging#api-interface-reference.   
`version`: The version of the called control plane API.   
`response_code`: The HTTP response code of the request.   
`status`: The status of the request.   
`repository/request_count` GA ** _(project)_**   
Data plane API request count per repository   
`DELTA`, `INT64`, `1`   
**[artifactregistry.googleapis.com/Repository](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Repository)** |  _Request count for all requests sent to Artifact Registry control data API for a repository. For example requests made by Docker, Maven, Pip, Twine, or Gradle tools are data plane requests._   
`method`: The name of the called data plane API. For the list of available APIs see https://cloud.google.com/artifact-registry/docs/audit-logging#Data%20plane%20API.   
`type`: The type of the called API: PREAMPLE, READ or WRITE.   
`response_code`: The HTTP response code of the request.   
`status`: The status of the request.   
`repository/request_latencies` GA ** _(project)_**   
Data plane API request latency per repository   
`DELTA`, `DISTRIBUTION`, `us`   
**[artifactregistry.googleapis.com/Repository](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Repository)** |  _The latency distribution for the requests sent to Artifact Registry data plane API for a repository in microseconds. For example requests made by Docker, Maven, Pip, Twine, or Gradle tools are data plane requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: The name of the called data plane API. For the list of available APIs see https://cloud.google.com/artifact-registry/docs/audit-logging#Data%20plane%20API.   
`type`: The type of the called API: PREAMPLE, READ or WRITE.   
`response_code`: The HTTP response code of the request.   
`status`: The status of the request.   
`repository/size` GA ** _(project)_**   
Repository size   
`GAUGE`, `INT64`, `By`   
**[artifactregistry.googleapis.com/Repository](https://docs.cloud.google.com/monitoring/api/resources#tag_artifactregistry.googleapis.com/Repository)** |  _The size of the repository in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
  
### autoscaler

Metrics from [Compute Engine Autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `autoscaler.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`capacity` GA ** _(project)_**   
Serving capacity   
`GAUGE`, `DOUBLE`, `1`   
**[autoscaler](https://docs.cloud.google.com/monitoring/api/resources#tag_autoscaler)** |  _Utilization target multiplied by number of serving VMs. Sampled every 60 seconds. After sampling, data is not visible for up to 190 seconds._   
`metric_type`: Name of the resource the autoscaling is based on - "cpu", "load balancing" or full metric name in domain-and-path format if scaling is based on Cloud Monitoring metric.   
`configured_max_size` GA ** _(project)_**   
Configured max size   
`GAUGE`, `INT64`, `1`   
**[autoscaler](https://docs.cloud.google.com/monitoring/api/resources#tag_autoscaler)** |  _The configured maximum number of virtual machine instances for the autoscaled managed instance group. The Autoscaler will not recommend a size above this value. This limit is defined in the instance group's autoscaling policy. Sampled every 60 seconds. After sampling, data is not visible for up to 190 seconds._  
`configured_min_size` GA ** _(project)_**   
Configured min size   
`GAUGE`, `INT64`, `1`   
**[autoscaler](https://docs.cloud.google.com/monitoring/api/resources#tag_autoscaler)** |  _The configured minimum number of virtual machine instances for the autoscaled managed instance group. The Autoscaler will not recommend a size below this value. This limit is defined in the instance group's autoscaling policy. Sampled every 60 seconds. After sampling, data is not visible for up to 190 seconds._  
`current_utilization` GA ** _(project)_**   
Current Autoscaler utilization   
`GAUGE`, `DOUBLE`, `1`   
**[autoscaler](https://docs.cloud.google.com/monitoring/api/resources#tag_autoscaler)** |  _The sum of the utilization of a specified metric for all serving VMs. Sampled every 60 seconds. After sampling, data is not visible for up to 190 seconds._   
`metric_type`: Name of the resource the autoscaling is based on - "cpu", "load balancing" or full metric name in domain-and-path format if scaling is based on Cloud Monitoring metric.   
`recommended_size` GA ** _(project)_**   
Recommended size   
`GAUGE`, `INT64`, `1`   
**[autoscaler](https://docs.cloud.google.com/monitoring/api/resources#tag_autoscaler)** |  _The final number of virtual machine instances that the Autoscaler recommends for the managed instance group. This recommendation is derived from the configured autoscaling policy, encompassing various inputs such as utilization signals (e.g., CPU, Load Balancing, custom metrics), predictive forecasts, and schedules. The calculation also incorporates behavioral controls like stabilization periods, scale-in controls, and instance cooldown periods. The result is always constrained by the min_num_replicas and max_num_replicas settings. The instance group's target size is influenced by this recommendation based on the autoscaler's mode. Sampled every 60 seconds. After sampling, data is not visible for up to 190 seconds._  
`scheduled_size` BETA ** _(project)_**   
Scheduled size   
`GAUGE`, `INT64`, `1`   
**[autoscaler](https://docs.cloud.google.com/monitoring/api/resources#tag_autoscaler)** |  _The minimum number of VMs that the autoscaler recommends according to the scaling schedule. Sampled every 60 seconds. After sampling, data is not visible for up to 190 seconds._   
`schedule_name`: Name of the scaling schedule.   
  
### backupdr

Metrics from [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `backupdr.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`backup_recovery_appliance/storage_pool/utilization` GA ** _(project)_**   
Backup/Recovery storage pool utilization   
`GAUGE`, `DOUBLE`, `%`   
**[backupdr.googleapis.com/ManagementConsole](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/ManagementConsole)** |  _Represents the utilization of backup/recovery appliance storage pools._   
`pool_name`: Name of the storage pool. E.g. [act_pri_pool000].   
`pool_usage`: State of storage_pool, one of [free, used].   
`pool_type`: Type of storage_pool, one of [Snapshot, Primary].   
`backup_recovery_appliance_name`: Backup recovery appliance name.   
`backup_recovery_appliance/v_disk_count/utilization` GA ** _(project)_**   
Backup/Recovery appliance vDisk utilization   
`GAUGE`, `DOUBLE`, `%`   
**[backupdr.googleapis.com/ManagementConsole](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/ManagementConsole)** |  _Represents the vDisk pool utilization for a backup/recovery appliance._   
`v_disk_usage`: State of v_disk_count, one of [free, used, leaked].   
`backup_recovery_appliance_name`: The Backup recovery appliance Name.   
`jobs/job_trend` GA ** _(project)_**   
Job Trend   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/ManagementConsole](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/ManagementConsole)** |  _Represents Backup/Recovery job count categorized by job status._   
`job_status`: Status of job, one of [successful, canceled, failed, Not Run, SuccessfulWithWarnings].   
`job_type`: Type of job, E.g. [Snapshot, Expiration, Mount].   
`resource_type`: Type of application associated E.g. [GCPInstance, FileSystem, SQLInstance].   
`backup_recovery_appliance_name`: The Backup recovery appliance Name.   
`onvault_pools/utilization` GA ** _(project)_**   
OnVault pool usage   
`GAUGE`, `INT64`, `By`   
**[backupdr.googleapis.com/ManagementConsole](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/ManagementConsole)** |  _Represents the usages of vault pools._   
`pool_name`: Name of the storage pool. E.g [act_pri_pool000].   
`backup_recovery_appliance_name`: The Backup recovery appliance Name.   
`protected_data/resources` GA ** _(project)_**   
Protected resources count   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/ManagementConsole](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/ManagementConsole)** |  _Represents the number of protected resources by resource type._   
`resource_type`: Type of resource associated E.g. [GCPInstance, FileSystem, SQLInstance].   
`protected_data/volume` GA ** _(project)_**   
Protected data volume   
`GAUGE`, `INT64`, `By`   
**[backupdr.googleapis.com/ManagementConsole](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/ManagementConsole)** |  _Represents the size of data(in bytes) protected by resource type._   
`resource_type`: Type of resource associated E.g. [GCPInstance, FileSystem, SQLInstance].   
`backup_recovery_appliance_name`: The Backup recovery appliance Name.   
`quota/alloydb_active_datasources_per_vault/exceeded` GA ** _(project)_**   
Active Vaulted AlloyDB datasources per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/alloydb_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/alloydb_active_datasources_per_vault/limit` GA ** _(project)_**   
Active Vaulted AlloyDB datasources per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/alloydb_active_datasources_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/alloydb_active_datasources_per_vault/usage` GA ** _(project)_**   
Active Vaulted AlloyDB datasources per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/alloydb_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/alloydb_backups_per_vault/exceeded` GA ** _(project)_**   
AlloyDB backups per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/alloydb_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/alloydb_backups_per_vault/limit` GA ** _(project)_**   
AlloyDB backups per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/alloydb_backups_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/alloydb_backups_per_vault/usage` GA ** _(project)_**   
AlloyDB backups per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/alloydb_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault/exceeded` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault/limit` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault/usage` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_asia_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per Asia multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_asia_multiregion/limit` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per Asia multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_asia_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_asia_multiregion/usage` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per Asia multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_eu_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per EU multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_eu_multiregion/limit` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per EU multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_eu_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_eu_multiregion/usage` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per EU multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_us_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per US multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_us_multiregion/limit` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per US multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_us_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_active_datasources_per_vault_per_us_multiregion/usage` GA ** _(project)_**   
Active Vaulted Cloud SQL datasources per vault per US multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/cloud_sql_active_datasources_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault/exceeded` GA ** _(project)_**   
Cloud SQL instance backups per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault/limit` GA ** _(project)_**   
Cloud SQL instance backups per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault/usage` GA ** _(project)_**   
Cloud SQL instance backups per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_asia_multiregion/exceeded` GA ** _(project)_**   
Cloud SQL instance backups per vault per Asia multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_asia_multiregion/limit` GA ** _(project)_**   
Cloud SQL instance backups per vault per Asia multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_asia_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_asia_multiregion/usage` GA ** _(project)_**   
Cloud SQL instance backups per vault per Asia multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_eu_multiregion/exceeded` GA ** _(project)_**   
Cloud SQL instance backups per vault per EU multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_eu_multiregion/limit` GA ** _(project)_**   
Cloud SQL instance backups per vault per EU multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_eu_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_eu_multiregion/usage` GA ** _(project)_**   
Cloud SQL instance backups per vault per EU multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_us_multiregion/exceeded` GA ** _(project)_**   
Cloud SQL instance backups per vault per US multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_us_multiregion/limit` GA ** _(project)_**   
Cloud SQL instance backups per vault per US multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_us_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_sql_backups_per_vault_per_us_multiregion/usage` GA ** _(project)_**   
Cloud SQL instance backups per vault per US multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/cloud_sql_backups_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault/exceeded` GA ** _(project)_**   
Active Vaulted Compute Disks per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault/limit` GA ** _(project)_**   
Active Vaulted Compute Disks per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault/usage` GA ** _(project)_**   
Active Vaulted Compute Disks per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_asia_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per Asia multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_asia_multiregion/limit` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per Asia multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_asia_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_asia_multiregion/usage` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per Asia multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_eu_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per EU multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_eu_multiregion/limit` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per EU multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_eu_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_eu_multiregion/usage` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per EU multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_nam11_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per nam11 multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_nam11_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_nam11_multiregion/limit` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per nam11 multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_nam11_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_nam11_multiregion/usage` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per nam11 multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_nam11_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_us_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per US multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_us_multiregion/limit` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per US multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_us_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_active_datasources_per_vault_per_us_multiregion/usage` GA ** _(project)_**   
Active Vaulted Compute Disks per vault per US multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_active_datasources_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault/exceeded` GA ** _(project)_**   
Compute Disk backups per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault/limit` GA ** _(project)_**   
Compute Disk backups per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_backups_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault/usage` GA ** _(project)_**   
Compute Disk backups per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_asia_multiregion/exceeded` GA ** _(project)_**   
Compute Disk backups per vault per Asia multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_asia_multiregion/limit` GA ** _(project)_**   
Compute Disk backups per vault per Asia multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_asia_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_asia_multiregion/usage` GA ** _(project)_**   
Compute Disk backups per vault per Asia multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_eu_multiregion/exceeded` GA ** _(project)_**   
Compute Disk backups per vault per EU multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_eu_multiregion/limit` GA ** _(project)_**   
Compute Disk backups per vault per EU multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_eu_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_eu_multiregion/usage` GA ** _(project)_**   
Compute Disk backups per vault per EU multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_nam11_multiregion/exceeded` GA ** _(project)_**   
Compute Disk backups per vault per nam11 multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_nam11_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_nam11_multiregion/limit` GA ** _(project)_**   
Compute Disk backups per vault per nam11 multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_nam11_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_nam11_multiregion/usage` GA ** _(project)_**   
Compute Disk backups per vault per nam11 multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_nam11_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_us_multiregion/exceeded` GA ** _(project)_**   
Compute Disk backups per vault per US multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_us_multiregion/limit` GA ** _(project)_**   
Compute Disk backups per vault per US multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_us_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disk_backups_per_vault_per_us_multiregion/usage` GA ** _(project)_**   
Compute Disk backups per vault per US multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/disk_backups_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/filestore_active_datasources_per_vault/exceeded` GA ** _(project)_**   
Active Vaulted Filestore datasources per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/filestore_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/filestore_active_datasources_per_vault/limit` GA ** _(project)_**   
Active Vaulted Filestore datasources per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/filestore_active_datasources_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/filestore_active_datasources_per_vault/usage` GA ** _(project)_**   
Active Vaulted Filestore datasources per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/filestore_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/filestore_backups_per_vault/exceeded` GA ** _(project)_**   
Filestore instance backups per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/filestore_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/filestore_backups_per_vault/limit` GA ** _(project)_**   
Filestore instance backups per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/filestore_backups_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/filestore_backups_per_vault/usage` GA ** _(project)_**   
Filestore instance backups per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/filestore_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault/exceeded` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault/limit` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault/usage` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_asia_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per Asia multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_asia_multiregion/limit` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per Asia multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_asia_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_asia_multiregion/usage` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per Asia multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_eu_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per EU multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_eu_multiregion/limit` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per EU multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_eu_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_eu_multiregion/usage` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per EU multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_nam11_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per nam11 multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_nam11_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_nam11_multiregion/limit` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per nam11 multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_nam11_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_nam11_multiregion/usage` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per nam11 multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_nam11_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_us_multiregion/exceeded` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per US multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_us_multiregion/limit` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per US multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_us_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_active_datasources_per_vault_per_us_multiregion/usage` GA ** _(project)_**   
Active Vaulted Compute VM instance Resources per vault per US multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_active_datasources_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault/exceeded` GA ** _(project)_**   
Compute VM instance backups per vault quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault/limit` GA ** _(project)_**   
Compute VM instance backups per vault quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_backups_per_vault. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault/usage` GA ** _(project)_**   
Compute VM instance backups per vault quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_backups_per_vault. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_asia_multiregion/exceeded` GA ** _(project)_**   
Compute VM instance backups per vault per Asia multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_asia_multiregion/limit` GA ** _(project)_**   
Compute VM instance backups per vault per Asia multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_asia_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_asia_multiregion/usage` GA ** _(project)_**   
Compute VM instance backups per vault per Asia multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_asia_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_eu_multiregion/exceeded` GA ** _(project)_**   
Compute VM instance backups per vault per EU multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_eu_multiregion/limit` GA ** _(project)_**   
Compute VM instance backups per vault per EU multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_eu_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_eu_multiregion/usage` GA ** _(project)_**   
Compute VM instance backups per vault per EU multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_eu_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_nam11_multiregion/exceeded` GA ** _(project)_**   
Compute VM instance backups per vault per nam11 multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_nam11_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_nam11_multiregion/limit` GA ** _(project)_**   
Compute VM instance backups per vault per nam11 multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_nam11_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_nam11_multiregion/usage` GA ** _(project)_**   
Compute VM instance backups per vault per nam11 multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_nam11_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_us_multiregion/exceeded` GA ** _(project)_**   
Compute VM instance backups per vault per US multi region. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Number of attempts to exceed the limit on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_us_multiregion/limit` GA ** _(project)_**   
Compute VM instance backups per vault per US multi region. quota limit   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current limit on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_us_multiregion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_backups_per_vault_per_us_multiregion/usage` GA ** _(project)_**   
Compute VM instance backups per vault per US multi region. quota usage   
`GAUGE`, `INT64`, `1`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Current usage on quota metric backupdr.googleapis.com/gce_backups_per_vault_per_us_multiregion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`storage/stored_bytes` GA ** _(project)_**   
Backup vault storage consumption   
`GAUGE`, `INT64`, `By`   
**[backupdr.googleapis.com/BackupVault](https://docs.cloud.google.com/monitoring/api/resources#tag_backupdr.googleapis.com/BackupVault)** |  _Represents the data usage of the Backup Vault. Sampled every 300 seconds. After sampling, data is not visible for up to 300 seconds._   
`resource_type`: The type of resource protected.   
`backup_schedule_type`: The identifier indicating whether the resource is protected using Backup Plan or Backup Template.   
  
### baremetalsolution

Metrics from [Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs) Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `baremetalsolution.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`instance/ethernet_fabric/port_bytes_count` BETA ** _(project)_**   
Forwarded Bytes Count   
`CUMULATIVE`, `INT64`, `By`   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)** |  _Number of bytes forwarded through a physical interface on the ethernet fabric._   
`direction`: Direction of bytes, one of [SERVER_IN, SERVER_OUT].   
`logical_port`: Name of the logical port.   
`physical_port`: Name of the physical port.   
`lun/avg_latency` BETA ** _(project)_**   
Avg latency of operations   
`GAUGE`, `INT64`, `us`   
**[baremetalsolution.googleapis.com/Lun](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Lun)** |  _The average latency of I/O operations._   
`direction`: Direction of operations, one of [READ, WRITE, TOTAL].   
`lun/bytes_count` BETA ** _(project)_**   
Bytes count   
`CUMULATIVE`, `INT64`, `By`   
**[baremetalsolution.googleapis.com/Lun](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Lun)** |  _Number of bytes written or read, cumulative._   
`direction`: Direction of bytes, one of [READ, WRITE].   
`lun/operation_count` BETA ** _(project)_**   
Operation count   
`CUMULATIVE`, `INT64`, `1`   
**[baremetalsolution.googleapis.com/Lun](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Lun)** |  _Number of operations performed, cumulative._   
`direction`: Direction of operations, one of [READ, WRITE].   
`lun/size` BETA ** _(project)_**   
Lun size in bytes.   
`GAUGE`, `INT64`, `By`   
**[baremetalsolution.googleapis.com/Lun](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Lun)** |  _Space allocated to the lun._   
`type`: Type, one of [AVAILABLE,USED].   
`volume/avg_latency` BETA ** _(project)_**   
Avg latency of operations   
`GAUGE`, `INT64`, `us`   
**[baremetalsolution.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Volume)** |  _The average latency of I/O operations._   
`direction`: Direction of operations, one of [READ, WRITE, TOTAL].   
`volume/bytes_count` BETA ** _(project)_**   
Bytes count   
`CUMULATIVE`, `INT64`, `By`   
**[baremetalsolution.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Volume)** |  _Number of bytes written or read, cumulative._   
`direction`: Direction of bytes, one of [READ, WRITE].   
`volume/operation_count` BETA ** _(project)_**   
Operation count   
`CUMULATIVE`, `INT64`, `1`   
**[baremetalsolution.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Volume)** |  _Number of operations performed, cumulative._   
`direction`: Direction of operations, one of [READ, WRITE].   
`volume/size` BETA ** _(project)_**   
Volume size in bytes   
`GAUGE`, `INT64`, `By`   
**[baremetalsolution.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Volume)** |  _Space allocated to the volume._   
`type`: Type, one of [AVAILABLE,USED].   
  
### bigquery

Metrics from [BigQuery](https://docs.cloud.google.com/bigquery/docs).**Note:** When a job runs in less than 60 seconds, metrics sampled every 60 seconds might not report any data. Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `bigquery.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`job/continuous/backlog_records` GA ** _(project)_**   
Estimated backlog records   
`GAUGE`, `INT64`, `1`   
**[bigquery.googleapis.com/ContinuousJob](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ContinuousJob)** |  _The estimated number of backlog records for each stage of the continuous job. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`stage_id`: The continuous job stage id.   
`job/continuous/estimated_backlog_logical_bytes` GA ** _(project)_**   
Estimated backlog logical bytes   
`GAUGE`, `INT64`, `By`   
**[bigquery.googleapis.com/ContinuousJob](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ContinuousJob)** |  _The number of bytes in the backlog for each stage of the continuous job. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`stage_id`: The continuous job stage id.   
`job/continuous/estimated_bytes_processed` GA ** _(project)_**   
Estimated bytes processed   
`GAUGE`, `INT64`, `By`   
**[bigquery.googleapis.com/ContinuousJob](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ContinuousJob)** |  _The estimated number of bytes processed for each stage of the continuous job. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`stage_id`: The continuous job stage id.   
`job/continuous/output_watermark` GA ** _(project)_**   
Output watermark   
`GAUGE`, `INT64`, `us`   
**[bigquery.googleapis.com/ContinuousJob](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ContinuousJob)** |  _The most recent timestamp, in microseconds since the epoch, up to which all data has been processed by this stage of the continuous job. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`stage_id`: The continuous job stage id.   
`job/continuous/records_read` GA ** _(project)_**   
Records read   
`GAUGE`, `INT64`, `1`   
**[bigquery.googleapis.com/ContinuousJob](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ContinuousJob)** |  _The number of input records read for each stage of the continuous job. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`stage_id`: The continuous job stage id.   
`job/continuous/records_written` GA ** _(project)_**   
Records written   
`GAUGE`, `INT64`, `1`   
**[bigquery.googleapis.com/ContinuousJob](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ContinuousJob)** |  _The number of output records written for each stage of the continuous job. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`stage_id`: The continuous job stage id.   
`job/continuous/slots/used_time` GA ** _(project)_**   
Slots used   
`DELTA`, `INT64`, `ms`   
**[bigquery.googleapis.com/ContinuousJob](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ContinuousJob)** |  _The total slot milliseconds used by the continuous job. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._  
`job/num_in_flight` GA ** _(project)_**   
Job count   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _In flight jobs. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`priority`: Job priority (batch or interactive).   
`job_type`: Job type.   
`state`: Job state.   
`managed_routine/python/cpu_utilizations` BETA ** _(project)_**   
Instance CPU utilization   
`DELTA`, `DISTRIBUTION`, `10^2.%`   
**[bigquery.googleapis.com/ManagedRoutineInvocation](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ManagedRoutineInvocation)** |  _CPU utilization per each instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`managed_routine/python/max_request_concurrencies` BETA ** _(project)_**   
Max Concurrent Requests   
`DELTA`, `DISTRIBUTION`, `Count`   
**[bigquery.googleapis.com/ManagedRoutineInvocation](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ManagedRoutineInvocation)** |  _Distribution of maximum concurrent requests across all Python UDF instances. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`managed_routine/python/memory_utilizations` BETA ** _(project)_**   
Instance memory utilization   
`DELTA`, `DISTRIBUTION`, `10^2.%`   
**[bigquery.googleapis.com/ManagedRoutineInvocation](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery.googleapis.com/ManagedRoutineInvocation)** |  _Memory utilization per each instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`query/biengine_fallback_count` GA ** _(project)_**   
BI Engine query fallback count   
`DELTA`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The reasons that queries failed BI Engine execution. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`reason`: BI Engine fallback reasons.   
`query/column_metadata_index_staleness` GA ** _(project)_**   
Column Metadata Index staleness   
`GAUGE`, `DISTRIBUTION`, `ms`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Distribution of staleness in milliseconds of the column metadata index for queries that successfully used the column metadata index in the last sampling interval. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`query/count` GA ** _(project)_**   
Query count   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)**   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _In flight queries. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`priority`: Query priority (batch or interactive).   
`query/execution_count` GA ** _(project)_**   
Query execution count   
`DELTA`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The number of queries executed. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`priority`: Query priority (batch or interactive).   
`caching_mode`: Query caching mode (BI Engine, etc).   
`query/execution_times` GA ** _(project)_**   
Query execution times   
`GAUGE`, `DISTRIBUTION`, `s`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)**   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Distribution of execution times for queries that completed successfully within the last sampling interval. Incomplete and failed queries are not included. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`priority`: Query priority (batch or interactive).   
`query/scanned_bytes` GA ** _(project)_**   
Scanned bytes   
`DELTA`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Scanned bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 21720 seconds._   
`priority`: Query priority (batch or interactive).   
`query/scanned_bytes_billed` GA ** _(project)_**   
Scanned bytes billed   
`DELTA`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Scanned bytes billed. Sampled every 60 seconds. After sampling, data is not visible for up to 21720 seconds._   
`priority`: Query priority (batch or interactive).   
`query/statement_scanned_bytes` BETA ** _(project)_**   
Statement scanned bytes   
`DELTA`, `INT64`, `By`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Scanned bytes broken down by statement type. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`priority`: Query priority (batch or interactive).   
`statement_type`: Query statement type (SELECT, CREATE_MODEL ...).   
`query/statement_scanned_bytes_billed` BETA ** _(project)_**   
Statement scanned bytes billed   
`DELTA`, `INT64`, `By`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Scanned bytes billed broken down by statement type. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`priority`: Query priority (batch or interactive).   
`statement_type`: Query statement type (SELECT, CREATE_MODEL ...).   
`slots/allocated` GA ** _(project)_**   
Slots used by project, reservation, and job type   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)**   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of BigQuery slots currently allocated for project. Slot allocation can be broken down based on reservation and job type. The accuracy of this metric can be poor, especially the break-down by reservation. Consider using resource charts instead. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`reservation`: Reservation. This field is unset if the query is on-demand.   
`job_type`: Job type.   
`slots/allocated_for_project` GA ** _(project)_**   
Slots used by project   
`GAUGE`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of BigQuery slots currently allocated for query jobs in the project. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`slots/allocated_for_project_and_job_type` GA ** _(project)_**   
Slots used by project and job type   
`GAUGE`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of BigQuery slots currently allocated for the project and job type. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_type`: Job type.   
`slots/allocated_for_reservation` GA ** _(project)_**   
Slots used by project in reservation   
`GAUGE`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of BigQuery slots currently allocated for project in the reservation. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`slots/assigned` GA ** _(project)_**   
Slots assigned   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The number of slots assigned to the given project/organization. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_type`: Job type.   
`reservation`: Reservation.   
`slots/capacity_committed` GA ** _(project)_**   
Slots capacity committed   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The total slot capacity commitments purchased through this administrator project/organization. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`plan`: Capacity commitment plan.   
`slots/max_assigned` GA ** _(project)_**   
Slots max assigned   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The maximum number of slots assigned to the given project/organization. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_type`: Job type.   
`reservation`: Reservation.   
`slots/total_allocated_for_reservation` GA ** _(project)_**   
Slots used across projects in reservation   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)**   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of BigQuery slots currently allocated across projects in the reservation. Note that the metric data is only reported while at least one project has been assigned to the reservation and is consuming slots. As an alternative, consider querying reservations information from INFORMATION_SCHEMA (https://cloud.google.com/bigquery/docs/information-schema-reservations), which does not have these limitations. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`slots/total_available` DEPRECATED ** _(project)_**   
Total slots   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)**   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _(Deprecated) Total number of BigQuery slots available for the project. If you are using the BigQuery Reservations API, consider using bigquery.googleapis.com/slots/assigned and bigquery.googleapis.com/slots/max_assigned instead. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`storage/insertall_inserted_bytes` GA ** _(project)_**   
InsertAll Inserted Bytes   
`DELTA`, `DOUBLE`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The number of bytes uploaded by the project using the InsertAll streaming API. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`storage/insertall_inserted_rows` GA ** _(project)_**   
InsertAll Inserted Rows   
`DELTA`, `DOUBLE`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The number of rows uploaded by the project using the InsertAll streaming API. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`storage/replication/dataset_staleness` BETA ** _(project)_**   
Replication latency   
`GAUGE`, `INT64`, `ms`   
**[bigquery_dataset](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dataset)** |  _Staleness of the data available in the other region replicated as part of the Cross Region Replication or Managed Disaster Recovery features. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`location`: The location that the dataset is replicated to.   
`replica_id`: Replica id.   
`replication_error`: Replication error.   
`storage/replication/network_egress_bytes_count` BETA ** _(project)_**   
Network Egress bytes   
`DELTA`, `INT64`, `By`   
**[bigquery_dataset](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dataset)** |  _Billed amount of bytes replicated, if your dataset is enabled for Cross Region Replication or Managed Disaster Recovery features. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`location`: The location where the bytes are replicated to.   
`storage/stored_bytes` GA ** _(project)_**   
Stored bytes   
`GAUGE`, `INT64`, `By`   
**[bigquery_dataset](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dataset)** |  _Number of logical bytes stored. The top 100 tables in a dataset are labeled, while the rest are grouped with no table label. Sampled every 1800 seconds. After sampling, data is not visible for up to 10800 seconds._   
`table`: Table name.   
`storage/table_count` GA ** _(project)_**   
Table count   
`GAUGE`, `INT64`, `1`   
**[bigquery_dataset](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dataset)** |  _Number of tables. Sampled every 1800 seconds. After sampling, data is not visible for up to 10800 seconds._  
`storage/uploaded_bytes` GA ** _(project)_**   
Uploaded bytes   
`DELTA`, `INT64`, `By`   
**[bigquery_dataset](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dataset)** |  _Uploaded bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 21720 seconds._   
`api`: Api used to upload the data (batch import or streaming)   
`table`: Table name.   
`storage/uploaded_bytes_billed` GA ** _(project)_**   
Uploaded bytes billed   
`DELTA`, `INT64`, `By`   
**[bigquery_dataset](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dataset)** |  _Uploaded bytes billed. Sampled every 60 seconds. After sampling, data is not visible for up to 21720 seconds._   
`api`: Api used to upload the data (batch import or streaming). Currently only streaming api is billed.   
`table`: Table name.   
`storage/uploaded_row_count` GA ** _(project)_**   
Uploaded rows   
`DELTA`, `INT64`, `1`   
**[bigquery_dataset](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dataset)** |  _Uploaded rows. Sampled every 60 seconds. After sampling, data is not visible for up to 21720 seconds._   
`api`: Api used to perform the batch import or streaming insert job. Rows added by using a query job with a `writeDisposition` of `WRITE_APPEND` are not shown.   
`table`: Table name.   
  
### bigquerybiengine

Metrics from [BigQuery BI Engine](https://docs.cloud.google.com/bi-engine/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `bigquerybiengine.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`model/inflight_requests` GA ** _(project)_**   
Inflight requests   
`GAUGE`, `INT64`, `1`   
**[bigquery_biengine_model](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_biengine_model)** |  _Inflight requests to a BI model. Only reported without LookerStudio native BigQuery integration. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`model/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[bigquery_biengine_model](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_biengine_model)** |  _BI Engine request count. Only reported without LookerStudio native BigQuery integration. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`cache_miss`: (BOOL) Indicates if request was not served from memory cache. Large number of requests with this field set to true is the sign that reservation size should be increased. .   
`status`: Completion status of the request.   
`execution_mode`: BIEngine or BigQuery. BigQuery means that request was served using BigQuery slots rather than using BI Engine reservation. .   
`model/request_latencies` GA ** _(project)_**   
Request execution times   
`GAUGE`, `DISTRIBUTION`, `ms`   
**[bigquery_biengine_model](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_biengine_model)** |  _Distribution of request execution times. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`cache_miss`: (BOOL) Indicates if request was served from memory cache. Large number of requests with this field set to true is the sign that reservation size should be increased. Only reported without LookerStudio native BigQuery integration.   
`status`: Completion status of the request.   
`execution_mode`: BIEngine or BigQuery. BigQuery means that request was served using BigQuery slots rather than using BI Engine reservation. .   
`reservation/top_tables_cached_bytes` GA ** _(project)_**   
Reservation used bytes by table   
`GAUGE`, `INT64`, `By`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The amount of data stored in the BI Engine cache per table for the largest tables in the cache. Sampled every 600 seconds. After sampling, data is not visible for up to 720 seconds._   
`project_id`: Project Id.   
`dataset_id`: Dataset Id.   
`table_id`: Table Id.   
`reservation/total_bytes` GA ** _(project)_**   
Reservation total bytes   
`GAUGE`, `INT64`, `By`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Size of the BI engine reservation. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`reservation/used_bytes` GA ** _(project)_**   
Reservation used bytes   
`GAUGE`, `INT64`, `By`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Utilization of the BI engine reservation. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
  
### bigquerydatatransfer

Metrics from [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `bigquerydatatransfer.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`transfer_config/active_runs` GA ** _(project)_**   
Active run count   
`GAUGE`, `INT64`, `1`   
**[bigquery_dts_config](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dts_config)** |  _Number of transfer runs that are running or pending of the transfer configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`state`: Run state (RUNNING or PENDING).   
`run_cause`: Run cause.   
`transfer_config/completed_runs` GA ** _(project)_**   
Completed run count   
`DELTA`, `INT64`, `1`   
**[bigquery_dts_config](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dts_config)** |  _Number of completed DTS runs per transfer configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: Run error status code.   
`completion_state`: Run completion state.   
`run_cause`: Run cause.   
`data_source_id`: Run data source.   
`transfer_config/last_execution_job_rows` GA ** _(project)_**   
Last executed job row count   
`GAUGE`, `INT64`, `1`   
**[bigquery_dts_config](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dts_config)** |  _Number of returned rows from last executed job of transfer configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`run_cause`: Run cause.   
`transfer_config/run_duration_seconds` GA ** _(project)_**   
Run latency distribution   
`DELTA`, `DISTRIBUTION`, `s`   
**[bigquery_dts_config](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_dts_config)** |  _Distribution of the execution time (in seconds) of each transfer run per transfer configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`run_cause`: Run cause.   
  
### bigquerystorage

Metrics from the [BigQuery Storage API](https://docs.cloud.google.com/bigquery/docs/reference/storage). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `bigquerystorage.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`dataflow_write/connection_results_count` BETA ** _(project)_**   
Connection Results   
`DELTA`, `INT64`, `1`   
**[bigquerystorage.googleapis.com/DataflowWrite](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquerystorage.googleapis.com/DataflowWrite)** |  _Total accumulation of BigQuery Write API connection results._   
`result`: String representation of status code.   
`dataflow_write/request_count` BETA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[bigquerystorage.googleapis.com/DataflowWrite](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquerystorage.googleapis.com/DataflowWrite)** |  _Total accumulation of BigQuery Write API request count._   
`result`: String representation of status code.   
`dataflow_write/server_side_latencies` BETA ** _(project)_**   
Server Side Latencies   
`DELTA`, `DISTRIBUTION`, `1`   
**[bigquerystorage.googleapis.com/DataflowWrite](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquerystorage.googleapis.com/DataflowWrite)** |  _The latency distribution (in milliseconds) in BigQuery Write API frontend from receiving a AppendRowsRequest to sending a AppendRowsResponse._   
`result`: String representation of status code.   
`dataflow_write/transcoding_latencies` BETA ** _(project)_**   
Transcoding Latencies   
`DELTA`, `DISTRIBUTION`, `1`   
**[bigquerystorage.googleapis.com/DataflowWrite](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquerystorage.googleapis.com/DataflowWrite)** |  _The duration distribution (in milliseconds) in BigQuery Write API frontend taken by transcoding data._   
`result`: String representation of status code.   
`dataflow_write/uploaded_bytes_count` BETA ** _(project)_**   
Uploaded Bytes   
`DELTA`, `INT64`, `1`   
**[bigquerystorage.googleapis.com/DataflowWrite](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquerystorage.googleapis.com/DataflowWrite)** |  _Total accumulation of BigQuery Write API ingested bytes._   
`result`: String representation of status code.   
`dataflow_write/uploaded_row_count` BETA ** _(project)_**   
Uploaded Rows   
`DELTA`, `INT64`, `1`   
**[bigquerystorage.googleapis.com/DataflowWrite](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquerystorage.googleapis.com/DataflowWrite)** |  _Total accumulation of BigQuery Write API ingested rows._   
`result`: String representation of status code.   
`read/concurrent_streams` GA ** _(project)_**   
Concurrent ReadRows streams   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Number of concurrent ReadRows streams. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`write/concurrent_connections` BETA ** _(project)_**   
concurrent connection count   
`GAUGE`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Concurrent connection per project for BigQuery Write API. To be consistent with concurrent connection quota, the metric is by default on the project that initiated the AppendRowsRequests (associated with the API key or the service account). Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._  
`write/connection_results_count` BETA ** _(project)_**   
Connection results count   
`DELTA`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Total accumulation of connection results with BigQuery Write API. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`result`: String representation of status code .   
`write/server_side_latencies` BETA ** _(project)_**   
server side latency   
`DELTA`, `DISTRIBUTION`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The latency distribution (in milliseconds) in BigQuery Write API frontend from receiving a AppendRowsRequest to sending a AppendRowsResponse. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._  
`write/transcoding_latencies` BETA ** _(project)_**   
transcoding latency   
`DELTA`, `DISTRIBUTION`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _The transcoding latency distribution (in milliseconds) in BigQuery Write API frontend. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._  
`write/uploaded_bytes_count` BETA ** _(project)_**   
Uploaded bytes count   
`DELTA`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Total accumulation of BigQuery Write API ingested bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`result`: String representation of status code .   
`write/uploaded_row_count` BETA ** _(project)_**   
Uploaded rows count   
`DELTA`, `INT64`, `1`   
**[bigquery_project](https://docs.cloud.google.com/monitoring/api/resources#tag_bigquery_project)** |  _Total accumulation of BigQuery Write API ingested rows. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`result`: String representation of status code .   
  
### bigtable

Metrics from [Bigtable](https://docs.cloud.google.com/bigtable/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `bigtable.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`backup/bytes_used` GA ** _(project)_**   
Backup storage used.   
`GAUGE`, `INT64`, `By`   
**[bigtable_backup](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_backup)** |  _Backup storage used in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`source_table`: The source table of the backup.   
`storage_type`: Type of disk storage.   
`client/application_blocking_latencies` GA ** _(project)_**   
Application Blocking Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The total latency introduced by your application when Cloud Bigtable has available response data but your application has not consumed it. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`client_name`: Cloud Bigtable client name.   
`client/attempt_latencies` GA ** _(project)_**   
Attempt Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Client observed latency per RPC attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`streaming`: (BOOL) Cloud Bigtable streaming method.   
`status`: Cloud Bigtable attempt status.   
`client_name`: Cloud Bigtable client name.   
`client/client_blocking_latencies` GA ** _(project)_**   
Client Blocking Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The latency introduced by the client by blocking on sending more requests to the server when there are too many pending requests in bulk operations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`client_name`: Cloud Bigtable client name.   
`client/connectivity_error_count` GA ** _(project)_**   
Connectivity Error Count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of requests that failed to reach the Google network. (Requests without google response headers). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`client/first_response_latencies` GA ** _(project)_**   
First Response Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Latency from operation start until the response headers were received. The publishing of the measurement will be delayed until the attempt response has been received. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`client/operation_latencies` GA ** _(project)_**   
Operation Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of the total end-to-end latency across all RPC attempts associated with a Bigtable operation. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`streaming`: (BOOL) Cloud Bigtable streaming method.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`client/retry_count` GA ** _(project)_**   
Retry Count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The number of additional RPCs sent after the initial attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`client/server_latencies` GA ** _(project)_**   
Server Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The latency measured between the time when Google frontend receives an RPC and sending back the first byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`streaming`: (BOOL) Cloud Bigtable streaming method.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`cluster/autoscaling/max_node_count` GA ** _(project)_**   
Maximum nodes   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Maximum number of nodes in an autoscaled cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Storage type for the cluster.   
`cluster/autoscaling/min_node_count` GA ** _(project)_**   
Minimum nodes   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Minimum number of nodes in an autoscaled cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Storage type for the cluster.   
`cluster/autoscaling/recommended_node_count_for_cpu` GA ** _(project)_**   
Recommended nodes based on CPU   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Recommended number of nodes in an autoscaled cluster based on CPU usage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`cluster/autoscaling/recommended_node_count_for_storage` GA ** _(project)_**   
Recommended nodes based on storage   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Recommended number of nodes in an autoscaled cluster based on storage usage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`cluster/autoscaling/storage_utilization_at_max` GA ** _(project)_**   
Storage utilization at autoscaler max   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Storage utilization at autoscaling max, i.e., storage used as a fraction of total storage capacity if the cluster is scaled to maximum node count. Writes are blocked if this reaches 100%. For details, see https://docs.cloud.google.com/bigtable/docs/autoscaling#how-it-works. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_type`: Type of disk storage (ssd and ssd+infrequent_access for SSD clusters, hdd for HDD clusters).   
`cluster/cpu_load` GA ** _(project)_**   
CPU load   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _CPU load of a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`cluster/cpu_load_by_app_profile_by_method_by_table` GA ** _(project)_**   
CPU load by app profile, method, and table   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _CPU load of a cluster. Split by app profile, method, and table. Contains the same underlying data as bigtable.googleapis.com/cluster/cpu_load. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`app_profile`: Cloud Bigtable application profile.   
`method`: Cloud Bigtable API method.   
`table`: Cloud Bigtable table name.   
`cluster/cpu_load_hottest_node` GA ** _(project)_**   
CPU load (hottest node)   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _CPU load of the busiest node in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`cluster/cpu_load_hottest_node_high_granularity` GA ** _(project)_**   
CPU load (hottest node) high granularity   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _CPU load of the busiest node in a cluster sampled at a high granularity. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/disk_load` GA ** _(project)_**   
Disk load   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _For HDD clusters, the utilization of HDD disks. For SSD clusters with tiered storage enabled, the utilization of the infrequent access tier disks. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`cluster/node_count` GA ** _(project)_**   
Nodes   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Number of nodes in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Storage type for the cluster.   
`cluster/storage_utilization` GA ** _(project)_**   
Storage utilization   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Storage used as a fraction of total storage capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_type`: Type of disk storage (ssd and ssd+infrequent_access for SSD clusters, hdd for HDD clusters).   
`disk/bytes_used` GA ** _(project)_**   
Data stored   
`GAUGE`, `INT64`, `By`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Amount of compressed data for tables stored in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_type`: Type of disk storage (ssd, hdd, or infrequent_access).   
`disk/per_node_storage_capacity` GA ** _(project)_**   
Storage capacity per node   
`GAUGE`, `INT64`, `By`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Capacity of compressed data for tables that can be stored per node in the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Type of disk storage (ssd and ssd+infrequent_access for SSD clusters, hdd for HDD clusters).   
`disk/storage_capacity` GA ** _(project)_**   
Storage capacity   
`GAUGE`, `INT64`, `By`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Capacity of compressed data for tables that can be stored in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Type of disk storage (ssd and ssd+infrequent_access for SSD clusters, hdd for HDD clusters).   
`materialized_view/intermediate_storage` GA ** _(project)_**   
Data for intermediate processing.   
`GAUGE`, `INT64`, `By`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Amount of data used by intermediate processing for the materialized view in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`storage_type`: Type of disk storage.   
`materialized_view/max_delay` GA ** _(project)_**   
Maximum processing delay   
`GAUGE`, `INT64`, `s`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Upper bound of processing delay for the materialized view. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`materialized_view/storage` GA ** _(project)_**   
Materialized view data.   
`GAUGE`, `INT64`, `By`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Amount of data used for the materialized view storage in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`storage_type`: Type of disk storage.   
`materialized_view/system_errors` GA ** _(project)_**   
System error count   
`DELTA`, `INT64`, `1`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Number of errors from system for the materialized view. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`canonical_status`: Canonical error status.   
`materialized_view/user_errors` GA ** _(project)_**   
User error count   
`DELTA`, `INT64`, `1`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Number of errors from user data for the materialized view. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`canonical_status`: Canonical error status.   
`memory_layer/hit_ratio` BETA ** _(project)_**   
Memory layer hit ratio   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Ratio of number of read requests that successfully read from the memory layer compared to all memory eligible read requests. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`memory_layer/ineligible_reason_count` BETA ** _(project)_**   
Memory layer ineligible reason count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of requests that were ineligible for the memory layer, broken down by the reason. One request may be counted for multiple reasons. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`reason`: Reason that request is ineligible for the memory layer.   
`memory_layer/max_request_units` BETA ** _(project)_**   
Memory layer max request units   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Maximum number of Request-Units per second used in a 5 minute window. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`memory_layer/read_latencies` BETA ** _(project)_**   
Memory layer read request latencies   
`DELTA`, `DISTRIBUTION`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of server read request latencies for a table that attempted to reach the memory layer. The latency is measured between the time when Cloud Bigtable (behind the Google frontend) receives an RPC and the time when it sends back the last byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`memory_access`: Whether the memory read was successful in this request.   
`memory_layer/read_request_count` BETA ** _(project)_**   
Memory layer read request count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of read requests for a table that went to the memory layer, broken down by whether the memory read was successful. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`memory_access`: Whether the memory read was successful in this request.   
`memory_layer/request_unit_count` BETA ** _(project)_**   
Memory layer request unit count   
`DELTA`, `DOUBLE`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The Request-Unit usage for read requests that attempt to use the memory layer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`memory_access`: Whether the memory read was successful in this request.   
`memory_layer/storage_capacity` BETA ** _(project)_**   
Memory layer storage capacity   
`GAUGE`, `INT64`, `By`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Memory layer storage capacity in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`replication/latency` GA ** _(project)_**   
Replication latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of the replication latencies of mutations to a table, measured as the difference between the commit time at the source and destination clusters. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`source_cluster`: Source cluster of the replicated data.   
`source_zone`: Source zone of the replicated data.   
`replication/max_delay` GA ** _(project)_**   
Replication maximum delay   
`GAUGE`, `DOUBLE`, `s`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Upper bound for replication delay between clusters of a table. Indicates the time frame during which latency information may not be accurate. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`source_cluster`: Source cluster of the replicated data.   
`source_zone`: Source zone of the replicated data.   
`server/data_boost/eligibility_count` GA ** _(project)_**   
Data Boost traffic eligibility count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Current Bigtable requests that are eligible and ineligible for Data Boost. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`app_profile`: Cloud Bigtable application profile.   
`eligibility`: Whether request is eligible for Data Boost.   
`server/data_boost/ineligible_reasons` GA ** _(project)_**   
Data Boost traffic ineligible reasons   
`GAUGE`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Reasons that current traffic is ineligible for Data Boost. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`app_profile`: Cloud Bigtable application profile.   
`ineligible_reason`: Reason that request is ineligible for Data Boost.   
`server/data_boost/spu_usage` GA ** _(project)_**   
Data Boost SPU Usage   
`GAUGE`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The Serverless-Processing-Units usage (in SPU-seconds) for Data Boost requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`app_profile`: Cloud Bigtable application profile.   
`method`: Cloud Bigtable API method.   
`server/error_count` GA ** _(project)_**   
Error count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of server requests for a table that failed with an error. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`error_code`: gRPC Error Code.   
`app_profile`: Cloud Bigtable application profile.   
`server/latencies` GA ** _(project)_**   
Server Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of server request latencies for a table. The latency is measured between the time when Cloud Bigtable (behind the Google frontend) receives an RPC and the time when it sends back the last byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/modified_rows_count` GA ** _(project)_**   
Modified rows   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of rows modified by server requests for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/multi_cluster_failovers_count` GA ** _(project)_**   
Multi-cluster failovers   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of failovers during multi-cluster requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/read_latencies_by_storage_tier` BETA ** _(project)_**   
Server Read Latencies by Storage Tier   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of server read request latencies by storage tier for a table. The latency is measured between the time when Cloud Bigtable (behind the Google frontend) receives an RPC and the time when it sends back the last byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`storage_tier`: Type of storage tier accessed in the request (ssd, infrequent_access, ssd+infrequent_access, or unknown).   
`server/read_request_count_by_storage_tier` BETA ** _(project)_**   
Read request count by Storage Tier   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of server read requests by storage tier for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`storage_tier`: Type of storage tier accessed in the request (ssd, infrequent_access, ssd+infrequent_access, or unknown).   
`server/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of bytes of request data received by servers for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of server requests for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/request_max_per_minute_count` GA ** _(project)_**   
Five-second maximum requests per minute   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Maximum number of requests received in a five-second span per minute. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/returned_rows_count` GA ** _(project)_**   
Returned rows   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of rows returned by server requests for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of bytes of response data sent by servers for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`table/bytes_transferred_to_infrequent_access` BETA ** _(project)_**   
Data moved to infrequent access storage   
`GAUGE`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Amount of uncompressed data moved to infrequent access storage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`table/bytes_used` GA ** _(project)_**   
Data stored   
`GAUGE`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Amount of compressed data stored in a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`storage_type`: Type of disk storage (ssd, hdd, or infrequent_access).   
`table/change_stream_log_used_bytes` GA ** _(project)_**   
Change stream data   
`GAUGE`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Amount of disk storage used by the change stream logs. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`storage_type`: Type of disk storage.   
  
### billingbudgets

Metrics from the [Cloud Billing](https://docs.cloud.google.com/billing/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `billingbudgets.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`quota/budget_count/exceeded` GA ** _(project)_**   
Budget limit per billing account quota exceeded error   
`DELTA`, `INT64`, `1`   
**[billingbudgets.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_billingbudgets.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric billingbudgets.googleapis.com/budget_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`billing_account_id`: Billing account id.   
`quota/budget_count/limit` GA ** _(project)_**   
Budget limit per billing account quota limit   
`GAUGE`, `INT64`, `1`   
**[billingbudgets.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_billingbudgets.googleapis.com/Location)** |  _Current limit on quota metric billingbudgets.googleapis.com/budget_count. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`billing_account_id`: Billing account id.   
`quota/budget_count/usage` GA ** _(project)_**   
Budget limit per billing account quota usage   
`GAUGE`, `INT64`, `1`   
**[billingbudgets.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_billingbudgets.googleapis.com/Location)** |  _Current usage on quota metric billingbudgets.googleapis.com/budget_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`billing_account_id`: Billing account id.   
  
### blockchainnodeengine

Metrics from the [Blockchain Node Engine](https://docs.cloud.google.com/blockchain-node-engine/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `blockchainnodeengine.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`node/active_peers` BETA ** _(project)_**   
Peer Count   
`GAUGE`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _The number of connected peers of the node. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/beacon_aggregated_attestation_processing_requests_count` BETA ** _(project)_**   
Aggregated Attestation Requests Count   
`DELTA`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _Total number of all aggregated attestations submitted for processing. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/beacon_aggregated_attestation_processing_successes_count` BETA ** _(project)_**   
Aggregated Attestations Verified For Gossip   
`DELTA`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _Total number of aggregated attestations verified for gossip. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/beacon_attestation_processing_signature_seconds` BETA ** _(project)_**   
Signature Verification Latencies   
`GAUGE`, `DISTRIBUTION`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _Current time spent on the signature verification of attestation processing. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/block_height` BETA ** _(project)_**   
Block Height   
`GAUGE`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _The block height of the node. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/block_timestamp` BETA ** _(project)_**   
Block Timestamp   
`GAUGE`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _The timestamp of the most recent block. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/cpu/utilization` BETA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _The amount of work the CPU handles to process resources. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/disk/total_ops_count` BETA ** _(project)_**   
Cumulative Disk Operations   
`DELTA`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _Cumulative count of disk reads and writes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`direction`: Direction of flow of bytes/operations (read or write).   
`node/memory/utilization` BETA ** _(project)_**   
Memory Utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _The amount of memory in use currently by running processes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/pending_transactions` BETA ** _(project)_**   
Pending Transactions   
`GAUGE`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _The number of transactions available to be processed and included in the next block. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/total_request_count` BETA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _The total number of requests received by the node. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`endpoint`: RPC endpoint to which requests are sent.   
`node/validators_total` BETA ** _(project)_**   
Validator Count   
`GAUGE`, `INT64`, `1`   
**[blockchainnodeengine.googleapis.com/BlockchainNode](https://docs.cloud.google.com/monitoring/api/resources#tag_blockchainnodeengine.googleapis.com/BlockchainNode)** |  _Total count of validators that are specifically monitored by this beacon node. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
