---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/quality-alerts/
title: Configure quality alerts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:20.644409+00:00
---

# Configure quality alerts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/quality-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Configure quality alerts Stay organized with collections  Save and categorize content based on your preferences. 

Quality alerts notify you when your agent's performance drops below a defined threshold. You can use these alerts to detect **quality drift** —an observable decrease in agent performance over time. This decrease can occur even if the underlying model remains the same, often driven by changes in real-world user behavior, evolving data patterns, or subtle interactions in complex prompt chains.

**Why use quality alerts?**

  * **Automatic Detection:** Identify performance drops without manual spot-checks.
  * **Proactive Response:** Get notified using Slack, email, or Pub/Sub.
  * **Traceability:** Link alerting policies directly back to the specific traces that caused the drift.



When you configure an **Online Monitor** , the system automatically exports numeric evaluation scores to Cloud Monitoring. These metrics trigger **incidents** in Cloud Monitoring. You can then create **alerting policies** to notify your team when quality issues arise.

You can create targeted alerting policies for a specific monitor:

  1. In the Google Cloud console, navigate to the **Agent Platform > Agents** page.
  2. In the left navigation menu, select **Evaluation**. 

[Go to Evaluation](https://console.cloud.google.com/agent-platform/agent-evaluation)

  3. Select the **Online monitors** tab. Click **More options** _more_vert_ for a monitor and select **Create alerting policy**.

  4. Review the **Alerting policy templates** available for that monitor.

  5. Select the templates you want to enable. The system provides one template per metric configured on the monitor.

  6. **Configure Notifications:** Select your **Notification Channels**. If you uncheck **Use notification channels** , the system performs checks but does not proactively notify users. You can still view triggered incidents on the **Monitoring > Alerting** page.

  7. Click **Create**.




## Create recommended alerts from the dashboard

The Evaluation Dashboard provides a shortcut to enable broad quality guardrails for all active monitors:

  1. In the Google Cloud console, navigate to the **Agent Platform > Agents** page.
  2. In the left navigation menu, select **Deployments** and select your agent. 

[Go to Deployments](https://console.cloud.google.com/agent-platform/runtimes)

  3. Select the **Dashboard** tab and select the **Evaluation** subsection.

  4. Click the **Recommended Alerts** button in the top right corner.

  5. Review the available templates, such as:

     * **Online Monitor - Low evaluation score:** Triggers if the aggregate score for a monitor falls too low.
     * **Individual Metric Alerts:** Specific thresholds for metrics like **Task Success** or **Tool Use Quality**.
  6. Select the templates and notification channels, then click **Create**.




## Programmatic alert creation

For large-scale deployments, you can configure quality alerts using the `gcloud` CLI or the Cloud Monitoring API.

### Using gcloud

Create an alert policy from a JSON or YAML configuration file:
    
    
    gcloud monitoring policies create --policy-from-file="policy.yaml"
    

The following is an example `policy.yaml` that triggers if the average **Task Success** score falls below 80% over a 30-minute window:
    
    
    displayName: "Low Task Success Score"
    conditions:
    - displayName: "Task Success < 0.8"
      conditionThreshold:
        filter: >
          metric.type="aiplatform.googleapis.com/online_evaluator/scores"
          AND metric.labels.evaluation_metric_name="task_success"
        comparison: COMPARISON_LT
        thresholdValue: 0.8
        duration: 1800s
        aggregations:
        - alignmentPeriod: 60s
          perSeriesAligner: ALIGN_MEAN
    combiner: OR
    enabled: true
    notificationChannels:
    - "projects/YOUR_PROJECT_ID/notificationChannels/CHANNEL_ID"
    

### Using the Agent Platform SDK
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[AlertPolicyServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.alert_policy_service.AlertPolicyServiceClient.html)()
    project_name = f"projects/YOUR_PROJECT_ID"
    
    policy = {
        "display_name": "Agent Quality Drift",
        "conditions": [{
            "display_name": "Low Evaluation Score",
            "condition_threshold": {
                "filter": (
                    'metric.type="aiplatform.googleapis.com/online_evaluator/scores"'
                ),
                "comparison": [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ComparisonType](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ComparisonType.html).COMPARISON_LT,
                "threshold_value": 0.7,
                "duration": {"seconds": 3600},
                "aggregations": [{
                    "alignment_period": {"seconds": 60},
                    "per_series_aligner": [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).Aggregation.Aligner.ALIGN_MEAN,
                }],
            },
        }],
        "combiner": [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[AlertPolicy](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.html).[ConditionCombinerType](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.ConditionCombinerType.html).OR,
        "enabled": True,
    }
    
    response = client.[create_alert_policy](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.alert_policy_service.AlertPolicyServiceClient.html#google_cloud_monitoring_v3_services_alert_policy_service_AlertPolicyServiceClient_create_alert_policy)(name=project_name, alert_policy=policy)
    print(f"Created alerting policy {response.name}")
    

## Manage alerting policies

Use the **Cloud Monitoring** console to view where your alerting policies are located and refine their configurations. Each incident includes labels for the associated Online Monitor to help you investigate the root cause. 

[Go to Alerting](https://console.cloud.google.com/monitoring/alerting)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
