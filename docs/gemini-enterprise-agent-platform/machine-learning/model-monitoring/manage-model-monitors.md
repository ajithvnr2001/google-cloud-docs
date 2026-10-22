---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/
title: Manage model monitor \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:31.116947+00:00
---

# Manage model monitor  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Manage model monitor Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to update and delete model monitors.

## Update a model monitor

Update a model monitor to modify the default configuration for monitoring jobs. You can't change the model version that a model monitor is associated with. Instead, create a new model monitor.

### Console

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/agent-platform/model-monitoring/model-monitors)

  2. Click the model monitor to go to the **Monitor details** page.

  3. Click **Edit configuration** to update the model monitor.

  4. Modify your schema, notifications, training data source, and objectives.

  5. Click **Save**.




### Python SDK

You can update the following specifications:

  * Display name
  * Training dataset
  * Model schema
  * Default monitoring objectives
  * Default monitoring output specification
  * Default monitoring notification specification
  * Default explanation specification for feature attribution



The following example updates the model schema:
    
    
    monitor_2.update(model_monitoring_schema=MODEL_MONITORING_SCHEMA)

## Delete a model monitor

Remove model monitors to prevent authorized users from inadvertently running monitoring jobs on unused model monitors. When you delete a model monitor, any associated monitoring data is deleted except for metrics and statistics exported by Monitoring, which remain in Cloud Monitoring and in your Cloud Storage.

### Console

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/agent-platform/model-monitoring/model-monitors)

  2. Click the model monitor to go to the **Monitor details** page.

  3. Click **Edit configuration** to update the model monitor.




### Python SDK
    
    
    from google.cloud.aiplatform.private_preview.centralized_model_monitoring
    import model_monitor
    
    my_model_monitor.delete(force=true)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
