---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureStatsAnomaly/
title: FeatureStatsAnomaly \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:45:29.189719+00:00
---

# FeatureStatsAnomaly  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureStatsAnomaly/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  FeatureStatsAnomaly Stay organized with collections  Save and categorize content based on your preferences. 

Stats and Anomaly generated at specific timestamp for specific feature. The startTime and endTime are used to define the time range of the dataset that current stats belongs to, e.g. prediction traffic is bucketed into prediction datasets by time window. If the Dataset is not defined by time window, startTime = endTime. timestamp of the stats and anomalies always refers to endTime. Raw stats and anomalies are stored in statsUri or anomalyUri in the tensorflow defined protos. Field dataStats contains almost identical information with the raw stats in Agent Platform defined proto, for UI to display.

Fields  
  
`score` `number` feature importance score, only populated when cross-feature monitoring is enabled. For now only used to represent feature attribution score within range [0, 1] for `[ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_SKEW](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.batchPredictionJobs#ModelDeploymentMonitoringObjectiveType.ENUM_VALUES.FEATURE_ATTRIBUTION_SKEW)` and `[ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_DRIFT](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.batchPredictionJobs#ModelDeploymentMonitoringObjectiveType.ENUM_VALUES.FEATURE_ATTRIBUTION_DRIFT)`. | `statsUri` `string` Path of the stats file for current feature values in Cloud Storage bucket. Format: gs:////stats. Example: gs://monitoring_bucket/featureName/stats. Stats are stored as binary format with Protobuf message [tensorflow.metadata.v0.FeatureNameStatistics](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/statistics.proto). | `anomalyUri` `string` Path of the anomaly file for current feature values in Cloud Storage bucket. Format: gs:////anomalies. Example: gs://monitoring_bucket/featureName/anomalies. Stats are stored as binary format with Protobuf message Anoamlies are stored as binary format with Protobuf message [tensorflow.metadata.v0.AnomalyInfo](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/anomalies.proto). | `distributionDeviation` `number` Deviation from the current stats to baseline stats. 1. For categorical feature, the distribution distance is calculated by L-inifinity norm. 2. For numerical feature, the distribution distance is calculated by Jensen–Shannon divergence. | `anomalyDetectionThreshold` `number` This is the threshold used when detecting anomalies. The threshold can be changed by user, so this one might be different from `[ThresholdConfig.value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ThresholdConfig#FIELDS.value)`. | `startTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), startTime is only used to indicate the monitoring intervals, so it always equals to (endTime - monitoringInterval).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `endTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The end timestamp of window where stats were generated. For objectives where time window doesn't make sense (e.g. Featurestore Snapshot Monitoring), endTime indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | JSON representation  
---  
      
    
    {
      "score": number,
      "statsUri": string,
      "anomalyUri": string,
      "distributionDeviation": number,
      "anomalyDetectionThreshold": number,
      "startTime": string,
      "endTime": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
