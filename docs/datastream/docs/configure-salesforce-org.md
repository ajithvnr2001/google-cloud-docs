---
url: https://docs.cloud.google.com/datastream/docs/configure-salesforce-org/
title: Configure a Salesforce organization for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:47.704430+00:00
---

# Configure a Salesforce organization for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-salesforce-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a Salesforce organization for CDC Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure change data capture (CDC) to stream data from a Salesforce organization to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage.

## Before you begin

Before you start configuring Salesforce for use with Datastream, you need to:

  * Have access to an active Salesforce organization
  * Have knowledge of how to navigate and change settings in Salesforce
  * Have knowledge of how to create users and profiles in Salesforce



## Configure a Salesforce organization for use with Datastream

To establish a connection between your Salesforce org and Datastream, you need to authenticate either by using a username and a password, or by using the OAuth 2.0 client credentials flow. To use the latter, you can create a [_Salesforce connected app_](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_overview.htm&type=5) or an [_external client app_](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5).

If your Salesforce org is configured to allow access from specific IP addresses, make sure that Salesforce accepts [Datastream IP addresses](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions). For information about how to manage your network access restrictions, see [Network access and profile-based IP restrictions](https://help.salesforce.com/s/articleView?id=000386441&type=1) and [Set trusted IP ranges for your organization](https://help.salesforce.com/s/articleView?id=sf.security_networkaccess.htm) in the Salesforce documentation.

## Configure a user

  1. In Salesforce, either create a user, or adjust the settings for an existing user as per the instructions that follow.
  2. Create a dedicated profile and assign it to the user.
  3. If your organization has IP address restrictions configured, make sure that you add the [Datastream IP addresses](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions) to the list of allowed IP addresses. For more information, see [Restrict login IP addresses in profiles](https://help.salesforce.com/s/articleView?id=platform.login_ip_ranges.htm&type=5).
  4. Make sure that the user profile has the [`API Enabled`](https://help.salesforce.com/s/articleView?id=sf.branded_apps_commun_api_permset.htm&type=5) permission so that the user can use both the [Salesforce REST API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm) and [Bulk API 2.0](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm).
  5. Make sure that the user profile has the permissions to read all [objects](https://help.salesforce.com/s/articleView?id=platform.users_profiles_object_perms.htm&type=5) and [fields](https://help.salesforce.com/s/articleView?id=platform.users_profiles_field_perms.htm&type=5) that you want to include in your stream. For security reasons, consider granting the user read-only permissions. For more information, see [Control who sees what](https://developer.salesforce.com/docs/atlas.en-us.securityImplGuide.meta/securityImplGuide/security_data_access.htm) in the Salesforce documentation.
  6. Optional: By default, Salesforce returns encrypted fields as masked fields. If you need your user to view the actual values of encrypted fields, grant them the `View Encrypted Data` permission. You can grant the permission by editing the user's permission set.



## Optional: Create and set up a connected app

Salesforce uses connected apps to integrate external applications with the Salesforce API, integrate service providers with your Salesforce org, or to control what data a third-party application can access from your Salesforce organization. If you prefer to use a connected app to authenticate your Salesforce instance in Datastream, perform the following steps:

  1. Create a connected app. For more information, see the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.connected_app_create.htm&type=5).
  2. Configure your connected app for the [OAuth 2.0 client credentials flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

**Note:** Make sure that the user to whom you want to assign the client credentials flow has the appropriate API permissions and access to all objects and fields that you want to include in your stream.   
  
In Salesforce, go to **Setup > Connected apps > Manage connected apps**. Click the connected app for which you want to edit permissions. Under **Client credentials flow** , click the user for whom you want to edit credentials flow settings.
  3. Make sure that your connected app has the `Manage user data via APIs (api)` scope enabled. For more information about scopes, see [OAuth tokens and scopes](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_tokens_scopes.htm&type=5).

  4. Make sure that your connected app can access the Salesforce APIs with the Datastream IP addresses. For more information, see [Restrict access to APIs with connected apps](https://help.salesforce.com/s/articleView?id=xcloud.security_api_access_control_all_users.htm&type=5) and [Configure trusted IP ranges for a connected app](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_edit_ip_ranges.htm&type=5).

  5. Get the consumer key and consumer secret:

     1. In Salesforce, enter `App` in the quick find box, and then select **App Manager**.
     2. Find your connected app in the list and expand the drop-down to the right of the row.
     3. Select **View**.
     4. In the **Manage connected apps** details page, click **Manage consumer details**.
     5. A screen opens asking you for a verification code. An email with the verification code is sent to the user to whom you assign the client credentials flow.
     6. Enter the verification code. You are then redirected to the consumer details page where you can find your key and secret. You need to provide the consumer key and secret when you create your connection profile.



## What's next

  * Learn more about the [Salesforce source](https://docs.cloud.google.com/datastream/docs/sources-salesforce).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
