---
url: https://docs.cloud.google.com/bare-metal/docs/bms-encryption-keys/
title: Set up encryption keys for a server \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:07:35.951496+00:00
---

# Set up encryption keys for a server  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-encryption-keys/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up encryption keys for a server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can set up encryption keys to encrypt your server passwords. These keys are customer-managed encryption keys (CMEK) that you can manage using Cloud Key Management Service (Cloud KMS). You can set them while provisioning a new server or while reimaging an existing one. You can use an encryption key with multiple servers.

Using an encryption key is optional. However, once you set up an encryption key, you have to use it. You can't change this setting. However, you can change the key or its version.

This feature is available only for the [Linux OSes supported by Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/bms-planning#linux).

## Before you begin

  1. Using Cloud KMS, create an encryption key.

**Note:** You don't have to create the Cloud KMS key in the same project that contains your Bare Metal Solution server.

To create an encryption key, follow these steps:

     1. In the project in which you want to create the key, [enable the Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com).

Do this only once per project.

     2. [Assign the following roles](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#iam-view-access-sa-gcloud) to your Bare Metal Solution service account. Do this only once per project.

        * `roles/cloudkms.viewer`: verify that the [`CryptoKeyVersion`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion) is available to use.
        * `roles/cloudkms.publicKeyViewer`: retrieve a public key.

To learn how to grant a role, see [Granting roles on a resource](https://docs.cloud.google.com/kms/docs/iam#granting_roles_on_a_resource).

To assign these roles, use the `gcloud projects add-iam-policy-binding` command.
    
    gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
    --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-bms. \
    --role roles/cloudkms.publicKeyViewer
    
    
    gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
    --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-bms. \
    --role roles/cloudkms.viewer
    

Replace the following:

        * KMS_PROJECT_ID: the project that contains your Cloud KMS key
        * PROJECT_NUMBER: the project that contains your Bare Metal Solution server
     3. [Create an asymmetric decryption key](https://docs.cloud.google.com/kms/docs/create-key#create-asymmetric-decrypt).

**Important:** You must select **3072 bit RSA - OAEP Padding - SHA256 Digest** algorithm. Using any other algorithm can result in undecipherable passwords.

You can create as many keys and versions as required.




## Set up encryption keys while provisioning a server

You can set up an encryption key for a new Bare Metal Solution server while provisioning it through the [Google Cloud console intake form](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections).

To set up an encryption key while provisioning a server, see [Use the Google Cloud console intake form to enter your selections](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections).

## Set up encryption keys while reimaging a server

To set up encryption keys while reimaging a server, see [Change the OS for a server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#change-os-for-server).

## View encryption keys and passwords of a server

To view encryption keys and passwords of a server, follow these steps:

###  Console 

  1. Go to the **Servers** page.

[Go to Servers](https://console.cloud.google.com/compute/bareMetalSolution/servers)

  2. Click the server name.

On the **Server details** page, view the encryption key in **Password encryption key** field.

  3. To view user accounts and their corresponding encrypted passwords, go to the **User Accounts** section.




###  gcloud 

Use the `gcloud alpha bms instances auth-info` command:
    
    
    gcloud alpha bms instances auth-info SERVER_NAME --project=PROJECT_ID --region=REGION
    

Replace the following:

  * SERVER_NAME: the name of the Bare Metal Solution server
  * PROJECT_ID: the ID of the project
  * REGION: the region of the Bare Metal Solution server



## Decrypt a password

To obtain the raw password, follow these steps:

  1. Obtain the ciphertext. Use the `gcloud alpha bms instances auth-info` command.
         
         gcloud alpha bms instances auth-info SERVER_NAME \
         --project=PROJECT_ID \
         --region=REGION \
         --format='value(userAccounts.USERNAME.ENCRYPTED_PASSWORD_FILE)' | tr -d ' \n' | base64 -d > CIPHERTEXT_FILE
         

Replace the following:

     * SERVER_NAME: the name of your Bare Metal Solution server
     * PROJECT_ID: the ID of your Bare Metal Solution project
     * REGION: the location of your Bare Metal Solution server
     * USERNAME: the username of the account associated with the password you want to decrypt. The value is either `root` or `customeradmin`.
     * ENCRYPTED_PASSWORD_FILE: the file in which you saved the encrypted password. To avoid problems with the format of the password after copying it, remove the spaces and newline (`'\n'`) characters.
     * CIPHERTEXT_FILE: the name of the ciphertext file

Example:
    
    gcloud alpha bms instances auth-info my-instance \
    --region=europe-west3 \
    --project=project-testing \
    --format='value(userAccounts.customeradmin.encryptedPassword)' | tr -d ' \n' | base64 -d > ciphertext
    

To obtain the ciphertext from the password copied from the Google Cloud console, use the following command:
    
    cat ENCRYPTED_PASSWORD_FILE | tr -d ' \n' | base64 -d > CIPHERTEXT_FILE
    

Replace the following:

     * ENCRYPTED_PASSWORD_FILE: the file in which you saved the encrypted password. To avoid problems with the format of the password after copying it, remove the spaces and newline (`'\n'`) characters.
     * CIPHERTEXT_FILE: the name of the ciphertext file

Example:
    
    cat encrypted_password | tr -d ' \n' | base64 -d > ciphertext
    

  2. Decrypt the password. Follow the steps in [Decrypt data](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa#decrypt_data).




## What's next

  * [Operate your Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#operate_a_server).
  * [Check the status of a server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#check_the_status_of_a_server).
  * [Manage servers](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_servers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
