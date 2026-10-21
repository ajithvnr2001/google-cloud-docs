---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/permissions-application/
title: Configure your Google Cloud project using the setup application \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:17.102035+00:00
---

# Configure your Google Cloud project using the setup application  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/permissions-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)



Send feedback 

#  Configure your Google Cloud project using the setup application Stay organized with collections  Save and categorize content based on your preferences. 

This document describes configuring Google Cloud permissions and Cloud Storage using the Appliance Cloud Setup Application.

The Appliance Cloud Setup Application prompts you for information, such as your transfer session ID, destination Cloud Storage bucket and Cloud Key Management Service (Cloud KMS) preferences. Using the information you provide, the Appliance Cloud Setup Application configures your Google Cloud permissions, preferred Cloud Storage bucket, and Cloud KMS key for your transfer.

## Before you begin

Ensure that you have the following:

  * The name of the project and the business location used for ordering the appliance.

  * The Appliance ID, session ID, bucket name, bucket prefix, and encryption key specified when ordering the appliance. These can be found in the email titled **Google Transfer Appliance Prepare Permissions and Storage**.

  * The Storage Transfer Service **service agent** listed in the email titled **Google Transfer Appliance Prepare Permissions and Storage**. It looks similar to the following example:

`project-TENANT_IDENTIFIER@storage-transfer-service.iam.gserviceaccount.com`

In this example, `TENANT_IDENTIFIER` is a generated number specific to this particular project.

We use Storage Transfer Service to transfer data from the appliance to your Cloud Storage bucket.




## Assign IAM roles

You must have the correct [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) on the project and Cloud Storage bucket.

If you are the project owner, `roles/owner` is sufficient. Skip to the next section, Download the Appliance Cloud Setup Application.

If you don't have `roles/owner` you must have the following roles:

  * `roles/serviceusage.serviceUsageAdmin`: To enable the required APIs in the project.
  * `roles/iam.serviceAccountCreator`: To create new service accounts.
  * `roles/iam.serviceAccountKeyAdmin`: To create and download service account keys. Can be granted at the project level, or can be granted to the Appliance service account once it's been created by the permissions app.
  * `roles/storagetransfer.admin`: To create the Storage Transfer Service service account.
  * `roles/transferappliance.viewer`: To fetch Cloud Storage bucket and Cloud Key Management Service key details.
  * `roles/storage.admin`: Can be granted at the project level if you haven't created a Cloud Storage bucket, or can be granted at the bucket level if you're using an existing Cloud Storage bucket.
  * `roles/cloudkms.admin`: Can be granted at the project level if you haven't created a Cloud KMS key, or can be granted at the key level if you're using an existing Cloud KMS key.



### Viewing roles

To view IAM roles that your principals have for a project and its resources, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. The page displays all the principals that have IAM roles on your project.




## Download the Appliance Cloud Setup Application

To download the Appliance Cloud Setup Application:

  1. Open the Google Cloud console Welcome page.

[ Open the Google Cloud console Welcome page](https://console.cloud.google.com/welcome)

  2. Verify that the name of the project used for the transfer is displayed in the project selector. The project selector tells you what project you are currently working in.

![Selecting a Google Cloud project from the project selector](https://docs.cloud.google.com/static/iam/img/quickstart-project-selector.png)

If you don't see the name of the project you are using for the transfer, click the project selector, then select the correct project.

  3. Click Activate Cloud Shell.

![Starting devshell from the menu bar.](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/devshell.png)

  4. In Cloud Shell, use the `wget` command to download the Appliance Cloud Setup Application:
         
         wget https://storage.googleapis.com/transferappliance/cloudsetup/ta_cloudsetup_x86_64-linux -O ta_cloudsetup_x86_64-linux
         




## Run the Appliance Cloud Setup Application

In Cloud Shell, run the following command to start the Appliance Cloud Setup Application:
    
    
    chmod 0777 ta_cloudsetup_x86_64-linux && ./ta_cloudsetup_x86_64-linux
    

The app walks you through the steps required to configure your project.

### Application output

The Appliance Cloud Setup Application completes the following actions:

  * Grants permissions to the Appliance service accounts used to transfer data to your Cloud Storage bucket.
  * If you chose to use a customer-managed encryption key, grants permission to the Appliance service accounts to access Cloud KMS key data.
  * Displays the following information:

    * The **Google Cloud cryptographic key resource name** , if you chose to use a customer-managed Cloud KMS encryption key.
    * The **Google Cloud Cloud Storage destination bucket name**.
    * A **Google Cloud Cloud Storage destination bucket prefix** , if you supplied one.
    * If applicable, the Online Transfer service account name, and the Storage Transfer Service service agent name.



The information displayed is also stored within the home directory on Cloud Shell, named `SESSION_ID-output.txt`, where `SESSION_ID` is the session ID for this particular transfer.

The names of the service accounts granted permission for this particular transfer are stored within the home directory on Cloud Shell, named `cloudsetup.log`.

## Send CMEK information to Google

If you specified a customer-managed encryption key, send us the key information by completing the form linked from the email titled **Google Transfer Appliance Prepare Permissions and Storage**.

## Download service account keys

Download and save a service account key for the Online Transfer Service Account.
    
    
    gcloud iam service-accounts keys create key.json \
      --iam-account=APPLIANCE_SERVICE_ACCOUNT_EMAIL

The value of APPLIANCE_SERVICE_ACCOUNT_EMAIL is displayed in the output of the permissions app:
    
    
    ...
    
    Appliance Service Account Name:
    example-sa@example-project.iam.gserviceaccount.com
    

When you receive your appliance, upload the key to the `/tmp` directory on the appliance.

## Troubleshooting

### Error 400: Service account does not exist

**Issue:**

Appliance Cloud Setup Application displays the following message:
    
    
    Service account ta-SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com
    does not exist.
    

Where `SESSION_ID` is the session ID provided to Appliance Cloud Setup Application.

**Solution:**

Verify the session ID for your transfer. The session ID is unique to each transfer session and shared by the Transfer Appliance Team. If you haven't received a session ID, contact [data-support@google.com](mailto:data-support@google.com).

### Error: Listing KMS locations

**Issue:**

Appliance Cloud Setup Application displays the following message:
    
    
    Error: listing kms locations
    

**Solution:**

Do the following within Cloud Shell:

  1. Re-authenticate by running `gcloud auth login`.

  2. Retry Appliance Cloud Setup Application.




If the error persists, contact the Transfer Appliance Team at [data-support@google.com](mailto:data-support@google.com).

### Error: Creating Cloud KMS key constraint error

**Issue:**

Appliance Cloud Setup Application displays a message similar to the following:
    
    
    Error: creating cloud kms key violates constraint error: code = FailedPrecondition
    desc= europe-west6 violates constraint 'constraints/gcp.resourceLocations' on
    the resource 'projects/test/locations/europe-west6'
    

**Solution:**

Your Google Cloud project may have organization policies that disallow creating Cloud Key Management Service keys in certain locations. The following are possible solutions:

  * Choose a different location to create the Cloud Key Management Service key.
  * Update the organization policy to allow Cloud Key Management Service key creation in the location you desire.



For more information see [Restricting Resource Locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
