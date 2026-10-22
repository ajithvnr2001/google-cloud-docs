---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-undelete-ca/
title: Undelete a Certificate Authority \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:27.663547+00:00
---

# Undelete a Certificate Authority  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-undelete-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Undelete a Certificate Authority Stay organized with collections  Save and categorize content based on your preferences. 

Restore a deleted CA, if still within the grace period of 30 days.

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
    
    // Undelete a Certificate Authority from the specified CA pool.
    func unDeleteCa(w io.Writer, projectId string, location string, caPoolId string, caId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"	// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"		// The id of the CA pool under which the CA is present.
    	// caId := "ca-id"				// The id of the CA to be undeleted.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	fullCaName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s/certificateAuthorities/%s",
    		projectId, location, caPoolId, caId)
    
    	// Check if the CA is deleted.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#GetCertificateAuthorityRequest.
    	caReq := &privatecapb.GetCertificateAuthorityRequest{Name: fullCaName}
    	caResp, err := caClient.GetCertificateAuthority(ctx, caReq)
    	if err != nil {
    		return fmt.Errorf("GetCertificateAuthority failed: %w", err)
    	}
    
    	if caResp.State != privatecapb.[CertificateAuthority_DELETED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_STATE_UNSPECIFIED_CertificateAuthority_ENABLED_CertificateAuthority_DISABLED_CertificateAuthority_STAGED_CertificateAuthority_AWAITING_USER_ACTIVATION_CertificateAuthority_DELETED) {
    		return fmt.Errorf("you can only undelete deleted Certificate Authorities. %s is not deleted", caId)
    	}
    
    	// Create the UndeleteCertificateAuthority.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#UndeleteCertificateAuthorityRequest.
    	req := &privatecapb.UndeleteCertificateAuthorityRequest{Name: fullCaName}
    
    	op, err := caClient.UndeleteCertificateAuthority(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UndeleteCertificateAuthority failed: %w", err)
    	}
    
    	if caResp, err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("UndeleteCertificateAuthority failed during wait: %w", err)
    	}
    
    	if caResp.State == privatecapb.[CertificateAuthority_DELETED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_STATE_UNSPECIFIED_CertificateAuthority_ENABLED_CertificateAuthority_DISABLED_CertificateAuthority_STAGED_CertificateAuthority_AWAITING_USER_ACTIVATION_CertificateAuthority_DELETED) {
    		return fmt.Errorf("unable to undelete Certificate Authority. Current state: %s", caResp.State.String())
    	}
    
    	fmt.Fprintf(w, "Successfully undeleted Certificate Authority: %s.", caId)
    	return nil
    }
    

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).State;
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UndeleteCertificateAuthorityRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UndeleteCertificateAuthority {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: The id of the CA pool under which the deleted CA is present.
        // certificateAuthorityName: The name of the CA to be restored (undeleted).
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateAuthorityName = "certificate-authority-name";
    
        undeleteCertificateAuthority(project, location, poolId, certificateAuthorityName);
      }
    
      // Restore a deleted CA, if still within the grace period of 30 days.
      public static void undeleteCertificateAuthority(
          String project, String location, String poolId, String certificateAuthorityName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          String certificateAuthorityParent =
              [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html).of(project, location, poolId, certificateAuthorityName)
                  .toString();
    
          // Confirm if the CA is in DELETED stage.
          if (getCurrentState(certificateAuthorityServiceClient, certificateAuthorityParent)
              != State.DELETED) {
            System.out.println("CA is not deleted !");
            return;
          }
    
          // Create the Request.
          [UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UndeleteCertificateAuthorityRequest.html) undeleteCertificateAuthorityRequest =
              [UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UndeleteCertificateAuthorityRequest.html).newBuilder()
                  .setName(certificateAuthorityParent)
                  .build();
    
          // Undelete the CA.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[undeleteCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_undeleteCertificateAuthorityCallable__)()
                  .futureCall(undeleteCertificateAuthorityRequest);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) response = futureCall.get(5, TimeUnit.SECONDS);
    
          // CA state changes from DELETED to DISABLED if successfully restored.
          // Confirm if the CA is DISABLED.
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()
              || getCurrentState(certificateAuthorityServiceClient, certificateAuthorityParent)
              != State.DISABLED) {
            System.out.println(
                "Unable to restore the Certificate Authority! Please try again !"
                    + response.[getError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          // The CA will be in the DISABLED state. Enable before use.
          System.out.println(
              "Successfully restored the Certificate Authority ! " + certificateAuthorityName);
        }
      }
    
      // Get the current state of CA.
      private static State getCurrentState(
          [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) client, String certificateAuthorityParent) {
        return client.[getCertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_getCertificateAuthority__org_jspecify_annotations_Nullable_com_google_cloud_security_privateca_v1_CertificateAuthorityName_)(certificateAuthorityParent).getState();
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def undelete_certificate_authority(
        project_id: str, location: str, ca_pool_name: str, ca_name: str
    ) -> None:
        """
        Restore a deleted CA, if still within the grace period of 30 days.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: the name of the CA pool under which the deleted CA is present.
            ca_name: the name of the CA to be restored (undeleted).
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
        ca_path = caServiceClient.certificate_authority_path(
            project_id, location, ca_pool_name, ca_name
        )
    
        # Confirm if the CA is in DELETED stage.
        ca_state = caServiceClient.get_certificate_authority(name=ca_path).state
        if ca_state != privateca_v1.CertificateAuthority.State.DELETED:
            print("CA is not deleted !")
            return
    
        # Create the Request.
        request = privateca_v1.UndeleteCertificateAuthorityRequest(name=ca_path)
    
        # Undelete the CA.
        operation = caServiceClient.undelete_certificate_authority(request=request)
        result = operation.result()
    
        print("Operation result", result)
    
        # Get the current CA state.
        ca_state = caServiceClient.get_certificate_authority(name=ca_path).state
    
        # CA state changes from DELETED to DISABLED if successfully restored.
        # Confirm if the CA is DISABLED.
        if ca_state == privateca_v1.CertificateAuthority.State.DISABLED:
            print("Successfully undeleted Certificate Authority:", ca_name)
        else:
            print(
                "Unable to restore the Certificate Authority! Please try again! Current state:",
                ca_state,
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
