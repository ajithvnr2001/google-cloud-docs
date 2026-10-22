---
url: https://docs.cloud.google.com/storage/docs/authentication/creating-signatures/
title: Create signatures \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:36.103997+00:00
---

# Create signatures  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/authentication/creating-signatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create signatures Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use the [Google Cloud `signBlob` method](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signBlob) to create a [signature](https://docs.cloud.google.com/storage/docs/authentication/signatures) from a string-to-sign or policy document. Signatures are used as credentials in certains requests, such as [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls). This guide uses RSA keys for creating signatures.

**Important:** The [Google-managed service account keys](https://docs.cloud.google.com/iam/docs/service-account-creds#google-managed-keys) used by the `signBlob` method are rotated regularly. If you set an expiration time for a signature that is greater than 12 hours and generate the signature using the `signBlob` method, the signature is usable for at least 12 hours, but might stop working prior to the expiration time due to key rotation. Signatures generated using the `signBlob` method are best used for short-lived access to resources.

## Before you begin

  1. Enable the Service Account Credentials API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

  2. You must have the `iam.serviceAccounts.signBlob` permission for the service account that you use in this guide. The `iam.serviceAccounts.signBlob` permission is included in the `roles/iam.serviceAccountTokenCreator` role.

  3. The service account that you use in this guide must have permission to perform the request encoded within the signature. For example, if the signature will be used to read object data from a bucket, the service account must have permission to read the object data.




## Create a signature

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "payload": "REQUEST_INFORMATION"
         }

Where:

     * `REQUEST_INFORMATION` is a [string-to-sign](https://docs.cloud.google.com/storage/docs/authentication/signatures#string-to-sign) or a [policy document](https://docs.cloud.google.com/storage/docs/authentication/signatures#policy-document). For both, content must be base64-encoded.
  3. Use [`cURL`](http://curl.haxx.se/) to call the IAM API with a [`signBlob`](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signBlob) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:signBlob"

Where:

     * `JSON_FILE_NAME` is the name of the file you created in Step 2.

     * `SERVICE_ACCOUNT_EMAIL` is the email address of the service account you want to use to create the signature. For example, `example-service-account@my-pet-project.iam.gserviceaccount.com`.

If successful, a _message digest_ is returned in the `signedBlob` field in the response, which is base64 encoded.

  4. To complete the signature, ensure the message digest is base64 decoded, and then hex-encode the message digest.




## What's next

  * See the reference page for signing blobs with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-blob).
  * [Create a signed URL manually](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-manually), using the signature you created.
  * [Create a signed URL with Google Cloud tools](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers).
  * Learn more about [signatures](https://docs.cloud.google.com/storage/docs/authentication/signatures).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
