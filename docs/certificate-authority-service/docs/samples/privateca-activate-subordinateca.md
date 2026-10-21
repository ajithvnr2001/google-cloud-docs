---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-activate-subordinateca/
title: Activate a Subordinate Certificate Authority \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:10:31.107535+00:00
---

# Activate a Subordinate Certificate Authority  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-activate-subordinateca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Activate a Subordinate Certificate Authority Stay organized with collections  Save and categorize content based on your preferences. 

Activate an already created Subordinate Certificate Authority.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a subordinate certificate authority](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca)



## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[ActivateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ActivateCertificateAuthorityRequest.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[SubordinateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.SubordinateConfig.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    
    public class ActivateSubordinateCa {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Set a unique id for the CA pool.
        // subordinateCaName: The CA to be activated.
        // pemCaCertificate: The signed certificate, obtained by signing the CSR.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String subordinateCaName = "subordinate-certificate-authority-name";
        String pemCaCertificate =
            "-----BEGIN CERTIFICATE-----\n" + "sample-pem-certificate\n" + "-----END CERTIFICATE-----";
    
        // certificateAuthorityName: The name of the certificate authority which signed the CSR.
        // If an external CA (CA not present in Google Cloud) was used for signing,
        // then use the CA's issuerCertificateChain.
        String certificateAuthorityName = "certificate-authority-name";
    
        activateSubordinateCa(
            project, location, poolId, certificateAuthorityName, subordinateCaName, pemCaCertificate);
      }
    
      // Activate a subordinate CA.
      // *Prerequisite*: Get the CSR of the subordinate CA signed by another CA. Pass in the signed
      // certificate and (issuer CA's name or the issuer CA's Certificate chain).
      // *Post*: After activating the subordinate CA, it should be enabled before issuing certificates.
      public static void activateSubordinateCa(
          String project,
          String location,
          String poolId,
          String certificateAuthorityName,
          String subordinateCaName,
          String pemCaCertificate)
          throws ExecutionException, InterruptedException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
          // Subordinate CA parent.
          String subordinateCaParent =
              [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html).of(project, location, poolId, subordinateCaName).toString();
    
          // Construct the "Activate CA Request".
          [ActivateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ActivateCertificateAuthorityRequest.html) activateCertificateAuthorityRequest =
              [ActivateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ActivateCertificateAuthorityRequest.html).newBuilder()
                  .setName(subordinateCaParent)
                  // The signed certificate.
                  .[setPemCaCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ActivateCertificateAuthorityRequest.Builder.html#com_google_cloud_security_privateca_v1_ActivateCertificateAuthorityRequest_Builder_setPemCaCertificate_java_lang_String_)(pemCaCertificate)
                  .setSubordinateConfig(
                      [SubordinateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.SubordinateConfig.html).newBuilder()
                          // Follow one of the below methods:
    
                          // Method 1: If issuer CA is in Google Cloud, set the Certificate Authority
                          // Name.
                          .setCertificateAuthority(
                              [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html).of(
                                      project, location, poolId, certificateAuthorityName)
                                  .toString())
    
                          // Method 2: If issuer CA is external to Google Cloud, set the issuer's
                          // certificate chain.
                          // The certificate chain of the CA (which signed the CSR) from leaf to root.
                          // .setPemIssuerChain(
                          //     SubordinateConfigChain.newBuilder()
                          //         .addAllPemCertificates(issuerCertificateChain)
                          //         .build())
    
                          .build())
                  .build();
    
          // Activate the CA.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[activateCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_activateCertificateAuthorityCallable__)()
                  .futureCall(activateCertificateAuthorityRequest);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while activating the subordinate CA! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          System.out.println(
              "Subordinate Certificate Authority activated successfully ! !" + subordinateCaName);
          TimeUnit.SECONDS.sleep(3);
          // The current state will be STAGED.
          // The Subordinate CA has to be ENABLED before issuing certificates.
          System.out.println(
              "Current State: "
                  + certificateAuthorityServiceClient
                  .getCertificateAuthority(subordinateCaParent)
                  .getState());
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def activate_subordinate_ca(
        project_id: str,
        location: str,
        ca_pool_name: str,
        subordinate_ca_name: str,
        pem_ca_certificate: str,
        ca_name: str,
    ) -> None:
        """
        Activate a subordinate Certificate Authority (CA).
        *Prerequisite*: Get the Certificate Signing Resource (CSR) of the subordinate CA signed by another CA. Pass in the signed
        certificate and (issuer CA's name or the issuer CA's Certificate chain).
        *Post*: After activating the subordinate CA, it should be enabled before issuing certificates.
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: set it to the CA Pool under which the CA should be created.
            pem_ca_certificate: the signed certificate, obtained by signing the CSR.
            subordinate_ca_name: the CA to be activated.
            ca_name: The name of the certificate authority which signed the CSR.
                If an external CA (CA not present in Google Cloud) was used for signing,
                then use the CA's issuerCertificateChain.
        """
    
        ca_service_client = privateca_v1.CertificateAuthorityServiceClient()
    
        subordinate_ca_path = ca_service_client.certificate_authority_path(
            project_id, location, ca_pool_name, subordinate_ca_name
        )
        ca_path = ca_service_client.certificate_authority_path(
            project_id, location, ca_pool_name, ca_name
        )
    
        # Set CA subordinate config.
        subordinate_config = privateca_v1.SubordinateConfig(
            # Follow one of the below methods:
            # Method 1: If issuer CA is in Google Cloud, set the Certificate Authority Name.
            certificate_authority=ca_path,
            # Method 2: If issuer CA is external to Google Cloud, set the issuer's certificate chain.
            # The certificate chain of the CA (which signed the CSR) from leaf to root.
            # pem_issuer_chain=privateca_v1.SubordinateConfig.SubordinateConfigChain(
            #     pem_certificates=issuer_certificate_chain,
            # )
        )
    
        # Construct the "Activate CA Request".
        request = privateca_v1.ActivateCertificateAuthorityRequest(
            name=subordinate_ca_path,
            # The signed certificate.
            pem_ca_certificate=pem_ca_certificate,
            subordinate_config=subordinate_config,
        )
    
        # Activate the CA
        operation = ca_service_client.activate_certificate_authority(request=request)
        result = operation.result()
    
        print("Operation result:", result)
    
        # The current state will be STAGED.
        # The Subordinate CA has to be ENABLED before issuing certificates.
        print(
            f"Current state: {ca_service_client.get_certificate_authority(name=subordinate_ca_path).state}"
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
