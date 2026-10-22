---
url: https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam/
title: Configure IAM policies \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:47.146938+00:00
---

# Configure IAM policies  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure IAM policies

This page describes how to configure Identity and Access Management (IAM) policies that let members create and manage Certificate Authority Service resources. For more information about IAM, see [Overview for IAM](https://docs.cloud.google.com/iam/docs/overview).

### General IAM policies

In CA Service, you grant IAM roles to users or service accounts for creating and managing CA Service resources. You can add these role bindings at the following levels:

  * CA pool level to manage access for a specific CA pool and for the CAs in that CA pool.
  * Project level or organization level to grant access to all CA pools in that scope.



Roles are inherited, if granted at a higher resource level. For example, a user who is granted the Auditor (`roles/privateca.auditor`) role at the project level is able to view all resources under the project. IAM policies that are set on a certificate authority (CA) pool are inherited by all the CAs in that CA pool.

IAM roles can't be granted on certificates and CA resources.

### Conditional IAM policies

If you have a shared CA pool that might be used by multiple users who are authorized to request different types of certificates, you can define IAM conditions to enforce attribute-based access to perform certain operations on a CA pool.

IAM conditional role bindings let you grant access to principals only if specified conditions are met. For example, if the [Certificate Requester](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles#predefined_roles) role is bound to the user `alice@example.com` on a CA pool with the condition that the requested DNS SANs are a subset of `['alice@example.com', 'bob@example.com']`, then that user is able to request certificates from the same CA pool only if the requested SAN is one of those two allowed values. You can set conditions on IAM bindings using Common Expression Language (CEL) expressions. These conditions can help you further restrict the type of certificates a user is able to request. For information about using CEL expressions for IAM conditions, see [Common Expression Language (CEL) dialect for IAM policies](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel#iam-policies).

## Before you begin

  * Enable the API.
  * Create a CA and CA pool by following the instructions in any one of the quickstarts.
  * Read about the [IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control) roles available for Certificate Authority Service.



## Configuring IAM policy bindings at the project level

The following scenarios describe how you can grant users access to CA Service resources at the project level.

### Managing resources

A CA Service Admin (`roles/privateca.admin`) has the permissions to manage all CA Service resources, and set IAM policies on CA pools and certificate templates.

**Note:** We recommend that you assign the CA Service Admin (`roles/privateca.admin`) role selectively, and implement a special access control for this role to prevent unauthorized access or use.

To assign the CA Service Admin (`roles/privateca.admin`) role to a user at the project level, use the following instructions:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to Identity and Access Management](https://console.cloud.google.com/iam-admin/iam)

  2. Select the project.

  3. Click person_add **Grant access**.

  4. In the **New principals** field, enter the principal's email address or other identifier.

  5. In the **Select a role** list, select the **CA Service Admin** role.

  6. Click **Save**.




### gcloud
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=MEMBER \
      --role=roles/privateca.admin
    

Replace the following:

  * PROJECT_ID: the unique identifier of the project
  * MEMBER: the user or service account that you want to assign the CA Service Admin role to



The `--role` flag specifies the IAM role that you want to assign to the member.

### Creating resources

A CA Service Operation Manager (`roles/privateca.caManager`) can create, update, and delete CA pools and CAs. This role also allows the caller to revoke certificates issued by the CAs in the CA pool.

To assign the CA Service Operation Manager (`roles/privateca.caManager`) role to a user at the project level, use the following instructions:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to Identity and Access Management](https://console.cloud.google.com/iam-admin/iam)

  2. Select the project.

  3. Click person_add **Grant access**.

  4. In the **New principals** field, enter the principal's email address or other identifier.

  5. In the **Select a role** list, select the **CA Service Operation Manager** role.

  6. Click **Save**.




### gcloud
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=MEMBER \
      --role=roles/privateca.caManager
    

Replace the following:

  * PROJECT_ID: the unique identifier of the project
  * MEMBER: the user or service account that you want to add the IAM role for



The `--role` flag specifies the IAM role that you want to assign to the member.

For more information about the `gcloud projects add-iam-policy-binding` command, see [gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).

Optionally, creating a CA using an existing Cloud KMS key also requires the caller to be an administrator for the Cloud KMS key.

The Cloud KMS Admin (`roles/cloudkms.admin`) has complete access to all Cloud KMS resources, except the encrypt and decrypt operations. For more information about IAM roles for Cloud KMS, see [Cloud KMS: Permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).

To grant the Cloud KMS Admin (`roles/cloudkms.admin`) role to a user, use the following instructions:

### Console

  1. In the Google Cloud console, go to the **Cloud Key Management Service** page.

[Go to Cloud Key Management Service](https://console.cloud.google.com/security/kms)

  2. Under **Key rings** , click the key ring that contains the CA signing key.

  3. Click the key that is the CA signing key.

  4. If the info panel is not visible, click **Show info panel**. Then, click **Permissions**.

  5. Click person_add **Add principal**.

  6. In the **New principals** field, enter the principal's email address or other identifier.

  7. In the **Select a role** list, select the **Cloud KMS Admin** role.

  8. Click **Save**.




### gcloud
    
    
    gcloud kms keys add-iam-policy-binding KEY \
      --keyring=KEYRING --location=LOCATION \
      --member=MEMBER \
      --role=roles/cloudkms.admin
    

Replace the following:

  * KEY: the unique identifier of the key
  * KEYRING: the key ring that contains the key. For more information about key rings, see [Key rings](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_rings).
  * MEMBER: the user or service account that you want to add the IAM binding for



The `--role` flag specifies the IAM role that you want to assign to the member.

For more information about the `gcloud kms keys add-iam-policy-binding` command, see [gcloud kms keys add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding).

### Auditing resources

A CA Service Auditor (`roles/privateca.auditor`) has read access to all resources in CA Service. When granted for a specific CA pool, it grants read access to the CA pool. If the CA pool is in the Enterprise tier, the user with this role can also view certificates and CRLs issued by the CAs in the CA pool. Assign this role to individuals who are accountable for validating security and operations of the CA pool.

To assign the CA Service Auditor (`roles/privateca.auditor`) role to a user at the project level, use the following instructions:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to Identity and Access Management](https://console.cloud.google.com/iam-admin/iam)

  2. Select the project.

  3. Click person_add **Grant access**.

  4. In the **New principals** field, enter the principal's email address or other identifier.

  5. In the **Select a role** list, select the **CA Service Auditor** role.

  6. Click **Save**.




### gcloud
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=MEMBER \
      --role=roles/privateca.auditor
    

Replace the following:

  * PROJECT_ID: the unique identifier of the project
  * MEMBER: the unique identifier of the user that you want to assign the CA Service Auditor (`roles/privateca.auditor`) role to



The `--role` flag specifies the IAM role that you want to assign to the member.

## Configuring IAM policy bindings at the resource level

This section describes how you can configure IAM policy bindings for a particular resource in CA Service.

### Managing CA pools

You can grant the CA Service Admin (`roles/privateca.admin`) role at the resource level to manage a specific CA pool or certificate template.

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **CA pool manager** tab, and then select the CA pool that you want to grant permissions for.

  3. If the info panel is not visible, click **Show info panel**. Then, click **Permissions**.

  4. Click person_add **Add principal**.

  5. In the **New principals** field, enter the principal's email address or other identifier.

  6. In the **Select a role** list, select the **CA Service Admin** role.

  7. Click **Save**. The principal is granted the selected role on the CA pool resource.




### gcloud

To set the IAM policy, run the following command:
    
    
    gcloud privateca pools add-iam-policy-binding POOL_ID \
      --location LOCATION \
      --member MEMBER \
      --role roles/privateca.admin
    

Replace the following:

  * POOL_ID: the unique identifier of the CA pool that you want to set the IAM policy for
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * MEMBER: the user or service account to which you want to assign the IAM role



The `--role` flag specifies the IAM role that you want to assign to the member.

For more information about the `gcloud privateca pools add-iam-policy-binding` command, see [gcloud privateca pools add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/add-iam-policy-binding).

Follow the same steps to grant the **CA Service Admin** role on a certificate template.

You can also grant the CA Service Operation Manager (`roles/privateca.caManager`) role on a specific CA pool. This role allows the caller to revoke certificates issued by CAs in that CA pool.

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **CA pool manager** tab, and then select the CA pool that you want to grant permissions for.

  3. If the info panel is not visible, click **Show info panel**. Then, click **Permissions**.

  4. Click person_add **Add principal**.

  5. In the **New principals** field, enter the principal's email address or other identifier.

  6. In the **Select a role** list, select the **CA Service Operation Manager** role.

  7. Click **Save**. The principal is granted the selected role on the CA pool resource that the CA belongs to.




### gcloud

To grant the role for a specific CA pool, run the following `gcloud` command:
    
    
    gcloud privateca pools add-iam-policy-binding POOL_ID \
      --location LOCATION \
      --member MEMBER \
      --role roles/privateca.caManager
    

Replace the following:

  * POOL_ID: the unique identifier of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * MEMBER: the unique identifier of the user that you want to assign the CA Service Operation Manager (`roles/privateca.caManager`) role to



The `--role` flag specifies the IAM role that you want to assign to the member.

For more information about the `gcloud privateca pools add-iam-policy-binding` command, see [gcloud privateca pools add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/add-iam-policy-binding).

### Creating certificates

Grant the CA Service Certificate Manager (`roles/privateca.certificateManager`) role to users to let them submit certificate issuance requests to a CA pool. This role also gives read access to CA Service resources. To only allow certificate creation without read access, grant the CA Service Certificate Requester (`roles/privateca.certificateRequester`) role. For more information about IAM roles for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).

To grant the user access to create certificates for a specific CA, use the following instructions.

**Caution:** We recommend that you grant the CA Service Certificate Manager role selectively on a CA pool. If there is a CA in the CA pool that permits issuing CA certificates, it might allow the caller to create their own subordinate CA certificates that chain up to that CA. For more information about certificate issuance policy, see [templates and issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template).

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click **CA pool manager** , and then select the CA pool that you want to grant permissions for.

  3. If the info panel is not visible, click **Show info panel**. Then, click **Permissions**.

  4. Click person_add **Add principal**.

  5. In the **New principals** field, enter the principal's email address or other identifier.

  6. In the **Select a role** list, select the **CA Service Certificate Manager** role.

  7. Click **Save**. The principal is granted the selected role on the CA pool resource that the CA belongs to.




### gcloud
    
    
    gcloud privateca pools add-iam-policy-binding 'POOL_ID' \
      --location LOCATION \
      --member MEMBER \
      --role roles/privateca.certificateManager
    

Replace the following:

  * POOL_ID: the unique identifier of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * MEMBER: the unique identifier of the user that you want to assign the CA Service Certificate Manager (`roles/privateca.certificateManager`) role to



The `--role` flag specifies the IAM role that you want to assign to the member.

### Adding IAM policy bindings to a certificate template

To add an IAM policy on a particular certificate template, use the following instructions:

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **Template manager** tab, and then select the certificate template that you want to grant permissions for.

  3. If the info panel is not visible, click **Show info panel**. Then, click **Permissions**.

  4. Click person_add **Add principal**.

  5. In the **New principals** field, enter the principal's email address or other identifier.

  6. Select a role to grant from the **Select a role** drop-down list.

  7. Click **Save**.




### gcloud
    
    
    gcloud privateca templates add-iam-policy-binding TEMPLATE_ID \
      --location=LOCATION \
      --member=MEMBER \
      --role=ROLE
    

Replace the following:

  * LOCATION: the location of the certificate template. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * MEMBER: the user or service account that you want to add the IAM policy binding for
  * ROLE: the role that you want to grant to the member



For more information about the `gcloud privateca templates add-iam-policy-binding` command, see [gcloud privateca templates add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/add-iam-policy-binding).

For more information about modifying a user's IAM role, see [Granting access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-gcloud-manual).

## Removing IAM policy bindings

You can remove an existing IAM policy binding using the Google Cloud CLI `remove-iam-policy-binding` command.

To remove an IAM policy on a particular CA pool, use the following `gcloud` command:

### gcloud
    
    
    gcloud privateca pools remove-iam-policy-binding POOL_ID \
      --location=LOCATION \
      --member=MEMBER \
      --role=ROLE
    

Replace the following:

  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * MEMBER: the user or service account that you want to remove the IAM policy binding for
  * ROLE: the role that you want to remove for the member



For more information about the `gcloud privateca pools remove-iam-policy-binding` command, see [gcloud privateca pools remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/remove-iam-policy-binding).

To remove an IAM policy on a particular certificate template, use the following `gcloud` command:

### gcloud
    
    
    gcloud privateca templates remove-iam-policy-binding TEMPLATE_ID \
      --location=LOCATION \
      --member=MEMBER \
      --role=ROLE
    

Replace the following:

  * LOCATION: the location of the certificate template. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * MEMBER: the user or service account that you want to remove the IAM policy binding for
  * ROLE: the role that you want to remove for the member



For more information about the `gcloud privateca templates remove-iam-policy-binding` command, see [gcloud privateca templates remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/remove-iam-policy-binding).

For more information about removing a user's IAM role, see [Revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-gcloud-manual).

## What's next

  * Review the [IAM roles for CA Service, and their associated permissions](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
  * Learn about [templates and issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).
  * Learn how to [manage policy controls](https://docs.cloud.google.com/tutorials/manage-policy-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
