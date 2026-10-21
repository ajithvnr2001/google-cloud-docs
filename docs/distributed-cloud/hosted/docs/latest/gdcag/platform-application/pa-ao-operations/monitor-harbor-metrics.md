---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/monitor-harbor-metrics/
title: Monitor Harbor metrics \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:49.672787+00:00
---

# Monitor Harbor metrics  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/monitor-harbor-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Monitor Harbor metrics Stay organized with collections  Save and categorize content based on your preferences. 

The metrics dashboard of the Managed Harbor Service (MHS) component provides graphs and visualization panels for viewing storage consumption and the number of vulnerability scans performed.

Open the following URL to access the user cluster health dashboard:
    
    
    https://GDC_URL/platform-obs/grafana/d/haas-billing/haas-billing-dashboard?orgId=ORG_ID
    

Replace the following:

  * `GDC_URL`: the URL of your organization in Google Distributed Cloud (GDC) air-gapped.
  * `ORG_ID`: the ID for your organization in GDC.



## View the MHS metrics dashboard

In this dashboard, you can gain valuable insights for your Harbor instances, such as the following:

  * The number of Harbor vulnerability scans performed.
  * The amount of object storage capacity used.
  * The number of Harbor projects.



Use the **Harbor Vulnerability Scans** panel to view the number of vulnerability scans you are performing for your Harbor instances.

Use the **Object Storage Used Capacity** panel to view storage consumption metrics and measure the amount of object storage resources you are using.

Use the **Harbor Projects** panel to view the count of all Harbor projects in the Harbor instance.

![View the metrics dashboard for Harbor storage usage and vulnerability.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/haas-metrics-dashboard.png)

**Figure 1.** Use the MHS dashboard in Grafana to view metrics for Harbor vulnerability scans, storage consumption, and project counts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
