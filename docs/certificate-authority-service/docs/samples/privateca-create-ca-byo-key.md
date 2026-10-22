---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-ca-byo-key/
title: Create a root CA using a self-managed key \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:21.675192+00:00
---

# Create a root CA using a self-managed key  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-ca-byo-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Create a root CA using a self-managed key Stay organized with collections  Save and categorize content based on your preferences. 

This samples creates a root certificate authorities (CAs) using a self-managed key in a CA pool in us-central1 region.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_project_service_identity" "privateca_sa" {
      provider = google-beta
      service  = "privateca.googleapis.com"
    }
    
    resource "google_kms_crypto_key_iam_binding" "privateca_sa_keyuser_signerverifier" {
      crypto_key_id = "projects/keys-project/locations/us-central1/keyRings/key-ring/cryptoKeys/crypto-key"
      role          = "roles/cloudkms.signerVerifier"
    
      members = [
        "serviceAccount:${google_project_service_identity.privateca_sa.email}",
      ]
    }
    
    resource "google_kms_crypto_key_iam_binding" "privateca_sa_keyuser_viewer" {
      crypto_key_id = "projects/keys-project/locations/us-central1/keyRings/key-ring/cryptoKeys/crypto-key"
      role          = "roles/viewer"
      members = [
        "serviceAccount:${google_project_service_identity.privateca_sa.email}",
      ]
    }
    
    resource "google_privateca_certificate_authority" "default" {
      // This example assumes this pool already exists.
      // Pools cannot be deleted in normal test circumstances, so we depend on static pools
      pool                     = "ca-pool"
      certificate_authority_id = "my-certificate-authority"
      location                 = "us-central1"
      deletion_protection      = false # set to true to prevent destruction of the resource
      key_spec {
        cloud_kms_key_version = "projects/keys-project/locations/us-central1/keyRings/key-ring/cryptoKeys/crypto-key/cryptoKeyVersions/1"
      }
    
      config {
        subject_config {
          subject {
            organization = "Example, Org."
            common_name  = "Example Authority"
          }
        }
        x509_config {
          ca_options {
            # is_ca *MUST* be true for certificate authorities
            is_ca                  = true
            max_issuer_path_length = 10
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
    
      depends_on = [
        google_kms_crypto_key_iam_binding.privateca_sa_keyuser_signerverifier,
        google_kms_crypto_key_iam_binding.privateca_sa_keyuser_viewer,
      ]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
