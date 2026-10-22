---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-overview/
title: Monitoring and logging overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:32:57.658826+00:00
---

# Monitoring and logging overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Monitoring and logging overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped provides monitoring, logging, and alerting services, letting you maintain visibility, data observability, and control over your deployments. These services let you configure custom resources for the observability of your own applications and services.

This overview outlines the key components and considerations for the observability stack in GDC.

## Observability features

GDC includes the following features as part of its observability resources:

  * **Integrated stack** : GDC offers a comprehensive and integrated suite of observability tools, including metrics collection, monitoring dashboards, alerting mechanisms, and log management, all within the secure confines of your air-gapped environment.
  * **Automated data collection** : Agents and services automatically gather metrics and logs from various sources like infrastructure components, applications, and audit trails for comprehensive data capture. However, you can also configure resources to collect logs and metrics and gain insights from your own workloads.
  * **Data security and sovereignty** : All collected data remains within your air-gapped environment, ensuring compliance with security and data residency regulations.
  * **Open standards and integration** : Use open standards and APIs to integrate with existing monitoring tools, incident management systems, and security information and event management (SIEM) solutions.



## Key components

The GDC observability stack includes the following components for application insights and performance analytics:

  * **Monitoring** :

    * **Metrics collection** : GDC includes agents and services that collect key metrics from infrastructure components such as computing, storage, networking, and applications. These metrics provide insights into system performance, resource utilization, and application health.
    * **Monitoring platform** : A dedicated service within the air-gapped environment collects, stores, and processes metrics. This service offers dashboards, visualizations, and tools for analyzing trends, identifying anomalies, and troubleshooting issues.
    * **Integration with existing tools** : The monitoring service integrates with existing tools and frameworks, letting you use standard interfaces and workflows.
  * **Logging** :

    * **Log collection** : GDC automatically collects logs from various sources, including system components, applications, and audit trails. This centralized log collection simplifies troubleshooting and security analysis.
    * **Log storage and retention** : A dedicated logging service within the air-gapped environment provides secure and scalable log storage. Configure retention policies to meet compliance and operational requirements.
    * **Log analysis and search** : Search and filtering capabilities enable efficient log analysis to identify root causes, troubleshoot issues, and detect security threats.
  * **Alerting** :

    * **Alerting policies** : Define alerting policies based on metric thresholds, events, or anomalies. These policies trigger notifications when specific conditions are met, enabling proactive responses to potential issues.
    * **Notification channels** : Configure various notification channels, such as email, SMS, or integration with incident management systems, to ensure alerts reach the appropriate destination.
    * **Alert escalation** : Implement alert escalation procedures to ensure timely responses and prevent alert fatigue.



## High-level workflow

The GDC observability stack operates with the following workflow:

  1. **Deployment** : Deploy your observability solution within your isolated environment.
  2. **Configuration** : Configure data sources, metrics, and log collection parameters based on your monitoring and logging requirements.
  3. **Data collection** : Agents and services automatically collect metrics and logs from designated sources.
  4. **Monitoring and analysis** : Use dashboards, visualizations, and analytical tools to monitor system performance, application health, and security events.
  5. **Alerting** : Define alerting policies based on thresholds, events, or anomalies to trigger notifications through various channels.
  6. **Troubleshooting and remediation** : Utilize collected logs and metrics to investigate and diagnose issues, enabling resolution and minimizing downtime.



## Benefits

You obtain the following benefits when using observability solutions in GDC:

  * **Enhanced visibility** : Gain deep insights into your air-gapped environment's health, performance, and security.
  * **Issue mitigation** : Detect and address potential problems before they impact operations through real-time monitoring and alerting.
  * **Improved security** : Strengthen security by monitoring activities, analyzing audit trails, and identifying potential threats.
  * **Streamlined troubleshooting** : Diagnose and resolve issues using centralized logs and detailed performance metrics.
  * **Increased operational efficiency** : Optimize resource utilization, reduce downtime, and improve overall operational efficiency.
  * **Compliance and data sovereignty** : Keep all observability data within your air-gapped environment to maintain compliance with data residency and security regulations.



By taking advantage of these features and benefits, you can effectively manage and secure your isolated environments, ensuring smooth operations and minimizing risks.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
