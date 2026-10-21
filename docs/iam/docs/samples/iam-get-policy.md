---
url: https://docs.cloud.google.com/iam/docs/samples/iam-get-policy/
title: Get an IAM policy \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:20.942313+00:00
---

# Get an IAM policy  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-get-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Get an IAM policy Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates retrieving an IAM policy.

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
      auto response = client.GetIamPolicy(name);
      if (!response) throw std::move(response).status();
      std::cout << "Policy successfully retrieved: " << response->DebugString()
                << "\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy GetPolicy(string projectId)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            var policy = service.Projects.GetIamPolicy(new GetIamPolicyRequest(),
                projectId).Execute();
            return policy;
        }
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.admin.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class GetProjectPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
    
        getProjectPolicy(projectId);
      }
    
      // Gets a project's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getProjectPolicy(String projectId) throws IOException {
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
          [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder()
                  .setResource([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId).toString())
                  .build();
          return projectsClient.getIamPolicy(request);
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import resourcemanager_v3
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def get_project_policy(project_id: str) -> policy_pb2.Policy:
        """Get policy for project.
    
        project_id: ID or number of the Google Cloud project you want to use.
        """
    
        client = resourcemanager_v3.ProjectsClient()
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        policy = client.get_iam_policy(request)
        print(f"Policy retrieved: {policy}")
    
        return policy

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
