---
url: https://docs.cloud.google.com/apigee/docs/api-security/aas-apigee-overview/
title: Advanced API Security enabled from your Apigee instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:50:29.906934+00:00
---

# Advanced API Security enabled from your Apigee instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/aas-apigee-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Advanced API Security enabled from your Apigee instance Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes Advanced API Security features and functionality when enabled from your Apigee instance.

This product includes GeoLite Data created by MaxMind, available from [https://www.maxmind.com](https://www.maxmind.com/).**Note:** To use Advanced API Security you must first [provision Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro). When Apigee is successfully provisioned, you can [set up and enable Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security/enable-security).

The diagram below illustrates how Advanced API Security works.

![Overview of Advanced API Security.](https://docs.cloud.google.com/static/apigee/docs/api-security/images/api-security-overview.png)

Advanced API Security continually monitors your APIs to protect them from security threats, including attacks from malicious clients and abuse. Advanced API Security analyzes your API traffic to identify suspicious API requests, and provides tools to block or flag those requests if you decide to do so. In addition, Advanced API Security evaluates your API configurations to ensure they meet security standards, and gives you recommendations for improving them if needed.

Advanced API Security uses the following process to protect your APIs:

  1. Advanced API Security collects data for recent traffic passing through your APIs.
  2. Advanced API Security analyzes the data to detect unusual traffic patterns that indicate a threat to your APIs.
  3. Advanced API Security presents the results of the analysis in following pages in the Apigee UI: 
     * Abuse detection
     * Security reports
     * Risk assessment
  4. After reviewing the analysis, you can choose to block or flag requests from specific IP addresses using the security actions page. You can also create security alerts, which notify you of events related to Advanced API Security.



Note that Advanced API Security does not support APIs running under [Apigee Adapter for Envoy](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter).

## Use Advanced API Security

Advanced API Security is available as a paid add-on for the following organization types: 

  * Apigee Subscription and Pay-as-you-go organizations
  * Apigee hybrid organizations
  * Apigee organizations with [data residency enabled.](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) See [Data residency and Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-and-apigee-hybrid) for information on use with DRZ-enabled hybrid organizations.



To use Advanced API Security, you must first enable it, as described in the following sections: 

  * [ Manage Advanced API Security for Pay-as-you-go organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-pay-as-you-go-organizations)
  * [ Manage Advanced API Security for Subscription organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-subscription-organizations)



You can try Advanced API Security for free in any trial organization. Contact [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html) to learn more.

## Advanced API Security features

The following sections briefly describe the features of Advanced API Security.

### Abuse detection

[Abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection) shows you security incidents involving your APIs. A security incident is a group of detected security events that are related to each other. Advanced API Security uses [detection rules](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules), based on Google's machine-learning algorithms, to identify patterns that are signs of malicious activity, including API scraping and anomalies. You can then take measures to counter those threats using security actions.

### Security reports

[ Security reports](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs) give you more in-depth analysis of security threats to your APIs. For example, you can create reports for the number of malicious requests by various dimensions, such as the country of origin of the request. You can view these reports in the Apigee UI or via the API.

### Risk assessment

[Risk assessment](https://docs.cloud.google.com/apigee/docs/api-security/security-scores) helps you identify APIs that don't conform to security standards. Risk assessment regularly evaluates your API configurations and calculates scores to rate their security level. When a low score indicates a configuration issue, Advanced API Security provides recommendations to resolve the problem.

### Security actions

[Security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) let you define how Apigee handles detected traffic, based on information from the Abuse detection page. For example, you can create a security action to deny requests from an IP address that has been identified as a source of abuse.

### Security alerts

You can configure [security alerts](https://docs.cloud.google.com/apigee/docs/api-security/security-alerts) to send you notifications when Advanced API Security detects events related to Advanced API Security, such as changes to your security scores or security incidents.

## Data obfuscation with Advanced API Security

Advanced API Security works with data that is obfuscated to replace sensitive data with a hashed value. See [Obfuscate user data for Apigee API Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/obfuscate-user-data-for-analytics) for information on the data obfuscation functionality.

When obfuscation is configured, Advanced API Security checks such as in Abuse detection and Security actions are applied before the obfuscation. For example, it's possible to detect abuse from a specific IP address even if the IP address is obfuscated. However, obfuscated values (such as client IP address) are not viewable to users in clear (unhashed) text within the Advanced API Security UIs or APIs. The hashed values are shown. 

In some cases you need to obtain an unobfuscated data value to use with Advanced API Security. For example, you might need a client IP address to configure a Security action. If the value is already obfuscated, you can't retrieve the clear text IP address. Using the obfuscated (hashed) value in the Security action configuration doesn't work since data obfuscation uses a one-way hash and Advanced API Security cannot convert the hashed value back to the clear text value. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
