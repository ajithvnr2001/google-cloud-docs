---
url: https://docs.cloud.google.com/vpc-service-controls/docs/release-notes/
title: VPC Service Controls release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:40:55.724805+00:00
---

# VPC Service Controls release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Resources ](https://docs.cloud.google.com/vpc-service-controls/docs/resources)



Send feedback 

#  VPC Service Controls release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to VPC Service Controls. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/vpc-sc-release-notes.xml) directly. 

## October 14, 2026

Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages))**: Support for using Workload Identity Federation for GKE in ingress and egress rules to allow access to resources protected by a service perimeter is available in Preview.

You can specify the following Workload Identity Federation for GKE principals in ingress and egress rules:

  * All GKE Pods that use a Kubernetes service account (by service account name or ID)
  * All GKE Pods in a Kubernetes namespace
  * All GKE Pods in a cluster



For more information, see [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups) and [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

## October 08, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Cloud Storage for Firebase](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firebase_cloud_storage)



Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages))**: Support for automated remediation suggestions is available in the VPC Service Controls violation analyzer.

Remediation suggestions analyze access denial events and generate actionable, narrowly scoped configuration changes to resolve perimeter denials and adhere to the principle of least privilege. The remediation engine can automatically propose ingress rules, egress rules, VPC accessible services updates, and existing or new context-aware access levels.

For more information, see [Resolve access denials with remediation suggestions](https://docs.cloud.google.com/vpc-service-controls/docs/remediation-suggestions).

## September 30, 2026

Feature

**VPC Service Controls feature:** Support for using Google Cloud folders and organizations as resources in ingress and egress rules is [generally available](https://cloud.google.com/products#product-launch-stages).

With this update, you can create rules that allow access to and from the resources protected by service perimeters and bypass common resource size limitations.

For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

Feature

**VPC Service Controls feature** : Folder membership support in VPC Service Controls service perimeters is [generally available](https://cloud.google.com/products#product-launch-stages). You can configure Google Cloud folders as members in service perimeters to automatically protect all projects and subfolders within that folder hierarchy.

For more information, see [Folder support in service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/folder-membership) and [Configure folders in service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/configure-folder).

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Universal Ledger](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_universal_ledger)



## September 08, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Observability API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_observability_api)



## September 03, 2026

Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages))**: VPC Service Controls supports retrieving and updating service perimeters that contain deleted IAM principals. When you enable this feature, you can manage perimeters that contain deleted user, group, or service account identities without triggering the `The email address is invalid or non-existent` error.

For more information, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities#deleted-principals).

## August 26, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Cloud FTP](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_ftp)



## August 14, 2026

Feature

[Generally available (GA)](https://cloud.google.com/products#product-launch-stages) support for the following integrations:

  * [Agent Identity API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_agent_identity)
  * [Agent Identity Credentials API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_agent_identity_credentials)



Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/vpc-service-controls)



## August 13, 2026

Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages)):** Support for optimizing service perimeters using the VPC Service Controls recommender is available.

The recommender detects architectural risks and perimeter misconfigurations, including the following:

  * **Critical resources at risk of exfiltration** : Identifies active and sensitive services (such as BigQuery and Cloud Storage) operating outside service perimeters.

  * **Unconfigured VPC accessible services** : Identifies perimeters that leave APIs unrestricted from within the security boundary.

  * **Misconfigured VPC accessible services** : Identifies mismatches between allowed accessible APIs and restricted services inside a perimeter.




