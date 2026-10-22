---
url: https://docs.cloud.google.com/docs/security/respond-to-abuse-misuse/
title: Respond to abuse notifications and warnings in Google Cloud \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:05.007478+00:00
---

# Respond to abuse notifications and warnings in Google Cloud  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/respond-to-abuse-misuse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



#  Respond to abuse notifications and warnings in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

To help keep Google Cloud systems and our customers safe, we work to ensure that our products are used in the intended manner and that our platform isn't misused or abused. As described in the [Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice), we work to protect against the violations defined in the [Terms of Service](https://cloud.google.com/terms/) and [Acceptable Use Policy](https://cloud.google.com/terms/aup).

Examples of abuse or misuse include the following issues:

  * Potentially compromised service account credentials
  * Potentially compromised API keys
  * Cryptocurrency alerting
  * Malware or unwanted software
  * Phishing



Google Cloud has a dedicated team of engineers and security experts who work to protect our systems and customers. When Google becomes aware of abusive activity, we notify affected customers and take measures to help prevent future abuse. We strive to ensure that our interventions don't impact your critical work. For more information, see [Project suspension guidelines](https://docs.cloud.google.com/resource-manager/docs/project-suspension-guidelines).

This page describes what you can do if you receive a notification about abuse or misuse from us.

## Respond to an abuse notification

If you receive an abuse notification or warning, you must promptly address or remedy any violations that are noted in the notification and review the Terms of Service and Acceptable Use Policy.

You can check your [Google Cloud abuse logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface) and troubleshoot your environment using the diagnostic tools that are part of Google Cloud (such as Security Command Center).

If you're locked out of your account, see [Account lockouts](https://docs.cloud.google.com/docs/security/compromised-credentials#account-lockouts).

## Example issues and responses

