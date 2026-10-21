---
url: https://docs.cloud.google.com/certificate-authority-service/docs/release-notes/
title: Certificate Authority Service release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:23:38.257290+00:00
---

# Certificate Authority Service release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Resources ](https://docs.cloud.google.com/certificate-authority-service/docs/resources)



Send feedback 

#  Certificate Authority Service release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Certificate Authority Service. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/certificate-authority-service-release-notes.xml) directly. 

## June 27, 2025

v1

Feature

You can backdate the `not_before_time` of certificates by specifying the `backdate_duration` field within the issuance policy of your CA Pool. This new optional field in the issuance policy allows you to control the `not_before_time` of all certificates issued from a given CA Pool. 

If `backdate_duration` is not set: Certificates are issued with a `not_before_time` equal to the current issuance time.

If `backdate_duration` is set: Certificates are issued with a `not_before_time` equal to the issuance time minus the specified `backdate_duration`. The `not_after_time` automatically adjusts to maintain the requested certificate lifetime.

## March 03, 2025

v1

Feature

Certificate Authority Service is now available in the following region:

  * europe-north2 (Stockholm)



For more information, see [Certificate Authority Service locations](https://cloud.google.com/certificate-authority-service/docs/locations).

## February 13, 2025

v1

Feature

Custom Authority Information Access (AIA) and CRL Distribution Point (CDP) extensions for certificate authorities (CAs) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can create CAs with custom AIA and CDP certificate extensions. These custom URLs are embedded directly into certificates issued by your CA, providing precise control over certificate validation paths. If custom AIA and CDP extensions are not specified, the system continues to use the default Google Cloud Storage (GCS) publishing locations for AIA and CDP information in issued certificates. The AIA extension enables clients to locate the issuer's certificate, while the CDP extension provides access to the Certificate Revocation List (CRL).

## June 24, 2024

v1

Feature

Certificate Authority Service is now available in the following region:

  * africa-south1



For more information, see [Certificate Authority Service locations](https://cloud.google.com/certificate-authority-service/docs/locations).

## May 06, 2024

v1

Feature

Implement fine-grained policy controls over your certificate issuance using certificate templates. Certificate templates can be used in conjunction with IAM conditions to effectively create different policy controls for different users on the same CA pool. You can test certificate issuance in a validation mode and proactively identify conflicts between the CA pool's issuance policies and the certificate template's policies. For information, see [Request a certificate using a certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/issue-certificate-using-template). The feature is in General Availability (GA).

## October 25, 2023

v1

Feature

Certificate Authority Service is now available in the following region:

  * europe-west10



For more information, see [Certificate Authority Service locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).

## October 05, 2023

v1

Feature

Certificate Authority Service is now available in the following region:

  * me-central2



For more information, see [Certificate Authority Service locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).

## September 15, 2023

v1

Feature

Certificate Authority Service now supports [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency).

## July 24, 2023

v1

Feature

The following Assured Workloads compliance programs now support Certificate Authority Service:

  * [Australia Regions with Assured Support](https://docs.cloud.google.com/assured-workloads/docs/compliance-programs#aus-regions-support)
  * [Canada Regions and Support](https://docs.cloud.google.com/assured-workloads/docs/compliance-programs#can-regions-support)
  * Canada Protected B
  * [Israel Regions and Support](https://docs.cloud.google.com/assured-workloads/docs/compliance-programs#il-regions-support)
  * [US Regions and Support](https://docs.cloud.google.com/assured-workloads/docs/compliance-programs#us-regions-support)



See [supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) for more information.

## July 04, 2023

v1

Feature

Certificate Authority Service now supports [Workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

## June 21, 2023

v1

Feature

Certificate Authority Service is now available in the following regions:

  * me-central1
  * europe-west12



For more information, see [Certificate Authority Service locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).

## April 25, 2023

v1

Announcement

**General Availability** : Certificate Authority Service integrates with Certificate Manager to enable certificate issuance. The integration enables users to create a Google-managed certificate issued by their Certificate Authority Service instance. For information, see [Create a Google-managed certificate issued by Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/certificates#cert-cas).

## March 20, 2023

v1

Feature

**General Availability** : You can create resources such as certificate authorities (CA) and certificate authority pools with X.509 name constraints. Name constraints on CA resources are enforced when issuing certificates, which lets you control which names are permitted or excluded. 

For more information, see [CA certificate name constraints](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls#name-constraints).

## April 13, 2022

v1

Announcement

Learn how to [get started with using the Cloud Client Libraries for the Certificate Authority Service API](https://docs.cloud.google.com/certificate-authority-service/docs/reference/libraries).

## January 25, 2022

v1

Announcement

Certificate Authority Service provides a [public issue tracker](https://issuetracker.google.com/issues/new?component=1124905) that you can use for suggesting product features, providing product and documentation feedback, and reporting issues. For more information, see [File bugs or feature requests](https://docs.cloud.google.com/certificate-authority-service/docs/getting-support#file_bugs_or_feature_requests).

## November 24, 2021

v1

Announcement

You can now browse all the code samples for Certificate Authority Service on the documentation site. To check all the available code samples, see [All CA Service code samples](https://docs.cloud.google.com/certificate-authority-service/docs/samples).

## July 02, 2021

v1

Announcement

Certificate Authority Service is now [generally available](https://cloud.google.com/products/#product-launch-stages) with the following new features.

  * **Certificate authority (CA) pools** : A CA pool is a container for multiple CAs with a common certificate issuance policy and IAM policy. More information: [Overview of CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool).
  * **Certificate templates** : Certificate templates are reusable and parameterized schemas for common certificate issuance scenarios. The reusable configs feature has been retired, and certificate template replaces it. More information: [Certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template).
  * **Identity reflection** : Identity reflection is a special certificate issuance mode that limits an unprivileged certificate requester. With the identity reflection mode, the unprivileged certificate requester can only request certificates with a SAN corresponding to the identity in their credential. More information: [Using identity reflection](https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection).
  * **Updates to CA states** : A new state called `STAGED` has been added to the list of CA states. The new set of CA states can be found here: [Certificate authority states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).
  * **New locations** : CA Service has expanded the list of locations where you can create your resources. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).



In addition to the above features, Certificate Authority Service has the following updates as part of the GA release.

  * **Pricing** : CA Service offers a simple pay-as-you-go pricing model. Large volume customers can also avail the subscription-based pricing model. More information: [Pricing](https://cloud.google.com/certificate-authority-service/pricing).
  * **Service Level Agreement (SLA)** : SLA for CA Service is now publicly available and offers 99.9% availability per region for certificate creation. More information: [SLA](https://cloud.google.com/certificate-authority-service/sla).
  * **Compliance** : CA Service meets ISO 27001, 27017, 27018, SOC1, SOC2, SOC3, BSI C5, and PCI compliance standards.



## October 19, 2020

v1beta1

Announcement

Certificate Authority Service is available in Preview. The Preview features should not be used for production use, as all CAs and certificates created during the Preview period will be erased with the GA release.

## April 04, 2020

v1beta1

Announcement

Certificate Authority Service is available in private Alpha.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
