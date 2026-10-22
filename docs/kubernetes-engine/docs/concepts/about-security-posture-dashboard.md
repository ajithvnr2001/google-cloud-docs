---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard/
title: About the security posture dashboard \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:54.399390+00:00
---

# About the security posture dashboard  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  About the security posture dashboard Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of the security posture dashboard in the Google Cloud console, which provides you with opinionated, actionable recommendations to improve your security posture. To explore the dashboard yourself, go to the [**Security Posture page**](https://console.cloud.google.com/kubernetes/security) in the Google Cloud console.

## When to use the security posture dashboard

You should use the security posture dashboard if you're a cluster administrator or a security administrator who wants to automate detection and reporting of common security concerns across multiple clusters and workloads, with minimal intrusion and disruption to your running applications. The security posture dashboard integrates with products such as Cloud Logging, and Policy Controller to improve your visibility into your security posture.

If you use VPC Service Controls, you can also [update your perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) to protect the security posture dashboard by adding `containersecurity.googleapis.com` to the list of services.

The security posture dashboard doesn't change any of our responsibilities or your responsibilities under the [shared responsibility model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility#gke). You're still responsible for protecting your workloads.

### Usage as part of a broad security strategy

The security posture dashboard provides insights about your workload security posture at the _runtime phase_ of the software delivery lifecycle. To gain comprehensive coverage of your applications throughout the lifecycle from source control to maintenance, we recommend that you use the dashboard with other security tooling.

GKE offers the security posture dashboard to monitor security in the Google Cloud console.

