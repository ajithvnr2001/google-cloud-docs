---
url: https://docs.cloud.google.com/iam/docs/samples/iam-modify-policy-remove-member/
title: Remove a member from a role binding \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:47.984857+00:00
---

# Remove a member from a role binding  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-modify-policy-remove-member/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Remove a member from a role binding Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates removing a member from a role binding in an IAM policy.

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
        public static Policy RemoveMember(Policy policy, string role, string member)
        {
            try
            {
                var binding = policy.Bindings.First(x => x.Role == role);
                if (binding.Members.Count != 0 && binding.Members.Contains(member))
                {
                    binding.Members.Remove(member);
                }
                if (binding.Members.Count == 0)
                {
                    policy.Bindings.Remove(binding);
                }
                return policy;
            }
            catch (System.InvalidOperationException e)
            {
                System.Diagnostics.Debug.WriteLine("Role does not exist in policy: \n" + e.ToString());
                return policy;
            }
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
    
    // removeMember removes a member from a role binding.
    func removeMember(w io.Writer, policy *iam.Policy, role, member string) {
    	bindings := policy.Bindings
    	bindingIndex, memberIndex := -1, -1
    	for bIdx := range bindings {
    		if bindings[bIdx].Role != role {
    			continue
    		}
    		bindingIndex = bIdx
    		for mIdx := range bindings[bindingIndex].Members {
    			if bindings[bindingIndex].Members[mIdx] != member {
    				continue
    			}
    			memberIndex = mIdx
    			break
    		}
    	}
    	if bindingIndex == -1 {
    		fmt.Fprintf(w, "Role %q not found. Member not removed.\n", role)
    		return
    	}
    	if memberIndex == -1 {
    		fmt.Fprintf(w, "Role %q found. Member not found.\n", role)
    		return
    	}
    
    	members := removeIdx(bindings[bindingIndex].Members, memberIndex)
    	bindings[bindingIndex].Members = members
    	if len(members) == 0 {
    		bindings = removeIdx(bindings, bindingIndex)
    		policy.Bindings = bindings
    	}
    	fmt.Fprintf(w, "Role %q found. Member removed.\n", role)
    }
    
    // removeIdx removes arr[idx] from arr.
    func removeIdx[T any](arr []T, idx int) []T {
    	return append(arr[:idx], arr[idx+1:]...)
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class RemoveMember {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
        // TODO: Replace with your role.
        String role = "roles/existing-role";
        // TODO: Replace with your principal.
        // For examples, see https://cloud.google.com/iam/docs/principal-identifiers
        String member = "principal-id";
    
        removeMember(policy, role, member);
      }
    
      // Removes principal from a role; removes binding if binding contains no members.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) removeMember([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String role, String member) {
        // Creating new builder with all values copied from origin policy
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).Builder policyBuilder = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)();
    
        // Getting binding with suitable role.
        [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null;
        for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
          if (b.getRole().equals(role)) {
            binding = b;
            break;
          }
        }
    
        if (binding != null && binding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)().contains(member)) {
          List<String> newMemberList = new ArrayList<>(binding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)());
          // Removing principal from the role
          newMemberList.remove(member);
    
          System.out.println("Member " + member + " removed from " + role);
    
          // Adding all remaining principals to create new binding
          [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) newBinding = binding.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_toBuilder__)()
                  .[clearMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_clearMembers__)()
                  .[addAllMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addAllMembers_java_lang_Iterable_java_lang_String__)(newMemberList)
                  .build();
    
          List<Binding> newBindingList = new ArrayList<>(policyBuilder.getBindingsList());
    
          // Removing old binding to replace with new one
          newBindingList.remove(binding);
    
          // If binding has no more members, binding will not be added
          if (!newBinding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)().isEmpty()) {
            newBindingList.add(newBinding);
          }
    
          // Update the policy to remove the principal.
          policyBuilder.[clearBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__)()
                  .[addAllBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__)(newBindingList);
        }
    
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policyBuilder.build();
    
        System.out.println("Exising principals: " + updatedPolicy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)());
    
        return updatedPolicy;
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.iam.v1 import policy_pb2
    from snippets.get_policy import get_project_policy
    from snippets.set_policy import set_project_policy
    
    
    def modify_policy_remove_principal(
        project_id: str, role: str, principal: str
    ) -> policy_pb2.Policy:
        """Remove a principal from certain role in project policy.
    
        project_id: ID or number of the Google Cloud project you want to use.
        role: role to revoke.
        principal: The principal to revoke access from.
    
        For principal ID formats, see https://cloud.google.com/iam/docs/principal-identifiers
        """
        policy = get_project_policy(project_id)
    
        for bind in policy.bindings:
            if bind.role == role:
                if principal in bind.members:
                    bind.members.remove(principal)
                break
    
        return set_project_policy(project_id, policy, False)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
