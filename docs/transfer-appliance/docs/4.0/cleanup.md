---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/cleanup/
title: Clean up access \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:42.798300+00:00
---

# Clean up access  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/cleanup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Clean up access Stay organized with collections  Save and categorize content based on your preferences. 

After we complete copying your data from all appliances, we recommend that you remove the access previously granted to our service accounts. This applies the practice of least privilege to your data and helps ensure your data's security.

This section describes:

  * Revoking our service accounts from accessing your Cloud Storage buckets.
  * Revoking our service accounts from accessing your Cloud KMS roles.
  * Destroying the Cloud KMS key used to encrypt your data on Transfer Appliance.



Wait until we copy all of your data to Cloud Storage before completing the steps below.

**Important:** If you are using the Cloud KMS key that you generated and shared with the Transfer Appliance Team for any other purpose, including for other appliances copying data or for use in your Cloud Storage bucket, do not destroy the key.

Once the Cloud KMS key is destroyed, any encrypted data on Transfer Appliance cannot be recovered. Similarly, once you revoke the service accounts from Cloud Storage buckets and the Cloud KMS key, no further data can be copied from the appliance to your Cloud Storage buckets.

### Revoking Cloud KMS key access for the service account

Revoking Cloud KMS key access for the Transfer Appliance service account ensures that we can no longer decrypt Transfer Appliance data on your behalf.

**Important:** If another transfer is in progress or if another appliance is using the same key, do not revoke Cloud KMS key access for the service account. Revoking access stops the transfer.

To revoke Cloud KMS CryptoKey Decrypter and Cloud KMS CryptoKey Public Key Viewer roles from the service account, follow these steps:

###  Google Cloud Console 

  1. Go to the **Cryptographic Keys** page in the Google Cloud console.