For more information, see [Optimize perimeters with recommender](https://docs.cloud.google.com/vpc-service-controls/docs/recommender).

## August 06, 2026

Feature

**VPC Service Controls feature:** The VPC Service Controls service patterns feature is [generally available](https://cloud.google.com/products#product-launch-stages). You can use service patterns to explicitly configure which Google APIs (both supported and unsupported) can be accessed from VPC networks within a service perimeter when using the private VIP (`private.googleapis.com`) or a Private Service Connect endpoint with the `all-apis` bundle.

For more information, see [VPC Service Controls service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services#service-patterns).

## August 04, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Gemini Cloud Assist](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_assist)



## August 03, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Antigravity in Gemini Enterprise](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gemini_enterprise_antigravity)



## June 30, 2026

Feature

**VPC Service Controls feature** : Support for specifying Private Service Connect endpoints in service perimeters is [generally available](https://cloud.google.com/products#product-launch-stages). This feature lets you configure Private Service Connect endpoints in ingress and egress rules to enable communication using internal IP addresses.

For more information, see [Configure Private Service Connect endpoints in service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/psc-endpoint).

## June 29, 2026

Feature

**VPC Service Controls feature:** Support for using the following identities in ingress and egress rules to allow access to resources protected by a service perimeter is [generally available](https://cloud.google.com/products#product-launch-stages):

  * Agent identities
  * SPIFFE formats for third-party workforce and workload identities



For more information, see [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups) and [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

## June 24, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Conversational Analytics API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_conversational_analytics)



## June 06, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Firebase Phone Number Verification](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firebase_phone_number_verification)



## June 03, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Workload Identity API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_workloadidentity)



## May 13, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Firebase Phone Number Verification](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firebase_phone_number_verification)



## May 04, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Cloud Network Insights](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_network_insights)



## April 30, 2026

Feature

**VPC Service Controls feature:** Support for using IAM roles in ingress and egress rules to allow access to resources protected by a service perimeter is [generally available](https://cloud.google.com/products#product-launch-stages). This feature includes the following updates:

  * You can use the [`gcloud access-context-manager supported-permissions describe`](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#check-role) command to check the support status of an IAM role.

  * You can use the [`gcloud access-context-manager supported-permissions list`](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#list-permissions) command to retrieve the complete list of all supported permissions.




For more information, see [Configure IAM roles in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles).

## April 22, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [App Topology](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_app_topology)



Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Agent Registry](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_agent_registry)



## April 01, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Cluster Director](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cluster_director)



## March 26, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Oracle Database@Google Cloud](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_oracle_database)



## March 25, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [App Lifecycle Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_saasservicemgmt)



## March 23, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Oracle Database@Google Cloud](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_oracle_database)



## March 16, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [CX Agent Studio](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cx_agent_studio)



Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages)):** VPC Service Controls supports the following identities in ingress and egress rules to allow access to resources protected by a service perimeter:

  * Agent identities

  * SPIFFE formats for third-party workforce and workload identities




This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

## March 10, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Managed Lustre](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_managed_lustre)



## February 25, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Security Operations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_secops)



## February 17, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Vector Search 2.0](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_vector_search_2)



## February 11, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Managed Lustre](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_managed_lustre)



## February 04, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [CX Agent Studio](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cx_agent_studio)



## February 03, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Distributed Cloud Edge Container API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#edgecontainer)



## January 22, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Privileged Access Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_pam)



## January 13, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Cloud Location Finder](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_location_finder)



## January 09, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Model Armor](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_model_armor)



## January 08, 2026

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Gemini Cloud Assist](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_assist)



## January 07, 2026

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Unified Maintenance](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_unified_maint)



## December 20, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Firebase App Hosting](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firebase_app_hosting)



## December 15, 2025

Feature

**VPC Service Controls feature:** The VPC Service Controls violation analyzer is [generally available](https://cloud.google.com/products#product-launch-stages). You can use the violation analyzer to diagnose access denial events and generate comprehensive evaluation reports to help resolve the denial events.

The violation analyzer includes the following capabilities and updates:

  * You can use a denial event's unique ID to generate a comprehensive evaluation report.
  * Edit ingress and egress rules of a selected perimeter directly from the troubleshooting results page.
  * View log entry details associated with a denial event directly on the troubleshooting results page.
  * A few previous [limitations](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer#limitations) in the violation analyzer have been removed.
  * You don't need to enable the `Policy Troubleshooter API` to use the violation analyzer.



For more information, see [Diagnose an access denial in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).

## December 08, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Firebase App Hosting](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firebase_app_hosting)



## December 05, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [App Design Center](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_app_design_center)



## November 24, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Unified Maintenance](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_unified_maint)



## November 19, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Address Validation](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_address_validation)



## November 13, 2025

Change

Updated the limitations for the following integration in the [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) page:

  * [Policy Simulator](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iam_policy_simulator): simulations on organization and folder resources are not protected by VPC Service Controls.



## October 01, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Vertex AI Agent Engine](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_agent_engine)



## September 23, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Telemetry API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_telemetry)



Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_managed_kafka)



## September 18, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Personalized Service Health](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_service_health)



## September 03, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_managed_kafka)



## August 18, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Secure Web Proxy](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_swp)



## August 14, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [License Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_license_manager)



## August 06, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [FleetPackage API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_fleetpackage)



## August 04, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Backup for GKE](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gkebackup)



## August 01, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Eventarc Advanced](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_eventarc_advanced)



## July 31, 2025

Feature

**VPC Service Controls feature:** The VPC Service Controls violation dashboard is [generally available](https://cloud.google.com/products#product-launch-stages). This dashboard provides an aggregated view of all access denials by service perimeters in your organization.

  * The following charts are added to the dashboard: 
    * Violation count
    * Top violations by access policy
  * While creating a new log bucket during the dashboard setup, you can now select the region and retention period.



For more information, see [Set up and view the violation dashboard](https://docs.cloud.google.com/vpc-service-controls/docs/violation-dashboard).

## July 24, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [License Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_license_manager)



## July 14, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Address Validation API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_address_validation)

  * [Places (New) API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_places_new)




## July 08, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Firebase Crashlytics](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firebase_crashlytics)



## July 07, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Apigee API hub](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_api_hub)



## June 30, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [`FleetPackage` API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_fleetpackage)



## June 26, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Parameter Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_parameter_manager)



## May 22, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Model Armor](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_model_armor)



## May 19, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Storage batch operations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_storage_batch_operations)



## May 17, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Assured Open Source Software](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_assured_oss_name)



## April 29, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Apigee API hub](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_api_hub)



Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Secure Web Proxy](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_swp)



## April 25, 2025

Change

Updated the limitations for the following integration in the [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) page:

  * [Firestore](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firestore): using Firestore Enterprise edition with restricted VIP requires adding IP ranges to an allowlist.



## April 23, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Service Usage](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_usage)



## April 22, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Agent Assist](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_agent_assist)



## April 09, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Database Center](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_database_center_api)



## April 02, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Agentspace Enterprise](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gemini_enterprise)



## March 28, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Storage Intelligence API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_storage)



Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages)):** VPC Service Controls adds support for using IAM roles in ingress and egress rules to allow access to resources protected by service perimeters. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Configure IAM roles in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles).

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Firebase Data Connect](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firebase_data_connect)



## March 27, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Service Networking](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_service_networking)



## March 25, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Telemetry (OTLP) API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_telemetry)



## March 24, 2025

Change

The [Dialogflow](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dialogflow) entry has been corrected to reflect that the Dialogflow integration with VPC Service Controls is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

The integration of Dialogflow with VPC Service Controls has been [generally available](https://cloud.google.com/products#product-launch-stages) since January 29, 2021.

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Parameter Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_parameter_manager)



## March 21, 2025

Feature

VPC Service Controls now supports custom organization policies. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Create custom constraints for VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/custom-constraints).

## February 27, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Service Usage](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_usage)



## February 24, 2025

Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages)):** The VPC Service Controls violation analyzer lets you diagnose access denial events for services in your perimeters using an encrypted troubleshooting token generated by VPC Service Controls. The violation analyzer also provides troubleshooting results that can help you understand and resolve the access denial events. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Diagnose an access denial event using the VPC Service Controls violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).

