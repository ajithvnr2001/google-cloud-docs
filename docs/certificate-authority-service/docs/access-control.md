---
url: https://docs.cloud.google.com/certificate-authority-service/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:15.086670+00:00
---

# Access control with IAM  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access control with IAM

This page describes the IAM roles for Certificate Authority Service.

CA Service uses [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/roles-overview) for access control. With IAM, you control access by defining who (identity) has what access (role) for which resource. IAM roles contain a set of permissions that lets users perform specific actions on Google Cloud resources. By following the principle of least privilege while granting IAM roles, you can protect the integrity of Certificate Authority Service resources and manage the security of the CA pool, and of the overall public key infrastructure (PKI) itself.

To learn how to assign IAM roles to a user or service account, read [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.

## Predefined roles

The following table lists the predefined IAM roles and the permissions associated with each of them:

Role | Permissions | Description  
---|---|---  
CA Service Auditor  
`roles/privateca.auditor` |  `privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.certificateAuthorities.list`  
`privateca.certificateAuthorities.get`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`privateca.certificates.list`  
`privateca.certificates.get`  
`privateca.locations.get`  
`privateca.locations.list`  
`privateca.operations.get`  
`privateca.operations.list`  
`privateca.certificateRevocationLists.list`  
`privateca.certificateRevocationLists.get`  
`privateca.certificateRevocationLists.getIamPolicy`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list` | The CA Service Auditor role has read-only access to all CA Service resources, and can retrieve and list properties of the CA pool, CA, certificates, revocation lists, IAM policies, and projects. We recommend that you assign this role to individuals who are accountable for validating security and operations of the CA pool, and don't have any daily responsibilities assigned to administer the service.   
CA Service Certificate Requester  
`roles/privateca.certificateRequester` |  `privateca.certificates.create` | A CA Service Certificate Requester role can submit certificate requests to a CA pool. We recommend that you grant this role to trusted individuals who are allowed to request certificates.  
  
A user with this role can request arbitrary certificates subject to the issuance policy.  
  
Unlike the CA Service Certificate Manager role, this role does not allow the user to get or list the newly issued certificate, or to get any information about the CA pool.   
CA Service Workload Certificate Requester  
`roles/privateca.workloadCertificateRequester` |  `privateca.certificates.createForSelf` | A CA Service Workload Certificate Requester can request certificates from CA Service with caller's identity.   
CA Service Certificate Manager  
`roles/privateca.certificateManager` | All permissions from `roles/privateca.auditor`, plus:  
`privateca.certificates.create` | A CA Service Certificate Manager can submit certificate issuance requests to a CA pool like the CA Service Certificate Requester. In addition, this role also inherits the permissions of the CA Service Auditor role. We recommend that you assign this role to individuals accountable for creating, tracking, and reviewing certificate requests on a CA pool, such as a manager or a lead engineer.   
CA Service Certificate Template User  
`roles/privateca.templateUser` |  `privateca.certificateTemplates.get`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.use` | A CA Service Certificate Template User can read, list, and use certificate templates.   
CA Service Operation Manager  
`roles/privateca.caManager` | All permissions from `roles/privateca.auditor`, plus:  
`privateca.certificates.update`  
`privateca.caPools.create`  
`privateca.caPools.delete`  
`privateca.caPools.update`  
`privateca.certificateAuthorities.create`  
`privateca.certificateAuthorities.delete`  
`privateca.certificateAuthorities.update`  
`privateca.certificateRevocationLists.update`  
`privateca.certificateTemplates.create`  
`privateca.certificateTemplates.delete`  
`privateca.certificateTemplates.update`  
`privateca.certificates.update`  
`privateca.operations.cancel`  
`privateca.operations.delete`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`storage.buckets.create` | A CA Service Operation Manager can create, update, and delete CA pools and CAs. This role can also revoke certificates and create Cloud Storage buckets. It also includes the same abilities as the CA Service Auditor. In this role, individuals are responsible for configuring and deploying CA pools in the organization, along with configuring the CA pool's issuance policy.  
  
This role does not allow creating certificates. To do that, use the CA Service Certificate Requester, CA Service Certificate Manager, or CA Service Admin roles.   
CA Service Pool Reader  
`roles/privateca.poolReader` | `privateca.caPools.get` | A user with the CA Service Pool Reader role can read CA pools in CA Service.  
CA Service Admin  
`roles/privateca.admin` | All permissions from `roles/privateca.certificateManager`, and `roles/privateca.caManager`, plus:  
  
`privateca.*.setIamPolicy`  
`privateca.caPools.use`  
`privateca.operations.cancel`  
`privateca.operations.delete`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`storage.buckets.create` | The CA Service Admin role inherits permissions from the CA Service Operation Manager and CA Service Certificate Manager roles. This role can perform all actions within CA Service. A CA Service Admin can set IAM policies for the CA pool and create Cloud Storage buckets. We recommend that you rarely assign this role once the service is established. In this role, individuals can perform all aspects of administration including assigning rights to others and managing certificate requests in CA Service. We recommend that you implement a special control and access to this role account to prevent unauthorized access or use.   
  
## CA Service Service Agent role

When providing existing Cloud KMS keys or Cloud Storage buckets, the CA Service Service Agent service account (`service-PROJECT_NUMBER@gcp-sa-privateca.iam.gserviceaccount.com`) must be granted access to the respective resource.

For Cloud KMS, `roles/cloudkms.signerVerifier` is required to use the signing key and read the public key. `roles/viewer` is required to monitor the key for Cloud Monitoring integration.

For Customer-managed encryption keys (CMEK) used for encrypting data at rest, the role `roles/cloudkms.cryptoKeyEncrypterDecrypter` is required. This allows the service agent to encrypt and decrypt data at rest.

For Cloud Storage, `roles/storage.objectAdmin` is required to write the CA certificate and CRLs to a bucket. `roles/storage.legacyBucketReader` is required to monitor the bucket for Cloud Monitoring integration. For more information, see [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

**Note:** When accessing the service through the Google Cloud CLI or Google Cloud console, these roles are automatically bound during CA pool creation.

When accessing the service through the API, execute the following commands.

  1. Create a service account with the Service Agent role.

### gcloud
         
         gcloud beta services identity create --service=privateca.googleapis.com --project=PROJECT_ID
         

Where:

     * PROJECT_ID is the unique identifier of the project where the CA pool is created.

  2. Grant your service account the required roles by using the following `gcloud` command.

If existing Cloud KMS keys are provided:

### gcloud

For Cloud KMS signing keys:
         
         gcloud kms keys add-iam-policy-binding 'KEY_NAME' \
             --keyring='KEYRING_NAME' \
             --location='LOCATION' \
             --member='serviceAccount:service-PROJECT_NUMBER@gcp-sa-privateca.iam.gserviceaccount.com' \
             --role='roles/cloudkms.signerVerifier'
         
         
         gcloud kms keys add-iam-policy-binding 'KEY_NAME' \
             --keyring='KEYRING_NAME' \
             --location='LOCATION' \
             --member='serviceAccount:service-PROJECT_NUMBER@gcp-sa-privateca.iam.gserviceaccount.com' \
             --role='roles/viewer'
         

For Cloud KMS encryption keys:
         
         gcloud kms keys add-iam-policy-binding 'KEY_NAME' \
             --keyring='KEYRING_NAME' \
             --location='LOCATION' \
             --member='serviceAccount:service-PROJECT_NUMBER@gcp-sa-privateca.iam.gserviceaccount.com' \
             --role='roles/cloudkms.cryptoKeyEncrypterDecrypter'
         

Where:

     * 'KEY_NAME' is the name of your key.
     * 'KEYRING_NAME' is the name of your key ring.
     * 'LOCATION' is the Cloud KMS location where you created your key ring.
     * 'PROJECT_NUMBER' is project number of the Google Cloud project that contains the key.
  3. Grant your service account `roles/storage.objectAdmin` and `roles/storage.legacyBucketReader` roles by using the following `gcloud` command.

If existing Cloud Storage buckets are provided:

### gcloud
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
           --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-privateca.iam.gserviceaccount.com \
           --role=roles/storage.objectAdmin
         

Where:

     * BUCKET_NAME is the name of your Cloud Storage bucket.
     * PROJECT_NUMBER is the unique identifier of your service account.
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
      --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-privateca.iam.gserviceaccount.com \
      --role=roles/storage.legacyBucketReader
    




## API permissions

The following table lists the permissions that the caller must have to call each method in the CA Service API:

Permission | Description  
---|---  
`privateca.caPools.create` | Create a certificate authority (CA) pool.  
`privateca.caPools.update` | Update a CA pool.  
`privateca.caPools.list` | List CA pools in a project.  
`privateca.caPools.get` | Retrieve a CA pool.  
`privateca.caPools.delete` | Delete a CA pool.  
`privateca.caPools.use` | Use a CA Pool.  
`privateca.caPools.getIamPolicy` | Retrieve the IAM policy of the CA pool.  
`privateca.caPools.setIamPolicy` | Set an IAM policy for the CA pool.  
`privateca.certificateAuthorities.create` | Create a CA.  
`privateca.certificateAuthorities.delete` | Schedule a CA for deletion.  
`privateca.certificateAuthorities.get` | Get a CA or CA certificate signing request.  
`privateca.certificateAuthorities.list` | List CAs in a project.  
`privateca.certificateAuthorities.update` | Update a CA, including activating, enabling, disabling, and restoring the CA.  
`privateca.certificates.create` | Request certificates from CA Service.  
`privateca.certificates.createForSelf` | Request certificates from CA Service with caller's identity.  
`privateca.certificates.get` | Get a certificate and its metadata.  
`privateca.certificates.list` | List all certificates in a CA.  
`privateca.certificates.update` | Update a certificate's metadata, including revocation.  
`privateca.certificateRevocationLists.get` | Get a certificate revocation list (CRL) in a CA.  
`privateca.certificateRevocationLists.getIamPolicy` | Get the IAM policy for a CRL.  
`privateca.certificateRevocationLists.list` | List all CRLs in a CA.  
`privateca.certificateRevocationLists.setIamPolicy` | Set the IAM policy for a CRL.  
`privateca.certificateRevocationLists.update` | Update a CRL.  
`privateca.certificateTemplates.create` | Create a certificate template.  
`privateca.certificateTemplates.get` | Retrieve a certificate template.  
`privateca.certificateTemplates.list` | List all certificate templates.  
`privateca.certificateTemplates.update` | Update a certificate template.  
`privateca.certificateTemplates.delete` | Delete a certificate template.  
`privateca.certificateTemplates.getIamPolicy` | Get IAM policy for a certificate template.  
`privateca.certificateTemplates.setIamPolicy` | Set IAM policy for a certificate template.  
`privateca.certificateTemplates.use` | Use a certificate template.  
`privateca.operations.cancel` | Cancel a long-running operation.  
`privateca.operations.delete` | Delete a long-running operation.  
`privateca.operations.get` | Get a long-running operation.  
`privateca.operations.list` | List long-running operations in a project.  
  
## What's next

  * Learn how [IAM](https://docs.cloud.google.com/iam/docs/overview) centralizes management of permissions and access scopes for Google Cloud resources.
  * Learn how to [configure IAM policies](https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam).
  * Learn more about [Customer-managed encryption keys (CMEK)](https://cloud.google.com/kms/docs/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
