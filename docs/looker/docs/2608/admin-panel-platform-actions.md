---
url: https://docs.cloud.google.com/looker/docs/2608/admin-panel-platform-actions/
title: Admin settings - Actions \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:55:57.010243+00:00
---

# Admin settings - Actions  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2608/admin-panel-platform-actions/

You are viewing documentation for Looker 26.8. Click this link to see the [most recent documentation](https://docs.cloud.google.com/looker/docs/intro). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/2608/intro)



Send feedback 

#  Admin settings - Actions Stay organized with collections  Save and categorize content based on your preferences. 

The **Actions** page in the **Platform** section of the **Admin** menu lets you enable services that are integrated with Looker. For information about building and testing actions to add to the Looker Action Hub _or_ your own private action hub server, see the [Sharing data through an action hub](https://docs.cloud.google.com/looker/docs/2608/action-hub) documentation page.

This page described how to enable an individual action in the Looker Action Hub.

## Before you begin

**Note:** To use Looker integrations, the Looker Action Hub must be able to communicate with the Looker instance and fulfill these [Looker Action Hub requirements](https://docs.cloud.google.com/looker/docs/2608/action-hub#looker_action_hub_requirements). Admins of customer-hosted instances may need to consider [additional factors](https://docs.cloud.google.com/looker/docs/2608/action-hub#considerations_for_customer-hosted_instances) when choosing to enable Looker integrations from the Looker Action Hub, especially integrations that [support streamed results](https://docs.cloud.google.com/looker/docs/2608/action-hub#uses_streaming) or that use [OAuth](https://docs.cloud.google.com/looker/docs/2608/action-hub#configuring_an_action_for_oauth).

To access the **Actions** page in the **Platform** section of the **Admin** menu, your user must have the [Admin role](https://docs.cloud.google.com/looker/docs/2608/admin-panel-users-roles#default_roles).

## Test the Looker Action Hub connection

**Note:** This option is available only for the Looker Action Hub. It is not available for [custom action hubs](https://docs.cloud.google.com/looker/docs/2608/action-hub#setting_up_a_local_action_hub_server).

To test your instance's connection to the Looker Action Hub, select **Test Connection**. A "Health check passed" message indicates a successful connection. If your instance can't connect to the Looker Action Hub, Looker displays a health check authentication error message.

## Enable an action

**Tip:** To prompt Looker to check the Looker Action Hub server for new actions, select **Refresh** at the top of the actions list.

Each service that is integrated into Looker's **Actions** page has its own requirements. The [list of integrations](https://docs.cloud.google.com/looker/docs/2608/actions-overview#list_of_integrated_services) has a table of all the available services. See the **How to use this integration** column for links to articles about setting up and using each service.

First perform any setup steps required on the integrated service. Then enable the integration in Looker, specifying any required information for that service.

To enable an integration, perform the following steps:

  1. On the **Platform** page of the **Admin** , select **Actions**.

  2. Find the service that you want to enable, and select the **Enable** button to the right of the service.

Looker then displays the enablement page for the selected service.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-actions-enable-2308.png)

If applicable, enter the required information to configure this action. You should be able to gather this information from your account with the service that you're enabling.

  3. Turn on the **Enabled** switch. Looker automatically tests the action's configuration and displays an error if the action is configured incorrectly. Once you've made changes, select **Test Again** to retest the action's configuration.

  4. Select **Save** to save the action's configuration and close the action enablement page. The action is now available as a destination in the [Looker Scheduler](https://docs.cloud.google.com/looker/docs/2608/scheduling).




## List of integrated services

To view the list of integrated services, see the [Actions overview](https://docs.cloud.google.com/looker/docs/2608/actions-overview#list_of_integrated_services) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
