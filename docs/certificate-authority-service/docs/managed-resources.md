---
url: https://docs.cloud.google.com/certificate-authority-service/docs/managed-resources/
title: Configure publication and storage \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:01.785317+00:00
---

# Configure publication and storage  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/managed-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure publication and storage

Certificate Authority Service (CA Service) uses Cloud Storage buckets to publish CA certificates and certificate revocation lists (CRLs) for your public key infrastructure (PKI).

This document describes how to configure the Cloud Storage buckets used by CA Service to publish CA certificates and CRLs for your PKI. You can use a Google-managed bucket or a customer-managed bucket for more direct control. For more information about Cloud Storage buckets, see [About Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets). This document also covers managing publication settings, such as enabling or disabling publication and choosing an encoding format.

## Use a Google-managed bucket

CA Service automatically manages the lifecycle of the Cloud Storage buckets. You aren't billed separately for these resources.

By default, when you create a CA pool, CA Service creates and manages a Cloud Storage bucket with the following characteristics:

  * **Location:** The bucket is in the same project and location as the pool.
  * **Centralized storage:** The bucket stores CA certificates and CRLs for all CAs in the CA pool.
  * **Publicly readable:** Objects are automatically accessible to clients using Authority Information Access (AIA) and CRL Distribution Point (CDP) extensions.



### Advantages of a Google-managed bucket

A Google-managed bucket simplifies management. When you create a CA pool, CA Service automatically creates and manages the bucket for publishing CA certificates and CRLs. You don't need to configure any additional Cloud Storage buckets.

### VPC Service Controls considerations

