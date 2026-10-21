---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/monitor-dns-metrics/
title: Monitor Cloud DNS metrics \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:54:42.677775+00:00
---

# Monitor Cloud DNS metrics  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/monitor-dns-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Monitor Cloud DNS metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to read Cloud DNS metrics dashboards in Google Distributed Cloud (GDC) air-gapped. The metrics dashboard provides graphs and visualization panels for viewing the health and performance of your Managed DNS Zones. Use these dashboards to monitor DNS requests, response rate, and latency.

This document is for developers in platform administrator or application operator groups that need to monitor DNS system health. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

Open the following URL to access the Cloud DNS dashboard:
    
    
    https://GDC_URL/PROJECT_NAME/grafana/d/cfemcae44701sb/cloud-dns
    

Replace the following:

  * `GDC_URL`: the URL of your organization in Google Distributed Cloud (GDC) air-gapped.
  * `PROJECT_NAME`: the name of your project.



## Cloud DNS dashboard

The Cloud DNS dashboard presents graphs and visualization panels that contain information about the requests, errors, and latency for your Managed DNS Zones.

### QPS per Managed Zone

This panel displays the queries per second (QPS) for each Managed DNS Zone in the selected project. It helps you visualize the rate of total DNS requests being handled by each zone.

![QPS per Managed Zone](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/dns-qps.png)

### Error Rate per Managed Zone

This panel shows the rate of DNS responses that are not `NOERROR` (successful resolution) or `NXDOMAIN` (hostname not found). Monitoring this metric helps you identify potential issues with DNS resolution, such as misconfigurations or server problems.

![Error Rate per Managed Zone](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/dns-error-rate.png)

### P99 latency per Managed Zone

This panel displays the 99th percentile of DNS request latency. This metric is useful for understanding the performance of your DNS zones and identifying potential bottlenecks that may be impacting request times.

![P99 latency per Managed Zone](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/dns-p99-latency.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
