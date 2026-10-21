---
url: https://docs.cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-looker-reports/
title: Connect to a private connections Looker (Google Cloud core) instance from a report \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:38:32.437109+00:00
---

# Connect to a private connections Looker (Google Cloud core) instance from a report  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-looker-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Connect to a private connections Looker (Google Cloud core) instance from a report Stay organized with collections  Save and categorize content based on your preferences. 

The Looker connector lets you add a Looker Explore as a data source so that you can analyze Looker data in a [Data Studio Pro](https://docs.cloud.google.com/looker/docs/studio/about-looker-studio-pro) report. This documentation page describes how to connect a Data Studio Pro report to a Looker (Google Cloud core) instance that uses a private connections by performing the following tasks:

  * Find the Looker instance ID
  * Use the Looker instance ID to set up a Looker data source



## Before you begin

Your Looker instance must fulfill certain [requirements to be eligible to connect to Data Studio](https://docs.cloud.google.com/looker/docs/studio/limits-of-the-looker-connector). Additionally, a Looker [admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) must enable the [**Data Studio** BI connector](https://docs.cloud.google.com/looker/docs/bi-connectors#looker_studio) in the **Platform** section of the instance's **Admin** panel.

To add a Looker Explore as a data source in Data Studio, you must have [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permissions for the model that contains the Explore.

A Looker data source uses [viewer's data credentials](https://docs.cloud.google.com/looker/docs/studio/data-credentials), so any user viewing Looker data in Data Studio must have at least [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) and [`clear_cache_refresh`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#clear_cache_refresh) permissions for the model that contains the data source's Looker Explore. Learn more about the [Looker permissions that are required](https://docs.cloud.google.com/looker/docs/studio/overview-of-looker-connector-permissions) to enable the Looker connector, create a Looker data source, and view Looker data in Data Studio.

**Important:** The Looker connector can't connect to a Looker (Google Cloud core) instance that is inside a [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) perimeter. For more information about limitations of the Looker connector, see the [Overview of Looker connector requirements, limits, and feature support](https://docs.cloud.google.com/looker/docs/studio/limits-of-the-looker-connector) documentation page. 

Your Data Studio Pro Google Cloud project must be in the same network as the Google Cloud project that hosts the Looker (Google Cloud core) instance.

## Connect to a Looker (Google Cloud core) instance

When [connecting to a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/studio/connect-to-looker), you specify the Looker (Google Cloud core) instance by using either the instance URL or the instance ID, depending on the instance's [network configuration](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#overview):

  * Use the **Instance URL** to connect to instances that use a public IP network, including the following types of instances:

    * [Public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections)
    * [Hybrid connections (PSC)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip)
    * [Hybrid connections (PSA)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip)



If your Looker (Google Cloud core) instance uses a public IP network, refer to the [Connect to Looker](https://docs.cloud.google.com/looker/docs/studio/connect-to-looker) documentation page for instructions on how to connect to your instance.

  * Use the **Instance ID** to connect to instances that use private connections, including the following types of instances:

    * [Private connections (Private Service Connect)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc)
    * [Private connections (private services access)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa)



### Find the Looker instance ID

To find your Looker instance ID, from the Looker **Help** menu, select **Looker Instance ID**.

![Looker Help menu showing Looker instance ID selection and dialog.](https://docs.cloud.google.com/static/looker/docs/images/looker-instance-id-2504.png)

Looker displays the instance ID in the following format:
    
    
    projects/PROJECT_ID/locations/REGION/instances/INSTANCE_NAME
    

The variables in the previous example represent the following information about your instance:

  * `PROJECT_ID`: The name of the Google Cloud project in which you created the Looker (Google Cloud core) instance.
  * `REGION`: The region in which your Looker (Google Cloud core) instance is hosted.
  * `INSTANCE_NAME`: The name of your Looker (Google Cloud core) instance; it isn't associated with the instance URL.



You can copy the instance ID to your clipboard by clicking the **Copy** button.

### Use the instance ID to connect from a report

Next, you can use the [Looker connector](https://docs.cloud.google.com/looker/docs/studio/connect-to-looker#use_looker_connector) to connect to a Looker (Google Cloud core) private connections (private services access) instance or a private connections (Private Service Connect) instance.

Within your report, perform the following steps:

  1. From the **Data** panel, select **Add data**.
  2. Select the Looker connector.
  3. In the **Enter Looker Instance URL/ID** field, enter the instance ID that you copied from your instance.



![Looker connector instance URL or ID field.](https://docs.cloud.google.com/static/looker/docs/studio/images/looker-connector-instance-id-2504.png)

Once connected, you will see the instance listed in the **Saved Looker Instances** list, and it will be listed by the full instance ID.

## Use the instance ID to connect from Connected Sheets

To connect to a Looker (Google Cloud core) private IP (private services access) only instance or a private IP (Private Service Connect) only instance from Connected Sheets, enter the Looker instance ID in the **Connect to Looker** dialog. Enter the entire instance ID, using the following format:
    
    
    projects/<project id>/locations/<region>/instances/<instance name>
    

## Add or remove a public IP connection after connecting to Data Studio Pro

For instances that use [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) or [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect), admins can [add or remove a public IP connection](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings). Adding or removing a public IP connection has the following effects:

  * To create new connections to Looker (Google Cloud core) instances that have a public IP connection, you must use the instance URL. No network check is performed when data is accessed.
  * To create new connections to Looker (Google Cloud core) instances that don't have a public IP connection, you must use the instance ID. Private network enforcement is in place for data access.
  * Data sources that were created when a public IP connection was enabled will function only when a public IP connection is enabled. If the Looker (Google Cloud core) instance's public IP connection has been disabled, users must reconnect to the instance using the instance URL.
  * Data sources that were created when a public IP connection was disabled will function only when a public IP connection is disabled. Users must reconnect to the data source if the public IP connection has been enabled.



## Troubleshooting

If you receive an error while trying to connect to a Looker (Google Cloud core) private connections (PSA) instance or to a private connections (Private Service Connect) instance or data source, you may not be on the correct network to access the instance data. Select the same network as the one being used by the instance and retry the connection.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
