---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-list-ca-pool/
title: List CA pool \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:00.386743+00:00
---

# List CA pool  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-list-ca-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  List CA pool Stay organized with collections  Save and categorize content based on your preferences. 

List all CA pools in the given project and location.

## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.security.privateca.v1.[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.LocationName.html);
    import java.io.IOException;
    
    public class ListCaPools {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        String project = "your-project-id";
        String location = "ca-location";
        listCaPools(project, location);
      }
    
      // List all CA pools present in the given project and location.
      public static void listCaPools(String project, String location) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          // Set the Location Name which contains project and location of the pool.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.LocationName.html) locationName =
              [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.LocationName.html).newBuilder().setProject(project).setLocation(location).build();
    
          String caPoolName = "";
          System.out.println("Available CA pools: ");
    
          // List the CA pools.
          for ([CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html) caPool :
              certificateAuthorityServiceClient.listCaPools(locationName).iterateAll()) {
            caPoolName = caPool.getName();
            // caPoolName represents the full resource name of the
            // format 'projects/{project-id}/locations/{location}/ca-pools/{ca-pool-id}'.
            // Hence stripping it down to just CA pool id.
            System.out.println(
                caPoolName.substring(caPoolName.lastIndexOf("/") + 1) + " " + caPool.isInitialized());
          }
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def list_ca_pools(project_id: str, location: str) -> None:
        """
        List all CA pools present in the given project and location.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        location_path = caServiceClient.common_location_path(project_id, location)
    
        request = privateca_v1.ListCaPoolsRequest(parent=location_path)
    
        print("Available CA pools:")
    
        for ca_pool in caServiceClient.list_ca_pools(request=request):
            ca_pool_name = ca_pool.name
            # ca_pool.name represents the full resource name of the
            # format 'projects/{project-id}/locations/{location}/ca-pools/{ca-pool-name}'.
            # Hence stripping it down to just pool name.
            print(caServiceClient.parse_ca_pool_path(ca_pool_name)["ca_pool"])
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
