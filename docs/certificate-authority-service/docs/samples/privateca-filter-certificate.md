---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-filter-certificate/
title: Filter certificates \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:27.875471+00:00
---

# Filter certificates  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-filter-certificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Filter certificates Stay organized with collections  Save and categorize content based on your preferences. 

Filter certificates based on a condition.

## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.security.privateca.v1.[CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html);
    import com.google.cloud.security.privateca.v1.[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[ListCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificatesRequest.html);
    import java.io.IOException;
    
    public class FilterCertificates {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Id of the CA pool which contains the certificates to be listed.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
    
        filterCertificates(project, location, poolId);
      }
    
      // Filter certificates based on a condition and list them.
      public static void filterCertificates(String project, String location, String poolId)
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
    
          // Create the certificate request and set the filter condition.
          [ListCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificatesRequest.html) listCertificatesRequest =
              [ListCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificatesRequest.html).newBuilder()
                  .setParent(caPool.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html#com_google_cloud_security_privateca_v1_CaPoolName_toString__)())
                  /* Filter certificates based on the given condition.
                  For more info on conditions supported,
                  see:
                  https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#filtering_support
                  Few examples for constructing conditions:
                  certificate_description.subject_description.not_after_time=
                      timestamp(com.google.protobuf)
                  certificate_description.subject_description.subject_alt_name.dns_names:my-dns
                  Here, we are filtering certificates which has organization name = csr-org-name */
                  .setFilter(
                      "certificate_description.subject_description.subject.organization=csr-org-name")
                  .build();
    
          // Retrieve and print the certificate names.
          System.out.println("Available certificates: ");
          for ([Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate.html) certificate :
              certificateAuthorityServiceClient
                  .listCertificates(listCertificatesRequest)
                  .iterateAll()) {
            System.out.println(certificate.getName());
          }
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def filter_certificates(
        project_id: str, location: str, ca_pool_name: str, filter_condition: str
    ) -> None:
        """
        Filter certificates based on a condition and list them.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: name of the CA pool which contains the certificates to be listed.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        ca_pool_path = caServiceClient.ca_pool_path(project_id, location, ca_pool_name)
    
        # Create the certificate request and set the filter condition.
        request = privateca_v1.ListCertificatesRequest(
            parent=ca_pool_path,
            filter=filter_condition,
        )
    
        # Retrieve and print the certificate names.
        print("Available certificates: ")
        for cert in caServiceClient.list_certificates(request=request):
            print(f"- {cert.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
