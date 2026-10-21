---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-subordinateca/
title: Create a Subordinate Certificate Authority \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:49.273232+00:00
---

# Create a Subordinate Certificate Authority  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-subordinateca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Create a Subordinate Certificate Authority Stay organized with collections  Save and categorize content based on your preferences. 

Create a subordinate certificate authority from a root or subordinate CA.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a subordinate certificate authority](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca)



## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).[KeyVersionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.KeyVersionSpec.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).[SignHashAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.SignHashAlgorithm.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html);
    import com.google.cloud.security.privateca.v1.[CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html).[SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html);
    import com.google.cloud.security.privateca.v1.[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).[KeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.html);
    import com.google.cloud.security.privateca.v1.[Subject](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.html);
    import com.google.cloud.security.privateca.v1.[SubjectAltNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.SubjectAltNames.html);
    import com.google.cloud.security.privateca.v1.[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html);
    import com.google.cloud.security.privateca.v1.[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html).[CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class CreateSubordinateCa {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Set it to the CA Pool under which the CA should be created.
        // subordinateCaName: Unique name for the Subordinate CA.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String subordinateCaName = "subordinate-certificate-authority-name";
    
        createSubordinateCertificateAuthority(project, location, poolId, subordinateCaName);
      }
    
      public static void createSubordinateCertificateAuthority(
          String project, String location, String poolId, String subordinateCaName)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          String commonName = "commonname";
          String orgName = "csr-org-name";
          String domainName = "dns.example.com";
          int caDuration = 100000; // Validity of this CA in seconds.
    
          // Set the type of Algorithm.
          [KeyVersionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.KeyVersionSpec.html) keyVersionSpec =
              [KeyVersionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.KeyVersionSpec.html).newBuilder().[setAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.KeyVersionSpec.Builder.html#com_google_cloud_security_privateca_v1_CertificateAuthority_KeyVersionSpec_Builder_setAlgorithm_com_google_cloud_security_privateca_v1_CertificateAuthority_SignHashAlgorithm_)([SignHashAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.SignHashAlgorithm.html).RSA_PKCS1_4096_SHA256).build();
    
          // Set CA subject config.
          [SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html) subjectConfig =
              [SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html).newBuilder()
                  .setSubject(
                      [Subject](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.html).newBuilder().[setCommonName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.Builder.html#com_google_cloud_security_privateca_v1_Subject_Builder_setCommonName_java_lang_String_)(commonName).[setOrganization](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.Builder.html#com_google_cloud_security_privateca_v1_Subject_Builder_setOrganization_java_lang_String_)(orgName).build())
                  // Set the fully qualified domain name.
                  .setSubjectAltName([SubjectAltNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.SubjectAltNames.html).newBuilder().[addDnsNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.SubjectAltNames.Builder.html#com_google_cloud_security_privateca_v1_SubjectAltNames_Builder_addDnsNames_java_lang_String_)(domainName).build())
                  .build();
    
          //  Set the key usage options for X.509 fields.
          [X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html) x509Parameters =
              [X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html).newBuilder()
                  .[setKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_Builder_setKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_)(
                      [KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).newBuilder()
                          .[setBaseKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_Builder_setBaseKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_)(
                              [KeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.html).newBuilder().[setCrlSign](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setCrlSign_boolean_)(true).[setCertSign](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setCertSign_boolean_)(true).build())
                          .build())
                  .[setCaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_Builder_setCaOptions_com_google_cloud_security_privateca_v1_X509Parameters_CaOptions_)([CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html).newBuilder().[setIsCa](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_CaOptions_Builder_setIsCa_boolean_)(true).build())
                  .build();
    
          // Set certificate authority settings.
          [CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html) subCertificateAuthority =
              [CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).newBuilder()
                  .setType([CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).Type.SUBORDINATE)
                  .[setKeySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.Builder.html#com_google_cloud_security_privateca_v1_CertificateAuthority_Builder_setKeySpec_com_google_cloud_security_privateca_v1_CertificateAuthority_KeyVersionSpec_)(keyVersionSpec)
                  .setConfig(
                      [CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html).newBuilder()
                          .[setSubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.Builder.html#com_google_cloud_security_privateca_v1_CertificateConfig_Builder_setSubjectConfig_com_google_cloud_security_privateca_v1_CertificateConfig_SubjectConfig_)(subjectConfig)
                          .[setX509Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.Builder.html#com_google_cloud_security_privateca_v1_CertificateConfig_Builder_setX509Config_com_google_cloud_security_privateca_v1_X509Parameters_)(x509Parameters)
                          .build())
                  // Set the CA validity duration.
                  .setLifetime([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(caDuration).build())
                  .build();
    
          // Create the CertificateAuthorityRequest.
          [CreateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest.html) subCertificateAuthorityRequest =
              [CreateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest.html).newBuilder()
                  .setParent([CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html).of(project, location, poolId).toString())
                  .[setCertificateAuthorityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest.Builder.html#com_google_cloud_security_privateca_v1_CreateCertificateAuthorityRequest_Builder_setCertificateAuthorityId_java_lang_String_)(subordinateCaName)
                  .setCertificateAuthority(subCertificateAuthority)
                  .build();
    
          // Create Subordinate CA.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[createCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_createCertificateAuthorityCallable__)()
                  .futureCall(subCertificateAuthorityRequest);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while creating Subordinate CA !" + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          System.out.println(
              "Subordinate Certificate Authority created successfully : " + subordinateCaName);
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    from google.protobuf import duration_pb2
    
    
    def create_subordinate_ca(
        project_id: str,
        location: str,
        ca_pool_name: str,
        subordinate_ca_name: str,
        common_name: str,
        organization: str,
        domain: str,
        ca_duration: int,
    ) -> None:
        """
        Create Certificate Authority (CA) which is the subordinate CA in the given CA Pool.
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: set it to the CA Pool under which the CA should be created.
            subordinate_ca_name: unique name for the Subordinate CA.
            common_name: a title for your certificate authority.
            organization: the name of your company for your certificate authority.
            domain: the name of your company for your certificate authority.
            ca_duration: the validity of the certificate authority in seconds.
        """
    
        ca_service_client = privateca_v1.CertificateAuthorityServiceClient()
    
        # Set the type of Algorithm
        key_version_spec = privateca_v1.CertificateAuthority.KeyVersionSpec(
            algorithm=privateca_v1.CertificateAuthority.SignHashAlgorithm.RSA_PKCS1_4096_SHA256
        )
    
        # Set CA subject config.
        subject_config = privateca_v1.CertificateConfig.SubjectConfig(
            subject=privateca_v1.Subject(
                common_name=common_name, organization=organization
            ),
            # Set the fully qualified domain name.
            subject_alt_name=privateca_v1.SubjectAltNames(dns_names=[domain]),
        )
    
        # Set the key usage options for X.509 fields.
        x509_parameters = privateca_v1.X509Parameters(
            key_usage=privateca_v1.KeyUsage(
                base_key_usage=privateca_v1.KeyUsage.KeyUsageOptions(
                    crl_sign=True,
                    cert_sign=True,
                )
            ),
            ca_options=privateca_v1.X509Parameters.CaOptions(
                is_ca=True,
            ),
        )
    
        # Set certificate authority settings.
        certificate_authority = privateca_v1.CertificateAuthority(
            type_=privateca_v1.CertificateAuthority.Type.SUBORDINATE,
            key_spec=key_version_spec,
            config=privateca_v1.CertificateConfig(
                subject_config=subject_config,
                x509_config=x509_parameters,
            ),
            # Set the CA validity duration.
            lifetime=duration_pb2.Duration(seconds=ca_duration),
        )
    
        ca_pool_path = ca_service_client.ca_pool_path(project_id, location, ca_pool_name)
    
        # Create the CertificateAuthorityRequest.
        request = privateca_v1.CreateCertificateAuthorityRequest(
            parent=ca_pool_path,
            certificate_authority_id=subordinate_ca_name,
            certificate_authority=certificate_authority,
        )
    
        operation = ca_service_client.create_certificate_authority(request=request)
        result = operation.result()
    
        print(f"Operation result: {result}")
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_privateca_certificate_authority" "root_ca" {
      // This example assumes this pool already exists.
      // Pools cannot be deleted in normal test circumstances, so we depend on static pools
      pool                                   = "my-pool"
      certificate_authority_id               = "my-certificate-authority-root"
      location                               = "us-central1"
      deletion_protection                    = false # set to true to prevent destruction of the resource
      ignore_active_certificates_on_deletion = true
      config {
        subject_config {
          subject {
            organization = "ACME"
            common_name  = "my-certificate-authority"
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
            }
          }
        }
      }
      key_spec {
        algorithm = "RSA_PKCS1_4096_SHA256"
      }
      // valid for 10 years
      lifetime = "${10 * 365 * 24 * 3600}s"
    }
    
    resource "google_privateca_certificate_authority" "sub_ca" {
      // This example assumes this pool already exists.
      // Pools cannot be deleted in normal test circumstances, so we depend on static pools
      pool                     = "my-sub-pool"
      certificate_authority_id = "my-certificate-authority-sub"
      location                 = "us-central1"
      deletion_protection      = false # set to true to prevent destruction of the resource
      subordinate_config {
        certificate_authority = google_privateca_certificate_authority.root_ca.name
      }
      config {
        subject_config {
          subject {
            organization = "ACME"
            common_name  = "my-subordinate-authority"
          }
        }
        x509_config {
          ca_options {
            is_ca = true
            # Force the sub CA to only issue leaf certs.
            # Use e.g.
            #    max_issuer_path_length = 1
            # if you need to chain more subordinates.
            zero_max_issuer_path_length = true
          }
          key_usage {
            base_key_usage {
              cert_sign = true
              crl_sign  = true
            }
            extended_key_usage {
            }
          }
        }
      }
      // valid for 5 years
      lifetime = "${5 * 365 * 24 * 3600}s"
      key_spec {
        algorithm = "RSA_PKCS1_2048_SHA256"
      }
      type = "SUBORDINATE"
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
