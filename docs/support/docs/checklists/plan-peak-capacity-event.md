---
url: https://docs.cloud.google.com/support/docs/checklists/plan-peak-capacity-event/
title: Prepare for a peak capacity event \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:09.853360+00:00
---

# Prepare for a peak capacity event  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/checklists/plan-peak-capacity-event/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Prepare for a peak capacity event Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to prepare for peak capacity events and high traffic so that you can deliver your services with minimal to no downtime, and with no degrading of performance or user experience.

When managing events in the cloud, there are three key phases:

  1. **Preparation** : complete activities and tasks to prepare for your event, including an architecture review, capacity planning, and creating reservations.
  2. **Execution** : when your event begins, closely monitor it and react accordingly.
  3. **Analysis** : after your event is completed, analyze what went well, what didn't, and how to improve future events.



This guide focuses on the _preparation_ phase.

## Checklist

Learn how to prepare for a peak capacity event by completing the following tasks:

  1. Create an event request
  2. Understand event management best practices
  3. Review service limits and quota recommendations
  4. Set up Unified Maintenance
  5. Request and secure the appropriate capacity for your event
  6. Prepare for rapid issue resolution during your event
  7. Manage and optimize your cloud resources
  8. Schedule and conduct load testing
  9. Schedule and conduct disaster recovery testing



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=support--plan-peak-capacity-event)

* * *

## Before you begin

