---
url: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates/
title: Configure Workload Identity Federation with X.509 certificates \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:53.920235+00:00
---

# Configure Workload Identity Federation with X.509 certificates  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure Workload Identity Federation with X.509 certificates Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to use Workload Identity Federation with X.509 certificates that are issued by your certificate authority (CA) to authenticate to Google Cloud and access Google Cloud resources.

If your workloads possess an mTLS client certificate, you can authenticate to Google Cloud by registering one or more CAs with Workload Identity Federation as trust anchors. You can also register intermediate CAs.

By using Workload Identity Federation, you can let these workloads obtain short-lived Google Cloud credentials through a mutual TLS (mTLS) connection. Workloads can use these short-lived credentials to access Google Cloud APIs.

## Concepts

The X.509 certificate-based federation concepts include the following:

  * A _trust anchor_ is a CA certificate that is considered as the root of trust. Any client certificate chains should be chained up to one of the trust anchors.

  * An _intermediate CA_ is an optional CA certificate that helps build the client certificate chain.

  * A _trust store_ contains the trust anchor certificates and intermediate CA certificates that are used to validate the client certificate chain. A CA issues trusted certificates for the client.

You can upload the following types of client certificates to the trust store:

    * Certificates issued by third-party CAs of your choice
    * Certificates issued by your private CAs
    * Signed certificates, as described in Create self-signed certificates



## Before you begin

To start configuring Workload Identity Federation, do the following:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