## February 18, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Agentspace Enterprise](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gemini_enterprise)



Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [NotebookLM Enterprise](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_notebooklm_enterprise)



## February 14, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Database Insights API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_database_insights_api)



Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages)):** The VPC Service Controls violation dashboard provides an aggregated view of all access denials by service perimeters in your organization. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Set up and view the violation dashboard](https://docs.cloud.google.com/vpc-service-controls/docs/violation-dashboard).

## February 10, 2025

Feature

**VPC Service Controls feature:** Support for using third-party identities (both single identities and groups) in the ingress and egress rules to allow access to resources protected by a service perimeter is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups).

## February 07, 2025

Feature

**VPC Service Controls feature:** Support for adding projects as a source in the egress rules of a service perimeter is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

Feature

**VPC Service Controls feature:** Support for adding titles in the ingress and egress rules of a service perimeter is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

## January 31, 2025

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Autoscaling](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_autoscaling)



## January 10, 2025

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Database Insights API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_database_insights_api)



## December 16, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Memorystore for Valkey](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_memorystore_for_valkey)



## December 11, 2024

Feature

**VPC Service Controls feature:** Support for using identity groups in the ingress and egress rules to allow access to resources protected by a service perimeter is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups).

## November 20, 2024

Feature

**VPC Service Controls feature:** VPC Service Controls extends support for etags in the [service perimeter resources](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters). For example, you can use the `--etag` flag with the gcloud CLI commands such as `gcloud access-context-manager perimeters update` and `gcloud access-context-manager perimeters describe`. This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

## November 15, 2024

Feature

**VPC Service Controls feature (Status:[Preview](https://cloud.google.com/products#product-launch-stages)):** VPC Service Controls adds support for using groups of third-party identities in ingress and egress rules to allow access to resources protected by service perimeters. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups).

## October 21, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Vertex AI in Firebase](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_vertex_ai_in_firebase)



## October 18, 2024

Fixed

Updated the correct support status for the following integration in the [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) page:

  * [Dialogflow](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dialogflow) is in [Preview stage](https://cloud.google.com/products#product-launch-stages).



_This note is incorrect; see entry forMarch 24, 2025_

## October 15, 2024

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Audit Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_audit_manager)



## September 19, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Cloud Contact Center as a Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_ccaip_name)



## September 11, 2024

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Privileged Access Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_pam)



## August 30, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Cloud VMware Engine](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_vmware_engine)



## August 21, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Workload Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_workload_manager)



## August 20, 2024

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Contact Center AI Platform](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_ccaip_name)



## July 31, 2024

Feature

**VPC Service Controls feature:** VPC Service Controls supports using identity groups and third-party identities (only single identities) in ingress and egress rules to allow access to resources protected by service perimeters. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups). You can also learn an [example of using identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/identity-groups-examples).

## July 17, 2024

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Commerce Org Governance API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_org_governance)



## July 02, 2024

Feature

