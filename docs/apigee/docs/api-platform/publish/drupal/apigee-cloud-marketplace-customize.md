---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize/
title: Customize an Apigee Developer Portal Kickstart in Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:02.550470+00:00
---

# Customize an Apigee Developer Portal Kickstart in Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Customize an Apigee Developer Portal Kickstart in Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes options for customizing, maintaining, and securing your Apigee Developer Portal Kickstart solution. Once deployed, all Cloud services components utilized by the portal can generally be customized following standard [Google Cloud documentation](https://cloud.google.com/). The sections below provide configuration options and production guidelines specific to the portal solution. 

## Connect to Apigee or Apigee hybrid

To use the Apigee Developer Portal Kickstart solution with an Apigee or Apigee hybrid organization, the portal must be deployed to the Google Cloud project used during Apigee provisioning. During deployment, [service account](https://cloud.google.com/compute/docs/access/service-accounts) is created with the `Apigee Developer Admin` role. This role is required for service account callers to Apigee APIs.

**NOTE** : Confirm the name of the Apigee or Apigee hybrid org before beginning the deployment process for the Apigee Developer Portal Kickstart solution. The org name must be provided during the installation process.

## Configure HTTPS for the portal

In the portal deployment launch configuration, you can opt to configure HTTPS for your portal. Checkbox configuration options include: 

**Unchecked** | The deployment script will not automatically enable TLS. TLS can be configured manually after deployment using [Cloud Load Balancing](https://cloud.google.com/load-balancing). This is the default option.   
---|---  
**Checked** | The deployment package will enable TLS, provision an IP address, configure a domain name, and request an SSL certificate using [nip.io](https://nip.io). Use of nip.io is not endorsed by Google, but is offered as a convenience option for testing deployments. Selecting this option indicates acceptance of the terms and conditions for nip.io.   
  
## Use Cloud SQL with CMEK

The Cloud SQL instance for the portal is created in the region you choose during launch configuration. By default, Google encrypts data at rest using Google-owned and Google-managed encryption keys. To use a customer-managed encryption key (CMEK) to encrypt the data stored in the CloudSQL instance, follow the steps outlined in [Using customer-managed encryption keys](https://cloud.google.com/sql/docs/mysql/configure-cmek) configure a key.

**Note** : CMEK should be configured before beginning the portal launch configuration. The **Resource Name of the Encryption key** must be provided prior to deploying the portal.

## Manage Cloud SQL

To manage the Cloud SQL instance after deployment: 

  * Go to the [Cloud SQL instances page](https://console.cloud.google.com/sql/instances).
  * Select an instance to edit by clicking the instance name.
  * Click **Edit**.
  * See [Editing instances](https://cloud.google.com/sql/docs/mysql/edit-instance) for configuration setting details.



## Configure and update managed instance groups

A [managed instance group (MIG)](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) is a collection of virtual machine (VM) instances that you can manage as a single entity. You can make your workloads scalable and highly available by taking advantage of automated MIG services including: autoscaling, autohealing, regional (multiple zone) deployment, and automatic updating. 

To configure your MIGs after deployment: 

  * Go to the [VM instances page](https://console.cloud.google.com/compute/instances).
  * Select an instance to edit by clicking the instance name.
  * Click **Edit**.
  * See [ Creating and managing regional MIGs](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) for configuration setting details.



New VM images for the Apigee Developer Portal Kickstart solutions will be released regularly. Customers can use the steps detailed in [Updating instances in a MIG](https://cloud.google.com/compute/docs/instance-groups/updating-migs) to replace or restart instances in a MIG to use the latest image.

## Enable private IP with VPC Service Controls

To enable a private IP address for your Cloud SQL instance: 

  * Confirm that private services access is available on your VPC network. See [ Configuring private services access](https://cloud.google.com/sql/docs/mysql/configure-private-services-access) for a detailed list of required steps.
  * Cloud Deployment Manager is not supported by VPC Service Controls. To enable Deployment Manager for your portal deployments within VPC Service Controls, [ add the Cloud Deployment Manager service account](https://cloud.google.com/vpc-service-controls/docs/supported-products#deployment_manager) to allow calls to APIs protected by VPC Service Controls.



## Customize the portal code

If customizations are made to the portal code or startup scripts after deployment, those changes must be exported and backed up in Filestore to prevent their loss during any updates to the Apigee Developer Portal Kickstart base image. 

For example, if new Drupal modules are installed on a Compute Engine instance, create a backup using the following steps: 

  1. Run the `/opt/apigee/scripts/export-code.sh`to export the changes.
  2. The script copies the exported files to the Filestore instance mounted at `/mnt/fileshare/portalname/`.
  3. Restart the instances in the managed instance group to trigger pick up of the changes across the group. The startup script automatically detects if a code backup exists, loads the changes, fixes file permissions, and applies the `settings.php` file.
  4. Update Drupal core and modules using `composer update`. Apigee updates to the base image only provide OS updates, PHP patches, and NGINX updates. All Drupal core and module updates are managed by the customer and must be applied manually.



To add any customizations to the startup script, create a script at `/mnt/fileshare/$PORTAL_NAME/custom-startup-script.sh`. 

If installing any PHP packages, run the `service supervisor restart` command to apply the changes.

## Create backups

The creation of regular backups is recommended as a best practice for your Apigee Developer Portal Kickstart solution. For detailed steps, see: 

  * [Backing up a Cloud SQL database](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups)
  * [Restoring a Cloud SQL database](https://cloud.google.com/sql/docs/mysql/backup-recovery/restore)
  * [Backing up and restoring Filestore](https://cloud.google.com/filestore/docs/backup-restore)



## Configure a portal for production usage

To configure your portal for production usage, the following steps are recommended: 

**[Cloud SQL Database](https://cloud.google.com/sql/docs/mysql)** | 

  * Verify or change the machine type of the database 
  * Disable the public IP of the database and [ configure Private IP](https://cloud.google.com/sql/docs/mysql/configure-private-ip)
  * Enable automated backups of the database 
  * Enable high availability for the database

  
---|---  
**[Filestore](https://cloud.google.com/filestore/docs/how-to)** | 

  * Enable backups for Filestore

  
**[Cloud Load Balancing](https://cloud.google.com/load-balancing/docs/concepts)** | 

  * Enable Cloud CDN to cache static content 
  * Add a custom SSL certificate if preferred

  
**[Managed Instance Groups](https://cloud.google.com/compute/docs/instance-groups)** | 

  * Adjust the minimum and maximum number of instances required for production traffic **NOTE** : Machine types cannot be changed after the initial portal deployment.

  
**Authentication** | 

  * Remove HTTP Basic Auth access restriction on your site. Run the following commands to make your portal site publicly accessible:
        
        gcloud beta runtime-config configs variables set site_basic_auth/enabled 0 \
          --is-text --config-name=PORTAL_NAME --project=GCP_PROJECT_NAME
        
        gcloud beta compute instance-groups managed rolling-action \
          replace INSTANCE_GROUP_ID --region=GCP_REGION \
          --replacement-method=substitute --project=GCP_PROJECT_NAME


  
  
## What's next

  * Learn more about [Support resources](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/get-support-cloud-marketplace) for the Apigee Developer Portal Kickstart solution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
