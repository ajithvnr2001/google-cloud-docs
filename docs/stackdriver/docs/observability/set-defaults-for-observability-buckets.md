---
url: https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets/
title: Set defaults for observability buckets \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:07.131575+00:00
---

# Set defaults for observability buckets  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Set defaults for observability buckets Stay organized with collections  Save and categorize content based on your preferences. 

If you have compliance or regulatory requirements to store your data in specific locations or to use customer-managed encryption keys (CMEKs), then we recommend that you configure both organization policies and default settings for observability buckets. Organization policies and default settings for observability buckets let you specify the storage location and whether those buckets use Google-default encryption or customer-managed encryption keys (CMEKs).

For organizations, folders, and projects, default settings for observability buckets let you configure the following:

  * A default storage location.
  * For each location, a default Cloud Key Management Service key.



There are two different ways the system uses default settings:

  * When the system automatically creates an observability bucket, it uses the default settings to determine the bucket's location and encryption key. If you haven't defined default settings, then the system selects the location and the bucket uses Google-default encryption.

  * When you initiate creation of an observability bucket by issuing an API request, you provide the location. However, the system automatically uses the Cloud KMS key defined by the default settings to encrypt the data, unless the arguments to the API request specify the key.




Because the parent of an observability bucket is always a project, when you create a bucket, the system first searches for project-level default settings. If those don't exist, then the system searches the parent's ancestors for default settings. For example, if you define default settings for a folder, then those settings apply to descendants of the folder, except those descendants that have default settings configured.

You can also use organization policies to restrict the locations of new observability buckets, to require the use of CMEKs, or to restrict which Cloud KMS keys can be used for encryption. If you configure organization policies that require use of CMEKs, then you must configure default settings for observability buckets. If you don't, then provisioning for system-created observability buckets fails.

This document doesn't apply to log buckets, which store log data. For information about setting a default location or requiring CMEKs for log buckets, see [Configure default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/default-settings).

## Applicable organization policies

