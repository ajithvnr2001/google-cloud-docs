---
url: https://docs.cloud.google.com/apigee/docs/apihub/configure-advanced-api-security-multi-gateway/
title: Configure Apigee Advanced API Security for multiple Apigee organizations and gateways \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:57:11.395085+00:00
---

# Configure Apigee Advanced API Security for multiple Apigee organizations and gateways  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/configure-advanced-api-security-multi-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure Apigee Advanced API Security for multiple Apigee organizations and gateways Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page explains how to configure and manage the Apigee Advanced API Security add-on for multiple Apigee organizations and gateways. 

## Before you begin

Before you can configure Apigee Advanced API Security for multiple Apigee organizations and gateways, ensure that you have completed the following: 

  * Provision API hub. For more information, see [Provision API hub](https://docs.cloud.google.com/apigee/docs/apihub/provision).
  * For Apigee X and Apigee hybrid gateways, attach the Apigee runtime projects to API hub. Ensure to select the API assets to import into API hub. For information about attaching Apigee X and Apigee Hybrid runtime projects, see [Attach a runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project). 
  * For Apigee Edge Public Cloud gateways, create the Apigee Edge plugin instance in API hub. For more information, see [Create plugin instances](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances).
  * Enable and configure API insights for the gateways (plugin instances) that you want to cover with Advanced API Security. For more information, see [Configure API insights](https://docs.cloud.google.com/apigee/docs/apihub/configure-api-insights).
  * Grant the required IAM roles and permissions to your principal account. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/advanced-api-security-multi-gateway#iam-roles). 



## Enable Advanced API Security for multiple Apigee organizations and gateways

To use Advanced API Security for multiple Apigee organizations and gateways, you must first enable this add-on for your API hub instance and then configure the runtime projects and environments that you want to be covered by Advanced API Security. 

**Caution:** Pricing for Advanced API Security varies based on your existing Apigee organization license type. We recommend that you use the **Advanced API Security advisor tool** to understand the costs before following the instructions on this page. For more information, see [Advanced API Security advisor tool](https://docs.cloud.google.com/apigee/docs/apihub/advanced-api-security-advisor). 

### Console

To enable the Advanced API Security add-on for your API hub instance, do the following: 

  1. In the Google Cloud console, go to the **API hub > Add-on management** page. 

[Go to Add-on management](https://console.cloud.google.com/apigee/api-hub/add-on-management)

  2. Locate the **Advanced API Security** card and click **Enable add-on**. 

The **Manage Apigee add-ons** pane appears. 

  3. Configure the runtime projects and environments that you want to be covered by Advanced API Security: 
     1. Click **Add runtime project**.
     2. Click the **Select Apigee runtime project** drop-down and select the Apigee runtime project that you want to add. **Note:** The drop-down list only displays the runtime projects, across Apigee X, Apigee hybrid, and Apigee Edge Public Cloud gateways that configured to API hub. 
     3. Configure the Apigee environments for the selected runtime project. Do one of the following: 
        * Enter the environment names that you want to cover from the selected Apigee runtime project. This gives you granular control over which runtime data is assessed, helping you to manage costs. **Note:** API hub doesn't validate the environment names that you enter for Apigee Edge Public Cloud gateways. Ensure that you have the correct environment names before proceeding. 

For Apigee X/hybrid gateways, the environment names are validated against the actual environment configurations in the runtime project. 

        * Select the **Enable add on for all Apigee gateway environments in this runtime project** checkbox to enable Advanced API Security for all the environments in the selected runtime project. 
**Notes:**
        * API hub doesn't automatically add newly created environments to your configured runtime project after Advanced API Security is enabled. You must add these new environments manually. You can do this by either re-selecting the option to **Enable the add-on for all environments in the runtime project** or by adding each new environment individually. 
        * The option to select all environments is only available for Apigee X and Apigee hybrid runtime projects. Environments for Apigee Edge Public Cloud runtime projects must be manually entered. 
     4. Click **Add**.
     5. Optional: Repeat the previous steps to add additional runtime projects. 
     6. Click **Save**. 

Advanced API Security is enabled for your API hub instance and the runtime projects and environments that you configured. 

![Add-on enabled screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/add-on-enabled.png)![Add-on enabled screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/add-on-enabled.png)




### REST

To enable the Advanced API Security add-on for your API hub instance, use the [projects.locations.apiHubAddons.enable](https://docs.cloud.google.com/apigee/docs/apihub/reference/rest/v1/projects.locations.apiHubAddons/enable) API. 

For more information, see [Manage add-ons](https://docs.cloud.google.com/apigee/docs/apihub/manage-add-ons). 

## Manage runtime projects and environments for Advanced API Security

### Console

To manage the configured runtime projects and environments for Advanced API Security, do the following: 

  1. In the Google Cloud console, go to the **API hub > Add-on management** page. 

[Go to Add-on management](https://console.cloud.google.com/apigee/api-hub/add-on-management)

  2. Locate the **Advanced API Security** card and click **Manage add-on**. 

The **Manage Apigee add-ons** pane appears. 

  3. To remove a runtime project or environment, do the following: 
     1. Click remove_circle_outline **Remove runtime project** in the row of the runtime project or environment you want to remove.
     2. In the confirmation dialog, click **Remove**.
  4. To add a runtime project or environment, click **Add runtime project**. 
     1. In the **Add runtime project** dialog, complete the required steps, and then click **Add**.
  5. Click **Save** to save your changes. 



## Limitations

  * Advanced API Security doesn't support [abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection), [security reports](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs), and [security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) for multiple Apigee organizations and gateways. 

Support for these capabilities is limited to a single Apigee X/hybrid organization. See [Advanced API Security enabled from your Apigee instance](https://docs.cloud.google.com/apigee/docs/api-security/aas-apigee-overview) for more information. 

  * Advanced API Security supports VPC Service Controls (VPC-SC) for Apigee organizations created after June 4, 2026. For Apigee organizations created on or before that date, VPC-SC support is limited; to avoid potential feature limitations, we recommend enabling this add-on for API hub instances associated with organizations that don't have VPC-SC enabled. 
  * Advanced API Security doesn't support custom plugins (gateways from third-party providers). It is currently supported only for Apigee X, hybrid, and Apigee Edge Public Cloud gateways. 
  * Apigee Edge Private Cloud gateways are not supported.



## Considerations

  * If you have not yet enabled the Advanced API Security add-on, the **Risk assessment** page displays an empty state with instructions to enable the add-on through the **Add-on management** page.
  * You can only enable Advanced API Security with multi-gateway support for runtime projects that are attached to API hub. 
  * If you have an existing Apigee X/hybrid runtime project attached, but are unable to see any gateways or environments, then you may need to edit the project settings to import the necessary API assets into API hub. For more information, see [Edit project association settings](https://docs.cloud.google.com/apigee/docs/apihub/edit-project-association-settings).
  * API hub doesn't automatically add newly created environments to your configured runtime project after Advanced API Security is enabled. You must add these new environments manually. You can do this by either re-selecting the option to **Enable the add-on for all environments in the runtime project** or by adding each new environment individually. 



## What's next

  * View security scores across all projects and gateways, see [View security scores across all projects and gateways](https://docs.cloud.google.com/apigee/docs/apihub/view-security-scores-multi-gateway).
  * View security scores for a given API across its deployments in gateways, see [View security scores for APIs](https://docs.cloud.google.com/apigee/docs/apihub/view-api-security-scores).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
