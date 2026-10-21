---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/export-permissions-step-by-step/
title: Configuring Google Cloud permissions and Cloud Storage for data export from Cloud Storage to appliance step-by-step \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:06.966226+00:00
---

# Configuring Google Cloud permissions and Cloud Storage for data export from Cloud Storage to appliance step-by-step  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/export-permissions-step-by-step/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Configuring Google Cloud permissions and Cloud Storage for data export from Cloud Storage to appliance step-by-step Stay organized with collections  Save and categorize content based on your preferences. 

This document describes configuring Google Cloud permissions and Cloud Storage step-by-step, including:

  * Preparing your Cloud Storage bucket.
  * Preparing a Cloud Key Management Service key to secure your data.
  * Providing the Transfer Appliance Team your Cloud Storage bucket configuration data.



## Before you begin

Ensure that you have an email from the Transfer Appliance Team titled _Google Transfer Appliance Permissions_. This email contains:

  * The names of the service accounts required for your transfer.

  * A session ID that you'll need to configure your appliance.

  * A form that you'll complete once you've configured your account.




## Prepare the permissions on Cloud Storage bucket

We use two [_service accounts_](https://docs.cloud.google.com/iam/docs/service-accounts) to transfer your data. Service accounts are special accounts that are used by an application, not a person, to do work. In this case, the service accounts allow Transfer Appliance to use Cloud Storage resources on your behalf to transfer data between Cloud Storage and the appliance. You grant these accounts the necessary roles to transfer data.

To prepare the Cloud Storage bucket, follow these steps:

  1. In an email titled _Google Transfer Appliance Permissions_ , the Transfer Appliance Team provides you the following service accounts:

     * A **session service account** that is tied to this particular transfer. It looks like the following example:

`ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com`

In this example, `SESSION_ID` is the session ID for this particular transfer.

     * A **[service agent](https://docs.cloud.google.com/iam/docs/service-agents)** that is tied to the Transfer service for on-premises data service, which we use to transfer data between Cloud Storage and the appliance. It looks similar to the following example:

`project-TENANT_IDENTIFIER@storage-transfer-service.iam.gserviceaccount.com`

In this example, `TENANT_IDENTIFIER` is a generated number specific to this particular project.

Note the service accounts for the next steps.

The service accounts allow Transfer Appliance to manipulate Google Cloud resources on your behalf, namely to transfer data between Cloud Storage and the appliance. You grant these accounts the necessary roles to transfer data between Cloud Storage and the appliance.

  2. Cloud Storage buckets are tied to Google Cloud projects. The bucket you select must be in the same project as was used to order the appliance.

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

Transfer Appliance secures your data on the appliance by encrypting the data. A Cloud Key Management Service (Cloud KMS) public [_key_](https://docs.cloud.google.com/kms/docs/resource-hierarchy#keys) is used to encrypt your data on Transfer Appliance, and a private key is used to decrypt your data.

We use the session service account from Prepare the permissions on Cloud Storage bucket to upload the data from your Cloud Storage bucket to the appliance.

You have the following option for managing encryption keys:

  * **Create and manage encryption keys yourself**. You create and manage the encryption keys used for your transfer, by following the directions below. You prepare a Cloud KMS asymmetric decryption key and add the session service account to the key.



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

**Note:** If your project uses VPC Service Controls, verify that the Cloud Storage bucket and the Cloud KMS key that you provide are within the same project. For more information, see [List and describe service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#list-and-describe).

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

     7. Select **Add another role** and add the **Cloud KMS CryptoKey Decrypter** role.

     8. Click **Save**.

### Command line

     1. Run the following command to grant the session service account the **`roles/cloudkms.publicKeyViewer`** role:
            
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

We send an email titled _Google Transfer Appliance Permissions_ to collect information about your Cloud Storage bucket. We use the information you provide to configure the transfer data between Cloud Storage and the Transfer Appliance..

In the form linked from that email, enter the following information:

  * The **Google Cloud project ID**.
  * Select your choice for **Encryption** : 
    * **Customer-managed encryption key** , select the encryption key from the **Select a customer-managed encryption-key** drop-down menu.
  * The **Google Cloud Cloud Storage bucket name** used for this transfer.



## What's next?

[Configure IP network ports](https://docs.cloud.google.com/transfer-appliance/docs/4.0/ip-network-ports) for Transfer Appliance to work on your network.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