**VPC Service Controls feature:** Support to programmatically [retrieve the list of services](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#list-services) that are supported by VPC Service Controls is [generally available](https://cloud.google.com/products#product-launch-stages). Using this feature, you also can [retrieve the list of methods and permissions](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#list-methods) supported by VPC Service Controls for a service.

  * The following changes are made in the output of the `gcloud access-context-manager supported-services list` command: 
    * The field name `SUPPORT_STAGE` is changed into `SERVICE_SUPPORT_STAGE`.
    * The status `BETA` is changed into `PREVIEW` in the `SERVICE_SUPPORT_STAGE` field.
    * A new status `DEPRECATED` is added in the `SERVICE_SUPPORT_STAGE` field.
  * The field name `supportStage` is changed into `serviceSupportStage` in the output of the `gcloud access-context-manager supported-services describe` command.



## June 27, 2024

Feature

**VPC Service Controls feature:** Support for using an internal IP address to allow access to protected resources is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Allow access to protected resources from an internal IP address](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access). Make sure that you read the updated [Limitations](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access#limitations) section before using this feature.

## May 29, 2024

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * Kubernetes Metadata API



For more information, see [Anthos On-Prem API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_anthos_on_prem_api), [Google Kubernetes Engine](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gke), and [GKE Multi-Cloud](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_anthos_multicloud).

## May 23, 2024

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Workload Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_workload_manager)



## May 22, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Sovereign Controls by Partners](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_controls_partner)



## April 29, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Backup and DR Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_backupdr)



Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Cloud Quotas](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_quotas)



## April 10, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Secure Source Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_ssm)



Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [API keys](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_api_keys)



## April 08, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Migration Center](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_migration_center)



## March 21, 2024

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Sovereign Controls by Partners](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_controls_partner)



## March 19, 2024

Feature

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Cloud Code](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_code)



Announcement

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [App Hub](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_app_hub)



## March 14, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Earth Engine](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_earthengine)



Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [API keys](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_api_keys)



## March 07, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Storage Insights](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_storage_insights)



## March 01, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Google Cloud Serverless for Apache Spark](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dataproc_serverless) (formerly known as Dataproc Serverless)



## February 27, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Colab Enterprise](https://docs.cloud.google.com/colab/docs/service-controls)



Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Infrastructure Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_infrastructure_manager)



Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Earth Engine](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_earthengine)



## February 21, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Dataform](https://docs.cloud.google.com/dataform/docs/vpc-service-controls)



## February 14, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Security Command Center](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_security_command_center)



## February 08, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Web Security Scanner](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_scanner_name)



## January 31, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Blockchain Node Engine](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_blockchainnodeengine)



## January 26, 2024

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Parallelstore](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_parallelstore)



## January 17, 2024

Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Personalized Service Health](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_service_health)



Feature

The ability to programmatically retrieve the [list of services that are supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#list-services) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Using this feature, you can also retrieve the [list of methods and permissions supported by VPC Service Controls for a service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#list-methods).

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Integration Connectors](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_integration-connectors)



## December 16, 2023

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Microservices](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_microservices)



## December 06, 2023

Feature

The ability to [allow access to protected resources from an internal IP address](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 21, 2023

Announcement

[Preview stage](https://cloud.google.com/products#product-launch-stages) supported for the following integration:

  * [Web Security Scanner](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_scanner_name)



## November 20, 2023

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm#confidential-space)



## November 08, 2023

Announcement

[Preview stage](https://cloud.google.com/products#product-launch-stages) supported for the following integration:

  * [Security Command Center](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_security_command_center)



Announcement

[Preview stage](https://cloud.google.com/products#product-launch-stages) supported for the following integration:

  * [Confidential Space](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_confidential_space)



## November 01, 2023

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Duet AI in Google Cloud](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_duetai)



## September 28, 2023

Announcement

[Preview stage](https://cloud.google.com/products#product-launch-stages) supported for the following integration:

  * [Infrastructure Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_infrastructure_manager)



## September 13, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Serial console](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_serial_console)



## August 15, 2023

Announcement

General availability support for the following integration:

  * [NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



## August 14, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Backup and DR Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_backupdr)



## August 09, 2023

Change

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Certificate Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_certificate_manager)



Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration: 

  * [Generative AI App Builder - Enterprise Search](https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction)



## August 04, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Certificate Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_certificate_manager)



## July 19, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Integration Connectors](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_integration-connectors)



## July 18, 2023

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Batch](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_batch)



## July 12, 2023

Issue

The **Quota** page displays only the default quota limits and doesn't include any additional quotas provided by Google.

For information about VPC Service Controls quotas, see [Quotas and limits](https://cloud.google.com/vpc-service-controls/quotas).

## June 22, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Cloud Customer Care](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_support_name)



## June 20, 2023

Announcement

General availability for the following integration:

  * [Live Stream API](https://docs.cloud.google.com/livestream/docs/how-to/vpc/secure-pipeline)



## June 01, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration: 

  * [Storage Insights](https://cloud.google.com/storage/docs/insights/using-inventory-reports)



## May 08, 2023

Announcement

General availability for the following integration:

  * [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc)



## April 14, 2023

Change

VPC Service Controls support for Cloud Scheduler jobs with the following targets is now in [Preview](https://cloud.google.com/products#product-launch-stages):

  * Cloud Functions
  * Cloud Run
  * Dataflow API
  * Data Pipelines



To learn more, see the documentation on how to [secure cron jobs with VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc).

## April 10, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Looker (Google Cloud core)](https://cloud.google.com/looker/docs/looker-core)



## March 27, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Dataflow Data Pipelines](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_data_pipelines)



## March 23, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Resource Manager tags API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_crm)



## March 17, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [On-Demand Scanning API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_on-demand_scanning)



## March 10, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Public Certificate Authority](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_public_ca)



## February 22, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Visual Inspection AI](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_visual_inspection)



## February 17, 2023

Feature

The ability to [add individual VPC networks](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management) to a perimeter is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Previously, all VPC networks in a host project were added to a perimeter. You can now do the following:

  * Add individual VPC networks as members of a perimeter.
  * Create an ingress rule to authorize individual VPC networks to access a perimeter.



## February 10, 2023

Feature

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Policy Simulator](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iam_policy_simulator)



## January 26, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Identity Platform](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_identity_platform)



## January 24, 2023

Announcement

General availability for the following integration:

  * [BigQuery Data Policy API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_bigquerydatapolicy_api)



## January 19, 2023

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Essential Contacts](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_essential_contacts)



## January 09, 2023

Feature

Support for Cloud Tasks is now at [General Availability](https://cloud.google.com/products#product-launch-stages). To learn more, see the Cloud Tasks documentation on [setting up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/tasks/docs/use-vpc-service-controls).

## January 04, 2023

Feature

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Policy Troubleshooter](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iam_policy_troubleshooter)



## December 20, 2022

Feature

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Video Stitcher API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_video_stitcher)



## December 15, 2022

Feature

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Batch](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_batch)



## December 12, 2022

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Bare Metal Solution](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_baremetalsolution)



## December 05, 2022

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Cloud IDS](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_ids)
  * [Document AI Warehouse](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_docaiwarehouse)



## November 17, 2022

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Data Lineage API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_Data%20Lineage%20API)



