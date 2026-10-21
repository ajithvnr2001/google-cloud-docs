---
url: https://docs.cloud.google.com/kms/docs/enable-autokey/
title: Enable Cloud KMS Autokey \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:29.341831+00:00
---

# Enable Cloud KMS Autokey  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/enable-autokey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Enable Cloud KMS Autokey Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to enable and configure Cloud KMS Autokey using the Google Cloud console, the Google Cloud CLI, the Cloud KMS API, or Terraform. You can enable Autokey with dedicated-project key storage for a folder, or you can enable Autokey with same-project key storage for an individual project or for all projects within a folder. For more information about Autokey, see [ Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

This document is intended for administrators.

## Autokey configuration inheritance

When you configure Autokey on a folder, child folders and projects within that folder inherit the Autokey configuration of their parent folder. When you configure Autokey on a child folder or project, you decide whether to inherit the configuration from the parent resource or to create a new Autokey configuration for that resource. Autokey configurations applied on child resources override the configuration of the parent folder.

The following table shows supported Autokey configuration use cases:

Resource type | Autokey configuration | Description  
---|---|---  
Organization | Not applicable | Autokey can't be enabled for organizations. Child resources within an organization inherit an empty `AutokeyConfig` resource. In the Google Cloud console, these resources show an Autokey **Status** of **Not enabled**. If you want to restrict Autokey usage within your organization or disable it entirely, you can use organization policies. For more information, see [Control Autokey usage](https://docs.cloud.google.com/kms/docs/control-autokey-usage).  
Folder | `DEDICATED_KEY_PROJECT` | Autokey with dedicated-project key storage is enabled for resource projects within the folder. For resource projects that inherit this configuration, Autokey creates keys in the dedicated key project.  
Folder | `RESOURCE_PROJECT` | Autokey with same-project key storage is enabled for resource projects within the folder. For resource projects that inherit this configuration, Autokey creates keys in the same project as the resources that they protect.  
Folder | `DISABLED` | Autokey is disabled within the folder, however, child folders and projects can still override this configuration. If you want to restrict Autokey within your folder or disable it entirely, you can use organization policies. For more information, see [Control Autokey usage](https://docs.cloud.google.com/kms/docs/control-autokey-usage).  
Folder | `KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED` | The folder inherits the Autokey configuration from its parent folder or organization.  
Project | `RESOURCE_PROJECT` | Autokey with same-project key storage is enabled for the resource project. For resources created in this project, Autokey creates keys in the same project.  
Project | `DISABLED` | Autokey is disabled for the resource project. Developers who create resources in this project must manually create and provision keys if they want to use CMEK for the resources that they create.  
Project | `KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED` | The project inherits the Autokey configuration from its parent folder.  
  
## Before you begin

Before you can enable Autokey with dedicated-project key storage for a folder, you must have the following:

  * An organization resource that contains a folder where you want to enable Autokey. If you don't have a folder where you want to enable Autokey, you can [create a new resource folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders). Enabling Autokey on this folder enables Autokey for all resource projects within the folder.

  * If you have resource projects where you want to use Autokey with dedicated-project key storage, but they aren't inside a folder where you will enable Autokey, you can [move existing resource projects into new folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#moving_a_project_into_a_folder).




Before you can enable Autokey with same-project key storage, you must have one of the following:

  * A Google Cloud project where you want to enable Autokey and where the `keyHandles.create` permission is not blocked by an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview).
  * A Google Cloud folder where you want to enable Autokey, which contains at least one project where the `keyHandles.create` permission is not blocked by an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview).



### Required roles

To get the permissions that you need to enable and configure Autokey, ask your administrator to grant you the following IAM roles on the folder, project, or a parent resource: 

  * To enable Autokey: 
    * [Cloud KMS Autokey Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.autokeyAdmin) (`roles/cloudkms.autokeyAdmin`)
    * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * To enable Autokey with dedicated-project key storage: 
    * [Folder IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderIamAdmin) (`roles/resourcemanager.folderIamAdmin`)
    * [Billing Account user ](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.user) (`roles/billing.user`)
  * To view Autokey configuration: [Cloud KMS Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.viewer) (`roles/cloudkms.viewer`) 
  * To view all effective Autokey configurations: 
    * Cloud Asset Viewer (`roles/cloudasset.viewer`) - on the organization 
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to enable and configure Autokey. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to enable and configure Autokey:

  * To enable Autokey: 
    * `cloudkms.autokeyConfigs.*`
    * `serviceusage.services.enable`
  * To enable Autokey with dedicated-project key storage: 
    * `resourcemanager.folders.get`
    * `resourcemanager.folders.getIamPolicy`
    * `resourcemanager.folders.setIamPolicy`
    * `billing.resourceAssociations.create`
  * To view Autokey configuration: 
    * `cloudkms.folders.showEffectiveAutokeyConfig`
    * `cloudkms.projects.showEffectiveAutokeyConfig`
  * To view all effective Autokey configurations: 
    * `cloudasset.assets.query`
    * `serviceusage.services.use`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Terraform setup

This section contains example Terraform variables and resources that are prerequisites for the rest of the Terraform samples in this document. If you're not using Terraform to create or manage your Autokey configurations, skip this section.

#### Click here to show or hide the Terraform setup sample