A [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter restricts access to Google-managed Cloud Storage buckets to clients within that perimeter. AIA and CDP URLs for CA certificates and CRLs are not accessible from outside the perimeter. This lack of accessibility can cause certificate validation failures for clients outside the perimeter.

For information about creating a root CA, see [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca). For information about creating a subordinate CA, see [Create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca). For information about choosing a key algorithm, see [Choose a key algorithm](https://docs.cloud.google.com/certificate-authority-service/docs/choosing-key-algorithm).

## Use a customer-managed bucket

Customer-managed resources are only available for CAs in the [Enterprise tier](https://docs.cloud.google.com/certificate-authority-service/docs/tiers). You must create and configure these resources before creating your CA, and then delete them when you delete the CA. You're billed directly for these resources.

You can specify existing Cloud Storage buckets in your project for publishing CA certificates and CRLs for a CA pool. This provides direct control over the bucket's configuration, including its location, storage class, lifecycle policies, and access controls.

### Advantages of a customer-managed bucket

Using a customer-managed bucket provides direct control over your storage bucket. You can update attributes, such as access management, to meet your organizational requirements.

To create a CA with a customer-managed bucket, you must have administrative access to the bucket to grant the appropriate access to CA Service. For more information, see [CA Service Service Agent](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles#service_agent).

### Location of Cloud Storage buckets

Create customer-managed Cloud Storage buckets in the same location as your CA Service resources.

For example, if your CA is in `us-west1`, you can create the Cloud Storage buckets in any US single region (like `us-west1` or `us-east1`), the `NAM4` dual-region, or the `US` multi-region. For a list of available locations, see [Cloud Storage locations](https://docs.cloud.google.com/storage/docs/locations).

**Caution:** If you delete these resources or remove the [CA Service Service Agent](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles#service_agent) account from the buckets' IAM policies, you might cause CA outages. To configure alerts for these scenarios, see [Create an alerting policy](https://docs.cloud.google.com/certificate-authority-service/docs/monitoring#create_an_alerting_policy).

### Before you begin

  * Ensure that a Cloud Storage bucket exists. See [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

**Note:** For optimal performance and to meet data residency requirements, ensure that the bucket is in the same location as your CA Service CA pool.
  * Ensure the bucket is accessible to the CA Service service account.




#### Required roles

To ensure that the service account has the necessary permissions to write and manage objects (specifically, CA certificates and CRLs) and enable monitoring, ask your administrator to grant the following IAM roles to the service account on the customer-managed Cloud Storage bucket: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To write and manage CA certificates and CRLs: [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) 
  * To allow Cloud Monitoring integration for the bucket: [Storage Legacy Bucket Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Configure the CA to use the bucket

To specify a customer-managed Cloud Storage bucket when you create a certificate authority, use the `--bucket` flag with the `gcloud privateca roots create` or `gcloud privateca subordinates create` commands.

For details on creating CAs, see the following:

  * [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca)
  * [Create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca)



### Manage access to certificates and CRLs

When using a customer-managed bucket, you can control its access permissions. The CA certificates and CRLs published by CA Service inherit the bucket's default object permissions unless you configure them otherwise. To provide public access to the Certificate Authority Information Access (AIA) and CRL Distribution Point (CDP) URLs, make the published objects publicly readable.

By default, CA Service uses HTTP URLs in AIA and CDP extensions for referencing CA certificates and CRLs. Use HTTP URLs for maximum client compatibility. Some clients don't support HTTPS in AIA or CDP extensions. Digital signatures ensure the integrity and authenticity of CA certificates and CRLs.

For more information, see [Overview of access control](https://docs.cloud.google.com/storage/docs/access-control) and [Setting object permissions](https://docs.cloud.google.com/storage/docs/access-control/set-object-permissions) in the Cloud Storage documentation.

## Manage publication settings

By default, when you create a CA pool, CA Service enables CA certificate and CRL publication to Cloud Storage buckets. You can update these publication settings to enable publication, disable publication, or change the encoding format.

### Enable publication for a CA pool

To enable CA certificate and CRL publication for all CAs in a CA pool, do the following:

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Under the **CA pool manager** tab, click the name of the CA pool that you want to edit.

  3. On the **CA pool** page, click mode_edit**Edit**.

  4. Under **Configure allowed key algorithms and sizes** , click **Next**.

  5. Under **Configure accepted certificate request methods** , click **Next**.

  6. Under **Configure publishing options** , click the toggle for **Publish CA certificate to Cloud Storage bucket for CAs in this pool**.

  7. Click the toggle for **Publish CRL to Cloud Storage bucket for CAs in this pool**.




### gcloud

Run the following command:
    
    
    gcloud privateca pools update POOL_ID --location LOCATION --publish-crl --publish-ca-cert
    

Replace the following:

  * `POOL_ID`: the name of the CA pool
  * `LOCATION`: the location of the CA pool. For a list of available locations, see [CA Service locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations)

**Note:** The `--publish-ca-cert` and `--publish-crl` flags are enabled by default. Run the command with `--no-publish-ca-cert` and `--no-publish-crl` to disable them.

For more information about the `gcloud privateca pools update` command, see [gcloud privateca pools update](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/update).

To learn more about enabling CRL publication for revoking certificates, see [Revoking certificates](https://docs.cloud.google.com/certificate-authority-service/docs/revoking-certificates).

### Disable publication for a CA pool

**Note:** Disabling publication doesn't delete the Cloud Storage bucket or its permissions, and it doesn't remove previously hosted CA certificates or CRLs. However, it stops future CRL publication and omits the AIA and CDP extensions from future certificates.

To disable CA certificate and CRL publication for all CAs in a CA pool, do the following:

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Under the **CA pool manager** tab, click the name of the CA pool that you want to edit.

  3. On the **CA pool** page, click mode_edit**Edit**.

  4. Under **Configure allowed key algorithms and sizes** , click **Next**.

  5. Under **Configure accepted certificate request methods** , click **Next**.

  6. Under **Configure publishing options** , click the toggle for **Publish CA certificate to Cloud Storage bucket for CAs in this pool**.

  7. Click the toggle for **Publish CRL to Cloud Storage bucket for CAs in this pool**.




### gcloud

Run the following command:
    
    
    gcloud privateca pools update POOL_ID --location LOCATION --no-publish-crl --no-publish-ca-cert
    

Replace the following:

  * `POOL_ID`: the name of the CA pool
  * `LOCATION`: the location of the CA pool. For a list of available locations, see [CA Service locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations)



### Choose an encoding format

To update the encoding format of published CA certificates and CRLs, do the following:

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Under the **CA pool manager** tab, click the name of the CA pool that you want to edit.

  3. On the **CA pool** page, click mode_edit**Edit**.

  4. Under **Configure allowed key algorithms and sizes** , click **Next**.

  5. Under **Configure accepted certificate request methods** , click **Next**.

  6. Under **Configure publishing options** , click the **Publishing Encoding Format** list.

  7. Select the publishing encoding format.




### gcloud

Run the following command:
    
    
    gcloud privateca pools update POOL_ID --location=LOCATION --publishing-encoding-format=PUBLISHING_ENCODING_FORMAT
    

Replace the following:

  * `POOL_ID`: the name of the CA pool

  * `LOCATION`: the location of the CA pool. For a list of available locations, see [CA Service locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations)

  * `PUBLISHING_ENCODING_FORMAT`: the encoding format can be `PEM` or `DER`

For more information about the `gcloud privateca pools update` command, see [gcloud privateca pools update](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/update).




## What's next

  * Learn how to [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).
  * Learn how to [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca).
  * Learn how to [Create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca).
  * Learn how to [Create a subordinate CA from an external CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-sub-ca-from-external-ca).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
