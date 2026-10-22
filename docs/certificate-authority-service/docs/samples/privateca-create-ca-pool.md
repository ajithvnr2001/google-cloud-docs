---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-ca-pool/
title: Create a CA pool \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:21.060629+00:00
---

# Create a CA pool  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-create-ca-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Create a CA pool Stay organized with collections  Save and categorize content based on your preferences. 

Create a new CA pool in the specified project and zone.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool)



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
    
    // Create a Certificate Authority pool. All certificates created under this CA pool will
    // follow the same issuance policy, IAM policies, etc.
    func createCaPool(w io.Writer, projectId string, location string, caPoolId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"	// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"		// A unique id/name for the ca pool.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	caPool := &privatecapb.CaPool{
    		// Set the tier (see: https://cloud.google.com/certificate-authority-service/docs/tiers).
    		Tier: privatecapb.[CaPool_ENTERPRISE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CaPool_TIER_UNSPECIFIED_CaPool_ENTERPRISE_CaPool_DEVOPS),
    	}
    
    	locationPath := fmt.Sprintf("projects/%s/locations/%s", projectId, location)
    
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#CreateCaPoolRequest.
    	req := &privatecapb.CreateCaPoolRequest{
    		Parent:   locationPath,
    		CaPoolId: caPoolId,
    		CaPool:   caPool,
    	}
    
    	op, err := caClient.CreateCaPool(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateCaPool failed: %w", err)
    	}
    
    	if _, err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("CreateCaPool failed during wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "CA Pool created")
    
    	return nil
    }
    

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html);
    import com.google.cloud.security.privateca.v1.[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html).[IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.html);
    import com.google.cloud.security.privateca.v1.[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html).[Tier](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.Tier.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html);
    import com.google.cloud.security.privateca.v1.[CreateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCaPoolRequest.html);
    import com.google.cloud.security.privateca.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.LocationName.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class CreateCaPool {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Set a unique poolId for the CA pool.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        createCaPool(project, location, poolId);
      }
    
      // Create a Certificate Authority Pool. All certificates created under this CA pool will
      // follow the same issuance policy, IAM policies,etc.,
      public static void createCaPool(String project, String location, String poolId)
          throws InterruptedException, ExecutionException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          [IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.html) issuancePolicy = [IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.html).newBuilder()
              .setIdentityConstraints([CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html).newBuilder()
                  .[setAllowSubjectPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setAllowSubjectPassthrough_boolean_)(true)
                  .[setAllowSubjectAltNamesPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setAllowSubjectAltNamesPassthrough_boolean_)(true)
                  .build())
              .build();
    
          /* Create the pool request
            Set Parent which denotes the project id and location.
            Set the Tier (see: https://cloud.google.com/certificate-authority-service/docs/tiers).
          */
          [CreateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCaPoolRequest.html) caPoolRequest =
              [CreateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCaPoolRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.LocationName.html).of(project, location).toString())
                  .[setCaPoolId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCaPoolRequest.Builder.html#com_google_cloud_security_privateca_v1_CreateCaPoolRequest_Builder_setCaPoolId_java_lang_String_)(poolId)
                  .setCaPool(
                      [CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html).newBuilder()
                          .[setIssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.Builder.html#com_google_cloud_security_privateca_v1_CaPool_Builder_setIssuancePolicy_com_google_cloud_security_privateca_v1_CaPool_IssuancePolicy_)(issuancePolicy)
                          .setTier([Tier](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.Tier.html).ENTERPRISE)
                          .build())
                  .build();
    
          // Create the CA pool.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient.[createCaPoolCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_createCaPoolCallable__)().futureCall(caPoolRequest);
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while creating CA pool !" + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          System.out.println("CA pool created successfully: " + poolId);
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def create_ca_pool(project_id: str, location: str, ca_pool_name: str) -> None:
        """
        Create a Certificate Authority pool. All certificates created under this CA pool will
        follow the same issuance policy, IAM policies,etc.,
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: a unique name for the ca pool.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        ca_pool = privateca_v1.CaPool(
            # Set the tier (see: https://cloud.google.com/certificate-authority-service/docs/tiers).
            tier=privateca_v1.CaPool.Tier.ENTERPRISE,
        )
        location_path = caServiceClient.common_location_path(project_id, location)
    
        # Create the pool request.
        request = privateca_v1.CreateCaPoolRequest(
            parent=location_path,
            ca_pool_id=ca_pool_name,
            ca_pool=ca_pool,
        )
    
        # Create the CA pool.
        operation = caServiceClient.create_ca_pool(request=request)
    
        print("Operation result:", operation.result())
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_privateca_ca_pool" "default" {
      name     = "ca-pool"
      location = "us-central1"
      tier     = "ENTERPRISE"
      publishing_options {
        publish_ca_cert = true
        publish_crl     = true
      }
      labels = {
        foo = "bar"
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
