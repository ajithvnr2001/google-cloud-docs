---
url: https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state/
title: Enable, disable, and restore certificate authorities \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:30.528322+00:00
---

# Enable, disable, and restore certificate authorities  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable, disable, and restore certificate authorities

This document explains how you can manage the state of your certificate authority (CA).

## Enable a CA

All subordinate CAs are created in the `AWAITING_USER_ACTIVATION` state, and they are set to the `STAGED` state after activation. All root CAs are created in the `STAGED` state by default. You must change the CA state to `ENABLED` to include it in a CA pool's certificate issuance rotation. For more information about the operational states of a CA, see [Certificate authority states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).

To enable a CA that is in the `STAGED` or `DISABLED` state, use the following instructions:

### Console

  1. In the Google Cloud console, go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. Under **Certificate authorities** , select your target CA.

  3. Click **Enable**.

  4. In the dialog that opens, click **Confirm**.




### gcloud

To enable a root CA, use the following command:

**Note:** If you want to target a subordinate CA, replace `roots` with `subordinates` in the following command.
    
    
    gcloud privateca roots enable CA_ID --location LOCATION --pool POOL_ID
    

Replace the following:

  * CA_ID: the unique identifier of the CA
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * POOL_ID: the unique identifier of the CA pool that the CA belongs to



For more information about the `gcloud privateca roots enable` command, see [gcloud privateca roots enable](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/enable).

###  Go 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	privateca "cloud.google.com/go/security/privateca/apiv1"
    	"cloud.google.com/go/security/privateca/apiv1/privatecapb"
    )
    
    // Enable the Certificate Authority present in the given ca pool.
    // CA cannot be enabled if it has been already deleted.
    func enableCa(w io.Writer, projectId string, location string, caPoolId string, caId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"	// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"		// The id of the CA pool under which the CA is present.
    	// caId := "ca-id"				// The id of the CA to be enabled.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	fullCaName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s/certificateAuthorities/%s",
    		projectId, location, caPoolId, caId)
    
    	// Create the EnableCertificateAuthorityRequest.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#EnableCertificateAuthorityRequest.
    	req := &privatecapb.EnableCertificateAuthorityRequest{Name: fullCaName}
    
    	op, err := caClient.EnableCertificateAuthority(ctx, req)
    	if err != nil {
    		return fmt.Errorf("EnableCertificateAuthority failed: %w", err)
    	}
    
    	var caResp *privatecapb.CertificateAuthority
    	if caResp, err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("EnableCertificateAuthority failed during wait: %w", err)
    	}
    
    	if caResp.State != privatecapb.[CertificateAuthority_ENABLED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_STATE_UNSPECIFIED_CertificateAuthority_ENABLED_CertificateAuthority_DISABLED_CertificateAuthority_STAGED_CertificateAuthority_AWAITING_USER_ACTIVATION_CertificateAuthority_DELETED) {
    		return fmt.Errorf("unable to enable Certificate Authority. Current state: %s", caResp.State.String())
    	}
    
    	fmt.Fprintf(w, "Successfully enabled Certificate Authority: %s.", caId)
    	return nil
    }
    

