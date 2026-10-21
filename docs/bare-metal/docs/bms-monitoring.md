---
url: https://docs.cloud.google.com/bare-metal/docs/bms-monitoring/
title: Monitoring in a Bare Metal Solution environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:37.653205+00:00
---

# Monitoring in a Bare Metal Solution environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-monitoring/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitoring in a Bare Metal Solution environment

Bare Metal Solution lets you run specialized workloads in regional extensions located near Google Cloud data centers. By implementing a Bare Metal Solution environment, you can lower your overall costs and reduce risks associated with migration to the cloud.

## Monitoring overview

One of our main priorities is to deliver the highest availability for the Bare Metal Solution environment. For that reason, Google Cloud and our partners perform a variety of monitoring activities. The following is a list of infrastructure devices in a Bare Metal Solution environment that we monitor:

**Compute infrastructure**

  * Server hardware 



**Storage infrastructure**

  * Storage devices 
  * SAN switches 



**Network infrastructure**

  * Routers 
  * Switches 
  * Interconnect infrastructure 



Google Cloud also keeps track of the data center environment, including server room temperature and humidity.

We do not monitor operating systems, application-level activity and workloads, and network traffic traveling to and from the Bare Metal Solution servers. To preview a utility that enables you to use Cloud Operations to monitor OS-level activity, contact [Google Cloud Sales](https://cloud.google.com/contact).

## Monitoring tools

Our partner uses commercial grade software solutions for monitoring that comply fully with the Information Technology Infrastructure Library (ITIL). Google Cloud and our partner also use Google Cloud services, such as Pub/Sub, Cloud Run functions, and Cloud Monitoring, to collect and process this monitoring data. Our internal ticketing and notification systems work directly with these services.

## Monitoring data

At a high level, our monitoring data comes from the following sources:

  * SNMP traps
  * Syslog messages
  * Messages from dedicated management software
  * Intelligent Platform Management Interface (IPMI)



Common metrics of the monitored devices:

  * CPU utilization
  * Network Interface: 
    * Bandwidth utilization
    * Packet discards
    * Errors



## Alerting

Google Cloud conducted extensive normalization and validation activities for the specific requirements of the Bare Metal Solution environment. If a certified event falls outside of the normal range, the monitoring system triggers an alert.

## Incident management

Google Cloud and our partner infrastructure provider have a dedicated 24/7 team responsible for incident response. A bridge team is also available 24/7 to perform the initial analysis of each support ticket and take the necessary actions to mitigate the issue. Based on the severity of the incident, we deploy appropriate teams to resolve the incident.

[Cloud Customer Care](https://cloud.google.com/support-hub) works with the Google Cloud Engineering SysOps Team. They can provide you with updates, and coordinate any actions that require your help. As needed, the Google Cloud Engineering Team engages with the infrastructure provider partner or hardware vendors to help resolve your issue.

## Root cause analysis process

When incidents have a wide and serious impact, Google provides incident reports that outline the symptoms, impact, root cause, remediation, and future prevention of incidents. As with postmortems, we pay particular attention to the steps that we take to learn from the issue and improve reliability.

We hope that this summary of our monitoring capabilities helps you to be confident in the Bare Metal Solution environment as you migrate your infrastructure and applications to the cloud. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
