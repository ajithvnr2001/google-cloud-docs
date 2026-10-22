---
url: https://docs.cloud.google.com/architecture/infra-reliability-guide/manage-and-monitor/
title: Manage and monitor your Google Cloud infrastructure \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:54.528200+00:00
---

# Manage and monitor your Google Cloud infrastructure  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/infra-reliability-guide/manage-and-monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Manage and monitor your Google Cloud infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-23 UTC

After you deploy an application to production in Google Cloud, you might need to modify the infrastructure that it uses. For example, you might need to change the machine types of your VMs or change the storage class of the Cloud Storage buckets. This part of the [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide) summarizes change-management guidelines that you can follow to reduce the reliability risk of the infrastructure resources. This part also describes how you can monitor the availability of Google Cloud infrastructure.

## Deploy infrastructure changes progressively

When you need to change your Google Cloud infrastructure, as much as possible, deploy the changes to production progressively. For example, if you need to change the machine types of the VMs, deploy the changes to a few VMs in one zone, and monitor the effects of the changes. If you observe any issues, revert the infrastructure quickly to the previous stable state. Diagnose and resolve the issues, and then restart the progressive deployment process. After verifying that your workload runs as expected, gradually deploy the changes across all of your infrastructure.

## Control changes to global resources

When you modify global resources such as Virtual Private Cloud (VPC) networks and global load balancers, take extra care to verify the changes before deploying them to production.

Because global resources are resilient to zone and [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) outages, you might decide to use single instances of certain global resources in your architecture. In such deployments, the global resources can become single points of failure. For example, if you inadvertently misconfigure a forwarding rule of your global load balancer, the frontend can stop receiving or processing user requests. Effectively, the application is unavailable to users in this case though the backend is intact. To avoid such situations, exercise rigorous control over changes to global resources. For example, in your change-review process, you can classify any modifications to global resources as high-risk changes that additional reviewers must verify and approve.

## Monitor availability of Google Cloud infrastructure

You can monitor the current status of the Google Cloud services across all the regions by using the [Google Cloud Service Health Dashboard](https://status.cloud.google.com/). You can also view a [history](https://status.cloud.google.com/summary) of the infrastructure failures (called _incidents_) for each service. The history page provides the details of each incident, such as the incident duration, affected zones and regions, affected services, and any recommended workarounds.

You can also view incidents relevant to your project using [Personalized Service Health](https://console.cloud.google.com/servicehealth/incidents). Service Health also lets you request incident information using an API on a per-project or per-organization basis and lets you configure alerts.

Google provides regular updates about the status of each incident, including an estimated time for the next update. You can programmatically get status updates for incidents by using an RSS feed. For more information, see [Use Google Cloud Service Health as a fallback](https://docs.cloud.google.com/service-health/docs/service-health-fallback).

**Note:** Even when there's no infrastructure outage, your application might be unavailable due to errors in the application or configuration issues. For example, a software update might have caused the application servers to crash, or an administrator might have inadvertently deleted the load balancer forwarding rules. For help with troubleshooting issues with specific Google Cloud resources, see the documentation for the appropriate service.

[ Previous arrow_back  Manage traffic and load  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load)

[ Next What's next  arrow_forward  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/whats-next)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
