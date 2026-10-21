---
url: https://docs.cloud.google.com/storage/docs/terraform-create-bucket-upload-object/
title: Use Terraform to create storage buckets and upload objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:12.054505+00:00
---

# Use Terraform to create storage buckets and upload objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/terraform-create-bucket-upload-object/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use Terraform to create storage buckets and upload objects Stay organized with collections  Save and categorize content based on your preferences. 

In this quickstart guide, you'll create a [Terraform configuration file](https://developer.hashicorp.com/terraform/language) that provisions a storage bucket and uploads a `sample_file.txt` object to the bucket. To complete this quickstart, you'll use your local shell and terminal or the Cloud Shell Editor and Cloud Shell terminal. You'll also use the Terraform CLI, which is preinstalled in Cloud Shell.

## Before you begin

To set up a project for this quickstart, complete the following steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Storage API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=storage-component.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Storage API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=storage-component.googleapis.com)




## Create the folder structure and Terraform configuration file

To create the Terraform configuration file and the file you'll upload as an object to Cloud Storage, complete the following steps:

### Cloud Shell

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 



  2. Set the default Google Cloud project where you want to apply your Terraform configuration:  

         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

  3. In the Cloud Shell terminal, set the home directory as the active directory:  

         
         cd

  4. Create a new folder named `terraform`:  

         
         mkdir terraform

  5. Launch the Cloud Shell Editor by clicking **Open Editor** on the toolbar of the Cloud Shell window.
  6. In the **Explorer** pane, right-click the `terraform` folder and then click **New File**.
  7. Enter `main.tf` as the file name and then click **OK**.
  8. In the **Explorer** pane, right-click the `terraform` folder and then click **New File**.
  9. Enter `sample_file.txt` as the file name and then click **OK**.



### Local shell

  1. If you haven't already, [install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform#local-shell). Make sure you [install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI. 

By default, Terraform reads the configuration created by Google Cloud CLI and deploys the resources you later specify into your active Google Cloud CLI project.

  2. In your terminal, set the home directory as the active directory:  

         
         cd

  3. Create a new folder named `terraform`:  

         
         mkdir terraform

  4. In your text editor of choice, create a new file named `main.tf` in your `terraform` folder.
  5. In your text editor of choice, create a new file named `sample_file.txt` in your `terraform` folder.



## Define the infrastructure in the Terraform configuration file

To define the infrastructure you want to provision in your Terraform configuration file, complete the following steps:

  1. Open the `main.tf` file.

  2. Copy the following sample to the `main.tf` file.
         
         # Create new storage bucket in the US
         # location with Standard Storage
         
         resource "google_storage_bucket" "static" {
          name          = "BUCKET_NAME"
          location      = "US"
          storage_class = "STANDARD"
         
          uniform_bucket_level_access = true
         }
         
         # Upload a text file as an object
         # to the storage bucket
         
         resource "google_storage_bucket_object" "default" {
          name         = "OBJECT_NAME"
          source       = "OBJECT_PATH"
          content_type = "text/plain"
          bucket       = google_storage_bucket.static.id
         }

Replace:

     * BUCKET_NAME with the name of the bucket you want to create. For example, `my-bucket`.