We recommend that you [ use a dedicated project to manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#dedicated-project). 
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the IAM, Resource Manager, Service Account Credentials, and Security Token Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com,iamcredentials.googleapis.com,sts.googleapis.com&redirect=https%3A//console.cloud.google.com)




## Required roles

To get the permissions that you need to configure Workload Identity Federation, ask your administrator to grant you the following IAM roles on the project: 

  * [Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the IAM Owner (`roles/owner`) basic role also includes permissions to configure identity federation. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Create a trust store

This section shows you how to create a trust store. At a high level, the steps are as follows:

  * Generate self-signed certificates
  * Format the certificates
  * Create the trust store



### Generate self-signed certificates

This section shows you how to generate keys and create signed certificates. If you have already created certificates, you can skip this section and continue with Format the certificates.

This section uses `openssl` commands to create root and intermediate certificates.

To generate a root certificate and a signed intermediate certificate with valid `keyUsage` and `extendedKeyUsage` fields, do the following:

  1. Create an `openssl` configuration file to create your signing certificates. At minimum, the file is similar to the following, but you can set additional fields as needed.
         
         cat > example.cnf << EOF
         [req]
         distinguished_name = empty_distinguished_name
         [empty_distinguished_name]
         # Kept empty to allow setting via -subj command-line argument.
         [ca_exts]
         basicConstraints=critical,CA:TRUE
         keyUsage=keyCertSign
         extendedKeyUsage=clientAuth
         [leaf_exts]
         keyUsage=critical,Digital Signature, Key Encipherment
         basicConstraints=critical, CA:FALSE
         EOF
         

  2. Create the root certificate.
         
         openssl req -x509 \
             -new -sha256 -newkey rsa:2048 -nodes \
             -days 3650 -subj '/CN=root' \
             -config example.cnf \
             -extensions ca_exts \
             -keyout root.key -out root.cert
         

  3. Create the signing request for the intermediate certificate.
         
         openssl req \
             -new -sha256 -newkey rsa:2048 -nodes \
             -subj '/CN=int' \
             -config example.cnf \
             -extensions ca_exts \
             -keyout int.key -out int.req
         

  4. Create the intermediate certificate.
         
         openssl x509 -req \
             -CAkey root.key -CA root.cert \
             -set_serial 1 \
             -days 3650 \
             -extfile example.cnf \
             -extensions ca_exts \
             -in int.req -out int.cert
         

  5. Create the signing request for leaf certificate.
         
         openssl req -new -sha256 -newkey rsa:2048 -nodes \
             -subj '/CN=example' \
             -config example.cnf \
             -extensions leaf_exts \
             -keyout leaf.key -out leaf.req
         

  6. Create the leaf certificate issued by the intermediate.
         
         openssl x509 -req \
             -CAkey int.key -CA int.cert \
             -set_serial 1 -days 1 \
             -extfile example.cnf \
             -extensions leaf_exts \
             -in leaf.req -out leaf.cert
         




### Format the certificates

To include new or existing certificates in a trust store, format the certificates into a one-line string, and store them in environment variables. The certificates must be PEM formatted. To format the certificates and store them in environment variables, do the following:

  1. Save the root certificate as a one-line string.
         
         export ROOT_CERT=$(cat root.cert | sed 's/^[ ]*//g' | sed -z '$ s/\n$//' | tr '\n' $ | sed 's/\$/\\n/g')
         

  2. Save an intermediate certificate as a one-line string.
         
         export INTERMEDIATE_CERT=$(cat int.cert | sed 's/^[ ]*//g' | sed -z '$ s/\n$//' | tr '\n' $ | sed 's/\$/\\n/g')
         




### Create the trust store

In this section, you create a trust store using a YAML-formatted file that contains your trust anchors and intermediate CAs.

This file contains the certificate content from the environment variables that you created in Format the certificates. To add additional trust anchors, add additional `trustAnchors` entries under `trustStore`. To add additional intermediate CA certificates, add additional `intermediateCas` entries under `trustStore`.

To create the trust store file, run the following command:
    
    
    cat << EOF > trust_store.yaml
    trustStore:
      trustAnchors:
      - pemCertificate: "${ROOT_CERT}"
      intermediateCas:
      - pemCertificate: "${INTERMEDIATE_CERT}"
    EOF
    

## Define an attribute mapping and condition

The client X.509 certificate can contain multiple attributes. You must select which attribute you want to use as the subject identifier by mapping `google.subject` in Google Cloud to the attribute from your certificate. For example, if the attribute in the certificate is the subject common name, then the mapping would be as follows: `google.subject=assertion.subject.dn.cn`

Optionally, you can [map additional attributes](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping). You can then refer to these attributes when granting access to resources.

Your attribute mappings can use the attributes within the client certificate, including the following:

  * `serialNumberHex`: the serial number
  * `subject.dn.cn`: the subject common name
  * `subject.dn.o`: the subject organization name
  * `subject.dn.ou`: the subject last organization unit
  * `issuer.dn.cn`: the issuer common name
  * `issuer.dn.o`: the issuer organization name
  * `issuer.dn.ou`: the issuer last organization unit
  * `san.dns`: the subject alternative name's first DNS name
  * `san.uri`: the subject alternative name's first URI
  * `sha256Fingerprint`: SHA256 leaf certificate hash (Base64)



You must map one of these attributes to `google.subject` to uniquely identify the subject. To protect against spoofing threats, choose an attribute with a unique value that can't be changed. By default, the `google.subject` identifier is set to the client certificate subject common name, `assertion.subject.dn.cn`.

Optionally, you can define an [attribute condition](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions). Attribute conditions are CEL expressions that can check assertion attributes and target attributes. If the attribute condition evaluates to `true` for a given credential, the credential is accepted. Otherwise, the credential is rejected.

**Warning:** Although you can grant access to all of the identities in a workload identity pool, doing so can incur risk, especially when the trust anchors contain a well-known public root CA. We recommend that you limit access using [attribute condition](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions).

You can use an attribute condition to restrict which subjects can use Workload Identity Federation to obtain short-lived Google Cloud tokens.

For example, the following condition restricts access to client certificates containing SPIFFE ID `spiffe://example/path`:
    
    
    assertion.san.uri=="spiffe://example/path"
    

## Configure Workload Identity Federation

This section shows you how to configure a workload identity pool and a workload identity pool provider. You need only perform these steps once for each trust store. You can then use the same workload identity pool and provider for multiple workloads and across multiple Google Cloud projects.

### Create the workload identity pool and provider

###  Console 

  1. In the Google Cloud console, go to the **New workload provider and pool** page.

[Go to New workload provider and pool](https://console.cloud.google.com/iam-admin/workload-identity-pools/create)

  2. In the **Create an identity pool** section, enter the following:

     * **Name** : Name for the pool. The name is also used as the pool ID. You can't change the pool ID later.
     * **Description** : Text that describes the purpose of the pool.
  3. Click **Continue**.

  4. In the **Add a provider to pool** section, do the following:

     1. In **Select a provider** , select **X509**.
     2. In **Provider name** , enter a name for the provider. The name is also used as the provider ID. You can't change the provider ID after the provider is created.
     3. In **Trust anchors** , enter your trusted CA certificates in PEM format. These are used to validate the client certificate chain.
     4. Optional: In **Intermediate certificates** , enter any intermediate CA certificates in PEM format to help build the full trust chain.
     5. Click **Continue**.
  5. In the **Configure provider attributes** section, add the attribute mappings and conditions that you've identified previously.

  6. Click **Save**.




###  gcloud 

  1. To create a new workload identity pool, execute the following command:
         
         gcloud iam workload-identity-pools create POOL_ID \
             --location="global" \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"
         

Replace the following:

     * `POOL_ID`: The unique ID for the pool.
     * `DISPLAY_NAME`: The name of the pool.
     * `DESCRIPTION`: A description of the pool that you choose. This description appears when you grant access to pool identities.
  2. To add an X.509 workload identity pool provider, run the following command:
         
         gcloud iam workload-identity-pools providers create-x509 PROVIDER_ID \
             --location=global \
             --workload-identity-pool="POOL_ID" \
             --trust-store-config-path="TRUST_STORE_CONFIG" \
             --attribute-mapping="MAPPINGS" \
             --attribute-condition="CONDITIONS"
         

Replace the following:

     * `PROVIDER_ID`: A unique workload identity pool provider ID of your choice.
     * `POOL_ID`: The workload identity pool ID that you created earlier.
     * `TRUST_STORE_CONFIG`: The trust store YAML file.
     * `MAPPINGS`: A comma-separated list of attribute mappings that you created earlier in this document. For example, `google.subject=assertion.subject.dn.cn`.
     * `CONDITIONS`: Optional. An attribute condition that you created earlier in this document. Remove the parameter if you don't have an attribute condition.



## Configure Context-Aware Access Policy Enforcement for Workload Identity Federation

You can strengthen resource security against token replay attacks by [enabling Context-Aware Access](https://docs.cloud.google.com/chrome-enterprise-premium/docs/configure_cba_for_workloads), which enforces mTLS validation for access requests. In this process, an mTLS binding incorporates policies based on the transport context and uses the state of the client's certificate within the TLS session to make authorization decisions. For X.509 workload identity federation, an mTLS binding ensures that the entire authentication flow is securely tied to a trusted workload. This mitigates the risk of credential theft, because the authentication is bound to a specific, trusted endpoint.

## Authenticate a workload

You must perform these steps once for each workload.

### Allow your external workload to access Google Cloud resources

To provide your workload with access to Google Cloud resources, we recommend that you grant direct resource access to the principal. In this case, the principal is the federated user. Some Google Cloud products have [Google Cloud API limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services). If your workload calls an API endpoint that has a limitation, you can instead use service account impersonation. In this case, the principal is the Google Cloud service account, which acts as the identity. You grant access to the service account on the resource.

### Direct resource access

You can grant access to a federated identity directly on resources by using the Google Cloud console or the gcloud CLI.

### Console

To use the Google Cloud console to grant IAM roles directly on a resource, you must go to the resource's page, and then grant the role. The following example shows you how to go to the Cloud Storage page and grant the role Storage Object Viewer (`roles/storage.objectViewer`) to a federated identity directly on a Cloud Storage bucket.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to grant the role.

  3. Select the **Permissions** tab near the top of the page.

  4. Click the _add_box_ **Grant access** button.

The **Add principals** dialog appears.

  5. In the **New principals** field, enter one or more identities that need access to your bucket.

###  By subject 
         
         principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
         

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `POOL_ID`: the workload pool ID
     * `SUBJECT`: the individual subject mapped from your IdP—for example, `administrator@example.com`

###  By group 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP
    

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_POOL_ID`: the workload pool ID
     * `GROUP`: the group mapped from your IdP—for example: `administrator-group@example.com`

###  By attribute 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE
    

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_POOL_ID`: the workload pool ID
     * `ATTRIBUTE_NAME`: one of the attributes that was mapped from your IdP
     * `ATTRIBUTE_VALUE`: the value of the attribute

  6. Select a role (or roles) from the **Select a role** drop-down menu. The roles you select appear in the pane with a short description of the permissions they grant.

  7. Click **Save**.




###  gcloud 

To use the gcloud CLI to grant IAM roles on a resource in a project, do the following:

  1. Obtain the project number of the project in which the resource is defined.
         
         gcloud projects describe $(gcloud config get-value core/project) --format=value\(projectNumber\)
         

  2. Grant access to the resource.

To use the gcloud CLI to grant the role Storage Object Viewer (`roles/storage.objectViewer`) to external identities that meet certain criteria, run the following command. 

### By subject
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT"

### By group
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP"

### By attribute
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE"

Replace the following:

     * `BUCKET_ID`: the bucket on which to grant access
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). of the project that contains the workload identity pool
     * `POOL_ID`: the pool ID of the workload identity pool
     * `SUBJECT`: the expected value for the attribute that you've mapped to `google.subject`
     * `GROUP`: the expected value for the attribute that you've mapped to `google.groups`
     * `ATTRIBUTE_NAME`: the name of a custom attribute in your attribute mapping
     * `ATTRIBUTE_VALUE`: the value of the custom attribute in your attribute mapping

You can grant roles on any Google Cloud resource that supports IAM allow policies.

**Note:** You must use the project number, not the project ID, in the member identifier.



### Service account impersonation

  1. To create a service account for the external workload, do the following:

     1. Enable the IAM, Security Token Service, and Service Account Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,sts.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

     2. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that represents the workload. We recommend that you [use a dedicated service account for each workload](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#use-dedicated-service-accounts). The service account doesn't need to be in the same project as the workload identity pool, but you must refer to the project that contains the service account.

     3. [Grant the service account access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to resources that you want external identities to access.

  2. To let the federated identity impersonate the service account, do the following:




### Console

To use the Google Cloud console to grant IAM roles to a federated identity with service account, do the following:

### Service Account in the same project

  1. To grant access using service account impersonation for a service account in the same project, do the following:

     1. Go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)

     2. Select **Grant access**.

     3. In the **Grant access to service account** dialog, select **Grant access using Service Account impersonation**.

     4. In the **Service accounts** list, select the service account for the external identities to impersonate, and do the following:

     5. To choose which identities in the pool can impersonate the service account, perform one of the following actions:

        * To allow only specific identities of the workload identity pool to impersonate the service account, select **Only identities matching the filter**.

        * In the **Attribute name** list, select the attribute that you want to filter on.

        * In the **Attribute value** field, enter the expected value of the attribute; for example, if you use an attribute mapping `google.subject=assertion.sub`, set **Attribute** name to `subject` and **Attribute value** to the value of the `sub` claim in tokens that are issued by your external identity provider.

     6. To save the configuration, click **Save** and then **Dismiss**.




### Service account in a different project

**Note:** Service accounts from different projects won't appear in the "CONNECTED SERVICE ACCOUNTS" section of your **Workload Identity Pool**.

  1. To grant access using service account impersonation for a service account in a different project, do the following:

     1. Go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select the service account that you want to impersonate.

     3. Click **Manage access**.

     4. Click **Add principal**.

     5. In the **New principal** field, enter one of the following [principal identifiers](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types) for the identities in your pool that will impersonate the service account.

###  By subject 
            
            principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
            

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `POOL_ID`: the workload pool ID
        * `SUBJECT`: the individual subject mapped from your IdP—for example, `administrator@example.com`

###  By group 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID
        * `GROUP`: the group mapped from your IdP—for example: `administrator-group@example.com`

###  By attribute 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID
        * `ATTRIBUTE_NAME`: one of the attributes that was mapped from your IdP
        * `ATTRIBUTE_VALUE`: the value of the attribute

### By pool
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID

     6. In **Select a role** , select the Workload Identity User role (`roles/iam.workloadIdentityUser`).

     7. To save the configuration, click **Save**.




### gcloud

To grant the Workload Identity User role (`roles/iam.workloadIdentityUser`) to a federated principal or principal set, run the following command. To learn more about Workload Identity Federation principal identifiers, see [Principal types](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types). 

### By subject
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT"

### By group
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP"

### By attribute
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE"

Replace the following:

  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account
  * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). of the project that contains the workload identity pool
  * `POOL_ID`: the pool ID of the workload identity pool
  * `SUBJECT`: the expected value for the attribute that you've mapped to `google.subject`
  * `GROUP`: the expected value for the attribute that you've mapped to `google.groups`
  * `ATTRIBUTE_NAME`: the name of a custom attribute in your attribute mapping
  * `ATTRIBUTE_VALUE`: the value of the custom attribute in your attribute mapping

**Note:** You must use the project number, not the project ID, in the member identifier.

### Download or create a credential configuration

The [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) and the gcloud CLI can automatically obtain external credentials and use these credentials to impersonate a service account. To let libraries and tools complete this process, you must provide a credential configuration file.

Additionally, for X.509 certificate federation, a certificate configuration file is required.

The configuration files include the following:

  * **Credential Configuration** : A JSON file that defines how the client library interacts with the Security Token Service (STS).
  * **Certificate Configuration** : A JSON file that specifies the local paths for the client certificate and private key on your workload.

**Note:** Unlike a [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys), a credential configuration file doesn't contain a private key and doesn't need to be kept confidential. For the credential configuration file details, see [AIP-4117: External Account Credentials (Workload Identity Federation)](https://google.aip.dev/auth/4117).

Create credential and certificate configuration files that let the library obtain access tokens using X.509 certificates.

###  Direct resource access 

To create credential and certificate configuration files for direct resource access, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools/)

  2. Click the name of the pool that contains the provider you want to use.

  3. Click **add_box Grant access**.

  4. In the **Grant access to service account** panel, select **Grant access using federated identities (Recommended)**.

  5. Click **Download config**.

  6. In the **Configure your application** section, select the provider that contains the external identities and provide the following settings:

     * **Client certificate path** : The local path to your client certificate file.
     * **Client private key path** : The local path to your client private key file.
     * **Trust chain path** : (Optional) The path of the trust chain file that contains the client certificate and any intermediate certificates that are required for certificate lookup but are not configured in the X.509 provider.
  7. To download a ZIP archive containing the **Credential Configuration** and **Certificate Configuration** files, click **Download config**.

  8. Click **Dismiss**.




If you want to use the Security Token Service regional endpoints—for example, `https://sts.us-central1.rep.mtls.googleapis.com`, see [Using regional Security Token Service endpoints for better reliability](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints).

###  gcloud 

  1. To create credential and certificate configuration files for direct resource access by using [`gcloud iam workload-identity-pools create-cred-config`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config), run the following command:
         
         gcloud iam workload-identity-pools create-cred-config \
           projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID \
             --credential-cert-path=CLIENT_CERT_PATH \
             --credential-cert-private-key-path=CLIENT_PRIVATE_KEY_PATH \
             --credential-cert-trust-chain-path=TRUST_CHAIN_PATH \
             --sts-location=REGION \
             --output-file=FILEPATH.json
         

Replace the following:

     * `PROJECT_NUMBER`: The project number of the project that contains the workload identity pool.
     * `POOL_ID`: The ID of the workload identity pool.
     * `PROVIDER_ID`: The ID of the workload identity pool provider.
     * `CLIENT_CERT_PATH`: The path of the client certificate file.
     * `CLIENT_PRIVATE_KEY_PATH`: The path of the client certificate private key file.
     * `TRUST_CHAIN_PATH`: Optional. The path of the trust chain file that contains the client certificate and any intermediate certificates that are required for certificate lookup but are not configured in the X.509 provider.
     * `REGION`: Optional. Specify the region of the [regional Security Token Service endpoints](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints), if they are available.
     * `FILEPATH`: The file to save the configuration to.

Running this command will also create a certificate configuration file and store it at the default gcloud CLI location:

     * Linux and macOS: `~/.config/gcloud/certificate_config.json`

     * Windows: `%APPDATA%\gcloud\certificate_config.json`




###  Service account impersonation 

To create credential and certificate configuration files with service account impersonation, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools/)

  2. Click the name of the pool that contains the provider you want to use.

  3. Click **add Grant access**.

  4. Select **Grant access using service account impersonation**.

  5. Select the service account that you want to impersonate.

  6. Click **Download config**.

  7. In the **Configure your application** dialog, provide the following settings:

     * **Client certificate path** : The local path to your client certificate file.
     * **Client private key path** : The local path to your client private key file.
     * **Trust chain path** : (Optional) The path of the trust chain file that contains the client certificate and any intermediate certificates that are required for certificate lookup but are not configured in the X.509 provider.
  8. To download a ZIP archive containing the **Credential Configuration** and **Certificate Configuration** files, click **Download config**.

  9. Click **Dismiss**.




If you want to use the Security Token Service regional endpoints—for example, `https://sts.us-central1.rep.mtls.googleapis.com`, see [Using regional Security Token Service endpoints for better reliability](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints).

###  gcloud 

  1. To create credential and certificate configuration files with service account impersonation by using [`gcloud iam workload-identity-pools create-cred-config`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config), run the following command:
         
         gcloud iam workload-identity-pools create-cred-config \
           projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID \
             --service-account=SERVICE_ACCOUNT_EMAIL \
             --service-account-token-lifetime-seconds=SERVICE_ACCOUNT_TOKEN_LIFETIME \
             --credential-cert-path=CLIENT_CERT_PATH \
             --credential-cert-private-key-path=CLIENT_PRIVATE_KEY_PATH \
             --credential-cert-trust-chain-path=TRUST_CHAIN_PATH \
             --sts-location=REGION \
             --output-file=FILEPATH.json
         

Replace the following:

     * `PROJECT_NUMBER`: The project number of the project that contains the workload identity pool.
     * `POOL_ID`: The ID of the workload identity pool.
     * `PROVIDER_ID`: The ID of the workload identity pool provider.
     * `SERVICE_ACCOUNT_EMAIL`: If you use service account impersonation, replace SERVICE_ACCOUNT_EMAIL with the email address of the service account.
     * `SERVICE_ACCOUNT_TOKEN_LIFETIME`: The lifetime of the service account access token, in seconds, if you use service account impersonation. If omitted, this lifetime defaults to one hour. Omit this flag if you don't use service account impersonation. To specify a lifetime longer than one hour, you must configure the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` [organizational policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).
     * `CLIENT_CERT_PATH`: The path of the client certificate file.
     * `CLIENT_PRIVATE_KEY_PATH`: The path of the client certificate private key file.
     * `TRUST_CHAIN_PATH`: Optional. The path of the trust chain file that contains the client certificate and any intermediate certificates that are required for certificate lookup but are not configured in the X.509 provider.
     * `REGION`: Optional. Specify the region of the [regional Security Token Service endpoints](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints), if they are available.
     * `FILEPATH`: The file to save configuration to.

Running this command will also create a certificate configuration file and store it at the default Google Cloud CLI location:

     * Linux and macOS: `~/.config/gcloud/certificate_config.json`

     * Windows: `%APPDATA%\gcloud\certificate_config.json`




### Use the credential configuration to access Google Cloud

To let tools and client libraries use your credential configuration, do the following. To learn more about Application Default Credentials, see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

  1. If you downloaded a ZIP archive from the Google Cloud console, extract the archive on your external workload.

  2. Update the **Certificate Configuration** file with the actual local file paths for your client certificate and private key for the following fields:

     * `cert_path`: Path to your client certificate.
     * `key_path`: Path to your private key.
  3. Initialize an environment variable `GOOGLE_APPLICATION_CREDENTIALS` and set it to the credential configuration file:

#### Bash
         
         export GOOGLE_APPLICATION_CREDENTIALS=`pwd`/FILEPATH.json
           

Replace `FILEPATH` with the relative path to the credential configuration file. 

#### PowerShell
         
         $env:GOOGLE_APPLICATION_CREDENTIALS = Resolve-Path 'FILEPATH.json'
           

Replace `FILEPATH` with the relative path to the credential configuration file. 

  4. Ensure that the client library can find the certificate configuration file. The certificate configuration file is located at one of the following paths:

     * The path where you extract the ZIP archive. (if you downloaded the configuration from the Google Cloud console).

     * The default gcloud CLI path:

       * Linux and macOS: `~/.config/gcloud/certificate_config.json`

       * Windows: `%APPDATA%\gcloud\certificate_config.json`

     * The path set in the `GOOGLE_API_CERTIFICATE_CONFIG` environment variable.

  5. Use the following Cloud Client Libraries that support Workload Identity Federation with X.509 certificates.

###  Go 

Client libraries for Go support X.509 Workload Identity Federation if they use version 0.16.0 or later of the [`cloud.google.com/go/auth` module](https://pkg.go.dev/cloud.google.com/go/auth) and version 0.189.0 of the [`google.golang.org/api` module](https://pkg.go.dev/google.golang.org/api).

To check which version of these modules your client library uses, run the following command while in the directory containing the go.mod file for your module:
         
         go list -m cloud.google.com/go/auth
           go list -m cloud.google.com/api
         

###  Python

Client libraries for Python support X.509 Workload Identity Federation if they use version 2.39.0 or later of the [`google-auth` package](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth)

To check which version of this package your client library uses, run the following command in the environment where the package is installed:
         
         pip show google-auth
         

To specify a project ID for the authentication client, you can set the `GOOGLE_CLOUD_PROJECT` environment variable, or you can allow the client to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [user guide for the `google-auth` package](https://github.com/googleapis/google-cloud-python/blob/main/packages/google-auth/docs/user-guide.rst#using-external-identities).

  6. If your workload runs on macOS, set `CLOUDSDK_PYTHON_SITEPACKAGES=1` to configure gcloud CLI to use Python libraries outside of its installation directory.

  7. To authenticate using the gcloud CLI, run the following command:
         
         gcloud auth login --cred-file=FILEPATH.json
         

Replace `FILEPATH` with the path to the credential configuration file.

Support for X.509 Workload Identity Federation in gcloud CLI is available in [version 538.0 and later versions of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).




### Obtain an access token using plain request to access Google Cloud

#### Create the trust chain

This step shows you how to create the trust chain. You pass the trust chain in the `subject_token` field when calling Security Token Service in plain request.

Format the certificates that need to be included in the chain as a JSON-formatted list as specified in [RFC 7515](https://www.rfc-editor.org/rfc/rfc7515#section-4.1.6). The leaf certificate used for the mTLS handshake must be specified as the first item. Each certificate in the bundle should be a base64-encoded string.

  1. Save the leaf certificate and the intermediate certificate to base64-encoded strings.
         
         export LEAF_CERT=$(openssl x509 -in leaf.cert -out leaf.der -outform DER && cat leaf.der | openssl enc -base64 -A)
         
         
         export INTERMEDIATE_CERT=$(openssl x509 -in int.cert -out int.der -outform DER && cat int.der | openssl enc -base64 -A)
         

  2. Create a JSON-formatted list of strings that can be passed as `subject_token` in the call to Security Token Service, later in this guide.
         
         export TRUST_CHAIN="[\\\"${LEAF_CERT}\\\", \\\"${INTERMEDIATE_CERT}\\\"]"
         




#### Obtain access token

To obtain the access token, do the following:

  1. Perform token exchange with mTLS and the client certificate:
         
         curl --key CLIENT_CERT_KEY \
         --cert CLIENT_CERT \
         --request POST 'https://sts.mtls.googleapis.com/v1/token' \
         --header "Content-Type: application/json" \
         --data-raw '{
             "subject_token_type": "urn:ietf:params:oauth:token-type:mtls",
             "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
             "audience": "WORKLOAD_IDENTITY_POOL_URI",
             "requested_token_type": "urn:ietf:params:oauth:token-type:access_token",
             "scope": "https://www.googleapis.com/auth/cloud-platform",
             "subject_token": "TRUST_CHAIN"
         }'
         

Replace the following:

     * `CLIENT_CERT_KEY`: The client certificate private key
     * `CLIENT_CERT`: The client certificate
     * `WORKLOAD_IDENTITY_POOL_URI`: The URL of the workload identity pool provider in the following format:

`//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID`

     * `TRUST_CHAIN`: The trust chain needed to verify the leaf certificate, must at least include `CLIENT_CERT` as the first item. If you followed instructions in Format the certificates section, replace `TRUST_CHAIN` with `'"${TRUST_CHAIN}"'`

To use regional Security Token Service endpoints, replace `https://sts.mtls.googleapis.com/v1/token` with the following:
    
    https://sts.REGION.rep.mtls.googleapis.com/v1/token 

Replace `REGION` with a [Google Cloud location](https://cloud.google.com/about/locations), for example, `us-central1` or `europe-west4`.

  2. Optional: If you use service account impersonation, call the [`generateAccessToken` method](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateAccessToken) of the [IAM Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest) with the token from Security Token Service to get an access token.
         
         curl -X POST 'https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:generateAccessToken' \
             -H "Content-Type: application/json; charset=utf-8" \
             -H "Authorization: Bearer STS_TOKEN" \
             -d '{"scope": ["https://www.googleapis.com/auth/cloud-platform"]}'
         

Replace the following:

     * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account.
     * `STS_TOKEN`: The access token generated by the Security Token Service in the previous step.
  3. Use the bearer access token to access Google Cloud resources—for example:
         
         curl -X GET 'https://storage.googleapis.com/my_object' -H "Authorization: Bearer $ACCESS_TOKEN"
         




## Limits

The following table lists limits.

Item | Limit | Notes  
---|---|---  
Number of trust anchors | 3 | Each certificate must not exceed 32 KB.  
Number of intermediate certificates | 10 | Each certificate shouldn't exceed 32 KB.  
Number of name constraints allowed during validation of root and intermediate certificates | 10 |   
Intermediate certificates that share the same Subject and Subject Public Key information | 5 | This limit is for each trust store.  
Certificate chain depth | 5 | The maximum depth for a certificate chain, including the root and client certificates.  
Number of times intermediate certificates can be evaluated when attempting to build the chain of trust | 100 |   
Keys of certificates uploaded and passed from the client | RSA keys can be from 2048 to 4096 bits. ECDSA certificates must use either P-256 or P-384 curves. | RSA-2048 and P-256 are recommended for normal use cases, use others for best security practice.  
Maximum leaf certificate lifetime | 390 days. | Certificates with a validity period that's more than 390 days will stop working after they've been valid for more than 390 days.  
  
## What's next

  * Read more about [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * Learn about [best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).
  * See how you can [manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
