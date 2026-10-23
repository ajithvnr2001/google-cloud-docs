---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/permissions-step-by-step/
title: Configuring Google Cloud permissions and Cloud Storage step-by-step \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:08.881218+00:00
---

# Configuring Google Cloud permissions and Cloud Storage step-by-step  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/permissions-step-by-step/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)



Send feedback 

#  Configuring Google Cloud permissions and Cloud Storage step-by-step Stay organized with collections  Save and categorize content based on your preferences. 

This document describes configuring Google Cloud permissions and Cloud Storage step-by-step, including:

  * Preparing your destination Cloud Storage bucket.
  * Preparing a Cloud Key Management Service key to secure your data.
  * Providing the Transfer Appliance Team your Cloud Storage bucket configuration data.



## Before you begin

Ensure that you have an email from the Transfer Appliance Team titled _Google Transfer Appliance Prepare Permissions and Storage_. This email contains:

  * The names of the service accounts required for your transfer.

  * A session ID that you'll need to configure your appliance.

  * A form that you'll complete once you've configured your account.




## Prepare the destination Cloud Storage bucket

To store your data in Cloud Storage, you must prepare a [_bucket_](https://docs.cloud.google.com/storage/docs/buckets). Buckets are the basic containers that hold your data within Cloud Storage.

We use two [_service accounts_](https://docs.cloud.google.com/iam/docs/service-accounts) to move your data from Transfer Appliance to the destination Cloud Storage bucket that you prepare. Service accounts are special accounts that are used by an application, not a person, to do work. In this case, the service accounts allow Transfer Appliance to use Cloud Storage resources on your behalf to copy data from the appliance to your Cloud Storage bucket. You grant these accounts the necessary roles to copy data from the appliance to your Cloud Storage bucket.

To prepare the destination Cloud Storage bucket, follow these steps:

  1. In an email titled _Google Transfer Appliance Prepare Destination Bucket_ , the Transfer Appliance Team provides you the following service accounts:

     * A **session service account** that is tied to this particular transfer. It looks like the following example:

`ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com`

In this example, `SESSION_ID` is the session ID for this particular transfer.

     * A **[service agent](https://docs.cloud.google.com/iam/docs/service-agents)** that is tied to the Transfer service for on-premises data service, which we use to transfer data from the appliance to your Cloud Storage bucket. It looks similar to the following example:

`project-TENANT_IDENTIFIER@storage-transfer-service.iam.gserviceaccount.com`

In this example, `TENANT_IDENTIFIER` is a generated number specific to this particular project.

Note the service accounts for the next steps.

The service accounts allow Transfer Appliance to manipulate Google Cloud resources on your behalf, namely to copy data from the appliance to Cloud Storage. You grant these accounts the necessary roles to copy data from the appliance to your Cloud Storage bucket.

  2. Cloud Storage buckets are tied to Google Cloud projects. The bucket you select must be in the same project as was used to order the appliance.

If you don't have a Cloud Storage bucket, create one:

###  Google Cloud Console 

     1. Open the Cloud Storage Buckets page in the Google Cloud console.

[ Open the Cloud Storage Buckets page](https://console.cloud.google.com/storage/browser)

     2. Click **Create bucket** to open the bucket creation form.

     3. Enter your bucket information and click **Continue** to complete each step:

        * Specify a **Name** , subject to the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

        * Select a **Default storage class** for the bucket. The default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) is assigned by default to all objects uploaded to the bucket. Next, select a **Location** for the bucket data.

        * Select an **Access control** model to determine how you [control access](https://docs.cloud.google.com/storage/docs/access-control) to the bucket's objects.

        * Optionally, you can add [bucket labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels) and choose an [encryption method](https://docs.cloud.google.com/storage/docs/encryption).

        * Do not set a retention policy on the bucket.

     4. Click **Done**.

### Command line

Use the [`gcloud storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) command:
    
    gcloud storage buckets create gs://BUCKET_NAME --uniform-bucket-level-access --location=LOCATION --project=PROJECT_ID
    

In this example:

     * `BUCKET_NAME`: The name of the bucket you're creating, subject to [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `LOCATION`: Your desired Cloud Storage [bucket location](https://docs.cloud.google.com/storage/docs/locations).
     * `PROJECT_ID`: The project ID to create your bucket under.

Do not set a retention policy on the bucket.

  3. To grant the Transfer Appliance service accounts permission to use your Cloud Storage bucket, do the following:

###  Google Cloud Console 

     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click the **Bucket overflow** menu (![](https://docs.cloud.google.com/static/transfer-appliance/docs/images/overflow_menu_icon.png)) associated with the bucket to which you are granting principal a role.

     3. Choose **Edit bucket permissions**.

     4. Click the **\+ Add principals** button.

     5. In the **New principals** field, enter the following identities:

        * The session service account. It looks like the following example:

`ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com`

In this example, `SESSION_ID` is the session ID for this particular transfer.

        * The Transfer service for on-premises data service agent. It looks similar to the following example:

`project-TENANT_IDENTIFIER@storage-transfer-service.iam.gserviceaccount.com`

In this example, `TENANT_IDENTIFIER` is a generated number specific to this particular project.

     6. From the **Select a role** drop-down menu, select the **Storage Admin** role.

The roles you select appear in the pane with a short description of the permissions they grant.

     7. Click **Save**.

### Command line

Use the [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) command:
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
    --member=serviceAccount:ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com \
    --role=roles/storage.admin
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
    --member=serviceAccount:project-TENANT_IDENTIFIER@storage-transfer-service.iam.gserviceaccount.com \
    --role=roles/storage.admin
    

In this example:

     * `BUCKET_NAME`: The name of the bucket you're creating.
     * `SESSION_ID`: The session ID for this particular transfer.
     * `TENANT_IDENTIFIER`: A generated number specific to this particular project.




## Prepare the Cloud KMS key

Transfer Appliance secures your data on the appliance by encrypting the data before you ship the appliance back to us. A Cloud Key Management Service (Cloud KMS) public [_key_](https://docs.cloud.google.com/kms/docs/resource-hierarchy#keys) is used to encrypt your data on Transfer Appliance, and a private key is used to decrypt your data.

We use the session service account from Prepare the destination Cloud Storage bucket to upload the data from the appliance to your Cloud Storage bucket.

You have the following options for managing encryption keys:

  * **Google-owned and Google-managed encryption keys**. You can request that we create and manage the Cloud KMS keys for you. If you want to use this method, you are done with configuring your Google Cloud project and you can continue with steps described in [Receive your appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance).

  * **Create and manage encryption keys yourself**. You create and manage the encryption keys used for your transfer, by following the directions below. You prepare a Cloud KMS asymmetric decryption key and add the session service account to the key. The session service account uses the asymmetric decryption key to decrypt and copy your data to Cloud Storage.




To prepare Cloud KMS keys, do the following:

  1. If you don't have a Cloud Key Management Service key ring, do the following to create one:

###  Google Cloud Console 

     1. Go to the **Cryptographic Keys** page in the Google Cloud console.

[Go to the Cryptographic Keys page](https://console.cloud.google.com/security/kms)

     2. Click **Create key ring**.

     3. In the **Key ring name** field, enter the desired name for your key ring.

     4. From the **Key ring location** dropdown, select a location like `"us-east1"`.

     5. Click **Create**.

### Command line
    
    gcloud kms keyrings create KEY_RING --location=LOCATION --project=PROJECT_ID
    

In this example:

     * `LOCATION`: The Cloud Key Management Service location for the key ring. For example, `global`.
     * `KEY_RING`: The key ring's name.
     * `PROJECT_ID`: The Google Cloud project ID that your storage bucket is under.

  2. Create an asymmetric decryption key by doing the following:

**Note:** If your project uses VPC Service Controls, verify that the destination Cloud Storage bucket and the Cloud KMS key that you provide are within the same project. For more information, see [List and describe service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#list-and-describe).

###  Google Cloud Console 

     1. Go to the **Cryptographic Keys** page in the Google Cloud console.

[Go to the Cryptographic Keys page](https://console.cloud.google.com/security/kms)

     2. Click the name of the key ring that you want to create a key for.

     3. Click **Create key**.

     4. In the **What type of key do you want to create?** section, choose **Generated key**.

     5. In the **Key name** field, enter the name for your key.

     6. Click the **Protection level** dropdown and select **Software**.

     7. Click the **Purpose** dropdown and select **Asymmetric decrypt**.

     8. Click the **Algorithm** dropdown and select **4096-bit RSA - OAEP Padding - SHA256 Digest**

     9. Click **Create**.

### Command line

Run the following command to create an asymmetric decryption key:
    
    gcloud kms keys create KEY --keyring=KEY_RING \
    --location=LOCATION --purpose=asymmetric-encryption \
    --default-algorithm=rsa-decrypt-oaep-4096-sha256 \
    --project=PROJECT_ID
    

In this example:

     * `KEY`: The name of the Cloud Key Management Service key. For example, `ta-key`.
     * `KEY_RING`: The key ring's name.
     * `LOCATION`: The Cloud Key Management Service location for the key ring. For example, `global`.
     * `PROJECT_ID`: The Google Cloud project ID that your storage bucket is under.

  3. Add the session service account as a principal to the asymmetric key by doing the following:

###  Google Cloud Console 

     1. Go to the **Cryptographic Keys** page in Google Cloud console.

[Go to the Cryptographic Keys page](https://console.cloud.google.com/security/kms)

     2. Click the key ring that contains your asymmetric key.

     3. Select the checkbox for the asymmetric key.

     4. In the **Info panel** , click **Add principal**.

**Add principals** is displayed.

     5. In the **New principals** field, enter the session service account provided by the Transfer Appliance Team. It looks like the following example:

`ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com`

In this example, `SESSION_ID` is the session ID for this particular transfer.

     6. In the **Select a role** field, add the **Cloud KMS CryptoKey Public Key Viewer** role.

     7. Click **Add another role**.

     8. In the **Select a role** field, add the **Cloud KMS CryptoKey Decrypter** role.

     9. Click **Save**.

### Command line

     1. Run the following command to grant the session service account the **`roles/cloudkms.cryptoKeyDecrypter`** role:
            
            gcloud kms keys add-iam-policy-binding KEY \
            --keyring=KEY_RING --location=LOCATION \
            --member=serviceAccount:ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com \
            --role=roles/cloudkms.cryptoKeyDecrypter
            

In this example:

        * `KEY`: The name of the Cloud Key Management Service key. For example, `ta-key`.
        * `KEY_RING`: The key ring's name.
        * `LOCATION`: The Cloud Key Management Service location for the key ring. For example, `global`.
        * `SESSION_ID`: The session ID for this particular transfer.
     2. Run the following command to grant the session service account the **`roles/cloudkms.publicKeyViewer`** role:
            
            gcloud kms keys add-iam-policy-binding KEY \
            --keyring=KEY_RING --location=LOCATION \
            --member=serviceAccount:ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com \
            --role=roles/cloudkms.publicKeyViewer
            

In this example:

        * `KEY`: The name of the Cloud Key Management Service key. For example, `ta-key`.
        * `KEY_RING`: The key ring's name.
        * `LOCATION`: The Cloud Key Management Service location for the key ring. For example, `global`.
        * `SESSION_ID`: The session ID for this particular transfer.

  4. Obtain your asymmetric key's path by doing the following:

###  Google Cloud Console 

     1. Go to the **Cryptographic Keys** page in the Google Cloud console.

[Go to the Cryptographic Keys page](https://console.cloud.google.com/security/kms)

     2. Click the key ring that contains your asymmetric decryption key.

     3. Click the asymmetric decryption key's name.

     4. Select the key version that you want, and click More _more_vert_.

     5. Click **Copy Resource Name**.

An example of the key format is:
            
            projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY/cryptoKeyVersions/VERSION_NUMBER

In this example:

        * `PROJECT_ID`: The Google Cloud project ID that your storage bucket is under.
        * `LOCATION`: The Cloud Key Management Service location for the key ring.
        * `KEY_RING`: The key ring's name.
        * `KEY`: The name of the Cloud Key Management Service key.
        * `VERSION_NUMBER`: The key's version number.

The Transfer Appliance Team requires the entire key path, including the version number, so they can apply the correct key to your data.

### Command line

Run the following command to list your asymmetric key's full path, including its version number:
    
    gcloud kms keys versions list --keyring=KEY_RING \
    --key=KEY --location=LOCATION \
    --project=PROJECT_ID
    

In this example:

     * `KEY_RING`: The name of your key ring.
     * `KEY`: The name of your asymmetric key.
     * `LOCATION`: The Google Cloud location of the key ring.
     * `PROJECT_ID`: The Google Cloud project ID that your storage bucket is under.

The following sample response resembles the output that is returned:
    
    NAME STATE
    projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY/cryptoKeyVersions/VERSION_NUMBER
    ENABLED
    

In this example:

     * `PROJECT_ID`: The Google Cloud project ID that your storage bucket is under.
     * `LOCATION`: The Cloud Key Management Service location for the key ring.
     * `KEY_RING`: The key ring's name.
     * `KEY`: The name of the Cloud Key Management Service key.
     * `VERSION_NUMBER`: The key's version number.

The Transfer Appliance Team requires the string under `NAME` that ends in `/cryptoKeyVersions/VERSION_NUMBER`, where `VERSION_NUMBER` is your key's version number.




## Provide the Transfer Appliance Team with bucket configuration data

We send an email titled _Google Transfer Appliance Prepare Permissions and Storage_ to collect information about your Cloud Storage bucket. We use the information you provide to configure the transfer from Transfer Appliance to Cloud Storage.

In the form linked from that email, enter the following information:

  * The **Google Cloud project ID**.
  * Select your choice for **Encryption** : 
    * **Google-owned and Google-managed encryption key** , if you chose to have Google to manage your encryption key.
    * **Customer-managed encryption key** , if you chose to manage your own encryption key. Select the desired encryption key from the **Select a customer-managed encryption-key** drop-down menu.
  * The **Google Cloud Cloud Storage destination bucket name** used for this transfer.
  * Optional: An **object prefix**. Without an object prefix, objects are transferred to Cloud Storage with the source's path, not including the root path, before the file name on the filesystem. For example, if you have the following files: 
    * `/source_root_path/file1.txt`
    * `/source_root_path/dirA/file2.txt`
    * `/source_root_path/dirA/dirB/file3.txt`
Then the object names in Cloud Storage are: 
    * `file1.txt`
    * `dirA/file2.txt`
    * `dirA/dirB/file3.txt`
The object prefix is added to the object's destination name in Cloud Storage, after the `/` character of the destination bucket name and before any path names that the object was transferred from, not including the source's root path. This can help you distinguish between objects transferred from other transfer jobs. The following table demonstrates several examples of object prefixes and their resulting object names in Cloud Storage, if the source object's path is `/source_root_path/sub_folder_name/object_name`: Prefix | Destination object name  
---|---  
None | `/destination_bucket/sub_folder_name/object_name`  
`prefix/` | `/destination_bucket/prefix/sub_folder_name/object_name`  



## What's next?

[Configure IP network ports](https://docs.cloud.google.com/transfer-appliance/docs/4.0/ip-network-ports) for Transfer Appliance to work on your network.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