This sample completes the following setup steps:

  1. Define variables that are used in subsequent Terraform samples.
  2. Create a resource folder. You can skip this step if you plan to only use same-project key storage in individual projects.
  3. Grant Autokey administrator and user roles.


    
    
      variable "organization_ID" {
        description = "Your Google Cloud Org ID"
        type        = string
        default     = "ORGANIZATION_ID"
      }
    
      variable "billing_account" {
        description = "Your Google Cloud Billing Account ID"
        type        = string
        default     = "BILLING_ACCOUNT_ID"
      }
    
      /* List the users who should have the authority to enable and configure
        Autokey at a folder level */
      variable "autokey_folder_admins" {
        type    = list(string)
        default = [AUTOKEY_ADMIN_USER_IDS]
      }
    
      /* List the users who should have the authority to protect their resources
        with Autokey */
      variable "autokey_folder_users" {
        type    = list(string)
        default = [AUTOKEY_DEVELOPER_USER_IDS]
      }
    
      /* List the users who should have the authority to manage crypto operations
        in the Autokey key project */
      variable "autokey_project_kms_admins" {
        type    = list(string)
        default = [KEY_PROJECT_ADMIN_USER_IDS]
      }
    
      # Create a new folder
      resource "google_folder" "autokey_folder" {
        parent       = "organizations/${var.organization_ID}"
        display_name = "autokey_folder"
      }
      /* To use a folder that already exists, omit this block and instead create a
         variable for the folder ID instead, and then update subsequent resources
         to use the variable. */
    
      # Set permissions for key admins to use Autokey in this folder
      resource "google_folder_iam_binding" "autokey_folder_admin" {
        folder  = google_folder.autokey_folder.name
        role    = "roles/cloudkms.autokeyAdmin"
        members = var.autokey_folder_admins
      }
    
      /* Set permissions for users to protect resources with Autokey in
        this folder */
      resource "google_folder_iam_binding" "autokey_folder_users" {
        folder  = google_folder.autokey_folder.name
        role    = "roles/cloudkms.autokeyUser"
        members = var.autokey_folder_users
      }
      

Replace the following:

  1. `BILLING_ACCOUNT_ID`: your Google Cloud billing account ID. The billing account ID is an 18-character alphanumeric value separated by dashes—for example, `010101-F0FFF0-10XX01`.
  2. `AUTOKEY_ADMIN_USER_IDS`: a list of email addresses for users that should have the `roles/cloudkms.autokeyAdmin` role—for example, `"Ariel@example.com", "Charlie@example.com"`.
  3. `AUTOKEY_DEVELOPER_USER_IDS`: a list of email addresses for users that should have the `roles/cloudkms.autokeyUser` role—for example, `"Kalani@example.com", "Mahan@example.com"`.
  4. `KEY_PROJECT_ADMIN_USER_IDS`: a list of email addresses for users that should have the `roles/cloudkms.admin` role—for example, `"Sasha@example.com", "Nur@example.com"`.



## Set up Autokey with dedicated-project key storage

When you use Autokey with dedicated-project key storage in a folder, you need to choose a single key project to contain all keys created by Autokey in that folder. If you are using same-project key storage, then you don't need a dedicated key project; continue from Enable Autokey with same-project key storage.

We recommend creating a new key project to contain Cloud KMS resources created by Autokey. You should create the key project inside your organization resource. If you already have a key project that you want to use for keys created by Autokey, you can skip the Create a key project section and continue from Configure the Autokey key project on this page.

The key project can be created inside the same folder where you plan to enable Autokey. You shouldn't create other resources inside the key project. If you attempt to create resources protected by Autokey in the key project, Autokey rejects the request for a new key.

If you might want to migrate to [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) in the future, create the key project inside the same folder as the resources protected by those keys.

If your organization uses the `constraints/gcp.restrictCmekCryptoKeyProjects` organization policy constraint to ensure that all CMEKs are from specified key projects, you must add your key project to the list of allowed projects. For more information about CMEK organization policy, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

### Create a key project

###  Console 

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. For **Select organization** , select the organization resource where you want to create a project.
  3. Click **Create project**.
  4. In the **New project** window that appears, enter a project name and select a billing account. A project name can contain only letters, numbers, single quotes, hyphens, spaces, or exclamation points, and must be between 4 and 30 characters.
  5. For **Location** , select the resource that you want to be the parent for your key project.
  6. To finish creating the project, click **Create**.



###  gcloud 

  * Create a new project:
        
        gcloud projects create PROJECT_ID \
            --PARENT_TYPE=PARENT_ID
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that contains the key ring.
    * `PARENT_TYPE`: the type of the resource where you want to create the new key project. Enter `organization` to create the new key project under a given organization, or enter `folder` to create the new key project under a given folder.
    * `PARENT_ID`: the ID of the organization or folder where you want to create the key project.



###  REST 

  * Create a new project:
        
        curl "https://cloudresourcemanager.googleapis.com/v3/projects/"
            --request "POST" \
            --header "authorization: Bearer TOKEN" \
            --header "content-type: application/json" \
            --data '{ "projectId": "PROJECT_ID", "name": "PROJECT_NAME", "parent": "PARENT_TYPE/PARENT_ID" }'
        

Replace the following:

    * `PROJECT_ID`: the identifier that you want to use for your dedicated key project.
    * `PROJECT_NAME`: the name that you want to use for your dedicated key project.
    * `PARENT_TYPE`: the resource type of the parent resource where you want to create the dedicated key project—for example, `organizations` or `folders`.
    * `PARENT_ID"`: the resource identifier of the parent resource where you want to create the dedicated key project.