[Go to the Cryptographic Keys page](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key used in Prepare the Cloud KMS key.

  3. Select the checkbox for the key whose access you are revoking from the service account.

  4. Click **Show Info Panel**.

The information panel is displayed.

  5. To revoke the **Cloud KMS CryptoKey Decrypter** role from the service account, do the following:

     1. In the **Permissions** tab, expand **Cloud KMS CryptoKey Decrypter**.

     2. Locate the service account. It looks like the following example:

`service-PROJECT_ID@gcp-sa-transferappliance.iam.gserviceaccount.com`

In this example, `PEOJECT_ID` is the Google Cloud project ID that your key is under.

     3. Click delete Delete.

     4. In the delete window, select the service account and click **Remove**.

  6. To revoke the **Cloud KMS CryptoKey Public Key Viewer** role from the service account, do the following:

     1. In the **Permissions** tab, expand the **Cloud KMS CryptoKey Public Key Viewer** role.

     2. Locate the session service account. It looks like the following example:

`service-PROJECT_ID@gcp-sa-transferappliance.iam.gserviceaccount.com`

In this example, `PEOJECT_ID` is the Google Cloud project ID that your key is under.

     3. Click delete Delete.

     4. In the delete window, select the checkbox next to the service account and click **Remove**.




### Command line

  1. Run the following command to revoke the **roles/cloudkms.cryptoKeyDecrypter** role from the session service account:
         
         gcloud kms keys remove-iam-policy-binding KEY \
           --keyring KEY_RING \
           --location LOCATION \
           --member=serviceAccount:service-PROJECT_ID@gcp-sa-transferappliance.iam.gserviceaccount.com \
           --role roles/cloudkms.cryptoKeyDecrypter
         

In this example:

     * `KEY`: The name of the Cloud Key Management Service key. For example, `ta-key`.
     * `KEY_RING`: The key ring's name.
     * `LOCATION`: The Cloud Key Management Service location for the key ring. For example, `global`.
     * `PROJECT_ID`: The Google Cloud project ID that your key is under.
  2. Run the following command to revoke the **roles/cloudkms.publicKeyViewer** role from the session service account:
         
         gcloud kms keys remove-iam-policy-binding KEY \
           --keyring KEY_RING \
           --location LOCATION \
           --member=serviceAccount:service-PROJECT_ID@gcp-sa-transferappliance.iam.gserviceaccount.com \
           --role roles/cloudkms.publicKeyViewer
         

In this example:

     * `KEY`: The name of the Cloud Key Management Service key. For example, `ta-key`.
     * `KEY_RING`: The key ring's name.
     * `LOCATION`: The Cloud Key Management Service location for the key ring. For example, `global`.
     * `PROJECT_ID`: The Google Cloud project ID that your key is under.



### Revoking Cloud Storage bucket access for the service accounts

Revoking Cloud Storage bucket access for the Transfer Appliance service accounts ensures that we can no longer use Cloud Storage resources on your behalf.

**Important:** If another transfer is in progress, do not revoke Cloud Storage bucket access for the Transfer Appliance service accounts. Revoking access for either service account stops the transfer.

To revoke Cloud Storage bucket access for the Transfer Appliance service accounts, do the following:

###  Google Cloud Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Locate the Cloud Storage bucket that your data was copied to and select the checkbox next to the bucket name.

  3. Click **Show Info Panel**.

The information panel is displayed.

  4. In the **Permissions** tab, expand **Storage Admin Role**.

  5. Locate the associated service accounts. There will be from 2 to 4 accounts depending on your configuration. Service accounts are described in [Service account quick reference](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-permissions#service_account_quick_reference).

For each service account:

     1. Click delete Delete.

     2. To confirm deletion, select the checkbox next to the service account and click **Remove**.




### Command line

Use the [`gcloud storage buckets remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding) command:
    
    
    gcloud storage buckets remove-iam-policy-binding gs://BUCKET_NAME\
    --member=serviceAccount:ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com \
    --role=roles/storage.admin
    
    
    
    gcloud storage buckets remove-iam-policy-binding gs://BUCKET_NAME\
    --member=serviceAccount:project-IDENTIFIER@storage-transfer-service.iam.gserviceaccount.com \
    --role=roles/storage.admin
    

You may have additional service accounts, depending on your configuration. Refer to the [Service account quick reference](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-permissions#service_account_quick_reference) for details.

In this example:

  * `SESSION_ID`: The session ID for this particular transfer.
  * `IDENTIFIER`: A generated number specific to this particular project.
  * `BUCKET_NAME`: The name of your Cloud Storage bucket.



### Destroying the Cloud KMS key

Destroying the Cloud KMS key ensures that any data previously encrypted by the key can no longer be decrypted by anyone.

**Important:** If you are using the Cloud KMS key that you generated and shared with the Transfer Appliance Team for any other purpose, including for other appliances copying data or for use in your Cloud Storage bucket, do not destroy the key.

For more information about destroying keys, see [Destroying and restoring key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

To destroy the Cloud KMS key, do the following:

###  Google Cloud Console 

  1. Go to the **Cryptographic Keys** page in the Google Cloud console.

[Go to the Cryptographic Keys page](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring used to Prepare the Cloud KMS key.

  3. Locate the row that contains the key you are destroying.

  4. Select more_vert **More > Destroy**.

A confirmation dialog is displayed.

  5. In the confirmation dialog, click **Schedule destruction**.




### Command line

Use the `gcloud kms keys version destroy` command:
    
    
    gcloud kms keys versions destroy VERSION_NUMBER
    --keyring=KEY_RING \
    --key=KEY --location=LOCATION \
    --project=PROJECT_ID
    

In this example:

  * `VERSION_NUMBER`: The key's version number.
  * `KEY_RING`: The name of your key ring.
  * `KEY`: The name of your asymmetric key.
  * `LOCATION`: The Google Cloud location of the key ring.
  * `PROJECT_ID`: The Google Cloud project ID that your key is under.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