To control where your observability buckets are created and who manages the encryption keys for those buckets, you might want to configure the following organization policies:

  * A policy with a constraint ID `constraints/gcp.resourceLocations`. This policy [defines the set of locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) where new resources can be created. To use observability buckets, this set of locations must include at least one [supported observability buckets location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

  * A `Deny` policy with the constraint ID `constraints/gcp.restrictNonCmekServices`. This policy requires that [new resources are encrypted with CMEKs](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

  * A policy with the constraint ID `constraints/gcp.restrictCmekCryptoKeyProjects`. This policy limits which Cloud Key Management Service keys are used for encryption.




You can create organization policies that apply at the organization, folder, or project level. For more information, see [Creating and editing policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies).

**Note:** If you configure organization policies that require use of CMEKs, then you must configure default settings for observability buckets. For example, if you create an organization policy that requires CMEK for a specific folder, then for that folder or for one of its hierarchical ancestors, you must configure default settings. If you don't configure default settings, then provisioning for system-created observability buckets fails.

## How organization policies affect configuring a default location

When you issue a command to set a default location, Google Cloud Observability verifies that the specified location is allowed by your organization policies and is a supported observability buckets location. If either verification fails, then the command to set the default location also fails.

If you modify the list of locations allowed by your organization policies such that the default storage location is no longer allowed, then you must separately update that setting. You might also need to configure a default Cloud KMS key for the updated default location.

## How organization policies and default settings interact

The parent of an observability bucket must be a project. That is, the system can't create an observability bucket in a folder or in an organization. However, if you configure default settings for observability buckets for an organization or a folder, then those default settings apply to all projects that are descendants of that organization or folder.

The following table lists the rules the system uses to determine the location of a new observability bucket:

Use organization policy  
to restrict location | Project (or ancestor) has a  
default storage location | How the system determines the location for a new observability bucket | No | No | The system selects the location from the supported locations for observability buckets.  
---|---|---  
Yes | No | The system selects the location from the intersection of those locations the organization policies allow and those observability buckets support. **If the intersection is empty, then the system doesn't create the observability bucket.**  
No | Yes | The system sets the location to the default storage location defined in the project's default settings. If the project doesn't define a default storage location, then the system uses the default storage location defined for an ancestor.  
Yes | Yes | The system sets the location to the default storage location defined in the project's default settings. If the project doesn't define a default storage location, then the system uses the ancestor's default storage location. **If the default storage location isn't allowed by the organization policies, then the system doesn't create the observability bucket.**  
**Note:** If you set a default Cloud KMS key for a location, then you must also set that location as the default storage location. If you don't set a default storage location, then your observability buckets aren't encrypted with your default Cloud KMS key even if those buckets are in the location where the key is defined.

The following table lists the rules the system uses to determine whether a new observability bucket uses CMEKs, and if so, the value of the Cloud KMS key. To encrypt an observability bucket, a Cloud KMS key must be in the location of the bucket and be allowed by organization policies. If you don't specify an organization policy with the `gcp.restrictCmekCryptoKeyProjects` constraint, then all keys are allowed:

Use organization policy  
to require CMEKs | Project (or ancestor) has a  
default Cloud KMS key | How the system determines which Cloud KMS key to use. | No | No | The observability bucket doesn't use CMEKs.  
---|---|---  
Yes | No | **The system doesn't create new observability buckets** because the organization policy requires CMEKs but a default Cloud KMS key isn't defined.  
No | Yes | To identify a key for encryption, the system first determines whether a default storage location is set for the project or for one of its ancestors. If not, the system selects a location and creates the observability bucket. The bucket doesn't use a CMEK. If a default storage location is found, then the system searches the project's default settings for a default Cloud KMS key. If the project's default settings don't specify an appropriate key, then the system searches the ancestor's default settings for a default key that is in the location of the new bucket. One of the following occurs:

  * A key isn't found: The new observability bucket doesn't use a CMEK.
  * A key is found and is allowed: The system creates the observability bucket.
  * A key is found but isn't allowed: **The system doesn't create the new observability bucket**.

  
Yes | Yes | To identify a key for encryption, the system first determines whether a default storage location is set for the project or for one of its ancestors. If a default storage location isn't set, then **the system doesn't create the new observability bucket**. If a default storage location is found, then the system searches the project's default settings for a default Cloud KMS key. If the project's default settings don't specify an appropriate key, then the system searches the ancestor's default settings for a default key that is in the location of the new bucket. One of the following occurs:

  * A key isn't found: **The new observability bucket isn't created.**
  * A key is found and is allowed: The system creates the observability bucket.
  * A key is found but isn't allowed: **The system doesn't create the new observability bucket**.

  
  
## View default settings for observability buckets

This section describes how you can view the default settings for observability buckets for a _resource_ , which is an organization, folder, or project.

To retrieve the default settings for observability buckets, you must issue multiple commands. The first command returns the default storage location. The second command returns the Cloud KMS key for that location.

The commands described in this section are for a specific resource. The responses of these commands are limited to user-configured values for that resource. These commands don't return settings that the resource might use but that are configured for an ancestor.

### Before you begin

Configure your project, your IAM roles, and select the interface that you plan to use.

#### Configure your project and roles

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. To get the permission that you need to view the default settings for observability buckets for an organization, folder, or project, ask your administrator to grant you the [Observability Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`) IAM role on the organization, folder, or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `observability.settings.get` permission, which is required to view the default settings for observability buckets for an organization, folder, or project. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




#### Select the interface you plan to use

### gcloud

**Note** : You must use gcloud CLI version 586.0.0 or later.

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

### Get the default storage location for a resource

To get the default storage location for a resource, you send a command to a resource-specific endpoint, and set the location of that command to `global`. The response data includes the default storage location and the name of a service account. If you require CMEK for the resource, then this service account is used to retrieve Cloud KMS keys.

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

Use one of the following to pass to the command the ID of the project, folder, or organization that you want to query: 

  * `--project=PROJECT_ID`, where PROJECT_ID contains the ID of your project.
  * `--folder=FOLDER_ID`, where FOLDER_ID contains the ID of your folder.
  * `--organization=ORGANIZATION_ID`, where ORGANIZATION_ID contains the ID of your organization.

Set the `default_storage_location` to a [supported location](/stackdriver/docs/observability/observability-bucket-locations) 

Execute the [`gcloud observability settings describe`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/settings/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability settings describe \
     --location=global --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability settings describe `
     --location=global --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability settings describe ^
     --location=global --project=PROJECT_ID

The following illustrates the response of the command: 
    
    
    Parsed [location] resource: projects/my-project/locations/global
    defaultStorageLocation: eu
    name: projects/my-project/locations/global/settings
    serviceAccountId: service-12345@gcp-sa-observability.iam.gserviceaccount.com
    

###  Terraform 

You can use Terraform to set a default storage location for a resource, which is a project, folder, or organization. You can't use Terraform to report the default storage location for a resource.

###  REST 

  1. For the resource whose default settings you want to display, select the appropriate endpoint and then in the APIs Explorer, specify the path parameter:

Organization:

     * API endpoint: [`organizations.locations.getSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations/getSettings)
     * Path parameter:
           
           organizations/ORGANIZATION_ID/locations/global/settings
           

Folder:

     * API endpoint: [`folders.locations.getSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations/getSettings)
     * Path parameter:
           
           folders/FOLDER_ID/locations/global/settings
           

Project:

     * API endpoint: [`projects.locations.getSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations/getSettings)

     * Path parameter:
           
           projects/PROJECT_ID/locations/global/settings
           

The variables in the previous expressions have the following meaning:

     * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
     * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).
     * PROJECT_ID: The identifier of the project.
  2. Click **Execute**.

When successful, the response is a [`Settings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/Settings) object. If the `default_storage_location` field is empty, then a default storage location isn't set.

For example, if you issue a `getSettings` command and set the path parameter to an organization, the response is similar to one of the following:

     * Default storage location set to `"us"`:
           
           default_storage_location: "us"
           service_account_id: service-org-ORGANIZATION_ID@gcp-sa-observability.iam.gserviceaccount.com
           

     * No default storage location set:
           
           service_account_id: service-org-ORGANIZATION_ID@gcp-sa-observability.iam.gserviceaccount.com
           




### Get the default Cloud KMS key for a resource and location

Cloud KMS keys are regional resources. They can only be used to encrypt or decrypt data that is stored in the same location as the key. For each location supported by observability buckets, and for each organization, folder, or project, you can configure the default settings for observability buckets with a Cloud KMS key.

This section describes how to get the default Cloud KMS key for a resource and location.

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * LOCATION: The location of the Cloud KMS key for your resource. The resource is a project, folder, or organization. If you set the location to `global`, then command returns the default storage location for the resource. 
  * Use one of the following to pass to the command the ID of the project, folder, or organization that you want to query: 
    * `--project=PROJECT_ID`, where PROJECT_ID contains the ID of your project.
    * `--folder=FOLDER_ID`, where FOLDER_ID contains the ID of your folder.
    * `--organization=ORGANIZATION_ID`, where ORGANIZATION_ID contains the ID of your organization.



Execute the [`gcloud observability settings describe`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/settings/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability settings describe \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability settings describe `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability settings describe ^
     --location=LOCATION --project=PROJECT_ID

The following illustrates the response of the command: 
    
    
    Parsed [location] resource: projects/my-project/locations/us
    kmsKeyName: projects/my-project/locations/us/keyRings/test/cryptoKeys/test-key
    name: projects/my-project/locations/us/settings
    serviceAccountId: service-12345@gcp-sa-observability.iam.gserviceaccount.com
    

###  Terraform 

You can use Terraform to set a default Cloud Key Management Service key for a location and resource, which is a project, folder, or organization. You can't use Terraform to report the default storage location for a resource.

###  REST 

  1. For the resource whose default settings you want to display, select the appropriate endpoint and then in the APIs Explorer, specify the path parameter:

Organization:

     * API endpoint: [`organizations.locations.getSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations/getSettings)

     * Path parameter:
           
           organizations/ORGANIZATION_ID/locations/LOCATION_ID/settings
           

Folder:

     * API endpoint: [`folders.locations.getSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations/getSettings)
     * Path parameter:
           
           folders/FOLDER_ID/locations/LOCATION_ID/settings
           

Project:

     * API endpoint: [`projects.locations.getSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations/getSettings)
     * Path parameter:
           
           projects/PROJECT_ID/locations/LOCATION_ID/settings
           

The variables in the previous expressions have the following meaning:

     * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
     * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).
     * PROJECT_ID: The identifier of the project.
     * LOCATION_ID: The location whose CMEK configuration you want to view.
  2. Click **Execute**.

When successful, the response is a [`Settings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/Settings) object.

For example, suppose that you issue the `getSettings` command and set the path parameter to `organizations/ORGANIZATION_ID/locations/LOCATION_ID/settings`, then the response is similar to one of the following:

     * When a Cloud KMS key isn't set for the organization and location, the response lists only a service account:
           
           service_account_id: service-org-ORGANIZATION_ID@gcp-sa-observability.iam.gserviceaccount.com
           

     * When the Cloud KMS key is set for the organization and location, the response includes a service account and the Cloud KMS key name:
           
           name: "organizations/ORGANIZATION_ID/locations/LOCATION_ID/settings"
           service_account_id: service-org-ORGANIZATION_ID@gcp-sa-observability.iam.gserviceaccount.com
           kms_key_name: "projects/my-kms-project/locations/LOCATION_ID/keyRings/my-key-ring/cryptoKeys/my-key"
           




## Set the default settings for observability buckets

This section describes how you can configure default settings for observability buckets for a resource, which is an organization, folder, or project.

If you plan to require CMEK for a resource and location, then configure the default settings for observability buckets for that pair before you set the default storage location. When you configure default settings for a resource and location, you specify the Cloud KMS key to use.

These instructions are for the APIs Explorer, which lets you issue API commands from a documentation page. However, you can also issue a `curl` command.

### Example configurations

This section lists common use cases.

#### Require new buckets to be in a specific location

To require that new system-created observability buckets in your organization be in the `us` location, set the default storage location for your organization to `us`.

To override the organization-level settings and to require that new system-created observability buckets in the child folder named `my-eu-projects` be in the `eu` region, set the default storage location for the `my-eu-projects` folder to `eu`.

#### Require new buckets to be in a specific location and to use CMEK

To require that all new system-created observability buckets in your organization be in the `us` location and use CMEK, do the following:

  1. Configure the default settings for observability buckets for your organization and the `us` location to specify a Cloud KMS key.

  2. Set the default storage location for your organization to be `us`.




### Before you begin

If you are only planning to set the default storage location, then you don't need any Cloud KMS roles.

  1. Complete the required setup to view default settings for observability buckets.

  2. To get the permissions that you need to set the default settings for observability buckets for an organization, folder, or project, ask your administrator to grant you the following IAM roles on the organization, folder, or project: 

     * [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)
     * [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to set the default settings for observability buckets for an organization, folder, or project. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to set the default settings for observability buckets for an organization, folder, or project:

     * `observability.settings.get`
     * `observability.settings.update`
     * `cloudkms.cryptoKeys.getIamPolicy`
     * `cloudkms.cryptoKeys.setIamPolicy`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. If you plan to require use of CMEK, then make sure that you have a Cloud KMS key in the required location. If necessary, create a [Cloud KMS key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and a [Cloud KMS key](https://docs.cloud.google.com/kms/docs/create-key).

**Note:** The location of your Cloud KMS key ring must be in a [supported observability buckets location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  4. Determine the resource whose default settings for observability buckets you plan to update. This resource can be an organization, folder, or project.

If you configure default settings for an organization or a folder, then they apply to all descendants of that organization or folder. If you configure default settings for observability buckets for a project, then they apply only to that project.




### Grant resource's service account access to a key

**Note:** This section applies only if you plan to require new system-created observability buckets to use CMEK.

For the resource whose default settings you plan to configure, grant its service account a role:

  1. Identify the Cloud KMS key that you want to use for encryption and decryption.

Cloud KMS keys are regional. For example, if you plan to require new system-created observability buckets to be in the `us` location, then you need a Cloud KMS key in the `us` location.

  2. Identify the service account for your resource.

For example, if you want all new system-created observability buckets in your organization to be in the `us` location and to use CMEK, then issue a `getSettings` call to the `global` location and set the path parameter to an organization. The response data lists the organization's service account:
         
         service_account_id: service-org-ORGANIZATION_ID@gcp-sa-observability.iam.gserviceaccount.com
         

  3. Grant the service account you identified in the previous step the [Cloud KMS CryptoKey Encrypter/Decrypter (`roles.cloudkms.cryptoKeyEncrypterDecrypter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) role for the Cloud KMS key that you want to use to encrypt and decrypt data.

This role binding is for a specific Cloud KMS key.

###  gcloud 

Run the [`gcloud kms keys add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) command:
         
         gcloud kms keys add-iam-policy-binding KMS_KEY_NAME \
         --project=KMS_PROJECT_ID \
         --member=serviceAccount:SERVICE_ACCT_NAME@gcp-sa-observability.iam.gserviceaccount.com \
         --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
         --location=LOCATION_ID \
         --keyring=KMS_KEY_RING
         

Before running the previous command, make the following replacements:

     * KMS_KEY_NAME: The name of the key.
     * KMS_PROJECT_ID: The unique alphanumeric identifier, composed of your Google Cloud project name and a randomly assigned number, of the Google Cloud project running Cloud KMS. For information about getting this identifier, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * SERVICE_ACCT_NAME: The name of your resource's service account, which you identified in the previous step.
     * LOCATION_ID: The location of your Cloud KMS key.
     * KMS_KEY_RING: The Cloud KMS key ring's name.

###  Console 

     1. In the Google Cloud console, go to the **Key management** page. 

[Go to Key management](https://console.cloud.google.com/security/kms)

     2. Select the name of the key ring that contains the key.
     3. Select the checkbox for the key.

The **Permissions** tab becomes available.

     4. In the **Add members** dialog, specify the email address of the Google Cloud Observability service account to which you are granting access.

     5. In the **Select a role** menu, select **Cloud KMS CryptoKey Encrypter/Decrypter**.

     6. Click **Add**.




### Set the default Cloud KMS key for a resource and location

**Note:** This section applies only if you plan to require new system-created observability buckets in a resource to use CMEK.

In the previous step, you granted a resource's service account the permissions to encrypt and decrypt data for a specific Cloud KMS key. For example, you might have granted an organization's service account an IAM role that lets it access a Cloud KMS key that is in the `us` location.

In this step, for that resource and for the location of the Cloud KMS key, you update the default settings for observability buckets with the key information. For example, in this step, you might configure the default settings for observability buckets for your organization and for the `us` location, to the Cloud KMS key that is also in the `us` location.

As a follow-on step, set the default storage location. If you don't set a default storage location, then your observability buckets aren't encrypted with your default Cloud KMS key even if those buckets are in the location where the key is defined.

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * KMS_KEY_NAME: The name of the Cloud KMS key.
  * LOCATION: The location of the Cloud KMS key for your resource. The resource is a project, folder, or organization. If you set the location to `global`, then the command returns the default storage location for the resource. 
  * Use one of the following to pass to the command the ID of the project, folder, or organization that you want to query: 
    * `--project=PROJECT_ID`, where PROJECT_ID contains the ID of your project.
    * `--folder=FOLDER_ID`, where FOLDER_ID contains the ID of your folder.
    * `--organization=ORGANIZATION_ID`, where ORGANIZATION_ID contains the ID of your organization.



Execute the [`gcloud observability settings update`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/settings/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability settings update \
     --kms-key-name=KMS_KEY_NAME \
     --update-mask=kmsKeyName \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability settings update `
     --kms-key-name=KMS_KEY_NAME `
     --update-mask=kmsKeyName `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability settings update ^
     --kms-key-name=KMS_KEY_NAME ^
     --update-mask=kmsKeyName ^
     --location=LOCATION --project=PROJECT_ID

The update command initiates a long-running operation. The following illustrates the response of the command: 
    
    
    Parsed [location] resource: projects/my-project/locations/us
    Request issued for: [us]
    Waiting for operation [projects/my-project/locations/us/operations/operation-1775247021184-64e93e8161585-1a55612f-73382a5a] to complete...done.
    Updated location [us].
    '@type': type.googleapis.com/google.cloud.observability.v1.Settings
    kmsKeyName: projects/my-project/locations/us/keyRings/test/cryptoKeys/test-key
    name: projects/my-project/locations/us/settings
    serviceAccountId: service-12345@gcp-sa-observability.iam.gserviceaccount.com
    

###  Terraform 

To set a default Cloud Key Management Service key for a location and a resource, do the following:

  1. Select the appropriate Terraform resource based on the Google Cloud resource that you want to configure:

Organization:

     * Use the Terraform resource [`google_observability_organization_settings`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_organization_settings).
     * Set the `organization` field to the ID of the organization.

Folder:

     * Use the Terraform resource [`google_observability_folder_settings`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_folder_settings).
     * Set the `folder` field to the ID of the folder.

Project:

     * Use the Terraform resource [`google_observability_project_settings`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_project_settings).
     * Set the `project` field to the ID of the project.
  2. Set the following fields:

     1. Set the `location` field to the location for the default Cloud KMS key.
     2. Set the `kms_key_name` field to the Cloud KMS key.



###  REST 

  1. For the resource whose default settings you want to set, select the appropriate endpoint and then in the APIs Explorer, specify the path parameter:

Organization:

     * API endpoint: [`organizations.locations.updateSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations/updateSettings)
     * Path parameter:
           
           organizations/ORGANIZATION_ID/locations/LOCATION_ID/settings
           

Folder:

     * API endpoint: [`folders.locations.updateSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations/updateSettings)
     * Path parameter:
           
           folders/FOLDER_ID/locations/LOCATION_ID/settings
           

Project:

     * API endpoint: [`projects.locations.updateSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations/updateSettings)
     * Path parameter:
           
           projects/PROJECT_ID/locations/LOCATION_ID/settings
           

The variables in the preceding expressions have the following meanings:

     * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
     * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).
     * PROJECT_ID: The identifier of the project.
     * LOCATION_ID: The location of your Cloud KMS key.
  2. Set the **updateMask** field as follows:
         
         updateMask=kmsKeyName
         

  3. Configure the **Request body** as follows:
         
         {
           "kmsKeyName":"projects/KMS_PROJECT_ID/locations/LOCATION_ID/keyRings/KMS_KEY_RING/cryptoKeys/KMS_KEY_NAME"
         }
         

Before entering the values, make the following replacements:

     * KMS_PROJECT_ID: The unique alphanumeric identifier, composed of your Google Cloud project name and a randomly assigned number, of the Google Cloud project running Cloud KMS. For information about getting this identifier, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * LOCATION_ID: The location of your Cloud KMS key.
     * KMS_KEY_RING: The Cloud KMS key ring's name.
     * KMS_KEY_NAME: The name of the key.

The value of `"kmsKeyName"` is the fully qualified name of your key.

  4. Click **Execute**.

When successful, the response is a [`Settings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/Settings) object.

For example, suppose that you issue the `updateSettings` command to set a Cloud KMS key and that you set the path parameter to `organizations/ORGANIZATION_ID/locations/LOCATION_ID/settings`, then the response is similar to the following:
         
         name: "organizations/ORGANIZATION_ID/locations/LOCATION_ID/settings"
         service_account_id: service-org-ORGANIZATION_ID@gcp-sa-observability.iam.gserviceaccount.com
         kms_key_name: "projects/KMS_PROJECT_ID/locations/LOCATION_ID/keyRings/KMS_KEY_RING/cryptoKeys/KMS_KEY_NAME"
         




### Set the default storage location for a resource

**Note:** Always set a default storage location when you want your observability buckets to use CMEKs. If you don't set a default storage location, then your observability buckets aren't encrypted with your default Cloud KMS key even if those buckets are in a location where a default key is defined.

This step describes how to set a default storage location for a resource, which is an organization, folder, or project. All descendants in the resource hierarchy automatically use the default storage location, except for those descendants where you've configured a default storage location.

For example, if you set the default storage location for an organization to the `us` location, then new system-created observability buckets in that organization are in the `us` location. If you want a folder or project to have a different default storage location, then configure default settings for observability buckets for the folder or project.

If you want the system-created observability buckets in a resource to use CMEK, then you complete the following steps before you set the default storage location for the resource:

  1. Grant the resource's service account the IAM role that lets the service account encrypt and decrypt data. This role is for a specific Cloud KMS key, and that key is in a specific location.
  2. Configure the default settings for observability buckets for the resource and key location with the Cloud KMS key information.



###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * DEFAULT_STORAGE_LOCATION: The default storage location for your project, folder, or organization. This location applies to new observability buckets. You must enter a [supported observability bucket location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations). 
  * Use one of the following to pass to the command the ID of the project, folder, or organization that you want to query: 
    * `--project=PROJECT_ID`, where PROJECT_ID contains the ID of your project.
    * `--folder=FOLDER_ID`, where FOLDER_ID contains the ID of your folder.
    * `--organization=ORGANIZATION_ID`, where ORGANIZATION_ID contains the ID of your organization.



Execute the [`gcloud observability settings update`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/settings/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability settings update \
     --default-storage-location=DEFAULT_STORAGE_LOCATION \
     --update-mask=defaultStorageLocation \
     --location=global --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability settings update `
     --default-storage-location=DEFAULT_STORAGE_LOCATION `
     --update-mask=defaultStorageLocation `
     --location=global --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability settings update ^
     --default-storage-location=DEFAULT_STORAGE_LOCATION ^
     --update-mask=defaultStorageLocation ^
     --location=global --project=PROJECT_ID

The update command initiates a long-running operation. The following illustrates the response of the command: 
    
    
    Parsed [location] resource: projects/my-project/locations/global
    Request issued for: [global]
    Waiting for operation [projects/my-project/locations/global/operations/operation-1775247065869-64e93eabfee29-f7d39a96-5e23c6c7] to complete...done.
    Updated location [global].
    '@type': type.googleapis.com/google.cloud.observability.v1.Settings
    defaultStorageLocation: us
    name: projects/my-project/locations/global/settings
    serviceAccountId: service-12345@gcp-sa-observability.iam.gserviceaccount.com
    

###  Terraform 

To set a default location, do the following:

  1. Select the appropriate Terraform resource based on the Google Cloud resource that you want to configure:

Organization:

     * Use the Terraform resource [`google_observability_organization_settings`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_organization_settings).
     * Set the `organization` field to the ID of the organization.

Folder:

     * Use the Terraform resource [`google_observability_folder_settings`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_folder_settings).
     * Set the `folder` field to the ID of the folder.

Project:

     * Use the Terraform resource [`google_observability_project_settings`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_project_settings).
     * Set the `project` field to the ID of the project.
  2. Set the following fields:

     1. Set the `location` field to `global`.
     2. Set the `default_storage_location` field to a [supported location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).



###  REST 

To set the default storage location for your organization, folder, or project, do the following:

  1. For the resource whose default settings you want to set, select the appropriate endpoint and then in the APIs Explorer, specify the path parameter:

Organization:

     * API endpoint: [`organizations.locations.updateSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations/updateSettings)
     * Path parameter:
           
           organizations/ORGANIZATION_ID/locations/global/settings
           

Folder:

     * API endpoint: [`folders.locations.updateSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations/updateSettings)
     * Path parameter:
           
           folders/FOLDER_ID/locations/global/settings
           

Project:

     * API endpoint: [`projects.locations.updateSettings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations/updateSettings)
     * Path parameter:
           
           projects/PROJECT_ID/locations/global/settings
           

The variables in the preceding expressions have the following meanings:

     * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
     * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).
     * PROJECT_ID: The identifier of the project.
  2. Set the **updateMask** field as follows:
         
         updateMask=defaultStorageLocation
         

  3. Configure the **Request body** as follows:
         
         {
           "defaultStorageLocation":"DEFAULT_STORAGE_LOCATION"
         }
         

Replace DEFAULT_STORAGE_LOCATION with a [supported observability bucket location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

For example, suppose you want all new system-created observability buckets in your organization to be in the `us` location and to use CMEK. In previous steps, you granted the organization's service account an IAM role that lets it encrypt and decrypt data by using a Cloud KMS key that is in the `us` location. You complete the configuration by setting DEFAULT_STORAGE_LOCATION to `us`.

  4. Click **Execute**.

When successful, the response is a [`Settings`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/Settings) object.

For example, if you issue an `updateSettings` command and set the path parameter to an organization and set the default storage location to `us`, then the response is similar to the following:
         
         default_storage_location: "us"
         service_account_id: service-org-ORGANIZATION_ID@gcp-sa-observability.iam.gserviceaccount.com
         




## Update the default storage location for a resource

To update the default storage location for an organization, folder, or project, follow the same procedure as when you set the default storage location.

## Manage your Cloud KMS keys

The following sections describe how to change, disable, or revoke access to a Cloud KMS key.

### Update the default Cloud KMS key for a resource and location

To update the Cloud KMS key for a specific resource and location, follow the same procedure as when you set the Cloud KMS key.

### Unset the default Cloud KMS key for a resource and location

**Warning:** When you have organization policies that require CMEK, you can't unset the default Cloud KMS key for a resource and location unless an ancestor of that resource specifies a default Cloud KMS key for the location.

To unset or clear the Cloud KMS key for a specific resource and location, follow the same procedure as described in Set the default Cloud KMS key for a location. However, when you configure the request body, set the value of the key to an empty string.
    
    
    {
      "kmsKeyName"=""
    }
    

The system uses the following algorithm to determine whether a new observability bucket in a resource uses CMEK, and if so, which key to use:

  1. The system searches the resource's default settings for a Cloud KMS key for the specified location. If the resource doesn't have a default Cloud KMS key, then the system searches the ancestors of the resource for a default Cloud KMS key:

  2. After the search completes, the system does one of the following:

     * If a Cloud KMS key was found, then that key is used to encrypt the data stored in the new observability bucket.

     * If a Cloud KMS key wasn't found, then one of the following occurs:

       * When organization policies exist that require CMEK, provisioning of the new observability bucket fails.

       * When organization policies don't exist, the new observability bucket doesn't use CMEK.




### Revoke key access for a resource and location

When you configure the default settings for observability buckets for a resource and location with a Cloud KMS key, you must grant the resource's service account the [Cloud KMS CryptoKey Encrypter/Decrypter (`roles.cloudkms.cryptoKeyEncrypterDecrypter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) role for the key.

**Note:** If you revoke key access for a resource and location, then for existing observability buckets, the behavior is the same as if the key is unavailable. Additionally, the system can't create new observability buckets.

If you don't want a resource to have access to a key, then remove the IAM binding for that key. You can remove this binding by running the [`gcloud kms keys remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/remove-iam-policy-binding) command.

It might take several hours for the role change to fully propagate.

## Key-rotation behavior

Google Cloud Observability doesn't automatically rotate the encryption key for temporary disaster-recovery files when the Cloud KMS key associated with the Google Cloud organization or folder rotates. Existing recovery files continue to use the key version with which they were created. New recovery files use the current primary key version.

To learn more, see [Key rotation](https://docs.cloud.google.com/kms/docs/key-rotation).

## Limitations

The following are known limitations when you configure your default settings for observability buckets to have a CMEK setting.

### Degradation due to key unavailability

Google Cloud Observability uses the Cloud KMS API to access both Cloud KMS keys and [Cloud EKM keys](https://docs.cloud.google.com/kms/docs/ekm#considerations). Both types of keys might become unavailable.

If a key becomes unavailable, then the following occur:

  * You can't query stored data.
  * Google Cloud Observability buffers the most recent three hours of data. Data older than this sliding three-hour window might be discarded.
  * For permanent data storage, a Cloud KMS key must be available and accessible for at least 24 consecutive hours in the 48-hour period after data has been written. If the Cloud KMS key isn't available and accessible for this period, then data might not be fully persisted to storage and might be discarded.



## What's next

  * [Troubleshoot observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/troubleshoot-default-bucket-settings).
  * [Manage observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
