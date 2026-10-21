---
url: https://docs.cloud.google.com/support/docs/peak-events/secure-capacity/
title: Secure capacity for your event \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:33.990197+00:00
---

# Secure capacity for your event  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/peak-events/secure-capacity/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Secure capacity for your event Stay organized with collections  Save and categorize content based on your preferences. 

A critical component of event readiness is capacity planning, where you determine the amount of cloud resources needed to ensure your workloads have what they need to operate effectively, without over provisioning and paying unnecessarily for what you don't need.

Capacity is the total amount of a particular resource that's available, shared across all customers. However, to ensure that a few customers or projects can't monopolize resources, Google Cloud restricts how much of a particular shared Google Cloud resource that you can use with [quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

Each quota represents a specific resource, such as API calls to a particular service, the number of VMs used by your project at a given time, the number of load balancers used concurrently by your project, or the number of projects that you can create.

While many services have default quotas for some resources, the quotas that apply to your applications are specific to you, your project, or your organization. [Enabling billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project) for your project increases quotas for most services. Quotas can also increase as your use of Google Cloud expands over time.

As you're preparing for your high traffic event or peak season, you need to **ensure that your quotas match your resource requirements so that you don't encounter unexpected failures**.

We recommend that you do the following:

  * Use [Cloud Monitoring tools](https://docs.cloud.google.com/monitoring) to get visibility into your application usage and capacity, and the overall health of your applications and infrastructure.

  * Evaluate the average and peak utilizations of your top cloud workloads, and their current and future capacity needs, to determine how much over-provisioning is needed to prepare for traffic spikes.

  * Run load tests to determine how much load the system can handle while meeting its latency targets, given a fixed amount of resources.




## Use Capacity Planner

**Private preview**

Capacity Planner is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you don't have access to Capacity Planner, [contact your account team](https://cloud.google.com/contact), and request a capacity planning session.

Capacity Planner lets you view historical and forecasted usage of your virtual machine (VM) instances, Persistent Disk volumes, and GPUs. You can also view reservations, reserve resources in advance, and manage your project's quota limits by seeing how close you are to your limit, and setting up automatic quota increase requests. For more information, see [View usage and forecast data in Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/view-data).

## Enable the quota adjuster

The quota adjuster monitors your resource consumption and proactively submits quota adjustment requests on your behalf so that you don't have to make manual requests. For more information, see [How the quota adjuster works](https://docs.cloud.google.com/docs/quotas/quota-adjuster#how-the-quota-adjuster-works).

## Request a quota adjustment

If your quotas aren't sufficient for what you need, you can request a quota adjustment. There are three primary ways to submit a quota increase request:

  * Through the Google Cloud console
  * Through a support case
  * Directly with your account team or TAM



If you need a quota increase request addressed quickly, you should consider using the Google Cloud console. However, if the request requires more analysis, you might need to work with your account team.

To adjust a quota value through the Google Cloud console, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

Most quota increase requests are evaluated by automated systems. Their decision is based on criteria including the availability of resources, the length of time you've used Google Cloud, and other factors. Requests that don't meet the criteria are denied. If your request is denied, you can try requesting the quota increase by [creating a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures), or by contacting your account team or TAM.

## Create a reservation

Reservations help ensure that you have the Compute Engine resources available to create VMs with the same hardware (memory and vCPUs) and optional resources (GPUs and Local SSD disks) whenever you need them.

An _on-demand reservation_ is provisioned at the time you request it, if the requested capacity is available. A _future reservation_ lets you request capacity in advance and provides you with a high level of assurance in obtaining and securing capacity for peak scale events. We recommend that you procure future reservations well in advance of your event. For more information, see the following:

  * [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview)
  * [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project)
  * [Create future reservation requests for a single project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations)



## What's next

  * [Prepare to resolve issues during your event](https://docs.cloud.google.com/support/docs/peak-events/issue-resolution)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
