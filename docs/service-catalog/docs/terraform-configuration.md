---
url: https://docs.cloud.google.com/service-catalog/docs/terraform-configuration/
title: Creating a Terraform configuration \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:26.039047+00:00
---

# Creating a Terraform configuration  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/terraform-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating a Terraform configuration

When curating Service Catalog solutions for your organization, you can create a Terraform configuration, or _config_ , which your users deploy using Terraform. After you create the configuration, you can share it with users by assigning it to [catalogs](https://docs.cloud.google.com/service-catalog/docs/create-catalog).

In this guide, you use [Cloud Build](https://docs.cloud.google.com/build/docs) to run Terraform commands in the latest version of the Terraform Docker image, and you use [Cloud Storage](https://docs.cloud.google.com/storage/docs) to store and manage Terraform resources such as modules and [state files](https://www.terraform.io/docs/state/index.html).

For resources and guidance on using Terraform, see [Using Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

## Before you begin

**Note:** Starting April 29, 2024, Cloud Build uses Compute Engine service accounts by default, instead of Cloud Build service accounts. This doesn't affect any existing Google Cloud projects where Cloud Build is already enabled. If you enable Cloud Build for a project on or after April 29th, 2024, you or your organization administrator must update your organization policies or your Compute Engine service accounts to prevent issues. For more details, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).

  * You must have the following [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/understanding-roles):

    * [Catalog Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#instance_admin_role) _OR_ [Catalog Manager](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_manager_role) for the Google Cloud organization associated with the Google Cloud project which has Service Catalog enabled. If you don't have this role, contact your Organization Administrator to request access.
    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) for the Google Cloud project where you want to create your solution. If your Terraform config is in a different project, you must also have the Storage Admin role for the project that contains your Terraform config.
    * [Cloud Build Editor](https://docs.cloud.google.com/build/docs/iam-roles-permissions#predefined_roles) for the Google Cloud project where you want to create the solution.

If you plan to use your own service account, you must also have the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role for the Google Cloud project that contains the service account that you plan to use.

If you don't have these roles, contact your Organization Administrator to request access.

  * If you plan to use your own service account, your service account must have the following [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles):

    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) for the Google Cloud project where you want to create your solution. If your Terraform config is in a different project, your service account must also have the role [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) for the project containing the Terraform config.
    * [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging) for the Google Cloud project where you want to create your solution.

If you don't have these roles, contact your Organization Administrator to request access.

  * Set up Cloud Build in the project where you're creating the config: 

    1. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

Enabling the API automatically creates a Cloud Build service account that you use in the following step.
    2. Go to the [Cloud Build](https://console.cloud.google.com/project/_/cloud-build/builds) page.
    3. On the Left Panel, select **Settings**.
    4. Use the service account provided under the section **Service account email**.
    5. If you aren't using your own service account, grant the following IAM roles to the service account. For steps to grant roles, see [Configuring access for Cloud Build Service Account](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account). 
       * [Project Editor](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#using_basic_roles) (`roles/editor`)
       * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) (`roles/storage.admin`)

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

## Uploading your configuration files to Cloud Storage

You use Cloud Storage to manage your Terraform configuration files for Service Catalog.

### Creating a Cloud Storage bucket

To set up Cloud Storage, create a bucket in the same project where you enabled Service Catalog for your organization:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**. 
  3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
     1. In the **Get started** section, do the following: 
        * Enter a globally unique name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/bucket-naming#requirements).
        * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), expand the **Labels** section (expand_more), click _add_box_ **Add label** , and specify a `key` and a `value` for your label. 
     2. In the **Choose where to store your data** section, do the following: 
        1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
        2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
           * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
        3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

           1. In the **Bucket** menu, select a bucket.
           2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

              * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
              * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
              * Click **Done**.

     3. In the **Choose how to store your data** section, do the following: 
        1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.
        2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
     4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
     5. In the **Choose how to protect object data** section, do the following: 
        * Select any of the options under **Data protection** that you want to set for your bucket. 
          * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
          * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
          * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
            * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
            * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
        * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
  4. Click **Create**. 



### Enabling Object Versioning

You must use Object Versioning for your bucket to protect your Terraform configuration from being deleted or overwritten. To enable Object Versioning, see Cloud Storage's documentation on [Using Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning).

### Granting access to your bucket

When users in your organization deploy the configuration, their Cloud Build service account must have read access to your bucket. If your bucket is stored in the same Google Cloud project where users deploy the configuration, then the service account already has this access.

If your users are deploying the configuration in a different Google Cloud project, grant access to the bucket using one of the following methods:

  * Grant the [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/storage.objectViewer`) role to your users' Cloud Build service accounts, or to a Google Cloud resource where your users deploy Terraform configurations, such as a project, folder, or organization.

  * Use an [Access Control List](https://docs.cloud.google.com/storage/docs/access-control/lists) (ACL) to manage access to the bucket.




For details on managing access to buckets, see Cloud Storage's [Overview of access control](https://docs.cloud.google.com/storage/docs/access-control).

### Creating and uploading a Terraform module

After setting up your Cloud Storage bucket, you must create and upload a Terraform [module](https://www.terraform.io/docs/modules/index.html), which is a container of all of your configuration files. Service Catalog uses the module to automatically generate a JSON schema file to define the variables of your configuration.

When you call modules outside of the current directory, use the remote path instead of a relative path. For example, instead of `source = "../../"`, use `source = "GoogleCloudPlatform/cloud-run/google"`.

**Note:** Terraform state files are created and stored in the projects where your users deploy the configuration.

For modules of common Google Cloud use cases, see [Terraform blueprints and modules for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints).

The following code sample illustrates a Terraform configuration file, `main.tf`:
    
    
    variable "machine_type" {
      type    = string
      default = "n1-standard-1"
    }
    
    variable "zone" {
      type    = string
      default = "us-central1-a"
    }
    
    variable "deployment_identifier" {
      description = "The unique name for your instance"
      type        = string
    }
    
    resource "google_compute_instance" "default" {
      name         = "vm-${var.deployment_identifier}"
      machine_type = var.machine_type
      zone         = var.zone
    
      boot_disk {
        device_name = "boot"
        auto_delete = true
        initialize_params {
          image = "debian-cloud/debian-11"
        }
      }
    
      network_interface {
        network = "default"
        access_config {
          // Ephemeral IP
        }
      }
    }
    

After creating your module, compress the file(s) into a zip file. Make sure the module is stored at the root of the zip file.

To ensure proper storage of the module when you zip your Terraform files, run the following command: `none zip solution.zip file1.tf file2.tf file3.tf`

**Note:** If you try to create a product with a zip file that contains Terraform modules in subdirectories or folders other than the root directory, the Validation can't run successfully.

Then, upload the zip file to your bucket. For steps to upload the zip file, see Cloud Storage's documentation on [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects#console).

## Creating the configuration in Service Catalog

After setting up a Cloud Storage bucket with your Terraform module, you create a Service Catalog solution that includes the bucket.

To create the Terraform configuration as a Service Catalog solution:

  1. Go to the Service Catalog Admin [**Solutions** page](https://console.cloud.google.com/catalog/admin/solutions) in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/catalog/admin/solutions)

  2. To choose the Google Cloud project, click **Select**.

  3. Click **Create solution**. In the drop-down list, select **Create Terraform config**.

  4. Enter a name, description, and tagline for your Terraform configuration. The tagline is a short description of a solution that users see as they browse Service Catalog.

  5. In the **Link to Terraform config** field, provide the link to the Cloud Storage bucket that contains your zip file for the Terraform module, such as `gs://my-terraform-bucket/my-zip-file.zip`.

  6. Optionally, upload an icon for the solution. The recommended dimensions for an icon are 80 by 80 pixels.

  7. Optionally, enter a support link and contact information for the creator.

  8. Optionally, add a link to the documentation for the solution.

  9. Select the Terraform version you want to use to deploy the solution.

  10. Optionally, you can provide your own service account by clicking the checkbox next to **Select or enter your own service account**. If your service account is located in the same Google Cloud project where you're creating your solution, select **Select a service account from the current project** , and select your service account from the drop-down menu. If your service account is located in a different Google Cloud project from your solution, select **Enter a service account email from any project** , and enter the email of your service account.

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).
  11. Click **CREATE**.




The solution is created and appears on the Service Catalog Admin **Solutions** page.

The following screenshot illustrates creating a Terraform configuration:

![Create a Terraform configuration](https://docs.cloud.google.com/static/service-catalog/images/screen-privatecatalog-create-terraform.png)

## Next steps

  * [Assign the Terraform configuration](https://docs.cloud.google.com/service-catalog/docs/assign-solutions) to a catalog, so that users in your organization can access and deploy the solution.
  * [Update a solution](https://docs.cloud.google.com/service-catalog/docs/manage-solutions#update_terraform_configuration) with the latest Terraform configuration details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
