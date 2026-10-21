---
url: https://docs.cloud.google.com/certificate-authority-service/docs/view-issued-certificates/
title: View issued certificates \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:35.825517+00:00
---

# View issued certificates  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/view-issued-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View issued certificates

This page explains how you can view the issued certificates using the Google Cloud console, Google Cloud CLI, and Cloud Client Libraries.

You can only view certificates issued by [Enterprise tier](https://docs.cloud.google.com/certificate-authority-service/docs/tiers) CAs.

### View issued certificates

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **CA manager** tab.

  3. On the **Certificate authorities** page, click the name of the CA.

  4. At the bottom of the **Certificate authority** details page, click **View issued certificates** to view the list of certificates issued by the CA.

A list of certificates appear on the **All certificates** page. The details displayed include the status of the certificate, issuing CA, the CA pool that contains the CA, the certificate's expiration date, and more.




### gcloud

To list all certificates issued by a particular CA in a CA pool, use the following `gcloud` command:
    
    
    gcloud privateca certificates list --issuer-pool ISSUER_POOL --issuer-location ISSUER_LOCATION --ca CA_NAME
    

For more information about the `gcloud privateca certificates list` command, see [gcloud privateca certificates list](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/list).

To list all certificates across all CAs in a given location, use the following `gcloud` command:
    
    
    gcloud privateca certificates list --location LOCATION
    

**Note:** Google Cloud CLI does not support cross-region listing for certificates. Use the Google Cloud console to view all the certificates in the project.

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
    
    // List Certificates present in the given CA pool.
    func listCertificates(
    	w io.Writer,
    	projectId string,
    	location string,
    	caPoolId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"		// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"			// The CA Pool id in which the certificate exists.
    
    	ctx := context.Background()
    	caClient, err := privateca.NewCertificateAuthorityClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.Close()
    
    	fullCaName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s", projectId, location, caPoolId)
    
    	// Create the ListCertificatesRequest.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#ListCertificatesRequest.
    	req := &privatecapb.ListCertificatesRequest{Parent: fullCaName}
    
    	it := caClient.ListCertificates(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("unable to get the list of cerficates: %w", err)
    		}
    
    		fmt.Fprintf(w, " - %s (common name: %s)", resp.Name,
    			resp.CertificateDescription.SubjectDescription.Subject.CommonName)
    	}
    
    	return nil
    }
    

###  Java 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.security.privateca.v1.[CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html);
    import com.google.cloud.security.privateca.v1.[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import java.io.IOException;
    
    public class ListCertificates {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Id of the CA pool which contains the certificates to be listed.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        listCertificates(project, location, poolId);
      }
    
      // List Certificates present in the given CA pool.
      public static void listCertificates(String project, String location, String poolId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          [CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html) caPool =
              [CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html).newBuilder()
                  .setProject(project)
                  .setLocation(location)
                  .setCaPool(poolId)
                  .build();
    
          // Retrieve and print the certificate names.
          System.out.println("Available certificates: ");
          for ([Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html) certificate :
              certificateAuthorityServiceClient.listCertificates(caPool).iterateAll()) {
            System.out.println(certificate.getName());
          }
        }
      }
    }

###  Python 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def list_certificates(
        project_id: str,
        location: str,
        ca_pool_name: str,
    ) -> None:
        """
        List Certificates present in the given CA pool.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: name of the CA pool which contains the certificates to be listed.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        ca_pool_path = caServiceClient.ca_pool_path(project_id, location, ca_pool_name)
    
        # Retrieve and print the certificate names.
        print(f"Available certificates in CA pool {ca_pool_name}:")
        for certificate in caServiceClient.list_certificates(parent=ca_pool_path):
            print(certificate.name)
    
    

### View all the certificates issued in your project

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **Private certificate manager** tab.

A list of certificates appear on the **All certificates** page.

The details displayed include the status of the certificate, issuing CA, the CA pool that contains the CA, the certificate's expiration date, and more. You can filter the certificates using any of the parameters.




### View details for a single certificate

### Console

  1. In the Google Cloud console, go to the **Certificate Authority Service** page.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Pick your target CA under the **CA Manager** tab.

  3. Click the CA name.

  4. At the bottom of the **Certificate authority** details page, click **View issued certificates** to see the list of issued certificates.

  5. Click more_vert in the **Actions** column for the certificate you want to download.

  6. Under **Download** , click **Certificate**. You can download the _certificate chain_ by clicking **Certificate chain**.




### gcloud

To see the full description of a certificate, run the following command:
    
    
    gcloud privateca certificates describe CERT_NAME --issuer-pool POOL_ID --issuer-location ISSUER_LOCATION
    

For more information about the `gcloud privateca certificates describe` command, see [gcloud privateca certificates describe](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe).

To export the PEM-encoded X.509 certificate chain and to a file, run the following command:
    
    
    gcloud privateca certificates export CERT_NAME \
        --issuer-pool POOL_ID \
        --issuer-location ISSUER_LOCATION \
        --include-chain \
        --output-file certificate-file
    

For more information about the `gcloud privateca certificates export` command, see [gcloud privateca certificates export](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/export).

**Note:** You may omit `---include-chain` to export only the leaf certificate.

## List certificates across all CA pools

To list all certificates across all CA pools for a given project `PROJECT_ID` and location `LOCATION` when calling the API, specify the CA resource name with a wildcard `-`.

Example: `projects/PROJECT_ID/locations/LOCATION/caPools/-`

## Proof-of-possession for certificates

Proof-of-possession of the private key ensures that the requester of a certificate holds the private key for that certificate. CA Service checks proof-of-possession only if the requester provides a PKCS #10 CSR according to [RFC 2986](https://tools.ietf.org/html/rfc2986). Proof-of-possession for other forms of certificate requests, such as requests by [CertificateConfig](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/CertificateConfig) is not enforced.

It is the responsibility of client applications that accept certificates to validate whether the certificate holder possesses the private key of that certificate. Enforcing proof-of-possession checks during certificate issuance is a form of defense-in-depth to protect against misbehaving clients. The existence of such clients, regardless of whether the CA checks proof-of-possession, could constitute a security vulnerability.

## What's next

  * Learn how to [revoke certificates](https://docs.cloud.google.com/certificate-authority-service/docs/revoking-certificates).
  * Learn how to [sort and filter certificates](https://docs.cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