## November 07, 2022

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Config Controller](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_config_controller)



## November 01, 2022

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [BigQuery Data Policy API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_bigquerydatapolicy_api)



## October 26, 2022

Feature

General availability for the following integration:

  * [Organization Policy Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_org_policy)



## October 11, 2022

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/configure-private-clusters)



## September 20, 2022

Feature

General availability for the following integration:

  * [Analytics Hub](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_analytics_hub_name)



## September 06, 2022

Change

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Organization Policy Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_org_policy)



## September 05, 2022

Announcement

General availability support for the following integration:

  * [Service Account Credentials API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_service_account_credentials)



## August 10, 2022

Announcement

General availability for the following integration:

  * [Web Risk](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_webrisk)



## August 08, 2022

Feature

Beta stage support for the following integration:

  * [Service Account Credentials API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_service_account_credentials)



## August 05, 2022

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Integration Platform](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_integration_platform)



## July 26, 2022

Feature

General availability for the following integration:

  * [BigQuery Reservation API](https://docs.cloud.google.com/bigquery/docs/reservations-tasks#add_bigquery_reservation_api_to_vpc_service_controls)



## June 30, 2022

Feature

Support to add individual VPC networks to a perimeter is now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

Previously, the entire VPC host project was added to a perimeter. VPC Service Controls now supports the following enhancements ([Preview](https://cloud.google.com/products/#product-launch-stages) release):

  * You can now add individual VPC networks as members of a perimeter.
  * You can create an ingress rule to authorize individual VPC networks to access a perimeter.



## June 24, 2022

Change

General Availability for the following integration:

[Security Token Service](https://docs.cloud.google.com/iam/docs/workload-identity-federation)

## June 08, 2022

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [AlloyDB](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_alloydb_api)



## June 07, 2022

Feature

General availability for the following integration:

  * [Migrate for Compute Engine](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/create-a-service-perimeter)



## June 01, 2022

Feature

General availability for the following integrations:

  * [Firestore](https://docs.cloud.google.com/firestore/docs/securing-with-vpc-sc)
  * [Firestore in Datastore mode](https://docs.cloud.google.com/datastore/docs/securing-with-vpc-sc)



## May 31, 2022

Feature

General availability for the following integration:

  * [Cloud Domains](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_domains)



## May 17, 2022

Feature

General availability for the following integration:

  * [Google Cloud Deploy](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_deploy)



## May 12, 2022

Feature

General availability for the following integration:

  * [Database Migration Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dms_name)



## May 04, 2022

Feature

[General availability](https://cloud.google.com/products#product-launch-stages) support for the following integration:

  * [Image streaming](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_image_streaming)



## March 31, 2022

Feature

General availability of scoped policies for VPC Service Controls.

To delegate administration of VPC Service Controls perimeters and access levels to folder-level and project-level administrators, you can use [scoped policies](https://docs.cloud.google.com/access-context-manager/docs/scoped-policies). You can create access policies that are scoped to specific folders or projects.

## March 28, 2022

Feature

General availability for the following integration:

  * [Transcoder API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_transcoder)



## March 24, 2022

Feature

General availability for the following integrations:

  * [Cloud Profiler](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_profiler)
  * [Cloud Monitoring](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_monitoring)



## March 17, 2022

Announcement

Preview stage support for the following integration:

  * [Web Risk](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_webrisk)



Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Migrate for Compute Engine](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/create-a-service-perimeter)



## March 08, 2022

Announcement

General availability for the following integration:

  * [Assured Workloads](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_assured_workloads_name)



## March 03, 2022

Announcement

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Workflows](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_workflows)



## February 16, 2022

Announcement

General availability for the following integration:

  * [Speaker ID](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_speakerid)



## February 01, 2022

Feature

[Preview](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Cloud Debugger](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_debugger)



Feature

General availability for the following integrations:

  * [Cloud TPU](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_tpu)



## January 28, 2022

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Cloud Monitoring](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_monitoring)



## January 19, 2022

Feature

[Preview](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Image streaming](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_image_streaming) for container images stored in Artifact Registry.



## January 12, 2022

Feature

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Firestore](https://docs.cloud.google.com/firestore/docs/securing-with-vpc-sc)
  * [Datastore](https://docs.cloud.google.com/datastore/docs/securing-with-vpc-sc)



## January 11, 2022

Announcement

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Google Cloud Deploy](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_deploy)



## December 06, 2021

Announcement

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Firebase Security Rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firebase_rules)



## November 23, 2021

Feature

General availability for the following integration: * [Connect Gateway](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_fleets)

Fleet-related APIs (GKE Hub, GKE Connect, Connect Gateway) are now grouped together.

## November 15, 2021

Feature

General availability for the following integration:

  * [Contact Center AI Insights](https://docs.cloud.google.com/contact-center/insights/docs)



## October 28, 2021

Announcement

General availability for the following integration:

  * [Eventarc](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_eventarc)



## October 20, 2021

Feature

General availability for the following integration:

  * [reCAPTCHA Enterprise](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_recaptcha_enterprise)



## October 18, 2021

Announcement

General availability for the following integration:

  * [Network Connectivity Center](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_network_connectivity_center)



## September 30, 2021

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Speaker ID](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_speakerid)



## September 29, 2021

Feature

General availability for the following integration: 

  * [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest)



## August 10, 2021

Feature

General availability for the following integration:

  * [Cloud DNS](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dns)



## July 30, 2021

Feature

General availability for the following integration:

  * [Filestore](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#filestore)



## July 27, 2021

Feature

Support for [Cloud Run](https://docs.cloud.google.com/run) is now at General Availability (GA).

## July 20, 2021

Announcement

[Preview stage support](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * Network Connectivity Center



## July 19, 2021

Announcement

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Eventarc](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_eventarc)



## July 09, 2021

Announcement

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Container Threat Detection](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_container_threat_detection)



## July 05, 2021

Announcement

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Traffic Director](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_td)



## July 02, 2021

Feature

General availability for the following integration:

  * [Certificate Authority Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cas)



## July 01, 2021

Announcement

[Preview stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Filestore](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#filestore)



## June 29, 2021

Feature

General availability for the following integration:

  * [Traffic Director](https://docs.cloud.google.com/traffic-director/docs/overview)



This note is incorrect; see entry for [July 5, 2021](https://docs.cloud.google.com/vpc-service-controls/docs/release-notes#July_05_2021)

## June 22, 2021

Feature

General availability for the following integration:

  * [Identity-Aware Proxy for TCP forwarding](https://docs.cloud.google.com/iap/docs/securing-tcp-with-vpc-sc)



## June 09, 2021

Feature

Integration with Document AI [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_documentai) is now generally available.

## May 24, 2021

Feature

General availability for the following integration:

  * [Retail API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_retail)



## May 06, 2021

Feature

General availability for the following integration:

  * [Memorystore for Memcached](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_memstore-memcache)



## May 05, 2021

Change

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Ads Data Hub](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_ads_data_hub)



## April 22, 2021

Feature

General Availability release of [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for VPC Service Controls.

## April 13, 2021

Feature

General availability for the following integration:

  * [VM Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_vm_manager)



## April 06, 2021

Feature

[Preview support](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * [Cloud Life Sciences](https://docs.cloud.google.com/life-sciences/docs)



## March 24, 2021

Feature

General availability for the following integration:

  * [OS Login](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_os_login)



## March 11, 2021

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Transcoder API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_transcoder)



## March 08, 2021

Feature

[Preview](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * [Memorystore for Memcached](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_memstore-memcache)



## February 16, 2021

Feature

Preview release of [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for VPC Service Controls.

## January 25, 2021

Feature

[Preview](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * [AI Platform (Unified)](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_aip_unified)



## January 20, 2021

Feature

General availability for the following integration:

  * [AI Platform Prediction](https://docs.cloud.google.com/ai-platform/prediction/docs/vpc-service-controls)



## January 19, 2021

Feature

[Preview support](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)



## January 07, 2021

Feature

General availability for the following integration:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs/instances/protecting-resources-vpc-service-controls)



## December 14, 2020

Feature

[Preview support](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs)



## December 08, 2020

Feature

[Preview support](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * [Identity-Aware Proxy for TCP forwarding](https://docs.cloud.google.com/iap/docs/securing-tcp-with-vpc-sc)



## November 16, 2020

Feature

[General availability](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Artifact Registry](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_artifacts)



## November 04, 2020

Feature

[Preview support](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs)



## October 29, 2020

Feature

[Beta](https://cloud.google.com/products/#product-launch-stages) stage support for the following integration:

  * [VM Manager](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_vm_manager)



## October 05, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [OS Login](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_os_login)



## September 01, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Speech-to-Text](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_speech)



## July 28, 2020

Feature

General availability for the following integration:

  * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis)



## July 20, 2020

Feature

General availability for the following integration:

  * [AI Platform Training](https://docs.cloud.google.com/ai-platform/training/docs/vpc-service-controls)



## July 14, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [AI Platform Prediction](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_aip-prediction)



## June 30, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Cloud Composer](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_composer)
  * [Cloud Healthcare API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_healthcare)



Feature

Beta release of the VPC Service Controls Troubleshooter.

The VPC Service Controls Troubleshooter allows you to use the unique identifiers generated by VPC Service Controls errors to understand and resolve common denials to services in your perimeters.

During the beta period, the following error types are supported:

  * `NO_MATCHING_ACCESS_LEVEL`
  * `NETWORK_NOT_IN_SAME_SERVICE_PERIMETER`
  * `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER`



For more information, read about [the VPC Service Controls Troubleshooter](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter).

Feature

General availability of dry run mode for service perimeters.

This release introduces dry run configurations for your service perimeters, allowing you to test changes to perimeters before enforcing the changes. For more information, [read about dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).

## June 26, 2020

Change

[Beta stage support](https://cloud.google.com/products/#product-launch-stages) for the following integration:

  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/securing-with-vpcsc)



## June 11, 2020

Feature

General availability for bulk changes to service perimeters.

Using Access Context Manager's Bulk API, you can replace all of your organization's service perimeters in one operation. For more information, see [Making bulk changes to service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/bulk-operations).

## June 04, 2020

Feature

The VPC accessible services feature is now generally available. Use VPC accessible services to limit the access of network endpoints and VMs in a perimeter to only services protected by that perimeter.

For more information about the feature, see [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).

## May 21, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Service Directory](https://docs.cloud.google.com/service-directory/docs/securing-with-vpc-sc)



## May 13, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis)



## April 09, 2020

Feature

The beta version of dry run mode for service perimeters is now available.

This release introduces a new method of configuring service perimeters: dry run mode. For more information, [read about dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).

Feature

The beta version of the VPC accessible services feature is now available.

The [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) feature introduces the ability to limit the access of network endpoints inside your service perimeter to an explicit set of services.

To learn how to configure VPC accessible services for your perimeter, read about [limiting access to services inside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#accessible-services).

## April 03, 2020

Feature

Beta support for bulk changes to service perimeters.

Using the beta release of Access Context Manager's Bulk API, you can perform operations such as replacing all of your organization's service perimeters. For more information, see [Making bulk changes to service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/bulk-operations).

## April 01, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Container Analysis](https://docs.cloud.google.com/container-registry/docs/container-analysis)



## March 31, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [AutoML Natural Language](https://docs.cloud.google.com/natural-language/automl/docs)
  * [AutoML Tables](https://docs.cloud.google.com/automl-tables/docs)
  * [AutoML Translation](https://docs.cloud.google.com/translate/automl/docs)
  * [AutoML Video Intelligence](https://docs.cloud.google.com/video-intelligence/automl/docs)
  * [AutoML Vision](https://docs.cloud.google.com/vision/automl/docs)
  * [Artifact Registry](https://docs.cloud.google.com/artifacts/docs)



## March 24, 2020

Feature

General availability for the following integration:

  * [Cloud Functions](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_functions)



## March 10, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for:

  * [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs)



## February 06, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Cloud Translation](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_translate)



## January 31, 2020

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Cloud Functions](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_functions)
  * [Cloud Data Fusion](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_data_fusion)



## December 20, 2019

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integration:

  * [AI Platform Training](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_aip-training)



## December 18, 2019

Feature

[Beta stage support](https://cloud.google.com/products/#product-launch-stages) for the following integrations:

  * [Cloud Asset Inventory](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_asset_api)



## December 17, 2019

Feature

General availability support for:

  * [Cloud SQL](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_sql_admin_api)



## December 16, 2019

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Trace API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_trace)



## December 10, 2019

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Profiler API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_profiler)



## December 02, 2019

Feature

Unique identifier for VPC Service Controls access errors.

When a request for resources in a perimeter is denied (a 403 error), a unique identifier is generated that you can use to identify the corresponding log entry using Stackdriver Logging.

For more information, see:

  * [Unique Identifier helps troubleshooting VPC Service Controls perimeter](https://docs.cloud.google.com/blog/products/identity-security/unique-identifier-helps-troubleshooting-vpc-service-controls-perimeter)
  * [VPC Service Controls troubleshooting documentation](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#using_the_errors_unique_id)



## October 30, 2019

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following integrations:

  * [Natural Language API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_natural_language_api)



## August 22, 2019

Change

The [limits](https://docs.cloud.google.com/vpc-service-controls/quotas) for VPC Service Controls have been increased:

  * Previously, only 50 perimeters per policy were allowed. That limit has been increased to 100.
  * Previously, only 2500 projects total were allowed across all perimeters for one policy. That limit has been increased to 4000.



## August 09, 2019

Feature

[General availability](https://cloud.google.com/products/#product-launch-stages) for the following integrations:

  * [Cloud Dataflow](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dataflow)



## May 24, 2019

Feature

[General availability](https://cloud.google.com/products/#product-launch-stages) for the following integrations:

  * [Cloud Key Management Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_kms)
  * [Cloud Spanner](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_spanner)
  * [Container Registry](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_registry)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gke)



## April 01, 2019

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following:

  * Cloud Dataflow



## March 29, 2019

Feature

[Beta stage](https://cloud.google.com/products/#product-launch-stages) support for the following:

  * Cloud Key Management Service
  * Cloud Spanner



## March 08, 2019

Feature

General availability of VPC Service Controls.

## February 28, 2019

Feature

[Alpha stage](https://cloud.google.com/terms/launch-stages) support for the Google Kubernetes Engine API.

[Beta stage](https://cloud.google.com/terms/launch-stages) support for Google Kubernetes Engine private clusters.

As of this release, GKE private clusters can be protected by VPC Service Controls service perimeters.

For more information, refer to the [VPC Service Controls page](https://docs.cloud.google.com/vpc-service-controls) and the [documentation](https://docs.cloud.google.com/vpc-service-controls/docs).

## December 20, 2018

Feature

Public beta release of VPC Service Controls.

As of this release, VPC Service Controls supports the following services:

  * Cloud Bigtable
  * Cloud Storage
  * BigQuery
  * Cloud Pub/Sub
  * Cloud Dataproc
  * Stackdriver Logging



VPC Service Controls also has Alpha stage support for the following services:

**Note:** We recommend you protect these services for testing purposes only.

  * Container Registry
  * Cloud Key Management Service
  * Cloud Spanner



Issue

Legacy Cloud Storage buckets can in certain cases be written to out of a service perimeter even when access is denied.

Additionally, Cloud Storage audit logs do not always report VPC Service Controls errors correctly.

For more information, read about [Cloud Storage limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#storage).

Issue

The Java and Python client libraries for all supported services are fully supported for access using the VPC Service Controls restricted VIP. Support for others language is at Alpha stage and should be used for testing purposes only. Client libraries updated since November 1, 2018 must be used.

Service account keys and OAuth2 client metadata used to authenticate must be updated as of November 1, 2018.

For more information, read about [client library limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#clientlibraries).

Issue

A Cloud DNS private zone or BIND must be used to map Container Registry to the restricted VIP.

The following Google-managed repositories are available to all projects regardless of service perimeters:

  * dataflow.gcr.io
  * gcr.io/cloud-airflow-releaser
  * gcr.io/cloudsql-docker
  * gcr.io/gke-node-images
  * gcr.io/kubeflow-images-public
  * gcr.io/kubernetes-helm
  * gcr.io/project-calico
  * gcr.io/stackdriver-agents
  * gke.gcr.io
  * k8s.gcr.io
  * mirror.gcr.io



For more information, read about [Container Registry limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#registry).

Issue

To create Compute Engine images from Cloud Storage inside a service perimeter, the user performing the configuration must be added to an access level for that perimeter.

For more information, read about [Compute Engine limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#computeengine).

Issue

Because VPC Service Controls does not currently support folder and organization resources, log exports of folder-level and organization-level logs (including aggregate logs) do not support service perimeters.

Aggregated Stackdriver Logging logs can access data protected by a service perimeter. IAM should be used to control access to that data.

For more information, read about [Logging limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#logging).

Issue

Cloud Dataproc requires additional steps to set up a functional cluster inside a service perimeter.

For more information, read about [Cloud Dataproc limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#dataproc).

Issue

Cloud Functions is not supported by VPC Service Controls. However, you can use Access Context Manager to allow functions outside a service perimeter to access resources protected by VPC Service Controls by adding the Cloud Functions service account to an access level for that perimeter.

For more information, read about [Cloud Functions limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#functions).

Issue

To use the Google Cloud Platform Console with services protected by a service perimeter, the user accessing the services must be added to an access level for that perimeter.

Issue

Cloud Shell is not supported. It is treated as outside of service perimeters and denied access to data protected by VPC Service Controls.

Issue

To configure Cloud Billing exporting inside a service perimeter, the user performing the configuration must be added to an access level for that perimeter.

For more information, read about [Cloud Billing limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#billing).

Issue

The BigQuery Data Transfer Service is not supported. Additionally, there are known limitations with the legacy BigQuery interface, the third-party ODBC driver for BigQuery, and BigQuery audit logs.

For more information, read about [BigQuery limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#bigquery).

Issue

App Engine is not supported by VPC Service Controls. However, you can use Access Context Manager to allow App Engine apps outside a service perimeter to access resources protected by VPC Service Controls by adding the App Engine service account to an access level for that perimeter.

For more information, read about [App Engine limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#appengine).

Issue

VPC Service Controls policy only applies to new Cloud Pub/Sub push subscriptions. Push subscriptions that exist before a service perimeter is created will not be blocked by that perimeter.

For more information, read about [Cloud Pub/Sub limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#pubsub).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
