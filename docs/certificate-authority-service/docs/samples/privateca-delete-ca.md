---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-delete-ca/
title: Delete Certificate Authority \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:16.707420+00:00
---

# Delete Certificate Authority  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-delete-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Delete Certificate Authority Stay organized with collections  Save and categorize content based on your preferences. 

Delete the Certificate Authority from the specified CA pool.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Delete certificate authorities](https://docs.cloud.google.com/certificate-authority-service/docs/deleting-certificate-authorities)



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
    
    // Delete a Certificate Authority from the specified CA pool.
    // Before deletion, the CA must be disabled or staged and must not contain any active certificates.
    func deleteCa(w io.Writer, projectId string, location string, caPoolId string, caId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"	// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"		// The id of the CA pool under which the CA is present.
    	// caId := "ca-id"				// The id of the CA to be deleted.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	fullCaName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s/certificateAuthorities/%s",
    		projectId, location, caPoolId, caId)
    
    	// Check if the CA is disabled or staged.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#GetCertificateAuthorityRequest.
    	caReq := &privatecapb.GetCertificateAuthorityRequest{Name: fullCaName}
    	caResp, err := caClient.GetCertificateAuthority(ctx, caReq)
    	if err != nil {
    		return fmt.Errorf("GetCertificateAuthority failed: %w", err)
    	}
    
    	if caResp.State != privatecapb.CertificateAuthority_DISABLED &&
    		caResp.State != privatecapb.[CertificateAuthority_STAGED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_STATE_UNSPECIFIED_CertificateAuthority_ENABLED_CertificateAuthority_DISABLED_CertificateAuthority_STAGED_CertificateAuthority_AWAITING_USER_ACTIVATION_CertificateAuthority_DELETED) {
    		return fmt.Errorf("you can only delete disabled or staged Certificate Authorities. %s is not disabled", caId)
    	}
    
    	// Create the DeleteCertificateAuthorityRequest.
    	// Setting the IgnoreActiveCertificates to True will delete the CA
    	// even if it contains active certificates. Care should be taken to re-anchor
    	// the certificates to new CA before deleting.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#DeleteCertificateAuthorityRequest.
    	req := &privatecapb.DeleteCertificateAuthorityRequest{
    		Name:                     fullCaName,
    		IgnoreActiveCertificates: false,
    	}
    
    	op, err := caClient.DeleteCertificateAuthority(ctx, req)
    	if err != nil {
    		return fmt.Errorf("DeleteCertificateAuthority failed: %w", err)
    	}
    
    	if caResp, err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("DeleteCertificateAuthority failed during wait: %w", err)
    	}
    
    	if caResp.State != privatecapb.[CertificateAuthority_DELETED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_STATE_UNSPECIFIED_CertificateAuthority_ENABLED_CertificateAuthority_DISABLED_CertificateAuthority_STAGED_CertificateAuthority_AWAITING_USER_ACTIVATION_CertificateAuthority_DELETED) {
    		return fmt.Errorf("unable to delete Certificate Authority. Current state: %s", caResp.State.String())
    	}
    
    	fmt.Fprintf(w, "Successfully deleted Certificate Authority: %s.", caId)
    	return nil
    }
    

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).State;
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[DeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCertificateAuthorityRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class DeleteCertificateAuthority {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: The id of the CA pool under which the CA is present.
        // certificateAuthorityName: The name of the CA to be deleted.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateAuthorityName = "certificate-authority-name";
        deleteCertificateAuthority(project, location, poolId, certificateAuthorityName);
      }
    
      // Delete the Certificate Authority from the specified CA pool.
      // Before deletion, the CA must be disabled and must not contain any active certificates.
      public static void deleteCertificateAuthority(
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
    
          // Check if the CA is enabled.
          State caState =
              certificateAuthorityServiceClient
                  .getCertificateAuthority(certificateAuthorityNameParent)
                  .getState();
          if (caState == State.ENABLED) {
            System.out.println(
                "Please disable the Certificate Authority before deletion ! Current state: " + caState);
            return;
          }
    
          // Create the DeleteCertificateAuthorityRequest.
          // Setting the setIgnoreActiveCertificates() to true, will delete the CA
          // even if it contains active certificates. Care should be taken to re-anchor
          // the certificates to new CA before deleting.
          [DeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCertificateAuthorityRequest.html) deleteCertificateAuthorityRequest =
              [DeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCertificateAuthorityRequest.html).newBuilder()
                  .setName(certificateAuthorityNameParent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html#com_google_cloud_security_privateca_v1_CertificateAuthorityName_toString__)())
                  .[setIgnoreActiveCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCertificateAuthorityRequest.Builder.html#com_google_cloud_security_privateca_v1_DeleteCertificateAuthorityRequest_Builder_setIgnoreActiveCertificates_boolean_)(false)
                  .build();
    
          // Delete the Certificate Authority.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[deleteCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_deleteCertificateAuthorityCallable__)()
                  .futureCall(deleteCertificateAuthorityRequest);
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while deleting Certificate Authority !" + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          // Check if the CA has been deleted.
          caState =
              certificateAuthorityServiceClient
                  .getCertificateAuthority(certificateAuthorityNameParent)
                  .getState();
          if (caState == State.DELETED) {
            System.out.println(
                "Successfully deleted Certificate Authority : " + certificateAuthorityName);
          } else {
            System.out.println(
                "Unable to delete Certificate Authority. Please try again ! Current state: " + caState);
          }
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def delete_certificate_authority(
        project_id: str, location: str, ca_pool_name: str, ca_name: str
    ) -> None:
        """
        Delete the Certificate Authority from the specified CA pool.
        Before deletion, the CA must be disabled and must not contain any active certificates.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: the name of the CA pool under which the CA is present.
            ca_name: the name of the CA to be deleted.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
        ca_path = caServiceClient.certificate_authority_path(
            project_id, location, ca_pool_name, ca_name
        )
    
        # Check if the CA is enabled.
        ca_state = caServiceClient.get_certificate_authority(name=ca_path).state
        if ca_state != privateca_v1.CertificateAuthority.State.DISABLED:
            print(
                "Please disable the Certificate Authority before deletion ! Current state:",
                ca_state,
            )
            raise RuntimeError(
                f"You can only delete disabled Certificate Authorities. "
                f"{ca_name} is not disabled!"
            )
    
        # Create the DeleteCertificateAuthorityRequest.
        # Setting the ignore_active_certificates to True will delete the CA
        # even if it contains active certificates. Care should be taken to re-anchor
        # the certificates to new CA before deleting.
        request = privateca_v1.DeleteCertificateAuthorityRequest(
            name=ca_path, ignore_active_certificates=False
        )
    
        # Delete the Certificate Authority.
        operation = caServiceClient.delete_certificate_authority(request=request)
        result = operation.result()
    
        print("Operation result", result)
    
        # Get the current CA state.
        ca_state = caServiceClient.get_certificate_authority(name=ca_path).state
    
        # Check if the CA has been deleted.
        if ca_state == privateca_v1.CertificateAuthority.State.DELETED:
            print("Successfully deleted Certificate Authority:", ca_name)
        else:
            print(
                "Unable to delete Certificate Authority. Please try again ! Current state:",
                ca_state,
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
