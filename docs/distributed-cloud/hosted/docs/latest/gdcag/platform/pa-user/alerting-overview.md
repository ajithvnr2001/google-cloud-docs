---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/alerting-overview/
title: Alerting overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:04.277023+00:00
---

# Alerting overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/alerting-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Alerting overview Stay organized with collections  Save and categorize content based on your preferences. 

Alerts help you stay informed about the health and performance of your air-gapped deployments. They provide timely notifications when specific conditions are met, letting you do the following:

  * **Proactively address issues** : Detect and respond to problems before they impact users or business operations.
  * **Reduce downtime** : Minimize service disruptions by taking corrective action quickly.
  * **Maintain service levels** : Ensure your applications meet performance and availability targets.
  * **Gain operational insights** : Identify trends and patterns in your environment to optimize resource utilization and performance.



This page provides an overview of creating and managing alerts in Google Distributed Cloud (GDC) air-gapped environments. It explains how to use monitoring data to proactively identify and respond to critical events within your applications and infrastructure.

## Alerting policy types

Metric-based alerting policies track monitoring data and notify specific people when a resource meets a pre-established condition. For example, an alerting policy that monitors the CPU utilization of a virtual machine might send a notification when an event activates the policy. Alternatively, a policy that monitors an uptime check might notify on-call and development teams.

On the other hand, to monitor recurring events in your logs over time, use log-based metrics to create alerting policies. Log-based metrics generate numerical data from logging data. Log-based metrics are suitable when you want to do any of the following:

  * Count the message occurrences in your logs, like a warning or error. Receive a notification when the number of events crosses a threshold.
  * Observe trends in your data, like latency values in your logs. Receive a notification if the values change unacceptably.
  * Create charts to display the numeric data extracted from your logs.



In GDC, alerts can generate pages and tickets for critical errors. Pages require immediate attention from an operator, while tickets are less urgent.

## Key components

The GDC alerting service uses the following components:

  * **Prometheus** : An open-source monitoring system widely used for collecting and storing metrics. It provides a powerful query language (PromQL) for defining alert rules.
  * **Monitoring platform** : A managed monitoring service that collects metrics from various sources, including Prometheus. It offers advanced features like Grafana dashboards, custom metrics, and alerting.
  * **Alertmanager** : A component responsible for receiving, processing, and routing alerts. It supports grouping, silencing, and inhibiting alerts to reduce noise and improve efficiency.



## Alerting workflow

GDC provides an alerting framework that integrates with various monitoring tools and services. The typical workflow involves the following stages:

  1. **Data collection** : Use tools like Prometheus and Fluent Bit to collect metrics and logs from your applications, infrastructure, and Kubernetes.
  2. **Monitoring** : Store and visualize the collected data in Grafana dashboards.
  3. **Alerting rules** : Define alert rules based on specific conditions, such as CPU usage exceeding a threshold or application errors exceeding a certain rate.
  4. **Alertmanager** : Alertmanager receives alerts triggered by the defined rules and handles notification routing and silencing.
  5. **Notifications** : Receive alerts through various channels, such as email, messages, or webhooks.



## Best practices

When setting up alerts, consider the following best practices:

  * **Define clear and actionable alerts** : Ensure your alerts provide specific information about the issue and suggest appropriate actions.
  * **Set appropriate severity levels** : Categorize alerts based on their impact and urgency to prioritize response efforts.
  * **Avoid alert fatigue** : Fine-tune your alert rules to minimize false positives and unnecessary notifications.
  * **Test your alerts regularly** : Verify that your alerts are triggered correctly and notifications are delivered as expected.
  * **Document your alerting strategy** : Document your alert rules, notification channels, and escalation procedures.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
