---
url: https://docs.cloud.google.com/apigee/docs/edge-private-cloud/release-notes/
title: Apigee Edge for Private Cloud release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:12.386041+00:00
---

# Apigee Edge for Private Cloud release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/edge-private-cloud/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee Edge for Private Cloud release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents releases and patches for Apigee Edge for Private Cloud. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

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

  * [Release notes published before September 2026](https://docs.apigee.com/release/notes/apigee-release-notes)
  * [Apigee Edge for Public Cloud release notes](https://docs.cloud.google.com/apigee/docs/edge-public-cloud/release-notes)
  * [Known issues with Edge for Private Cloud](https://docs.apigee.com/release/known-issues#private-cloud-known-issues)



rss_feed Subscribe: 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/apigee-edge-private-cloud-release-notes.xml) directly. 

## October 15, 2026

4.54.00

Announcement

Released Apigee Edge for Private Cloud 4.54.00.

Designated Apigee Edge for Private Cloud 4.54.00.00 a long-term support (LTS) release: 18 months of full support ending April 2028, then 18 months of maintenance ending October 2029. After October 2029, 4.54.00.00 receives no software updates, security mitigations, or technical support.

Installing a later 4.54 minor release or patch does not change those dates. To extend the support lifecycle, upgrade to the next LTS release.

For the support lifecycle phases, release cadences, and version numbering, see [Apigee Edge for Private Cloud release and lifecycle policy](https://docs.apigee.com/release/private-cloud-release-lifecycle-policy).

4.54.00

Announcement

This release replaces Java 8 with Java 17 and Java 21, removes the Classic UI and the `apigee-sso` component, and updates the bundled Cassandra, Postgres, OpenLDAP, ZooKeeper, Qpid Broker-J, Nginx, and Consul versions. These changes are not backward-compatible.

For the 4.54.00 versions and the 4.53.01 versions they replace, see [Supported software and supported versions](https://docs.apigee.com/release/supported-software).

Before upgrading, read [Changes in Edge for Private Cloud 4.54.00](https://docs.apigee.com/private-cloud/v4.54.00/changes-privatecloud-45400), then [Update Apigee Edge 4.53.00 or 4.53.01 to 4.54.00](https://docs.apigee.com/private-cloud/v4.54.00/update-apigee-edge-4530x-45400) or [New installation overview](https://docs.apigee.com/private-cloud/v4.54.00/installation-overview). For known issues, see [Known issues with Edge for Private Cloud](https://docs.apigee.com/release/known-issues#private-cloud-known-issues).

4.54.00

Announcement

Replaced the Classic UI (`edge-ui`) with the [New Edge UI](https://docs.apigee.com/private-cloud/v4.54.00/new-edge-ui) (`edge-management-ui`).

The New Edge UI is the only management UI in 4.54.00 and is installed by default. Deployments running the Classic UI must transition to it before upgrading. Custom Classic UI properties do not carry over automatically. The default port also changes from `9000` to `3001`, configurable with `conf_uebe_port`, so firewall rules and load balancer target ports that point at `9000` fail until they are updated.

For the migration steps and the supported feature list, see [Migrate to the New Edge UI](https://docs.apigee.com/private-cloud/v4.54.00/migrate-ui) and [What features are supported?](https://docs.apigee.com/private-cloud/v4.54.00/new-edge-ui#features).

4.54.00

Breaking

In deployments with Apigee SSO enabled, an integrated OIDC identity broker in `apigee-openldap` replaces the standalone `apigee-sso` component and Apache Tomcat 9.0.x. Before upgrading, take a complete and validated LDAP backup; existing `apigee-sso` configurations do not migrate automatically. Deployments not using Apigee SSO require no action.

For migration prerequisites, validation checks, and rollback constraints, see [Option 2: Upgrade UI (with Apigee SSO)](https://docs.apigee.com/private-cloud/v4.54.00/update-apigee-edge-4530x-45400#upgrade-ui-with-apigee-sso).

4.54.00

Breaking

4.54.00 runs Java in mixed mode: Java 17 for Cassandra and ZooKeeper, Java 21 for the Management Server, Message Processor, Router, and Qpid Broker-J. Both Oracle JDK and OpenJDK are supported at those versions.

Oracle JDK 8 and OpenJDK 8 are no longer supported.

API proxies with custom JavaCallout policies or custom resource JARs can break on Java 21. For details, see [Changes in Edge for Private Cloud 4.54.00](https://docs.apigee.com/private-cloud/v4.54.00/changes-privatecloud-45400).

4.54.00

Change

Upgraded Nginx on the Edge Router to 1.30.0.

If you are upgrading from Nginx 1.20.x, see [Nginx 1.30 changes in Apigee Edge 4.54.00](https://docs.apigee.com/private-cloud/v4.54.00/nginx-45400) for the full list of changes.

4.54.00

Change

Changed the TLS defaults on Message Processors to the Java 21 cryptographic baseline.

Message Processors run on Java 21, which enables TLS 1.3 by default ([JEP 332](https://openjdk.org/jeps/332)) and prefers it for outbound backend connections, falling back to TLS 1.2. No configuration change is required if your target servers and load balancers negotiate TLS 1.3, or negotiate TLS 1.2 with forward-secret (ECDHE) cipher suites.

Java 21 also disables the non-forward-secret static RSA key-exchange suites (`TLS_RSA_*`). If you have overridden `conf_http_HTTPTransport.ssl.cipher.suites.whitelist` or `conf_message-processor-communication_local.http.ssl.ciphers` with static RSA suites only, backend calls fail with `no cipher suites in common` and the Router cannot complete a TLS handshake with the Message Processor. Replace the `TLS_RSA_*` entries with modern cipher suites and restart the Message Processor.

For the remediation path, see [Legacy backend requirements and remediation](https://docs.apigee.com/private-cloud/v4.54.00/changes-privatecloud-45400#legacy-tls-remediation).

4.54.00

Feature

Added Basic authentication to the New Edge UI, which lets you sign in without configuring an identity provider.

The [New Edge UI](https://docs.apigee.com/private-cloud/v4.54.00/new-edge-ui) supports Basic authentication without additional configuration. You can also configure Apigee SSO, or an external identity provider such as SAML or OIDC. This feature is generally available in 4.54.00.

4.54.00

Feature

Added automated pre-flight validation checks to `apigee-setup` and `apigee-service`, which surface environment configuration problems before a component is installed.

This feature is generally available in 4.54.00.

4.54.00

Security

Fixed multiple security vulnerabilities in Apigee Edge for Private Cloud 4.54.00.

These fixes ship as part of the component upgrades in this release; see [Changes in Edge for Private Cloud 4.54.00](https://docs.apigee.com/private-cloud/v4.54.00/changes-privatecloud-45400).

4.54.00

Change

Changed the default garbage collector on Message Processors to the Garbage-First garbage collector.

Message Processors set `useG1GC=true` and `useStringDeduplication=true` by default in 4.54.00. In 4.53.01 neither was set by default. To configure garbage collection, see [Configure the garbage collector for Message Processors](https://docs.apigee.com/private-cloud/v4.54.00/configuring-gc-message-processors-4.54).

## September 02, 2026

Announcement

Apigee Edge for Private Cloud release notes are now published on Google Cloud documentation.

Release notes and patch announcements for Apigee Edge for Private Cloud are published on the [Apigee Edge for Private Cloud release notes](https://docs.cloud.google.com/apigee/docs/edge-private-cloud/release-notes) page from September 2026 onward. You can [subscribe](https://docs.cloud.google.com/apigee/docs/edge-private-cloud/release-notes#sub) to that page with a feed reader to be notified when a new release or patch is published.

Release notes published before September 2026 remain available in the [Apigee Edge release notes archive](https://docs.apigee.com/release/notes/apigee-release-notes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
