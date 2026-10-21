---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-status/
title: Use Policy Controller dashboards \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:56.476838+00:00
---

# Use Policy Controller dashboards  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use Policy Controller dashboards Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Policy Controller dashboards to view your policy coverage and cluster violations.

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce, and who set up alerting and monitor IT systems for performance and vulnerabilities. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

**Caution:** For Google Distributed Cloud (VMware or bare metal), GKE on AWS, GKE on Azure, and GKE attached clusters, the Policy Controller dashboard requires Kubernetes cluster versions 1.26 or later and the following product versions: 

  * **GKE on AWS** : 1.26.2-gke.1001 or later
  * **GKE on Azure** : 1.26.2-gke.1001 or later
  * **GKE attached clusters** : 1.25.0-gke.3 or later



Use the Google Cloud console to view a dashboard that contains information about your policy coverage. The dashboard shows information such as the following:

  * The number of clusters in a fleet (including unregistered clusters) that have Policy Controller installed.
  * The number of clusters with Policy Controller installed that contain policy violations.
  * The number of constraints applied to your clusters per enforcement action.



If you are using [Policy Controller bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles), you can see an overview of your compliance based on the standards in one or more bundles. This overview is aggregated at a fleet level and also includes your unregistered clusters ([Preview](https://cloud.google.com/products/#product-launch-stages)).

## Before you begin

  1. Make sure that your clusters are registered to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) and that your clusters have Policy Controller installed.

  2. To get the permissions that you need to use the Policy Controller dashboard, ask your administrator to grant you the following IAM roles:

     * GKE Hub Viewer (`roles/gkehub.viewer`) on the project containing your fleet
     * Monitoring Viewer (`roles/monitoring.viewer`) on each project with a cluster in your fleet

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## View Policy Controller status

You can view information about your policy coverage in the Google Cloud console.

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

On the **Dashboard** tab, see an overview of your Policy Controller coverage with the following information:

     * **Policy Controller coverage** shows the number of clusters with and without Policy Controller installed.
     * **Clusters in violation** shows the number of clusters without any violations and the number of clusters with violations. The violations are based on which [constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints) are applied to the cluster.
     * **Enforcement** action shows the type of action specified in each constraint. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/auditing-constraints).
     * **Compliance by standards** an overview of your compliance based on the standards in one or more Policy Controller bundles. If you are not using any bundles, the status in this section shows as "100% not applied".
  2. To view more detailed information about policy violations in your cluster, go to the **Violations** tab:

     1. In the **View by** section, select one of the following options:

        * **Constraint** : view a flat list of all constraints with violations in your cluster.
        * **Namespace** : view constraints with violations, organized by the namespace that contains the resource with a violation.
        * **Resource kind** : view constraints with violations, organized by the resource with a violation.
     2. From any view, select the constraint name that you want to view.

The **Details** tab shows information about the violation, including the recommended action to resolve it.

The **Affected Resources** tab shows information about which resources are being evaluated by the constraint and have policy violations.




## View policy findings in Security Command Center

After Policy Controller is installed, you can view policy violations in Security Command Center. This lets you view your security posture for your Google Cloud resources and your Kubernetes resources in the same place. You must have the [Security Command Center activated in your organization](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) [at the Standard or Premium tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

**Note:** Security Command Center shows only violations related to the following Policy Controller bundles: [`pci-dss-v3.2.1`](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pci-dss-v3) and [`cis-k8s-v1.5.1`](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-k8s-benchmark).

In Security Command Center, policy violations show as `Misconfiguration` findings. The category and next steps for each finding are the same as the constraint description and remediation steps.

For more information about using Policy Controller in Security Command Center, see [Policy Controller vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#policy-controller).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
