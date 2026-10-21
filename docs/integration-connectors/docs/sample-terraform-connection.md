---
url: https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/
title: Sample terraform template for connection creation \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:59:33.337644+00:00
---

# Sample terraform template for connection creation  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Reference ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sample terraform template for connection creation

The following is a sample terraform template for connection creation.

**Note:** This sample is not specific to any connector. It just shows how a connection creation terraform template looks like. You must repurpose this sample based on the connection that you want to create.
    
    
    resource "google_integration_connectors_connection" "testconnection" {
      name              = "test-connection"
      description       = "tf updated description"
      location          = "us-central1"
      service_account   = "${data.google_project.default.number}-compute@developer.gserviceaccount.com"
      connector_version = "projects/${data.google_project.default.project_id}/locations/global/providers/zendesk/connectors/zendesk/versions/1"
      // These show all the different types of config variables, not necessary that each resource will use everything.
      config_variable {
        key           = "proxy_enabled"
        boolean_value = false
      }
      config_variable {
        key           = "sample_integer_value"
        integer_value = 1
      }
    
      config_variable {
        key = "sample_encryption_key_value"
        encryption_key_value {
          type         = "GOOGLE_MANAGED"
          kms_key_name = "sampleKMSKkey"
        }
      }
    
      config_variable {
        key = "sample_secret_value"
        secret_value {
          secret_version = google_secret_manager_secret_version.default.name
        }
      }
    
      suspended = false
      auth_config {
        // These show all the different types of additional variables, not necessary that each resource will use everything.
        additional_variable {
          key          = "sample_string"
          string_value = "sampleString"
        }
        additional_variable {
          key           = "sample_boolean"
          boolean_value = false
        }
        additional_variable {
          key           = "sample_integer"
          integer_value = 1
        }
        additional_variable {
          key = "sample_secret_value"
          secret_value {
            secret_version = google_secret_manager_secret_version.default.name
          }
        }
        additional_variable {
          key = "sample_encryption_key_value"
          encryption_key_value {
            type         = "GOOGLE_MANAGED"
            kms_key_name = "sampleKMSKkey"
          }
        }
        auth_type = "USER_PASSWORD"
        auth_key  = "sampleAuthKey"
        user_password {
          username = "user@xyz.com"
          password {
            secret_version = google_secret_manager_secret_version.default.name
          }
        }
      }
    
      destination_config {
        key = "url"
        destination {
          host = "https://test.zendesk.com"
          port = 80
        }
      }
      lock_config {
        locked = false
        reason = "Its not locked"
      }
      log_config {
        enabled = true
      }
      node_config {
        min_node_count = 2
        max_node_count = 50
      }
      labels = {
        foo = "bar"
      }
      ssl_config {
        // These show all the different types of additional variables, not necessary that each resource will use everything.
        additional_variable {
          key          = "sample_string"
          string_value = "sampleString"
        }
        additional_variable {
          key           = "sample_boolean"
          boolean_value = false
        }
        additional_variable {
          key           = "sample_integer"
          integer_value = 1
        }
        additional_variable {
          key = "sample_secret_value"
          secret_value {
            secret_version = google_secret_manager_secret_version.default.name
          }
        }
        additional_variable {
          key = "sample_encryption_key_value"
          encryption_key_value {
            type         = "GOOGLE_MANAGED"
            kms_key_name = "sampleKMSKkey"
          }
        }
        client_cert_type = "PEM"
        client_certificate {
          secret_version = google_secret_manager_secret_version.default.name
        }
        client_private_key {
          secret_version = google_secret_manager_secret_version.default.name
        }
        client_private_key_pass {
          secret_version = google_secret_manager_secret_version.default.name
        }
        private_server_certificate {
          secret_version = google_secret_manager_secret_version.default.name
        }
        server_cert_type = "PEM"
        trust_model      = "PRIVATE"
        type             = "TLS"
        use_ssl          = true
      }
    
      eventing_enablement_type = "EVENTING_AND_CONNECTION"
      eventing_config {
        // These show all the different types of additional variables, not necessary that each resource will use everything.
        additional_variable {
          key          = "sample_string"
          string_value = "sampleString"
        }
        additional_variable {
          key           = "sample_boolean"
          boolean_value = false
        }
        additional_variable {
          key           = "sample_integer"
          integer_value = 1
        }
        additional_variable {
          key = "sample_secret_value"
          secret_value {
            secret_version = google_secret_manager_secret_version.default.name
          }
        }
        additional_variable {
          key = "sample_encryption_key_value"
          encryption_key_value {
            type         = "GOOGLE_MANAGED"
            kms_key_name = "sampleKMSKkey"
          }
        }
        registration_destination_config {
          key = "registration_destination_config"
          destination {
            host = "https://test.zendesk.com"
            port = 80
          }
        }
        auth_config {
          auth_type = "USER_PASSWORD"
          auth_key  = "sampleAuthKey"
          user_password {
            username = "user@xyz.com"
            password {
              secret_version = google_secret_manager_secret_version.default.name
            }
          }
          // These show all the different types of additional variables, not necessary that each resource will use everything.
          additional_variable {
            key          = "sample_string"
            string_value = "sampleString"
          }
          additional_variable {
            key           = "sample_boolean"
            boolean_value = false
          }
          additional_variable {
            key           = "sample_integer"
            integer_value = 1
          }
          additional_variable {
            key = "sample_secret_value"
            secret_value {
              secret_version = google_secret_manager_secret_version.default.name
            }
          }
          additional_variable {
            key = "sample_encryption_key_value"
            encryption_key_value {
              type         = "GOOGLE_MANAGED"
              kms_key_name = "sampleKMSKkey"
            }
          }
        }
        enrichment_enabled = true
      }
      depends_on = [google_secret_manager_secret_iam_member.default]
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
