---
url: https://docs.cloud.google.com/certificate-authority-service/docs/issue-certificate-using-template/
title: Request a certificate using a certificate template \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:35.975167+00:00
---

# Request a certificate using a certificate template  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/issue-certificate-using-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request a certificate using a certificate template

This page describes how to request a certificate using a [certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template#certificate-template).

Certificate templates let you implement [fine-grained policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-concepts#ca-service-policy-controls) over your certificate issuance. For example, you can use certificate templates to standardize the issuance of server TLS certificates across CA pools in your organization. Or, you can use certificate templates to apply policies at a more granular level, such as to specific users. This is useful in situations when you need to restrict the kinds of certificates that different individuals can issue. You can also reuse templates for common issuance scenarios.

## Before you begin

  1. [Prepare your environment for CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/prepare-environment).

  2. To get the permissions that you need to issue certificates using a certificate template, ask your administrator to grant you the CA Service Certificate Template User (`roles/privateca.templateUser`) IAM role on the certificate template.

For more information about the predefined IAM roles for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).

For information about granting an IAM role to a principal, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).




## Test certificate issuance

Before using a certificate template to request a signed certificate, we recommend that you verify the certificate template's ability to successfully generate a certificate. Certificate issuance fails when there is a conflict between the CA pool's issuance policies and the certificate template's policies. By testing issuance, you can proactively identify and resolve these conflicts. Note that test certificates are not PEM encoded, they are unsigned, and they incur no charges for generation.

To test certificate issuance using a certificate template, follow these steps:

### Console

  1. Go to the **Certificate Authority Service** page on the Google Cloud console.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **Template Manager** tab.

  3. Click the certificate template that you want to test. The **Template Details** page appears.

  4. To create a test request, click **Create certificate** , and then click **Test certificate issuance**. The certificate request form appears.

  5. Specify the following details that are required to create a certificate request:

     * **Region** : location of the certificate. This must be the same as the CA pool's location.
     * **CA pool** : the CA pool responsible for issuing the certificate.
     * **Certificate template** : the template that you want to use for certificate issuance.
     * **Domain** : the domain name of the site that you want to secure with a SSL or TLS certificate.
  6. Click **Generate certificate**.

  7. After the certificate is created, click **View**. The test or sample certificate is displayed on the same page in a separate panel.

  8. If certificate issuance fails due to conflicts, [resolve the conflicts](https://docs.cloud.google.com/certificate-authority-service/docs/issue-certificate-using-template#resolve-policy-conflicts), and submit the test certificate request again.




## Issue certificates using a certificate template

To issue a signed certificate using a certificate template, do the following:

### Console

  1. Go to the **Certificate Authority Service** page on the Google Cloud console.

[Go to Certificate Authority Service}](https://console.cloud.google.com/security/cas)

  2. Click the **Template Manager** tab.

  3. In the **Certificate templates** page, click the certificate template that you want to use. The **Template details** page appears.

  4. Click **Create certificate**.

  5. Select a region. This region must be the same as the region of the CA pool that you intend to use.

  6. Select the CA pool.

  7. To generate a certificate using a Certificate Signing Request (CSR), see [Request a certificate using CSR](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates#use-csr).

  8. To generate a certificate using an auto-generated key, see [Request certificate using an auto-generated key](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates#auto-generated-key).




**Generate the certificate**

  1. Click **Generate certificate**. If the certificate is generated successfully, a message is displayed.
  2. To see the generated certificate, click **View certificate** , and then click **View**.



**Optional: Download the signed certificate**

  1. To download the PEM-encoded certificate chain, click **Download certificate chain**.
  2. To download the associated PEM-encoded private key, click **Download private key**.



### gcloud

To issue a certificate using a certificate template, add the `--template` flag to the `gcloud privateca certificates create` command in the following format:

`--template=projects/PROJECT_ID/locations/LOCATION/certificateTemplates/CERTIFICATE_TEMPLATE`

Replace CERTIFICATE_TEMPLATE with the name of the certificate template that you want to use for issuing this certificate. The specified template must be in the same location as the issuing CA pool. See the samples provided for [generating test DNS certificates](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/manage-policy-controls#generating-test-dns-certificates) and [generating production certificates](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/manage-policy-controls#generate-prod-certificates) for more information.

### Terraform
    
    
    /**
     * Copyright 2022 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *      http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    resource "google_privateca_certificate_template" "template" {
      location    = "us-central1"
      name        = "my-certificate-template"
      description = "An updated sample certificate template"
    
      identity_constraints {
        allow_subject_alt_names_passthrough = true
        allow_subject_passthrough           = true
    
        cel_expression {
          description = "Always true"
          expression  = "true"
          location    = "any.file.anywhere"
          title       = "Sample expression"
        }
      }
    
      passthrough_extensions {
        additional_extensions {
          object_id_path = [1, 6]
        }
    
        known_extensions = ["EXTENDED_KEY_USAGE"]
      }
    
      predefined_values {
        additional_extensions {
          object_id {
            object_id_path = [1, 6]
          }
    
          value    = "c3RyaW5nCg=="
          critical = true
        }
    
        aia_ocsp_servers = ["string"]
    
        ca_options {
          is_ca                  = false
          max_issuer_path_length = 6
        }
    
        key_usage {
          base_key_usage {
            cert_sign          = false
            content_commitment = true
            crl_sign           = false
            data_encipherment  = true
            decipher_only      = true
            digital_signature  = true
            encipher_only      = true
            key_agreement      = true
            key_encipherment   = true
          }
    
          extended_key_usage {
            client_auth      = true
            code_signing     = true
            email_protection = true
            ocsp_signing     = true
            server_auth      = true
            time_stamping    = true
          }
    
          unknown_extended_key_usages {
            object_id_path = [1, 6]
          }
        }
    
        policy_ids {
          object_id_path = [1, 6]
        }
      }
    }
    
    resource "google_privateca_certificate_authority" "test_ca" {
      pool                     = "my-pool"
      certificate_authority_id = "my-certificate-authority-test-ca"
      location                 = "us-central1"
      deletion_protection      = false # set to true to prevent destruction of the resource
      config {
        subject_config {
          subject {
            organization = "HashiCorp"
            common_name  = "my-certificate-authority"
          }
          subject_alt_name {
            dns_names = ["hashicorp.com"]
          }
        }
        x509_config {
          ca_options {
            # is_ca *MUST* be true for certificate authorities
            is_ca = true
          }
          key_usage {
            base_key_usage {
              # cert_sign and crl_sign *MUST* be true for certificate authorities
              cert_sign = true
              crl_sign  = true
            }
            extended_key_usage {
              server_auth = false
            }
          }
        }
      }
      key_spec {
        algorithm = "RSA_PKCS1_4096_SHA256"
      }
    }
    
    
    resource "google_privateca_certificate" "default" {
      pool                  = "my-pool"
      location              = "us-central1"
      certificate_authority = google_privateca_certificate_authority.test_ca.certificate_authority_id
      lifetime              = "860s"
      name                  = "my-certificate-from-template"
      pem_csr               = tls_cert_request.example.cert_request_pem
      certificate_template  = google_privateca_certificate_template.template.id
    }
    
    resource "tls_private_key" "example" {
      algorithm = "RSA"
    }
    
    resource "tls_cert_request" "example" {
      private_key_pem = tls_private_key.example.private_key_pem
    
      subject {
        common_name  = "example.com"
        organization = "ACME Examples, Inc"
      }
    }
    

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

A certificate request might fail if a [policy conflict](https://docs.cloud.google.com/docs/policy-conflicts) is detected between the CA pool's issuance policy and the certificate template. When this happens, you must [resolve the policy conflict](https://docs.cloud.google.com/docs/policy-conflicts#resolve-policy-conflicts) before you can submit the certificate request again.

### Share a certificate request link

To share a certificate request form link with others in your organization so that they can request a certificate using the same parameters, do the following:

### Console

  1. In the Google Cloud console, go to the **CA pool manager** tab, and click **Share request form link**.
  2. In the **Share request form link** panel that appears, select the CA pool and the certificate template that you chose to create your request. The certificate request link is displayed.
  3. Copy the link and share as required.



**Note:** To create a certificate request using the shared link generated, the requester must have the **CA Service Certificate Manager** and the **CA Service Certificate Template User** role on the project.

### View certificates issued using a template

To view the certificates issued using a certificate template, do the following:

### Console

  1. In the Google Cloud console, go to the **Template Manager** tab.
  2. Click the certificate template that you have used for certificate issuance.
  3. On the **Template Details** page, click **Certificates**. The list of certificates issued using the selected certificate template are displayed.



## What's next

  * Learn how to [view issued certificates](https://docs.cloud.google.com/certificate-authority-service/docs/view-issued-certificates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
