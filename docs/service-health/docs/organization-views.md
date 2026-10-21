---
url: https://docs.cloud.google.com/service-health/docs/organization-views/
title: View organization incidents in the Google Cloud console \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:09.261793+00:00
---

# View organization incidents in the Google Cloud console  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/organization-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  View organization incidents in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Personalized Service Health to monitor Google Cloud service health [incidents](https://docs.cloud.google.com/service-health/docs/concepts#incident) across your organization. To learn how to programmatically access organization-level [events](https://docs.cloud.google.com/service-health/docs/concepts#service_health_event), see [Manage organization events with the Service Health API](https://docs.cloud.google.com/service-health/docs/organization-events).

## Overview

Personalized Service Health helps you monitor active disruptions impacting Google Cloud products and services. While you can view incidents on a project-by-project basis, you may find an organization-level view useful for broader insights.

With an organization-level view in Service Health, you can:

  * **Get a consolidated view of incidents.** See all unique incidents impacting one or more projects across your entire organization in a single dashboard.
  * **Assess impact faster.** Quickly understand which Google Cloud services are affected and gain a sense of the scope of impact across projects in your organization.
  * **Improve operational efficiency.** Avoid checking for incidents project-by-project during widespread service disruptions and focus your response efforts.



## Before you begin

To view incidents for an organization in Service Health:

  1. **Enable the Personalized Service Health API.** You must enable the Service Health API _per project_ for each project you want to include in the organization-level aggregated view. Enable the API for all relevant projects within your organization. For more information, refer to [Manage events affecting your organization: Before you begin](https://docs.cloud.google.com/service-health/docs/organization-events#before_you_begin).

  2. **Grant the required Identity and Access Management (IAM) permissions.** Accessing the Service Health Aggregated Views dashboard requires specific IAM permissions: `servicehealth.organizationEvents.list` and `servicehealth.organizationImpacts.list`. These permissions ensure only authorized users can view organization-level service health information. For more information, refer to [Manage Personalized Service Health access](https://docs.cloud.google.com/service-health/docs/manage-access).




## View incidents for an organization in the Google Cloud console

To view incidents for an organization in the Google Cloud console, follow these steps:

  1. Select your organization in the Google Cloud console:

     1. In the Google Cloud console, click the **Project selector** at the top of the page.
     2. In the **Select from** dialog, select your organization from the list.
     3. Click **Open**.
  2. Click the **Service Health** section. The organization-level view displays incidents relevant to your entire organization.

Within this view, you can:

     * **Review the incident list.** The main view displays a filterable list of unique incidents. Each incident in this list has impacted at least one project within your selected organization.
     * **Review incident details.** Click an individual incident in the list to view its summary details. The summary card provides key information, including:

       * A description of the incident.
       * Granular disruption status (**Affected** or **Resolved**) and recovery timestamps for each impacted product and location.
       * The number of projects within your organization that are impacted.
       * The number of projects within your organization that are potentially at risk.
     * **View impacted projects.** Within the incident details, go to the **Impact** tab or click the **View** button associated with impacted projects. This section lists all projects within your organization that are affected by this specific incident. The list of impacted projects is filterable and sortable by columns such as Project ID, Project Number, and Relevance.

     * **Examine project details.** To view more detailed information about how a specific project is affected by an incident, click the individual project listed in the **Impact** tab. This opens the standard Service Health view for that project, which provides project-specific incident information.




## Use the Service Health API

You can programmatically access organization-level incident data through the Service Health Organization API. This lets you integrate service health information into your automated workflows and dashboards.

For detailed information and examples on how to query organization-level events, see the [Service Health Organization Events documentation](https://docs.cloud.google.com/service-health/docs/organization-events).

## What's next

  * Learn more about [Service Health](https://docs.cloud.google.com/service-health/docs/overview).
  * Explore the [Service Health API documentation](https://docs.cloud.google.com/service-health/docs/organization-events).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
