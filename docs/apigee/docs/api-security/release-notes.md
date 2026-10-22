---
url: https://docs.cloud.google.com/apigee/docs/api-security/release-notes/
title: Apigee Advanced API Security release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:30.932227+00:00
---

# Apigee Advanced API Security release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee Advanced API Security release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Apigee Advanced API Security in 2022 and later. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

### What is a feed reader?

Really simple syndication (RSS) feed readers aggregate content from websites that you specify.

Feed reader notifications can be email-, browser-, desktop-, or mobile-based. Some readers are free, or have free versions, and some require a subscription.

A few examples:

  * [Feedly](https://feedly.com)
  * [Feedreader](https://feedreader.com)
  * [Feeder](https://feeder.co/)



More information on RSS:

  * [RSS](https://en.wikipedia.org/wiki/RSS)
  * [ Comparison of feed aggregators](https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators)



Close

See also:

  * [2021 and prior Release notes](https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes)
  * [Known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)

rss_feed Subscribe: 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/apigee-api-security-release-notes.xml) directly. 

## July 10, 2026

Deprecated

**Deprecation and shutdown of GenAI Incident Summary (generative AI Insights)**

The standalone **GenAI Incident Summary** (generative AI Insights) feature in Apigee Advanced API Security Abuse Detection, currently in Preview, is deprecated and shut down as of July 9, 2026. This feature used Google Cloud generative AI large language models (LLMs) to provide automated summaries and mitigation guidance for security incidents identified by the Abuse Detection clustering tool.

For more information, see [GenAI Incident Summary deprecation](https://docs.cloud.google.com/apigee/docs/deprecations/genai-incident-summary).

## March 17, 2026

Announcement

On March 17, 2026 we released an updated version of Advanced API Security abuse detection

Feature

**VPC-SC support in abuse detection**

This release includes full support in Advanced API Security abuse detection for VPC-SC customers. This includes support for VPC-SC with the Advanced Anomaly Detection ML model used for abuse detection, as well as detection exclusion lists.

For usage information, see [Abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection) in the documentation.

## March 10, 2026

Announcement

On March 10, 2026 we released an updated version of Advanced API Security Abuse Detection

Feature

**General availability of monitoring conditions in risk assessment v2**

Starting with this release, the risk assessment v2 monitoring conditions feature is generally available. 

For information on monitoring conditions features and usage see [monitoring conditions and alerts](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#monitoring-conditions). For usage information and a list of all features in Risk Assessment v2, see the [Risk Assessment v2 customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#risk-assessment-v2).

## February 03, 2026

Announcement

On February 3, 2026 we released an updated version of Advanced API Security security actions

Feature

**Support for configuring two condition types within a single security action** Announcing the availability of support for two condition types in a single security action. For example, you can include both IP addresses and ASN numbers in the same security action.

This feature is available in Apigee and Apigee hybrid 1.16.0 and later.

**Note:** This feature is available when configuring the security action via the API, not the UI, at this time.

For usage information, see [Configure multiple condition types](https://docs.cloud.google.com/apigee/docs/api-security/security-actions-api#configure-multiple-condition-types) in the documentation.

## January 12, 2026

Announcement

On January 12, 2026 we released an updated version of Advanced API Security Abuse Detection

Feature

**Introduction of Terraform support for managing Advanced API Security abuse detection exclusion lists**

You can now use Terraform to manage Advanced API Security abuse detection exclusion lists. The feedback feature allows you to specify CIDR ranges and IP addresses to exclude from future incident reports, and is used to exclude traffic known to be safe, such as requests related to automated testing.

**Note:** Exclusion lists are not available for VPC-SC customers at this time.

For usage information, see [Exclude traffic from abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#exclude-traffic-from-abuse-detection) and [Use Terraform in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview) in the Apigee documentation and the [ Terraform abuse detection feedback (exclusion lists) instructions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_feedback).

## December 17, 2025

Announcement

On December 17, 2025 we released an updated version of Advanced API Security Risk Assessment

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**General availability of Risk Assessment v2 and support for assessments using additional policies**

Announcing the [general availability](https://cloud.google.com/products#product-launch-stages) of Risk Assessment v2 and support for assessments using the VerifyIAM policy and these three AI policies: SanitizeUserPrompt, SanitizeModelResponse, and SemanticCacheLookup.

**Note:** The Risk Assessment v2 monitoring conditions feature remains in preview.

For usage information, see [Risk Assessment overview and UI](https://docs.cloud.google.com/apigee/docs/api-security/security-scores) in the documentation.

Feature

**New risk assessment type field when creating or updating a risk assessment version 2 custom security profile**

The API for creating and updating a version 2 risk assessment custom security profile now includes a `risk_assessment_type` field to specify whether the custom security profile applies to an Apigee/Apigee hybrid instance or to API hub multi-gateway.

This field is optional and defaults to `APIGEE`; this is not a breaking change for existing risk assessment users.

See [REST Resource: organizations.securityProfilesV2](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2) for information on the new functionality.

## October 02, 2025

Announcement

On October 2, 2025 we released an updated version of Advanced API Security Abuse Detection

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Introduction of exclusion lists for Abuse Detection and incidents**

You can now specify CIDR ranges and IP addresses to exclude from future incident reports. Use this feature to exclude traffic known to be safe, such as requests related to automated testing.

The new functionality includes the ability to create and manage multiple "exclusion lists" which define traffic to exclude and the reasons it is excluded.

**Note:** Exclusion lists are not available for VPC-SC customers at this time.

For usage information, see [Exclude traffic from abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#exclude-traffic-from-abuse-detection) in the documentation.

## September 19, 2025

Announcement

On September 19, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**New security actions status icons and "expired" note in the security actions UI**

This release adds security status icons to the Apigee UI to make it easier to see, at a glance, whether a security action is enabled, disabled, or paused, and an "expired" note when an action is expired.

The status icons display next to the action's status in the security actions list and in the security action details page.

For information on security actions and security action statuses, see the [Security Actions customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/security-actions).

## September 18, 2025

Announcement

On September 18, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Improvements to the Abuse Detection incident model**

This release includes improvements to the incident model, including lower noise and higher accuracy for abuse detection incidents.

**Note: This feature is not currently available to customers with VPC-SC enabled.**

For information on abuse detection incidents, see the [Abuse Detection customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incidents).

## August 25, 2025

Announcement

On August 25, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Additional details and explanations for incidents and traffic identified as anomalous in Abuse Detection Advanced Anomaly Detection**

Starting with this release, additional details are available for anomalies detected in incidents and detected traffic, including details on why traffic was flagged as anomalous, the days and times it triggered, time series charts showing anomalous traffic spikes, and direct links to the Google Cloud Logging for events.

See the [Abuse detection "Details view"](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#details-view) for more information.

## August 11, 2025

Announcement

On August 11, 2025 we released an updated version of Advanced API Security Abuse Detection

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Improved performance when viewing IP address-specific details for abuse detection incidents**

With this release, the IP address detail information for abuse incidents displays more quickly for IP addresses with high traffic volumes, potentially reducing load times from minutes to seconds.

For usage information, see the [Abuse Detection incident detail documentation](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details).

## August 06, 2025

Announcement

On August 6, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Availability of Shadow API Discovery for APIs in any Google Cloud project**

Using Shadow API Discovery, you can find undocumented/shadow APIs in your existing cloud infrastructure. Shadow APIs pose a security risk to your system, since they might be unsecured, unmonitored, and unmaintained.

With this release, you can configure and run API observation jobs in any Google Cloud project, without needing to provision Apigee in that project. You can also centrally view the results of API observation jobs and compare discovered API endpoints and operations to APIs cataloged in API hub to identify shadow APIs.

See the [Shadow API Discovery overview](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery) for information on Shadow API Discovery and how to add it to projects.

**Note:** Data residency is not currently supported for Shadow API Discovery. See [data residency compatibility](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-compatibility).

## August 04, 2025

Announcement

On August 4, 2025 we announced new functionality in Advanced API Security Abuse Detection.

Feature

**Terraform support for configuring Advanced API Security**

We have expanded our Terraform support for Advanced API Security, enabling you to automate the management of your security posture. You can now use Terraform to manage add-on enablement for [Subscription](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_addons_config) and [PAYG](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_environment_addons_config) environments, create [Risk Assessment security profiles](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_profile_v2) and [monitoring conditions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_monitoring_condition), [configure IP address resolution](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_environment#client_ip_resolution_config-1), and [create security actions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_action).

For information, see [Configure Advanced API Security using Terraform](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#configure-advanced-api-security-using-terraform).

## July 14, 2025

Announcement

On July 14, 2025 we released an updated version of Advanced API Security 

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Support for editing and deleting security actions**

With this release you can edit and delete existing security actions using either the UI or the Apigee Management APIs.

For usage information, see the [security actions documentation](https://docs.cloud.google.com/apigee/docs/api-security/security-actions).

## July 01, 2025

Announcement

On July 1, 2025 we released a new version of Advanced API Security Abuse Detection.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Support for AppGroups in Abuse Detection attributes**

Abuse Detection incidents and detected traffic now show information on AppGroups and AppGroup apps when the AppGroup is part of the request or traffic.

**Note:** This functionality is not available in Apigee hybrid at this time.

For usage information, see the [Abuse Detection documentation](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details).

## June 16, 2025

Announcement

On June 16, 2025 we released a new version of Advanced API Security Abuse Detection.

Feature

**API address drill down details are now available in the preview release of Advanced API Security Abuse Detection incidents in the detected traffic tab.**

This new functionality shows details related to specific API addresses when viewing detected abuse in detected traffic.

For usage information, see the [Abuse Detection customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details) for incident details.

## June 04, 2025

Announcement

On June 4, 2025 we released an update to the Anomaly Detection model in Advanced API Security Abuse Detection.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**New model for Abuse Detection's Advanced Anomaly Detection rule**

With this release, we introduced a new and improved machine learning model for anomaly detection in Advanced API Security. This new model includes the following improvements:

  * **Trained on customer-specific traffic patterns.** The new model is trained exclusively on your organization's historical API traffic data. It continues to learn from your API traffic patterns over time to increase accuracy.
  * **Engineered by Google for anomaly detection.** The new model is a custom Vertex AI-based machine learning model, engineered and also used internally by Google specifically to detect anomalies in traffic patterns.



Usage requirements:

  * In order to use this new model, you must explicitly opt in to allow the model to use your traffic and other data to train for anomaly detection. Note that your data is never shared with other customers for training purposes.
  * The new model is not available for VPC-SC customers at this time.



The new anomaly detection model replaces the old model, with no customer-facing changes to the API or UI. Upon opting in for model training, you can expect to start seeing detected anomalies within 6 hours. If you have already opted in to allow the older version of our anomaly detection model to use your traffic data for training, you will not need to opt in again.

For more information on this model and on Abuse Detection, see [Abuse Detection customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection), including [Detection rules](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules).

## May 27, 2025

Announcement

On May 27, 2025 we released an updated version of Apigee Advanced API Security.

Feature

With this release, Advanced API Security expands its runtime region support to include `africa-south1` (Johannesburg).

For a list of supported regions, see [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

## May 20, 2025

Announcement

On May 20, 2025 we released a new version of Advanced API Security Abuse Detection.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Advanced API Security Abuse Detection incident reports now include the ability to view raw data**

With this new functionality, you can view raw data underlying an incident report, including client IP address, API proxy, developer app, and other attributes.

For usage information, see the [Abuse Detection customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details).

## March 25, 2025

Announcement

On March 25, 2025 we released an updated version of Advanced API Security.

Announcement

**Risk Assessment v2 is now the default Risk Assessment version**

Starting with this release, Risk Assessment v2 is the default Risk Assessment version in the UI. You will see the see v2 functionality and interfaces unless you choose to switch back to v1 by clicking **Switch to v1** in the upper right of the UI.

**Note:** Rollouts of this functionality to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Change

**New Advanced API Security support when using data residency (DRZ) with Apigee hybrid**

Advanced API Security is now available for Apigee hybrid orgs using DRZ, for hybrid versions 1.14.0 and later. See [Using data residency with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/latest/using-data-residency-with-apigee-hybrid).

See [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-and-apigee-hybrid) for information on DRZ and Advanced API Security support across organization types.

Feature

**New features added to public preview of Risk Assessment v2**

This release introduces new features to the Risk Assessment v2 preview:

  * **Security monitoring conditions.** Security monitoring conditions allow you to map resources (proxies or environments) to security profiles. Cloud Monitoring can then use this mapping to alert or create dedicated dashboards so that you can track security scores over time.
  * **Alerts on security monitoring conditions.** Once you've created a monitoring condition, you can set up alerts using Alerting in Cloud Monitoring so that you're notified when the security scores change.



For information on monitoring conditions features and usage see [monitoring conditions and alerts](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#monitoring-conditions). For usage information and a list of all features in Risk Assessment v2, see the [Risk Assessment v2 customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#risk-assessment-v2).

**Note:** Rollouts of this functionality to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

## March 07, 2025

Announcement

On March 7, 2025 we released an updated version of Apigee Advanced API Security.

Feature

**Availability of data obfuscation support with Advanced API Security**

With this release, data obfuscation can be used with Advanced API Security. 

For usage information, see [Obfuscate user data for Apigee API Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/obfuscate-user-data-for-analytics) and [Data obfuscation with Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security#data-obfuscation-with-advanced-api-security).

## January 13, 2025

Announcement

On January 13, 2025 we released an updated version of Apigee's Shadow API Discovery.

Feature

**Shadow API Discovery latency improvements**

This release improves Shadow API Discovery and removes the latency impact on load balancers previously documented as part of Shadow API Discovery enablement.

For more information on Shadow API Discovery, see the [Shadow API Discovery customer documentation](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery).

## January 07, 2025

Announcement

On January 7, 2024 we released a new version of Advanced API Security Abuse Detection.

**Note:** Rollouts of this release to production instances have begun and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**API key drill down details are now available in the preview release of Advanced API Security Abuse Detection incidents.**

This new functionality allows viewing details of detected abuse by the API key used to access the API.

For usage information, see the [Abuse Detection customer documentation for incident details](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details).

## January 06, 2025

Announcement

On January 6, 2025 we released an updated version of Advanced API Security.

Feature

**UI support for environment-level client IP address resolution**

This release introduces the ability to view the client IP address resolution setting for an environment in the Apigee Console.

For more information and usage instructions, see the [Client IP resolution customer documentation](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution).

## December 20, 2024

Announcement

On December 20, 2024 we released an updated version of Apigee.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Support for environment-level client IP address resolution**

This release introduces the ability to specify, per environment, how to capture the client IP address on API requests from the X-Forwarded-For header. When configured for the environment, the specified client IP address is used to apply security actions, populate the `ax_resolved_client_ip` Analytics variable and the new `client.resolved.ip` flow variable. The new configuration option can be used to specify the request IP address used in Advanced API Security.

This functionality is not available in Apigee hybrid at this time.

For more information and usage instructions, see the [Client IP resolution customer documentation](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution), [Analytics dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions), and [client flow variable](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#client).

## November 14, 2024

Announcement

On November 14, 2024 we released a new version of Advanced API Security

Feature

**IP address drill down details are now available in the preview release of Advanced API Security Abuse Detection Incidents.**

This new functionality allows viewing details of detected abuse by source IP.

For usage information, see the [Abuse Detection customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details).

## October 08, 2024

Announcement

On October 8, 2024 we released an updated version of Advanced API Security.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**New features added to the Risk Assessment v2 preview**

This release introduces new features to the Risk Assessment v2 [preview](https://cloud.google.com/products/#product-launch-stages):

  * **Support for custom security profiles.** You can create your own security profiles, with unique combinations of risk assessment checks and weights, to use for proxy risk assessment.
  * **New assessment checks.** We've added additional checks you can use when assessing proxy risk.
  * **Assess proxies across multiple profiles.** You can now switch between security profiles to see differences in scoring across profiles.



For usage information and a list of all features in Risk Assessment v2, see the [Risk Assessment v2 customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#risk-assessment-v2).

## October 04, 2024

Announcement

**On October 4, 2024 we released an updated version of Advanced API Security.**

Change

**Fixed:** Delay in score generation for Risk Assessment v2 with VPC-SC-enabled organizations only

In Risk Assessment v2, which is in [preview](https://cloud.google.com/products/#product-launch-stages), this issue has been resolved: 

With VPC-SC-enabled organizations only, when generating scores for new organizations or scoring changes to included proxies, shared flows, and target server configurations, score generation could have take as much as three hours.

See the [Risk Assessment v2 customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#risk-assessment-v2) for information on the functionality.

Change

Risk Assessment v2 is now available in the `me-central2` region. See [Available Apigee API Analytics Regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions) for region information.

## September 11, 2024

Issue

**Delay in score generation for Risk Assessment v2 with VPC-SC-enabled organizations only**

This issue impacts Risk Assessment v2 only, which is in [preview](https://cloud.google.com/products/#product-launch-stages).

_With VPC-SC-enabled organizations only,_ when generating scores for new organizations or scoring changes to included proxies, shared flows, and target server configurations, score generation could take as much as three hours.

See the [Risk Assessment v2 customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#risk-assessment-v2) for information on the functionality.

## September 10, 2024

Announcement

On September 10, 2024 we released an updated version of Advanced API Security.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Proxy-specific security actions**

You can now create security actions that apply only to one or more specified proxies.

This new functionality is not available with Apigee hybrid at this time.

See [Security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) to learn more about proxy-specific security actions.

## August 13, 2024

Announcement

On August 13, 2024 we released an updated version of Advanced API Security.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

**Note:** This functionality is not available in the `me-central2` region at this time. See [Available Apigee API Analytics Regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions) for region information. We will announce with a release note when that region is supported.

Feature

**Public preview of Risk Assessment v2**

This release introduces Risk Assessment v2 in [preview](https://cloud.google.com/products/#product-launch-stages). Risk Assessment v2 includes these improvements:

  * Improved reliability: Faster score calculations with recent proxy data.
  * Simplified score display: The new score is a percentage, where 100% means full alignment with the security profile.



For usage information and a list of all improvements and changes in v2, see [Risk Assessment v2](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#risk-assessment-v2).

## August 05, 2024

Announcement

On August 5, 2024 we released an updated version of Advanced API Security.

Feature

Shadow API Discovery, which is in [preview](https://cloud.google.com/products/#product-launch-stages), now supports the use of tags to label and organize observation results.

For usage information, see [Use tags](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery#use-tags).

## August 02, 2024

Announcement

The preview release of generative AI summaries and recommendations for Advanced API Security Abuse Detection incidents is now re-enabled after resolution of the known issue noted on [July 19](https://docs.cloud.google.com/apigee/docs/api-security/release-notes#July_19_2024).

For usage instructions, see the [Incident details](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details) documentation.

## July 26, 2024

Feature

Advanced API Security now supports data residency. Data residency meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Advanced API Security data is stored. For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

Announcement

On July 26, 2024, we released an updated version of Advanced API Security.

## July 19, 2024

Announcement

The preview release of generative AI summaries and recommendations for Advanced API Security Abuse Detection incidents has been temporarily disabled due to a known issue. We will announce in a release note when the functionality is re-enabled.

## June 27, 2024

Announcement

On June 27, 2024 we released a new version of Advanced API Security

Rollouts of this feature are ongoing and will take multiple days to complete across all Google Cloud zones. You might not be able to use the functionality until the rollout is complete.

Feature

**Preview release of generative AI incident report summaries**

This release introduces the [preview](https://cloud.google.com/products/#product-launch-stages) release of generative AI summaries and recommendations for Advanced API Security Abuse Detection incidents. The new generative AI features are available for all Advanced API Security-enabled projects and do not require the Gemini Code Assist add-on.

For usage information, see the [Abuse Detection customer documentation](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details).

## June 17, 2024

Announcement

On June 17, 2024 we released an updated version of Advanced API Security.

Feature

Shadow API Discovery, which is in [preview](https://cloud.google.com/products/#product-launch-stages), no longer requires separate creation of P4SA permissions in order to enable the functionality.

For usage information, see the [Shadow API Discovery documentation](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery).

## May 29, 2024

Announcement

On May 29, 2024 we released a new version of Advanced API Security

NOTE: Rollouts of this feature are ongoing and will take multiple days to complete across all Google Cloud zones. You might not be able to use the functionality until the rollout is complete.

Feature

**Preview release of Shadow API Discovery**

This release introduces Shadow API Discovery in [preview](https://cloud.google.com/products/#product-launch-stages). Shadow API Discovery finds shadow APIs (also known as undocumented or unmanaged APIs) in your existing cloud infrastructure. Shadow APIs pose a security risk to your system, since they might be unsecured, unmonitored, and unmaintained. 

For a feature overview and usage information, see [Shadow API Discovery](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery).

## May 14, 2024

Announcement

On May 14, 2024 we released an updated version of Advanced API Security.

NOTE: Rollouts of this feature are ongoing and will take multiple days to complete across all Google Cloud zones. You may not be able to use the functionality until the rollout is complete.

Feature

**Addition of autonomous system numbers (ASN), HTTP methods, and region codes as supported security action rule condition types.**

This new functionality is not available with Apigee hybrid at this time.

See [Create a security action](https://docs.cloud.google.com/apigee/docs/api-security/security-actions#create-a-security-action) to learn more.

## May 09, 2024

Announcement

On May 9, 2024 we released an updated version of Advanced API Security.

Feature

**Addition of CIDR range support when specifying IPv4 addresses for security action rules.**

Apigee Advanced API Security now includes support for CIDR range specification when creating security action rules that restrict access based on IP addresses.

This new functionality is not available with Apigee hybrid at this time.

See [Create a security action](https://docs.cloud.google.com/apigee/docs/api-security/security-actions#create-a-security-action) to learn more.

## March 04, 2024

Announcement

On March 4, 2024 we released an updated version of Advanced API Security.

Feature

**New conditions for security actions**

You can now create [security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) based on the following condition types (in addition to the condition types for Detection rules and IP addresses that were already available):

  * API keys
  * API products
  * Access tokens
  * Developers
  * Developer apps
  * User agents



**These new conditions are not available with Apigee hybrid at this time.**

See [Create a security action](https://docs.cloud.google.com/apigee/docs/api-security/security-actions#create-a-security-action) to learn more.

## January 16, 2024

Announcement

On January 16, 2024 we released an updated version of Advanced API Security.

Feature

**Training machine learning models for abuse detection on your data**

You now have the option to allow Apigee to [train your organization's machine learning models for abuse detection on your data](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#help-improve-your-machine-learning-models-for-abuse-detection). Training the models on your data helps improve their accuracy for detecting security incidents.

## December 13, 2023

Announcement

On December 13, 2023 we released an updated version of Advanced API Security.

Feature

**Performance improvements to Risk Assessment security scores**

Risk Assessment [security scores](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#security-scores) now load faster in the Apigee UI, due to improved server side caching of scores.

Feature

**Public preview of archiving security incidents**

With this release, you can now [archive security incidents](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#archive-incidents) that you no longer want to see displayed in the [incidents list](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#environment-details). For example, you might want to archive incidents that you have already dealt with and no longer need to track. Archiving incidents can help you focus on those incidents that still require your attention. Archiving does not delete the incident: you can always unarchive it whenever you want.

## December 06, 2023

Announcement

On December 6, 2023 we released an updated version of Advanced API Security.

Feature

**New button to create a security action is now in several places in the Abuse detection and Risk assessment pages**

The new button links directly to the Security actions page from the Abuse detection or Risk assessment pages, so you can easily create a [security action](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) for the environment you are currently viewing. The button is in the following locations:

  * The Source assessment view in the Risk assessment page
  * The Detected Traffic, Incident, and Incident details views in the Abuse detection page



## December 05, 2023

Announcement

On December 5, 2023 we released an updated version of Advanced API Security.

Change

**Changes to proxy security scores**

The following changes have been made to the way proxy security scores are calculated:

  * Previously, adding a policy to a proxy or shared flow, but not attaching the policy to any flow (preflow, postflow or conditional flow), could affect the proxy's score.

With this release, you must attach a policy in a flow in order for the policy to affect the proxy's score. A policy that is not attached in a flow is treated as if no policy were present for scoring.

  * Previously, proxies with no policies were not considered in scoring.

With this release, proxies with no policies _are_ considered in scoring.




See [How policies affect proxy security scores](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#how-policies-affect-proxy-security-scores) to learn more.

## November 01, 2023

Announcement

On December 6, 2024 we release an updated version of Advanced API Security.

Feature

**Public preview of Advanced API Security custom profiles in the Apigee UI**

With this release, you can now create and edit [custom security profiles](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#create-and-edit-security-profiles) in the Apigee UI. Custom profiles let you specify the security categories that your security scores are based on.

The Security scores page in the Apigee UI has been renamed to the [Risk assessment](https://docs.cloud.google.com/apigee/docs/api-security/security-scores) page, and the page now has tabs for security scores and security profiles.

## October 06, 2023

Announcement

On October 6, 2023, we released an updated version of Advanced API Security.

Feature

**Public Preview of Advanced API Security Actions**

Advanced API Security's new [Security Actions](https://cloud.google.com/apigee/docs/api-security/security-actions) feature lets you create security actions that define how Apigee handles detected traffic. You can create the following security actions:

  * _Deny_ actions, which deny requests that meet specified conditions, for example, originating at an IP address that has been identified as a source of abuse. 

  * _Flag_ actions, which let requests pass through, but add headers to requests to identify them as suspicious.

  * _Allow_ actions, which are used to override deny actions in specific cases when the request is trusted.


**Note:** At the present time, Security Actions is only available for Apigee, but not for Apigee hybrid.

## September 27, 2023

Announcement

On September 27, 2023, we released an updated version of Advanced API Security.

Feature

**Public preview of Advanced API Security Alerting**

Advanced API Security's new [alerting feature](https://docs.cloud.google.com/apigee/docs/api-security/security-alerts) lets you create alerts for events related to API security using Google Cloud Monitoring, such as changes to your security scores or incidents involving detected API abuse. You can configure alerts to send you notifications by email or other channels when these events occur, so you can take action to counteract them.

## September 25, 2023

Announcement

On September 25, 2023 we release an updated version of Advanced API Security.

**Note:** Rollouts of this release to production instances may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Change

If a flow hook contains any [FlowCallout](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy) policies, Advanced API Security scores now processes all policies from the shared flows that the flow callouts are pointing to for scoring. Further callout chaining is not supported.

Fixed

Bug ID | Description  
---|---  
300849647 | Fixed a bug in Security scores for proxies that don't contain any policies in the categories authorization, mediation, threat or CORS .  
  
## August 25, 2023

Announcement

On August 25, 2023, we released an updated version of Apigee Advanced API Security.

Feature

This release includes [custom profiles](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#custom-security-profile) for Advanced API Security scores. Custom profiles let you specify the security categories you want your security scores to be based on. In this release, you must create a security profile in the [security scores API](https://docs.cloud.google.com/apigee/docs/api-security/security-scores-api#use-a-custom-security-profile). However, you can view scores for the profile in the [security scores UI](https://docs.cloud.google.com/apigee/docs/api-security/security-scores).

## August 03, 2023

Announcement

On August 3, 2023, we released an updated version of Apigee Advanced API Security.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Change

Previously, [Advanced API Security scores](https://cloud.google.com/apigee/docs/api-security/security-scores) didn't evaluate proxies calling shared flows via flow hooks and the [FlowCallout](https://cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy) policy in the proxy. With this release, security scores take into account proxies calling shared flows this way. As a result, your security scores may change because they now factor in the shared flows in the environment.

## April 20, 2023

Announcement

On April 20, 2023 we released an updated version of Apigee Advanced API Security.

Feature

This release contains a new Advanced API Security [**Detected Traffic**](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#detected-traffic) view, which displays information about API traffic originating from detected bots. This information was previously displayed in the **Abuse metrics** section of the **Security scores** view.

## March 23, 2023

Announcement

On March 23, 2023, we released an updated version of Apigee Advanced API Security.

Issue

The two new detection rules, Advanced Anomaly Detection and Advanced API Scraper, are not available for organizations with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls). We are actively working to resolve this issue.

Feature

**Public preview release of Advanced API Security abuse detection**

Advanced API Security's new [abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection) feature lets you view security incidents involving your APIs. Abuse detection uses Google's machine learning algorithms to detect API traffic patterns that are a sign of malicious activity targeting your APIs.

Abuse detection includes two new types of detection rules powered by machine learning models:

  * Advanced Anomaly Detection: Detects unusual patterns of API traffic.
  * Advanced API scraper: Detects attempts to extract information from APIs for malicious purposes.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
