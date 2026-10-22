---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-certificate-config/
title: Create a Certificate using a Certificate Authority \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:42.916079+00:00
---

# Create a Certificate using a Certificate Authority  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-certificate-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Create a Certificate using a Certificate Authority Stay organized with collections  Save and categorize content based on your preferences. 

Use a created Certificate Authority to issue a certificate

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_privateca_certificate_authority" "test_ca" {
      certificate_authority_id               = "my-example-certificate-authority"
      location                               = "us-central1"
      pool                                   = "my-pool"
      ignore_active_certificates_on_deletion = true
      deletion_protection                    = false # set to true to prevent destruction of the resource
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
      key_spec {
        algorithm = "RSA_PKCS1_4096_SHA256"
      }
    }
    
    resource "google_privateca_certificate" "default" {
      pool                  = "my-pool"
      location              = "us-central1"
      certificate_authority = google_privateca_certificate_authority.test_ca.certificate_authority_id
      lifetime              = "860s"
      name                  = "my-example-certificate"
      config {
        subject_config {
          subject {
            common_name         = "san1.example.com"
            country_code        = "us"
            organization        = "google"
            organizational_unit = "enterprise"
            locality            = "mountain view"
            province            = "california"
            street_address      = "1600 amphitheatre parkway"
          }
          subject_alt_name {
            email_addresses = ["email@example.com"]
            ip_addresses    = ["127.0.0.1"]
            uris            = ["http://www.ietf.org/rfc/rfc3986.txt"]
          }
        }
        x509_config {
          ca_options {
            is_ca = false
          }
          key_usage {
            base_key_usage {
              crl_sign      = false
              decipher_only = false
            }
            extended_key_usage {
              server_auth = false
            }
          }
        }
        public_key {
          format = "PEM"
          key    = base64encode(data.tls_public_key.example.public_key_pem)
        }
      }
    }
    
    resource "tls_private_key" "example" {
      algorithm = "RSA"
    }
    
    data "tls_public_key" "example" {
      private_key_pem = tls_private_key.example.private_key_pem
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
