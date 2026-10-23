---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/validate-request-signature/
title: Validate an approved request signature \u00a0|\u00a0 Access Approval \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:15.104147+00:00
---

# Validate an approved request signature  |  Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/validate-request-signature/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Validate an approved request signature

Each approved Access Approval request is signed with an asymmetric cryptographic key to validate the approval. Approved requests can be signed with a Google-owned and managed key or a customer-provided Cloud KMS key.

When you validate a signature, you can be sure that the bytestring of the serialized approved request is valid. To finish validating the contents of the approval, you must deserialize the message and compare the deserialized message with the contents of the approved request.

## Before you begin

To ensure that the Access Approval service account for your resource has the necessary permissions to verify approved request signatures, ask your administrator to grant the [Cloud KMS CryptoKey Signer/Verifier ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.signerVerifier) (`roles/cloudkms.signerVerifier`) IAM role to the Access Approval service account for your resource on the key, key ring, or key project. **Important:** You must grant this role to the Access Approval service account for your resource, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Access Approval service account for your resource the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Validate a request signed using a Google-owned and managed key

  1. In the Google Cloud console, go to the **Access Approval** page.

[Go to Access Approval](https://console.cloud.google.com/security/access-approval)

  2. Locate and select the approved Access Approval request that you want to validate. The **Request details** page opens.

  3. Under **Google-managed public key** , click content_copy **Copy**.

  4. Open the Cloud Shell, and then save the public key as a new file named `public_key`:
         
         echo GOOGLE_MANAGED_PUBLIC_KEY > ./public_key
         

Replace `GOOGLE_MANAGED_PUBLIC_KEY` with the contents of the **Google-managed public key** field.

  5. In the Google Cloud console, on the **Request details** page, under **Signature** , click content_copy **Copy**.

  6. Open the Cloud Shell, and then save the signature as a new file named `signature.txt`:
         
         echo SIGNATURE > ./signature.txt
         

Replace `SIGNATURE` with the contents of the **Signature** field.

  7. Decode the signature using the `base64` command and save the result as `decoded_signature`:
         
         base64 ./signature.txt -d > ./decoded_signature
         

  8. In the Google Cloud console, on the **Request details** page, under **Serialized Approval Request** , click content_copy **Copy**.

  9. Open the Cloud Shell, and then save the serialized approval request as a new file named `serialized_approval_request.txt`:
         
         echo SERIALIZED_APPROVAL_REQUEST > ./serialized_approval_request.txt
         

Replace `SERIALIZED_APPROVAL_REQUEST` with the contents of the **Serialized Approval Request** field.

  10. Decode the serialized approval request and save the result as `decoded_serialized_approval_request`:
         
         base64 ./serialized_approval_request.txt -d > ./decoded_serialized_approval_request
         

  11. Use `openssl` to verify the signature:
         
         openssl dgst \
             -sha256 \
             -verify ./public_key \
             -signature ./decoded_signature \
             ./decoded_serialized_approval_request
         

If the signature is valid, the output should be `Verified OK`. This confirms that the serialized approval request is valid.




## Validate a request signed using a customer-provided key

  1. In the Google Cloud console, go to the **Access Approval** page.

[Go to Access Approval](https://console.cloud.google.com/security/access-approval)

  2. Locate and select the approved Access Approval request that you want to validate. The **Request details** page opens.

  3. In the Google Cloud console, on the **Request details** page, under **Signature** , click content_copy **Copy**.

  4. Open the Cloud Shell, and then save the signature as a new file named `signature.txt`:
         
         echo SIGNATURE > ./signature.txt
         

Replace `SIGNATURE` with the contents of the **Signature** field.

  5. Decode the signature and save the result as `decoded_signature`:
         
         base64 ./signature.txt -d > ./decoded_signature
         

  6. In the Google Cloud console, on the **Request details** page, under **Serialized Approval Request** , click content_copy **Copy**.

  7. Open the Cloud Shell, and then save the serialized approval request as a new file named `serialized_approval_request.txt`:
         
         echo SERIALIZED_APPROVAL_REQUEST > ./serialized_approval_request.txt
         

Replace `SERIALIZED_APPROVAL_REQUEST` with the contents of the **Serialized Approval Request** field.

  8. Decode the serialized approval request and save the result as `decoded_serialized_approval_request`:
         
         base64 ./serialized_approval_request.txt -d > ./decoded_serialized_approval_request
         

  9. Under **Customer-managed key** , make note of the resource identifier of the key.

  10. [Retrieve the public key](https://docs.cloud.google.com/kms/docs/retrieve-public-key) for the key that you identified in the previous step. Save the downloaded public key in the PEM format as `./public_key`.

  11. Use `openssl` to verify the signature:
         
         openssl dgst \
             -sha256 \
             -verify ./public_key \
             -signature ./decoded_signature \
             ./decoded_serialized_approval_request
         

If the signature is valid, the output should be `Verified OK`. This confirms that the serialized approval request is valid.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
