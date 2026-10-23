---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/upgrade-config-sync/
title: Upgrade Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:35.403190+00:00
---

# Upgrade Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/upgrade-config-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Upgrade Config Sync Stay organized with collections  Save and categorize content based on your preferences. 

Upgrading the Config Sync version installed on your clusters gives you access to the latest features, stability improvements, and security updates while keeping your installation within the [supported version window](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync#version_support_policy). You can upgrade Config Sync using the Google Cloud console or the Google Cloud CLI.

## Manually upgrade Config Sync

To stay within the [support window](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync#recommended_version), we recommend that you upgrade at least every nine months. However, you can upgrade more frequently to get the latest features and security updates.

### Upgrade from an unsupported version

If your version of Config Sync is unsupported, you can try to upgrade it by using one of the following options:

  * (Recommended) Perform a step-by-step upgrade with increments of no more than two minor versions at a time. For example, if you're on version N-4 (an unsupported version), you should upgrade to N-2 (a supported version), and then you can upgrade to N (a supported version). This approach is the safest method to upgrade, but only works if the first incremental upgrade is to a supported version.
  * Upgrade directly to a supported version. If you can't perform a step-by-step upgrade, you can try upgrading directly to a supported version. For example, if you're on version N-6 (an unsupported version), trying to perform an incremental upgrade to N-4 (an unsupported version) won't work. In this scenario, you can try upgrading directly to N-2 (the earliest supported version).
  * If your Config Sync version is significantly behind, and the previous options don't work, you can uninstall and reinstall Config Sync.



## Upgrade Config Sync

Before you upgrade Config Sync, check the [release notes](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/release-notes) for details on what's changed between versions.

**Note:** If you use Config Controller to install and manage Config Sync, you don't need to manually upgrade. Config Controller is a managed service, so Google upgrades it automatically. For details on Config Controller changes, see the [Config Controller release notes](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/release-notes).

To upgrade Config Sync, complete the following steps:

###  console 

  1. In the Google Cloud console, go to the **Config** page under the **Features** section. 

[Go to Config](https://console.cloud.google.com/kubernetes/config_management)

  2. Under the **Settings** tab, next to the cluster whose Config Sync version you want to upgrade, select **Edit cluster config**.
  3. From the **Version** drop-down list, select the version that you want to upgrade to.
  4. Click **Upgrade Config Sync**.



###  gcloud 

  1. (Optional) If you want to check which Config Sync version is installed on your clusters before you upgrade, run the following command:
         
         gcloud beta container fleet config-management version
         

  2. Run the following command:
         
         gcloud beta container fleet config-management upgrade \
             --version=VERSION \
             --membership=MEMBERSHIP_NAME
         

Replace the following:

     * `VERSION`: the version that you want to upgrade to.
     * `MEMBERSHIP_NAME`: the fleet membership name that you chose when you registered your cluster. You can find the membership name by running `gcloud container fleet memberships list`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
