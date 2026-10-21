---
url: https://docs.cloud.google.com/assured-workloads/docs/monitor-frameworks/
title: Monitor Assured Workloads frameworks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:51.409285+00:00
---

# Monitor Assured Workloads frameworks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/monitor-frameworks/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor Assured Workloads frameworks

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Applicable only for[Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview)_ **Note:** Before deploying or monitoring Assured Workloads frameworks, you must be added to an allowlist. Request access to the allowlist by filling out [the sign-up form](https://forms.gle/JsX7kziFjEGsDhcQ8).

Assured Workloads actively monitors your framework deployments for compliance violations by comparing a deployed [data boundary's](https://docs.cloud.google.com/assured-workloads/docs/data-boundaries) requirements to the folder or project to which it's assigned. When your folder or project drifts from one or more of the data boundary's cloud control requirements, a violation occurs. Violation types include the following:

  * **Location** : When a child resource in an assigned folder or project is deployed to a non-compliant location, a violation occurs. This violation can occur by modifying a default value for the _Restrict Resource Locations_ cloud control for a given framework, which is mapped to the [`gcp.resourceLocations`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) organization policy constraint.
  * **Service usage** : When a non-compliant service endpoint (such as `compute.googleapis.com`) is enabled on an assigned folder or project, a violation will occur. This violation can occur if you modify the default value for the _Restrict Service Usage_ cloud control for a given framework, which is mapped to the [`gcp.restrictServiceUsage`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy constraint.
  * **Encryption** : Some data boundaries require [Customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek) set to a specific set of service endpoints. To enforce this requirement, the _Enforce CMEK for Supported Services_ cloud control is applied. If you add non-compliant services or remove existing or required services from this cloud control, a violation will occur. This violation is mapped to the [`gcp.restrictNonCmekServices`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek) organization policy constraint.
  * **Access** : Some data boundaries require [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval) or [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency), which together help you authorize requests from Google personnel to access Customer Data and determine when and why such data was accessed. When you modify these cloud controls, for example, by changing the default values for the _Enable Access Transparency_ cloud control, you can cause a violation to occur.
  * **Configuration** : Changing a cloud control value to a non-compliant value can cause a violation to occur.



When a violation occurs, you can resolve it or create exceptions for it where appropriate. A violation can have one of three statuses:

  * **Unresolved:** The violation hasn't been addressed, or was previously granted an exception before non-compliant changes were made on the folder or resource.
  * **Resolved:** The violation has been addressed by following steps to remediate the issue.
  * **Exception:** The violation has been granted an exception, and a business justification has been provided.



Monitoring is automatically enabled when you apply an Assured Workloads framework to a resource.

## View violations in your organization

To view specific compliance violations and their details, complete the following steps:

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/compliance/monitoring/preview/violations)

  2. If prompted, select your organization.

  3. Click the **Assured Workloads Violations** tab. Two tabs are shown: **Organization Policy Violations** and **Resource Violations**. If more than one unresolved violation exists, the error icon is active on the tab.

The **Organization Policy Violations** tab is selected by default. This tab displays all unresolved organization policy violations across Assured Workloads frameworks folders or projects in the organization.

The **Resource Violations** tab displays all unresolved violations associated with the resource across all Assured Workloads frameworks folders or projects in the organization.

  4. For either tab, use the **Quick filters** options to filter by violation status, violation type, assignment, affected frameworks, organization policy control, or specific resource types.

  5. For either tab, if there are existing violations, click a violation ID to see more detailed information.




From the **Violation details** page, you can perform the following tasks:

  * Copy the violation ID.

  * View the Assured Workloads framework's resource where the violation occurred and when it first occurred.

  * View the audit log, which includes the following:

    * When the violation happened.

    * Which policy was modified to cause the violation and which user made that modification.

    * If an exception was granted, which user granted it.

    * Where applicable, view the specific resource that the violation occurred on.

  * View the affected organization policy.

  * View and add compliance violation exceptions. Previous exceptions for the resource are listed. These exceptions include the user that granted the exception, its user-provided justification, and the time it was granted.

**Note:** If any additional non-compliant changes are made beyond the scope of the original exception, a new unresolved violation will occur. Information about the new unresolved violation and its cause will be shown on this page.
  * Follow the remediation steps to resolve the exception.




For organization policy violations, you can also see the following:

  * **Affected organization policy** : To view the policy associated with the compliance violation, click **View Policy**.
  * **Child resource violations** : Resource-based organization policy violations can cause child resource violations. To view or resolve child resource violations, click the **Violation ID**.



For resource violations, you can also see the following:

  * **Parent organization policy violations** : When parent organization policy violations are the cause of a child resource violation, they need to be addressed first at the child level. Once the child resource violation has been resolved, then resolve the parent organization policy violation. To see the violation details, click **View Violation**.
  * Any other violations on the specific resource that is causing the resource violation are also visible.



## Resolve violations

To remediate a violation, complete the following steps:

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/compliance/monitoring/preview/violations)

  2. If prompted, select your organization.

  3. Click the **Assured Workloads Violations** tab. Two tabs are shown: **Organization Policy Violations** and **Resource Violations**. If more than one unresolved violation exists, the error icon is active on the tab. Click the tab for which you want to view violations.

  4. Click the **Violation ID** to see more detailed information.

  5. In the **Remediation** section, follow the instructions to address the issue.




## Add violation exceptions

Sometimes a violation might be valid for a particular situation. You can acknowledge one or more violations by completing the following steps to add an exception.

**Note:** If you've previously granted a violation exception, its state can change back to **unresolved** if any additional non-compliant changes are made.

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/compliance/monitoring/preview/violations)

  2. If prompted, select your organization.

  3. Click the **Assured Workloads Violations** tab. Two tabs are shown: **Organization Policy Violations** and **Resource Violations**. If more than one unresolved violation exists, the error icon is active on the tab.

The **Organization Policy Violations** tab is selected by default. This tab displays all unresolved organization policy violations across Assured Workloads frameworks folders or projects in the organization.

The **Resource Violations** tab displays all unresolved violations associated with the resource across all Assured Workloads frameworks folders or projects in the organization.

Click the tab for which you want to view violations.

  4. From the list of violations, select one or more that you want to add an exception for. You can acknowledge up to 100 organization policy violations and up to 400 resource violations in a single operation. Click **Acknowledge**.

  5. Enter a business justification for the exception. If you selected more than one violation, this exception will apply to all of them. For organization policy violations, if you want the exception to apply to all child resources, select the **Apply to all existing child resource violations** checkbox. Click **Submit**.




The violation status is now set to **Exception**.

## What's next

  * Understand the available [frameworks and data boundaries](https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview#built-in-frameworks) for Assured Workloads.
  * Learn which [products are supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) for each data boundary.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
