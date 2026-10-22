---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-disable-ca/
title: Disable a Certificate Authority \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:43.134622+00:00
---

# Disable a Certificate Authority  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-disable-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Disable a Certificate Authority Stay organized with collections  Save and categorize content based on your preferences. 

Disable a Certificate Authority in the given CA pool.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Enable, disable, and restore certificate authorities](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state)



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
    
    // Disable a Certificate Authority from the specified CA pool.
    func disableCa(w io.Writer, projectId string, location string, caPoolId string, caId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"	// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"		// The id of the CA pool under which the CA is present.
    	// caId := "ca-id"				// The id of the CA to be disabled.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	fullCaName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s/certificateAuthorities/%s",
    		projectId, location, caPoolId, caId)
    
    	// Create the DisableCertificateAuthorityRequest.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#DisableCertificateAuthorityRequest.
    	req := &privatecapb.DisableCertificateAuthorityRequest{Name: fullCaName}
    
    	op, err := caClient.DisableCertificateAuthority(ctx, req)
    	if err != nil {
    		return fmt.Errorf("DisableCertificateAuthority failed: %w", err)
    	}
    
    	var caResp *privatecapb.CertificateAuthority
    	if caResp, err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("DisableCertificateAuthority failed during wait: %w", err)
    	}
    
    	if caResp.State != privatecapb.[CertificateAuthority_DISABLED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_STATE_UNSPECIFIED_CertificateAuthority_ENABLED_CertificateAuthority_DISABLED_CertificateAuthority_STAGED_CertificateAuthority_AWAITING_USER_ACTIVATION_CertificateAuthority_DELETED) {
    		return fmt.Errorf("unable to disabled Certificate Authority. Current state: %s", caResp.State.String())
    	}
    
    	fmt.Fprintf(w, "Successfully disabled Certificate Authority: %s.", caId)
    	return nil
    }
    

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).State;
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[DisableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DisableCertificateAuthorityRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class DisableCertificateAuthority {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: The id of the CA pool under which the CA is present.
        // certificateAuthorityName: The name of the CA to be disabled.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateAuthorityName = "certificate-authority-name";
        disableCertificateAuthority(project, location, poolId, certificateAuthorityName);
      }
    
      // Disable a Certificate Authority which is present in the given CA pool.
      public static void disableCertificateAuthority(
          String project, String location, String poolId, String certificateAuthorityName)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          // Create the Certificate Authority Name.
          [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html) certificateAuthorityNameParent =
              [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html).newBuilder()
                  .setProject(project)
                  .setLocation(location)
                  .setCaPool(poolId)
                  .setCertificateAuthority(certificateAuthorityName)
                  .build();
    
          // Create the Disable Certificate Authority Request.
          [DisableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DisableCertificateAuthorityRequest.html) disableCertificateAuthorityRequest =
              [DisableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DisableCertificateAuthorityRequest.html).newBuilder()
                  .setName(certificateAuthorityNameParent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html#com_google_cloud_security_privateca_v1_CertificateAuthorityName_toString__)())
                  .build();
    
          // Disable the Certificate Authority.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[disableCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_disableCertificateAuthorityCallable__)()
                  .futureCall(disableCertificateAuthorityRequest);
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while disabling Certificate Authority !" + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          // Get the current CA state.
          State caState =
              certificateAuthorityServiceClient
                  .getCertificateAuthority(certificateAuthorityNameParent)
                  .getState();
    
          // Check if the Certificate Authority is disabled.
          if (caState == State.DISABLED) {
            System.out.println("Disabled Certificate Authority : " + certificateAuthorityName);
          } else {
            System.out.println(
                "Cannot disable the Certificate Authority ! Current CA State: " + caState);
          }
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def disable_certificate_authority(
        project_id: str, location: str, ca_pool_name: str, ca_name: str
    ) -> None:
        """
        Disable a Certificate Authority which is present in the given CA pool.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: the name of the CA pool under which the CA is present.
            ca_name: the name of the CA to be disabled.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
        ca_path = caServiceClient.certificate_authority_path(
            project_id, location, ca_pool_name, ca_name
        )
    
        # Create the Disable Certificate Authority Request.
        request = privateca_v1.DisableCertificateAuthorityRequest(name=ca_path)
    
        # Disable the Certificate Authority.
        operation = caServiceClient.disable_certificate_authority(request=request)
        operation.result()
    
        # Get the current CA state.
        ca_state = caServiceClient.get_certificate_authority(name=ca_path).state
    
        # Check if the CA is disabled.
        if ca_state == privateca_v1.CertificateAuthority.State.DISABLED:
            print("Disabled Certificate Authority:", ca_name)
        else:
            print("Cannot disable the Certificate Authority ! Current CA State:", ca_state)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