Depending on the Customer Care support package that you have purchased, make sure that you understand the event readiness services available to you:

  * **Enhanced Support** : you can optimize readiness for your events, launches, and migrations by using [Planned Event Support](https://docs.cloud.google.com/support/docs/enhanced#pes) which is a Value-Add Service that provides coverage for critical phases of high-traffic short-term digital events like grand openings, new product launches, or data migrations.

**Note:** The Planned Event Support requests require a lead time of 60 days.
  * **Premium Support** : you can use the [Event Management Service](https://docs.cloud.google.com/support/docs/premium#event_management) for planned peak events, such as a product launch or major sales event. With this service, Customer Care and your account team guides you through the following:

    * Preparing your systems for key moments and heavy workloads
    * Running load tests and disaster tests to proactively resolve potential issues
    * Engaging with Customer Care in the event of any issues that might occur
    * Reviewing the outcomes of your event and making recommendations for future events.
**Note:** The Event Management Service requests require a lead time of 30 days.



## Create an event request

Premium Support customers can create event requests as a part of the [Event Management Service](https://docs.cloud.google.com/support/docs/premium#event_management). To engage with Customer Care team for your event, [create an event request](https://docs.cloud.google.com/support/docs/peak-events/create-manage-event-requests).

## Understand event management best practices

You should understand and follow certain event management best practices:

  1. **Detail your event planning process** : while in the preparation phase for a peak capacity event, you should engage with your account team to help you review the details and activities associated with your event and understand the overall impact on your projects.

  2. **Monitor and react during execution** : when your peak season or launch event begins, you'll need to closely monitor activity and react as needed. If any issues occur, a well-defined incident management and escalation process is key to reducing the effort and time it takes to address and resolve the issue.

  3. **Review and document your analysis** : when your peak season or launch event is over, review and analyze the event, and document the lessons learned so that you can apply them to your next major event.




For more information, see [Event management best practices](https://docs.cloud.google.com/support/docs/peak-events/best-practices).

## Review service limits and quota recommendations

The _service limit recommender_ lets you proactively monitor your project quotas to avoid hitting limits during peak traffic. It analyzes your quota utilization over the last 30 days and automatically provides recommendations and insights when usage approaches 80% of a limit.

Regularly reviewing these recommendations can help you identify and address potential quota bottlenecks before they impact your service's availability and performance. This also lets you to request quota adjustments ahead of time, ensuring a smooth experience during your peak event.

To learn how to enable service limit quota recommendations, see [Service limit (quota) recommender](https://docs.cloud.google.com/recommender/docs/service-limit-quota-recommender).

## Set up Unified Maintenance

Unified Maintenance centralizes planned maintenance management across Google Cloud services. By integrating with Cloud Logging, it provides notifications to help you prepare for scheduled changes and protect your workflows. For more information, see [Unified Maintenance overview](https://docs.cloud.google.com/unified-maintenance/docs/overview).

To learn how to set up Unified Maintenance, see [Set up Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/set-up-unified-maintenance).

## Request and secure the appropriate capacity for your event

A critical component of the preparation phase is capacity planning, where you determine the amount of cloud resources needed to ensure your workloads have what they need to operate effectively. As you're preparing for your high traffic event or peak season, make sure that your quotas match your resource requirements so that you don't encounter unexpected failures. For more information, see [Secure capacity for your event](https://docs.cloud.google.com/support/docs/peak-events/secure-capacity).

### Use Capacity Planner

**Private preview**

Capacity Planner is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you don't have access to Capacity Planner, [contact your account team](https://cloud.google.com/contact), and request a capacity planning session.

Capacity Planner lets you view historical and forecasted usage of your virtual machine (VM) instances, Persistent Disk volumes, and GPUs. You can also view reservations, reserve resources in advance, manage your project's quota limits, and set up automatic quota increase requests. For more information, see [View usage and forecast data in Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/view-data).

  1. In the Google Cloud console, go to the **Capacity Planner** page.

[Go to Capacity Planner](https://console.cloud.google.com/capacity/usage)

  2. Using the resource selector on the console toolbar, select a project, folder, or organization.

  3. Select the type of Compute Engine resource you want to view usage data for:

     * To view your VMs' usage data, click the **Virtual machine** tab, if it isn't already selected.

     * To view your Persistent Disk volumes' usage data, click the **Disk** tab.

     * To view your GPUs' usage data, click the **GPU** tab.

  4. You can filter elements to see different data visualizations for the usage and forecast data of the resource.




### Enable the quota adjuster

The quota adjuster monitors your resource consumption and proactively submits quota adjustment requests on your behalf so that you don't have to make manual requests. For more information, see [How the quota adjuster works](https://docs.cloud.google.com/docs/quotas/quota-adjuster#how-the-quota-adjuster-works).

  1. In the Google Cloud console, go to the **IAM & Admin** > **Quotas and system limits** page.

[Go to Quotas and system limits](https://console.cloud.google.com/iam-admin/quotas)

  2. Click the **Configurations** tab.

  3. To turn on the quota adjuster, click the **Enable** toggle to the on position.




When the **Status** column reads **Enabled** , the quota adjuster monitors your usage and issues quota adjustment requests when resource use approaches its quota value.

### Request a quota adjustment

If your quotas aren't sufficient for what you need, you can request a quota adjustment. For more information, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

  1. In the Google Cloud console, go to the **IAM & Admin** > **Quotas and system limits** page.

[Go to Quotas and system limits](https://console.cloud.google.com/iam-admin/quotas)

  2. Select the checkbox next to the quota that you want to update.

Optionally, to search for a quota, use the filter_list **Filter**.

  3. Click create **Edit** and the **Quota changes** pane appears.

  4. In the **New value** field, enter the quota value that you want. Some quota values have a unit of measurement; if this applies, select the unit that you want in the adjacent list.

  5. If you see a message indicating that you will remove the [quota override](https://docs.cloud.google.com/docs/quotas/view-manage#create_override) by requesting a quota greater than the override, select the checkbox to proceed, and then select **Apply for higher quota**.

  6. In the **Request description** field, enter a description, and then click **Done**.

  7. Click **Next** and provide your contact details.

  8. Click **Submit request**.




If your request is denied, you can try requesting the quota increase by [creating a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures), or by contacting your account team.

### Create a reservation

Reservations help ensure that you have the Compute Engine resources available to create VMs with the same hardware (memory and vCPUs) and optional resources (GPUs and Local SSD disks) whenever you need them.

An _on-demand reservation_ is provisioned at the time you request it, if the requested capacity is available. A _future reservation_ lets you request capacity in advance. We recommend that you procure future reservations well in advance of your event. For more information, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

#### Create a single-project on-demand reservation

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. On the **On-demand reservations** tab (default), click add_box **Create reservation**.

The **Create a reservation** page opens.

  3. Enter a **Name** for your reservation.

  4. Select a **Region** and **Zone** where you want to reserve resources.

  5. For the **Share type** , select **Local** if it isn't already selected.

  6. To allow a reservation of GPU VMs to be consumed by Vertex AI [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations), in the **Google Cloud services** section, select **Share reservation**.

  7. Select a **Use with VM instance** option:

     * To allow matching VMs to automatically consume this reservation, select **Use reservation automatically** if it isn't already selected.

     * To consume this reservation's resources only when creating matching VMs that specifically target this reservation by name, select **Select specific reservation**.

**Note:** If your instance template specifies an A3 machine type or a compact placement policy, then you must select **Select specific reservation**. Otherwise, you encounter errors.
  8. Enter the **Number of VM instances** that you want to reserve.

  9. In the **Machine configuration** section, do the following:

     1. To specify the properties of your VMs from an existing [instance template](https://docs.cloud.google.com/compute/docs/instance-templates), select **Use instance template**.

     2. Specify an **Instance Template**. If you select a regional template, you can only reserve resources in that region.

  10. To automatically delete the reservation at a specified time, select the **Enable auto-delete** checkbox. Automatically deleting reservations can be useful to avoid unnecessary charges when you stop consuming the reservation.

  11. To create the reservation, click **Create**.

The **Reservations** page opens. It might take up to a minute to create the reservation.




#### Create a single-project future reservation

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Click add_box **Create future reservation**. The **Create a future reservation** page appears.

  4. In the **Configurations** section, do the following: 

     1. Select **Use instance template**.

     2. In **Instance template** list, select the instance template. If you select a regional instance template, then you can only reserve resources within the same region as the template's region.

  5. In the **Location** section, in the **Region** and **Zone** lists, select the region and zone in which to reserve resources.

  6. In the **Capacity details** section, in the **Total capacity needed** , enter the [total count of VMs](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) that you want to reserve.

**Important:** Verify that you have sufficient quota for the resources that you want to reserve, both when you submit your request and at the request's start time. Otherwise, Google Cloud might decline your future reservation request or deliver only part of the requested resources.
  7. In the **Reservation period** section, do the following:

     1. In the **Start time** field, specify a start time for the reservation period. The start time can't be later than one year from when you submit your future reservation request for review. To have sufficient time to optionally modify, cancel, or delete the future reservation before it enters its lock time, specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

     2. In the **End time** field, specify an end time for the reservation period. In the **Duration summary** section, you can see the length of the reservation period. To increase the likelihood that Google Cloud approves your future reservation request after you submit it, we recommend that you specify a reservation period of at least 365 days.

  8. Click **Next**.

  9. In the **Auto-delete** section, do one of the following:

     * To enable Compute Engine to automatically delete the auto-created reservations for your future reservation request, do the following:

**Caution:** If you enable the auto-delete option, then Compute Engine deletes all the auto-created reservations at the specified deletion time, whether the reservations are fully consumed or not.
       1. Select the **Enable auto-delete** checkbox.

       2. Optional: In the **Auto-delete time** field, enter a date and time when to delete the auto-created reservations. The date and time must be after the end time of the reservation period. If you leave this field empty, then Compute Engine deletes the auto-created reservations within two hours after the reservation period's end time.

     * To disable automatic deletion, clear the **Enable auto-delete** checkbox.

  10. In the **Use with VM instance** section, select one of the following options:

     * To let matching VMs automatically consume the auto-created reservations, select **Use reservation automatically**.

     * To consume the auto-created reservations only when you create matching VMs that specifically target the reservations, select **Select specific reservation**.

  11. Click **Next**.

  12. In the **Future reservation name** field, enter a name for your future reservation request.

  13. In the **Prefix** field, enter a name prefix. All auto-created reservations for this future reservation request use this prefix.

  14. To finish creating the draft future reservation request, click **Save a draft**. The **Reservations** page appears. Creating the future reservation request can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).




## Prepare for rapid issue resolution during your event

How you respond to, categorize, and solve incidents of differing severity can significantly affect your operations during an event. Make sure to use a centralized incident management system for effective tracking throughout the incident lifecycle.

In addition to reviewing your contacts and enabling Personalized Service Health, you should do the following:

  * Review [best practices for working with Customer Care](https://docs.cloud.google.com/support/docs/best-practices)
  * Create a communication plan
  * Ensure that you have access to relevant resources, including ability to create support cases, troubleshoot issues, and access your disaster recovery environment.



For more information, see [Prepare to resolve issues during your event](https://docs.cloud.google.com/support/docs/peak-events/issue-resolution).

### Review your contacts

Many Google Cloud offerings send out notifications to share important information with Google Cloud users. By default, these notifications are sent to members with certain Identity and Access Management (IAM) roles. With Essential Contacts, you can customize who receives notifications by providing your own list of contacts. For more information, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

  1. In the Google Cloud console, go to the **IAM & Admin** > **Essential Contacts** page.

[Go to Essential Contacts](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Make sure the name of your project, folder, or organization appears in the resource selector on the console toolbar. The resource selector tells you what project, folder, or organization you are managing contacts for.

  3. To list the contacts by category, select **Category**. To list the contacts alphabetically, select **Contacts**.

**Note:** When you view contacts for an organization or folder, you don't see contacts for its child resources. If you are viewing contacts for a child resource (folder or project) that inherits contacts from its ancestors (organizations or other folders), you see the inherited contacts for any ancestors that you have permission to view contacts for.



### Enable Personalized Service Health

Personalized Service Health lets you identify Google Cloud service disruptions relevant to your projects so that you can manage and respond to them efficiently. For more information, see the [Personalized Service Health overview](https://docs.cloud.google.com/service-health/docs/overview).

Make sure that you have enabled the Service Health API ahead of your event and that your organization can access the dashboard and configure alerts. For more information, see [Manage Personalized Service Health access](https://docs.cloud.google.com/service-health/docs/manage-access).

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.  


[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Service Health API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicehealth.googleapis.com)




## Manage and optimize your cloud resources

Manage and optimize the resources that are used by your Google Cloud workloads. This involves right-sizing resources based on actual usage and demand, using auto scaling for dynamic resource allocation, and reviewing architecture and security recommendations.

In addition to reviewing Active Assist recommendations, you should do the following:

  * Review [Google Cloud best practices](https://docs.cloud.google.com/support/docs/peak-events/optimize-resources#best-practices)
  * [Review scalability](https://docs.cloud.google.com/support/docs/peak-events/optimize-resources#scalability)
  * Review your product versions
  * Review alerts and dashboards



For more information, see [Optimize your cloud resources](https://docs.cloud.google.com/support/docs/peak-events/optimize-resources).

### Review Active Assist recommendations

Active Assist refers to the portfolio of tools used in Google Cloud to generate recommendations and insights to help you optimize your Google Cloud projects. For more information, see [What is Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist).

  1. In the Google Cloud console, go to the **Active Assist**.

[Go to Active Assist](https://console.cloud.google.com/active-assist/dashboard)

  2. Using the resource selector on the console toolbar, select a Google Cloud project, folder, or organization.

You can only see recommendations at an organization or folder level if you have permissions for that organization or folder, regardless of your permissions for folders or projects within it.

  3. In the navigation pane, click **All recommendations**.

Recommendations that you can filter, sort, and share are displayed. You can explore recommendations in detail, see what resources are affected, and what impact applying a recommendation might have.

  4. To learn more about a recommendation, in the **Recommendation** column, click a recommendation.

Relevant data that might help you decide whether to apply or dismiss the recommendation is displayed.

  5. If you have the permission to, you can apply or dismiss a recommendation by clicking the applicable button.

Note that some recommendations might not be directly applicable. Follow the instructions detailed in the console to apply them.




## Schedule and conduct load testing

Load testing can determine whether your system will scale successfully during production use, and find any bottlenecks that prevent it from scaling.

  1. **Three to five months before your event** , you should perform load testing on critical projects and workloads to simulate peak traffic.

  2. Investigate the quota and cost implications of the load tests and consider creating [Cloud Billing budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) that will monitor the expense of the services that you are going to stress the most.

  3. After each test, evaluate the results and use Capacity Planner to visualize your usage and forecast data, and request quota increases as necessary. In this document, see Use Capacity Planner and Request a quota adjustment.




If you require assistance, contact your account team. Your account team can help discuss architectural best practices to improve the overall reliability and availability of your services based on the results of your load testing.

## Schedule and conduct disaster recovery testing

If you have a robust and well-tested disaster recovery (DR) strategy, you can minimize the impact of disruptions, achieve faster recovery times, and resume core operations more rapidly when things go wrong.

Your DR strategy should include detailed emergency response requirements, backup operations, and recovery procedures.

  1. **One to three months before your event** , make sure to run through simulations of disaster scenarios to identify any gaps in your DR plans and readiness.

  2. After each test, evaluate the results to determine if any architectural changes are required. Review and optimize resources as needed. In this document, see Manage and optimize your cloud resources.




If you require assistance, contact your account team. They can help discuss best practices for disaster recovery and incident response processes.

For more information about disaster recovery, see [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

## Summary of resources

The following table lists the guides that are referred to in this document.

Create an event request  
---  
  
  * [Create an event request](https://docs.cloud.google.com/support/docs/peak-events/create-manage-event-requests)

  
Understand event management best practices  
  
  * [Event management best practices](https://docs.cloud.google.com/support/docs/peak-events/best-practices)

  
Review service limits and quota recommendations  
  
  * [Review service limits and quota recommendations](https://docs.cloud.google.com/recommender/docs/service-limit-quota-recommender)

  
Set up Unified Maintenance  
  
  * [Set up Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/set-up-unified-maintenance)

  
Request and secure the appropriate capacity for your event  
  
  * [About future reservation requests](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview)
  * [Create and manage support cases](https://docs.cloud.google.com/support/docs/customer-care-procedures)
  * [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates)
  * [Quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster)
  * [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview)
  * [Secure capacity for your event](https://docs.cloud.google.com/support/docs/peak-events/secure-capacity)
  * [Use reservations with prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations)
  * [Use reservations with training](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations)
  * [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage)
  * [View usage and forecast data in Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/view-data)

  
Prepare for rapid issue resolution during your event  
  
  * [Manage Personalized Service Health access](https://docs.cloud.google.com/service-health/docs/manage-access)
  * [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts)
  * [Personalized Service Health overview](https://docs.cloud.google.com/service-health/docs/overview)
  * [Prepare to resolve issues during your event](https://docs.cloud.google.com/support/docs/peak-events/issue-resolution)

  
Manage and optimize your cloud resources  
  
  * [Optimize your cloud resources](https://docs.cloud.google.com/support/docs/peak-events/optimize-resources)
  * [What is Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)

  
Schedule and conduct load testing  
  
  * [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)

  
Schedule and conduct disaster recovery testing  
  
  * [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)

  
  
## What's next

  * [Best practices for working with Customer Care](https://docs.cloud.google.com/support/docs/best-practices)
  * [Best practices for working with Premium Support](https://docs.cloud.google.com/support/docs/premium-best-practices)
  * [Language support and working hours](https://docs.cloud.google.com/support/docs/language-working-hours)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
