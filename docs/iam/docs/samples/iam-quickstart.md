---
url: https://docs.cloud.google.com/iam/docs/samples/iam-quickstart/
title: Quickstart \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:00.450126+00:00
---

# Quickstart  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates basic usage of IAM.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Write an allow policy by using client libraries](https://docs.cloud.google.com/iam/docs/write-policy-client-libraries)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/iam/admin/v1/iam_client.h"
    #include "google/cloud/project.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <project-id>\n";
        return 1;
      }
    
      // Create a namespace alias to make the code easier to read.
      namespace iam = ::google::cloud::iam_admin_v1;
      iam::IAMClient client(iam::MakeIAMConnection());
      auto const project = google::cloud::Project(argv[1]);
      std::cout << "Service Accounts for project: " << project.project_id() << "\n";
      int count = 0;
      for (auto sa : client.ListServiceAccounts(project.FullName())) {
        if (!sa) throw std::move(sa).status();
        std::cout << sa->name() << "\n";
        ++count;
      }
      if (count == 0) std::cout << "No Service Accounts found.\n";
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    using Google.Apis.Iam.v1;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    
    public class QuickStart
    {
        public static void Main(string[] args)
        {
            // TODO: Replace with your project ID
            var projectId = "your-project";
            // TODO: Replace with the ID of your principal.
            // For examples, see https://cloud.google.com/iam/docs/principal-identifiers
            var member = "your-principal";
            // Role to be granted
            var role = "roles/logging.logWriter";
    
            // Initialize service
            CloudResourceManagerService crmService = InitializeService();
    
            // Grant your principal the "Log Writer" role for your project
            AddBinding(crmService, projectId, member, role);
    
            // Get the project's policy and print all principals with the the "Log Writer" role
            var policy = GetPolicy(crmService, projectId);
            var binding = policy.Bindings.FirstOrDefault(x => x.Role == role);
            Console.WriteLine("Role: " + binding.Role);
            Console.Write("Members: ");
            foreach (var m in binding.Members)
            {
                Console.Write("[" + m + "] ");
            }
            Console.WriteLine();
    
            // Remove principal from the "Log Writer" role
            RemoveMember(crmService, projectId, member, role);
        }
    
        public static CloudResourceManagerService InitializeService()
        {
            // Get credentials
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
    
            // Create the Cloud Resource Manager service object
            CloudResourceManagerService crmService = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            return crmService;
        }
    
        public static Policy GetPolicy(CloudResourceManagerService crmService, String projectId)
        {
            // Get the project's policy by calling the
            // Cloud Resource Manager Projects API
            var policy = crmService.Projects.GetIamPolicy(
                new GetIamPolicyRequest(),
                projectId).Execute();
            return policy;
        }
    
        public static void SetPolicy(CloudResourceManagerService crmService, String projectId, Policy policy)
        {
            // Set the project's policy by calling the
            // Cloud Resource Manager Projects API
            crmService.Projects.SetIamPolicy(
               new SetIamPolicyRequest
               {
                   Policy = policy
               }, projectId).Execute();
        }
    
        public static void AddBinding(
            CloudResourceManagerService crmService,
            string projectId,
            string member,
            string role)
        {
            // Get the project's policy
            var policy = GetPolicy(crmService, projectId);
    
            // Find binding in policy
            var binding = policy.Bindings.FirstOrDefault(x => x.Role == role);
    
            // If binding already exists, add principal to binding
            if (binding != null)
            {
                binding.Members.Add(member);
            }
            // If binding does not exist, add binding to policy
            else
            {
                binding = new Binding
                {
                    Role = role,
                    Members = new List<string> { member }
                };
                policy.Bindings.Add(binding);
            }
    
            // Set the updated policy
            SetPolicy(crmService, projectId, policy);
        }
    
        public static void RemoveMember(
            CloudResourceManagerService crmService,
            string projectId,
            string member,
            string role)
        {
            // Get the project's policy 
            var policy = GetPolicy(crmService, projectId);
    
            // Remove the principal from the role
            var binding = policy.Bindings.FirstOrDefault(x => x.Role == role);
            if (binding == null)
            {
                Console.WriteLine("Role does not exist in policy.");
            }
            else
            {
                if (binding.Members.Contains(member))
                {
                    binding.Members.Remove(member);
                }
                else
                {
                    Console.WriteLine("The member has not been granted this role.");
                }
    
                if (binding.Members.Count == 0)
                {
                    policy.Bindings.Remove(binding);
                }
            }
    
            // Set the updated policy
            SetPolicy(crmService, projectId, policy);
        }
    }

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"strings"
    	"time"
    
    	"google.golang.org/api/cloudresourcemanager/v1"
    )
    
    func main() {
    	// TODO: Add your project ID
    	projectID := flag.String("project_id", "", "Cloud Project ID")
    	// TODO: Add the ID of your principal.
    	// For examples, see https://cloud.google.com/iam/docs/principal-identifiers
    	member := flag.String("member_id", "", "Your principal ID")
    	flag.Parse()
    
    	// The role to be granted
    	var role string = "roles/logging.logWriter"
    
    	// Initializes the Cloud Resource Manager service
    	ctx := context.Background()
    	crmService, err := cloudresourcemanager.NewService(ctx)
    	if err != nil {
    		log.Fatalf("cloudresourcemanager.NewService: %v", err)
    	}
    
    	// Grants your principal the "Log writer" role for your project
    	addBinding(crmService, *projectID, *member, role)
    
    	// Gets the project's policy and prints all principals with the "Log Writer" role
    	policy := getPolicy(crmService, *projectID)
    	// Find the policy binding for role. Only one binding can have the role.
    	var binding *cloudresourcemanager.Binding
    	for _, b := range policy.Bindings {
    		if b.Role == role {
    			binding = b
    			break
    		}
    	}
    	fmt.Println("Role: ", binding.Role)
    	fmt.Print("Members: ", strings.Join(binding.Members, ", "))
    
    	// Removes member from the "Log writer" role
    	removeMember(crmService, *projectID, *member, role)
    
    }
    
    // addBinding adds the principal to the project's IAM policy
    func addBinding(crmService *cloudresourcemanager.Service, projectID, member, role string) {
    
    	policy := getPolicy(crmService, projectID)
    
    	// Find the policy binding for role. Only one binding can have the role.
    	var binding *cloudresourcemanager.Binding
    	for _, b := range policy.Bindings {
    		if b.Role == role {
    			binding = b
    			break
    		}
    	}
    
    	if binding != nil {
    		// If the binding exists, adds the principal to the binding
    		binding.Members = append(binding.Members, member)
    	} else {
    		// If the binding does not exist, adds a new binding to the policy
    		binding = &cloudresourcemanager.Binding{
    			Role:    role,
    			Members: []string{member},
    		}
    		policy.Bindings = append(policy.Bindings, binding)
    	}
    
    	setPolicy(crmService, projectID, policy)
    
    }
    
    // removeMember removes the principal from the project's IAM policy
    func removeMember(crmService *cloudresourcemanager.Service, projectID, member, role string) {
    
    	policy := getPolicy(crmService, projectID)
    
    	// Find the policy binding for role. Only one binding can have the role.
    	var binding *cloudresourcemanager.Binding
    	var bindingIndex int
    	for i, b := range policy.Bindings {
    		if b.Role == role {
    			binding = b
    			bindingIndex = i
    			break
    		}
    	}
    
    	// Order doesn't matter for bindings or members, so to remove, move the last item
    	// into the removed spot and shrink the slice.
    	if len(binding.Members) == 1 {
    		// If the principal is the only member in the binding, removes the binding
    		last := len(policy.Bindings) - 1
    		policy.Bindings[bindingIndex] = policy.Bindings[last]
    		policy.Bindings = policy.Bindings[:last]
    	} else {
    		// If there is more than one member in the binding, removes the principal
    		var memberIndex int
    		for i, mm := range binding.Members {
    			if mm == member {
    				memberIndex = i
    			}
    		}
    		last := len(policy.Bindings[bindingIndex].Members) - 1
    		binding.Members[memberIndex] = binding.Members[last]
    		binding.Members = binding.Members[:last]
    	}
    
    	setPolicy(crmService, projectID, policy)
    
    }
    
    // getPolicy gets the project's IAM policy
    func getPolicy(crmService *cloudresourcemanager.Service, projectID string) *cloudresourcemanager.Policy {
    
    	ctx := context.Background()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    	request := new(cloudresourcemanager.GetIamPolicyRequest)
    	policy, err := crmService.Projects.GetIamPolicy(projectID, request).Do()
    	if err != nil {
    		log.Fatalf("Projects.GetIamPolicy: %v", err)
    	}
    
    	return policy
    }
    
    // setPolicy sets the project's IAM policy
    func setPolicy(crmService *cloudresourcemanager.Service, projectID string, policy *cloudresourcemanager.Policy) {
    
    	ctx := context.Background()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    	request := new(cloudresourcemanager.SetIamPolicyRequest)
    	request.Policy = policy
    	policy, err := crmService.Projects.SetIamPolicy(projectID, request).Do()
    	if err != nil {
    		log.Fatalf("Projects.SetIamPolicy: %v", err)
    	}
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.List;
    
    public class Quickstart {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace with your project ID.
        String projectId = "your-project";
        // TODO: Replace with your service account name.
        String serviceAccount = "your-service-account";
        // TODO: Replace with the ID of your principal.
        // For examples, see https://cloud.google.com/iam/docs/principal-identifiers
        String member = "your-principal";
        // The role to be granted.
        String role = "roles/logging.logWriter";
    
        quickstart(projectId, serviceAccount, member, role);
      }
    
      // Creates new policy and adds binding.
      // Checks if changes are present and removes policy.
      public static void quickstart(String projectId, String serviceAccount,
                                    String member, String role) throws IOException {
    
        // Construct the service account email.
        // You can modify the ".iam.gserviceaccount.com" to match the name of the service account
        // to use for authentication.
        serviceAccount = serviceAccount + "@" + projectId + ".iam.gserviceaccount.com";
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
    
          // Grants your principal the "Log writer" role for your project.
          addBinding(iamClient, projectId, serviceAccount, member, role);
    
          // Get the project's policy and print all principals with the "Log Writer" role
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = getPolicy(iamClient, projectId, serviceAccount);
    
          [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null;
          List<Binding> bindings = policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)();
    
          for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : bindings) {
            if (b.getRole().equals(role)) {
              binding = b;
              break;
            }
          }
    
          System.out.println("Role: " + binding.[getRole](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getRole__)());
          System.out.print("Principals: ");
    
          for (String m : binding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)()) {
            System.out.print("[" + m + "] ");
          }
          System.out.println();
    
          // Removes principal from the "Log writer" role.
          removeMember(iamClient, projectId, serviceAccount, member, role);
        }
      }
    
      public static void addBinding([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient, String projectId, String serviceAccount,
                                    String member, String role) {
        // Gets the project's policy.
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = getPolicy(iamClient, projectId, serviceAccount);
    
        // If policy is not retrieved, return early.
        if (policy == null) {
          return;
        }
    
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).Builder updatedPolicy = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)();
    
        // Get the binding if present in the policy.
        [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null;
        for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : updatedPolicy.getBindingsList()) {
          if (b.getRole().equals(role)) {
            binding = b;
            break;
          }
        }
    
        if (binding != null) {
          // If binding already exists, adds principal to binding.
          binding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)().add(member);
        } else {
          // If binding does not exist, adds binding to policy.
          binding = [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html).newBuilder()
                  .setRole(role)
                  .[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)(member)
                  .build();
          updatedPolicy.[addBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_)(binding);
        }
    
        // Sets the updated policy.
        setPolicy(iamClient, projectId, serviceAccount, updatedPolicy.build());
      }
    
      public static void removeMember([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient, String projectId, String serviceAccount,
                                      String member, String role) {
        // Gets the project's policy.
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).Builder policy = getPolicy(iamClient, projectId, serviceAccount).toBuilder();
    
        // Removes the principal from the role.
        [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null;
        for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
          if (b.getRole().equals(role)) {
            binding = b;
            break;
          }
        }
    
        if (binding != null && binding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)().contains(member)) {
          List<String> newMemberList = new ArrayList<>(binding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)());
          newMemberList.remove(member);
    
          [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) newBinding = binding.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_toBuilder__)().[clearMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_clearMembers__)()
                  .[addAllMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addAllMembers_java_lang_Iterable_java_lang_String__)(newMemberList)
                  .build();
          List<Binding> newBindingList = new ArrayList<>(policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)());
          newBindingList.remove(binding);
    
          if (!newBinding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)().isEmpty()) {
            newBindingList.add(newBinding);
          }
    
          policy.[clearBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__)()
                  .[addAllBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__)(newBindingList);
        }
    
        // Sets the updated policy.
        setPolicy(iamClient, projectId, serviceAccount, policy.build());
      }
    
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getPolicy([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient, String projectId, String serviceAccount) {
        // Gets the project's policy by calling the
        // IAMClient API.
        [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder()
                .setResource([ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html).of(projectId, serviceAccount).toString())
                .build();
        return iamClient.[getIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html#com_google_cloud_iam_admin_v1_IAMClient_getIamPolicy__org_jspecify_annotations_Nullable_com_google_api_resourcenames_ResourceName_)(request);
      }
    
      private static void setPolicy([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient, String projectId,
                                    String serviceAccount, [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy) {
        List<String> paths = Arrays.asList("bindings", "etag");
        // Sets a project's policy.
        [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request = [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                .setResource([ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html).of(projectId, serviceAccount).toString())
                .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(policy)
                // A FieldMask specifying which fields of the policy to modify. Only
                // the fields in the mask will be modified. If no mask is provided, the
                // following default mask is used:
                // `paths: "bindings, etag"`
                .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(paths).build())
                .build();
        iamClient.[setIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html#com_google_cloud_iam_admin_v1_IAMClient_setIamPolicy__org_jspecify_annotations_Nullable_com_google_api_resourcenames_ResourceName_com_google_iam_v1_Policy_)(request);
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest)
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def quickstart(project_id: str, principal: str) -> None:
        """Demonstrates basic IAM operations.
    
        This quickstart shows how to get a project's IAM policy,
        add a principal to a role, list members of a role,
        and remove a principal from a role.
    
        Args:
            project_id: ID or number of the Google Cloud project you want to use.
            principal: The principal ID requesting the access.
        """
    
        # Role to be granted.
        role = "roles/logging.logWriter"
        crm_service = [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html)()
    
        # Grants your principal the 'Log Writer' role for the project.
        modify_policy_add_role(crm_service, project_id, role, principal)
    
        # Gets the project's policy and prints all principals with the 'Log Writer' role.
        policy = get_policy(crm_service, project_id)
        binding = next(b for b in policy.bindings if b.role == role)
        print(f"Role: {(binding.role)}")
        print("Members: ")
        for m in binding.members:
            print(f"[{m}]")
    
        # Removes the principal from the 'Log Writer' role.
        modify_policy_remove_principal(crm_service, project_id, role, principal)
    
    
    def get_policy(
        crm_service: [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html), project_id: str
    ) -> policy_pb2.Policy:
        """Gets IAM policy for a project."""
    
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        policy = crm_service.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_get_iam_policy)(request)
        return policy
    
    
    def set_policy(
        crm_service: [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html),
        project_id: str,
        policy: policy_pb2.Policy,
    ) -> None:
        """Adds a new role binding to a policy."""
    
        request = iam_policy_pb2.SetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
        request.policy.CopyFrom(policy)
    
        crm_service.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_set_iam_policy)(request)
    
    
    def modify_policy_add_role(
        crm_service: [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html),
        project_id: str,
        role: str,
        principal: str,
    ) -> None:
        """Adds a new role binding to a policy."""
    
        policy = get_policy(crm_service, project_id)
    
        for bind in policy.bindings:
            if bind.role == role:
                bind.members.append(principal)
                break
        else:
            binding = policy_pb2.Binding()
            binding.role = role
            binding.members.append(principal)
            policy.bindings.append(binding)
    
        set_policy(crm_service, project_id, policy)
    
    
    def modify_policy_remove_principal(
        crm_service: [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html),
        project_id: str,
        role: str,
        principal: str,
    ) -> None:
        """Removes a principal from a role binding."""
    
        policy = get_policy(crm_service, project_id)
    
        for bind in policy.bindings:
            if bind.role == role:
                if principal in bind.members:
                    bind.members.remove(principal)
                break
    
        set_policy(crm_service, project_id, policy)
    
    
    if __name__ == "__main__":
        # TODO: Replace with your project ID.
        project_id = "your-project-id"
        # TODO: Replace with the ID of your principal.
        # For examples, see https://cloud.google.com/iam/docs/principal-identifiers
        principal = "your-principal"
        quickstart(project_id, principal)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
