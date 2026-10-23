---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-sa-compute-engine/
title: Configure permissions on target project service account \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:26.814417+00:00
---

# Configure permissions on target project service account  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-sa-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Configure permissions on target project service account Stay organized with collections  Save and categorize content based on your preferences. 

Migrate to Virtual Machines creates a default service account when you enable the Migrate to Virtual Machines API on the host project.

To be able to assign the service account used to run a Compute Engine instance on a target project, you must add the necessary permissions to the Migrate to Virtual Machines default service account.

## About the service account used to run a Compute Engine instance

Before you can test-clone or cut-over a VM, you must configure the target details of the [Compute Engine](https://docs.cloud.google.com/compute/docs/how-to) instance used to host the migrated VM. For both a test and a production environment, configure the target details for the Compute Engine instance to specify:

  * Google project
  * Number of CPUs
  * Amount of memory
  * Disk size



For example, you have the following environment:

  * Project A - Migrate to Virtual Machines **host** project
  * Project B - Compute Engine **target** project



By default, the Compute Engine instance running on target Project B does not have a service account assigned to it.

If the target Compute Engine instance requires access to Google Cloud services and APIs, [create a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount) in the target project with the necessary permissions to access those services and APIs. Then, assign that service account to the Compute Engine instance when you [configure its target details](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target).

You perform all configuration of Compute Engine instances from the Migrate to Virtual Machines host project. Before you can assign a service account in the target project to aCompute Engine instance, you must ensure that the Migrate to Virtual Machines default service account has the necessary permissions on the target service account.

## Configuring the default service account

To assign a service account to a [Compute Engine](https://docs.cloud.google.com/compute/docs/how-to) instance running on a **target** project, the default Migrate to Virtual Machines service account on the **host** project must be added to the `Service Account User` role on the target service account.

**To add the default service account to the Service Account User role:**

  1. Determine the email address of the Migrate to Virtual Machines default service account:

     1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

     2. Select the **Targets** tab.

At the top of the page is an information box showing the email address of the Migrate to Virtual Machines default service account in the form:

`service-HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com`

     3. Save that email address for use below.

  2. In the Google Cloud console, go to the **Service Accounts** page.

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

  3. Select the **target** project.

  4. Select the checkbox next to the chosen **target** service account.

  5. Click **Manage Access**. A list of roles that have been granted on the service account are displayed.

  6. Expand the **Service Account User** role to view the principals that have been granted that role on the service account.

  7. If the email address of the Migrate to Virtual Machines default service account is not listed, select **Add Principal**.

  8. Enter the email address of the Migrate to Virtual Machines default service account as the **New principal**.

  9. Select the **Service Accounts > Service Account User** role.

  10. Select **Save**.

You should now be able to assign the service account to a [Compute Engine](https://docs.cloud.google.com/compute/docs/how-to) instance running on a **target** project.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
