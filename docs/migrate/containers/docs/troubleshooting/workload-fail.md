---
url: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/workload-fail/
title: My workload does not start \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:13.369607+00:00
---

# My workload does not start  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/workload-fail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# My workload does not start

When attempting to start a migration, you may encounter an error that prevents your workload from starting correctly.

If you experience an error that prevents your workload from starting correctly, try the troubleshooting steps described in this document before contacting support.

## Add permissions required to pull images from Google Container Registry

For your workload to start, the cluster needs to pull the workload image from [Google Container Registry (GCR)](https://docs.cloud.google.com/container-registry), which might sometimes fail due to missing permissions.

To identify this issue, perform these steps:

  1. In the Google Cloud console, go to the **Object browser** page. 

[Go to Object browser](https://console.cloud.google.com/kubernetes/object/browser)

  2. Select your cluster.

  3. From the **Object Kinds** list, select **Pod**.

  4. From the list of pods that is displayed, locate the pod corresponding to your workload, and then to open pod details, click the pod name.

  5. On the **Pod details** page, if a banner appears that displays the `failed to pull and unpack image` and `403 forbidden` errors, then the permissions required to pull the workload image are missing.




To resolve this issue, perform these steps:

  1. [Add a role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#grant-single-role) called **Storage Object Viewer** to the **Default Compute Engine service account** in your project.

  2. Then, [delete](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete) the pod from your cluster.

A new pod is automatically created which replaces the deleted pod.




Your migrated workload should now be accessible.

## Disable GKE Autopilot clusters

As of Migrate to Containers, use of GKE Autopilot clusters is enabled by default. As a result, any new migrations created for Migrate to Containers will use GKE Autopilot clusters unless specified otherwise.

Try disabling GKE Autopilot clusters and attempt to start your migration workload again.

To disable GKE Autopilot clusters, perform these steps to set `v2kServiceManager` to `false`:

  1. [Edit your migration plan](https://docs.cloud.google.com/migrate/containers/docs/customizing-a-migration-plan#edit_the_migration_plan).

     1. In the `MIGRATION_NAME.yaml` file, locate `v2kServiceManager` and set it to `false`.

Change:
            
            v2kServiceManager: true
            

to:
            
            v2kServiceManager: false
            

     2. Save your file.

  2. [Reinitiate your migration](https://docs.cloud.google.com/migrate/anthos/docs/executing-a-migration) using Migrate to Containers.




If your workload still does not start correctly after disabling GKE Autopilot clusters, then contact your support channel.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
