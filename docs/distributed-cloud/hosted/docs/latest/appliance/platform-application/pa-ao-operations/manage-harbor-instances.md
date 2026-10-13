---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/manage-harbor-instances/
title: Manage Harbor registry instances \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:10.127482+00:00
---

# Manage Harbor registry instances  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/manage-harbor-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage Harbor registry instances Stay organized with collections  Save and categorize content based on your preferences. 

This page details how to manage your created Harbor registry instances. View your created Harbor registry instances using the Google Distributed Cloud (GDC) air-gapped appliance console or the GDCgdcloud CLI. 

## Before you begin

To view the Harbor registry instances, you must have the necessary identity and access roles:

  * Harbor Instance Viewer: required to view Harbor instances. Ask your Organization IAM Admin to grant you the Harbor Instance Viewer (`harbor-instance-viewer`) role.



## View Harbor registry instances

View the pre-configured Harbor registry instances in the GDC console or use the GDC gdcloud CLI.

###  Console 

  1. Navigate to the **Harbor Container Registry** page in the **CI/CD** section.
  2. View the list of created Harbor instances in the **Instances** section.
  3. For more detail about a specific instance, click the **Go to Harbor Instance** external link.



###  gdcloud 

View the Harbor registry instance:
    
    
    gdcloud harbor instances describe INSTANCE \
      --project=PROJECT
    

Replace the following:

  * `INSTANCE`: the name of the instance.
  * `PROJECT`: the name of the project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