###  Terraform 

The following Terraform sample creates a dedicated key project in the previously created folder.
    
    
    /* Define the project ID to use for the dedicated key project. The project
      ID must be 6 to 30 characters with lowercase letters, digits, hyphens. The
      project ID must start with a letter. Trailing hyphens are prohibited */
    variable "key_management_project_ID" {
      description = "Sets the project ID for the dedicated key project. This project will contain the Key Rings and Keys generated by Cloud KMS Autokey"
      type        = string
      default     = "KEY_PROJECT_ID"
    }
    
    # Create a key project to store keys created by Autokey
    resource "google_project" "key_management_project" {
      project_id      = var.key_management_project_ID
      name            = var.key_management_project_ID
      billing_account = var.billing_account
      folder_id       = google_folder.autokey_folder.name
    }
    
    output "project_number" {
      value = google_project.key_management_project.number
    }
    

Replace `KEY_PROJECT_ID` with the ID to use for the dedicated key project—for example, `autokey-key-project`.

### Set up a project lien

After you create the Cloud KMS project, we recommend that you [protect the project with a lien](https://docs.cloud.google.com/resource-manager/docs/project-liens#place-liens) ([Preview](https://cloud.google.com/products#product-launch-stages)) to avoid accidental deletion. When a project lien is enforced, the Cloud KMS project is blocked from deletion until the lien is removed.

### Prepare the dedicated key project

###  Console 

  1. Enable the Cloud KMS API on your key project.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  2. If you are using a new key project, grant Cloud KMS administrator permissions on the key project. Repeat the following steps to grant the **Cloud KMS Admin** role to yourself and each other Cloud KMS administrator user:

     1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)

     2. Select the key project.

     3. Click person_add **Grant Access** , and then enter the user's email address.

     4. Select the **Cloud KMS Admin** role.

     5. Click **Save**.




###  gcloud 

  1. Enable the Cloud KMS API on your key project:
         
         gcloud services enable cloudkms.googleapis.com
         

  2. Grant Cloud KMS administrator permissions on the key project. Repeat the following command to grant the `roles/cloudkms.admin` role to yourself and each other Cloud KMS administrator users:
         
         gcloud projects add-iam-policy-binding PROJECT_NUMBER \
             --role=roles/cloudkms.admin \
             --member=user:KEY_ADMIN_EMAIL
         

Replace the following:

     * `PROJECT_NUMBER`: the project number of the key project.
     * `KEY_ADMIN_EMAIL`: the email address of the user who is responsible for managing Cloud KMS keys.



###  REST 

  1. Enable the Cloud KMS API on your key project:
         
         curl "https://serviceusage.googleapis.com/v1/projects/PROJECT_ID/services/cloudkms.googleapis.com:enable" \
             --request "POST" \
             --header "authorization: Bearer TOKEN"
         

Replace `PROJECT_ID` with the identifier of your dedicated key project.

  2. Get the current IAM policy for the dedicated key project.
         
         curl "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy" \
             --request POST \
             --header "authorization: Bearer TOKEN"
             --header "Content-Type: application/json; charset=utf-8" \
             --data '{"options": {"requestedPolicyVersion": 3}}'
         

The response contains the project's current allow policy.

  3. Modify the returned allow policy to add the `roles/cloudkms.admin` role for each Cloud KMS administrator user, including yourself, using the following example role binding as a guide: `json { "role": "roles/cloudkms.admin", "members": [ "PRINCIPAL_LIST" ], }`

Replace `PRINCIPAL_LIST` with a comma-separated list of user principals;—for example, `admin_1@example.com,admin_2@example.com`.

This change doesn't take effect until you set the new policy.

  4. Set the new allow policy.

**Warning:** Setting a new policy permanently overwrites the existing policy on the project. To avoid removing role bindings unintentionally, always follow the read-modify-write pattern when updating an allow policy: read the existing allow policy, modify it as needed, and then write the updated version of the allow policy.
         
         curl "https://cloudresourcemanager.googleapis.com/1/projects/PROJECT_ID:setIamPolicy" \
             --request POST \
             --header "authorization: Bearer TOKEN" \
             --header "Content-Type: application/json; charset=utf-8" \
             --data 'ALLOW_POLICY'
         

Replace the following:

     * `PROJECT_ID`: the identifier of your dedicated key project.
     * `ALLOW_POLICY`: the updated allow policy JSON that you created in the previous step, including existing role grants and the ones that you just added.



###  Terraform 

The following Terraform sample enables the Cloud KMS API in the dedicated key project and grants the roles/cloudkms.admin to the Cloud KMS administrator principals identified previously.
    
    
    # Enable the Cloud KMS API in the key project
    resource "google_project_service" "enable_api" {
      service                    = "cloudkms.googleapis.com"
      project                    = google_project.key_management_project.project_id
      disable_on_destroy         = false
      disable_dependent_services = false
      depends_on                 = [google_project.key_management_project]
    }
    
    /* Grant role for Cloud KMS admins to use Autokey in the
       dedicated key project */
    resource "google_project_iam_binding" "autokey_project_admin" {
      project    = google_project.key_management_project.project_id
      role       = "roles/cloudkms.admin"
      members    = var.autokey_project_kms_admins
      depends_on = [ google_project.key_management_project ]
    }
    

