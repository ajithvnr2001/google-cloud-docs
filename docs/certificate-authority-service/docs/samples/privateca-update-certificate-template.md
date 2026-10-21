---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-update-certificate-template/
title: Update a Certificate template \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:29.813686+00:00
---

# Update a Certificate template  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-update-certificate-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Update a Certificate template Stay organized with collections  Save and categorize content based on your preferences. 

Update an existing Certificate template.

## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html);
    import com.google.cloud.security.privateca.v1.[CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate.html);
    import com.google.cloud.security.privateca.v1.[CertificateTemplateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplateName.html);
    import com.google.cloud.security.privateca.v1.[UpdateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateCertificateTemplate {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // certificateTemplateId: Id of the certificate template to update.
        String project = "your-project-id";
        String location = "ca-location";
        String certificateTemplateId = "certificate-template-id";
    
        updateCertificateTemplate(project, location, certificateTemplateId);
      }
    
      // Updates an existing certificate template.
      public static void updateCertificateTemplate(
          String project, String location, String certificateTemplateId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
        once, and can be reused for multiple requests. After completing all of your requests, call
        the `certificateAuthorityServiceClient.close()` method on the client to safely
        clean up any remaining background resources. */
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          String certificateTemplateName =
              [CertificateTemplateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplateName.html).of(project, location, certificateTemplateId).toString();
    
          // Set the parent name and the properties to be updated.
          [CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate.html) certificateTemplate =
              [CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate.html).newBuilder()
                  .setName(certificateTemplateName)
                  .setIdentityConstraints(
                      [CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html).newBuilder()
                          .[setAllowSubjectPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setAllowSubjectPassthrough_boolean_)(false)
                          .[setAllowSubjectAltNamesPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setAllowSubjectAltNamesPassthrough_boolean_)(true)
                          .build())
                  .build();
    
          // Set the mask corresponding to the properties updated above.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("identity_constraints.allow_subject_alt_names_passthrough")
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("identity_constraints.allow_subject_passthrough")
                  .build();
    
          /* Set the new template.
          Set the mask to specify which properties of the template should be updated. */
          [UpdateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest.html) request =
              [UpdateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest.html).newBuilder()
                  .setCertificateTemplate(certificateTemplate)
                  .setUpdateMask(fieldMask)
                  .build();
    
          // Create the update certificate template request.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient.[updateCertificateTemplateCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_updateCertificateTemplateCallable__)().futureCall(request);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get(60, TimeUnit.SECONDS);
    
          // Check for errors.
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error in updating certificate template ! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          // Get the updated certificate template and check if the properties have been updated.
          [CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html) updatedCertificateIdentityConstraints =
              certificateAuthorityServiceClient
                  .getCertificateTemplate(certificateTemplateName)
                  .getIdentityConstraints();
    
          if (!updatedCertificateIdentityConstraints.[getAllowSubjectPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_getAllowSubjectPassthrough__)()
              && updatedCertificateIdentityConstraints.getAllowSubjectAltNamesPassthrough()) {
            System.out.println("Successfully updated the certificate template ! " + response.[getName](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getName__)());
            return;
          }
    
          System.out.println("Error in updating certificate template ! ");
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    from google.protobuf import field_mask_pb2
    
    
    def update_certificate_template(
        project_id: str,
        location: str,
        certificate_template_id: str,
    ) -> None:
        """
        Update an existing certificate template.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            certificate_template_id: set a unique name for the certificate template.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        certificate_name = caServiceClient.certificate_template_path(
            project_id,
            location,
            certificate_template_id,
        )
    
        # Set the parent name and the properties to be updated.
        certificate_template = privateca_v1.CertificateTemplate(
            name=certificate_name,
            identity_constraints=privateca_v1.CertificateIdentityConstraints(
                allow_subject_passthrough=False,
                allow_subject_alt_names_passthrough=True,
            ),
        )
    
        # Set the mask corresponding to the properties updated above.
        field_mask = field_mask_pb2.FieldMask(
            paths=[
                "identity_constraints.allow_subject_alt_names_passthrough",
                "identity_constraints.allow_subject_passthrough",
            ],
        )
    
        # Set the new template.
        # Set the mask to specify which properties of the template should be updated.
        request = privateca_v1.UpdateCertificateTemplateRequest(
            certificate_template=certificate_template,
            update_mask=field_mask,
        )
        operation = caServiceClient.update_certificate_template(request=request)
        result = operation.result()
    
        print("Operation result", result)
    
        # Get the updated certificate template and check if the properties have been updated.
        cert_identity_constraints = caServiceClient.get_certificate_template(
            name=certificate_name
        ).identity_constraints
    
        if (
            not cert_identity_constraints.allow_subject_passthrough
            and cert_identity_constraints.allow_subject_alt_names_passthrough
        ):
            print("Successfully updated the certificate template!")
            return
    
        print("Error in updating certificate template!")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
