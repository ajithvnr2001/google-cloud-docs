---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/shared-vpc/
title: Configure permissions for a Shared VPC \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:08:55.638305+00:00
---

# Configure permissions for a Shared VPC  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/shared-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Configure permissions for a Shared VPC Stay organized with collections  Save and categorize content based on your preferences. 

[Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) allows an organization to connect resources from multiple projects to a common [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) so that they can communicate with each other securely and efficiently using internal IPs from that network.

When you use Shared VPC, you designate a project as a _Shared VPC host project_ and attach one or more _service projects_ to it. The VPC networks in the Shared VPC host project are called _Shared VPC networks_. [Eligible resources](https://docs.cloud.google.com/vpc/docs/shared-vpc#resources_that_can_be_attached_to_shared_vpc_networks_from_a_service_project) from service projects can use subnets in the Shared VPC network.

**Note:** Both Migrate to Virtual Machines and Shared VPC use the term _host_ project. For Migrate to Virtual Machines, you use the _host_ project to perform migrations. For Shared VPC, you use the _host_ project to define the VPC network.

## Use Shared VPC with Migrate to Virtual Machines

When your Migrate to Virtual Machines environment uses a Shared VPC, you must ensure that you have configured permissions correctly so that you can deploy a migrated VM to the Compute Engine target project.

For example, you have the following environment:

  * Project A - Migrate to Virtual Machines host project
  * Project B - Shared VPC host project and subnet definitions
  * Project C - Migrate to Virtual Machines target project and Shared VPC service project



In this example, you define a Shared VPC in Project B. Project B is referred to as the Shared VPC _host project_.

You then migrate a VM to a Compute Engine instance in Project C, the Migrate to Virtual Machines target project, where Project C accesses the Shared VPC. In this example, Project C is referred to as the Shared VPC _service project_. You must have already configured Project C to function as a service project of Project B, as described in [Provisioning Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared), before you deploy the Compute Engine instance.

However, before you can deploy the Compute Engine instance, you must also ensure that the Migrate to Virtual Machines default service account on Project A has the required permissions. Specifically, Migrate to Virtual Machines requires the `compute.networkUser` role on the subnetworks in the Shared VPC host project.

The following section describes how to configure the Migrate to Virtual Machines default service account.

### Required permissions for Shared VPC setup

To configure target details with a Shared VPC subnet in the Google Cloud console within a 3-project setup (Migrate to Virtual Machines host project, Migrate to Virtual Machines target project, and Shared VPC host project), you must have the following IAM permissions:

  1. **Compute Network User** (`roles/compute.networkUser`) on the Shared VPC host project (or specifically on the target subnet).
  2. **Compute Network Viewer** (`roles/compute.networkViewer`) on the Migrate to Virtual Machines target project.



Without these permissions, you can't view or select the Shared VPC subnets in the Migrate to Virtual Machines target configuration UI, even if you have permissions to create standalone VMs using those subnets.

## Configure the Migrate to Virtual Machines default service account

A default service account is created on the host project during the creation of the first migration, as described in [Install the Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector).

To deploy a Compute Engine instance to a target project that accesses a Shared VPC, you must add the `compute.networkUser` role on the subnetworks in the Shared VPC host project to the Migrate to Virtual Machines default service account. You have two options for how you add this role:

  * Assign the Migrate to Virtual Machines default service account to be a _Service Project Admin_ with access to only some of the subnets in the Shared VPC host project. This option provides a granular means to define Service Project Admins by granting them the `compute.networkUser` role for only some subnets in the Shared VPC host project.

See [Service Project Admins for some subnets](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#networkuseratsubnet) for the steps to this procedure.

  * Allow the Migrate to Virtual Machines default service account to be a _Service Project Admin_ with access to all subnets in the Shared VPC host project. In this case, you grant the role of `compute.networkUser` for the Shared VPC host project to the Migrate to Virtual Machines default service account. The default service account then has access to all the existing and future subnets in the Shared VPC host project.




To configure the Migrate to Virtual Machines default service account for access to **all subnets** in the Shared VPC host project:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Targets** tab.

At the top of the page is an information box showing the email address of the Migrate to Virtual Machines default service account in the form:

`service-M4CE_HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com`

  3. Copy the email address.

  4. Use that email address to grant the `compute.networkUser` role on the Shared VPC host project to the Migrate to Virtual Machines default service account:
         
         gcloud projects add-iam-policy-binding VPC_HOST_PROJECT_ID \
            --member=serviceAccount:service-M4CE_HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com \
            --role=roles/compute.networkUser




For more on assigning roles and permissions to a user account, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