### Enable Cloud KMS Autokey on a resource folder

###  Console 

  1. In the Google Cloud console, go to the **Key management controls** page.

[Go to Key management controls](https://console.cloud.google.com/security/kms/controls)

  2. From the context picker, select the folder where you want to enable Autokey with dedicated-project key storage.
  3. In the **Autokey** section, click **Manage**.
  4. Click **Configure**.
  5. For **Configuration source** , select **Configure for folder**.
  6. For **Configuration** , select **Enable dedicated-project key storage**.
  7. Select your key project and then click **Submit**.

A message confirms that Cloud KMS Autokey is enabled on the folder.




###  gcloud 

  1. Create a YAML file that contains the following `AutokeyConfig`:
         
         name: folders/FOLDER_NUMBER/autokeyConfig
         keyProjectResolutionMode: DEDICATED_KEY_PROJECT
         keyProject: projects/PROJECT_ID
         

Replace the following:

     * `FOLDER_NUMBER`: the number of the folder where you want to enable Autokey with dedicated-project key storage.
     * `PROJECT_ID`: the identifier of your dedicated key project.
  2. Apply the `AutokeyConfig` to the folder:
         
         gcloud kms autokey-config update AUTOKEY_CONFIG_PATH
         

Replace AUTOKEY_CONFIG_PATH with the path to the YAML file that you created in the previous step.




###  REST 

Create the `AutokeyConfig` for the folder where you want to enable Autokey with dedicated-project key storage:
    
    
    curl "https://cloudkms.googleapis.com/v1/folders/FOLDER_ID/autokeyConfig?updateMask=keyProject,keyProjectResolutionMode" \
        --request "PATCH" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"keyProject": "projects/PROJECT_ID", "keyProjectResolutionMode": "DEDICATED_KEY_PROJECT"}'
    

Replace the following:

  * `FOLDER_ID`: the ID of the folder where you want to enable Autokey.
  * `PROJECT_ID`: the ID of the key project.



###  Terraform 
    
    
    /* Enable AutokeyConfig for dedicated-project key storage in the
       folder */
    resource "google_kms_autokey_config" "autokey_config" {
      provider    = google-beta
      folder      = google_folder.autokey_folder.folder_id
      key_project = "projects/${google_project.key_management_project.project_id}"
      key_project_resolution_mode = "DEDICATED_KEY_PROJECT"
      /* For folder scope, valid values are DEDICATED_KEY_PROJECT,
         RESOURCE_PROJECT, and DISABLED. With DEDICATED_KEY_PROJECT, define the
        key_project as well. With RESOURCE_PROJECT, omit key_project. Keys will
        be created in the same project as the protected resource. */
    }
    

### Set up the Cloud KMS service agent

The Cloud KMS service agent for a key project creates keys and applies IAM policy bindings during resource creation, on behalf of a human Cloud KMS administrator. To be able to create and assign keys, the Cloud KMS service agent requires Cloud KMS administrator permissions.

###  gcloud 

  1. Create the Cloud KMS service agent:
         
         gcloud beta services identity create --service=cloudkms.googleapis.com \
             --project=PROJECT_NUMBER
         

Replace `PROJECT_NUMBER` with the project number of the key project.

The output is similar to the following:
         
         Service identity created: service-PROJECT_NUMBER@gcp-sa-ekms.iam.gserviceaccount.com
         

