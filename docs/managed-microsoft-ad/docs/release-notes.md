---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/release-notes/
title: Managed Microsoft AD release notes \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:00.850660+00:00
---

# Managed Microsoft AD release notes  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-microsoft-ad/docs/resources)



Send feedback 

#  Managed Microsoft AD release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Managed Service for Microsoft Active Directory. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/managedmicrosoftad-release-notes.xml) directly. 

## January 31, 2024

Feature

Managed Microsoft AD is available in the `africa-south1` (Johannesburg) region. For more information, see [Deploy domain controllers in additional regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions).

## November 03, 2023

Feature

Managed Microsoft AD is available in the `europe-west10` (Berlin) region. For more information, see [Deploy domain controllers in additional regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions).

## October 03, 2023

Feature

Managed Microsoft AD is available in the `me-central2` (Dammam) region. For more information, see [Deploy domain controllers in additional regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions).

## July 10, 2023

Feature

Support for [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) in Managed Microsoft AD is [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Workforce identity federation: supported products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#managed-service-for-microsoft-active-directory).

## June 02, 2023

Feature

Support for [joining a Windows Compute Engine VM automatically](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce) to a Managed Microsoft AD domain is [generally available](https://cloud.google.com/products#product-launch-stages) with the following updates:

  * Added a new `managed-ad-force` flag to reuse an existing computer account.
  * Improved the existing `managed-ad-ou-name` flag to specify the path of the custom OU.



For more information, see [Metadata](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#metadata).

Using the automated domain join feature, you can also [join GKE Windows Server nodes automatically](https://docs.cloud.google.com/managed-microsoft-ad/docs/automated-domain-join-gke) to a Managed Microsoft AD domain.

## May 17, 2023

Feature

Managed Microsoft AD is available in the following regions:

  * europe-west12 (Turin)
  * me-central1 (Doha)



For more information, see [Deploy domain controllers in additional regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions).

## December 19, 2022

Feature

Managed Microsoft AD supports applying Microsoft security baselines on your Managed Microsoft AD VMs. For more information, see [Microsoft security baselines](https://docs.cloud.google.com/managed-microsoft-ad/docs/hardening#security-baseline).

Feature

Managed Microsoft AD has added a set of new event IDs to audit logs that you can export for a domain. For the updated list of event IDs, see [Exported event IDs](https://docs.cloud.google.com/managed-microsoft-ad/docs/using-ad-audit-logs#event-ids).

## December 15, 2022

Feature

The ability to [join a Windows VM automatically to a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 07, 2022

Feature

Support for [schema extensions](https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension) in Managed Microsoft AD is [generally available](https://cloud.google.com/products/#product-launch-stages). Learn how to [extend the schema](https://docs.cloud.google.com/managed-microsoft-ad/docs/extend-schema).

Feature

Support for the [migration of users from an existing domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/domain-migration) to Managed Microsoft AD is available in [Preview](https://cloud.google.com/products#product-launch-stages). Learn how to [enable permissions for migrating an on-premises domain with SID History](https://docs.cloud.google.com/managed-microsoft-ad/docs/enable-migrate-permissions).

## October 05, 2022

Feature

Managed Microsoft AD is available in the following regions:

  * europe-southwest1 (Madrid)
  * europe-west8 (Milan)
  * europe-west9 (Paris)
  * me-west1 (Tel Aviv)
  * us-east5 (Columbus)
  * us-south1 (Dallas)



For more information, see [Adding and removing regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions).

## September 19, 2022

Feature

Managed Microsoft AD protects your Managed Microsoft AD instances against virus and malwares using the operating system's built-in antivirus. For more information, see [Security monitoring and protection](https://docs.cloud.google.com/managed-microsoft-ad/docs/hardening#monitoring-protection).

## July 21, 2022

Feature

You can use the Google Cloud console to [enable LDAPS](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-ldaps#console) and [configure multi-project access](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering#console) (domain peering) in Managed Microsoft AD.

## June 27, 2022

Feature

Support for [schema extensions](https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension) in Managed Microsoft AD is available for [Preview](https://cloud.google.com/products#product-launch-stages). Learn how to [extend the schema](https://docs.cloud.google.com/managed-microsoft-ad/docs/extend-schema).

## May 30, 2022

Feature

Support for [backing up and restoring Managed Microsoft AD domains](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore) is [generally available](https://cloud.google.com/products/#product-launch-stages).

## May 10, 2022

Feature

Managed Microsoft AD is available in the following regions:

  * `australia-southeast2` (Melbourne)
  * `europe-central2` (Warsaw)
  * `northamerica-northeast2` (Toronto)
  * `us-west3` (Salt Lake City)
  * `us-west4` (Las Vegas)



For more information, see [Adding and removing regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions).

## February 03, 2022

Feature

[Generally available](https://cloud.google.com/products/#product-launch-stages): Managed Microsoft AD now supports the use of [tags on domains](https://docs.cloud.google.com/managed-microsoft-ad/docs/tags-domain).

## July 30, 2021

Feature

Support for [audit logging](https://cloud.google.com/managed-microsoft-ad/docs/using-ad-audit-logs) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## June 21, 2021

Feature

Support for [integrating Managed Microsoft AD with Cloud SQL](https://cloud.google.com/managed-microsoft-ad/docs/how-to-use-ldaps) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## June 16, 2021

Feature

Support for [LDAPS](https://cloud.google.com/managed-microsoft-ad/docs/how-to-use-ldaps) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## March 04, 2021

Feature

Support for [Fine-Grained Password Policies (FGPP)](https://cloud.google.com/managed-microsoft-ad/docs/fgpp-concepts) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## January 14, 2021

Feature

Managed Microsoft AD now supports [audit logging](https://docs.cloud.google.com/managed-microsoft-ad/docs/using-ad-audit-logs). This feature is in the [Preview stage](https://cloud.google.com/products/#product-launch-stages).

## August 24, 2020

Feature

You can now create Managed Microsoft Active Directory instances using [Terraform](https://www.terraform.io/docs/providers/google/r/active_directory_domain.html).

## July 09, 2020

Feature

The [Managed Microsoft AD SLA](https://cloud.google.com/managed-microsoft-ad/sla) has been published.

## March 23, 2020

Change

**GA pricing now in effect**

New pricing for Managed Microsoft AD is now in effect. Learn more about standard [Managed AD pricing](https://cloud.google.com/managed-microsoft-ad/pricing) and view [pricing examples](https://cloud.google.com/managed-microsoft-ad/pricing#pricing_examples).

## March 10, 2020

Feature

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) integration is now in [beta](https://cloud.google.com/products/#product-launch-stages). 

Learn more about [configuring VPC Service Controls](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-vpc-service-controls) for Managed Microsoft AD to provide additional security.

## February 20, 2020

Feature

Managed Service for Microsoft AD General Availability

  * Added support for deploying domain controllers from the following regions:

    * asia-east2
    * asia-northeast1
    * asia-northeast2
    * asia-south1
    * australia-southeast1
    * europe-west2
    * europe-west3
    * europe-west6
    * northamerica-northeast1
    * southamerica-east1

Learn about the [full list of supported regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions#regions).

  * AD-dependent VMs and apps can use multi-regional VPCs to reach domain controllers in any region, regardless of their relative locations.

  * Domain controllers from the same AD domain can be deployed in up to 4 regions, at domain creation or later.

  * The [Domain Functional Level](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels) (DFL) of all new Managed AD domains is Windows Server 2012 R2. Domains created during the Managed AD Beta may have an earlier DFL. Learn [how to check your DFL](https://www.technipages.com/active-directory-how-to-check-domain-and-forest-functional-level).




Issue

Trust status is stale

When the trust between a Managed Microsoft AD domain and an on-premises Active Directory domain is broken, the status in the Cloud Console may not be correctly updated.

To validate the status of a trust, [go to the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad) in the Cloud Console and then select the domain. On the **Domain** page, in the **Trust relationships** table, select **Validate Trust**. Learn more about [getting domain info](https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domains#getting_domain_info).

## August 21, 2019

Feature

Managed Microsoft AD is now in beta!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
