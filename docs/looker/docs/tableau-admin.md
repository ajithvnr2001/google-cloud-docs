---
url: https://docs.cloud.google.com/looker/docs/tableau-admin/
title: Administering Tableau to Looker connections \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:38.284324+00:00
---

# Administering Tableau to Looker connections  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/tableau-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Administering Tableau to Looker connections Stay organized with collections  Save and categorize content based on your preferences. 

The Looker–Tableau BI Connector lets you use a Looker Explore as a data source in Tableau Desktop, Tableau Cloud, and Tableau Server. The Looker–Tableau BI Connector is built upon the Looker [Open SQL Interface](https://docs.cloud.google.com/looker/docs/sql-interface), which allows access to LookML models and Explores for applications that use Java Database Connectivity (JDBC) to connect to data sources.

See the following sections for information on the administration steps required for connecting to Looker from these Tableau products:

  * Tableau Desktop
  * Tableau Cloud
  * Tableau Server



## Tableau Desktop

To set up your Looker instance as a data source for [Tableau Desktop](https://docs.cloud.google.com/looker/docs/tableau-connector#desktop), a Looker admin must enable the [**Tableau Desktop**](https://docs.cloud.google.com/looker/docs/bi-connectors#tableau_desktop) toggle on the Looker [**BI Connectors**](https://docs.cloud.google.com/looker/docs/bi-connectors) page.

In addition, for [Looker (Google Cloud core) instances that are configured for private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) and [customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps), your instance must meet the following requirements:

  * The instance must be running Looker 25.16 or later.
  * Your network administrator must configure your network so that traffic from Tableau Desktop can reach your Looker instance. 



## Tableau Cloud

To set up your Looker instance as a data source for [Tableau Cloud](https://docs.cloud.google.com/looker/docs/tableau-connector#cloud), the following tasks are required:

  * A Looker admin must set up OAuth for Tableau Cloud.
  * A Tableau admin must register the OAuth client ID on Tableau Cloud.
  * A Tableau user with [permissions to add data sources](https://help.tableau.com/current/online/en-us/permission_license_siterole.htm) must add **Looker by Google** as a data source.
  * For [Looker (Google Cloud core) instances that are configured for private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) and [customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps), a network administrator must configure your network so that traffic from the Looker–Tableau BI Connector can reach your Looker instance.



### Set up OAuth for Tableau Cloud

To use the Looker–Tableau BI Connector for Tableau Cloud, you need to set up OAuth integration on your Looker instance.

You can use the Looker [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) to set up OAuth integration for the Looker–Tableau BI Connector:

  * If your Looker instance already has the API Explorer installed, you can access it with this URL format:
        
        https://LOOKER_INSTANCE_URL/extensions/marketplace_extension_api_explorer::api-explorer/
        

  * If your Looker instance doesn't have the API Explorer, you can install it from the Looker Marketplace. See the [Using the API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer#installing_the_api_explorer) page for information.




To use the API Explorer to set up OAuth integration on your Looker instance, follow these steps:

  1. Open the Looker API Explorer (see the [Using the API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer#starting_the_api_explorer) page for information).
  2. In the API Explorer's **Search** field, enter **Register OAuth App**.
  3. In the search results, click **Register OAuth App**.
  4. On the **Register OAuth App** page, click the **Run It** button.
  5. In the **Request** tab of the **Run It** dialog, enter the following information into the corresponding fields:

     * **client_guid** (suggested value: `tableau-cloud`):
           
           client_guid
           

     * **body** :
           
           {
              "redirect_uri": "TABLEAU_CLOUD_URL/auth/add_oauth_token",
              "display_name": "Looker-Tableau-Cloud (manual)",
              "description": "Client for Looker-Tableau Cloud integration (manually added)",
              "enabled": true,
              "group_id": ""
            }
           

  6. Select the checkbox for **I understand that this API endpoint will change data.**

  7. Click **Run**.

  8. You can verify that you successfully set up authentication by using the `Get OAuth Client App` method in the API Explorer by following these steps:

     * In the API Explorer's **Search** field, enter **Get OAuth Client App**. 
     * Click **Run It**.
     * In the **client_guid** field, enter the value that you used when you registered the OAuth:
           
           client_guid
           

If you set up OAuth successfully, the **Response** tab will return the values that you entered when you registered the app.




### Register the OAuth client ID on Tableau Cloud

After you set up OAuth for Tableau Cloud in the Looker API, you need to register the custom OAuth client on Tableau Cloud by following these steps:

  1. Sign in to Tableau Cloud using your admin credentials, and then navigate to the **Settings** page.
  2. In the **General** tab of the **Settings** page, scroll to **OAuth Clients Registry** and click **Add OAuth Client**.
  3. In the **Create OAuth Client** dialog, enter the following information:

     * **Connection Type** : Select **Looker by Google** from the drop-down menu.
     * **OAuth Provider** : Select **Default IDP** from the drop-down menu.
     * **OAuth instance URL** : Enter your Looker instance URL with the `https://`. For example: `https://example.cloud.looker.com`:
           
           https://LOOKER_INSTANCE_URL
           

     * **Client ID** : Enter the **client_guid** value that you used when you set up OAuth for Tableau Cloud on your Looker instance:
           
           client_guid
           

     * **Client Secret** : Leave this field blank.

     * **Redirect URL** : Enter the **redirect_uri** value that you used when you set up OAuth for Tableau Cloud on your Looker instance:
           
           TABLEAU_CLOUD_URL/auth/add_oauth_token
           

  4. Click the **Add OAuth Client** button to register the OAuth client ID and return to the **Settings** page.

  5. Click the **Save** button at the bottom or top of the **Settings** page to save your changes.




### Add **Looker by Google** as a data source

A Tableau Cloud user who has a [Tableau role](https://help.tableau.com/current/online/en-us/permission_license_siterole.htm) that allows for creating data sources must add **Looker by Google** as a data source on your Tableau Cloud instance. If **Looker by Google** isn't added as a data source, it won't be visible or available to users who lack permission to add new data sources.

See the [Connecting to Looker data from Tableau Cloud](https://docs.cloud.google.com/looker/docs/tableau-connector#connecting-cloud) section in the Looker documentation for the procedure on adding Looker as a data source in Tableau Cloud.

## Tableau Server

To use Looker data for [Tableau Server](https://docs.cloud.google.com/looker/docs/tableau-connector#server), the following tasks are required:

  * A Looker admin must set up OAuth for Tableau Server.
  * A Tableau admin must install the Looker–Tableau BI Connector on Tableau Server
  * A Tableau admin must register the OAuth client ID on Tableau Server.
  * For [Looker (Google Cloud core) instances that are configured for private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) and [customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps), a network administrator must configure your network so that traffic from the Looker–Tableau BI Connector can reach your Looker instance. 



### Set up OAuth for the Tableau Server

To use the Looker–Tableau BI Connector for Tableau Server, you need to set up OAuth integration on your Looker instance.

You can use the Looker [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) to set up OAuth integration for the Looker–Tableau BI Connector:

  * If your Looker instance already has the API Explorer installed, you can access it with this URL format:
        
        https://LOOKER_INSTANCE_URL/extensions/marketplace_extension_api_explorer::api-explorer/
        

  * If your Looker instance doesn't have the API Explorer, you can install it from the Looker Marketplace. See the [Using the API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer#installing_the_api_explorer) page for information.




To use the API Explorer to set up OAuth integration on your Looker instance, follow these steps:

  1. Open the Looker API Explorer (see the [Using the API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer#starting_the_api_explorer) page for information).
  2. In the API Explorer's **Search** field, enter **Register OAuth App**.
  3. In the search results, click **Register OAuth App**.
  4. On the **Register OAuth App** page, click the **Run It** button.
  5. In the **Request** tab of the **Run It** dialog, enter the following information into the corresponding fields:

     * **client_guid** (suggested value: `tableau-server`):
           
           client_guid_server
           

     * **body** :
           
           {
            "redirect_uri": "TABLEAU_SERVER_URL/auth/add_oauth_token",
            "display_name": "Looker-Tableau-Server (manual)",
            "description": "Client for Looker-Tableau Server integration (manually added)",
            "enabled": true,
            "group_id": ""
           }
           

  6. Select the checkbox for **I understand that this API endpoint will change data.**

  7. Click **Run**.

  8. You can verify that you successfully set up authentication by using the `Get OAuth Client App` method in the API Explorer by following these steps:

     * In the API Explorer's **Search** field, enter **Get OAuth Client App**. 
     * Click **Run It**.
     * In the **client_guid** field, enter the value that you used when you registered the OAuth:
           
           client_guid_server
           

If you set up OAuth successfully, the **Response** tab will return the values that you entered when you registered the app.




### Install the Looker–Tableau BI Connector on Tableau Server

To install Looker–Tableau BI Connector on Tableau Server, perform the following steps:

  1. Download the latest version of the `avatica-<release_number>-looker.jar` file from <https://github.com/looker-open-source/calcite-avatica/releases>.
  2. Install the JAR file on your Tableau Server host machine. The default Tableau installation path for the file depends on the server's operating system:

     * Linux server: `/opt/tableau/tableau_driver/jdbc`
     * Windows server: `C:\Program Files\Tableau\Drivers`



### Register the OAuth client ID on Tableau Server

After you set up OAuth for Tableau Server in the Looker API, you need to register the custom OAuth client on Tableau Server by following these steps:

  1. Sign in to Tableau Server using your admin credentials, and then navigate to the **Settings** page.
  2. In the **General** tab of the **Settings** page, scroll to **OAuth Clients Registry** , and click **Add OAuth Client**.
  3. In the **Create OAuth Client** dialog, enter the following information:

     * **Connection Type** : Select **Looker by Google** from the drop-down menu.
     * **OAuth Provider** : Select **Default IDP** from the drop-down menu.
     * **OAuth instance URL** : Enter your Looker instance URL with the `https://`. For example: `https://example.cloud.looker.com`:
           
           https://LOOKER_INSTANCE_URL
           

     * **Client ID** : Enter the **client_guid** value that you used when you set up OAuth for Tableau Server on your Looker instance:
           
           client_guid_server
           

     * **Client Secret** : Leave this field blank.

     * **Redirect URL** : Enter the **redirect_uri** value that you used when you set up OAuth for Tableau Server on your Looker instance:
           
           TABLEAU_SERVER_URL/auth/add_oauth_token
           

  4. Click the **Add OAuth Client** button to register the OAuth client ID and return to the **Settings** page.

  5. Click the **Save** button at the bottom or top of the **Settings** page to save your changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
