---
url: https://docs.cloud.google.com/security-command-center/docs/finding-lifecycle-overview/
title: Overview of the finding lifecycle \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:22.669528+00:00
---

# Overview of the finding lifecycle  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/finding-lifecycle-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of the finding lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security Command Center and detection services manage findings through the following phases:

  * Detection: Detection services scan your environment to identify potential security problems, including vulnerabilities, misconfigurations, or threats and generate findings.
  * Triage and remediation: You investigate the root cause and address the underlying problem. After you resolve the problem, you can manually change the finding state to `INACTIVE`, or the detection service might automatically set the finding state to `INACTIVE`.
  * Mute: To reduce noise during an investigation, you can optionally set the mute state of one or more findings to filter them from default dashboards and notification workflows.
  * Retention: Security Command Center stores findings and snapshots according to data retention policies.



## Detection

A [detection service](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) identifies a security condition and creates a finding in Security Command Center. Based on the condition, the service defines the [finding class](https://docs.cloud.google.com/security-command-center/docs/finding-classes). If the detection service doesn't specify a class, the finding class is `Finding class unspecified`.

When a detection service first generates a finding, it sets the [finding state](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.sources.locations.findings#state) to `ACTIVE` with the following properties:

  * **Event time** (`event_time`): the date and time that the service first detected the finding or last updated information in the finding. To minimize noisy notifications, a service might update the `event_time` only when there are meaningful changes to the condition that created the finding, such as when it changes the `state` to `INACTIVE`.
  * **Create time** (`create_time`): the date and time that the detection service created the finding record in Security Command Center.



Security Command Center sets the `create_time` property automatically, and you can't change it manually. The detection service sets the `event_time` property initially, and then might update the value when there is a meaningful change to information about the finding.

## Triage and remediation

To indicate that you remediated a finding, you can manually set the finding `state` to `INACTIVE`.

Some [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) change the finding `state` automatically. Both the finding type and the behavior of the detection service determine whether the service automatically sets the finding state to `ACTIVE` or `INACTIVE`.

If you manually change a finding `state` to `INACTIVE`, and the detection service manages the state, it might reset the value to `ACTIVE` until it identifies that the condition that created the finding has been resolved.

The following sections explain when a detection service might automatically change finding properties.

### Vulnerability and misconfiguration findings

Information in this section describes properties of a finding that you might evaluate when investigating vulnerability and misconfiguration findings.

#### Updates to the `event_time` property

The `event_time` indicates when the service first detected the condition or last updated information about the condition.

In a vulnerability or misconfiguration finding, a detection service might update the `event_time` value when it detects a change to the condition that created the finding and also updates other finding fields. Detection services might not update the `event_time` with each scan.

Because detection services might not update `event_time` with each scan, if a detection service changes a finding's `state` to `INACTIVE` after a specific _active state_ period, the _active state_ period might not align with the `event_time` of the finding in Security Command Center.

Some changes to a finding, such as [muting a finding](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings) and [annotating a finding with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings) don't change the finding `event_time` property.

Security Command Center automatically updates the `event_time` value every 30 days, if no change has occurred, to help ensure that the finding is returned by queries for recent `ACTIVE` findings.

#### Updates to the `state` property

You can remediate vulnerabilities and misconfigurations by doing one of the following:

  * Fix the condition that caused the finding. For example, close an open firewall port, restrict access to the resource, or apply a patch.
  * Delete the affected resource.



If the service identifies that the problem no longer exists or that the resource no longer exists, it automatically changes the finding state from `ACTIVE` to `INACTIVE`.

The time it takes a service to update the finding state depends on several factors, including the following:

  * The frequency of service scans. Each service scans at different intervals. For information about service scan intervals, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).
  * The time that it takes you to permanently delete a resource. For example, projects remain in a _recovery period_ before permanent deletion. For more information, see [Delete a project](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects#shutting_down_projects). A service might not identify that you deleted a resource until the deletion is permanent.
  * The time that it takes Cloud Asset Inventory to update a resource. Depending on the [type of resource](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#data_freshness), it might take time to update information about the resource.

Updates to Microsoft Azure or AWS resources might take longer than updates to Google Cloud resources. For information, see the following:

    * [Finding is returned for a deleted AWS resource](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws#finding-deleted-aws-resource)
    * [Finding is returned for a deleted Azure resource](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure#finding-deleted-azure-resource)
  * A specific time window during which a finding remains `ACTIVE`. Some services, such as [Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud#finding-lifecycle) and [Artifact Registry vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-ar-overview#finding-lifecycle), retain a finding in the `ACTIVE` state for a specific time window.




For information about how a specific detection service manages finding states, see the documentation for that service.

### Threat findings

A [threat finding](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index) identifies suspicious activity in your Google Cloud environment.

You investigate threat findings, determine a suitable way to remediate the condition, and then manually change the finding state to `INACTIVE`. Threat detection services don't automatically set the state of a threat finding to `INACTIVE`. For more information, see [Approach to threat finding remediation](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#remediating_threats).

### Toxic combination and chokepoint findings

Risk Engine creates [Toxic combination and chokepoint findings](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview) during periodic attack path simulations. A toxic combination identifies a set of security-related conditions that could result in access to a high-value resource. A chokepoint identifies a resource where multiple attack paths converge.

For more information about how to change a finding to `INACTIVE`, see [Remediating toxic combinations and chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-manage#remediate).

### Posture violation findings

[Posture violation findings](https://docs.cloud.google.com/security-command-center/docs/finding-classes#posture-violation) identify resource configurations that don't align with your organization's security posture.

For information about how to change the finding state, see documentation specific to the service:

  * For the security posture service, see [Remediate posture findings](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#remediate-findings).

  * For Compliance Manager, see [Monitor your frameworks for compliance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-monitor-framework).




### Error findings

[Error findings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors) identify problems with the configuration of your Security Command Center environment. Configuration problems prevent [detection services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#services) from generating findings. Security Command Center automatically changes error findings to `INACTIVE` when it detects that the configuration problem no longer exists.

### Issues

Risk Engine creates issues to identify security risks in your Google Cloud environment.

For information about the lifecycle of the following issue types, see the respective document:

  * For Correlated Threats issues, see the [Issue lifecycle](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview#issue-lifecycle) section in "Correlated Threats overview".
  * For Toxic combination and Chokepoint issues, see the [Issue lifecycle](https://docs.cloud.google.com/security-command-center/docs/issues-overview#lifecycle) section in "Issues overview".



## Mute findings

You can reduce the volume of findings that you review by muting some findings. This hides the findings from default dashboards and the [default findings query](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#use_the_query_editor). Muted findings continue to be available in Security Command Center, and you can query them.

The [mute state](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.sources.locations.findings#mute) of a finding (`MUTED` or `UNMUTED`) is independent of the [finding state](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.sources.locations.findings#state). You can mute a finding that also has an `ACTIVE` state.

You can't mute [`SCC error`](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#mute-behavior) findings.

For more information about creating mute rules, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

For information about how muting a finding affects toxic combinations and chokepoints, see [Findings that receive attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#findings_that_receive_attack_exposure_scores).

## Retention of findings

Security Command Center retains findings and snapshots for a specific period based on the finding class, state, and service tier.

For more information about data retention and deletion policies across resources, see [Data and infrastructure security overview](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
