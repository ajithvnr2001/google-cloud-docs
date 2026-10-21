---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig/
title: FeaturestoreMonitoringConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:57:25.727093+00:00
---

# FeaturestoreMonitoringConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  FeaturestoreMonitoringConfig Stay organized with collections  Save and categorize content based on your preferences. 

Configuration of how features in Featurestore are monitored.

Fields  
  
`snapshotAnalysis` `object (`[SnapshotAnalysis](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#SnapshotAnalysis)`)` The config for Snapshot Analysis Based feature Monitoring. | `importFeaturesAnalysis` `object (`[ImportFeaturesAnalysis](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#ImportFeaturesAnalysis)`)` The config for ImportFeatures Analysis Based feature Monitoring. | `numericalThresholdConfig` `object (`[ThresholdConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#ThresholdConfig)`)` Threshold for numerical features of anomaly detection. This is shared by all objectives of Featurestore Monitoring for numerical features (i.e. Features with type (`[feature.ValueType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.features#Feature.ValueType)`) DOUBLE or INT64). | `categoricalThresholdConfig` `object (`[ThresholdConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#ThresholdConfig)`)` Threshold for categorical features of anomaly detection. This is shared by all types of Featurestore Monitoring for categorical features (i.e. Features with type (`[feature.ValueType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.features#Feature.ValueType)`) BOOL or STRING). | JSON representation  
---  
      
    
    {
      "snapshotAnalysis": {
        object ([SnapshotAnalysis](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#SnapshotAnalysis))
      },
      "importFeaturesAnalysis": {
        object ([ImportFeaturesAnalysis](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#ImportFeaturesAnalysis))
      },
      "numericalThresholdConfig": {
        object ([ThresholdConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#ThresholdConfig))
      },
      "categoricalThresholdConfig": {
        object ([ThresholdConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#ThresholdConfig))
      }
    }  
  
## SnapshotAnalysis

Configuration of the Featurestore's Snapshot Analysis Based Monitoring. This type of analysis generates statistics for each feature based on a snapshot of the latest feature value of each entities every monitoringInterval.

Fields  
  
`disabled` `boolean` The monitoring schedule for snapshot analysis. For EntityType-level config: unset / disabled = true indicates disabled by default for Features under it; otherwise by default enable snapshot analysis monitoring with monitoringInterval for Features under it. feature-level config: disabled = true indicates disabled regardless of the EntityType-level config; unset monitoringInterval indicates going with EntityType-level config; otherwise run snapshot analysis monitoring with monitoringInterval regardless of the EntityType-level config. Explicitly Disable the snapshot analysis based monitoring. | `monitoringInterval  
**(deprecated)**` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` This item is deprecated!Configuration of the snapshot analysis based monitoring pipeline running interval. The value is rolled up to full day. If both `[monitoringIntervalDays](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#SnapshotAnalysis.FIELDS.monitoring_interval_days)` and the deprecated `monitoringInterval` field are set when creating/updating EntityTypes/Features, `[monitoringIntervalDays](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#SnapshotAnalysis.FIELDS.monitoring_interval_days)` will be used.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `monitoringIntervalDays` `integer` Configuration of the snapshot analysis based monitoring pipeline running interval. The value indicates number of days. | `stalenessDays` `integer` Customized export features time window for snapshot analysis. Unit is one day. Default value is 3 weeks. Minimum value is 1 day. Maximum value is 4000 days. | JSON representation  
---  
      
    
    {
      "disabled": boolean,
      "monitoringInterval": string,
      "monitoringIntervalDays": integer,
      "stalenessDays": integer
    }  
  
## ImportFeaturesAnalysis

Configuration of the Featurestore's ImportFeature Analysis Based Monitoring. This type of analysis generates statistics for values of each feature imported by every `[ImportFeatureValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/importFeatureValues#google.cloud.aiplatform.v1beta1.FeaturestoreService.ImportFeatureValues)` operation.

Fields  
  
`state` `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#State)`)` Whether to enable / disable / inherite default hebavior for import features analysis. | `anomalyDetectionBaseline` `enum (`[Baseline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#Baseline)`)` The baseline used to do anomaly detection for the statistics generated by import features analysis. | JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#State)),
      "anomalyDetectionBaseline": enum ([Baseline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeaturestoreMonitoringConfig#Baseline))
    }  
  
## State

The state defines whether to enable ImportFeature analysis.

Enums  
---  
`STATE_UNSPECIFIED` | Should not be used.  
`DEFAULT` | The default behavior of whether to enable the monitoring. EntityType-level config: disabled. feature-level config: inherited from the configuration of EntityType this feature belongs to.  
`ENABLED` | Explicitly enables import features analysis. EntityType-level config: by default enables import features analysis for all Features under it. feature-level config: enables import features analysis regardless of the EntityType-level config.  
`DISABLED` | Explicitly disables import features analysis. EntityType-level config: by default disables import features analysis for all Features under it. feature-level config: disables import features analysis regardless of the EntityType-level config.  
  
## Baseline

Defines the baseline to do anomaly detection for feature values imported by each `[ImportFeatureValues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/importFeatureValues#google.cloud.aiplatform.v1beta1.FeaturestoreService.ImportFeatureValues)` operation.

Enums  
---  
`BASELINE_UNSPECIFIED` | Should not be used.  
`LATEST_STATS` | Choose the later one statistics generated by either most recent snapshot analysis or previous import features analysis. If non of them exists, skip anomaly detection and only generate a statistics.  
`MOST_RECENT_SNAPSHOT_STATS` | Use the statistics generated by the most recent snapshot analysis if exists.  
`PREVIOUS_IMPORT_FEATURES_STATS` | Use the statistics generated by the previous import features analysis if exists.  
  
## ThresholdConfig

The config for Featurestore Monitoring threshold.

Fields  
  
`threshold` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`value` `number` Specify a threshold value that can trigger the alert. 1. For categorical feature, the distribution distance is calculated by L-inifinity norm. 2. For numerical feature, the distribution distance is calculated by Jensen–Shannon divergence. Each feature must have a non-zero threshold if they need to be monitored. Otherwise no alert will be triggered for that feature. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // threshold
      "value": number
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
