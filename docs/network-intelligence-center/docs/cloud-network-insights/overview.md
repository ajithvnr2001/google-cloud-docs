---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview/
title: Cloud Network Insights overview \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:16.525918+00:00
---

# Cloud Network Insights overview  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Cloud Network Insights overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Network Insights, offered in partnership with AppNeta by Broadcom, provides visibility into network health and application performance across multicloud and hybrid environments.

Using Cloud Network Insights, your network and operations teams can monitor your network to identify whether an application's degradation is due to the network or the application itself. The source of the degradation could be in Google Cloud, third-party cloud service providers, last-mile connectivity to on-premises, or the internet.

Cloud Network Insights uses active synthetic probing to monitor these paths from the perspective of the user or the application, allowing you to monitor network routes even when no user traffic is present. You can then find potential issues before they impact your users.

## Features and benefits

Cloud Network Insights provides the following benefits:

  * **Proactive detection** : Identify network and application performance issues with synthetic testing, often before they impact users.
  * **End-to-end visibility** : Monitor paths across networks you don't own, such as ISP links and third-party cloud services.
  * **Rapid root cause analysis** : Quickly differentiate between network problems, application-level issues, or browser performance impacts.
  * **SLA validation** : Obtain metrics to verify if ISPs and other service providers meet their performance commitments.
  * **Web application insights** : Measure user experience metrics for web applications, such as DNS resolution time or full browser page-load times.
  * **Integrated monitoring** : Access metrics and logs directly within Google Cloud, leveraging Cloud Monitoring and Cloud Logging for dashboards and alerting.



## How Cloud Network Insights works

Cloud Network Insights performs active synthetic probing to collect real-time performance telemetry from across your network. _Monitoring Points_ —lightweight monitoring agent software—send their collected data and receive configuration updates by communicating securely over the internet with the central Cloud Network Insights control plane, hosted on Google Cloud and managed by AppNeta.

Cloud Network Insights captures elements such as packet-level timing, path hops, and application response codes to visualize the health of your network routes. After processing this data through specialized analysis engines, Cloud Network Insights exports the results with Google Cloud Observability to provide a unified view of your network health.

Monitor your network with Cloud Network Insights by doing the following:

  1. [**Deploy Monitoring Points**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/add-monitoring-points). These are the source of the synthetic probes and can be the destination or target of the probes.
  2. [**Configure monitoring policies**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies). These tell Monitoring Points what to probe (network paths or web paths) and how frequently to run tests.
  3. [**Set up alarms and logging**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-logging). Alarms in AppNeta identify persistent network disruptions and send logs and events to Google Cloud Observability for alerting and notifications.
  4. [**Set up alerts and notifications**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts). Configure Google Cloud alert policies to notify your team using email, Slack, PagerDuty, or other [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).
  5. [**Analyze metrics**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/view-dashboards). Cloud Network Insights provides hop-by-hop visualizations of network paths and exports telemetry data to Google Cloud Observability for alerting and dashboards.



### Monitoring Points

Monitoring Points are software agents that execute synthetic probes. You can deploy them to critical network segments that represent your user base or application backend to monitor your network or web application performance. For example, you can deploy Monitoring Points to a central VPC, a remote branch, or a specific cloud region closest to your customers.

You can deploy Monitoring Points as containers or as virtual appliances to your cloud or your on-premises network.

### Monitoring policies

Monitoring policies are sets of rules that control how monitoring behaves. They link a Monitoring Point (source) to a destination (target). Monitoring policies determine which Monitoring Points run tests, on what targets, and how frequently.

#### Monitoring paths

