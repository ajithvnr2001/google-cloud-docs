---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-certificate-csr/
title: Create Certificate using Certificate Signing Request \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:21.934189+00:00
---

# Create Certificate using Certificate Signing Request  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-certificate-csr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Create Certificate using Certificate Signing Request Stay organized with collections  Save and categorize content based on your preferences. 

Issue certificate by the specified certificate authority using a CSR.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Request a certificate](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates)



## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html);
    import com.google.cloud.security.privateca.v1.[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CreateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class CreateCertificateCsr {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
    
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Set a unique id for the CA pool.
        // certificateAuthorityName: The name of the certificate authority to sign the CSR.
        // certificateName: Set a unique name for the certificate.
        // pemCsr: Set the Certificate Issuing Request in the pem encoded format.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateAuthorityName = "certificate-authority-name";
        String certificateName = "certificate-name";
        String pemCsr =
            "-----BEGIN CERTIFICATE REQUEST-----\n"
                + "sample-pem-csr-format\n"
                + "-----END CERTIFICATE REQUEST-----";
    
        createCertificateWithCsr(
            project, location, poolId, certificateAuthorityName, certificateName, pemCsr);
      }
    
      // Create a Certificate which is issued by the specified Certificate Authority.
      // The certificate details and the public key is provided as a CSR (Certificate Signing Request).
      public static void createCertificateWithCsr(
          String project,
          String location,
          String poolId,
          String certificateAuthorityName,
          String certificateName,
          String pemCsr)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
          // certificateLifetime: The validity of the certificate in seconds.
          long certificateLifetime = 1000L;
    
          // Create certificate with CSR.
          // The pemCSR contains the public key and the domain details required.
          [Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html) certificate =
              [Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html).newBuilder()
                  .setPemCsr(pemCsr)
                  .setLifetime([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(certificateLifetime).build())
                  .build();
    
          // Create the Certificate Request.
          // Set the CA which is responsible for creating the certificate with the provided CSR.
          [CreateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.html) certificateRequest =
              [CreateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.html).newBuilder()
                  .setParent([CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html).of(project, location, poolId).toString())
                  .[setIssuingCertificateAuthorityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.Builder.html#com_google_cloud_security_privateca_v1_CreateCertificateRequest_Builder_setIssuingCertificateAuthorityId_java_lang_String_)(certificateAuthorityName)
                  .[setCertificateId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.Builder.html#com_google_cloud_security_privateca_v1_CreateCertificateRequest_Builder_setCertificateId_java_lang_String_)(certificateName)
                  .setCertificate(certificate)
                  .build();
    
          // Get the certificate response.
          ApiFuture<Certificate> future =
              certificateAuthorityServiceClient
                  .[createCertificateCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_createCertificateCallable__)()
                  .futureCall(certificateRequest);
    
          [Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html) certificateResponse = future.get();
    
          System.out.println("Certificate created successfully : " + certificateResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html#com_google_cloud_security_privateca_v1_Certificate_getName__)());
    
          // Get the signed certificate and the issuer chain list.
          System.out.println("Signed certificate:\n " + certificateResponse.[getPemCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html#com_google_cloud_security_privateca_v1_Certificate_getPemCertificate__)());
          System.out.println("Issuer chain list:\n" + certificateResponse.[getPemCertificateChainList](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html#com_google_cloud_security_privateca_v1_Certificate_getPemCertificateChainList__)());
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    from google.protobuf import duration_pb2
    
    
    def create_certificate_csr(
        project_id: str,
        location: str,
        ca_pool_name: str,
        ca_name: str,
        certificate_name: str,
        certificate_lifetime: int,
        pem_csr: str,
    ) -> None:
        """
        Create a Certificate which is issued by the specified Certificate Authority (CA).
        The certificate details and the public key is provided as a Certificate Signing Request (CSR).
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: set a unique name for the CA pool.
            ca_name: the name of the certificate authority to sign the CSR.
            certificate_name: set a unique name for the certificate.
            certificate_lifetime: the validity of the certificate in seconds.
            pem_csr: set the Certificate Issuing Request in the pem encoded format.
        """
    
        ca_service_client = privateca_v1.CertificateAuthorityServiceClient()
    
        # The public key used to sign the certificate can be generated using any crypto library/framework.
        # Also you can use Cloud KMS to retrieve an already created public key.
        # For more info, see: https://cloud.google.com/kms/docs/retrieve-public-key.
    
        # Create certificate with CSR.
        # The pem_csr contains the public key and the domain details required.
        certificate = privateca_v1.Certificate(
            pem_csr=pem_csr,
            lifetime=duration_pb2.Duration(seconds=certificate_lifetime),
        )
    
        # Create the Certificate Request.
        # Set the CA which is responsible for creating the certificate with the provided CSR.
        request = privateca_v1.CreateCertificateRequest(
            parent=ca_service_client.ca_pool_path(project_id, location, ca_pool_name),
            certificate_id=certificate_name,
            certificate=certificate,
            issuing_certificate_authority_id=ca_name,
        )
        response = ca_service_client.create_certificate(request=request)
    
        print(f"Certificate created successfully: {response.name}")
    
        # Get the signed certificate and the issuer chain list.
        print(f"Signed certificate: {response.pem_certificate}")
        print(f"Issuer chain list: {response.pem_certificate_chain}")
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_privateca_certificate_authority" "test_ca" {
      pool                     = "my-pool"
      certificate_authority_id = "my-certificate-authority"
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
      name                  = "my-certificate"
      pem_csr               = tls_cert_request.example.cert_request_pem
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
