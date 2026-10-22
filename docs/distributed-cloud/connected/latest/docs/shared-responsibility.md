---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/shared-responsibility/
title: Google Distributed Cloud connected shared responsibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:55.496017+00:00
---

# Google Distributed Cloud connected shared responsibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/shared-responsibility/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Resources ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/resources)



Send feedback 

#  Google Distributed Cloud connected shared responsibility Stay organized with collections  Save and categorize content based on your preferences. 

Monitoring and maintaining Google Distributed Cloud connected is a shared responsibility between you and Google. This page delineates those responsibilities.

## Overview

The following table summarizes the responsibilities for Distributed Cloud connected management tasks.

Issue | You | Google  
---|---|---  
Detect and notify you of disconnection from Google Cloud |  | X  
Detect and remedy power, cooling, and environment issues | X |   
Detect and remedy local network issues | X | X  
Identify and resolve issues with bastion host and boundary proxy instances | X |   
Monitor the Google Cloud control plane |  | X  
Monitor the Kubernetes control planes, worker nodes, and system services |  | X  
Monitor Google-supplied third-party solutions, such as Symcloud Storage |  | X  
Monitor and troubleshoot hardware procured directly from Google |  | X  
Monitor and troubleshoot hardware procured from a Google-certified third-party SI | X |   
Monitor and troubleshoot your local network | X |   
Monitor upstream network connectivity | X |   
Participate in joint diagnosis of network, power, or cooling issues | X |   
Platform observability, including metrics and logs. For more information, see [Logs and metrics](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/logs-metrics). |  | X  
Application observability, including metrics and logs. For more information, see [Monitor workload health](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/monitoring#monitor-workload-health-and-uptime). | X |   
Diagnose and remedy issues that part of your responsibilities | X |   
  
## Google's responsibilities

Google is responsible for the following aspects of your Distributed Cloud connected deployment:

  * The Distributed Cloud connected hardware that you've procured directly from Google; we're not responsible for hardware you've procured from a Google-partnered third-party systems integrator (SI)
  * The Google Cloud control plane
  * The Kubernetes control planes, worker nodes, and built-in system services running on the Distributed Cloud connected hardware
  * Google-supplied software add-ons and products



Google continuously monitors the health and performance of these aspects. For more information, see [Alerting strategy](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/monitoring#alerting-strategy). If we detect an issue, we notify you and take remedial action.

## Your responsibilities

You're responsible for the following aspects of your Distributed Cloud connected deployment:

  * Distributed Cloud connected hardware that you've procured from a Google-certified third-party systems integrator (SI); you're not responsible for hardware procured directly from Google
  * Your local network and its configuration
  * Your internet connectivity
  * Power, cooling, ambient temperature, and humidity at the deployment site
  * Third-party software solutions you've installed on your Distributed Cloud connected deployment
  * Your bastion host instances and boundary proxy deployments, if applicable
  * Your workloads



Google does not monitor these aspects nor notify you of any issues that arise. You are responsible for configuring alerts for your workloads and local environment. For more information, see [Alerting strategy](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/monitoring#alerting-strategy). If you believe that a workload issue is caused by Distributed Cloud connected, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

## Shared responsibilities

In some cases, Google might detect an issue that we believe falls within your responsibility. For example, we might detect rising temperatures within the Distributed Cloud connected hardware, followed by loss of connectivity to Google Cloud, which could indicate a cooling failure. In such situations, Google contacts you to collaboratively troubleshoot and remedy the issue. We might need further information about the incident in order to properly diagnose it; if you can't provide this information, resolution might be difficult.

### Connectivity failures

When the connection to Google Cloud is lost, your clusters enter [survivability mode](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/survivability) and your workloads continue to run for up to 7 days. Google can't monitor, diagnose, nor remedy issues until you restore this connection. We can't help you determine the cause of disconnection.

If we notice that your entire Distributed Cloud connected deployment has gone offline simultaneously, we might not notify you until we've confirmed the issue can't self-resolve; for example, an ISP outage at your deployment site could self-resolve within a reasonable timeframe.

#### Bastion host and boundary proxy deployments

If you've configured a bastion host instance or a boundary proxy instance on your Distributed Cloud connected deployment, Google monitors connectivity to those instances; if we detect an issue that we determine might be caused by your local network, we might ask you to troubleshoot and remedy them to restore proper operation.

### Information required for diagnosis

To diagnose issues that we detect with your Distributed Cloud connected deployment, we might ask for the following information:

  * Any configuration changes you've made to your local network, such as switches, routers, and firewalls, with second-accurate timestamps
  * Firewall denial logs, with second-accurate timestamps
  * Reasons and exact times for device restarts or power cycling, such as software or firmware upgrades, crashes, and other errors
  * Exact times of any power outages
  * Exact times of any local network outages, with second-accurate timestamps from router or firewall logs



### Third-party interoperability issues

For interoperability issues with third-party solutions, we might involve the corresponding vendor to diagnose them; this might include sharing log files and configuring diagnostic options. If available, we attempt to reproduce the issue in your lab environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