Monitoring policies generates _paths_ —visualizations of the route taken by the probe packets. Cloud Network Insights supports two types of monitoring paths: **network paths** and **web paths**.

  * [**Network paths**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies#network_monitoring): Network paths provide a hop-by-hop visualization of the infrastructure (Layer 3 and 4) between a source and a destination. This is used to identify exactly where in the network (such as a specific ISP router or a hybrid gateway) a problem is occurring. It captures metrics such as round-trip time (RTT), packet loss, jitter, and path changes. These paths operate in two modes: 
    * **Single-ended paths** : The Monitoring Point probes an external target (for example, `google.com`, a SaaS VIP, or a router) that _does not_ have a Monitoring Point installed. This relies on standard protocols (ICMP, TCP, UDP, or Echo) and is ideal for monitoring public or third-party targets.
    * **Dual-ended paths** : The Monitoring Point probes a different Monitoring Point or [Global Monitoring Target](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/global-monitoring-targets.html). Since you control both ends, this mode provides richer data, including precise one-way latency, jitter, and the ability to detect asymmetric routing such as different paths for uploading versus downloading.
  * [**Web paths**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies#web_monitoring): Provide a monitor of the end-to-end experience of a web application (Layer 7). These paths operate in two modes: 
    * **Browser** : The Monitoring Point uses a real browser engine (Selenium) to load full web pages, execute JavaScript, and render content. This measures the complete page load time and validates the actual user experience.
    * **HTTP** : The Monitoring Point sends synthetic HTTP or HTTPS requests to a URL or API endpoint. This creates a lightweight check for server availability, response time, and TLS or DNS performance without the overhead of loading a full page.



### Alarms

Alarms are the intelligence layer that identifies persistent network issues and represent a change in the state of your network health. They are created by [alarm rules in AppNeta](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-logging#create_alarm_rules_in_appneta) that define metric thresholds and how many times a metric must exceed that threshold (violation) in a period to trigger an event. These events are then sent to Cloud Logging.

### Metrics and logs

All collected telemetry is exported to Google Cloud Observability to visualize your network architecture and performance in a single pane of glass. Depending on the type of data, the telemetry data is sent to either [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) or [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).

  * **Cloud Monitoring (Metrics)** : Quantitative performance data is exported as standard Google Cloud metrics. 
    * [**Network Health**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/monitoring-metrics#network_path_metrics): includes metrics such as minimum, average, and maximum round-trip time, packet loss percentage, and jitter.
    * [**Web Experience**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/monitoring-metrics#web_path_metrics): includes metrics such as include total transaction time, DNS lookup time, time to first byte (TTFB), and HTTP status codes.
  * [**Cloud Logging (Events)**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/monitoring-metrics#web_path_metrics): Qualitative state changes and alarms are exported as structured logs. You can query these logs in the Logs Explorer to perform root-cause analysis or create log-based alerts for immediate notification. 
    * `networkmanagement.googleapis.com/insights_alarm`: Triggered when performance deviates from your defined baselines.
    * `networkmanagement.googleapis.com/insights_event`: Triggered by structural changes, such as when a Monitoring Point goes offline and online again, or a network route change (path change).



### Alerts and notifications

Alert policies are the mechanism within [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) that delivers notifications to your team.

  * [**Log-Based Alerting**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-logging#view-logs-gcp): Cloud Network Insights utilizes log-based alert policies. When an alarm triggers, it writes a structured log entry (`networkmanagement.googleapis.com/insights_alarm`) to Cloud Logging.
  * [**Pre-defined Templates**](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts#use-predefined-templates): To simplify configuration, Cloud Network Insights provides predefined alert policy templates in the Google Cloud console. These templates let you to quickly create policies for common scenarios such as a `Critical Network Alarm`.
  * **Notification Channels** : Alert policies connect to your existing Google Cloud notification channels, enabling you to receive Cloud Network Insights alerts using email, Slack, PagerDuty, SMS, or Pub/Sub.



## Actions and platforms

Cloud Network Insights management tasks are split between Google Cloud and AppNeta. The following table maps common actions to the correct platform you perform them on.

**Actions** | **Interface** | **Description**  
---|---|---  
[Deploy Monitoring Points](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/add-monitoring-points) | Google Cloud console | Download the installation bundles (Docker, Helm, OVA) and view the connection status (Active or Offline) of your Monitoring Points here.  
View Monitoring Points | Google Cloud console | View your fleet of agents, check software versions, and identify which Monitoring Points require upgrades.  
[Create monitoring policies](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies) | AppNeta | Define the rules for testing, including source, target and profiles. These policies generate the active network paths and web paths that collect telemetry.   
[View high-level metrics](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/view-dashboards) | Google Cloud console | View standard performance metrics (latency, loss, jitter) for your paths directly in Cloud Monitoring dashboards.  
Deep dive troubleshooting | AppNeta | View advanced diagnostics, such as hop-by-hop route visualizations (TruPath) or a timeline chart for web transactions.  
Create alarm rules | AppNeta | Define the thresholds that trigger events and logs to be sent to Google Cloud.  
[Configure alert policies and notifications](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts) | Google Cloud console | Configure notification policies (email, Slack, PagerDuty, or Pub/Sub) using log-based alerting policies.  
  
## Data synchronization

While configuration happens in two places, the data is synchronized back to Google Cloud:

  * **Metrics** : Performance data collected by Monitoring Points is exported to Cloud Monitoring.
  * **Logs** : Alarms and events generated by AppNeta are exported to Cloud Logging.



## What's next

  * To learn more about Cloud Network Insights, watch [the video overview and product demo](https://youtu.be/rqh9-32mX0E) on the Google Cloud channel on YouTube.



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
