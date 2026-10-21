---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-update-ca-label/
title: Update Certificate Authority Label \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:04:29.743615+00:00
---

# Update Certificate Authority Label  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-update-ca-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Update Certificate Authority Label Stay organized with collections  Save and categorize content based on your preferences. 

Update the labels in a Certificate Authority.

## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[UpdateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateAuthorityRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateCertificateAuthority {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Set it to the CA Pool under which the CA should be created.
        // certificateAuthorityName: Unique name for the CA.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateAuthorityName = "certificate-authority-name";
    
        updateCaLabel(project, location, poolId, certificateAuthorityName);
      }
    
      // Updates the labels in a certificate authority.
      public static void updateCaLabel(
          String project, String location, String poolId, String certificateAuthorityName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
        once, and can be reused for multiple requests. After completing all of your requests, call
        the `certificateAuthorityServiceClient.close()` method on the client to safely
        clean up any remaining background resources. */
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          // Set the parent path and the new labels.
          String certificateAuthorityParent =
              [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html).of(project, location, poolId, certificateAuthorityName)
                  .toString();
          [CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html) certificateAuthority =
              [CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).newBuilder()
                  .setName(certificateAuthorityParent)
                  .putLabels("env", "test")
                  .build();
    
          // Create a request to update the CA.
          [UpdateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateAuthorityRequest.html) request =
              [UpdateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateAuthorityRequest.html).newBuilder()
                  .setCertificateAuthority(certificateAuthority)
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("labels").build())
                  .build();
    
          // Update the CA and wait for the operation to complete.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[updateCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_updateCertificateAuthorityCallable__)()
                  .futureCall(request);
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) operation = futureCall.get(60, TimeUnit.SECONDS);
    
          // Check for errors.
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error in updating labels ! " + operation.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
          }
    
          // Get the updated CA and check if it contains the new label.
          [CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html) response =
              certificateAuthorityServiceClient.getCertificateAuthority(certificateAuthorityParent);
          if (response.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html#com_google_cloud_security_privateca_v1_CertificateAuthority_getLabelsMap__)().containsKey("env")
              && response.getLabelsMap().get("env").equalsIgnoreCase("test")) {
            System.out.println("Successfully updated the labels ! ");
          }
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    from google.protobuf import field_mask_pb2
    
    
    def update_ca_label(
        project_id: str,
        location: str,
        ca_pool_name: str,
        ca_name: str,
    ) -> None:
        """
        Update the labels in a certificate authority.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: set it to the CA Pool under which the CA should be updated.
            ca_name: unique name for the CA.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        # Set the parent path and the new labels.
        ca_parent = caServiceClient.certificate_authority_path(
            project_id, location, ca_pool_name, ca_name
        )
        certificate_authority = privateca_v1.CertificateAuthority(
            name=ca_parent,
            labels={"env": "test"},
        )
    
        # Create a request to update the CA.
        request = privateca_v1.UpdateCertificateAuthorityRequest(
            certificate_authority=certificate_authority,
            update_mask=field_mask_pb2.FieldMask(paths=["labels"]),
        )
    
        operation = caServiceClient.update_certificate_authority(request=request)
        result = operation.result()
    
        print("Operation result:", result)
    
        # Get the updated CA and check if it contains the new label.
    
        certificate_authority = caServiceClient.get_certificate_authority(name=ca_parent)
    
        if (
            "env" in certificate_authority.labels
            and certificate_authority.labels["env"] == "test"
        ):
            print("Successfully updated the labels !")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