###  Java 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).State;
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[EnableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.EnableCertificateAuthorityRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class EnableCertificateAuthority {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: The id of the CA pool under which the CA is present.
        // certificateAuthorityName: The name of the CA to be enabled.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateAuthorityName = "certificate-authority-name";
        enableCertificateAuthority(project, location, poolId, certificateAuthorityName);
      }
    
      // Enable the Certificate Authority present in the given ca pool.
      // CA cannot be enabled if it has been already deleted.
      public static void enableCertificateAuthority(
          String project, String location, String poolId, String certificateAuthorityName)
          throws IOException, ExecutionException, InterruptedException {
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
          // Create the Certificate Authority Name.
          [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html) certificateAuthorityParent =
              [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html).newBuilder()
                  .setProject(project)
                  .setLocation(location)
                  .setCaPool(poolId)
                  .setCertificateAuthority(certificateAuthorityName)
                  .build();
    
          // Create the Enable Certificate Authority Request.
          [EnableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.EnableCertificateAuthorityRequest.html) enableCertificateAuthorityRequest =
              [EnableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.EnableCertificateAuthorityRequest.html).newBuilder()
                  .setName(certificateAuthorityParent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html#com_google_cloud_security_privateca_v1_CertificateAuthorityName_toString__)())
                  .build();
    
          // Enable the Certificate Authority.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[enableCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_enableCertificateAuthorityCallable__)()
                  .futureCall(enableCertificateAuthorityRequest);
          [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while enabling Certificate Authority !" + response.[getError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          // Get the current CA state.
          State caState =
              certificateAuthorityServiceClient
                  .getCertificateAuthority(certificateAuthorityParent)
                  .getState();
    
          // Check if the CA is enabled.
          if (caState == State.ENABLED) {
            System.out.println("Enabled Certificate Authority : " + certificateAuthorityName);
          } else {
            System.out.println(
                "Cannot enable the Certificate Authority ! Current CA State: " + caState);
          }
        }
      }
    }

###  Python 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def enable_certificate_authority(
        project_id: str, location: str, ca_pool_name: str, ca_name: str
    ) -> None:
        """
        Enable the Certificate Authority present in the given ca pool.
        CA cannot be enabled if it has been already deleted.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: the name of the CA pool under which the CA is present.
            ca_name: the name of the CA to be enabled.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
        ca_path = caServiceClient.certificate_authority_path(
            project_id, location, ca_pool_name, ca_name
        )
    
        # Create the Enable Certificate Authority Request.
        request = privateca_v1.EnableCertificateAuthorityRequest(
            name=ca_path,
        )
    
        # Enable the Certificate Authority.
        operation = caServiceClient.enable_certificate_authority(request=request)
        operation.result()
    
        # Get the current CA state.
        ca_state = caServiceClient.get_certificate_authority(name=ca_path).state
    
        # Check if the CA is enabled.
        if ca_state == privateca_v1.CertificateAuthority.State.ENABLED:
            print("Enabled Certificate Authority:", ca_name)
        else:
            print("Cannot enable the Certificate Authority ! Current CA State:", ca_state)
    
    

## Disable a CA

Disabling a CA prevents it from issuing certificates. All certificate requests to a disabled CA are rejected. Other functionalities, such as revoking certificates, publishing Certificate Revocation Lists (CRLs), and updating the CA metadata can still take place.

**Note:** A disabled CA continues to be billed at its usual billing tier. Delete the CA if you want to avoid getting billed for it. For more information about pricing, see [Pricing for CA Service](https://docs.cloud.google.com/certificate-authority-service/pricing).

To disable a CA, use the following instructions:

### Console

  1. In the Google Cloud console, go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. Under **Certificate authorities** , select your target CA.

  3. Click **Disable**.

  4. In the dialog that opens, click **Confirm**.




### gcloud

To disable a root CA, use the following command.

**Note:** If you want to target a subordinate CA, replace `roots` with `subordinates` in the following `gcloud` command.
    
    
    gcloud privateca roots disable CA_ID --location LOCATION --pool POOL_ID
    

Replace the following:

  * CA_ID: the unique identifier of the root CA that you want to disable
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * POOL_ID: the unique identifier of the CA pool that the root CA belongs to



For more information about the `gcloud privateca roots disable` command, see [gcloud privateca roots disable](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/disable).

###  Go 

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
    

###  Java 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).State;
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[DisableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DisableCertificateAuthorityRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html);
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
          [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while disabling Certificate Authority !" + response.[getError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
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

###  Python 

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
    
    

## Restore a CA

When a CA is scheduled for deletion, there is a 30-day grace period before it is deleted. During the grace period, a CA Service Operation Manager (`roles/privateca.caManager`) or CA Service Admin (`roles/privateca.admin`) can stop the deletion process. You can restore a CA only during the grace period.

To restore a CA that is scheduled to be deleted to the disabled state, use the following instructions:

### Console

  1. In the Google Cloud console, go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. Under **Certificate authorities** , select the CA that you want to restore.

  3. Click **Restore**.

  4. In the dialog that opens, click **Confirm**.

  5. Check that the CA is now in the `DISABLED` state.




### gcloud

  1. Confirm that the CA is in the `DELETED` state.
         
         gcloud privateca roots describe CA_ID \
             --pool POOL_ID \
             --location LOCATION \
             --format="value(state)"
         

Where:

     * CA_ID: the unique identifier of the CA
     * POOL_ID: the unique identifier of the CA pool that the CA belongs to
     * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
     * `--format` flag is used to set the format for printing command output resources.

The command returns `DELETED`.

  2. Restore the CA.
         
         gcloud privateca roots undelete CA_ID --location LOCATION --pool POOL_ID
         

Replace the following:

     * CA_ID: the unique identifier of the CA
     * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
     * POOL_ID: the unique identifier of the CA pool that the CA belongs to

For more information about the `gcloud privateca roots undelete` command, see [gcloud privateca roots undelete](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/undelete).

  3. Confirm the state of the CA is now `DISABLED`.
         
         gcloud privateca roots describe CA_ID \
             --pool POOL_ID \
             --location LOCATION \
             --format="value(state)"
         

Where:

     * CA_ID: the unique identifier of the CA
     * POOL_ID: the unique identifier of the CA pool to which the CA belongs
     * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
     * `--format` flag is used to set the format for printing command output resources.

The command returns `DISABLED`.


**Note:** The restored CA cannot issue certificates until you enable it.

###  Go 

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
    

###  Java 

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

###  Python 

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

  * Learn about [CA states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).
  * Learn how to [delete CAs](https://docs.cloud.google.com/certificate-authority-service/docs/deleting-certificate-authorities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
