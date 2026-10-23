---
url: https://docs.cloud.google.com/iam/docs/samples/iam-disable-role/
title: Disable a custom role \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:08.271594+00:00
---

# Disable a custom role  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-disable-role/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Disable a custom role Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates disabling a custom role.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles)



## Code sample

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html);
    import com.google.iam.admin.v1.[UpdateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class DisableRole {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // Role ID must point to an existing role.
        String projectId = "your-project-id";
        String roleId = "testRole";
    
        [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) role = disableRole(projectId, roleId);
        System.out.println("Role name: " + role.[getName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html#com_google_iam_admin_v1_Role_getName__)());
        System.out.println("Role stage: " + role.[getStage](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html#com_google_iam_admin_v1_Role_getStage__)());
      }
    
      public static [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) disableRole(String projectId, String roleId)
              throws IOException {
        String roleName = "projects/" + projectId + "/roles/" + roleId;
        [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) role = [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).newBuilder()
                        .setName(roleName)
                        .setStage([Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).RoleLaunchStage.DISABLED)
                        .build();
    
        [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("stage").build();
        [UpdateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html) updateRoleRequest =
                  [UpdateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html).newBuilder()
                          .setName(roleName)
                          .setRole(role)
                          .setUpdateMask(fieldMask)
                          .build();
    
        // Initialize client for sending requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          return iamClient.updateRole(updateRoleRequest);
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.iam_admin_v1 import [GetRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetRoleRequest.html), [IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html), [Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html), [UpdateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UpdateRoleRequest.html)
    
    
    def disable_role(project_id: str, role_id: str) -> Role:
        """Disables an IAM role in a GCP project.
    
        Args:
            project_id: GCP project ID
            role_id: ID of GCP IAM role
    
        Returns: Updated google.cloud.iam_admin_v1.Role object with disabled stage
        """
        client = IAMClient()
        name = f"projects/{project_id}/roles/{role_id}"
        get_request = GetRoleRequest(name=name)
        try:
            role = client.[get_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_get_role)(get_request)
            role.stage = [Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html).[RoleLaunchStage](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.RoleLaunchStage.html).DISABLED
            update_request = UpdateRoleRequest(name=role.name, role=role)
            client.[update_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_update_role)(update_request)
            print(f"Disabled role: {role_id}: {role}")
            return role
        except NotFound as exc:
            raise NotFound(f'Role with id [{role_id}] not found, take some actions') from exc

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
