---
url: https://docs.cloud.google.com/iam/docs/samples/iam-modify-policy-add-member/
title: Add a principal to a role binding \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:43.241535+00:00
---

# Add a principal to a role binding  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-modify-policy-add-member/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Add a principal to a role binding Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates adding a principal to an existing role binding in an IAM policy.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



## Code sample

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System.Linq;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy AddMember(Policy policy, string role, string member)
        {
            var binding = policy.Bindings.First(x => x.Role == role);
            binding.Members.Add(member);
            return policy;
        }
    }
    

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"fmt"
    	"io"
    
    	"google.golang.org/api/iam/v1"
    )
    
    // addMember adds a member to a role binding.
    func addMember(w io.Writer, policy *iam.Policy, role, member string) {
    	for _, binding := range policy.Bindings {
    		if binding.Role != role {
    			continue
    		}
    		for _, m := range binding.Members {
    			if m != member {
    				continue
    			}
    			fmt.Fprintf(w, "Role %q found. Member already exists.\n", role)
    			return
    		}
    		binding.Members = append(binding.Members, member)
    		fmt.Fprintf(w, "Role %q found. Member added.\n", role)
    		return
    	}
    	fmt.Fprintf(w, "Role %q not found. Member not added.\n", role)
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.util.ArrayList;
    import java.util.List;
    
    public class AddMember {
      public static void main(String[] args) {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
        // TODO: Replace with your role.
        String role = "roles/existing-role";
        // TODO: Replace with your principal.
        // For examples, see https://cloud.google.com/iam/docs/principal-identifiers
        String member = "principal-id";
    
        addMember(policy, role, member);
      }
    
      // Adds a principal to a pre-existing role.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) addMember([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String role, String member) {
        List<Binding> newBindingsList = new ArrayList<>();
    
        for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
          if (b.getRole().equals(role)) {
            newBindingsList.add(b.toBuilder().[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)(member).build());
          } else {
            newBindingsList.add(b);
          }
        }
    
        // Update the policy to add the principal.
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)()
                .[clearBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__)()
                .[addAllBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__)(newBindingsList)
                .build();
    
        System.out.println("Added principal: " + updatedPolicy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)());
    
        return updatedPolicy;
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.iam.v1 import policy_pb2
    from snippets.get_policy import get_project_policy
    from snippets.set_policy import set_project_policy
    
    
    def modify_policy_add_principal(
        project_id: str, role: str, principal: str
    ) -> policy_pb2.Policy:
        """Add a principal to certain role in project policy.
    
        project_id: ID or number of the Google Cloud project you want to use.
        role: role to which principal need to be added.
        principal: The principal requesting access.
    
        For principal ID formats, see https://cloud.google.com/iam/docs/principal-identifiers
        """
        policy = get_project_policy(project_id)
    
        for bind in policy.bindings:
            if bind.role == role:
                bind.members.append(principal)
                break
    
        return set_project_policy(project_id, policy)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
