---
url: https://docs.cloud.google.com/certificate-authority-service/docs/listing-certificate-authorities/
title: List certificate authorities \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:36.301831+00:00
---

# List certificate authorities  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/listing-certificate-authorities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# List certificate authorities

This page explains how you can list the certificate authorities (CAs) in a Google Cloud project.

## List root CAs

This section shows how to view the root CAs.

### List root CAs across CA pools

To list all the root CAs across CA pools, do the following:

### Console

  1. In the Google Cloud console, go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. In the filter_list **Filter** field, select **Type** in the list.

  3. Set the value of **Type** as **Root**.




All CAs with **Type** set as **Root** are listed.

### gcloud

Run the following command:
    
    
    gcloud privateca roots list --location LOCATION
    

Replace LOCATION with the location of the root CAs. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).

### List root CAs in a particular CA pool

To list all the root CAs in a particular CA pool, use the following instructions:

### Console

  1. Go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. In the filter_list **Filter** field, select **Type** in the list.

  3. Set the value of **Type** as **Root**.

  4. In the **Filter** field, select **Pool** in the list.

  5. Click the name of the CA pool in the list.




### gcloud

Run the following command:
    
    
    gcloud privateca roots list --pool POOL_ID --location LOCATION
    

Replace the following:

  * POOL_ID: the name of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).



To list root CAs across all CA pools and locations, omit the `--pool` and `--location` flags from the command.

For more information about the `gcloud privateca roots list` command, see [gcloud privateca roots list](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/list).

## List subordinate CAs

This section shows how to view the subordinate CAs.

### List subordinate CAs across CA pools

To list all the subordinate CAs across CA pools, do the following:

### Console

  1. Go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. In the filter_list **Filter** field, select **Type** in the list.

  3. Set the value of **Type** as **Subordinate**.




All CAs with **Type** set as **Subordinate** are listed.

### gcloud

Run the following command:
    
    
    gcloud privateca subordinates list --location LOCATION
    

Replace LOCATION with the location of the subordinate CAs. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).

### List subordinate CAs in a particular CA pool

To list all the subordinate CAs in a particular CA pool, do the following:

### Console

  1. Go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. In the filter_list **Filter** field, select **Type** in the list.

  3. Set the value of **Type** as **Subordinate**.

  4. In the filter_list **Filter** field, select **Pool** in the list.

  5. Click the name of the CA pool in the list.




### gcloud

Run the following command:
    
    
    gcloud privateca subordinates list --pool POOL_ID --location LOCATION
    

Replace the following:

  * POOL_ID: the name of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).

**Note:** You can omit the `--pool` or `--location` flags to list subordinate CAs across all CA pools or locations.

For more information about the `gcloud privateca subordinates list` command, see [gcloud privateca subordinates list](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/subordinates/list).

## List all CAs

To list all the CAs in a CA pool, use the following instructions:

### Console

  1. Go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. In the filter_list **Filter** field, select **Pool** in the list.

  3. Click the name of the CA pool in the list.




Alternatively, you can view the CAs in a particular CA pool from the **CA pool manager** page by doing the following:

  1. Click the **CA pool manager** tab.
  2. On the **CA pools** page, click the name of the CA pool whose CAs you want to view.



On the **CA pool** details page, you can see the CAs listed under **Certificate authorities in pool**. You can filter the CAs based on type, tier, location, state, and more.

###  Go 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	privateca "cloud.google.com/go/security/privateca/apiv1"
    	"cloud.google.com/go/security/privateca/apiv1/privatecapb"
    	"google.golang.org/api/iterator"
    )
    
    // List all Certificate Authorities present in the given CA Pool.
    func listCas(w io.Writer, projectId string, location string, caPoolId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"	// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"		// The id of the CA pool under which the CAs to be listed are present.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	fullCaPoolName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s", projectId, location, caPoolId)
    
    	// Create the ListCertificateAuthorities.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#ListCertificateAuthoritiesRequest.
    	req := &privatecapb.ListCertificateAuthoritiesRequest{Parent: fullCaPoolName}
    
    	it := caClient.ListCertificateAuthorities(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("unable to get the list of cerficate authorities: %w", err)
    		}
    
    		fmt.Fprintf(w, " - %s (state: %s)", resp.Name, resp.State.String())
    	}
    
    	return nil
    }
    

###  Java 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.security.privateca.v1.[CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import java.io.IOException;
    
    public class ListCertificateAuthorities {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: The id of the CA pool under which the CAs to be listed are present.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        listCertificateAuthority(project, location, poolId);
      }
    
      // List all Certificate authorities present in the given CA Pool.
      public static void listCertificateAuthority(String project, String location, String poolId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          // Create CA pool name comprising of project, location and the pool name.
          [CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html) parent =
              [CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html).newBuilder()
                  .setProject(project)
                  .setLocation(location)
                  .setCaPool(poolId)
                  .build();
    
          // List the CA name and its corresponding state.
          for ([CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html) certificateAuthority :
              certificateAuthorityServiceClient.listCertificateAuthorities(parent).iterateAll()) {
            System.out.println(
                certificateAuthority.getName() + " is " + certificateAuthority.getState());
          }
        }
      }
    }

###  Python 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def list_certificate_authorities(
        project_id: str, location: str, ca_pool_name: str
    ) -> None:
        """
        List all Certificate authorities present in the given CA Pool.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: the name of the CA pool under which the CAs to be listed are present.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        ca_pool_path = caServiceClient.ca_pool_path(project_id, location, ca_pool_name)
    
        # List the CA name and its corresponding state.
        for ca in caServiceClient.list_certificate_authorities(parent=ca_pool_path):
            print(ca.name, "is", ca.state)
    
    

## What's next

  * Learn how to [delete CAs](https://docs.cloud.google.com/certificate-authority-service/docs/deleting-certificate-authorities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
