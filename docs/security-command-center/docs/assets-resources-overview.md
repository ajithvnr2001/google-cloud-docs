---
url: https://docs.cloud.google.com/security-command-center/docs/assets-resources-overview/
title: Assets and resources overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:45.248139+00:00
---

# Assets and resources overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/assets-resources-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Assets and resources overview Stay organized with collections  Save and categorize content based on your preferences. 

In Security Command Center, understanding the difference between resources and assets helps you manage security findings and investigate issues more effectively.

### The difference between a resource and an asset

  * **Resource** : A Google Cloud resource refers to the physical or logical entity that you create in your cloud environment, such as a Compute Engine virtual machine instance, a Cloud Storage bucket, or a BigQuery dataset.
  * **Asset** : An asset is a security-centric representation of a resource that Security Command Center monitors. Security Command Center uses the asset to track the historical state and security context of the resource when the configuration changes.



For more information about resources and assets, see [Asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types).

### The role of Cloud Asset Inventory

Security Command Center uses Cloud Asset Inventory as its primary source of truth for assets. When you use the **Assets** page in the console, the console displays asset metadata and details provided by Cloud Asset Inventory.

After you create, modify, or delete a Google Cloud resource, the change is updated in Cloud Asset Inventory, and then Cloud Asset Inventory sends data to Security Command Center. For more information, see [Inspect assets monitored by Security Command Center](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console).

### Representation of assets in findings

Findings in Security Command Center include information about the affected resource. In the finding details panel, look for fields in the **Affected resource** section, such as **Resource display name** or **Resource full name**. These fields identify which resource has the vulnerability or misconfiguration, or is the target of a threat.

## Ways to work with assets

In Security Command Center, you can use assets to manage findings, prioritize issues, and respond to threats in your environment. You can check, analyze, and manage assets in the following ways:

  * **Inspect and query assets** : view all monitored assets, run custom queries, and inspect specific asset details (such as metadata, IAM policies, and change history) in the Google Cloud console. For more information, see [Inspect assets that are monitored by Security Command Center](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console).
  * **Review and manage findings** : identify the affected resource for a specific security finding, review its context, and follow remediation guidance. For more information, see [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).
  * **Investigate and respond to threats** : investigate compromised resources, correlate asset change history (such as new service accounts or modified IAM policies) with threat detections. For more information, see [Investigating and responding to threats](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).
  * **Examine exposed resources in issues** : to help prioritize and remediate high-severity issues, view the exposed resources that are associated with a detected security issue. For more information, see [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate#view).
  * **Define high-value resource sets** : to classify high-value resource sets (such as production databases or sensitive projects), define resource value configurations. Doing so helps prioritize findings and assess overall attack exposure. For more information, see [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).



## What's next

  * Learn about [supported asset types](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types).
  * [Annotate assets with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
