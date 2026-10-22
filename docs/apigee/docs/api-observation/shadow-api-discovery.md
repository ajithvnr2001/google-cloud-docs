---
url: https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery/
title: Shadow API Discovery overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:50.271574+00:00
---

# Shadow API Discovery overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Shadow API Discovery overview Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

**Preview — Shadow API Discovery**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Shadow API Discovery finds shadow APIs (also known as undocumented APIs) in your existing cloud infrastructure. Shadow APIs pose a security risk to your system, since they might be unsecured, unmonitored, and unmaintained. Shadow API Discovery is part of [API Observation in Apigee](https://docs.cloud.google.com/apigee/docs/api-observation).

You can configure and run jobs to observe API activity in individual Google Cloud projects. Within your centralized [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) instance, you can attach those projects to view the results of those jobs and automatically compare them to "known" APIs documented in API hub. For information on using Shadow API Discovery in Apigee API hub, see [API observations in API hub](https://docs.cloud.google.com/apigee/docs/apihub/api-observation-overview).

For information on data residency compatibility for Shadow API Discovery, see [ Data residency compatibility](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-compatibility).

## Enable Shadow API Discovery

Shadow API Discovery is part of the Advanced API Security add-on and is available for Google Cloud projects with or without Apigee provisioning.

**If your Google Cloud project is provisioned for Apigee** :

  * For subscription customers, it's available with the Apigee organization. See [ Manage Advanced API Security for Subscription organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-subscription-organizations)
  * Pay-as-you-go customers must enable the add-on for at least one environment. See [ Manage Advanced API Security for Pay-as-you-go organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-pay-as-you-go-organizations)
  * Shadow API Discovery is not available for Apigee eval environments.



**If your Google Cloud project is _not_ provisioned for Apigee,** you can add Shadow API Discovery to your project by contacting [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html).

**Important:** Active Shadow API Discovery jobs also incur costs based on the volume of monitored traffic. See the "Using a Private Service Connect backend (load balancer) to access a published service" section of [Private Service Connect forwarding rules](https://cloud.google.com/vpc/pricing#psc-forwarding-rules) for information on costs. To eliminate these costs, disable the Shadow API Discovery job or jobs. 

### Enable Shadow API Discovery from Apigee

Instructions in this section for setting up and viewing the results of API observations are based on the Apigee UI in Cloud console. You can also use the Apigee Management (APIM) APIs to manage Shadow API Discovery. See [Shadow API discovery management APIs](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery-apis).

To use this feature, you must enable the add-on. If you are a Subscription customer, you can enable the add-on for your organization. See [ Manage Advanced API Security for Subscription organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-subscription-organizations) for more details. If you are a Pay-as-you-go customer, you can enable the add-on in your eligible environments. For more information, see [ Manage the Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-security-add-on).

### Enable Shadow API Discovery from API hub

To enable Shadow API Discovery from API hub, follow the instructions in [Configure API Observation in API hub](https://docs.cloud.google.com/apigee/docs/apihub/configure-api-observation). 

## Required roles and permissions for Shadow API Discovery

The table below shows the required roles to perform tasks related to Shadow API Discovery.

Task | Required Role(s)  
---|---  
Enable or disable Advanced API Security | [Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (roles/apigee.admin)  
Create observation sources and jobs | [ API Management Admin](https://cloud.google.com/iam/docs/roles-permissions/apim#apim.admin) (roles/apim.admin)  
View observations | [ API Management Viewer](https://cloud.google.com/iam/docs/roles-permissions/apim#apim.viewer) (roles/apim.viewer)  
  
## Access Shadow API Discovery in the Apigee UI

This section describes how to access Shadow API Discovery in the Apigee UI. 

To access Shadow API Discovery in the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > API Observation > Shadow API** page.

[Go to Shadow API](https://console.cloud.google.com/apigee/apiObservation/shadowApi)

  2. The main page shows any API observations that were already generated. Select the **API Observations** and **Observation Jobs** tabs to switch between viewing results and creating observation jobs.



### Create observation jobs

Observation jobs provide the instructions Shadow API Discovery needs to look for shadow APIs. Follow these steps to create an observation job. Be aware of the Behaviors and limitations that apply to observation job creation.

  1. Select the **Observation jobs** tab and then click **Create observation job**.
  2. Select one or more **Observation sources(s)** , or click **Create observation source** at the bottom of the **Observation source(s)** list to create new source locations if needed. Note that the observation source creation process might take several minutes.  
  
Observation sources include:  
**Source name:** A name you specify to identify the source.  
**Location:** A [location](https://cloud.google.com/docs/geography-and-regions) to observe in. Including more source regions allows a broader view of APIs across your infrastructure. See Best practices. Only one observation source can be created in a location.  
**Network** and **Subnetwork:** The VPC network and subnetwork. The network and subnetwork must be in the same project as the observation source. The subnetwork must also be in the same region as the observation source location. 
  3. **Create observation job**. Provide an observation job name, which must be unique per location. Select a location, which specifies where data aggregation and processing will occur. All data collected in the source regions is processed in and accessed from this region, consistent with [Google's Data Residency policies](https://cloud.google.com/assured-workloads/docs/data-residency). Creating a new observation job may take a few minutes to complete.
  4. **Enable observation job (Optional)**. You can enable the job when you create it, in which case it starts observing immediately. If you do not enable the job immediately, you can enable the observation job later from the observation job list.



#### Enable, disable, and delete observation jobs

To change whether an existing observation job is enabled (active), select either **Enable** or **Disable** from the **Actions** menu in the row for that job in the **Observation jobs** page.

To delete an existing observation job, select **Delete** from the **Actions** menu for that job. Deleting a job also removes the observation results associated with the job, so if you'd like to preserve the results while stopping the job from continuing, disable it rather than deleting it. Active jobs cannot be deleted; disable active jobs first if you need to delete them.

**Note:** You can't edit an observation job at this time. See Behaviors and limitations.

### View API Observations

To view API Observations for enabled observation jobs, choose the **API Observations** tab and then select the **Observation job** from the list.

**Note:** Observation jobs do not generate results immediately and are subject to limitations. See Behaviors and limitations for details.![API Observations page](https://docs.cloud.google.com/static/apigee/docs/api-observation/images/shadow_api_observations_list1.png)

The observations list shows these values:

  * **Hostname:** The API hostname. Click the hostname to view the observation details.
  * **API operations:** The number of API operations (such as GET or PUT requests) observed. 
  * **Server IPs:** IPs of servers hosting the discovered APIs.
  * **Source locations:** The source location(s) where traffic was observed.
  * **Last event detected (UTC):** The date and time when the most recent request to the API was detected.
  * **Tags:** A list of the tags you or someone else created to label this observation. See Use tags for more information.
  * **Actions:** Additional actions available for each observation.



#### View observation details

After clicking the hostname on the observations list, you'll see the observation details page.  
  
![Shadow API Discovery observation job detail](https://docs.cloud.google.com/static/apigee/docs/api-observation/images/shadow-api-tags-detail.png)

This page includes the following information about the observation.

  * The summary box at the top of the page shows: 
    * **API observation ID:** This is an Apigee-specific identifier.
    * **API operations:** See View API observations for a description of this field.
    * **Create time (UTC):** The date and time the observation job was created.
    * **Tags:** Use tags to organize observation job results.
    * **Last event detected time:** See View API observations for a description of this field.
  * A table of specific API operations detected on this discovered API. For each request, the following information is shown: 
    * **Path:** The request path.
    * **Method:** The request method (such as GET, PUT, etc.).
    * **Count:** The number of requests to that path with that method.
    * **Transaction request:** The request body from traffic data. Includes the request headers and corresponding transaction counts for this API operation.
    * **Transaction response headers:** The response headers from traffic data. Includes the response headers and corresponding transaction counts for this API operation.
    * **Transaction response codes:** The response codes and corresponding counts of responses with that code for this API operation.
    * **First seen (UTC):** The first date and time that the request to this API Operation was observed.
    * **Last seen (UTC):** The most recent date and time that the request to this API Operation was observed.



#### Use tags

_Tags_ allow you to categorize observation results. Tags are metadata and are for your tracking only; tags do not change anything in the observation results or trigger any actions. For example, adding a "Needs attention" tag does not create any notices or alerts. New observation results do not have tags.

Tags have these characteristics:

  * You can add the same tag to multiple observation results.
  * Tag names can include upper and lower case characters, numbers, and special characters, including spaces.
  * Once a tag is created, the name cannot be changed; remove and recreate the tag to rename it.
  * Removing a tag from all observation results deletes it from the system.



You can manage tags from either the observation list or the observation details page.

To manage tags from the API observations list:

  * See the existing tags in the observations list **Tags** column.
  * To manage tags for one result, select **Manage tags** from the **Actions** menu in the row for that result.
  * To manage tags for one or more results at the same time, select multiple results from the list and then **Manage tags** from the top of the list.



To manage tags from the API observation details:

  * See the existing tags in the **Tags** section.
  * To add or manage tags, choose **Manage tags** at the top of the page.



In the **Manage tags** side panel, to add tags, either select existing tags or add new ones. To remove tags, unselect them. Click **Save** to save the new tags. 

## Access Shadow API Discovery from API hub

For information on accessing Shadow API Discovery from API hub, see [Manage API Observation in API hub](https://docs.cloud.google.com/apigee/docs/apihub/manage-api-observation).

## Best practices

We recommend these practices when working with Shadow API Discovery:

  * Follow your organization's Data Residency rules to ensure compliance with any applicable regulations and laws. 
  * Aggregate from as many source regions as possible to get the best cross-regional correlation. Including more source regions in your observation jobs results in a broader view of APIs across your infrastructure.



## Behaviors and limitations

This section lists behaviors and limitations that apply to Shadow API Discovery:

  * Use of Shadow API Discovery does not guarantee observation of 100% of traffic or discovery of all shadow APIs.
  * Shadow API Discovery finds Shadow APIs on your Google Cloud infrastructure only.
  * Observation jobs and sources must be configured in the same project where the VPC network and subnetwork are set up.
  * Shadow API Discovery supports only External and Internal [ Application Load Balancers](https://cloud.google.com/load-balancing/docs/application-load-balancer) at this time. Network Load Balancers are not supported.
  * Shadow API Discovery finds HTTP protocol APIs, not gRPC.
  * Running API observation jobs on load balancers does not have any latency impact on API traffic.
  * **Warning:** Shadow API Discovery supports load balancers on one network per project. If you enable Shadow API Discovery on a project with multiple networks, you might see unexpected behavior.
  * There must be traffic flowing through load balancers in your observed projects in order to detect Shadow APIs.
  * It can take up to 30 minutes for a newly enabled observation job to detect traffic, depending on the traffic volume. Sparse traffic requires longer observation times before results are available.
  * Per region, there is a limit of a single observation source and a maximum of three observation jobs. If you need more than three observation jobs, please contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/) to discuss the use case.
  * Observation jobs can be created and disabled or deleted, but not edited. If you need to change an observation job, delete it and recreate it.
  * The following regions are currently supported for API observation and Shadow APIs: 
    * australia-southeast1
    * europe-west2
    * europe-west9
    * us-central1
    * us-east1
    * us-west1



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
