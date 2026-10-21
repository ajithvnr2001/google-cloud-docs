---
url: https://docs.cloud.google.com/java/docs/occ/
title: Optimistic concurrency control (OCC) \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:15.838883+00:00
---

# Optimistic concurrency control (OCC)  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/occ/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Optimistic concurrency control (OCC) Stay organized with collections  Save and categorize content based on your preferences. 

Optimistic Concurrency Control (OCC) is a strategy used to manage shared resources and prevent "lost updates" or race conditions when multiple users or processes attempt to modify the same resource simultaneously.

As an example, consider systems like Google Cloud IAM, where the shared resource is an **IAM Policy** applied to a resource (like a Project, Bucket, or Service). To implement OCC, systems typically use a version number or an `etag` (entity tag) field on the resource object.

## Introduction to OCC

Imagine two processes, A and B, try to update a shared resource at the same time:

  1. Process **A** reads the current state of the resource.

  2. Process **B** reads the _same_ current state.

  3. Process **A** modifies its copy and writes it back to the server.

  4. Process **B** modifies its copy and writes it back to the server.




Because Process **B** overwrites the resource _without_ knowing that Process **A** already changed it, Process **A** 's updates are **lost**.

OCC solves this by introducing a unique fingerprint which changes every time a entity is modified. In many systems (like IAM), this is done using an `etag`. The server checks this tag on every write:

  1. When you read the resource, the server returns an `etag` (a unique fingerprint).

  2. When you send the modified resource back, you must include the original `etag`.

  3. If the server finds that the stored `etag` does **not** match the `etag` you sent (meaning someone else modified the resource since you read it), the write operation fails with an `ABORTED` or `FAILED_PRECONDITION` error.




This failure forces the client to **retry** the entire process—re-read the _new_ state, re-apply the changes, and try the write again with the new `etag`.

## Implement the OCC Loop

The core of the OCC implementation is a `while` loop that handles the retry logic. Set a reasonable maximum number of retries to prevent infinite loops in cases of high contention.

### Steps of the Loop

**Step** | **Action** | **Implementation Example**  
---|---|---  
**Read** | Fetch the current resource state, including the `etag`. | `Policy policy = client.getIamPolicy(resourceName);`  
**Modify** | Apply the changes to the local object. | `policy = policy.toBuilder().addBinding(newBinding).build();`  
**Write/Check** | Attempt to save the modified resource using the old `etag`. This action must be inside a `try` block. | `try { client.setIamPolicy(resourceName, policy); return policy; } catch (AbortedException e) { // retry loop }`  
**Success/Retry** | If the write succeeds, exit the loop. If it fails with a concurrency error, increment the retry counter and continue the loop (go back to the Read step). |   
  
The following file provides a runnable example of how to implement the OCC loop using an IAM policy on a Project resource as the target.

**Note:** This example uses the `google-cloud-resourcemanager` library, but the same OCC pattern applies to any service or database that implements versioned updates.

### Installation

To use this example, add the following dependency to your `pom.xml`:
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-resourcemanager</artifactId>
      <version>1.45.0</version>
    </dependency>
    

### Example
    
    
    import com.google.api.gax.rpc.[AbortedException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AbortedException.html);
    import com.google.api.gax.rpc.[FailedPreconditionException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FailedPreconditionException.html);
    import com.google.cloud.resourcemanager.v3.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import java.util.ArrayList;
    import java.util.List;
    
    public class IamOccExample {
    
        /**
         * Executes an Optimistic Concurrency Control (OCC) loop to safely update a resource.
         *
         * This method demonstrates the core Read-Modify-Write-Retry pattern.
         *
         * @param projectId  The Google Cloud Project ID (e.g., "my-project-123").
         * @param role       The IAM role to grant (e.g., "roles/storage.objectAdmin").
         * @param member     The member to add (e.g., "user:user@example.com").
         * @param maxRetries The maximum number of times to retry the update.
         * @return The successfully updated IAM policy (or null on failure).
         */
        public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updateIamPolicyWithOcc(
                String projectId,
                String role,
                String member,
                int maxRetries
        ) throws Exception {
            // Setup Client
            try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
                String projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId).toString();
                int retries = 0;
    
                // START OCC LOOP (Read-Modify-Write-Retry)
                while (retries < maxRetries) {
                    try {
                        // READ: Get the current policy. This includes the current etag.
                        System.out.printf("Attempt %d: Reading current IAM policy for %s...%n", retries, projectName);
                        [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) getIamPolicyRequest = [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder()
                                .setResource(projectName)
                                .build();
                        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = projectsClient.getIamPolicy(getIamPolicyRequest);
    
                        // MODIFY: Apply the desired changes to the local Policy object.
                        List<Binding> bindings = new ArrayList<>(policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)());
                        [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) targetBinding = null;
                        int bindingIndex = -1;
    
                        for (int i = 0; i < bindings.size(); i++) {
                            if (bindings.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InputStreamSupplier.html#com_google_api_gax_rpc_InputStreamSupplier_get__)(i).getRole().equals(role)) {
                                targetBinding = bindings.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InputStreamSupplier.html#com_google_api_gax_rpc_InputStreamSupplier_get__)(i);
                                bindingIndex = i;
                                break;
                            }
                        }
    
                        if (targetBinding != null) {
                            if (targetBinding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)().contains(member)) {
                                System.out.printf("Policy for role %s and member %s exists already!%n", role, member);
                                return policy;
                            }
                            // Create a new binding based on existing one to add the member
                            [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) updatedBinding = targetBinding.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_toBuilder__)()
                                    .[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)(member)
                                    .build();
                            bindings.[set](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchedFuture.html#com_google_api_gax_rpc_BatchedFuture_set_ResponseT_)(bindingIndex, updatedBinding);
                        } else {
                            // Role not found, create a new binding
                            [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) newBinding = [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html).newBuilder()
                                    .setRole(role)
                                    .[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)(member)
                                    .build();
                            bindings.[add](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestParamsBuilder.html#com_google_api_gax_rpc_RequestParamsBuilder_add_java_lang_String_java_lang_String_)(newBinding);
                        }
    
                        // The policy builder now contains the modified bindings AND the original etag.
                        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)()
                                .[clearBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__)()
                                .[addAllBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__)(bindings)
                                .build();
    
                        // WRITE/CHECK: Attempt to write the modified policy.
                        System.out.printf("Attempt %d: Setting modified IAM policy...%n", retries);
                        [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) setIamPolicyRequest = [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                                .setResource(projectName)
                                .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(updatedPolicy)
                                .build();
                        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) resultPolicy = projectsClient.setIamPolicy(setIamPolicyRequest);
    
                        // SUCCESS: If the call succeeds, return the new policy and exit the loop.
                        System.out.printf("Successfully updated IAM policy in attempt %d.%n", retries);
                        return resultPolicy;
    
                    } catch ([AbortedException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AbortedException.html) | [FailedPreconditionException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FailedPreconditionException.html) e) {
                        // If the etag is stale (concurrency conflict), this will throw a retryable exception.
                        retries++;
                        System.out.printf("Concurrency conflict detected (etag mismatch). Retrying... (%d/%d)%n",
                                retries, maxRetries);
    
                        // Exponential backoff (100ms * retry count)
                        Thread.sleep(100L * retries);
                    }
                }
                // END OCC LOOP
            }
    
            System.out.printf("Failed to update IAM policy after %d attempts due to persistent concurrency conflicts.%n", maxRetries);
            return null;
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
