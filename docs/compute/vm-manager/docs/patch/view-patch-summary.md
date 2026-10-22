---
url: https://docs.cloud.google.com/compute/vm-manager/docs/patch/view-patch-summary/
title: View patch summary for VMs \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:19.032919+00:00
---

# View patch summary for VMs  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/patch/view-patch-summary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  View patch summary for VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the patch summary information on the **Patch** dashboard of the Google Cloud console. From this dashboard, you can do the following:

  * View the patch summary information for your VMs in a project, organization, or folders.
  * View the status of patch jobs in your project.
  * View the status of scheduled patch deployments.



## Before you begin

  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Required roles and permissions

To get the permissions that you need to view patch summary, ask your administrator to grant you the following IAM roles: 

  * View patch summary for VMs in an organization or folder: [OS Config Upgrade Report Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.upgradeReportViewer) (`roles/osconfig.upgradeReportViewer`) on the organization or folder 
  * View patch summary for VMs in a project: [OS Config Vulnerability Report Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.vulnerabilityReportViewer) (`roles/osconfig.vulnerabilityReportViewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view patch summary. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view patch summary:

  * View patch summary for VMs in an organization or folder: 
    * `osconfig.upgradeReports.getSummary`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
  * View patch summary for VMs in a project (Projects tab): 
    * `osconfig.upgradeReports.searchSummaries`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View patch summary for VMs in an organization or folder

You can set the view scope to an organization or folder and view the patch summary for VMs in all projects in that organization or folder.

Only those projects in your organization or folder that meet one of the following requirements are listed in the Patch summary table:

  * Contains one or more VMs on which VM Manager is enabled and running.
  * Contains one or more VMs on which VM Manager was running in the past 7 days and patch data is available.



To view patch summary for VMs in an organization or folder, do the following:

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. In the project drop-down list on the Google Cloud console, select the organization or folder for which you want to see the patch summary information.
  3. Click **Projects** tab.
  4. Optional: Specify the criteria for patch summary computation by using the query builder.
  5. Review patch summary information in the **Patch summary table**. The table includes a row for each project as shown in the following figure:

[ ![Patch summary for all projects.](https://docs.cloud.google.com/static/compute/images/manage-os/patch-summary.png)](https://docs.cloud.google.com/static/compute/images/manage-os/patch-summary.png)

The Patch summary table lists the following information that meets the criteria you've specified in the query builder:

     * **Project** : The name of projects in the organization that contain at least one VM and have VM Manager enabled.

Clicking on the project name opens the **VM instances** tab that lists the patch status of individual VMs in the project.

     * **Total VMs** : Total number of VMs in each project.

     * **Monitored VMs** : Number of VMs in the project that have VM Manager agent enabled and are being scanned for patches.

     * **Critical** : Number of VMs with at least one `CRITICAL` patch available.

     * **Important** : Number of VMs with one or more `IMPORTANT` patches available.

     * **Other** : Number of VMs for which there are patches available with a severity rating below `CRITICAL` or `IMPORTANT`.

     * **Up to date** : Number of VMs without any available patches.

     * **No data** : Number of VMs with no patch data available. Either VM Manager is not enabled for these VMs, or their operation system is not supported.

  6. Optional: Apply table filters if you want to view specific rows in the Patch summary table:

[ ![Table filter in the patch summary table.](https://docs.cloud.google.com/static/compute/images/manage-os/table-filter.png)](https://docs.cloud.google.com/static/compute/images/manage-os/table-filter.png)

For example, if you want to see patch summary for projects that have more than 10 VMs, then set the filter option **Total VMs** to `>= 10`.




### Use query builder to filter the patch summary information

Based on the criteria that you specify using the query builder, VM Manager computes and displays the patch summary for VMs in the projects in your organization or folder. You can then use the table filters in the Patch summary table to filter the displayed data.

For example, when you set the `OS` attribute in the query builder as `Debian`, VM Manager displays patch information for all VMs with Debian OS. If you want to view the patch summary for VMs in a specific project, use the filter to specify the project ID.

[ ![Query builder with one attribute.](https://docs.cloud.google.com/static/compute/images/manage-os/query-builder.png)](https://docs.cloud.google.com/static/compute/images/manage-os/query-builder.png)

To set a query in the query builder, do the following:

  1. Select an **Attribute**. The query builder supports the following attributes:

     * **OS** : Specify the short names of the operating systems such as `Windows` or `Debian`.
     * **OS version** : Specify the version of the operating system. For example, `21.04` or `10.0.22000`. You can specify a single asterisk (`*`) at the end of the OS version string to denote partial match, for example `10*`.
     * **VM running** : Specify whether you want to view patch summary for VMs that are in the `RUNNING` state.
     * **CVE ID** : The identifier of the CVE that is fixed by a particular patch, in the `CVE-2023-12345` format. If this attribute is set, only those patches that are related to the given CVE ID are considered to compute the patch summary information.
     * **Patch available** : Set this attribute to `true` to compute patch summary information only for those VMs with at least one patch available.
     * **Patch severity** : Specify the severity of patches applicable to the VMs.
  2. Choose one of the attributes and specify a value for the attribute. For example, if you want to see patch summary for VMs with a specific operating system, then select **OS**. You then get a list of comparison operators to choose from.

     1. Select an **Operator** , for example, `==`.
     2. In the **Value** field, specify the comparison value. For example `Debian`.
  3. To add another attribute, click **Add condition**.

  4. Click **Search**.


**Note:** VM Manager applies the query only to VMs on which VM Manager is enabled.

## What's next?

  * [Create a patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).
  * [Manage patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs).
  * [Schedule patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
