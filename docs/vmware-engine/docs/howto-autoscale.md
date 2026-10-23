---
url: https://docs.cloud.google.com/vmware-engine/docs/howto-autoscale/
title: Manage autoscale \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:08.290788+00:00
---

# Manage autoscale  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/howto-autoscale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage autoscale

Autoscale automatically expands or shrinks a cluster in a private cloud based on CPU, memory, and storage utilization thresholds. Google Cloud VMware Engine monitors the cluster based on defined metrics and adds or removes nodes from the cluster automatically. Autoscale is not available on clusters containing a single node and clusters which contain storage-only nodes.

**Important:** Adjustments to clusters based on autoscale count toward VMware Engine node quota corresponding to your Google Cloud project. To increase your quota and allow autoscale to add more nodes, see [Quotas and limits](https://docs.cloud.google.com/vmware-engine/quotas).

For each cluster in your private cloud, you can choose to apply autoscale. When metrics specified in autoscale are sustained for a period of 30 minutes, VMware Engine triggers an action based on the specified policy.

Because compute, memory, and storage usage are often independent, autoscale that monitors multiple metrics use `OR` logic for scale out and `AND` logic for scale in.

Autoscale doesn't consider prepaid nodes. If you purchase prepaid nodes, you must edit the minimum node count to the count of prepaid nodes.

## Enable autoscale

To enable autoscale on a cluster, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where the private cloud is located.

  3. Select the private cloud you want to access.

  4. On the private cloud details page, click the **Clusters** tab.

  5. Click the name of the cluster to enable autoscale for.

  6. On the cluster details page, click **Edit**.

  7. Select the metrics to use for autoscale and provide the **Scale out** and **Scale in** threshold.

     * **Scale out:** Add nodes to the cluster to increase resources to meet the resource demands.
     * **Scale in:** Remove nodes from the cluster to reduce resources to meet the resource demands.
  8. Enter the values for **Minimum nodes** , **Maximum nodes** , **Nodes per scale out** and **Duration** for **Cool-off period** under **Additional settings**.

     * **Minimum nodes:** Minimum number of nodes (3) in a cluster with autoscale enabled. If you purchased prepaid nodes, you must set the minimum node count to the number of prepaid nodes.
     * **Maximum nodes:** Maximum number of nodes (32) in a cluster with autoscale enabled.
     * **Nodes per scale out:** Number of nodes per scale out.
     * **Duration:** Sustained resource use for a time period beyond which autoscale takes action.
     * **Cool off period:** Minimum amount of time between actions taken due to autoscale.
  9. Click **Save**.


**Note:** The storage utilization metric can't be disabled, and the maximum utilization can't exceed 80%.

## View cluster autoscale settings

To view the autoscale settings of a cluster, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where the private cloud is located.

  3. Select the private cloud you want to access.

  4. On the private cloud details page, click the **Clusters** tab.

  5. Click the name of the cluster. Autoscale settings are displayed in the details section of the cluster. If autoscale isn't enabled on the cluster, no autoscale information is displayed.




## Edit autoscale

To edit autoscale on a cluster, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where the private cloud is located.

  3. Select the private cloud you want to access.

  4. On the private cloud details page, click the **Clusters** tab.

  5. Click the name of the cluster.

  6. On the cluster details page, click **Edit**.

  7. Update the chosen fields and click **Save**.




## Disable autoscale

To disable autoscale on a cluster, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where the private cloud is located.

  3. Select the private cloud you want to access.

  4. On the private cloud details page, click the **Clusters** tab.

  5. Click the name of the cluster.

  6. On the cluster details page, click **Edit**.

  7. Toggle **Select to turn on autoscaling** and click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
