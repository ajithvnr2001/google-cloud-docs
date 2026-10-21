---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fleet-security-posture/
title: Configure GKE security posture dashboard features at the fleet level \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:14.915898+00:00
---

# Configure GKE security posture dashboard features at the fleet level  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fleet-security-posture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Configure GKE security posture dashboard features at the fleet level Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to configure fleet-level default settings for the [Google Kubernetes Engine (GKE) security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard). The security posture dashboard provides you with opinionated and actionable recommendations to improve your clusters' security posture. You can enable settings for the security posture dashboard at the fleet level.

You can create fleet-level defaults for the security posture dashboard settings of Kubernetes security posture scanning.

This page is for Security specialists who want to implement first-party vulnerability detection solutions across a fleet of clusters. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the general overview of [workload vulnerability scanning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-workload-vulnerability-scanning).

To learn how to configure these settings for individual clusters, see the following resources:

  * [Automatically audit workloads for configuration issues](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration)
  * [Automatically scan workloads for known vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-posture-vulnerability-scanning) (Deprecated)



## Configure fleet-level defaults

This section describes how to configure security posture dashboard features as fleet-level defaults. Any new clusters that you register to a fleet during cluster creation have your specified security posture features enabled. The fleet-level default settings that you configure take priority over any default GKE security posture settings. To view the default settings that apply to your edition of GKE, see the [Cluster-specific features table](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#cluster-specific-features).

To configure fleet-level defaults for security posture, complete the following steps:

### Console

  1. In the Google Cloud console, go to the **Feature Manager** page.

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features/overview)

  2. In the **Security Posture** pane, click **Configure**.

  3. Review your fleet-level settings. All new clusters you register to the fleet inherit these settings.

  4. Optional: To change the default settings, click **Customize fleet settings**. In the **Customize fleet default configuration** dialog that appears, do the following:

     1. For **Configuration audit** , choose if [configuration auditing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning) should be enabled or disabled.
     2. For **Vulnerability scanning** (Deprecated), select the level of [vulnerability scanning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-workload-vulnerability-scanning) that you want; **Disabled** , **Basic** , or **Advanced (recommended)**.
     3. Click **Save**.

If you later disable fleet-level configuration for these features, your current workloads in existing member clusters are still scanned and you can see the security concerns on the security posture dashboard. However, any new clusters you create in that fleet won't be scanned for concerns, unless you enable the security posture features on them individually.

  5. To apply the setting to new clusters, click **Configure**.

  6. In the confirmation dialog, click **Confirm**.

  7. Optional: Sync existing clusters to the default settings:

     1. In the **Clusters in the fleet** list, select the clusters that you want to sync.
     2. Click **Sync to fleet settings** and click **Confirm** in the confirmation dialog that appears. This operation can take a few minutes to complete.



###  gcloud 

Make sure that you have [gcloud CLI version 455.0.0](https://docs.cloud.google.com/sdk/docs/install) or later.

### Configure defaults for a new fleet

You can [create an empty fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#optional_create_an_empty_fleet) with the security posture dashboard features you want enabled.

  * To create a fleet with workload configuration auditing enabled, run the following command:
        
        gcloud container fleet create --security-posture standard
        




### Configure defaults for an existing fleet

  * To enable workload configuration auditing on an existing fleet, run the following command:
        
        gcloud container fleet update --security-posture standard
        




### Disable security posture dashboard features at fleet level

  * To disable workload configuration auditing, run the following command:
        
        gcloud container fleet update --security-posture disabled
        

  * To disable workload vulnerability scanning, run the following command:
        
        gcloud container fleet update --workload-vulnerability-scanning disabled
        




If you disable fleet-level configuration for these features, your current workloads in existing member clusters are still scanned and you can see the security concerns on the security posture dashboard. However, any new clusters you create in that fleet won't be scanned for concerns, unless you enable the security posture features on them individually.

## What's next

  * Learn about the range of Google Cloud features to [secure your clusters and workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * Learn how [workload configuration auditing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning) detects common security configuration concerns.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
