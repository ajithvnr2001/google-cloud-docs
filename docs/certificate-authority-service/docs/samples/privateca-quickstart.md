---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-quickstart/
title: Quickstart \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:28.980750+00:00
---

# Quickstart  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates a certificate authority (CA) pool, creates a CA in the new CA pool, generates a new Certificate Signing Request (CSR) and uses the generated CSR to request a certificate from the new CA pool.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Issue a certificate using Terraform](https://docs.cloud.google.com/certificate-authority-service/docs/using-terraform)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    provider "google" {}
    provider "tls" {}
    
    resource "google_project_service" "privateca_api" {
      service            = "privateca.googleapis.com"
      disable_on_destroy = false
    }
    
    # Root CaPool & CA
    
    resource "google_privateca_ca_pool" "root" {
      name     = "root-pool"
      location = "us-central1"
      tier     = "ENTERPRISE"
      publishing_options {
        publish_ca_cert = true
        publish_crl     = true
      }
    }
    
    resource "google_privateca_certificate_authority" "root-ca" {
      certificate_authority_id = "my-root-ca"
      location                 = "us-central1"
      pool                     = google_privateca_ca_pool.root.name
      config {
        subject_config {
          subject {
            organization = "google"
            common_name  = "my-certificate-authority"
          }
        }
        x509_config {
          ca_options {
            is_ca = true
          }
          key_usage {
            base_key_usage {
              cert_sign = true
              crl_sign  = true
            }
            extended_key_usage {
              server_auth = true
            }
          }
        }
      }
      type = "SELF_SIGNED"
      key_spec {
        algorithm = "RSA_PKCS1_4096_SHA256"
      }
    
      // Disable CA deletion related safe checks for easier cleanup.
      deletion_protection                    = false
      skip_grace_period                      = true
      ignore_active_certificates_on_deletion = true
    }
    
    # Sub CaPool & CA
    
    resource "google_privateca_ca_pool" "subordinate" {
      name     = "sub-pool"
      location = "us-central1"
      tier     = "ENTERPRISE"
      publishing_options {
        publish_ca_cert = true
        publish_crl     = true
      }
    
      issuance_policy {
        baseline_values {
          ca_options {
            is_ca = false
          }
          key_usage {
            base_key_usage {
              digital_signature = true
              key_encipherment  = true
            }
            extended_key_usage {
              server_auth = true
            }
          }
        }
      }
    }
    
    resource "google_privateca_certificate_authority" "sub-ca" {
      pool                     = google_privateca_ca_pool.subordinate.name
      certificate_authority_id = "my-sub-ca"
      location                 = "us-central1"
      subordinate_config {
        certificate_authority = google_privateca_certificate_authority.root-ca.name
      }
      config {
        subject_config {
          subject {
            organization = "HashiCorp"
            common_name  = "my-subordinate-authority"
          }
          subject_alt_name {
            dns_names = ["hashicorp.com"]
          }
        }
        x509_config {
          ca_options {
            is_ca = true
            # Force the sub CA to only issue leaf certs
            max_issuer_path_length = 0
          }
          key_usage {
            base_key_usage {
              cert_sign = true
              crl_sign  = true
            }
            extended_key_usage {
              server_auth = true
            }
          }
        }
      }
      lifetime = "31536000s"
      key_spec {
        algorithm = "RSA_PKCS1_4096_SHA256"
      }
      type = "SUBORDINATE"
    
      // Disable CA deletion related safe checks for easier cleanup.
      deletion_protection                    = false
      skip_grace_period                      = true
      ignore_active_certificates_on_deletion = true
    }
    
    # Leaf cert
    
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
    
    resource "google_privateca_certificate" "default" {
      pool = google_privateca_ca_pool.subordinate.name
      # Explicitly refer the sub-CA so that the certificate creation will wait for the CA creation.
      certificate_authority = google_privateca_certificate_authority.sub-ca.certificate_authority_id
      location              = "us-central1"
      lifetime              = "860s"
      name                  = "my-certificate"
      pem_csr               = tls_cert_request.example.cert_request_pem
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
