---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-ca-pool-all-fields/
title: Create a Certificate Authority pool using all fields \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:27.018462+00:00
---

# Create a Certificate Authority pool using all fields  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-ca-pool-all-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Create a Certificate Authority pool using all fields Stay organized with collections  Save and categorize content based on your preferences. 

This sample shows all the possible fields for a Certificate Authority pool. 

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_privateca_ca_pool" "default" {
      name     = "ca-pool-all-fields"
      location = "us-central1"
      tier     = "ENTERPRISE"
      publishing_options {
        publish_ca_cert = false
        publish_crl     = true
      }
      labels = {
        foo = "bar"
      }
      issuance_policy {
        allowed_key_types {
          elliptic_curve {
            signature_algorithm = "ECDSA_P256"
          }
        }
        allowed_key_types {
          rsa {
            min_modulus_size = 5
            max_modulus_size = 10
          }
        }
        maximum_lifetime = "50000s"
        allowed_issuance_modes {
          allow_csr_based_issuance    = true
          allow_config_based_issuance = true
        }
        identity_constraints {
          allow_subject_passthrough           = true
          allow_subject_alt_names_passthrough = true
          cel_expression {
            expression = "subject_alt_names.all(san, san.type == DNS || san.type == EMAIL )"
            title      = "My title"
          }
        }
        baseline_values {
          aia_ocsp_servers = ["example.com"]
          additional_extensions {
            critical = true
            value    = "asdf"
            object_id {
              object_id_path = [1, 7]
            }
          }
          policy_ids {
            object_id_path = [1, 5]
          }
          policy_ids {
            object_id_path = [1, 5, 7]
          }
          ca_options {
            is_ca                  = true
            max_issuer_path_length = 10
          }
          key_usage {
            base_key_usage {
              digital_signature  = true
              content_commitment = true
              key_encipherment   = false
              data_encipherment  = true
              key_agreement      = true
              cert_sign          = false
              crl_sign           = true
              decipher_only      = true
            }
            extended_key_usage {
              server_auth      = true
              client_auth      = false
              email_protection = true
              code_signing     = true
              time_stamping    = true
            }
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
