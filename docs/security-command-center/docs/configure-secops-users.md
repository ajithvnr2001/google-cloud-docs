---
url: https://docs.cloud.google.com/security-command-center/docs/configure-secops-users/
title: Control access to features in Security Operations console pages \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:12.958433+00:00
---

# Control access to features in Security Operations console pages  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/configure-secops-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Control access to features in Security Operations console pages Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The Security Command Center Enterprise tier includes certain features available from Google Security Operations. You investigate and remediate vulnerabilities, misconfigurations, and threats using both [Google Cloud console and Security Operations console](https://docs.cloud.google.com/security-command-center/docs/scce-consoles-overview) pages.

Security Command Center Enterprise users need IAM permissions to access Security Command Center features in both the Google Cloud console and Security Operations console pages.

Google Security Operations has a set of predefined IAM roles that let you access [SIEM-related features](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#overview-perm-role) and [SOAR-related features](https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops#grant-iam-roles-in-the-google-cloud-console) in Security Operations console pages. You can grant the Google Security Operations roles at the project level.

Security Command Center has a set of predefined IAM roles that let you access features in Security Operations console pages that are unique to the Security Command Center Enterprise tier. These include the following:

  * [Security Center Admin Editor Viewer (`roles/securitycenter.adminEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor)
  * [Security Center Admin Viewer (`roles/securitycenter.adminViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer)



To view Security Command Center features available in Security Operations console pages, users need at least the **Security Center Admin Viewer** (`roles/securitycenter.adminViewer`) role. Grant the Security Command Center roles at the organization level.

As you plan the deployment, review the following to identify which users need access to features:

  * To grant user access to features and findings in the Google Cloud console, see [Access control with IAM](https://docs.cloud.google.com/security-command-center/docs/access-control).

  * To grant user access to SIEM-related threat detection and investigation features in Security Operations console pages, see [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#overview-perm-role).

  * To grant users access to SOAR-related response features in Security Operations console pages, see [Map IAM roles in the SOAR side of the Security Operations console](https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops). You also map the SOAR-related IAM roles to SOC roles, permission groups, and environments under **SOAR settings**.

  * To create custom IAM roles using Google SecOps IAM permissions, see [Create and assign a custom role to a group](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#custom-role).

  * To access features available with Security Command Center Enterprise, such as the [Posture Overview page](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-manage#view_an_overview_of_all_toxic_combination_cases), grant users the [required IAM roles](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#required_permissions) in the organization where Security Command Center Enterprise is activated.




The steps to grant access to features is different depending on the identity provider configuration.

  * If you use Google Workspace or Cloud Identity as the identity provider, you grant roles directly to a user or group. See [Configure a Google Cloud identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication) for an example of how to do this.

  * If you use Workforce Identity Federation to connect to a third-party identity provider (such as Okta or Azure AD), you grant roles to identities in a workforce identity pool or to a group within the workforce identity pool.

See [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access) for examples of how to grant SIEM-related features and SOAR-related features to a workforce identity pool.

Make sure the workforce pools include permissions to access Security Command Center-specific features in Security Operations console pages. The following are examples:

    * To grant the Security Center Admin Viewer role to all users in a workforce identity pool, run the following command:
          
          gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
              --role roles/securitycenter.adminViewer \
              --member "principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/*" \
              --condition None
          

Replace the following:

      * `ORGANIZATION_ID`: the numeric organization ID.
      * `WORKFORCE_POOL_ID`: the value you defined for the workforce identity pool ID.
    * To grant the Security Center Admin Viewer roles to a specific group, run the following commands:
          
          gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
              --role roles/securitycenter.adminViewer \
              --member "principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID" \
              --condition None
          

Replace `GROUP_ID`: a group in the mapped `google.groups` claim.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