See bucket naming requirements.
       * Bucket names can only contain lowercase letters, numeric characters, dashes (`-`), underscores (`_`), and dots (`.`). Spaces are not allowed. Names containing dots require [verification](https://docs.cloud.google.com/storage/docs/domain-name-verification).
       * Bucket names must start and end with a number or letter.
       * Bucket names must contain 3-63 characters. Names containing dots can contain up to 222 characters, but each dot-separated component can be no longer than 63 characters.
       * Bucket names cannot be represented as an IP address in dotted-decimal notation (for example, 192.168.5.4).
       * Bucket names cannot begin with the "goog" prefix.
       * Bucket names cannot contain "google" or close misspellings, such as "g00gle".
     * OBJECT_NAME with the name of the object you want to upload. For this quickstart, enter the name `sample_file.txt`.

     * OBJECT_PATH with the path to the object you want to upload. For this quickstart, enter the path `~/terraform/sample_file.txt`.

  3. Save the `main.tf` file.




## Initialize the working directory containing the Terraform configuration file

To initialize Terraform and the directory containing your Terraform configuration file, complete the following steps:

  1. In your terminal, set the `terraform` folder as the current working directory:
         
         cd ~/terraform

  2. Initialize Terraform:
         
         terraform init

  3. If you're using the Cloud Shell and you're prompted to authorize Cloud Shell, click **Authorize**.

Terraform initializes the working directory. If it successfully initializes the working directory, Terraform returns output similar to the following:
         
         Terraform has been successfully initialized!
         
         You may now begin working with Terraform. Try running "terraform plan" to see
         any changes that are required for your infrastructure. All Terraform commands
         should now work.
         
         If you ever set or change modules or backend configuration for Terraform,
         rerun this command to reinitialize your working directory. If you forget, other
         commands will detect it and remind you to do so if necessary.
         




## Preview the execution plan

The Terraform execution plan is based on the Terraform configuration and indicates the changes that Terraform plans to make to the Cloud Storage infrastructure and services.

View the Terraform execution plan:
    
    
    terraform plan

Example output:
    
    
    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
      + create
    
    Terraform will perform the following actions:
    
      # google_storage_bucket.static will be created
      + resource "google_storage_bucket" "static" {
          + force_destroy               = false
          + id                          = (known after apply)
          + location                    = "US"
          + name                        = "my-bucket"
          + project                     = "my-project"
          + public_access_prevention    = (known after apply)
          + self_link                   = (known after apply)
          + storage_class               = "STANDARD"
          + uniform_bucket_level_access = true
          + url                         = (known after apply)
    
          + versioning {
              + enabled = (known after apply)
            }
    
          + website {
              + main_page_suffix = (known after apply)
              + not_found_page   = (known after apply)
            }
        }
    
      # google_storage_bucket_object.default will be created
      + resource "google_storage_bucket_object" "default" {
          + bucket         = (known after apply)
          + content_type   = "text/plain"
          + crc32c         = (known after apply)
          + detect_md5hash = "different hash"
          + id             = (known after apply)
          + kms_key_name   = (known after apply)
          + md5hash        = (known after apply)
          + media_link     = (known after apply)
          + name           = "sample_file.txt"
          + output_name    = (known after apply)
          + self_link      = (known after apply)
          + source         = "sample_file.txt"
          + storage_class  = (known after apply)
        }
    
    Plan: 2 to add, 0 to change, 0 to destroy.
    

## Apply the changes proposed in the execution plan

To apply the changes in your Terraform configuration file, complete the following steps:

  1. Apply the changes from the execution plan to the Cloud Storage infrastructure with the following command. When you apply the changes, Terraform creates a storage bucket and uploads `sample_file.txt` to the bucket.
         
         terraform apply

Example output:
         
         Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
           + create
         
         Terraform will perform the following actions:
         
           # google_storage_bucket.static will be created
           + resource "google_storage_bucket" "static" {
               + force_destroy               = false
               + id                          = (known after apply)
               + location                    = "US"
               + name                        = "my-bucket"
               + project                     = "my-project"
               + public_access_prevention    = (known after apply)
               + self_link                   = (known after apply)
               + storage_class               = "STANDARD"
               + uniform_bucket_level_access = true
               + url                         = (known after apply)
         
               + versioning {
                   + enabled = (known after apply)
                 }
         
               + website {
                   + main_page_suffix = (known after apply)
                   + not_found_page   = (known after apply)
                 }
             }
         
           # google_storage_bucket_object.default will be created
           + resource "google_storage_bucket_object" "default" {
               + bucket         = (known after apply)
               + content_type   = "text/plain"
               + crc32c         = (known after apply)
               + detect_md5hash = "different hash"
               + id             = (known after apply)
               + kms_key_name   = (known after apply)
               + md5hash        = (known after apply)
               + media_link     = (known after apply)
               + name           = "sample_file.txt"
               + output_name    = (known after apply)
               + self_link      = (known after apply)
               + source         = "sample_file.txt"
               + storage_class  = (known after apply)
             }
         
         Plan: 2 to add, 0 to change, 0 to destroy.
         
         Do you want to perform these actions?
           Terraform will perform the actions described above.
           Only 'yes' will be accepted to approve.
         
           Enter a value:
         

  2. Type `yes` and press **Enter**.

If successful, Terraform returns output similar to the following:
         
         Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
         




## View your storage bucket and uploaded object

In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

The new bucket appears, containing the `sample_file.txt` object. Note that the resources might take a few minutes to get provisioned after you run `terraform apply`.

## Clean up your project

In order to avoid incurring unexpected charges from the Google Cloud resources you created during this quickstart, complete the following steps to clean up the resources:

  1. In your terminal, set the `terraform` folder as the current working directory:
         
         cd ~/terraform

  2. Delete the Cloud Storage resources that you created based on your Terraform configuration file:
         
         terraform destroy

  3. If successful, Terraform returns output similar to the following:
         
         Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
           - destroy
         
         Terraform will perform the following actions:
         
           # google_storage_bucket.static will be destroyed
           - resource "google_storage_bucket" "static" {
               - default_event_based_hold    = false -> null
               - force_destroy               = false -> null
               - id                          = "my-bucket" -> null
               - labels                      = {} -> null
               - location                    = "US" -> null
               - name                        = "" -> null
               - project                     = "example-project" -> null
               - public_access_prevention    = "inherited" -> null
               - requester_pays              = false -> null
               - self_link                   = "https://www.googleapis.com/storage/v1/b/cbonnie-bucket-9" -> null
               - storage_class               = "STANDARD" -> null
               - uniform_bucket_level_access = true -> null
               - url                         = "gs://BUCKET_NAME" -> null
             }
         
           # google_storage_bucket_object.default will be destroyed
           - resource "google_storage_bucket_object" "default" {
               - bucket           = "my-bucket" -> null
               - content_type     = "text/plain" -> null
               - crc32c           = "yZRlqg==" -> null
               - detect_md5hash   = "XrY7u+Ae7tCTyyK7j1rNww==" -> null
               - event_based_hold = false -> null
               - id               = "my-bucket-sample_file.txt" -> null
               - md5hash          = "XrY7u+Ae7tCTyyK7j1rNww==" -> null
               - media_link       = "https://storage.googleapis.com/download/storage/v1/b/BUCKET_NAME/o/sample_file.txt?generation=1675800386233102&alt=media" -> null
               - metadata         = {} -> null
               - name             = "sample_file.txt" -> null
               - output_name      = "sample_file.txt" -> null
               - self_link        = "https://www.googleapis.com/storage/v1/b/BUCKET_NAME/o/sample_file.txt" -> null
               - source           = "sample_file.txt" -> null
               - storage_class    = "STANDARD" -> null
               - temporary_hold   = false -> null
             }
         
         Plan: 0 to add, 0 to change, 2 to destroy.
         
         Do you really want to destroy all resources?
           Terraform will destroy all your managed infrastructure, as shown above.
           There is no undo. Only 'yes' will be accepted to confirm.
         
           Enter a value:
         

  4. Type `yes` and press **Enter**. If successful, Terraform returns output similar to the following:
         
         Destroy complete! Resources: 2 destroyed.
         

  5. In your terminal, delete the `terraform` folder.
         
         rm -rf ~/terraform

  6. To verify that the bucket and object were deleted, go to the **Buckets** page in the Google Cloud console.

[Go to Buckets](https://console.cloud.google.com/storage/browser)




## What's next

  * See [Terraform resources available for Cloud Storage](https://docs.cloud.google.com/storage/docs/terraform-for-cloud-storage).
  * See [Terraform resources for other Google Cloud products](https://docs.cloud.google.com/docs/terraform#docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
