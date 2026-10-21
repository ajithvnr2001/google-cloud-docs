---
url: https://docs.cloud.google.com/security-command-center/docs/respond-ai-threats/
title: Respond to AI threat findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:38.625793+00:00
---

# Respond to AI threat findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/respond-ai-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Respond to AI threat findings Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document offers informal guidance on how you can respond to findings of suspicious activities in your AI resources. The recommended steps might not be appropriate for all findings and might impact your operations. Before you take any action, you should investigate the findings; assess the information that you gather; and decide how to respond.

**Note:** The techniques that Security Command Center provides aren't guaranteed to be effective against any previous, current, or future threats that you face. For information about why Security Command Center does not provide official remediation guidance for threats, see [Approach to threat finding remediation](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#remediating_threats).

## Before you begin

  1. [Review the finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings). Note the affected resources and the detected binaries, processes, or libraries.
  2. To learn more about the finding that you're investigating, search for the finding in the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).



## General recommendations

  * Contact the owner of the affected resource.
  * Work with your security team to identify unfamiliar resources, including Agent Runtime instances, sessions, service accounts, and [agent identities](https://docs.cloud.google.com/agent-builder/agent-engine/agent-identity). Delete resources that were created with unauthorized accounts.
  * To identify and fix overly permissive roles, use [IAM Recommender](https://docs.cloud.google.com/iam/docs/recommender-overview). Delete or disable potentially compromised accounts.
  * For the Standard-legacy, Standard, Premium, and Enterprise (Deprecated) service tiers, investigate any [identity and access findings](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-findings#ciem-findings).
  * For further investigation, you can use incident response services, for example, [Mandiant](https://cloud.google.com/security/consulting/mandiant-incident-response-services).
  * For forensic analysis, collect and back up the logs of affected resources.



## Potentially compromised service account or agent identity

  * To remove a compromised agent identity, [delete its corresponding Agent Runtime instance](https://docs.cloud.google.com/agent-builder/agent-engine/manage/overview#delete).

  * [Disable the potentially compromised service account](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#disabling). For best practices, see [Disable unused service accounts before deleting them](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#disable-before-delete).

  * [Disable service account keys](https://docs.cloud.google.com/iam/docs/keys-disable-enable#disabling) for the potentially compromised project.

  * To see when your service accounts and keys were last used to call a Google API, use Activity Analyzer. For more information, see [View recent usage for service accounts and keys](https://docs.cloud.google.com/policy-intelligence/docs/activity-analyzer-service-account-authentication).

  * If you are confident that it is safe to delete the service account, [delete](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#deleting) it.

**Note:** If the compromised service account is a Agent Runtime [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), you can't directly delete it. In this case, ensure that the service agent doesn't have more permissions than it needs.
  * To use organization policies to restrict service account usage, see [Restricting service account usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts).

  * To use Identity and Access Management to restrict service account or service account key usage, see [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access).




## Exfiltration and extraction

  * [Revoke roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) for the principal that is listed in the **Principal email** row in the finding details until the investigation is complete.
  * To stop further exfiltration, add restrictive IAM policies to the affected resources.
  * To determine whether the affected datasets have sensitive information, [inspect them with Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage). You can configure the inspection job to send the results to Security Command Center. Depending on the quantity of information, Sensitive Data Protection costs can be significant. Follow best practices for [keeping Sensitive Data Protection costs under control](https://docs.cloud.google.com/sensitive-data-protection/docs/best-practices-costs).
  * Use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to create security perimeters around data services like BigQuery and Cloud SQL to prevent data transfers to projects outside the perimeter.



## Suspicious token generation

  * Validate the need for cross-project token generation. If it's unnecessary, remove the IAM role binding in the target project that grants the `iam.serviceAccounts.getAccessToken`, `iam.serviceAccounts.getOpenIdToken`, `iam.serviceAccounts.implicitDelegation`, or `iam.serviceAccounts.signJwt` permission to the principal from the source project.

  * Investigate the logs that are specified in the finding to validate the token generation methods used by your agentic workloads.




## Sensitive IAM roles or permissions granted

  * Use Organization Policy Service to [restrict identities with domain-restricted sharing](https://docs.cloud.google.com/organization-policy/restrict-domains).
  * To identify and fix overly permissive roles, use [IAM Recommender](https://docs.cloud.google.com/iam/docs/recommender-overview).



## What's next

  * Learn [how to work with threat findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).
  * Learn how to [review a finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings) through the Google Cloud console.
  * Learn about the [services that generate threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#threats).


  * Refer to a [list of all AI findings](https://docs.cloud.google.com/security-command-center/docs/ai-threats).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