This section includes examples that describe how to remediate and respond to issues that might have caused an alert. If you cannot resolve the issue on your own, and you have a [Cloud Customer Care package](https://docs.cloud.google.com/support), contact [Customer Care](https://enterprise.google.com/supportcenter/managecases). You can also consult the [Google Cloud Community Forum](https://www.googlecloudcommunity.com/gc/Google-Cloud/ct-p/google-cloud) to help resolve issues.

### Potentially compromised service account credentials

An alert for detected leaked credentials indicates that your organization might have inadvertently published the specified service account credentials in public repositories or websites.

To resolve this issue, complete the following steps:

  1. In the Google Cloud console, review the activity on your account.

[Go to Dashboard](https://console.cloud.google.com/home/dashboard)

  2. Revoke all credentials for the compromised service accounts. Rotate all credentials in the affected projects because every resource that is accessible to the service account might have been affected. For instructions, see [Handling compromised Google Cloud credentials](https://cloud.google.com/security/compromised-credentials).

  3. Delete all unauthorized VMs or resources.

  4. Verify that your service account credentials are not embedded in public repositories, stored in download directories, or unintentionally shared in other ways.




To help protect your organization against compromised credentials, see [Best practices to avoid compromised credentials](https://docs.cloud.google.com/docs/security/compromised-credentials#best_practices_to_avoid_compromised_credentials).

### Potentially compromised API keys

An alert for detected compromised API keys indicates that your organization might have inadvertently published the affected API key in public repositories or websites.

To resolve this issue, complete the following steps:

  1. If this key is supposed to be public, complete the following steps:

     1. In the Google Cloud console, review the API and billing activity on your account. Verify that the usage and billing are what you expect.

[Go to Dashboard](https://console.cloud.google.com/home/dashboard)

     2. If applicable, add [API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions) to your API key.

  2. If this key isn't supposed to be public, complete the following steps:

     1. In the Google Cloud console, generate a new API key. For instructions, see [Regenerate API keys](https://docs.cloud.google.com/docs/security/compromised-credentials#regenerate_api_keys)
     2. Verify that your API keys are not embedded in public repositories, stored in download directories, or unintentionally shared in other ways.
     3. If applicable, add [API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions) to your API key.
     4. If you're using Google Maps APIs, see [Google Maps Platform security guidance](https://developers.google.com/maps/api-security-best-practices).



To help protect your organization against compromised credentials, see [Best practices to avoid compromised credentials](https://docs.cloud.google.com/docs/security/compromised-credentials#best_practices_to_avoid_compromised_credentials).

### Cryptocurrency mining

This alert indicates that a project is engaged in cryptocurrency mining. This issue is usually preceded by a compromise, such as a leaked service account credential, that grants a bad actor access to your Google Cloud project.

To resolve this issue, complete the following steps:

  1. In the Google Cloud console, review the project's activity.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Terminate any unauthorized cryptomining activity and take measures to secure your account and any affected projects.

  3. If you have suspended resources, you can submit an appeal to regain access.




To help protect your organization against cryptocurrency mining attacks, see [Mitigate cryptocurrency mining attacks on Google Cloud](https://docs.cloud.google.com/docs/security/bps-for-protecting-against-cryptocurrency-attacks).

### Malware or unwanted software

This alert indicates that your organization includes a project that hosts, distributes, or facilitates distribution of [malware, unwanted software, or viruses](https://developers.google.com/search/docs/advanced/security/malware). To resolve this issue, complete the following steps:

  1. Remove any malicious content and mechanisms from your projects.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Verify that your project wasn't compromised by checking its usage and logs.

  3. If necessary, [shut down (delete) your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

  4. To regain access to your suspended resources, submit an appeal.




To help protect your organization against malware or unwanted software, see [Mitigate ransomware attacks using Google Cloud](https://docs.cloud.google.com/docs/security/mitigating-ransomware-attacks).

If your site has a red browser warning, it was identified by Google's [Safe Browsing program](https://safebrowsing.google.com/) as malicious. Safe Browsing operates separately from Google Cloud. You can [submit a review request](https://developers.google.com/search/docs/monitor-debug/security/malware#fixing-the-problem) for the page using the Search Console. For more information, see [Google Search Console](http://search.google.com/search-console) and [Get started with Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start).

### Phishing

This alert indicates that [phishing or deceptive social engineering](https://developers.google.com/search/docs/monitor-debug/security/social-engineering) content was published from your Google Cloud project. Hackers might try to take control of your site and use it to host deceptive content.

To resolve this issue, complete the following steps:

  1. Remove any phishing content and mechanisms from your projects.
  2. Verify that your project wasn't compromised by checking its usage and logs.
  3. If necessary, [shut down (delete) your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).
  4. To regain access to your suspended resources, submit an appeal.



If your site has a red browser warning, it was identified by Google's [Safe Browsing program](https://safebrowsing.google.com/) as malicious. Safe Browsing operates separately from Google Cloud. You can [submit a review request](https://developers.google.com/search/docs/monitor-debug/security/malware#fixing-the-problem) for the page using the Search Console. For more information, see [Google Search Console](http://search.google.com/search-console) and [Get started with Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start).

## Submit an appeal

You can submit an appeal to Google Cloud after you receive a warning or suspension notification and complete the remediation steps so that you can restore access to services.

To submit an appeal, in the Google Cloud console, select the project and access the **Appeals** page for the project. Ensure that your response includes the following:

  * What caused the issue.
  * The steps that you've taken to resolve the issue.
  * Whether the behavior was intentional.
  * Your [billing account ID](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-id).
  * Whether your project was compromised.



If you see an error message telling you that you don't have sufficient permission to access the page, verify that you're logged in as the project owner and have the [appropriate IAM permissions to edit the project](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). If you're logged into multiple accounts, log out of all other accounts and try logging in again.

**Note:** If you don't respond to the warning in a timely manner, your project might be suspended in accordance with the Terms of Service.

After you submit your appeal, Google Cloud reviews your appeal and responds back with a resolution and final disposition.

## Report suspected abuse

The protection of your data and workloads is a [shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate). You must actively monitor your Google Cloud environment and implement appropriate security controls and best practices. If you believe that your Google Cloud services are being abused, take immediate action to secure any affected services and accounts and report the abuse to [Google Cloud Customer Care](https://support.cloud.google.com/portal/). As described in the Terms of Service, we investigate reports of unauthorized financial charges that are related to abuse or compromise. You are financially responsible for charges that result from improperly secured resources.

To report an issue that isn't related to your services, use the [Report suspected abuse on Google Cloud](https://support.google.com/code/contact/cloud_platform_report) form.

## Best practices to help protect yourself from abuse

To help protect yourself from abuse on Google Cloud, consider the following:

  * Use strong passwords and enable two-factor authentication for your Google Cloud accounts. For more information, see [Single sign-on](https://docs.cloud.google.com/architecture/identity/single-sign-on).

  * Be careful about which third-party applications are granted access to your Google Cloud resources, and the authentication method they use. For more information about securing applications, see [Use IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely) and [Authentication methods at Google](https://docs.cloud.google.com/docs/authentication).

  * Monitor third-party software to help ensure that your project doesn't become compromised by vulnerabilities in third-party software you have installed. For more information on security best practices, see the [Securing instances](https://support.google.com/cloud/answer/6262505#gcp-instance) section of the Cloud Security FAQ.

  * If your primary business is to host third-party content or services or facilitate the sale of goods and services between third parties, enforce compliance with the Google Cloud Acceptable Use Policy. Implement the following:

    * Publish policies that define what content is prohibited on your platform.
    * Maintain a reporting intake process (for example, a webform or email alias) to receive notices of illegal or abusive content (in addition to a monitored communication channel for Google).
    * Promptly review and address any alerts, and remove content where appropriate.
  * Implement logging and detective controls and [monitor your Google Cloud logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs) for suspicious activity. For more information, see the following:

    * [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit)

    * [Google Cloud platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs)

    * [Network Intelligence Center overview](https://docs.cloud.google.com/network-intelligence-center/docs/overview)

    * [Sensitive Data Protection overview](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)

  * Use [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) to help identify vulnerabilities in your environment and remediate them.

  * Add contacts to the following [Essential Contacts categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories) for your projects so that you know as soon as your project is warned:

    * Security
    * Technical
    * Suspension
    * All
  * Make sure that email messages from `google-cloud-compliance@google.com` don't go to a spam folder.




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
