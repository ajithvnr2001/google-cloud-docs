---
url: https://docs.cloud.google.com/feeds/certificate-manager-release-notes.xml
title: Certificate Manager - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:31:47.066680+00:00
---

# Certificate Manager - Release notes

> Source: https://docs.cloud.google.com/feeds/certificate-manager-release-notes.xml

tag:google.com,2016:certificate-manager-release-notesCertificate Manager - Release notesGoogle Cloud Platform2026-10-14T00:00:00-07:00October 14, 2026tag:google.com,2016:certificate-manager-release-notes#October_14_20262026-10-14T00:00:00-07:00Change 

Google-managed public SSL certificates signed by [Google Public CA](https://docs.cloud.google.com/certificate-manager/docs/public-ca) (pki.goog) are gradually transitioning from a 90-day validity period to a 45-day validity period to improve security.

To align with modern industry-wide security standards and promote shorter certificate lifespans, Google-managed public certificates now rotate more frequently. This proactive rotation enhances the overall security posture of load balancers. The transition requires no manual intervention or configuration changes as Certificate Manager automatically manages both issuance and renewal.

For more information, see [Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/core-components#google-managed-certificates) and [Use Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/certificate-manager-best-practices#use_google_managed_certificates).

]]> September 24, 2026tag:google.com,2016:certificate-manager-release-notes#September_24_20262026-09-24T00:00:00-07:00Feature 

You can now attach tags to Certificate Manager resources during creation. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Create and manage tags for Certificate Manager resources](https://docs.cloud.google.com/certificate-manager/docs/create-manage-tags).

]]> May 19, 2026tag:google.com,2016:certificate-manager-release-notes#May_19_20262026-05-19T00:00:00-07:00Feature 

Certificate Manager (2nd gen) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Certificate Manager (2nd gen) offers a unified control plane to observe, manage, and automate certificates across your organization.

For more information, see [Certificate Manager (2nd gen) overview](https://docs.cloud.google.com/certificate-manager/docs/v2/overview).

]]> December 05, 2024tag:google.com,2016:certificate-manager-release-notes#December_05_20242024-12-05T00:00:00-08:00Announcement 

[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs) has passed HIPAA compliance validation and is [listed](https://docs.cloud.google.com/security/compliance/hipaa#covered-products) as a covered product in HIPPA compliance on Google Cloud.

]]> August 21, 2024tag:google.com,2016:certificate-manager-release-notes#August_21_20242024-08-21T00:00:00-07:00Feature 

You can now update the "labels" and "descriptions" of your certificate issuance configurations using the Google Cloud CLI or API. For more information, see [Manage certificate issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs#update).

### Change

Regional Google-managed certificates are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

### Change

Support for managing certificates independently in each project with separate authorization is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations).

]]> March 12, 2024tag:google.com,2016:certificate-manager-release-notes#March_12_20242024-03-12T00:00:00-07:00Feature 

Certificate Manager supports integration with regional external Application Load Balancers and regional internal Application Load Balancers. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

]]> February 22, 2024tag:google.com,2016:certificate-manager-release-notes#February_22_20242024-02-22T00:00:00-08:00Feature 

[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs) supports the management of certificates independently in each project with separate authorization. You can also issue regional managed certificates with Certificate Manager. This is a [public preview feature](https://cloud.google.com/products/#product-launch-stages). For more information, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

]]> September 28, 2023tag:google.com,2016:certificate-manager-release-notes#September_28_20232023-09-28T00:00:00-07:00Feature 

[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs) supports Mutual TLS (mTLS) authentication. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

]]> August 18, 2023tag:google.com,2016:certificate-manager-release-notes#August_18_20232023-08-18T00:00:00-07:00Feature 

Certificate Manager now supports integration with regional external Application Load Balancers and regional internal Application Load Balancers. This is a [public preview feature](https://cloud.google.com/products/#product-launch-stages). For more information, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

]]> April 19, 2023tag:google.com,2016:certificate-manager-release-notes#April_19_20232023-04-19T00:00:00-07:00Change 

The Certificate Authority Service integration feature is now generally available.

### Feature

Certificate Manager now supports Mutual TLS (mTLS) authentication. This is a public preview feature. For more information, see [Trust configs](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#trust-configs).

]]> December 15, 2022tag:google.com,2016:certificate-manager-release-notes#December_15_20222022-12-15T00:00:00-08:00Feature 

You can now view a list of certificates managed by Certificate Manager in your project in the Cloud Console. You can also view detailed information about each certificate. For instructions, see [Manage Certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates). 

Load Balancing SSL certificates, previously available in the "Certificates" tab on the "Load Balancing" page, are now also available in the Certificate Manager page in the "Classic Certificates" tab.

]]> June 28, 2022tag:google.com,2016:certificate-manager-release-notes#June_28_20222022-06-28T00:00:00-07:00Announcement 

This is the General Availability release of Certificate Manager.

]]> May 01, 2022tag:google.com,2016:certificate-manager-release-notes#May_01_20222022-05-01T00:00:00-07:00Announcement 

Billing has been enabled. Certificate Manager usage is billed at 100% discount until the end of the Preview period.

]]> April 05, 2022tag:google.com,2016:certificate-manager-release-notes#April_05_20222022-04-05T00:00:00-07:00Feature 

This release of Certificate Manager adds support for target SSL proxies and the global external HTTP(S) load balancer (preview).

]]> January 28, 2022tag:google.com,2016:certificate-manager-release-notes#January_28_20222022-01-28T00:00:00-08:00Announcement 

This is the initial Preview release of Certificate Manager.

]]>
