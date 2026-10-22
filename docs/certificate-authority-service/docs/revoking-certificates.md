---
url: https://docs.cloud.google.com/certificate-authority-service/docs/revoking-certificates/
title: Revoke certificates \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:25.739892+00:00
---

# Revoke certificates  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/revoking-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Revoke certificates

This page explains how to revoke certificates.

Certificate Authority Service supports certificate revocation by periodically publishing Certificate Revocation Lists (CRLs). You can only revoke certificates issued by CA pools in the Enterprise tier.

**Note:** While CA Service does support publishing CRLs in the Enterprise tier, effective revocation requires client applications to periodically download those CRLs and reject certificates whose serial numbers appear in them.

## Before you begin

Make sure you have the Certificate Authority Service Operation Manager (`roles/privateca.caManager`) or the CA Service Admin (`roles/privateca.admin`) Identity and Access Management (IAM) role. For more information about the predefined IAM roles for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).

For information about granting an IAM role, see [Granting a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

## Enable CRL publication

To revoke the certificates issued by a CA pool, you must enable CRL publication on the CA pool. You can enable CRL publication while creating a CA pool. If initially disabled, you can enable CRL publication later.

After you enable CRL publication, a new CRL is published daily and is valid for 7 days. A new CRL is also published within 15 minutes of any new certificate revocation.

Certificates contain a CRL Distribution Point (CDP) extension that specifies where the CRL information for the certificate can be found. By default, when you enable CRL publication, CA Service populates the CDP extension for all certificates that are issued by the CA with the [Cloud Storage publishing location](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificateAuthorities#AccessUrls.FIELDS.crl_access_urls) that the CA uses. To set your own links to appear in this certificate extension, set the [UserDefinedAccessUrls](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificateAuthorities#userdefinedaccessurls). To keep the default Cloud Storage publishing location link and also add your own links, add the Cloud Storage link to the list of links that you specify.

**Caution:** Any certificates issued while CRL publication was disabled don't have the necessary extension to perform revocation checks. We recommend that you ensure CRL publication is enabled **before** issuing any long-lived certificates.

To enable CRL publication on a CA pool, do the following:

### Console

  1. Go to the **Certificate Authority Service** page in the Google Cloud console.

[Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **CA Pool Manager** tab.

  3. Click the CA pool that you want to edit or click the CA pool that has the CA that you want to edit.

  4. On the **CA pool** page, click  edit 

**Edit**.

  5. Click **Next** until you get to the **Configure publishing options** section.

  6. Click the **Publish CRL to GCS bucket for CAs in this pool** toggle.

**Note:** Toggling this switch enables CRL publication for **all CAs** that are part of the CA pool in which your CA resides.



### gcloud

Run the following command:
    
    
    gcloud privateca pools update POOL_ID --location LOCATION --publish-crl
    

Replace the following:

  * POOL_ID: the name of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).



For more information about the `gcloud privateca pools update` command, see [gcloud privateca pools update](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/update).

CA Service enforces a limit of 500,000 unexpired revoked certificates per CRL.

Only the last 100 CRLs in chronological order are retained as [CertificateRevocationList](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificateAuthorities.certificateRevocationLists#CertificateRevocationList) resources, and older CRLs are automatically deleted. Retention of older CRLs in customer-managed Cloud Storage buckets is subject to the [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) and [retention policies](https://docs.cloud.google.com/storage/docs/bucket-lock) configured by customers.  
Note that CRLs that have been deleted from CA Service can still be accessed from service-managed Cloud Storage buckets, unless the CA is deleted. CRLs are never deleted from customer-managed Cloud Storage buckets, even if the CA is deleted.

**Tip:** We recommend that client applications access CRLs from the Cloud Storage bucket instead of using CRL APIs to ensure simplicity and high availability.

## Revoke a certificate

CA Service allows revoking certificates by serial number or resource name, and also accepts an optional reason. After a certificate is revoked, its serial number and revocation reason appear in all future CRLs until the certificate reaches its expiry date. An out-of-band CRL is also generated within 15 minutes of revocation.

To revoke a certificate, use the following steps:

### Console

  1. Go to the **Certificate Authority Service** page in the Google Cloud console. 

[Go to Certificate Authority Service ](https://console.cloud.google.com/security/cas)

  2. Click the **Private certificate manager** tab. 
  3. In the list of certificates, click more_vert**View more** in the row of the certificate you want to delete. 
  4. Click **Revoke**. 
  5. In the dialog that opens, click **Confirm**. 

**Note:** Google Cloud console does not support revoking a certificate using its serial number. If you want to revoke a certificate using its serial number, use the Google Cloud CLI.

### gcloud

  * To revoke a certificate using its resource name, run the following command:
        
        gcloud privateca certificates revoke \
            --certificate CERT_ID \
            --issuer-pool POOL_ID \
            --issuer-location ISSUER_LOCATION \
            --reason REVOCATION_REASON
        

Replace the following:

    * CERT_ID: the unique identifier of the certificate that you want to revoke
    * POOL_ID: the name of the CA pool that issued the certificate
    * ISSUER_LOCATION: the location of the issuing CA pool
    * REVOCATION_REASON: the reason for revoking the certificate

The `--reason` flag is optional. For more information about this flag, see [\--reason](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke#--reason), or use the following `gcloud` command with the `--help` flag:
    
    gcloud privateca certificates revoke **--help**
    

For more information about the `gcloud privateca certificates revoke` command, see [gcloud privateca certificates revoke](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke).

  * To revoke a certificate using its serial number, run the following command:
        
        gcloud privateca certificates revoke \
            --serial-number SERIAL_NUMBER \
            --issuer-pool POOL_ID \
            --issuer-location ISSUER_LOCATION \
            --reason REVOCATION_REASON
        

Replace the following:

    * SERIAL_NUMBER: the serial number of the certificate
    * POOL_ID: the name of the CA pool that issued the certificate
    * ISSUER_LOCATION: the location of the issuing CA pool
    * REVOCATION_REASON: the reason for revoking the certificate

For more information about the `gcloud privateca certificates revoke` command, see [gcloud privateca certificates revoke](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke).

When prompted to confirm, you can do so by entering 'Y':
    
    You are about to revoke Certificate [projects/PROJECT_ID/locations/CA_POOL_REGION/caPools/POOL_ID/certificates/CERT_ID]
    
    Do you want to continue? (Y/n) Y
    Revoked certificate [projects/PROJECT_ID/locations/CA_POOL_REGION/caPools/POOL_ID/certificates/CERT_ID] at DATE_TIME.
    
    




###  Go 

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
    

###  Java 

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

###  Python 

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
    
    

**Note:** CRLs are scheduled to be recreated on a daily basis. However, revoking a certificate will cause a new CRL to be created within 15 minutes. If CRL recreation becomes necessary before the next day, issue a dummy certificate and then revoke it to force the CRL recreation process.

## What's next

  * Learn how to [sort and filter certificates](https://docs.cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates).
  * Learn how to [implement a delegated OCSP responder](https://docs.cloud.google.com/certificate-authority-service/docs/ocsp-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