The output of the command indicates that the [Cloud EKM service account](https://docs.cloud.google.com/iam/docs/service-agents#external-key-management-service-service-account) (with the `gcp-sa-ekms` subdomain) has been created. However, the command also creates the [Cloud KMS service agent](https://docs.cloud.google.com/iam/docs/service-agents#cloud-kms-service-agent) (with the `gcp-sa-cloudkms` subdomain), which is the service agent that you use later in these instructions.

  2. Grant Cloud KMS administrator permissions to the service agent:
         
         gcloud projects add-iam-policy-binding PROJECT_NUMBER \
             --role=roles/cloudkms.admin \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudkms.iam.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with the project number of the key project.




###  Terraform
    
    
    # Create the Cloud KMS service agent
    resource "google_project_service_identity" "KMS_Service_Agent" {
      provider   = google-beta
      service    = "cloudkms.googleapis.com"
      project    = google_project.key_management_project.project_id
      depends_on = [google_project.key_management_project]
    }
    
    /* Grant role for the Cloud KMS service agent to use delegated
      Cloud KMS administrator permissions */
    resource "google_project_iam_member" "autokey_project_admin" {
      project = google_project.key_management_project.project_id
      role    = "roles/cloudkms.admin"
      member  = "serviceAccount:service-${google_project.key_management_project.number}@gcp-sa-cloudkms.iam.gserviceaccount.com"
    }
    

## Enable Autokey with same-project key storage

When you use Autokey with same-project key storage, Autokey creates your keys inside the same project as the resources that they protect. Projects that use same-project key storage can exist within folders that use dedicated-project key storage. When Autokey is enabled on a project, the project-level Autokey configuration overrides the Autokey configuration on the parent folder.

To enable Autokey with same-project key storage for an individual project, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Key management controls** page.

[Go to Key management controls](https://console.cloud.google.com/security/kms/controls)

  2. From the context picker, select the project where you want to enable Autokey with same-project key storage.
  3. In the **Autokey** section, click **Manage**.
  4. Click **Configure**.
  5. For **Configuration source** , select **Configure for project**.
  6. For **Configuration** , select **Enable same-project key storage**.
  7. Click **Submit**.

A message confirms that Cloud KMS Autokey is enabled on the project.




###  gcloud 

  1. Create a YAML file that contains the following `AutokeyConfig`:
         
         name: projects/PROJECT_ID/autokeyConfig
         keyProjectResolutionMode: RESOURCE_PROJECT
         keyProject:
         

Replace `PROJECT_ID` with the identifier of the project where you want to enable Autokey with same-project key storage.

  2. Apply the `AutokeyConfig` to the project:
         
         gcloud kms autokey-config update AUTOKEY_CONFIG_PATH
         

Replace AUTOKEY_CONFIG_PATH with the path to the YAML file that you created in the previous step.

  3. Enable the Cloud KMS API on the project:
         
         gcloud services enable cloudkms.googleapis.com
         




###  REST 

  1. Using the REST API, create the `AutokeyConfig` for the project where you want to enable Autokey with same-project key storage:
         
         curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/autokeyConfig?updateMask=keyProjectResolutionMode,keyProject" \
             --request "PATCH" \
             --header "authorization: Bearer TOKEN" \
             --header "content-type: application/json" \
             --data '{"keyProjectResolutionMode": "RESOURCE_PROJECT", "keyProject": ""}'
         

Replace `PROJECT_ID` with the ID of the project where you want to enable Autokey.

  2. In the gcloud CLI, enable the Cloud KMS API on the project:
         
         gcloud services enable cloudkms.googleapis.com
         




###  Terraform 

To enable Autokey with same-project key storage on an individual project, use a `autokey_config_project` resource similar to the following:
    
    
    /* To set autokey config for a project */
    resource "google_kms_autokey_config" "autokey_config_project" {
      provider = google-beta
      project = "projects/${google_project.key_management_project.project_id}"
      key_project_resolution_mode = "RESOURCE_PROJECT"
      # For project scope, valid values are RESOURCE_PROJECT or DISABLED
    }
    

To enable Autokey with same-project key storage for all projects within a folder, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Key management controls** page.

[Go to Key management controls](https://console.cloud.google.com/security/kms/controls)

  2. From the context picker, select the folder where you want to enable Autokey with same-project key storage.
  3. Click **Configure**.
  4. For **Configuration source** , select **Configure for folder**.
  5. For **Configuration** , select **Enable same-project key storage**.
  6. Click **Submit**.

A message confirms that Cloud KMS Autokey is enabled on the folder.




###  gcloud 

  1. Create a YAML file that contains the following `AutokeyConfig`:
         
         name: folders/FOLDER_NUMBER/autokeyConfig
         keyProjectResolutionMode: RESOURCE_PROJECT
         keyProject:
         

Replace `FOLDER_NUMBER` with the number of the folder where you want to enable Autokey with same-project key storage.

  2. Apply the `AutokeyConfig` to the folder:
         
         gcloud kms autokey-config update AUTOKEY_CONFIG_PATH
         

Replace AUTOKEY_CONFIG_PATH with the path to the YAML file that you created in the previous step.




###  REST 

  1. Using the REST API, create the `AutokeyConfig` for the folder where you want to enable Autokey with same-project key storage:
         
         curl "https://cloudkms.googleapis.com/v1/folders/FOLDER_ID/autokeyConfig?updateMask=keyProjectResolutionMode,keyProject" \
             --request "PATCH" \
             --header "authorization: Bearer TOKEN" \
             --header "content-type: application/json" \
             --data '{"keyProjectResolutionMode": "RESOURCE_PROJECT", "keyProject": ""}'
         

Replace `FOLDER_ID` with the ID of the folder where you want to enable Autokey. This command enables Autokey with same-project key storage for all projects within the folder.

  2. In the gcloud CLI, enable the Cloud KMS API on each project where you want to use Autokey with same-project key storage:
         
         gcloud services enable cloudkms.googleapis.com
         

You can enable the Cloud KMS API on each project all at once, or enable the API on individual projects as needed. Your developers can't use Autokey in the project until the Cloud KMS API is enabled for that project.




###  Terraform 

To enable Autokey with same-project key storage on all projects in a folder, use a `folder_config` resource similar to the following:
    
    
    /* Enable AutokeyConfig on a folder */
    resource "google_kms_autokey_config" "folder_config" {
      provider    = google-beta
      folder      = google_folder.autokey_folder.name
      key_project_resolution_mode = "RESOURCE_PROJECT"
      /* For folder scope, valid values are DEDICATED_KEY_PROJECT,
         RESOURCE_PROJECT, or DISABLED. With DEDICATED_KEY_PROJECT, define the
         key_project as well. With RESOURCE_PROJECT, omit key_project. Keys will
         be created in the same project as the protected resource. */
    }
    

## Clear Autokey configuration

You can clear the Autokey configuration on a folder or project to revert to using the configuration of the parent folder.

###  Console 

  1. In the Google Cloud console, go to the **Key management controls** page.

[Go to Key management controls](https://console.cloud.google.com/security/kms/controls)

  2. From the context picker, select the folder or project where you want to clear the Autokey configuration.
  3. In the **Autokey** section, click **Manage**.
  4. Click **Configure**.
  5. For **Configuration source** , select **Inherit**.
  6. Click **Submit**.



###  gcloud 

  1. Create a YAML file that contains the following `AutokeyConfig`:
         
         name: RESOURCE_TYPE/RESOURCE_ID/autokeyConfig
         keyProjectResolutionMode: KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED
         keyProject:
         

Replace the following:

     * `RESOURCE_TYPE`: the type of the resource where you want to clear the Autokey configuration. Set to `folders` or `projects`.
     * `RESOURCE_ID`: the identifier of the folder where you want to clear the Autokey configuration.
  2. Apply the `AutokeyConfig` to the folder or project:
         
         gcloud kms autokey-config update AUTOKEY_CONFIG_PATH
         

Replace AUTOKEY_CONFIG_PATH with the path to the YAML file that you created in the previous step.




###  REST 

Clear the `AutokeyConfig` for the folder or project where you want to revert to the inherited Autokey configuration:
    
    
    curl "https://cloudkms.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/autokeyConfig?updateMask:keyProjectResolutionMode,keyProject" \
        --request "PATCH" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"keyProjectResolutionMode": "KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED", "keyProject": ""}'
    

Replace the following:

  * `RESOURCE_TYPE`: the type of the resource where you want to disable Autokey. Set to `folders` or `projects`.
  * `RESOURCE_ID`: the identifier of the folder where you want to disable Autokey with same-project key storage.



###  Terraform 
    
    
    # Clear AutokeyConfig for the folder
    resource "google_kms_autokey_config" "autokey_config" {
      provider    = google-beta
      folder      = google_folder.autokey_folder.folder_id
      key_project = ""
      key_project_resolution_mode = "KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED"
    }
    

## View effective Autokey configuration

You can view the effective Autokey configuration of a folder or project. The effective Autokey configuration tells you the following:

  * Whether Autokey is enabled on the selected resource.
  * If Autokey is enabled, whether the selected resource uses dedicated-project key storage or same-project key storage.
  * If the selected resource uses dedicated-project key storage, the resource identifier of the dedicated key project.
  * Whether this Autokey configuration is inherited from a parent folder or configured on the selected resource.




###  Console 

  1. In the Google Cloud console, go to the **Key management controls** page.

[Go to Key management controls](https://console.cloud.google.com/security/kms/controls)

  2. From the context picker, select the folder or project where you want to view Autokey settings.
  3. In the **Autokey** section, click **Manage**.



###  gcloud 

View the effective `AutokeyConfig`:
    
    
    gcloud kms autokey-config show-effective-config \
        --RESOURCE_TYPE=RESOURCE_ID
    

Replace the following:

  * `RESOURCE_TYPE`: the type of the resource where you want to view the effective Autokey configuration. Set to `folder` or `project`.
  * `RESOURCE_ID`: the identifier of the resource where you want to view the effective Autokey configuration.



The output is similar to the following:
    
    
    keyProject: KEY_PROJECT
    keyProjectResolutionMode: KEY_PROJECT_RESOLUTION_MODE
    source:
      name: RESOURCE_IDENTIFIER
    

This output includes the following values:

  * `KEY_PROJECT`: the resource identifier of the key project—for example, `projects/PROJECT_ID`. If Autokey is disabled, or if the resource is a folder where same-project key storage is enabled, then this field is omitted.
  * `KEY_PROJECT_RESOLUTION_MODE`: the `keyProjectResolutionMode` of the resource—for example, `RESOURCE_PROJECT`, `DEDICATED_KEY_PROJECT`, or `DISABLED`. If Autokey is not enabled on the resource or any parent resource, then this field is omitted.
  * `RESOURCE_IDENTIFIER`: the resource identifier of the resource where the `AutokeyConfig` is configured. This lets you determine whether the `AutokeyConfig` is inherited from a parent resource or configured on the resource that you queried.



###  REST 

View the effective `AutokeyConfig` for a folder or project:
    
    
    curl "https://cloudkms.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID:showEffectiveAutokeyConfig" \
        --request "GET" \
        --header "authorization: Bearer TOKEN"
      ```
    
    Replace the following:
    

  * `RESOURCE_TYPE`: the type of the resource where you want to view the Autokey configuration. Set to `folders` or `projects`.
  * `RESOURCE_ID`: the identifier of the resource where you want to view the Autokey configuration.



The output is similar to the following:
    
    
    {
      "keyProject": KEY_PROJECT,
      "keyProjectResolutionMode": KEY_PROJECT_RESOLUTION_MODE,
      "source": {
        RESOURCE_IDENTIFIER
      }
    }
    

This output includes the following values:

  * `KEY_PROJECT`: the resource identifier of the key project—for example, `projects/PROJECT_ID`. If Autokey is disabled, or if the resource is a folder where same-project key storage is enabled, then this field is omitted.
  * `KEY_PROJECT_RESOLUTION_MODE`: the `keyProjectResolutionMode` of the resource—for example, `RESOURCE_PROJECT`, `DEDICATED_KEY_PROJECT`, or `DISABLED`. If Autokey is not enabled on the resource or any parent resource, then this field is omitted.
  * `RESOURCE_IDENTIFIER`: the resource identifier of the resource where the `AutokeyConfig` is configured. This lets you determine whether the `AutokeyConfig` is inherited from a parent resource or configured on the resource that you queried.



###  SQL 

You can use a SQL query with Cloud Asset Inventory to evaluate the effective Autokey configuration for all projects within a folder or an organization.

**Caution:** Recent configuration changes might not be available in Cloud Asset Inventory. If you need to see the most recent effective Autokey configuration details, use the Google Cloud console, the gcloud CLI, or the Cloud KMS API.

  1. Set bash environment variables for the organization ID and search scope.
         
         export ORG_ID="ORGANIZATION_ID"
         export TARGET_SCOPE="RESOURCE_TYPE/RESOURCE_ID" 
         

Replace the following:

     * `ORGANIZATION_ID`: the numerical identifier of your organization.
     * `RESOURCE_TYPE`: the type of the resource where you want to view effective Autokey configurations. Set to `organizations` to view configurations for all projects in your organization or `folders` to view configurations for all projects within a specific folder.
     * `RESOURCE_ID`: the numerical identifier of the organization or folder where you want to view effective Autokey configurations.
  2. Use the `gcloud asset query` command to execute the query.
         
         gcloud asset query \
             --organization="${ORG_ID}" \
             --statement="
         WITH ProjectConfigs AS (
           SELECT
             p.name AS project_name,
             ARRAY_AGG(
               STRUCT(
                 ancestor AS config_source,
                 c.resource.data.state AS state,
                 c.resource.data.keyProjectResolutionMode AS resolution_mode,
                 c.resource.data.keyProject AS key_project
               )
               ORDER BY offset
               LIMIT 1
             )[SAFE_OFFSET(0)] AS effective_config
           FROM
             STANDARD_METADATA p
           CROSS JOIN
             UNNEST(p.ancestors) AS ancestor WITH OFFSET AS offset
           JOIN
             cloudkms_googleapis_com_AutokeyConfig c
           ON
             ancestor = REGEXP_REPLACE(c.name, r'^//cloudkms\.googleapis\.com/([^/]+/\d+)/autokeyConfig$', r'\1')
           WHERE
             p.assetType = 'cloudresourcemanager.googleapis.com/Project'
           GROUP BY
             p.name
         )
         SELECT
           REPLACE(r.name, '//cloudresourcemanager.googleapis.com/', '') AS project_name,
           p.resource.data.projectId AS project_id,
           COALESCE(rc.effective_config.config_source, 'No Autokey') AS effective_config_source,
           rc.effective_config.state AS autokey_config_state,
           rc.effective_config.resolution_mode AS resolution_mode,
           CASE 
             WHEN rc.effective_config.resolution_mode = 'RESOURCE_PROJECT' THEN p.resource.data.projectId
             ELSE COALESCE(REPLACE(rc.effective_config.key_project, 'projects/', ''), 'No Key Project')
           END AS key_project
         FROM
           STANDARD_METADATA r
         LEFT JOIN
           ProjectConfigs rc
         ON
           r.name = rc.project_name
         LEFT JOIN
           cloudresourcemanager_googleapis_com_Project p
         ON
           r.name = p.name
         WHERE
           r.assetType = 'cloudresourcemanager.googleapis.com/Project'
           AND '${TARGET_SCOPE}' IN UNNEST(r.ancestors)
         "
         

The output includes the following fields:

     * `project_number`: the full numerical resource identifier of each project—for example, `projects/PROJECT_NUMBER`.
     * `project_id`: the identifier of each project—for example, `PROJECT_ID`.
     * `effective_config_source`: the resource identifier of the resource where the Autokey configuration of the project is set—for example, `folders/FOLDER_NUMBER` if the configuration is inherited from a parent folder or `projects/PROJECT_NUMBER` if the configuration is set on the project. If the project doesn't have or inherit an `AutokeyConfig`, this field shows `No Autokey`.
     * `autokey_config_state`: indicates whether an Autokey configuration is `ACTIVE` on the folder, even if that configuration is `DISABLED`. If the project doesn't have or inherit an `AutokeyConfig`, this field is empty.
     * `resolution_mode`: the key project resolution mode of the effective Autokey configuration on the project.
     * `key_project`: indicates where Autokey creates keys for resources in the project—for example, `projects/KEY_PROJECT_ID` when the project uses dedicated-project key storage or `RESOURCE_PROJECT_ID` when the project uses same-project key storage. When Autokey isn't enabled in the project, this field shows `No key project`.



## Disable Autokey

The same roles that can enable Autokey can disable it. To disable Autokey, you can clear the `AutokeyConfig` or set the `feedbackKeyProjectResolutionMode` to `DISABLED`. You can disable Autokey on a folder or a project. You can also disable Autokey for individual projects within a folder where Autokey is enabled.

After Autokey is disabled for a folder or project, the Cloud KMS service agent can no longer create keys for developers when they create resources in that folder or project.

If you want to fully disable Autokey, we recommend that you also remove the IAM bindings for the `roles/cloudkms.autokeyAdmin` and `roles/cloudkms.autokeyUser` roles.

Disabling Autokey doesn't affect existing keys in the key project. You can continue to use these keys to protect your resources.

### Disable Autokey for a folder or project

###  Console 

  1. In the Google Cloud console, go to the **Key management controls** page.

[Go to Key management controls](https://console.cloud.google.com/security/kms/controls)

  2. From the context picker, select the folder or project where you want to disable Autokey.
  3. In the **Autokey** section, click **Manage**.
  4. Click **Configure**.
  5. For **Configuration source** , select **Configure for folder** or **Configure for project**.
  6. For **Configuration** , select **Disable autokey for folder** or **Disable autokey for project**.
  7. Click **Submit**.

A message appears prompting you to confirm that you want to disable Autokey.

  8. To disable Autokey, click **Confirm**.

A message confirms that Cloud KMS Autokey is disabled.




###  gcloud 

  1. Create a YAML file that contains the following `AutokeyConfig`:
         
         name: RESOURCE_TYPE/RESOURCE_ID/autokeyConfig
         keyProjectResolutionMode: DISABLED
         keyProject:
         

Replace the following:

     * `RESOURCE_TYPE`: the type of the resource where you want to disable Autokey. Set to `folders` or `projects`.
     * `RESOURCE_ID`: the identifier of the folder where you want to disable Autokey with same-project key storage.
  2. Apply the `AutokeyConfig` to the folder or project:
         
         gcloud kms autokey-config update AUTOKEY_CONFIG_PATH
         

Replace AUTOKEY_CONFIG_PATH with the path to the YAML file that you created in the previous step.




###  REST 

Update the `AutokeyConfig` for the folder or project where you want to disable Autokey:
    
    
    curl "https://cloudkms.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/autokeyConfig?updateMask:keyProjectResolutionMode,keyProject" \
        --request "PATCH" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"keyProjectResolutionMode": "DISABLED", "keyProject": ""}'
    

Replace the following:

  * `RESOURCE_TYPE`: the type of the resource where you want to disable Autokey. Set to `folders` or `projects`.
  * `RESOURCE_ID`: the identifier of the folder where you want to disable Autokey with same-project key storage.



###  Terraform 
    
    
    # Clear AutokeyConfig for the folder
    resource "google_kms_autokey_config" "autokey_config" {
      provider    = google-beta
      folder      = google_folder.autokey_folder.folder_id
      key_project = ""
      key_project_resolution_mode = "DISABLED"
    }
    

### Revoke Autokey roles

Disabling Autokey by updating the `AutokeyConfig` prevents the Cloud KMS service agent from provisioning new keys in the affected project or folder. However, if you want to fully disable Autokey, we recommend that you also remove the IAM bindings for the `roles/cloudkms.autokeyAdmin` and `roles/cloudkms.autokeyUser` roles.

  1. Optional: Revoke the `roles/cloudkms.autokeyAdmin` role:
         
         gcloud resource-manager folders remove-iam-policy-binding \
             FOLDER_ID --role=roles/cloudkms.autokeyAdmin \
             --member=user:USER_EMAIL
         

Replace the following:

     * `FOLDER_ID`: the ID of the folder where you have disabled Autokey.
     * `USER_EMAIL`: the email address of the user for whom you want to revoke permission to manage Autokey.
  2. Optional: Revoke the `roles/cloudkms.autokeyUser` role at the folder level:
         
         gcloud resource-manager folders remove-iam-policy-binding \
             FOLDER_ID --role=roles/cloudkms.autokeyUser \
             --member=user:USER_EMAIL
         

Replace the following:

     * `FOLDER_ID`: the ID of the folder where you have disabled Autokey.
     * `USER_EMAIL`: the email address of the user for whom you want to revoke permission to use Autokey.
  3. Optional: Revoke the `roles/cloudkms.autokeyUser` role at the project level:
         
         gcloud projects remove-iam-policy-binding \
             RESOURCE_PROJECT_NUMBER \
             --role=roles/cloudkms.autokeyUser \
             --member=user:USER_EMAIL
         

Replace the following:

     * `RESOURCE_PROJECT_NUMBER`: the project number of a resource project within the folder where you have disabled Autokey.
     * `USER_EMAIL`: the email address of the user for whom you want to revoke permission to use Autokey.
  4. Optional: If you don't plan to continue using the key project for Autokey for other folders, revoke the `roles/cloudkms.admin` role for the Cloud KMS service agent:
         
         gcloud projects remove-iam-policy-binding \
             KEY_PROJECT_NUMBER \
             --role=roles/cloudkms.admin \
             --member=serviceAccount:service-KEY_PROJECT_NUMBER@gcp-sa-cloudkms.iam.gserviceaccount.com
         

Replace `KEY_PROJECT_NUMBER` with the numerical ID of the key project.

  5. Optional: If you don't plan to continue using keys created inside the key project, revoke the `roles/cloudkms.admin` role for the Cloud KMS administrator:
         
         gcloud projects remove-iam-policy-binding \
             KEY_PROJECT_NUMBER \
             --role=roles/cloudkms.admin \
             --member=user:KEY_ADMIN_EMAIL
         

Replace the following:

     * `KEY_PROJECT_NUMBER`: the project number of the key project.
     * `KEY_ADMIN_EMAIL`: the email address of the user for whom you want to revoke permission to configure Autokey.



## What's next

  * Learn more about [when to use Autokey](https://docs.cloud.google.com/kms/docs/kms-autokey).
  * Learn more about [how Autokey works](https://docs.cloud.google.com/kms/docs/autokey-overview).
  * Learn how to [Control Autokey usage](https://docs.cloud.google.com/kms/docs/control-autokey-usage).
  * Your Autokey developers can now [create protected resources using Autokey](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