For more details about other available tooling and for best practices to safeguard your applications from end to end, see [Protect your software supply chain](https://docs.cloud.google.com/software-supply-chain-security/docs/practices).

We also strongly recommend that you implement as many recommendations as possible from [Harden your cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).

## How the security posture dashboard works

To use the security posture dashboard, enable the Container Security API in your project. The dashboard shows you insights from capabilities that are built into GKE and from certain Google Cloud security products running in your project.

### Cluster-specific feature enablement

The GKE-specific capabilities in the security posture dashboard are categorized as follows:

  * **Kubernetes security posture** : The security posture of Kubernetes objects and resources in the cluster, such as Pod specifications. For details, see [About Kubernetes security posture scanning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning).

  * **Workload vulnerability scanning** : The security posture of the container operating system and application language packages. For details, see [About workload vulnerability scanning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-workload-vulnerability-scanning).

**Caution:** Starting on July 23, 2024, container OS vulnerability scanning is deprecated and is scheduled for shutdown on July 31, 2025. Starting on June 16, 2025, Advanced Vulnerability Insights is deprecated and is scheduled for shutdown on June 16, 2026. For more information about deprecation and shutdown dates, see [Vulnerability scanning removal from GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/vulnerability-scanning-gkee).



The following table describes the cluster-specific features:

Feature name | Availability | Included capabilities  
---|---|---  
Kubernetes security posture - standard tier |  Requires GKE version 1.27 or later. Enabled by default in all new clusters. | 

  * [Automatic scanning of workloads for configuration concerns](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration)
  * [Actionable security bulletin surfacing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning#security-bulletins)

  
Workload vulnerability scanning - standard tier | Disabled by default in all new clusters. **Caution:** Starting on July 23, 2024, container OS vulnerability scanning is deprecated and is scheduled for shutdown on July 31, 2025. Starting on June 16, 2025, Advanced Vulnerability Insights is deprecated and is scheduled for shutdown on June 16, 2026. For more information about deprecation and shutdown dates, see [Vulnerability scanning removal from GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/vulnerability-scanning-gkee). | 

  * [Automatic scanning of container images for actionable vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-posture-vulnerability-scanning#about-container-os-scanning)

  
Workload vulnerability scanning - advanced vulnerability insights | Disabled by default in all new clusters. **Caution:** Starting on July 23, 2024, container OS vulnerability scanning is deprecated and is scheduled for shutdown on July 31, 2025. Starting on June 16, 2025, Advanced Vulnerability Insights is deprecated and is scheduled for shutdown on June 16, 2026. For more information about deprecation and shutdown dates, see [Vulnerability scanning removal from GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/vulnerability-scanning-gkee). | 

  * [Automatic scanning of container images for actionable vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-posture-vulnerability-scanning#about-container-os-scanning)
  * [Automatic scanning of application language packages for vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-posture-vulnerability-scanning#enable-advanced-insights)

  
  
You can enable these features for standalone GKE clusters or [fleet member clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts). The security posture dashboard lets you observe all your clusters simultaneously, including all fleet members in your fleet host project.

## Integration with Security Command Center

If you activate Security Command Center in your organization or project, then you see security posture dashboard findings in Security Command Center. For more details about Security Command Center findings that appear on the security posture dashboard, see [Security sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard).

**Important** : Security bulletin findings that are published in Security Command Center _don't_ include a `cve` field that lists the associated CVEs. To view the CVEs, check the finding's `description` field, or review the security bulletin in the security posture dashboard. 

Also, if you activate Security Command Center in your organization or project, then the security posture dashboard shows the following additional panes:

  * **Top threats** : summarizes the top threats that affect your GKE workloads, grouped by severity and category.
  * **Top software vulnerabilities** ([Preview](https://cloud.google.com/products#product-launch-stages)): lists the top CVEs that are associated with Security Command Center findings for your GKE workloads.



To activate the Security Command Center Premium tier free trial in your project, do the following:

  1. In the Google Cloud console, go to the **GKE Security Posture** page.

[Go to GKE Security Posture](https://console.cloud.google.com/kubernetes/security)

  2. Find the **Sample threats** pane. This pane shows examples of the types of security findings that you might see after you enable Security Command Center. These examples don't represent actual security issues in your project.

If you see a pane titled **Top threats** , then Security Command Center is already activated. You can skip the remaining steps.

  3. In the **Sample threats** pane, click **Try security scanning for free**. The activation pane opens.

  4. Click **Start free trial**.


**Note:** Some Security Command Center features require you to [activate the Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier), or to [activate the Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier#activate-premium-org).

After you activate Security Command Center, it starts to analyze, or scan, your GKE workloads and your resources for other Google Cloud services. This initial scan is [usually complete within minutes or hours](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview#scan_latency).

## Benefits of the security posture dashboard

The security posture dashboard is a foundational security measure that you can enable for any eligible GKE cluster. Google Cloud recommends using the security posture dashboard for all your clusters for the following reasons:

  * **Minimal disruptions** : Features don't interfere with or disrupt running workloads.
  * **Actionable recommendations** : When available, the security posture dashboard provides action items to fix discovered concerns. These actions include commands that you can run and examples of configuration changes to make.
  * **Visualization** : The security posture dashboard provides a high-level visualization of concerns affecting clusters across your project, and includes charts and graphs to show the progress you've made and the potential impact of each concern.
  * **Opinionated results** : GKE assigns a severity rating to discovered concerns based on the expertise of our security teams and industry standards.
  * **Auditable event logs** : GKE adds all discovered concerns to Logging for better reportability and observability.
  * **Fleet observability** : If you've registered GKE clusters to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts), the dashboard lets you observe all of your project's clusters, including fleet member clusters and any standalone GKE clusters in the project.



## GKE security posture dashboard pricing

The pricing for the capabilities of the security posture dashboard is as follows, applicable to standalone GKE clusters and fleet GKE clusters:

GKE security posture dashboard pricing  
---  
Workload configuration auditing | No extra charge  
Security bulletin surfacing | No extra charge  
(Deprecated) Container OS vulnerability scanning | No extra charge  
(Deprecated) Advanced vulnerability insights | Uses Artifact Analysis pricing. For details, on the Artifact Analysis pricing page, see [Advanced vulnerability insights](https://docs.cloud.google.com/artifact-analysis/pricing#avi).  
Security Command Center findings | Uses [Security Command Center pricing](https://docs.cloud.google.com/security-command-center/pricing).  
  
Entries that are added to Cloud Logging use [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-costs). However, depending on the scale of your environment and the number of concerns discovered, you might not exceed the free ingestion and storage allotments for Logging. For details, see [Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-costs).

## Manage fleet security posture

If you use [_fleets_](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts) with GKE, you can configure GKE security posture features at the fleet level using the gcloud CLI. GKE clusters that you register as fleet members during cluster creation automatically inherit the security posture configuration. Clusters that were already fleet members before you changed the security posture configuration don't inherit the new configuration. This inherited configuration overrides the default settings that GKE applies to new clusters.

To learn how to change your fleet-level security posture configuration, see [Configure GKE security posture dashboard features at fleet-level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fleet-security-posture).

## About the Security Posture page

The Security Posture page in the Google Cloud console has the following tabs:

  * **Dashboard** : a high-level representation of the results of your scans. Includes charts and feature-specific information.
  * **Concerns** : a detailed, filterable view of any concerns discovered by GKE across your clusters and workloads. You can select individual concerns for details and mitigation options.
  * **Settings** : manage the security posture feature configuration for individual clusters or for fleets.



### Dashboard

The **Dashboard** tab provides a visual representation of the results of various GKE security posture scans and information from other Google Cloud security products that are enabled in your project. For details about the available scanning capabilities and other supported security products, see How the security posture dashboard works in this document.

If you use fleets with GKE, the dashboard also displays any discovered concerns for clusters including clusters in the project's fleet and standalone clusters. To switch the dashboard to view the posture of a specific fleet, select the host project for that fleet from the project selector drop-down menu in the Google Cloud console. If the selected project has the Container Security API enabled, the dashboard shows results for all member clusters of that project's fleet.

### Concerns

The **Concerns** tab lists active security concerns that GKE discovers when scanning your clusters and workloads. This page only displays concerns for the security posture features described in Cluster-specific feature enablement in this document. If you use fleets with GKE, you can see concerns for fleet member clusters and for standalone GKE clusters that the selected project owns.

#### Severity ratings

Where applicable, GKE assigns a severity rating to discovered concerns. You can use these ratings to determine the urgency with which you need to resolve the finding. GKE uses the following severity ratings, which are based on the [CVSS Qualitative Severity Rating Scale](https://www.first.org/cvss/specification-document#Qualitative-Severity-Rating-Scale):

  * **Critical** : Act immediately. An attack will lead to an incident.
  * **High** : Act promptly. An attack will very likely lead to an incident.
  * **Medium** : Act soon. An attack will likely lead to an incident.
  * **Low** : Act eventually. An attack could lead to an incident.



The precise speed of your response to concerns depends on your organization's threat model and risk tolerance. The severity ratings are a qualitative guideline to help you to develop a thorough incident response plan.

#### Concerns table

The **Concerns** table shows all the concerns detected by GKE. You can change the default view to group results by the type of concern, Kubernetes namespace, or by the affected workloads. You can use the filter pane to filter the results by severity rating, type of concern, Google Cloud location, and cluster name. To view details about a specific concern, click the name of that concern.

#### Concern details pane

When you click a concern in the **Concerns** table, the concern details pane opens. This pane provides a detailed description of the concern, and relevant information such as affected OS versions for vulnerabilities, CVE links, or risks associated with a specific configuration concern. The details pane provides a recommended action if applicable. For example, a workload that sets `runAsNonRoot: false` would return the recommended change you need to make to the Pod specification to mitigate the concern.

The **Affected resources** tab in the concern details pane shows a list of workloads in your enrolled clusters that are affected by that concern.

### Settings

The **Settings** tab lets you configure cluster-specific security posture features, like workload configuration auditing, on eligible GKE clusters in your project or fleet. You can view the enablement status of specific features for each cluster and change that configuration for eligible clusters. If you use fleets with GKE, you can also see whether your fleet member clusters have the same settings as the fleet-level configuration.

## Example workflow

This section is an example of the workflow for a cluster administrator who wants to scan workloads in a cluster for security configuration issues, such as root privileges.

  1. Enroll the cluster in Kubernetes security posture scanning by using the Google Cloud console.
  2. Check the security posture dashboard for scan results, which might take up to 30 minutes to appear.
  3. Click the **Concerns** tab to open the detailed results.
  4. Select the **Configuration** concern type filter.
  5. Click a concern in the table.
  6. On the concern details pane, note the recommended configuration change and update the Pod specification with the recommendation.
  7. Apply the updated Pod specification to the cluster.



The next time that the scan runs, the security posture dashboard no longer displays the concern that you fixed.

## What's next

  * Learn more about [Kubernetes security posture scanning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning).
  * Learn how to [automatically audit workloads for configuration issues](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration).
  * Learn how to [configure GKE security posture dashboard features at the fleet level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fleet-security-posture).
  * Learn how to [harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
