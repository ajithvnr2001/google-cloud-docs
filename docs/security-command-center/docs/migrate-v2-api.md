---
url: https://docs.cloud.google.com/security-command-center/docs/migrate-v2-api/
title: Migrate to v2 of the Security Command Center API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:04.370880+00:00
---

# Migrate to v2 of the Security Command Center API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/migrate-v2-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Migrate to v2 of the Security Command Center API Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the differences between version 1 (v1) and version 2 (v2) of the [Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/rest). It also explains how to migrate to the v2 Security Command Center API, in combination with the v1 [Security Command Center Management API](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest).

As of December 9, 2024, if you activate Security Command Center within an organization for the first time, then you must use only version 2 of the Security Command Center API in that organization. Earlier versions are not supported.

If you activated Security Command Center at the project level before December 9, 2024, then any projects you activate in the same organization will support all available versions of the Security Command Center API.

For all integrations with Security Command Center, we recommend that you adopt the v2 Security Command Center API and the v1 Security Command Center Management API. We recommend using the Cloud Client Libraries or the Google Cloud Terraform provider to call these APIs. For more information, see the following:

### Terraform

  * [Security Command Center API resources](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_folder_mute_config)
  * [Security Command Center Management API resources](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_management_folder_security_health_analytics_custom_module)



### Client libraries

  * [Security Command Center API client libraries](https://docs.cloud.google.com/security-command-center/docs/reference/libraries)
  * [Security Command Center Management API client libraries](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/libraries)



## Differences between the v1 and v2 APIs

As you migrate to the v2 Security Command Center API, be aware of the following differences from the v1 API.

### Data residency

The v2 Security Command Center API supports [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support), which gives you more control over where your Security Command Center data is located.

If data residency is enabled for your organization, then you must do the following to access resources that are [subject to data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#scc-resources-subject-to-drz):

  * Use a [regional service endpoint](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints) to access the resource.
  * Specify a location when you call the resource's methods.



If data residency is not enabled for your organization, we recommend that you call the location-aware version of each method and specify the `global` location. Doing so makes it easier to adopt data residency in the future.

To use the location-aware version of each method, do the following:

### Console

The Google Cloud console uses the location-aware version of each method whenever necessary.

### gcloud

When you run gcloud CLI commands that let you specify a location, like [`gcloud scc findings list`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list), always provide a location. There are a few ways to do this:

  * Use the `--location` flag.
  * If you provide the full path of the resource name, use a format that specifies a location, like `projects/123/sources/456/locations/global/findings/a1b2c3`.



### Terraform

Always provide the `location` argument for resources that support it, like [`google_scc_v2_organization_mute_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_organization_mute_config#location).

### REST

Call the version of the method with `locations` in its name. For example, call [`organizations.locations.findings.bulkMute`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.findings/bulkMute) rather than [`organizations.findings.bulkMute`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.findings/bulkMute).

### Client libraries

See the [code samples](https://docs.cloud.google.com/security-command-center/docs/samples) for Security Command Center or the [API reference](https://docs.cloud.google.com/security-command-center/docs/reference/libraries#resources) for your client library.

To learn how to use regional endpoints when data residency is enabled, see [Security Command Center regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints).

### Notification configurations and BigQuery export configurations

The v1 Security Command Center API lets you create and manage the following types of export configurations:

  * [Notification configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications), which send findings to Pub/Sub
  * [BigQuery export configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query), which stream findings to BigQuery



You can also create and manage these export configurations with the v2 Security Command Center API. However, if you create an export configuration with the v1 Security Command Center API, then it's not visible in the v2 Security Command Center API. Similarly, if you create an export configuration with the v2 Security Command Center API, then it's not visible in the v1 Security Command Center API.

In addition, export configurations that you create with the v2 Security Command Center API cannot use the `source_properties` field to [filter findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications). You must use another field instead.

### Console

In the Google Cloud console, if an export configuration was created with the v1 Security Command Center API, then it has a **Legacy** label. You can use the Google Cloud console to manage these resources.

If you create a new export configuration in the Google Cloud console, then it's always created with the v2 Security Command Center API. 

### gcloud

To manage export configurations that were created with the v1 Security Command Center API, don't specify a location when you run gcloud CLI commands such as [`gcloud scc notifications describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/notifications/describe):

  * Don't use the `--location` flag.
  * If you provide the full path for the configuration ID, use a format that doesn't specify a location, like `organizations/123/notificationConfigs/456`. Don't use a format like `organizations/123/**locations/global/** notificationConfigs/456`.



Similarly, to create or manage export configurations with the v2 Security Command Center API, specify a location when you run the gcloud CLI command. When you create new configurations, we recommend that you use the v2 Security Command Center API. 

### Terraform

Your Terraform configuration file defines export configurations as either v1 or v2 resources. For example, see the resources for notification configurations:

  * v1 
    * [`google_scc_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_notification_config)
    * [`google_scc_folder_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_notification_config)
    * [`google_scc_project_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_project_notification_config)
  * v2 
    * [`google_scc_v2_organization_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_organization_notification_config)
    * [`google_scc_v2_folder_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_folder_notification_config)
    * [`google_scc_v2_project_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_project_notification_config)



When you create new configurations, we recommend that you create v2 resources.

### REST

To manage export configurations that were created with the v1 Security Command Center API, you must use the v1 Security Command Center API.

When you create new configurations, we recommend that you use the v2 Security Command Center API.

### Client libraries

To manage export configurations that were created with the v1 Security Command Center API, you must use the Cloud Client Libraries for the v1 Security Command Center API.

When you create new configurations, we recommend that you use the v2 Security Command Center API.

### Built-in services and custom modules

The v1 Security Command Center API lets you view and update these resource types:

  * Security Command Center [built-in services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) and their enablement states
  * Custom modules for the following built-in services: 
    * [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.eventThreatDetectionSettings.customModules)
    * [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.securityHealthAnalyticsSettings.customModules)



To manage these resource types, use the [Security Command Center Management API](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest) and its [client libraries](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/libraries). The v2 Security Command Center API can't manage these resource types.

### Asset management

If your organization activated Security Command Center before June 20, 2023, then you might use the v1 Security Command Center API to [view assets](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.assets/list) in an organization, folder, or project. These Security Command Center asset management features are deprecated and are not available in the v2 Security Command Center API. These features will be removed from the v1 Security Command Center API on or after June 20, 2024.

Instead, you can use Cloud Asset Inventory to view your assets, including their security marks. For details, see [List assets](https://docs.cloud.google.com/asset-inventory/docs/list-assets).

You can also use the v2 Security Command Center API to [update security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-api-add-manage-security-marks) for your assets. The Security Command Center API methods that update security marks _are not_ deprecated.

## Update client libraries and Terraform provider

To update your code to use the v2 Security Command Center API, do the following:

### Terraform

Install the current version of the Terraform provider for Google Cloud. For details, see the [provider documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

In addition, update your Terraform configuration file to create resources that start with the prefix `google_scc_v2_` or `google_scc_management_`. Keep in mind that the following resources are not shared across the v1 and v2 APIs:

  * [`google_scc_folder_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_notification_config)
  * [`google_scc_folder_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_scc_big_query_export)
  * [`google_scc_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_notification_config)
  * [`google_scc_organization_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_organization_scc_big_query_export)
  * [`google_scc_project_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_project_notification_config)
  * [`google_scc_project_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_project_scc_big_query_export)



If you apply a Terraform execution plan that replaces these resources with their v2 equivalents, then Terraform will delete the v1 configurations and create new v2 configurations.

### C++

Update your application to include the client library's v2 header file:
    
    
    #include "google/cloud/securitycenter/v2/security_center_client.h"
    

In addition, update your application to use classes in the v2 namespace:
    
    
    namespace securitycenter = ::google::cloud::securitycenter_v2;
    

### C#

Install the v2 client library, then update your application to use that library:
    
    
    Install-Package Google.Cloud.SecurityCenter.V2
    

### Go

Install the v2 client library, then update your application to use that library:
    
    
    go get cloud.google.com/go/securitycenter/apiv2
    

### Java

Install the current version of the client library. For details, see [Install the client library](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).

In addition, update your application to use the classes, interfaces, and enums in the [`com.google.cloud.securitycenter.v2` package](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2).

### Node.js

Install the current version of the client library. For details, see [Install the client library](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).

In addition, update your application to use [`v2.SecurityCenterClient`](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/v2.securitycenterclient) and the classes, interfaces, and enums in the `protos.google.cloud.securitycenter.v2` namespace.

### PHP

Install the current version of the client library. For details, see [Install the client library](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).

In addition, update your application to use the classes and enums in the [`Google \ Cloud \ SecurityCenter \ V2` namespace](https://docs.cloud.google.com/php/docs/reference/cloud-security-center/latest/V2.Client.SecurityCenterClient).

### Python

Install the current version of the client library. For details, see [Install the client library](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).

In addition, update your application to use the classes in the [`google.cloud.securitycenter_v2` package](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center).

### Ruby

Install the current version of the client library. For details, see [Install the client library](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).

In addition, update your application to set the `version` parameter to `:v2` when it [creates a client object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center/latest/Google-Cloud-SecurityCenter#Google__Cloud__SecurityCenter_security_center_class_).

If you need to programmatically manage Security Command Center [built-in services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) and their enablement states, or custom modules for Event Threat Detection or Security Health Analytics, then you must also install a [client library for the Security Command Center Management API](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/libraries) and update your application to use that client library.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
