---
url: https://docs.cloud.google.com/looker/docs/mobile-app-enablement/
title: Enabling the mobile application \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:14.489181+00:00
---

# Enabling the mobile application  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/mobile-app-enablement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Enabling the mobile application Stay organized with collections  Save and categorize content based on your preferences. 

The Looker mobile application lets users perform the following functions from a mobile device:

  * [View their favorite and recently viewed content](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content)
  * [Access the boards they follow](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content#navigating_to_content_from_boards)
  * [Navigate to content in folders](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content#browsing_content_in_folders)
  * [View Looks](https://docs.cloud.google.com/looker/docs/mobile-app-viewing-looks) and [dashboards](https://docs.cloud.google.com/looker/docs/mobile-app-viewing-dashboards)



Admins can enable the Looker mobile app to let users [sign in](https://docs.cloud.google.com/looker/docs/mobile-app-sign-in) to their Looker instance on an Android or iOS device.

## Enabling the app for your instance

> When [IP allowlists](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) are enabled, users cannot connect to the instance from their service providers' IP addresses.

Access to the Looker mobile app is enabled for your instance by default. To disable or enable access to the mobile app for your instance, follow these steps:

  1. Open the [**Settings** page](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings) in the **General** section of the **Admin** panel.
  2. In the **Feature Configuration** section of the **General Settings** page, choose **Enabled** or **Disabled** under **Mobile Application Access**.

**Note:** The **Mobile Application Access** setting applies to both the [Looker app](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) and the [Looker (Legacy) app](https://docs.cloud.google.com/looker/docs/mobile-app-legacy).
  3. Select **Update** to apply your changes.




When the app is enabled for your instance, users can [install the app](https://docs.cloud.google.com/looker/docs/mobile-app-installation) and [sign in to your instance](https://docs.cloud.google.com/looker/docs/mobile-app-sign-in) on their mobile devices.

If you disable the **Mobile Application Access** setting for your instance, any existing mobile app sessions will be invalidated.

## Assigning mobile app access to specific users

Admins can use the [`mobile_app_access`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#mobile_app_access) permission to grant specific users and groups access to the Looker mobile app. To grant mobile app access to a specific user or group, follow these steps:

  1. Ensure that mobile app access is enabled for your Looker instance.
  2. Assign that user or group a [role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#assigning_roles) with a [permission set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets) that includes the [`mobile_app_access` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#mobile_app_access).



Users with the `mobile_app_access` permission can [sign in to the Looker mobile app](https://docs.cloud.google.com/looker/docs/mobile-app-sign-in) using the same authentication method that they use to sign in to your Looker instance. If a user does not have the `mobile_app_access` permission, Looker displays an error upon trying to sign in to the app.

See the [Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#assigning_roles) documentation page for information about assigning roles to users or groups.

## Forcing users to authenticate each time they sign in to the mobile app

Admins can require users to sign back in to Looker every time they open the mobile app by enabling the **Force mobile authentication** setting in the [**General Settings**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#force_mobile_authentication) section of the **Admin** panel. To enable this feature, follow these steps:

  1. Navigate to the **Settings** page in the **General** section of the **Admin** panel.
  2. Under **Force mobile authentication** , select **Enabled**.



When **Force mobile authentication** is enabled, users will be required to sign in to Looker every time they open the app on their mobile devices. Additionally, users will be logged out of the mobile app after 60 minutes of inactivity.

**Note:** If the **Force mobile authentication** setting is enabled, app lock verification supersedes a forced logout.

## Considerations for Looker (Google Cloud core) instances

If your instance is a Looker (Google Cloud core) instance that is using [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa) or [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc), your private network must be reachable by the mobile device.

## Considerations for customer-hosted instances

Admins of [customer-hosted](https://docs.cloud.google.com/looker/docs/glossary#customer-hosted) instances should consider the following requirements when enabling the mobile app for their instance:

  * The web server and API endpoints must be publicly accessible or otherwise reachable by the mobile app. 
    * To test connectivity, try accessing the URL of your Looker instance from a web browser on your mobile device.
  * The [API Host URL](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api#api_host_url) must have the same hostname as the instance URL and serve traffic on either port 443 or port 19999. The URL should follow this form: `https://<instance_name>.looker.com:<port>`



For additional information, see the [Looker API troubleshooting](https://docs.cloud.google.com/looker/docs/api-troubleshooting) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
