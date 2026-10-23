---
url: https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy/
title: Standard tier enhanced and automatically activated for some customers \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:24:53.547169+00:00
---

# Standard tier enhanced and automatically activated for some customers  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Standard tier enhanced and automatically activated for some customers Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy and Standard [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Starting February 11, 2026, the Security Command Center Standard tier will be migrated to a new set of capabilities. For a summary of the differences, see Differences between Standard and Standard-legacy tiers. To see the services that are available in each tier, see [Service tier comparison](https://docs.cloud.google.com/security-command-center/docs/service-tiers#comparison).

After Security Command Center Standard is migrated, some organizations and projects that are using the Standard tier will see new features and an update to the supported [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).

In addition, Security Command Center Standard will be automatically activated in some organizations where it isn't yet activated and that don't have data residency requirements.

The Standard tier migration and auto-activation process will occur over multiple months. This document provides more information and describes what to expect during the Standard tier migration and auto-activation process.

## Differences between Standard and Standard-legacy tiers

This section explains the differences in capabilities between the Standard and Standard-legacy tiers.

The following features are now available in the Standard tier:

  * [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview)
  * [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview)
  * [Data Security Posture Management](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security)
  * [Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud)
  * [Mandiant CVE assessments](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#mandiant-cve-assessment)



The following Standard-legacy tier features aren't supported in the Standard tier:

  * [Sensitive Data Protection discovery service](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery)
  * [Web Security Scanner custom scans](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans)



A modified set of Security Health Analytics capabilities is available in the Standard tier. For more information, see Security Health Analytics detectors migrated to Compliance Manager controls.

To view the services and features available with all tiers, see [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

## Overview of the Standard tier migration and auto-activation process

You might see the new features in your Security Command Center Standard activation if one of the following applies to your organization:

  * The Security Command Center Standard tier is already activated in your organization and the Premium tier isn't activated on any project in the organization.
  * The Security Command Center Standard tier is already activated for any project in the organization. You will see the new Security Command Center Standard tier capabilities in those projects.



Security Command Center Standard tier might be automatically activated at the organization level in the global region if Security Command Center hasn't been activated at the organization level, and both of the following scenarios apply:

  * The Premium tier isn't activated on any project within the organization.
  * The organization doesn't have data residency requirements, meaning it doesn't restrict resource locations using the [resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).



If you don't have Security Command Center activated in your organization, and the Standard tier isn't activated automatically, you can activate Security Command Center Standard manually. You get Security Command Center Standard-legacy features initially. Your organization will be migrated to the new Standard tier features at a later date.

After your organization or project is automatically migrated to new Standard tier features, the unsupported Standard-legacy tier services are disabled.

During manual activation, you specify the global region or one of the supported jurisdictions. For information, see Data residency considerations after the Standard tier is auto-activated.

## Organizations that aren't included in this change

If your organization has any of the following configurations, your organization isn't automatically activated with the Security Command Center Standard tier:

  * Your organization has an Enterprise tier activation.

  * Your organization has a Premium tier activation at either the organization level or project level. This type of activation includes the following:

    * Your organization has the Standard tier activated at the organization level and the Premium tier activated on any project. These organizations continue to see Standard-legacy features.

    * Your organization doesn't have any Security Command Center tier activated at the organization level and has the Premium tier activated on one or more projects. Security Command Center Standard isn't automatically activated in these organizations. To use Security Command Center Standard, you can activate it manually.

  * Your organization doesn't have any Security Command Center tier activated at the organization level and has data residency requirements, identified by at least one organization policy that restricts resource locations using a [resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). Security Command Center Standard isn't automatically activated in these organizations and must be activated manually.




For information about how to activate the Standard tier manually, see [Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier).

## Changes to organizations that are included in this change

The following sections describe changes and additional configuration if your organization is enabled with Standard tier features. This scenario includes the following scenarios:

  * You were using the Standard tier before February 11, 2026, and the features were migrated to the new set of capabilities.

  * Your organization was automatically activated with the Standard tier.

  * You manually activated the Standard tier after February 11, 2026, and then your organization was migrated to the new set of capabilities.




### Changes in Google Cloud console

The first time you access Security Command Center after the organization is migrated to the new Standard tier features, you will see the **Security insights are now enabled at no additional cost** prompt. If you click **Close** , this prompt doesn't reappear.

You can view the following in the Google Cloud console:

  * [AI Security dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection) on the **Risk Overview** page
  * [Data dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#data) on the **Risk Overview** page
  * [Compliance](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#compliance-page) page



Some features on these pages are disabled because the service that provides data must be manually enabled or configured.

If you're using Compute Engine or Google Kubernetes Engine, and Security Command Center generated findings for these resources, you'll see data in the [Compute Engine Security risk overview dashboard](https://docs.cloud.google.com/compute/docs/monitor-security-risks-console).

You can enable Vulnerability Assessment for Google Cloud and AI Protection on the **Settings > Services** page in Security Command Center.

For information about how to use Security Command Center, see [Use Security Command Center in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).

There might be a delay before data appears on these pages. To learn more, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).

### Services that aren't automatically enabled

The Standard tier migration and auto-activation process enables some services automatically. The following services in the Standard tier might require that you enable them manually or perform additional configuration:

  * [Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud):

    * If the Standard tier is newly activated in your organization, you must enable this service manually.

    * If your organization was migrated from the Standard-legacy tier to the Standard tier, this service is enabled automatically.

  * [Model Armor](https://docs.cloud.google.com/model-armor/overview): If you weren't using Model Armor before the automatic activation, you must perform [additional configuration](https://docs.cloud.google.com/model-armor/manage-templates).




Services that are automatically enabled generate findings that are based on the individual scan frequency of each service. A delay might occur before scans start for some services. To learn more, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).

### Data residency considerations after the Standard tier is auto-activated

After Security Command Center Standard is automatically activated in your organization, we recommend that you enable Vulnerability Assessment for Google Cloud.

If Security Command Center Standard was automatically activated in your organization, and then you enable an [organization policy that restricts resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), Security Command Center might be automatically deactivated within seven days after the policy is deployed.

Organizations aren't automatically deactivated in the following scenarios:

  * You changed the data residency configuration before enabling the organization policy.
  * You enabled Vulnerability Assessment for Google Cloud after the automatic activation and before deploying an organization policy that restricts resource locations.
  * You upgraded the organization to the Premium tier or Enterprise tier after the automatic activation.



To change the data location or data encryption configuration after the Standard tier is automatically activated for the organization, see [Modify data residency or data encryption configuration](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption).

If Security Command Center is automatically deactivated, existing findings remain stored and unchanged in the `global` region until they are deleted as defined in the [Data retention for findings policy](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention). You can't access these findings unless you reactivate Security Command Center in the `global` region.

To continue using Security Command Center, you must reactivate Security Command Center manually. For instructions, see [Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier).

When you manually activate Security Command Center, you choose the data residency configuration. If you don't enable data residency, Security Command Center is activated in the `global` region and you can access the previously created findings.

When you enable data residency, you also configure [supported data locations](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#security-command-center-locations).

If you enable data residency, you can't view previously created findings because they are stored in the global region and you configured a specific data location.

During manual activation, Security Command Center doesn't restrict your data residency configuration when the configuration conflicts with organization policies that limit resource locations.

### Security Health Analytics detectors are migrated to Compliance Manager controls

On the Standard tier, most Security Health Analytics detectors are migrated to Compliance Manager controls in the [Security Essentials framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#frameworks-gcp). The Compliance Manager version of these controls also generate findings for the equivalent security scenarios.

Security Health Analytics is enabled and all detectors continue to generate findings, but findings created by a Security Health Analytics detector that has an equivalent Compliance Manager control are labeled with the field-value identifier: `launch_state="LAUNCH_STATE_DEPRECATED"`.

A subset of Security Health Analytics detectors aren't migrated to Compliance Manager controls. Security Health Analytics generates findings from these detectors and they don't have the `launch_state` field set to `LAUNCH_STATE_DEPRECATED`.

The Security Essentials framework in Compliance Manager includes additional controls, beyond those that were migrated from Security Health Analytics. To see all available controls, select **Compliance** > **Monitor New** tab, and then the **Security Essentials** framework in the **Frameworks** panel.

For information about which detectors are migrated to Compliance Manager and which Google Cloud console pages let you investigate findings that are generated by each detector, see [Security Health Analytics features by tier](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#standard-features).

### Status of findings created by services that are no longer supported

Findings created by Standard-legacy tier services that aren't supported in the Standard tier are retained until they are deleted as defined in the [Data retention for findings policy](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).

### Service behavior when you reach the Standard tier feature limits

Certain services might have a limit on usage. When you reach that limit, you might be prompted to upgrade tiers. For information about the behavior when you reach the limit, see the documentation specific to that service.

### Update your integrations with other applications

If you ingest findings from Security Command Center to other services using the API, you might see the following newly available sources:

  * `Compliance Evaluation Service`
  * `Vulnerability Assessment`



Update your ingestion scripts to accept data from these sources.

If you use a search query in another application to view Security Health Analytics findings ingested from Security Command Center, such as in Google Security Operations, and you want to remove findings created by Security Health Analytics detectors that are migrated to Compliance Manager, update the search query to add a term that is equivalent to this Security Command Center finding query term:

`AND NOT launch_state="LAUNCH_STATE_DEPRECATED"`

For more information, see Security Health Analytics detectors are migrated to Compliance Manager controls.

## Changes to new Standard tier activations

When you activate the Security Command Center Standard tier, the features available to you depend on the activation scope.

  * For information about services available at the organization-level, see [Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier#standard-services).

  * For information about services available at the project-level, see [Activate Security Command Center for a project](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project).




For information about features in all tiers, see [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

For information about differences between the Standard and Standard-legacy tiers, see [Standard tier enhanced and automatically activated for some customers](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy#feature-differences).

## Downgrading from Premium to Standard tier activations

The following section describes what to expect when you downgrade from the Premium tier to the Standard tier.

If you enabled the following services on the Premium tier, they continue to run with a modified set of capabilities. Review the documentation for each service to understand how tier changes affect each service.

  * [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview#switching-tiers)

  * [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable#manage-service-tiers)

  * [Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security#downgrade-tiers)

  * [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#switching-tiers)

  * [Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud#upgrade-downgrade)




After downgrading, you might see Standard-legacy features in the Google Cloud console until your organization is migrated to the enhanced Standard tier.

## What's next

  * Review the features available in the [Security Command Center Standard tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

  * Use [Security Command Center Standard tier in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
