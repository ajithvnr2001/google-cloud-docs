---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-set-issuance-policy/
title: Set/ Update Issuance Policy \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:59.095573+00:00
---

# Set/ Update Issuance Policy  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-set-issuance-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Set/ Update Issuance Policy Stay organized with collections  Save and categorize content based on your preferences. 

Set/ Update the issuance policy for a CA pool. All certificates issued from this CA pool should meet the issuance policy.

## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html);
    import com.google.cloud.security.privateca.v1.[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html).[IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.html);
    import com.google.cloud.security.privateca.v1.[CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html);
    import com.google.cloud.security.privateca.v1.[UpdateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCaPoolRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.type.[Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateCaPoolIssuancePolicy {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: The CA pool for which the issuance policy is to be updated.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
    
        updateCaPoolIssuancePolicy(project, location, poolId);
      }
    
      /* Update the Issuance policy for a CA Pool. All certificates issued from this CA Pool should
      meet the issuance policy. */
      public static void updateCaPoolIssuancePolicy(String project, String location, String poolId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
        once, and can be reused for multiple requests. After completing all of your requests, call
        the `certificateAuthorityServiceClient.close()` method on the client to safely
        clean up any remaining background resources. */
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          /* Set the updated issuance policy for the CA Pool.
          This particular issuance policy allows only SANs that
          have DNS Names as "us.google.org" or ending in ".google.com". */
          String expr =
              "subject_alt_names.all(san, san.type == DNS && (san.value == \"dns.example.com\""
                  + " || san.value.endsWith(\".example.com\")) )";
    
          [CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html).[IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.html) issuancePolicy =
              [IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.html).newBuilder()
                  .setIdentityConstraints(
                      [CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.html).newBuilder()
                          .[setAllowSubjectPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setAllowSubjectPassthrough_boolean_)(true)
                          .[setAllowSubjectAltNamesPassthrough](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setAllowSubjectAltNamesPassthrough_boolean_)(true)
                          .[setCelExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder.html#com_google_cloud_security_privateca_v1_CertificateIdentityConstraints_Builder_setCelExpression_com_google_type_Expr_)([Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html).newBuilder().[setExpression](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.Builder.html#com_google_type_Expr_Builder_setExpression_java_lang_String_)(expr).build())
                          .build())
                  .build();
    
          [CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html) caPool =
              [CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.html).newBuilder()
                  .setName([CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html).of(project, location, poolId).toString())
                  .[setIssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.Builder.html#com_google_cloud_security_privateca_v1_CaPool_Builder_setIssuancePolicy_com_google_cloud_security_privateca_v1_CaPool_IssuancePolicy_)(issuancePolicy)
                  .build();
    
          /* 1. Set the CA pool with updated values.
          2. Set the update mask to specify which properties of the CA Pool should be updated.
          Only the properties specified in the mask will be updated. Make sure that the mask fields
          match the updated issuance policy.
          For more info on constructing path for update mask, see:
          https://cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancepolicy */
          [UpdateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCaPoolRequest.html) updateCaPoolRequest =
              [UpdateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCaPoolRequest.html).newBuilder()
                  .setCaPool(caPool)
                  .setUpdateMask(
                      [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder(
                          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                              .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)(
                                  "issuance_policy.identity_constraints.allow_subject_passthrough")
                              .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)(
                                  "issuance_policy.identity_constraints."
                                      + "allow_subject_alt_names_passthrough")
                              .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("issuance_policy.identity_constraints.cel_expression")
                              .build()))
                  .build();
    
          // Update CA Pool request.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient.[updateCaPoolCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_updateCaPoolCallable__)().futureCall(updateCaPoolRequest);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) operation = futureCall.get(60, TimeUnit.SECONDS);
    
          // Check for errors.
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error in updating CA Pool Issuance policy ! " + operation.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          // Get the CA Pool's issuance policy and verify if the fields have been successfully updated.
          [IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.html) response =
              certificateAuthorityServiceClient
                  .getCaPool([CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html).of(project, location, poolId).toString())
                  .getIssuancePolicy();
    
          // Similarly, you can check for other modified fields as well.
          if (response.getIdentityConstraints().getAllowSubjectPassthrough()
              && response.getIdentityConstraints().getAllowSubjectAltNamesPassthrough()) {
            System.out.println("CA Pool Issuance policy has been updated successfully ! ");
            return;
          }
    
          System.out.println(
              "Error in updating CA Pool Issuance policy ! Please try again ! " + response);
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    from google.protobuf import field_mask_pb2
    from google.type import expr_pb2
    
    
    def update_ca_pool_issuance_policy(
        project_id: str,
        location: str,
        ca_pool_name: str,
    ) -> None:
        """
        Update the issuance policy for a CA Pool. All certificates issued from this CA Pool should
        meet the issuance policy
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: a unique name for the ca pool.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        ca_pool_path = caServiceClient.ca_pool_path(project_id, location, ca_pool_name)
    
        # Set the updated issuance policy for the CA Pool.
        # This particular issuance policy allows only SANs that
        # have DNS Names as "us.google.org" or ending in ".google.com". */
        expr = expr_pb2.Expr(
            expression='subject_alt_names.all(san, san.type == DNS && (san.value == "us.google.org" || san.value.endsWith(".google.com")) )'
        )
    
        issuance_policy = privateca_v1.CaPool.IssuancePolicy(
            identity_constraints=privateca_v1.CertificateIdentityConstraints(
                allow_subject_passthrough=True,
                allow_subject_alt_names_passthrough=True,
                cel_expression=expr,
            ),
        )
    
        ca_pool = privateca_v1.CaPool(
            name=ca_pool_path,
            issuance_policy=issuance_policy,
        )
    
        # 1. Set the CA pool with updated values.
        # 2. Set the update mask to specify which properties of the CA Pool should be updated.
        # Only the properties specified in the mask will be updated. Make sure that the mask fields
        # match the updated issuance policy.
        # For more info on constructing path for update mask, see:
        # https://cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancepolicy */
        request = privateca_v1.UpdateCaPoolRequest(
            ca_pool=ca_pool,
            update_mask=field_mask_pb2.FieldMask(
                paths=[
                    "issuance_policy.identity_constraints.allow_subject_alt_names_passthrough",
                    "issuance_policy.identity_constraints.allow_subject_passthrough",
                    "issuance_policy.identity_constraints.cel_expression",
                ],
            ),
        )
        operation = caServiceClient.update_ca_pool(request=request)
        result = operation.result()
    
        print("Operation result", result)
    
        # Get the CA Pool's issuance policy and verify if the fields have been successfully updated.
        issuance_policy = caServiceClient.get_ca_pool(name=ca_pool_path).issuance_policy
    
        # Similarly, you can check for other modified fields as well.
        if (
            issuance_policy.identity_constraints.allow_subject_passthrough
            and issuance_policy.identity_constraints.allow_subject_alt_names_passthrough
        ):
            print("CA Pool Issuance policy has been updated successfully!")
            return
    
        print("Error in updating CA Pool Issuance policy! Please try again!")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
