---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/upgrade/upgrade-api-overview/
title: Overview of Upgrade API \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:32.191594+00:00
---

# Overview of Upgrade API  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/upgrade/upgrade-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Overview of Upgrade API Stay organized with collections  Save and categorize content based on your preferences. 

The Upgrade API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM). It manages the schedule for tenant organization upgrades.

To use the Upgrade API, we recommend that you use the GDC console or `kubectl` CLI. If your application needs to use your own libraries to call this API, use the following example and the [full API definition](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/upgrade/v1/upgrade-v1) to build your requests.

## Service endpoint and discovery document

The API endpoint for the Upgrade API is `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/upgrade.gdc.goog/v1`, where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.

Using the `kubectl proxy` command, you can access that URL in your browser or with a tool such as `curl` to get the discovery document for the Upgrade API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. After that command is running, you can access the document at the following URL: `http://127.0.0.1:8001/apis/upgrade.gdc.goog/v1`.

## Example upgrade MaintenanceWindow resource

You can interact with maintenance windows using the GDC console and `kubectl` CLI in GDC. There are two maintenance windows, one for patch upgrades and the other for minor upgrades.

The following is an example of a `MaintenanceWindow` object configured to define a maintenance window for GDC minor upgrades:
    
    
    apiVersion: upgrade.gdc.goog/v1
    kind: MaintenanceWindow
    metadata:
      name: minor-upgrade
      namespace: gpc-system
    spec:
      recurrence: FREQ=MONTHLY;BYSETPOS=1;BYDAY=SU
      timeWindow:
        end: "2022-04-03T06:00:00Z"
        start: "2022-04-03T00:00:00Z"
      upgradeType: MinorUpgrade
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
