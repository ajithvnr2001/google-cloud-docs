---
url: https://docs.cloud.google.com/migrate/kf/docs/2.9/how-to/monitoring-dashboard/
title: Create and use monitoring dashboards \u00a0|\u00a0 Kf 2.9 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:21.131809+00:00
---

# Create and use monitoring dashboards  |  Kf 2.9  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.9/how-to/monitoring-dashboard/

Version 2.9

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.9 ](https://docs.cloud.google.com/migrate/kf/docs/2.9)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.9/getting-started)



Send feedback 

#  Create and use monitoring dashboards Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Cloud Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards) to create custom dashboards and charts. Kf comes with a default template which can be used to create dashboards to monitor the performance of your applications.

## Application performance dashboard

Run the following commands to deploy a dashboard in your monitoring workspace in [Cloud monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards) to monitor performance of your apps. This dashboard has application performance metrics like requests/sec, round trip latency, HTTP error codes, and more.
    
    
    git clone https://github.com/google/kf
    cd ./kf/dashboards
    ./create-dashboard.py my-dashboard my-cluster my-space
    

## System resources and performance dashboard

You can view all the system resources and performance metrics such as list of nodes, pods, containers and much more using a built-in dashboard. Click the link below to access the system dashboard.

[ System dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/kubernetes)

More details about this dashboard can be found [here](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/observing).

## Create SLO and alerts

You can create [SLOs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) and [Alerts](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert) on available metrics to monitor performance and availability of both system and applications. For example, you can use the metrics `istio.io/service/server/response_latencies` to setup an alert on the application roundtrip latency.

## Configure dashboard access control

Follow [these instructions](https://docs.cloud.google.com/monitoring/access-control) to provide dashboard access to developers and other members on the team. The role `roles/monitoring.dashboardViewer` provides read-only access to dashboards.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
