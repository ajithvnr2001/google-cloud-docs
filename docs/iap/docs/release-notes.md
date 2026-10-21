---
url: https://docs.cloud.google.com/iap/docs/release-notes/
title: IAP release notes \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:52.635241+00:00
---

# IAP release notes  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Resources ](https://docs.cloud.google.com/iap/docs/resources)



Send feedback 

#  IAP release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to IAP. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

**Current version: release**

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/iap-release-notes.xml) directly. 

## August 31, 2026

Feature

**IAM Unified Access Policies for Agent Gateway are generally available (GA)**

IAM Unified Access Policies (Access policies) for Agent Gateway and Identity-Aware Proxy (IAP) are [generally available (GA)](https://cloud.google.com/products#product-launch-stages). Identity-Aware Proxy integrates with Agent Gateway and uses Access policies to help secure and govern agentic egress communication between agent principals and destination resources, such as Model Context Protocol (MCP) servers, other agents, and registered or unregistered endpoints.

Key capabilities include:

  * Multiple allow and deny rules within a single Access policy to establish fine-grained behavioral guardrails for egress traffic.
  * Common Expression Language (CEL) condition evaluation in rules to enforce egress access criteria based on tool names, read-only constraints, HTTP methods, and URL paths.
  * Dry-run and enforcement modes to validate and audit policy evaluation before blocking egress traffic.
  * End-to-end agent identity authentication and authorization using mutual TLS (mTLS) and Context-Aware Access (CAA) with Demonstrating Proof of Possession (DPoP).



For more information, see [IAM access policies overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iam-overview-uap).

## June 24, 2026

Feature

Identity-Aware Proxy (IAP) supports securing agent-to-anywhere egress for Agent Gateway. The feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). To learn more about IAP support for Agent Gateway, see [IAP for agents overview](https://docs.cloud.google.com/iap/docs/agent-overview).

## April 22, 2026

Feature

Identity-Aware Proxy (IAP) supports securing agent-to-anywhere egress for Agent Gateway. The feature is in [Preview](https://cloud.google.com/products#product-launch-stages). To learn more about IAP support for Agent Gateway, see [IAP for agents overview](https://docs.cloud.google.com/iap/docs/agent-overview).

## March 13, 2026

Feature

You can configure custom OAuth clients in Identity-Aware Proxy by using the Google Cloud console; the feature is generally available [(GA)](https://cloud.google.com/products#product-launch-stages). You must use custom OAuth clients to do the following:

  * Configure IAP for users who are outside of an organization.

  * Customize the OAuth consent screen with custom branding.

  * Provide default OAuth clients for inherited applications across all IAP-protected resources at the organization or project level.




For more information, see [Use custom OAuth clients with IAP](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration).

## October 28, 2025

Feature

The ability to use a path wildcard in the `aud` (audience) field when using a service account JWT to authenticate with an IAP-secured resource is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Authenticate with a service account JWT](https://docs.cloud.google.com/iap/docs/authentication-howto#create_the_jwt).

## April 15, 2025

Change

Identity-Aware Proxy (IAP) now charges quota for programmatic and browser user requests independently. If you use IAP for programmatic workloads and have browser users within the same project, this change provides an improved representation of quota consumption.

For more information, see [How can I address quota exceeded errors](https://docs.cloud.google.com/iap/docs/faq#how_can_i_address_quota_exceeded_errors_error_code_429).

## April 07, 2025

Feature

**Preview** : You can now enable IAP directly on your Cloud Run services without configuring load balancers.

For more information, see [Configure Identity-Aware Proxy for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run).

## February 07, 2025

Feature

**Generally available** : You can configure Workforce Identity Federation with IAP, and use an external identity provider (IdP) to authenticate and authorize a workforce—a group of users, such as employees, partners, and contractors—using Identity and Access Management (IAM), so that the users can securely access services deployed on Google Cloud or on-premises.

For more information, see [Configure IAP with Workforce Identity Federation](https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation).

Feature

**Generally available** : Support for service account JWT authentication for Identity Platform and Workforce Identity Federation configured applications. For more information, see [Authenticating with a service account JWT](https://docs.cloud.google.com/iap/docs/authentication-howto#authenticating_with_a_service_account_jwt).

## September 20, 2024

Feature

**Preview** : You can now use authorization policies to delegate authorization to Identity-Aware Proxy (IAP) and Identity and Access Management (IAM). For more information, see [Use authorization policies to delegate authorization to IAP and IAM](https://docs.cloud.google.com/iap/docs/auth-policies).

## June 28, 2024

Change

On February 14, 2024, the Cloud Audit Logging (CAL) type was inadvertently changed from `DATA_ACCESS` to `ADMIN_ACTIVITY`. This change causes a change in the log name and log bucket location for the `UpdateIapSettings` and `ValidateIapAttributeExpression` methods. 

The CAL type has been changed back to `DATA_ACCESS`.

## May 16, 2024

Feature

**Generally Available** : Service accounts can now use JSON Web Tokens (JWTs) to programmatically access resources protected by Identity-Aware Proxy (IAP). This provides a streamlined authentication process for workloads accessing IAP-protected applications and services. For more information, see [Programmatic authentication](https://docs.cloud.google.com/iap/docs/authentication-howto).

## May 06, 2024

Feature

Identity-Aware Proxy (IAP) now supports Workforce Identity Federation for application access. You can now use your extended workforce identities to access IAP-protected applications without having to sync your identities into Cloud Identity. For more information, see [Configure IAP with Workforce Identity Federation](https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation).

## April 23, 2024

Feature

WebSocket support for managing Compute Engine resource sessions is now available. For more information, see [Managing IAP sessions ](https://docs.cloud.google.com/iap/docs/sessions-howto).

## February 01, 2024

Change

Effective January 12, 2024, a BeyondCorp Enterprise license is no longer required to deploy internal applications with an internal load balancer when securing those applications with Identity-Aware Proxy. This provides a consistent experience when using Identity-Aware Proxy with all load balancers.

## January 16, 2024

Change

A BeyondCorp Enterprise license is no longer required when configuring Identity-Aware Proxy with an internal load balancer.

This note is incomplete; see entry for February 1, 2024. 

## August 17, 2023

Feature

Authenticating users with a Google-managed OAuth client and allowlisting OAuth clients for programmatic access are available in Preview.

## April 07, 2023

Feature

Support for [Identity-aware Proxy (IAP) with Cloud Run](https://docs.cloud.google.com/iap/docs/enabling-cloud-run) to use identity and context to guard access to your applications is now at general availability ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 16, 2021

Security

Security bulletin c2agxr12ne

Certain Google Cloud load balancers routing to an Identity-Aware Proxy enabled Backend Service could have been vulnerable to an untrusted party under limited conditions.

For details, see [GCP-2021-020](https://docs.cloud.google.com/support/bulletins)

## May 29, 2020

Feature

The ability to authenticate users with [external identities](https://docs.cloud.google.com/iap/docs/enable-external-identities) is now generally available.

## February 12, 2020

Feature

API for OAuth clients now generally available

You can now programmatically create OAuth clients in IAP via REST or gcloud. See [this topic](https://docs.cloud.google.com/iap/docs/programmatic-oauth-clients) for more information.

## August 07, 2019

Feature

Cloud IAP TCP forwarding general availability release

Using [Cloud IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview) is now generally available. Cloud IAP for TCP forwarding lets you control who can access administrative services like SSH and RDP on your backends.

## April 10, 2019

Feature

Cloud IAP with context-aware access general availability release

The ability to extend Cloud IAP access policies with [access levels](https://docs.cloud.google.com/access-context-manager/docs) and the [IAM Conditions Framework](https://docs.cloud.google.com/iam/docs/conditions-overview) is now generally available.

## February 26, 2019

Feature

Cloud IAP for on-premises apps general availability release

You can now [manage access to HTTP-based apps outside of Google Cloud Platform](https://docs.cloud.google.com/iap/docs/cloud-iap-for-on-prem-apps-overview). This includes apps on-premises in your enterprise's data centers and on other cloud providers.

## February 14, 2019

Feature

Cloud IAP Per-Resource Policies general availability release

The ability to [manage Cloud IAP policies](https://docs.cloud.google.com/iap/docs/managing-access) for each individual resource in a Google Cloud Platform project is now generally available.

## January 22, 2019

Feature

Cloud IAP TCP forwarding beta release

You can now use [Cloud IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview), allowing you to control who can access administrative services like SSH and RDP on your backends.

## October 04, 2018

Feature

Cloud IAP with context-aware access beta release

Cloud IAP access policies for Cloud IAP-secured applications, services, and versions have been extended to use [access levels](https://docs.cloud.google.com/access-context-manager/docs) and the [IAM Conditions Framework](https://docs.cloud.google.com/iam/docs/conditions-overview). Access levels allow access restrictions to resources based on IP address and end-user device attributes. IAM conditions allow access restrictions based on URL hosts, paths, date, and time.

## August 16, 2018

Feature

Cloud IAP Per-Resource Policies beta release

Cloud IAP policies can now be [managed](https://docs.cloud.google.com/iap/docs/managing-access) for each individual resource in a GCP project.

## August 31, 2017

Feature

Welcome to the Cloud IAP general release for App Engine standard environment, Compute Engine, and GKE!

Change

Java code samples were updated with security enhancements on August 15, 2017. If you're using the Java [signed headers](https://docs.cloud.google.com/iap/docs/signed-headers-howto) code sample, please update your application per the current samples.

Feature

AJAX requests with missing or expired credentials will now get an HTTP 401 response instead of being served a Google login page.

Feature

Cloud IAP now supports Cloud Audit Logging. Learn about [enabling Cloud Audit Logging](https://docs.cloud.google.com/iap/docs/audit-log-howto).

Change

When you use the programmatic authentication feature, the aud claim in the JWT must now be the Cloud IAP client ID. Previously, it could also be the application URL. For applications that used programmatic authentication recently, we placed this feature on our whitelist. We will remove the functionality on November 15, 2017. For details and updated code samples, refer to [programmatic authentication](https://docs.cloud.google.com/iap/docs/authentication-howto).

Feature

Cloud IAP now supports desktop and command-line applications. Learn about [authenticating from a desktop app](https://docs.cloud.google.com/iap/docs/authentication-howto#authenticating_from_a_desktop_app).

Issue

Cloud IAP for App Engine flexible environment is still in [beta](https://cloud.google.com/terms/launch-stages). This feature is not covered by any SLA or deprecation policy and may be subject to backward-incompatible changes for App Engine flexible environment.

Change

Due to internal security enhancements, App Engine standard environment apps no longer require `login: required` in `app.yaml` (or `security-constraint` for Java).

Feature

[Forseti Security](http://forsetisecurity.org/) is now available and strongly encouraged for Compute Engine apps. If you have any questions or require assistance, please post to discuss@forsetisecurity.org.

## August 07, 2017

Fixed

Cloud IAP can once again be enabled for App Engine flexible environment apps.

## July 20, 2017

Feature

Cloud IAP now supports [special URLs](https://docs.cloud.google.com/iap/docs/special-urls-howto) to help you enhance and personalize your app.

## July 14, 2017

Change

Cloud IAP now uses the following values when you secure your app with signed headers:

  * The JWT is now in the HTTP request header `x-goog-iap-jwt-assertion` instead of `x-goog-authenticated-user-jwt`.
  * When you [verify the ID token payload](https://docs.cloud.google.com/iap/docs/signed-headers-howto#verify_the_id_token_payload), the `aud` value should now be a string with client ID details instead of a URL.



## July 11, 2017

Feature

Added [best practices for caching](https://docs.cloud.google.com/iap/docs/concepts-best-practices).

## June 19, 2017

Feature

Cloud Audit Logging is now available for Cloud IAP-secured resources. Read about how to [Enable Cloud Audit Logging](https://docs.cloud.google.com/iap/docs/audit-log-howto).

Change

The Cloud IAP 403 "failed access" page now includes product and email details from the OAuth consent screen. As with the login page, these details are publicly visible to anyone who accesses your URL. You can change the information that displays on the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent?_ga=2.250325059.-492396546.1528399541).

## June 07, 2017

Feature

Added information about [Authenticating from a desktop app](https://docs.cloud.google.com/iap/docs/authentication-howto#authenticating_from_a_desktop_app) for Cloud IAP-secured resources.

## April 17, 2017

Change

When you use Cloud IAP with Compute Engine, GKE, or the App Engine flexible environment, you must also use [signed headers](https://docs.cloud.google.com/iap/docs/signed-headers-howto) to secure your app.

Issue

Cloud IAP can't currently be enabled for App Engine flexible environment apps.

## March 09, 2017

Issue

Cloud IAP has a static 403 "failed access" page. In a future release, admins will be able to customize the failure message text.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
