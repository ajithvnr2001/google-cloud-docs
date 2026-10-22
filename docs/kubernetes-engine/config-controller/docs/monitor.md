---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/monitor/
title: Monitor Config Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:22.416001+00:00
---

# Monitor Config Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  Monitor Config Controller Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to monitor Config Controller. Config Controller includes Config Connector, Config Sync and Policy Controller. Each operator includes multiple metrics.

This page is for IT administrators and Operators who monitor the health of deployed applications or services. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Set up Policy Controller monitoring

Allow Policy Controller to send metrics by running this command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:PROJECT_ID.svc.id.goog[gatekeeper-system/gatekeeper-admin]" \
      --role=roles/monitoring.metricWriter
    

Replace `PROJECT_ID` with the cluster's Google Cloud project ID.

## What's next

Learn more about options to monitor Config Connector, Config Sync and Policy Controller:

  * [Monitoring Config Connector with Prometheus](https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-prometheus)
  * [Use Config Sync metrics](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync)
  * [Use Policy Controller metrics](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
