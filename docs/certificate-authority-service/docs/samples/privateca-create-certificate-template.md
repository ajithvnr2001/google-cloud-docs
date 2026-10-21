---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-certificate-template/
title: Create a Certificate template \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:55:11.900005+00:00
---

# Create a Certificate template  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-certificate-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Create a Certificate template Stay organized with collections  Save and categorize content based on your preferences. 

Create a Certificate template that can be reused for common certificate issuance scenarios.

## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html);
    import com.google.cloud.security.privateca.v1.[CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate.html);
    import com.google.cloud.security.privateca.v1.[CreateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateTemplateRequest.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).[ExtendedKeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.ExtendedKeyUsageOptions.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).[KeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.html);
    import com.google.cloud.security.privateca.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.LocationName.html);
    import com.google.cloud.security.privateca.v1.[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html);
    import com.google.cloud.security.privateca.v1.[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html).[CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import com.google.type.[Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateCertificateTemplate {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* TODO(developer): Replace these variables before running the sample.
        location: For a list of locations, see:
        https://cloud.google.com/certificate-authority-service/docs/locations */
        String project = "your-project-id";
        String location = "ca-location";
        String certificateTemplateId = "certificate-template-id";
    
        createCertificateTemplate(project, location, certificateTemplateId);
      }
    
      /* Creates a Certificate template. These templates can be reused for common
      certificate issuance scenarios. */
      public static void createCertificateTemplate(
          String project, String location, String certificateTemplateId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
        once, and can be reused for multiple requests. After completing all of your requests, call
        the `certificateAuthorityServiceClient.close()` method on the client to safely
        clean up any remaining background resources. */
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          /* Describes any predefined X.509 values set by this template.
          The provided extensions are copied over to certificate requests that use this template.*/
          [KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html) keyUsage =
              [KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).newBuilder()
                  .[setBaseKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_Builder_setBaseKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_)(
                      [KeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.html).newBuilder()
                          .[setDigitalSignature](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setDigitalSignature_boolean_)(true)
                          .[setKeyEncipherment](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setKeyEncipherment_boolean_)(true)
                          .build())
                  .[setExtendedKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_Builder_setExtendedKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_ExtendedKeyUsageOptions_)([ExtendedKeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.ExtendedKeyUsageOptions.html).newBuilder().[setServerAuth](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.ExtendedKeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_ExtendedKeyUsageOptions_Builder_setServerAuth_boolean_)(true).build())
                  .build();
    
          [CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html) caOptions = [CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html).newBuilder().[setIsCa](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_CaOptions_Builder_setIsCa_boolean_)(false).build();
    
          /* CEL expression that is evaluated against the Subject and
          Subject Alternative Name of the certificate before it is issued. */
          [Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html) expr =
              [Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html).newBuilder().[setExpression](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.Builder.html#com_google_type_Expr_Builder_setExpression_java_lang_String_)("subject_alt_names.all(san, san.type == DNS)").build();
    
          // Set the certificate issuance schema.
          [CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate.html) certificateTemplate =
              [CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate.html).newBuilder()
                  .[setPredefinedValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate.Builder.html#com_google_cloud_security_privateca_v1_CertificateTemplate_Builder_setPredefinedValues_com_google_cloud_security_privateca_v1_X509Parameters_)(
                      [X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html).newBuilder().[setKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_Builder_setKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_)(keyUsage).[setCaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_Builder_setCaOptions_com_google_cloud_security_privateca_v1_X509Parameters_CaOptions_)(caOptions).build())
                  .setIdentityConstraints(
                      [CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html).newBuilder()
                          .[setCelExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setCelExpression_com_google_type_Expr_)(expr)
                          .[setAllowSubjectPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setAllowSubjectPassthrough_boolean_)(false)
                          .[setAllowSubjectAltNamesPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setAllowSubjectAltNamesPassthrough_boolean_)(false)
                          .build())
                  .build();
    
          // Set the parent and certificate template properties.
          [CreateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateTemplateRequest.html) certificateTemplateRequest =
              [CreateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateTemplateRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.LocationName.html).of(project, location).toString())
                  .setCertificateTemplate(certificateTemplate)
                  .[setCertificateTemplateId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateTemplateRequest.Builder.html#com_google_cloud_security_privateca_v1_CreateCertificateTemplateRequest_Builder_setCertificateTemplateId_java_lang_String_)(certificateTemplateId)
                  .build();
    
          // Create Template request.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[createCertificateTemplateCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_createCertificateTemplateCallable__)()
                  .futureCall(certificateTemplateRequest);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get(60, TimeUnit.SECONDS);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error creating certificate template ! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          System.out.println("Successfully created certificate template ! " + response.[getName](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getName__)());
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    from google.type import expr_pb2
    
    
    def create_certificate_template(
        project_id: str,
        location: str,
        certificate_template_id: str,
    ) -> None:
        """
        Create a Certificate template. These templates can be reused for common
        certificate issuance scenarios.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            certificate_template_id: set a unique name for the certificate template.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        # Describes any predefined X.509 values set by this template.
        # The provided extensions are copied over to certificate requests that use this template.
        x509_parameters = privateca_v1.X509Parameters(
            key_usage=privateca_v1.KeyUsage(
                base_key_usage=privateca_v1.KeyUsage.KeyUsageOptions(
                    digital_signature=True,
                    key_encipherment=True,
                ),
                extended_key_usage=privateca_v1.KeyUsage.ExtendedKeyUsageOptions(
                    server_auth=True,
                ),
            ),
            ca_options=privateca_v1.X509Parameters.CaOptions(
                is_ca=False,
            ),
        )
    
        # CEL expression that is evaluated against the Subject and
        # Subject Alternative Name of the certificate before it is issued.
        expr = expr_pb2.Expr(expression="subject_alt_names.all(san, san.type == DNS)")
    
        # Set the certificate issuance schema.
        certificate_template = privateca_v1.CertificateTemplate(
            predefined_values=x509_parameters,
            identity_constraints=privateca_v1.CertificateIdentityConstraints(
                cel_expression=expr,
                allow_subject_passthrough=False,
                allow_subject_alt_names_passthrough=False,
            ),
        )
    
        # Request to create a certificate template.
        request = privateca_v1.CreateCertificateTemplateRequest(
            parent=caServiceClient.common_location_path(project_id, location),
            certificate_template=certificate_template,
            certificate_template_id=certificate_template_id,
        )
        operation = caServiceClient.create_certificate_template(request=request)
        result = operation.result()
    
        print("Operation result:", result)
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
