---
url: https://docs.cloud.google.com/chronicle/docs/detection/mandiant-threat-defense-rbac/
title: Mandiant Threat Defense and RBAC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:56:25.766136+00:00
---

# Mandiant Threat Defense and RBAC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/mandiant-threat-defense-rbac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mandiant Threat Defense and RBAC

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

Mandiant Threat Defense uses a two-tier Role-Based Access Control (RBAC) system. This setup balances granular feature management with security requirements, ensuring that users possess both the appropriate feature permissions and data scopes to access Mandiant Threat Defense investigation reports.

## Data-based access control

To view Mandiant Threat Defense investigations, users must have the `chronicle.globalDataAccessScopes.permit` permission. If this permission is missing, Mandiant Threat Defense remains hidden, even if the user has feature-level roles.

For more information, see [Data RBAC overview](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

## Feature-based access control

Feature-based access control relates to specific actions, such as viewing or commenting, using Google Cloud Identity and Access Management (IAM) permissions.

The following roles grant full data access: `chronicle.viewer` and `chronicle.editor`. To restrict access, create a Custom Role in the Google Cloud console, and remove permissions, such as `chronicle.investigations.get` or `chronicle.investigationComments.create`.

For more information, see [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).

## Investigation status and attachments

Users that you configure with the appropriate control permissions can do the following:

  * **Investigation status:** Update investigation statuses, such as `Open` or `Closed`, directly within the interface.
  * **Attachments:** View and securely download evidence and supporting files attached to investigations.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
