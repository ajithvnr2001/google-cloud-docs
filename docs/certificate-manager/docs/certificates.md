---
url: https://docs.cloud.google.com/certificate-manager/docs/certificates/
title: Manage certificates \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:00:04.442975+00:00
---

# Manage certificates  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Manage certificates Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Certificate Manager to create and manage Transport Layer Security (TLS) (formerly [SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security#SSL_1.0,_2.0,_and_3.0)) certificates.

For more information, see [Supported TLS certificates](https://docs.cloud.google.com/certificate-manager/docs/overview#supported-certificates).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed. For more information about the gcloud CLI commands used on this page, see the [Certificate Manager CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager).

## Create a Google-managed certificate

Certificate Manager lets you create Google-managed certificates in the following ways:

  * Google-managed certificates with load balancer authorization (global)
  * Google-managed certificates with DNS authorization (global, regional, and cross-region)
  * Google-managed certificates with Certificate Authority Service (CA Service) (global, regional, and cross-region)



### Load balancer authorization

Load balancer authorization lets you obtain a Google-managed certificate for your domain when traffic is served by the load balancer. This method doesn't require any additional DNS records for certificate provisioning. You can use load balancer authorizations for new environments with no existing traffic. For information about when to use load balancer authorization with a Google-managed certificate, see [Domain authorization types for Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization).

You can create Google-managed certificates with load balancer authorization only in the `global` location. Load balancer authorized certificates don't support wildcard domains.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, click **Add Certificate**.

  3. In the **Certificate name** field, enter a unique name for the certificate.

  4. Optional: In the **Description** field, enter a description for the certificate. The description lets you identify the certificate.

  5. For **Location** , select **Global**. 

  6. For **Scope** , select one of the following options:

     * **Default** : if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
     * **Edge cache** : if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.

You can't use load balancer authorization with a **Regional** location or the **All regions** scope. 

  7. For **Certificate type** , select **Create Google-managed certificate**.

  8. For **Certificate Authority type** , select **Public**.

  9. In the **Domain Names** field, specify a comma-delimited list of domain names of the certificate. Each domain name must be a fully qualified domain name, such as `myorg.example.com`.

  10. For **Authorization type** , select **Load balancer authorization**.

  11. In the **Labels** field, specify labels to associate with the certificate. To add a label, click add_box**Add label** , and specify a key and a value for your label.

  12. Click **Create**.

The new certificate appears in the list of certificates.




###  gcloud 

To create a global Google-managed certificate with load balancer authorization, use the [`certificate-manager certificates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create):
    
    
    gcloud certificate-manager certificates create CERTIFICATE_NAME \
        --domains="DOMAIN_NAMES" \
        [--scope=SCOPE]
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DOMAIN_NAMES`: a comma-separated list of the target domains. Each domain name must be a fully qualified domain name, such as `myorg.example.com`.
  * `SCOPE`: enter one of the following options: 
    * `default`: if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
    * `all-regions`: if you plan to use the certificate with cross-region internal Application Load Balancer.
    * `edge-cache`: if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.



###  Terraform 

Use a [`google_certificate_manager_certificate` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate).
    
    
    resource "google_certificate_manager_certificate" "default" {
      name        = "${local.name}-rootcert-${random_id.tf_prefix.hex}"
      description = "Cert with LB authorization"
      managed {
        domains = [local.domain]
      }
      labels = {
        "terraform" : true
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Create the certificate by making a `POST` request to the `certificates.create` method as follows:
    
    
    POST /v1/projects/PROJECT_ID/locations/global/certificates?certificate_id=CERTIFICATE_NAME"
    {
     "managed": {
      "domains": ["DOMAIN_NAME"],
      "scope": "SCOPE" //optional
     }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DOMAIN_NAMES`: a comma-separated list of the target domains. Each domain name must be a fully qualified domain name, such as `myorg.example.com`.
  * `SCOPE`: enter one of the following options: 
    * `default`: if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
    * `all-regions`: if you plan to use the certificate with cross-region internal Application Load Balancer.
    * `edge-cache`: if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.



### DNS authorization

To use Google-managed certificates before your production environment is ready, you can provision them with DNS authorizations. For information about when to use DNS authorization with a Google-managed certificate, see [Domain authorization types for Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization).

To independently manage certificates across multiple projects, you can use per-project DNS authorization. For information about creating certificates with per-project DNS authorization, see [Create a DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations#auth-create).

Before you create the certificate, do the following:

  * [Create a DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations#auth-create) for each of the domain names covered by the certificate.
  * [Add the CNAME record to your DNS configuration](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations#cname-record) for the validation sub-domain in the DNS zone of the target domain.



#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, click **Add Certificate**.

  3. In the **Certificate name** field, enter a unique name for the certificate.

  4. Optional: In the **Description** field, enter a description for the certificate. The description lets you identify the certificate. 

  5. For **Location** , select **Global** or **Regional**.

If you've selected **Regional** , from the **Region** list, select your region.

  6. For **Scope** , select one of the following options:

     * **Default** : if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
     * **All regions** : if you plan to use the certificate with cross-region internal Application Load Balancer.
     * **Edge cache** : if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.

The **Scope** field is not available if you've selected a **Regional** location. 

  7. For **Certificate type** , select **Create Google-managed certificate**.

  8. For **Certificate Authority type** , select **Public**.

  9. In the **Domain Names** field, specify a comma-separated list of domain names of the certificate. Each domain name must be a fully qualified domain name, such as `myorg.example.com`. The domain name can also be a wildcard domain name, such as `*.example.com`.

  10. For **Authorization type** , select **DNS authorization**.

The page lists DNS authorizations of the domain names. If a domain name doesn't have an associated DNS authorization, follow these steps to create one:

     1. Click **Create missing DNS authorization**.
     2. In the **DNS authorization name** field, specify the name of the DNS authorization. The default DNS authorization type is `FIXED_RECORD`. To independently manage certificates across multiple projects, select the **Per project authorization** checkbox. 
     3. Click **Create DNS authorization**.
  11. In the **Labels** field, specify labels to associate to the certificate. To add a label, click add_box**Add label** , and specify a key and a value for your label.

  12. Click **Create**.

The new certificate appears in the list of certificates.




###  gcloud 

To create a Google-managed certificate with DNS authorization, run the [`certificate-manager certificates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create):
    
    
    gcloud certificate-manager certificates create CERTIFICATE_NAME \
        --domains="DOMAIN_NAME, *.DOMAIN_NAME" \
        --dns-authorizations="AUTHORIZATION_NAMES" \
        [--location=LOCATION] \
        [--scope=SCOPE]
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DOMAIN_NAME`: the name of the target domain. The domain name must be a fully qualified domain name, such as `myorg.example.com`, or a wildcard domain, such as `*.myorg.example.com`. The asterisk dot prefix (*.) signifies a wildcard certificate.
  * `AUTHORIZATION_NAMES`: a comma-separated list of the names of DNS authorizations.
  * `LOCATION`: the target Google Cloud location. The default is `global`.
  * `SCOPE`: enter one of the following options: 
    * `default`: if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
    * `all-regions`: if you plan to use the certificate with cross-region internal Application Load Balancer.
    * `edge-cache`: if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.



###  Terraform 

Use a [`google_certificate_manager_certificate` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate).
    
    
    resource "google_certificate_manager_certificate" "root_cert" {
      name        = "${local.name}-rootcert-${random_id.tf_prefix.hex}"
      description = "The wildcard cert"
      managed {
        domains = [local.domain, "*.${local.domain}"]
        dns_authorizations = [
          google_certificate_manager_dns_authorization.default.id
        ]
      }
      labels = {
        "terraform" : true
      }
    }

###  API 

Create the certificate by making a `POST` request to the `certificates. create` method as follows:
    
    
    POST /v1/projects/PROJECT_ID/locations/LOCATION/certificates?certificate_id=CERTIFICATE_NAME
    {
     "managed": {
      "domains": ["DOMAIN_NAME"],
      "issuanceConfig": "ISSUANCE_CONFIG_NAME",
      "scope": "SCOPE" //optional
     }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DOMAIN_NAME`: the name of the target domain. The domain name must be a fully qualified domain name, such as `myorg.example.com`.
  * `ISSUANCE_CONFIG_NAME`: the name of the certificate issuance configuration resource that references the target CA pool.
  * `SCOPE`: enter one of the following options: 
    * `default`: if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
    * `all-regions`: if you plan to use the certificate with cross-region internal Application Load Balancer.
    * `edge-cache`: if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.

**Note:** To specify multiple domains or DNS authorizations, provide a comma-separated list of values in their respective fields.

### Issued by CA Service

You can integrate Certificate Manager with CA Service to issue Google-managed certificates. To issue global Google-managed certificates, you use a regional CA pool in any region. To issue regional Google-managed certificates, you use a CA pool in the same region as your certificate.

Before you create the certificate, [configure CA Service integration with Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas#configure-integration).

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Owner role (`roles/certificatemanager.owner`)
  * CA Service Admin (`roles/privateca.admin`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, click **Add Certificate**.

  3. In the **Certificate name** field, enter a unique name for the certificate.

  4. Optional: In the **Description** field, enter a description for the certificate. The description lets you identify the certificate. 

  5. For **Location** , select **Global** or **Regional**.

If you've selected **Regional** , from the **Region** list, select your region.

  6. For **Scope** , select one of the following options:

     * **Default** : if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
     * **All regions** : if you plan to use the certificate with cross-region internal Application Load Balancer.
     * **Edge cache** : if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.

The **Scope** field is not available if you've selected a **Regional** location. 

  7. For **Certificate type** , select **Create Google-managed certificate**.

  8. For **Certificate Authority type** , select **Private**.

  9. In the **Domain Names** field, specify a comma-delimited list of domain names of the certificate. Each domain name must be a fully qualified domain name, such as `myorg.example.com`.

  10. For **Select a certificate issuance config** , select the name of the certificate issuance configuration resource referencing the target CA pool.

  11. In the **Labels** field, specify labels to associate to the certificate. To add a label, click add_box**Add label** , and specify a key and a value for your label.

  12. Click **Create**.

The new certificate appears in the list of certificates.




###  gcloud 

To create a Google-managed certificate with Certificate Authority Service, use the [`certificate-manager certificates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create):
    
    
    gcloud certificate-manager certificates create CERTIFICATE_NAME \
        --domains="DOMAIN_NAMES" \
        --issuance-config=ISSUANCE_CONFIG_NAME \
        [--location="LOCATION"] \
        [--scope=SCOPE]
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DOMAIN_NAME`: the name of the target domain. The domain name must be a fully qualified domain name, such as `myorg.example.com`, or a wildcard domain, such as `*.myorg.example.com`. The asterisk dot prefix (*.) signifies a wildcard certificate.
  * `ISSUANCE_CONFIG_NAME`: the name of the certificate issuance configuration resource that references the target CA pool.
  * `LOCATION`: the target Google Cloud location. The default is `global`.
  * `SCOPE`: enter one of the following options: 
    * `default`: if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
    * `all-regions`: if you plan to use the certificate with cross-region internal Application Load Balancer.
    * `edge-cache`: if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.



###  API 

Create the certificate by making a `POST` request to the `certificates.create` method as follows:
    
    
    POST /v1/projects/PROJECT_ID/locations/LOCATION/certificates?certificate_id=CERTIFICATE_NAME"
    {
     "managed": {
      "domains": ["DOMAIN_NAME"],
      "issuanceConfig": "ISSUANCE_CONFIG_NAME",
      "scope": "SCOPE" //optional
     }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DOMAIN_NAME`: the name of the target domain. The domain name must be a fully qualified domain name, such as `myorg.example.com`.
  * `ISSUANCE_CONFIG_NAME`: the name of the certificate issuance configuration resource that references the target CA pool.
  * `SCOPE`: enter one of the following options: 
    * `default`: if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
    * `all-regions`: if you plan to use the certificate with cross-region internal Application Load Balancer.
    * `edge-cache`: if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.



## Upload a self-managed certificate

To upload a self-managed certificate, upload the certificate (CRT) file and the corresponding private key (KEY) file. You can upload global and regional X.509 TLS (SSL) certificates of the following types:

  * Certificates generated by third-party certificate authorities (CAs) of your choice.
  * Certificates generated by certificate authorities that you control.
  * Self-signed certificates, as described in [Create a private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert).

**Note:** Certificate Manager doesn't validate the properties of self-managed certificates. Before you upload the certificate, make sure that the uploaded certificate is valid and meets your requirements. For example, make sure that the certificate is properly chained, root-trusted, and hasn't expired.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, click **Add Certificate**.

  3. In the **Certificate name** field, enter a unique name for the certificate.

  4. Optional: In the **Description** field, enter a description for the certificate. The description lets you identify the certificate. 

  5. For **Location** , select **Global** or **Regional**.

If you've selected **Regional** , from the **Region** list, select your region.

  6. For **Scope** , select one of the following options:

     * **Default** : if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
     * **All regions** : if you plan to use the certificate with cross-region internal Application Load Balancer.
     * **Edge cache** : if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.

The **Scope** field is not available if you've selected a **Regional** location. 

  7. For **Certificate type** , select **Create self-managed certificate**.

  8. For the **Certificate** field, do _either_ of the following:

     * Click the **Upload** button and select your PEM-formatted certificate file.
     * Copy and paste the contents of a PEM-formatted certificate. The contents must start with `-----BEGIN CERTIFICATE-----` and end with `-----END CERTIFICATE-----`.
  9. For the **Private key certificate** field, do _either_ of the following:

     * Click the **Upload** button and select your private key. Your private key must be PEM-formatted and not protected with a passphrase.
     * Copy and paste the contents of a PEM-formatted private key. The private keys must start with `-----BEGIN PRIVATE KEY-----` and end with `-----END PRIVATE KEY-----`.
  10. In the **Labels** field, specify labels to associate with the certificate. To add a label, click add_box**Add label** , and specify a key and a value for your label.

  11. Click **Create**.

The new certificate appears in the list of certificates.




###  gcloud 

To create a self-managed certificate, use the [`certificate-manager certificates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create):
    
    
    gcloud certificate-manager certificates create CERTIFICATE_NAME \
        --certificate-file="CERTIFICATE_FILE" \
        --private-key-file="PRIVATE_KEY_FILE" \
        [--location="LOCATION"] \
        [--scope=SCOPE]
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `CERTIFICATE_FILE`: the path and filename of the CRT certificate file.
  * `PRIVATE_KEY_FILE`: the path and filename of the KEY private key file.
  * `LOCATION`: the target Google Cloud location. The default is `global`.
  * `SCOPE`: enter one of the following options: 
    * `default`: if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
    * `all-regions`: if you plan to use the certificate with cross-region internal Application Load Balancer.
    * `edge-cache`: if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.



###  Terraform 

To upload a self-managed certificate, you can use a [`google_certificate_manager_certificate` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate) with the `self_managed` block.

###  API 

Upload the certificate by making a `POST` request to the `certificates.create` method as follows:
    
    
    POST /v1/projects/PROJECT_ID/locations/LOCATION/certificates?certificate_id=CERTIFICATE_NAME
    {
      self_managed: {
        pem_certificate: "PEM_CERTIFICATE",
        pem_private_key: "PEM_KEY",
        scope: SCOPE
      }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `PEM_CERTIFICATE`: the certificate PEM.
  * `PEM_KEY`: the key PEM.
  * `SCOPE`: enter one of the following options: 
    * `default`: if you plan to use the certificate with global external Application Load Balancer or global external proxy Network Load Balancer.
    * `all-regions`: if you plan to use the certificate with cross-region internal Application Load Balancer.
    * `edge-cache`: if you plan to use the certificate with Media CDN and specify multiple domains in the certificate.



## Update a certificate

You can update an existing certificate without modifying its assignments to domain names within the corresponding certificate map. When you update a certificate, make sure that the SANs in the new certificate exactly match the SANs in the existing certificate.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

### Google-managed certificates

For Google-managed certificates, you can update only a certificate's description and labels.

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, locate the certificate that you want to update, and then click the certificate's name. The **Certificate details** page displays detailed information about the selected certificate.

  3. Click **Edit**. The **Edit certificate** page appears.

  4. Optional: In the **Description** field, enter a new description for the certificate.

  5. Optional: You can add, remove, or change the labels associated with the certificate. To add a label, click the add_box**Add label** button, and then specify a `key` and a `value` for your label.

  6. Click **Save**. On the **Certificate details** page that appears, verify that the certificate is updated.




###  gcloud 

To update a Google-managed certificate, use the [`certificate-manager certificates update` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update):
    
    
    gcloud certificate-manager certificates update CERTIFICATE_NAME \
        [--description="DESCRIPTION"] \
        [--update-labels="LABELS"]
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DESCRIPTION`: a unique description of the certificate.
  * `LABELS`: a comma-separated list of labels applied to this certificate.



###  API 

Update the certificate by making a `PATCH` request to the `certificates.patch` method as follows:
    
    
    PATCH /v1/projects/PROJECT_ID/certificates/CERTIFICATE_NAME?updateMask=self_managed,labels,description
    {
      "description": "DESCRIPTION",
      "labels": {
        "LABEL_KEY": "LABEL_VALUE",
      }
    
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DESCRIPTION`: a description of the certificate.
  * `LABEL_KEY`: a label key applied to the certificate.
  * `LABEL_VALUE`: a label value applied to the certificate.



### Self-managed certificates

To update a self-managed certificate, you must upload the following PEM-encoded files:

  * The certificate CRT file
  * The corresponding private key KEY file




###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, locate the certificate that you want to update, and then click the certificate's name. The **Certificate details** page displays detailed information about the selected certificate.

  3. Click **Edit**. The **Edit certificate** page appears.

  4. Optional: In the **Description** field, enter a new description for the certificate.

  5. Optional: For the **Certificate** field, do either _one_ of the following:

     * Click the **Upload** button, and then select your PEM-formatted certificate file.
     * Copy and paste the contents of a PEM-formatted certificate. The contents must start with `-----BEGIN CERTIFICATE-----` and end with `-----END CERTIFICATE-----`.
**Note:** You can edit the **Certificate** field for only self-managed certificates. If you are updating the **Certificate** field, then make sure that you provide the private key in the **Private key certificate** field.
  6. Optional: For the **Private key certificate** field, do any _one_ of the following:

     * Click the **Upload** button, and then select your private key. Your private key must be PEM-formatted and must not be protected with a passphrase.
     * Copy and paste the contents of a PEM-formatted private key. The private keys must start with `-----BEGIN PRIVATE KEY-----` and end with `-----END PRIVATE KEY-----`.
**Note:** You can edit the **Private key certificate** field for only self-managed certificates.
  7. Optional: You can add, remove, or change the labels associated with the certificate. To add a label, click the add_box**Add label** button, and then specify a `key` and a `value` for your label.

  8. Click **Save**. On the **Certificate details** page that appears, verify that the certificate is updated.




###  gcloud 

To update a self-managed certificate, use the [`certificate-manager certificates update`command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/update):
    
    
    gcloud certificate-manager certificates update CERTIFICATE_NAME \
        --certificate-file="CERTIFICATE_FILE" \
        --private-key-file="PRIVATE_KEY_FILE" \
        --description="DESCRIPTION" \
        --update-labels="LABELS" \
        [--location="LOCATION"]
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `CERTIFICATE_FILE`: the path and filename of the CRT certificate file.
  * `PRIVATE_KEY_FILE`: the path and filename of the KEY private key file.
  * `DESCRIPTION`: a unique description value for this certificate.
  * `LABELS`: a comma-separated list of labels applied to this certificate.
  * `LOCATION`: the target Google Cloud location. This flag is optional. Specify this flag for regional certificates only.



###  API 

Update the certificate by making a `PATCH` request to the `certificates.patch` method as follows:
    
    
    PATCH /v1/projects/PROJECT_ID/locations/[LOCATION]/certificates/CERTIFICATE_NAME?updateMask=self_managed,labels,description
    {
       self_managed: { // Self-managed certificates only
        pem_certificate: "PEM_CERTIFICATE",
        pem_private_key: "PEM_KEY",
      }
      "description": "DESCRIPTION",
      "labels": {
        "LABEL_KEY": "LABEL_VALUE",
      }
    
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location. This flag is optional. Specify this flag for regional certificates only.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `PEM_CERTIFICATE`: the certificate PEM.
  * `PEM_KEY`: the key PEM.
  * `DESCRIPTION`: a meaningful description of the certificate.
  * `LABEL_KEY`: a label key applied to the certificate.
  * `LABEL_VALUE`: a label value applied to the certificate.



## List certificates

You can see all certificates in your project and their details, such as region, hostnames, expiration date, and type.

**Note:** By default, Certificate Manager supports environments with fewer than 10,000 provisioned certificates. If your environment exceeds this limit, contact [Support](https://docs.cloud.google.com/certificate-manager/docs/support) to enable certificate listing.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)
  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

The **Certificate Manager** page in the Google Cloud console can display a maximum of 10,000 certificates. If your project contains more than 10,000 certificates that are managed by Certificate Manager, use the gcloud CLI command.

To see certificates provisioned by Certificate Manager:

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. Click the **Certificates** tab. This tab lists all of the certificates managed by Certificate Manager in the selected project.




To see certificates provisioned through Cloud Load Balancing:

  1. In the Google Cloud console, go to the **Classic Certificates** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/lbCertificates)

  2. On the **Classic Certificates** tab, you can view a list of all the configured classic certificates in the selected project.

Classic certificates aren't managed by Certificate Manager. For more information about how to manage them, review the documentation on how to [use Google-managed certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) or [use self-managed certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).




###  gcloud 

To list certificates, use the [`certificate-manager certificates list` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/list):
    
    
    gcloud certificate-manager certificates list \
        [--location="LOCATION"] \
        --filter="FILTER" \
        --page-size="PAGE_SIZE" \
        --limit="LIMIT" \
        --sort-by="SORT_BY"
    

Replace the following:

  * `LOCATION`: the target Google Cloud location. To list certificates from all regions, use `-` as the value. The default is `-`. This flag is optional.
  * `FILTER`: an expression that constrains the returned results to specific values.

For example, you can filter the results by the following criteria:

    * Expiration time: `--filter='expire_time >= "2021-09-01T00:00:00Z"'`
    * SAN DNS names: `--filter='san_dnsnames:"example.com"'`
    * Certificate state: `--filter='managed.state=FAILED'`
    * Certificate type: `--filter='managed:*'`
    * Labels and creation time: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `LIMIT`: maximum number of results that you want to return

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




###  API 

List the certificates by making a `LIST` request to the `certificates.list` method as follows:
    
    
    GET /v1/projects/PROJECT_ID/locations/LOCATION/certificates?filter=FILTER&pageSize=PAGE_SIZE&sortBy=SORT_BY
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location. To list certificates from all regions, use `-` as the value.
  * `FILTER`: an expression that constrains the returned results to specific values.

For example, you can filter the results by the following criteria:

    * Expiration time: `--filter='expire_time >= "2021-09-01T00:00:00Z"'`
    * SAN DNS names: `--filter='san_dnsnames:"example.com"'`
    * Certificate state: `--filter='managed.state=FAILED'`
    * Certificate type: `--filter='managed:*'`
    * Labels and creation time: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




## View the state of a certificate

You can view the state of an existing certificate, including its provisioning state and other detailed information.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)
  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

If your project contains more than 10,000 certificates that are managed by Certificate Manager, the **Certificate Manager** page in the Google Cloud console won't list them. Instead, use the gcloud CLI command. However, if you have a direct link to the certificate's **Details** page, you can view its details in the Google Cloud console.

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the page that appears, select the **Certificates** tab.

  3. On the **Certificates** tab, go to the target certificate, and then click the certificate's name. The **Certificate details** page displays detailed information about the selected certificate.

  4. Optional: To view the REST response from the Certificate Manager API for this certificate, click **Equivalent REST**.

  5. Optional: If the certificate has an associated certificate issuance configuration that you want to view, then in the **Issuance config** field, click the name of the associated certificate issuance configuration resource. The Google Cloud console displays the full configuration of the certificate issuance configuration.




###  gcloud 

To view the status of a certificate, use the [`certificate-manager certificates describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/describe):
    
    
    gcloud certificate-manager certificates describe CERTIFICATE_NAME \
        [--location="LOCATION"]
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `LOCATION`: the target Google Cloud location. The default location is `global`. This flag is optional.



###  API 

View the certificate state by making a `GET` request to the `certificates.get` method as follows:
    
    
    GET /v1/projects/PROJECT_ID/locations/LOCATION/certificates/CERTIFICATE_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location.
  * `CERTIFICATE_NAME`: the name of the certificate.



## Delete a certificate

Before you delete a certificate, remove it from all certificate map entries that reference it; otherwise, the deletion fails. For more information, see [Delete a certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-delete).

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, select the checkbox of the certificate that you want to delete.

  3. Click **Delete**.

  4. In the dialog that appears, click **Delete** to confirm.




###  gcloud 

To delete a certificate, use the [`certificate-manager certificates delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/delete):
    
    
    gcloud certificate-manager certificates delete CERTIFICATE_NAME \
        [--location="LOCATION"]
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `LOCATION`: the target Google Cloud location. The default location is `global`. This flag is optional.



###  API 

Delete the certificate by making a `DELETE` request to the `certificates.delete` method as follows:
    
    
    DELETE /v1/projects/PROJECT_ID/locations/LOCATION/certificates/CERTIFICATE_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location.
  * `CERTIFICATE_NAME`: the name of the certificate.



## What's next

  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries)
  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)
  * [Manage certificate issuance configuration resources](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
