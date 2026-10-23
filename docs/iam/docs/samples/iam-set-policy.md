---
url: https://docs.cloud.google.com/iam/docs/samples/iam-set-policy/
title: Update a policy \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:22.510800+00:00
---

# Update a policy  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-set-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Update a policy Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates updating a policy.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)
  * [Restore a previous version of an IAM allow policy](https://docs.cloud.google.com/iam/docs/restore-iam-policy)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name) {
      iam::IAMClient client(iam::MakeIAMConnection());
      auto response =
          client.SetIamPolicy(name, [](google::iam::v1::Policy policy) {
            // change the policy, e.g., add/remove/edit a binding
            return policy;
          });
      if (!response) throw std::move(response).status();
      std::cout << "Policy successfully set: " << response->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy SetPolicy(string projectId, Policy policy)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            return service.Projects.SetIamPolicy(new SetIamPolicyRequest
            {
                Policy = policy
            }, projectId).Execute();
        }
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.admin.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class SetProjectPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
    
        setProjectPolicy(policy, projectId);
      }
    
      // Sets a project's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) setProjectPolicy([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String projectId)
              throws IOException {
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
          List<String> paths = Arrays.asList("bindings", "etag");
          [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request = [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .setResource([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId).toString())
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(policy)
                  // A FieldMask specifying which fields of the policy to modify. Only
                  // the fields in the mask will be modified. If no mask is provided, the
                  // following default mask is used:
                  // `paths: "bindings, etag"`
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(paths).build())
                  .build();
    
          return projectsClient.setIamPolicy(request);
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest)
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def set_project_policy(
        project_id: str, policy: policy_pb2.Policy, merge: bool = True
    ) -> policy_pb2.Policy:
        """
        Set policy for project. Pay attention that previous state will be completely rewritten.
        If you want to update only part of the policy follow the approach read->modify->write.
        For more details about policies check out https://cloud.google.com/iam/docs/policies
    
        project_id: ID or number of the Google Cloud project you want to use.
        policy: Policy which has to be set.
        merge: The strategy to be used forming the request. CopyFrom is clearing both mutable and immutable fields,
        when MergeFrom is replacing only immutable fields and extending mutable.
        https://googleapis.dev/python/protobuf/latest/google/protobuf/message.html#google.protobuf.message.Message.CopyFrom
        """
        client = [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html)()
    
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
        current_policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_get_iam_policy)(request)
    
        # Etag should as fresh as possible to lower chance of collisions
        policy.ClearField("etag")
        if merge:
            current_policy.MergeFrom(policy)
        else:
            current_policy.CopyFrom(policy)
    
        request = iam_policy_pb2.SetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        # request.etag field also will be merged which means you are secured from collision,
        # but it means that request may fail and you need to leverage exponential retries approach
        # to be sure policy has been updated.
        request.policy.CopyFrom(current_policy)
    
        policy = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_set_iam_policy)(request)
        return policy
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
