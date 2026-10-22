---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-revoke-certificate/
title: Revoke a Certificate \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:39.512471+00:00
---

# Revoke a Certificate  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-revoke-certificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Revoke a Certificate Stay organized with collections  Save and categorize content based on your preferences. 

Revoke an issued Certificate.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Revoke certificates](https://docs.cloud.google.com/certificate-authority-service/docs/revoking-certificates)



## Code sample

### Go

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	privateca "cloud.google.com/go/security/privateca/apiv1"
    	"cloud.google.com/go/security/privateca/apiv1/privatecapb"
    )
    
    // Revoke an issued certificate. Once revoked, the certificate will become invalid
    // and will expire post its lifetime.
    func revokeCertificate(
    	w io.Writer,
    	projectId string,
    	location string,
    	caPoolId string,
    	certId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"		// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"			// The CA Pool id in which the certificate exists.
    	// certId := "certificate"			// A unique name for the certificate.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	fullCertName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s/certificates/%s", projectId, location,
    		caPoolId, certId)
    
    	// Create the RevokeCertificateRequest and specify the appropriate revocation reason.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#RevokeCertificateRequest.
    	req := &privatecapb.RevokeCertificateRequest{
    		Name:   fullCertName,
    		Reason: privatecapb.[RevocationReason_PRIVILEGE_WITHDRAWN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_RevocationReason_REVOCATION_REASON_UNSPECIFIED_RevocationReason_KEY_COMPROMISE_RevocationReason_CERTIFICATE_AUTHORITY_COMPROMISE_RevocationReason_AFFILIATION_CHANGED_RevocationReason_SUPERSEDED_RevocationReason_CESSATION_OF_OPERATION_RevocationReason_CERTIFICATE_HOLD_RevocationReason_PRIVILEGE_WITHDRAWN_RevocationReason_ATTRIBUTE_AUTHORITY_COMPROMISE),
    	}
    
    	_, err = caClient.RevokeCertificate(ctx, req)
    	if err != nil {
    		return fmt.Errorf("RevokeCertificate failed: %w", err)
    	}
    
    	fmt.Fprintf(w, "Certificate %s revoked", certId)
    
    	return nil
    }
    

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CertificateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateName.html);
    import com.google.cloud.security.privateca.v1.[RevocationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.RevocationReason.html);
    import com.google.cloud.security.privateca.v1.[RevokeCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.RevokeCertificateRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class RevokeCertificate {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Id for the CA pool which contains the certificate.
        // certificateName: Name of the certificate to be revoked.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateName = "certificate-name";
        revokeCertificate(project, location, poolId, certificateName);
      }
    
      // Revoke an issued certificate. Once revoked, the certificate will become invalid and will expire
      // post its lifetime.
      public static void revokeCertificate(
          String project, String location, String poolId, String certificateName)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          // Create Certificate Name.
          [CertificateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateName.html) certificateNameParent =
              [CertificateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateName.html).newBuilder()
                  .setProject(project)
                  .setLocation(location)
                  .setCaPool(poolId)
                  .setCertificate(certificateName)
                  .build();
    
          // Create Revoke Certificate Request and specify the appropriate revocation reason.
          [RevokeCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.RevokeCertificateRequest.html) revokeCertificateRequest =
              [RevokeCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.RevokeCertificateRequest.html).newBuilder()
                  .setName(certificateNameParent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateName.html#com_google_cloud_security_privateca_v1_CertificateName_toString__)())
                  .[setReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.RevokeCertificateRequest.Builder.html#com_google_cloud_security_privateca_v1_RevokeCertificateRequest_Builder_setReason_com_google_cloud_security_privateca_v1_RevocationReason_)([RevocationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.RevocationReason.html).PRIVILEGE_WITHDRAWN)
                  .build();
    
          // Revoke certificate.
          ApiFuture<Certificate> response =
              certificateAuthorityServiceClient
                  .[revokeCertificateCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_revokeCertificateCallable__)()
                  .futureCall(revokeCertificateRequest);
          [Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html) certificateResponse = response.get();
    
          System.out.println("Certificate Revoked: " + certificateResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html#com_google_cloud_security_privateca_v1_Certificate_getName__)());
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def revoke_certificate(
        project_id: str,
        location: str,
        ca_pool_name: str,
        certificate_name: str,
    ) -> None:
        """
        Revoke an issued certificate. Once revoked, the certificate will become invalid and will expire post its lifetime.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: name for the CA pool which contains the certificate.
            certificate_name: name of the certificate to be revoked.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        # Create Certificate Path.
        certificate_path = caServiceClient.certificate_path(
            project_id, location, ca_pool_name, certificate_name
        )
    
        # Create Revoke Certificate Request and specify the appropriate revocation reason.
        request = privateca_v1.RevokeCertificateRequest(
            name=certificate_path, reason=privateca_v1.RevocationReason.PRIVILEGE_WITHDRAWN
        )
        result = caServiceClient.revoke_certificate(request=request)
    
        print("Certificate revoke result:", result)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
