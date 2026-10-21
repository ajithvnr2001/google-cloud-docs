---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-guide/
title: Deploy a backup/recovery appliance \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:50.962668+00:00
---

# Deploy a backup/recovery appliance  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Deploy a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## Before you begin

Use the following procedures to prepare for the deployment:

  * [Plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan)

  * [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-prep)




## Enable Backup and DR

###  Console 

  1. In the Google Cloud console, click menu **Menu**.

  2. Select **Operations** > **Backup and DR**.

  3. Click **Enable**. The **Setup Backup and DR** wizard opens.

  4. In the **Activate the management console** section, complete the following:

     1. Select the **Location** where you want the appliance management console to be located. This is the Google Cloud region, see [Supported regions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan#regions).

     2. Click **Continue**.

  5. In the **Deploy your first backup/recovery appliance** section, complete the following:

     1. In **Appliance name** , enter a name for the appliance. The name must start with a lowercase letter and can contain up to 23 characters. The appliance name can only contain lowercase letters, numeric characters, and dashes (-). Spaces are not allowed.

     2. Select a **VPC network**. You can select the network within the same project or from the Shared VPC project.

     3. Select the **Target project** where you want to deploy your backup/recovery appliance to.

     4. Select the **Region** and **Zone** where you want your backup/recovery appliances to be located. This is the Google Cloud region and zone, see [Supported regions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan#regions).

     5. Select **Subnetwork**. This is displayed based on the selected region and zone.

**Caution:** Don't use the subnetwork with IP range of 172.17.0.0/16. This subnet IP is used for Backup and DR internal purposes. Using this IP range might fail the backup/recovery appliance deployment.
     6. Select the [**Backup/recovery appliance type**](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan#appliance) based on the workload that you want to back up.

     7. Select a **Storage type** to store backups. This option only appears if you select **Basic for databases, VMware VMs, & other resources** for the **Backup/recovery appliance type**.

     8. Click **Set up**.

You are redirected to the status page. This can take about an hour to complete.

  6. When the deployment is complete, click **Log in to the management console** and the [appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/introduction) will open in a new window.

  7. If you want to deploy a second appliance, click **Deploy another backup/recovery appliance**. You can add up to 30 appliances to an appliance management console. If you need to add more than 30 appliances, create a new project, deploy a new appliance management console, and then deploy the appliances.

**Warning:** After the backup/recovery appliance has been deployed, the Compute Engine VM instances listing page shows a recommendation to save money by resizing the instance. Don't do this. Resizing the appliance or changing its machine configuration—changing the series, CPU, memory—can make the backup/recovery appliance unusable.



###  gcloud 

You can use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to create an appliance management console. Creating backup/recovery appliances using gcloud CLI is not supported. You must use the Google Cloud console to create backup/recovery appliances.

Use the following commands to create an appliance management console.

  1. Create an appliance management console:
         
         gcloud backup-dr management-servers create MANAGEMENT_SERVER_NAME \
           --location=LOCATION_ID \
         

**Note:** By default, the project set in your [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) config is used. To specify a different project, use the `--project` flag.

Replace the following:

     * `MANAGEMENT_SERVER_NAME`: a name for the management console, for example, `test name`. Once the management server is deployed, this name can't be changed. The name must be unique for a project and location.
     * `LOCATION_ID`: enter a management console supported [location](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan#management_console_supported_regions). Get the list of supported locations by using `gcloud backup-dr locations list`.
     * `PROJECT_ID`: the name of your project, for example, `test-project`. Use this flag, if you want to specify a different project.
  2. You can check the status of the operation:
         
         gcloud backup-dr operations describe FULL_OPERATION_ID
         

Replace the following:

     * `FULL_OPERATION_ID`: the operation ID that is displayed for the appliance management console. It is in this format: `projects/test-project/locations/us-central1/operations/operationID`

The output is displayed as:
    
    ```none
      Create in progress for management server [projects/test-project/locations/us-central1/operations/test-operation] \
      Run the [gcloud backup-dr operations describe] command to check the status of this operation.
      ```
    




###  Terraform 

You can use the following Terraform resource links to deploy an appliance management console and a backup/recovery appliance:

  * [Deploy a appliance management console using Terraform resource](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/backup_dr_management_server)
  * [Deploy a backup/recovery appliance using Terraform resource](https://github.com/GoogleCloudPlatform/terraform-google-backup-dr)

**Caution:** When deploying multiple backup/recovery appliances using Terraform, each appliance must be associated with a unique Service Account. Using the same Service Account for multiple appliances can lead to registration timeouts or management failures.



**Note:** For debugging purposes, the Backup and DR collects appliance logs and sends them to Cloud Logging. Standard Cloud Logging pricing applies to this log collection. For pricing information, see [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing). To reduce the cost of logging service, contact [customer support](https://docs.cloud.google.com/backup-disaster-recovery/docs/support) to disable the optional logs.

## What's next

After enabling Backup and DR, you can start exploring the [**appliance management console**](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/introduction) and protect workloads.

### Protect workloads

Use these instructions to protect Compute Engine instances:

  1. Learn about [Cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials).

  2. Assign required [roles and permission](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/permissions).

  3. Define a [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan).

  4. [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst)




### Protect databases and file systems within VMs

  1. [Add your hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications) and [discover applications on your hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/onboarding-wizard).

  2. [Install the Backup and DR agent on the hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector).

  3. Ensure [firewall rules](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan#firewall_configurations) are set.

  4. Define a [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan).

  5. [Apply a backup plan to the discovered applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
