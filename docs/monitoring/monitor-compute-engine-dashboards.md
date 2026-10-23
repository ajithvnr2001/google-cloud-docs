---
url: https://docs.cloud.google.com/monitoring/monitor-compute-engine-dashboards/
title: Quickstart: View and customize VM dashboards \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:55.979605+00:00
---

# Quickstart: View and customize VM dashboards  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/monitor-compute-engine-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View and customize VM dashboards

Learn how to view and customize dashboards for your Compute Engine virtual machine (VM) instances by completing the following tasks:

  1. Create a Compute Engine VM instance.
  2. View the default dashboard.
  3. Customize the default dashboard.
  4. Clean up.



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/welcome?walkthrough_id=monitoring--monitoring-quickstart-ootb-dashboards)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine and Cloud Monitoring APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,monitoring.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine and Cloud Monitoring APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,monitoring.googleapis.com)




## Create a VM instance

Create a VM instance if you don't already have one:

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Create a VM by clicking **Create instance**. Configure your instance by using the options in the navigation menu.
  3. In the **Machine configuration** option, do the following: 
     1. In the **Name** field, enter a descriptive name.
     2. In the **Machine type** preset drop-down, select **Shared-core > e2-small**.
  4. Verify that the **OS and storage** option displays **Debian GNU/Linux**. If not, click the **OS and storage** option and click **Change**. In the **Boot disk** dialog, set **Version** to **Debian GNU/Linux**.
  5. Click **Create**.



## View the VM's observability dashboard

The observability dashboard displays utilization metrics, throughput metrics, and data about logs:

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. In the **VM instances** page, click the instance name.
  3. Select the **Observability** tab.

If you created a VM, then it might take a few minutes before the charts display data.

  4. Explore the charts on the **Observability** tab.




## Create a custom observability dashboard

To create an editable copy of the observability dashboard, do the following:

  1. In the **Observability** toolbar, click **Save as dashboard**.
  2. Click **Submit**.
  3. Click **View in Monitoring**.

You are now viewing a dashboard which you can customize. This dashboard is managed by Cloud Monitoring.

To add a widget, click **Add widget** and complete the dialog. For example, to view your logs with your metric data, click **Add widget** , select **Logs** , and then click **Apply**.

To remove or modify a widget, use the options in the toolbar of the widget.

To reposition or resize a widget, use your pointer.

  4. If you modified the copy, then click **Save**.

  5. In the navigation pane, select **Dashboards**.

In the **My Dashboards** pane, you see your new dashboard listed.




You have successfully customized the observability dashboard for a Compute Engine VM instance. You can use the same procedure to customize dashboards for many other Google Cloud resources.

## View VM dashboards created by Monitoring

Cloud Monitoring creates and manages several dashboards that display metrics for your VM instances. You can access these dashboards from the **Dashboards** page in Cloud Monitoring:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. To view instance-specific dashboards, in the **My Dashboards** pane, click **VM Instances**.

The **VM Instances** page lists your VMs and contains links to VM-specific dashboards. These dashboards are created and managed by Cloud Monitoring.

  3. To view the metrics for all of your VMs, in the navigation pane, select **Dashboards** , and then select the **GCE VM Instance Monitoring** dashboard.

To create an editable copy of this dashboard, click **Copy Dashboard**.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you created a new project and you no longer need the project, then [delete the project](https://console.cloud.google.com/cloud-resource-manager).

If you used an existing project, then do the following:

  1. If you created a VM, then delete it:

     1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Select the checkbox for the instance that you want to delete. 
     3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 
  2. Delete the dashboard you created:

     1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

     2. Find the dashboard that you created, and then click **Delete**.



## What's next

  * To learn how to install the Ops Agent and collect metrics from an Apache server, see the quickstart [Collect Apache metrics with the Ops Agent](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine).

  * To learn how to test whether a URL is responding to requests and to simulate a failure, see the quickstart [Get notified if your application stops responding](https://docs.cloud.google.com/monitoring/monitoring-uptime).

  * To learn about testing your applications, see [Synthetic monitoring overview](https://docs.cloud.google.com/monitoring/uptime-checks/introduction).

  * To learn about the Ops Agent, see [Ops Agent overview](https://docs.cloud.google.com/monitoring/agent/ops-agent).

  * To learn about creating custom dashboards, see [Manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
