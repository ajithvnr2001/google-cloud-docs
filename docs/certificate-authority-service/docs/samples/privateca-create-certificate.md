---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-certificate/
title: Create a certificate \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:03.127497+00:00
---

# Create a certificate  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-certificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Create a certificate Stay organized with collections  Save and categorize content based on your preferences. 

Issue/ create a new certificate using a certificate authority.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Issue certificates that attest to third-party identity](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/using-3pi-with-reflection)
  * [Request a certificate](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates)



## Code sample

### Go

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	privateca "cloud.google.com/go/security/privateca/apiv1"
    	"cloud.google.com/go/security/privateca/apiv1/privatecapb"
    	"google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Create a Certificate which is issued by the Certificate Authority present in the CA Pool.
    // The key used to sign the certificate is created by the Cloud KMS.
    func createCertificate(
    	w io.Writer,
    	projectId string,
    	location string,
    	caPoolId string,
    	caId string,
    	certId string,
    	commonName string,
    	domainName string,
    	certDuration int64,
    	publicKeyBytes []byte) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"		// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"			// The CA Pool id in which the certificate authority exists.
    	// caId := "ca-id"					// The name of the certificate authority which issues the certificate.
    	// certId := "certificate"			// A unique name for the certificate.
    	// commonName := "cert-name"		// A common name for the certificate.
    	// domainName := "cert.example.com"	// Fully qualified domain name for the certificate.
    	// certDuration := int64(31536000)	// The validity of the certificate in seconds.
    	// publicKeyBytes 					// The public key used in signing the certificates.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	// Set the Public Key and its format.
    	publicKey := &privatecapb.PublicKey{
    		Key:    publicKeyBytes,
    		Format: privatecapb.[PublicKey_PEM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_PublicKey_KEY_FORMAT_UNSPECIFIED_PublicKey_PEM),
    	}
    
    	// Set Certificate subject config.
    	subjectConfig := &privatecapb.CertificateConfig_SubjectConfig{
    		Subject: &privatecapb.Subject{
    			CommonName: commonName,
    		},
    		SubjectAltName: &privatecapb.SubjectAltNames{
    			DnsNames: []string{domainName},
    		},
    	}
    
    	// Set the X.509 fields required for the certificate.
    	x509Parameters := &privatecapb.X509Parameters{
    		KeyUsage: &privatecapb.KeyUsage{
    			BaseKeyUsage: &privatecapb.KeyUsage_KeyUsageOptions{
    				DigitalSignature: true,
    				KeyEncipherment:  true,
    			},
    			ExtendedKeyUsage: &privatecapb.KeyUsage_ExtendedKeyUsageOptions{
    				ServerAuth: true,
    				ClientAuth: true,
    			},
    		},
    	}
    
    	// Set certificate settings.
    	cert := &privatecapb.Certificate{
    		CertificateConfig: &privatecapb.Certificate_Config{
    			Config: &privatecapb.CertificateConfig{
    				PublicKey:     publicKey,
    				SubjectConfig: subjectConfig,
    				X509Config:    x509Parameters,
    			},
    		},
    		Lifetime: &durationpb.Duration{
    			Seconds: certDuration,
    		},
    	}
    
    	fullCaPoolName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s", projectId, location, caPoolId)
    
    	// Create the CreateCertificateRequest.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#CreateCertificateRequest.
    	req := &privatecapb.CreateCertificateRequest{
    		Parent:                        fullCaPoolName,
    		CertificateId:                 certId,
    		Certificate:                   cert,
    		IssuingCertificateAuthorityId: caId,
    	}
    
    	_, err = caClient.CreateCertificate(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateCertificate failed: %w", err)
    	}
    
    	fmt.Fprintf(w, "Certificate %s created", certId)
    
    	return nil
    }
    

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html);
    import com.google.cloud.security.privateca.v1.[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html);
    import com.google.cloud.security.privateca.v1.[CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html).[SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html);
    import com.google.cloud.security.privateca.v1.[CreateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).[ExtendedKeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.ExtendedKeyUsageOptions.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).[KeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.html);
    import com.google.cloud.security.privateca.v1.[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.PublicKey.html);
    import com.google.cloud.security.privateca.v1.[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.PublicKey.html).[KeyFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.PublicKey.KeyFormat.html);
    import com.google.cloud.security.privateca.v1.[Subject](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.html);
    import com.google.cloud.security.privateca.v1.[SubjectAltNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.SubjectAltNames.html);
    import com.google.cloud.security.privateca.v1.[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html);
    import com.google.cloud.security.privateca.v1.[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html).[CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class CreateCertificate {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // publicKeyBytes: Public key used in signing the certificates.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Set a unique id for the CA pool.
        // certificateAuthorityName: The name of the certificate authority which issues the certificate.
        // certificateName: Set a unique name for the certificate.
        String project = "your-project-id";
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) publicKeyBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(new byte[]{});
        String location = "ca-location";
        String poolId = "ca-poolId";
        String certificateAuthorityName = "certificate-authority-name";
        String certificateName = "certificate-name";
    
        createCertificate(
            project, location, poolId, certificateAuthorityName, certificateName, publicKeyBytes);
      }
    
      // Create a Certificate which is issued by the Certificate Authority present in the CA Pool.
      // The public key used to sign the certificate can be generated using any crypto
      // library/framework.
      public static void createCertificate(
          String project,
          String location,
          String poolId,
          String certificateAuthorityName,
          String certificateName,
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) publicKeyBytes)
          throws InterruptedException, ExecutionException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          // commonName: Enter a title for your certificate.
          // orgName: Provide the name of your company.
          // domainName: List the fully qualified domain name.
          // certificateLifetime: The validity of the certificate in seconds.
          String commonName = "commonname";
          String orgName = "orgname";
          String domainName = "dns.example.com";
          long certificateLifetime = 1000L;
    
          // Set the Public Key and its format.
          [PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.PublicKey.html) publicKey =
              [PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.PublicKey.html).newBuilder().setKey(publicKeyBytes).[setFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.PublicKey.Builder.html#com_google_cloud_security_privateca_v1_PublicKey_Builder_setFormat_com_google_cloud_security_privateca_v1_PublicKey_KeyFormat_)([KeyFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.PublicKey.KeyFormat.html).PEM).build();
    
          [SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html) subjectConfig =
              [SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html).newBuilder()
                  // Set the common name and org name.
                  .setSubject(
                      [Subject](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.html).newBuilder().[setCommonName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.Builder.html#com_google_cloud_security_privateca_v1_Subject_Builder_setCommonName_java_lang_String_)(commonName).[setOrganization](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.Builder.html#com_google_cloud_security_privateca_v1_Subject_Builder_setOrganization_java_lang_String_)(orgName).build())
                  // Set the fully qualified domain name.
                  .setSubjectAltName([SubjectAltNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.SubjectAltNames.html).newBuilder().[addDnsNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.SubjectAltNames.Builder.html#com_google_cloud_security_privateca_v1_SubjectAltNames_Builder_addDnsNames_java_lang_String_)(domainName).build())
                  .build();
    
          // Set the X.509 fields required for the certificate.
          [X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html) x509Parameters =
              [X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html).newBuilder()
                  .[setKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_Builder_setKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_)(
                      [KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).newBuilder()
                          .[setBaseKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_Builder_setBaseKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_)(
                              [KeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.html).newBuilder()
                                  .[setDigitalSignature](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setDigitalSignature_boolean_)(true)
                                  .[setKeyEncipherment](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setKeyEncipherment_boolean_)(true)
                                  .[setCertSign](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setCertSign_boolean_)(true)
                                  .build())
                          .[setExtendedKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_Builder_setExtendedKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_ExtendedKeyUsageOptions_)(
                              [ExtendedKeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.ExtendedKeyUsageOptions.html).newBuilder().[setServerAuth](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.ExtendedKeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_ExtendedKeyUsageOptions_Builder_setServerAuth_boolean_)(true).build())
                          .build())
                  .[setCaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_Builder_setCaOptions_com_google_cloud_security_privateca_v1_X509Parameters_CaOptions_)([CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html).newBuilder().[setIsCa](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_CaOptions_Builder_setIsCa_boolean_)(true).buildPartial())
                  .build();
    
          // Create certificate.
          [Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html) certificate =
              [Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html).newBuilder()
                  .setConfig(
                      [CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html).newBuilder()
                          .setPublicKey(publicKey)
                          .[setSubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.Builder.html#com_google_cloud_security_privateca_v1_CertificateConfig_Builder_setSubjectConfig_com_google_cloud_security_privateca_v1_CertificateConfig_SubjectConfig_)(subjectConfig)
                          .[setX509Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.Builder.html#com_google_cloud_security_privateca_v1_CertificateConfig_Builder_setX509Config_com_google_cloud_security_privateca_v1_X509Parameters_)(x509Parameters)
                          .build())
                  .setLifetime([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(certificateLifetime).build())
                  .build();
    
          // Create the Certificate Request.
          [CreateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.html) certificateRequest =
              [CreateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.html).newBuilder()
                  .setParent([CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html).of(project, location, poolId).toString())
                  .[setCertificateId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.Builder.html#com_google_cloud_security_privateca_v1_CreateCertificateRequest_Builder_setCertificateId_java_lang_String_)(certificateName)
                  .setCertificate(certificate)
                  .[setIssuingCertificateAuthorityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest.Builder.html#com_google_cloud_security_privateca_v1_CreateCertificateRequest_Builder_setIssuingCertificateAuthorityId_java_lang_String_)(certificateAuthorityName)
                  .build();
    
          // Get the Certificate response.
          ApiFuture<Certificate> future =
              certificateAuthorityServiceClient
                  .[createCertificateCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_createCertificateCallable__)()
                  .futureCall(certificateRequest);
    
          [Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html) response = future.get();
          // Get the PEM encoded, signed X.509 certificate.
          System.out.println(response.[getPemCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html#com_google_cloud_security_privateca_v1_Certificate_getPemCertificate__)());
          // To verify the obtained certificate, use this intermediate chain list.
          System.out.println(response.[getPemCertificateChainList](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html#com_google_cloud_security_privateca_v1_Certificate_getPemCertificateChainList__)());
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    from google.protobuf import duration_pb2
    
    
    def create_certificate(
        project_id: str,
        location: str,
        ca_pool_name: str,
        ca_name: str,
        certificate_name: str,
        common_name: str,
        domain_name: str,
        certificate_lifetime: int,
        public_key_bytes: bytes,
    ) -> None:
        """
        Create a Certificate which is issued by the Certificate Authority present in the CA Pool.
        The key used to sign the certificate is created by the Cloud KMS.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: set a unique name for the CA pool.
            ca_name: the name of the certificate authority which issues the certificate.
            certificate_name: set a unique name for the certificate.
            common_name: a title for your certificate.
            domain_name: fully qualified domain name for your certificate.
            certificate_lifetime: the validity of the certificate in seconds.
            public_key_bytes: public key used in signing the certificates.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        # The public key used to sign the certificate can be generated using any crypto library/framework.
        # Also you can use Cloud KMS to retrieve an already created public key.
        # For more info, see: https://cloud.google.com/kms/docs/retrieve-public-key.
    
        # Set the Public Key and its format.
        public_key = privateca_v1.PublicKey(
            key=public_key_bytes,
            format_=privateca_v1.PublicKey.KeyFormat.PEM,
        )
    
        subject_config = privateca_v1.CertificateConfig.SubjectConfig(
            subject=privateca_v1.Subject(common_name=common_name),
            subject_alt_name=privateca_v1.SubjectAltNames(dns_names=[domain_name]),
        )
    
        # Set the X.509 fields required for the certificate.
        x509_parameters = privateca_v1.X509Parameters(
            key_usage=privateca_v1.KeyUsage(
                base_key_usage=privateca_v1.KeyUsage.KeyUsageOptions(
                    digital_signature=True,
                    key_encipherment=True,
                ),
                extended_key_usage=privateca_v1.KeyUsage.ExtendedKeyUsageOptions(
                    server_auth=True,
                    client_auth=True,
                ),
            ),
        )
    
        # Create certificate.
        certificate = privateca_v1.Certificate(
            config=privateca_v1.CertificateConfig(
                public_key=public_key,
                subject_config=subject_config,
                x509_config=x509_parameters,
            ),
            lifetime=duration_pb2.Duration(seconds=certificate_lifetime),
        )
    
        # Create the Certificate Request.
        request = privateca_v1.CreateCertificateRequest(
            parent=caServiceClient.ca_pool_path(project_id, location, ca_pool_name),
            certificate_id=certificate_name,
            certificate=certificate,
            issuing_certificate_authority_id=ca_name,
        )
        result = caServiceClient.create_certificate(request=request)
    
        print("Certificate creation result:", result)
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_privateca_certificate_authority" "authority" {
      // This example assumes this pool already exists.
      // Pools cannot be deleted in normal test circumstances, so we depend on static pools
      pool                     = "my-pool"
      certificate_authority_id = "my-sample-certificate-authority"
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
            is_ca = true
          }
          key_usage {
            base_key_usage {
              digital_signature = true
              cert_sign         = true
              crl_sign          = true
            }
            extended_key_usage {
              server_auth = true
            }
          }
        }
      }
      lifetime = "86400s"
      key_spec {
        algorithm = "RSA_PKCS1_4096_SHA256"
      }
    }
    
    
    resource "google_privateca_certificate" "default" {
      pool     = "my-pool"
      location = "us-central1"
      lifetime = "860s"
      name     = "my-sample-certificate"
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
            postal_code         = "94109"
          }
        }
        x509_config {
          ca_options {
            is_ca = false
          }
          key_usage {
            base_key_usage {
              crl_sign = true
            }
            extended_key_usage {
              server_auth = true
            }
          }
        }
        public_key {
          format = "PEM"
          key    = base64encode(data.tls_public_key.example.public_key_pem)
        }
      }
      // Certificates require an authority to exist in the pool, though they don't
      // need to be explicitly connected to it
      depends_on = [google_privateca_certificate_authority.authority]
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
