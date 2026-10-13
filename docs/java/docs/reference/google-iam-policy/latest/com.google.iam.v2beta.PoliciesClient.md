---
url: https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesClient
title: Class PoliciesClient (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:24.791674+00:00
---

# Class PoliciesClient (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PoliciesClient (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-iam-policy/google-iam-policy/src/main/java/com/google/iam/v2beta/PoliciesClient.java)| [Product Reference](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/n/a)  
---|---  
  
Service Description: An interface for managing Identity and Access Management (IAM) policies.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       String name = "name3373707";
       Policy response = policiesClient.getPolicy(name);
     }
     

Note: close() needs to be called on the PoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListPolicies |  Retrieves the policies of the specified kind that are attached to a resource.  The response lists only policy metadata. In particular, policy rules are omitted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPolicies(ListPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPoliciesPagedCallable() 
  * listPoliciesCallable() 

  
GetPolicy |  Gets a policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPolicy(GetPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPolicyCallable() 

  
CreatePolicy |  Creates a policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPolicyAsync(CreatePolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPolicyAsync(String parent, Policy policy, String policyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPolicyOperationCallable() 
  * createPolicyCallable() 

  
UpdatePolicy |  Updates the specified policy.  You can update only the rules and the display name for the policy.  To update a policy, you should use a read-modify-write loop:  1\. Use GetPolicy to read the current version of the policy. 2. Modify the policy as needed. 3. Use `UpdatePolicy` to write the updated policy.  This pattern helps prevent conflicts between concurrent updates. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePolicyAsync(UpdatePolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePolicyOperationCallable() 
  * updatePolicyCallable() 

  
DeletePolicy |  Deletes a policy. This action is permanent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePolicyAsync(DeletePolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePolicyOperationCallable() 
  * deletePolicyCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PoliciesSettings policiesSettings =
         PoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PoliciesClient policiesClient = PoliciesClient.create(policiesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PoliciesSettings policiesSettings =
         PoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     PoliciesClient policiesClient = PoliciesClient.create(policiesSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PoliciesSettings policiesSettings = PoliciesSettings.newHttpJsonBuilder().build();
     PoliciesClient policiesClient = PoliciesClient.create(policiesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PoliciesClient

## Static Methods 

### create()
    
    
    public static final PoliciesClient create()

Constructs an instance of PoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PoliciesSettings settings)
    
    
    public static final PoliciesClient create(PoliciesSettings settings)

Constructs an instance of PoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PoliciesStub stub)
    
    
    public static final PoliciesClient create(PoliciesStub stub)

Constructs an instance of PoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(PoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.stub.PoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesClient)` |   
  
## Constructors 

### PoliciesClient(PoliciesSettings settings)
    
    
    protected PoliciesClient(PoliciesSettings settings)

Constructs an instance of PoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesSettings)`  
  
  
### PoliciesClient(PoliciesStub stub)
    
    
    protected PoliciesClient(PoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.stub.PoliciesStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### createPolicyAsync(CreatePolicyRequest request)
    
    
    public final OperationFuture<Policy,PolicyOperationMetadata> createPolicyAsync(CreatePolicyRequest request)

Creates a policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       CreatePolicyRequest request =
           CreatePolicyRequest.newBuilder()
               .setParent("parent-995424086")
               .setPolicy(Policy.newBuilder().build())
               .setPolicyId("policyId546908653")
               .build();
       Policy response = policiesClient.createPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.CreatePolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy),[PolicyOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PolicyOperationMetadata)>` |   
  
### createPolicyAsync(String parent, Policy policy, String policyId)
    
    
    public final OperationFuture<Policy,PolicyOperationMetadata> createPolicyAsync(String parent, Policy policy, String policyId)

Creates a policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       String parent = "parent-995424086";
       Policy policy = Policy.newBuilder().build();
       String policyId = "policyId546908653";
       Policy response = policiesClient.createPolicyAsync(parent, policy, policyId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource that the policy is attached to, along with the kind of policy to create. Format: `policies/{attachment_point}/denypolicies` The attachment point is identified by its URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies`. For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID.  
`policy` | `[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy)`  
Required. The policy to create.  
`policyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for this policy, which will become the final component of the policy's resource name. The ID must contain 3 to 63 characters. It can contain lowercase letters and numbers, as well as dashes (`-`) and periods (`.`). The first character must be a lowercase letter.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy),[PolicyOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PolicyOperationMetadata)>` |   
  
### createPolicyCallable()
    
    
    public final UnaryCallable<CreatePolicyRequest,Operation> createPolicyCallable()

Creates a policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       CreatePolicyRequest request =
           CreatePolicyRequest.newBuilder()
               .setParent("parent-995424086")
               .setPolicy(Policy.newBuilder().build())
               .setPolicyId("policyId546908653")
               .build();
       ApiFuture<Operation> future = policiesClient.createPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.CreatePolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPolicyOperationCallable()
    
    
    public final OperationCallable<CreatePolicyRequest,Policy,PolicyOperationMetadata> createPolicyOperationCallable()

Creates a policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       CreatePolicyRequest request =
           CreatePolicyRequest.newBuilder()
               .setParent("parent-995424086")
               .setPolicy(Policy.newBuilder().build())
               .setPolicyId("policyId546908653")
               .build();
       OperationFuture<Policy, PolicyOperationMetadata> future =
           policiesClient.createPolicyOperationCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.CreatePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy),[PolicyOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PolicyOperationMetadata)>` |   
  
### deletePolicyAsync(DeletePolicyRequest request)
    
    
    public final OperationFuture<Policy,PolicyOperationMetadata> deletePolicyAsync(DeletePolicyRequest request)

Deletes a policy. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       DeletePolicyRequest request =
           DeletePolicyRequest.newBuilder().setName("name3373707").setEtag("etag3123477").build();
       Policy response = policiesClient.deletePolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.DeletePolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy),[PolicyOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PolicyOperationMetadata)>` |   
  
### deletePolicyAsync(String name)
    
    
    public final OperationFuture<Policy,PolicyOperationMetadata> deletePolicyAsync(String name)

Deletes a policy. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       String name = "name3373707";
       Policy response = policiesClient.deletePolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the policy to delete. Format: `policies/{attachment_point}/denypolicies/{policy_id}` Use the URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-policy`. For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy),[PolicyOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PolicyOperationMetadata)>` |   
  
### deletePolicyCallable()
    
    
    public final UnaryCallable<DeletePolicyRequest,Operation> deletePolicyCallable()

Deletes a policy. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       DeletePolicyRequest request =
           DeletePolicyRequest.newBuilder().setName("name3373707").setEtag("etag3123477").build();
       ApiFuture<Operation> future = policiesClient.deletePolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.DeletePolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePolicyOperationCallable()
    
    
    public final OperationCallable<DeletePolicyRequest,Policy,PolicyOperationMetadata> deletePolicyOperationCallable()

Deletes a policy. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       DeletePolicyRequest request =
           DeletePolicyRequest.newBuilder().setName("name3373707").setEtag("etag3123477").build();
       OperationFuture<Policy, PolicyOperationMetadata> future =
           policiesClient.deletePolicyOperationCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.DeletePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy),[PolicyOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PolicyOperationMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getPolicy(GetPolicyRequest request)
    
    
    public final Policy getPolicy(GetPolicyRequest request)

Gets a policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       GetPolicyRequest request = GetPolicyRequest.newBuilder().setName("name3373707").build();
       Policy response = policiesClient.getPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.GetPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy)` |   
  
### getPolicy(String name)
    
    
    public final Policy getPolicy(String name)

Gets a policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       String name = "name3373707";
       Policy response = policiesClient.getPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the policy to retrieve. Format: `policies/{attachment_point}/denypolicies/{policy_id}` Use the URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-policy`. For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy)` |   
  
### getPolicyCallable()
    
    
    public final UnaryCallable<GetPolicyRequest,Policy> getPolicyCallable()

Gets a policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       GetPolicyRequest request = GetPolicyRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Policy> future = policiesClient.getPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.GetPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable PoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.iam.v2beta.PoliciesSettings` |   
  
### getStub()
    
    
    public PoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.stub.PoliciesStub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listPolicies(ListPoliciesRequest request)
    
    
    public final PoliciesClient.ListPoliciesPagedResponse listPolicies(ListPoliciesRequest request)

Retrieves the policies of the specified kind that are attached to a resource.

The response lists only policy metadata. In particular, policy rules are omitted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       ListPoliciesRequest request =
           ListPoliciesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Policy element : policiesClient.listPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.ListPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PoliciesClient.ListPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesClient.ListPoliciesPagedResponse)` |   
  
### listPolicies(String parent)
    
    
    public final PoliciesClient.ListPoliciesPagedResponse listPolicies(String parent)

Retrieves the policies of the specified kind that are attached to a resource.

The response lists only policy metadata. In particular, policy rules are omitted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       String parent = "parent-995424086";
       for (Policy element : policiesClient.listPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource that the policy is attached to, along with the kind of policy to list. Format: `policies/{attachment_point}/denypolicies` The attachment point is identified by its URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies`. For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID.  
**Returns**  
---  
**Type** | **Description**  
`[PoliciesClient.ListPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesClient.ListPoliciesPagedResponse)` |   
  
### listPoliciesCallable()
    
    
    public final UnaryCallable<ListPoliciesRequest,ListPoliciesResponse> listPoliciesCallable()

Retrieves the policies of the specified kind that are attached to a resource.

The response lists only policy metadata. In particular, policy rules are omitted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       ListPoliciesRequest request =
           ListPoliciesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPoliciesResponse response = policiesClient.listPoliciesCallable().call(request);
         for (Policy element : response.getPoliciesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.ListPoliciesRequest),[ListPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.ListPoliciesResponse)>` |   
  
### listPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListPoliciesRequest,PoliciesClient.ListPoliciesPagedResponse> listPoliciesPagedCallable()

Retrieves the policies of the specified kind that are attached to a resource.

The response lists only policy metadata. In particular, policy rules are omitted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       ListPoliciesRequest request =
           ListPoliciesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Policy> future = policiesClient.listPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (Policy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.ListPoliciesRequest),[ListPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PoliciesClient.ListPoliciesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePolicyAsync(UpdatePolicyRequest request)
    
    
    public final OperationFuture<Policy,PolicyOperationMetadata> updatePolicyAsync(UpdatePolicyRequest request)

Updates the specified policy.

You can update only the rules and the display name for the policy.

To update a policy, you should use a read-modify-write loop:

1\. Use GetPolicy to read the current version of the policy. 2. Modify the policy as needed. 3. Use `UpdatePolicy` to write the updated policy.

This pattern helps prevent conflicts between concurrent updates.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       UpdatePolicyRequest request =
           UpdatePolicyRequest.newBuilder().setPolicy(Policy.newBuilder().build()).build();
       Policy response = policiesClient.updatePolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.UpdatePolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy),[PolicyOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PolicyOperationMetadata)>` |   
  
### updatePolicyCallable()
    
    
    public final UnaryCallable<UpdatePolicyRequest,Operation> updatePolicyCallable()

Updates the specified policy.

You can update only the rules and the display name for the policy.

To update a policy, you should use a read-modify-write loop:

1\. Use GetPolicy to read the current version of the policy. 2. Modify the policy as needed. 3. Use `UpdatePolicy` to write the updated policy.

This pattern helps prevent conflicts between concurrent updates.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       UpdatePolicyRequest request =
           UpdatePolicyRequest.newBuilder().setPolicy(Policy.newBuilder().build()).build();
       ApiFuture<Operation> future = policiesClient.updatePolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.UpdatePolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePolicyOperationCallable()
    
    
    public final OperationCallable<UpdatePolicyRequest,Policy,PolicyOperationMetadata> updatePolicyOperationCallable()

Updates the specified policy.

You can update only the rules and the display name for the policy.

To update a policy, you should use a read-modify-write loop:

1\. Use GetPolicy to read the current version of the policy. 2. Modify the policy as needed. 3. Use `UpdatePolicy` to write the updated policy.

This pattern helps prevent conflicts between concurrent updates.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PoliciesClient policiesClient = PoliciesClient.create()) {
       UpdatePolicyRequest request =
           UpdatePolicyRequest.newBuilder().setPolicy(Policy.newBuilder().build()).build();
       OperationFuture<Policy, PolicyOperationMetadata> future =
           policiesClient.updatePolicyOperationCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.UpdatePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.Policy),[PolicyOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2beta.PolicyOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
